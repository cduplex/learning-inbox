#!/usr/bin/env python3
"""Safely publish the generated Learning Inbox knowledge layer through a PR.

This program must run from a dedicated disposable Git worktree, never from the
human-maintained knowledgebase checkout. It reads raw evidence only to invoke the
repository's exporter. The raw archive, SQLite databases, credentials and runtime
state are never staged or sent to GitHub.
"""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import subprocess
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Sequence


class SyncError(RuntimeError):
    """A deliberately non-sensitive synchronization failure."""


@dataclass(frozen=True)
class GitHubIdentity:
    login: str
    noreply_email: str


@dataclass(frozen=True)
class SyncConfig:
    repo: str
    source_records: Path
    worktree: Path
    github_bin: str
    branch_prefix: str = "sync/learning-inbox-"


def only_generated_paths(paths: Sequence[str]) -> bool:
    """Allow commits only to generated knowledge data, never repository tooling."""
    return bool(paths) and all(
        path == "data/learning-inbox/INDEX.md"
        or path.startswith("data/learning-inbox/cards/")
        for path in paths
    )


def as_mapping(value: object) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def select_open_sync_pr(prs: Sequence[dict], branch_prefix: str) -> dict | None:
    """Return the one resumable automation PR, rejecting ambiguous recovery."""
    matching = []
    for pr in prs:
        head = as_mapping(pr.get("head"))
        branch = pr.get("headRefName") or head.get("ref")
        if isinstance(branch, str) and branch.startswith(branch_prefix):
            matching.append(pr)
    if len(matching) > 1:
        raise SyncError("multiple_open_sync_prs")
    return matching[0] if matching else None


def sync_branch_name(branch_prefix: str, timestamp: str) -> str:
    return branch_prefix + timestamp.replace("-", "").replace(":", "")


def _run(command: Sequence[str], *, cwd: Path | None = None) -> str:
    """Run a command without exposing provider or GitHub diagnostic payloads."""
    try:
        result = subprocess.run(
            list(command),
            cwd=cwd,
            check=False,
            text=True,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
        )
    except OSError as error:
        raise SyncError("command_unavailable") from error
    if result.returncode:
        raise SyncError("command_failed")
    return result.stdout


def _json(command: Sequence[str], *, cwd: Path | None = None) -> dict | list:
    try:
        return json.loads(_run(command, cwd=cwd))
    except json.JSONDecodeError as error:
        raise SyncError("invalid_command_response") from error


def _git(worktree: Path, *args: str) -> str:
    return _run(["git", *args], cwd=worktree)


def _gh(config: SyncConfig, *args: str) -> str:
    return _run([config.github_bin, *args])


def _gh_json(config: SyncConfig, *args: str) -> dict | list:
    return _json([config.github_bin, *args])


def _expected_remote(config: SyncConfig) -> set[str]:
    return {f"https://github.com/{config.repo}.git", f"git@github.com:{config.repo}.git"}


def ensure_worktree(config: SyncConfig) -> None:
    """Create or verify an isolated checkout which is safe to reset on each pass."""
    if not config.source_records.is_dir():
        raise SyncError("source_records_missing")
    if config.worktree.exists():
        if not (config.worktree / ".git").exists():
            raise SyncError("worktree_is_not_a_git_checkout")
        remote = _git(config.worktree, "remote", "get-url", "origin").strip()
        if remote not in _expected_remote(config):
            raise SyncError("worktree_remote_mismatch")
        return
    config.worktree.parent.mkdir(parents=True, exist_ok=True)
    _run(["git", "clone", f"https://github.com/{config.repo}.git", str(config.worktree)])


def configure_commit_identity(config: SyncConfig) -> GitHubIdentity:
    account = _gh_json(config, "api", "user")
    if not isinstance(account, dict) or not isinstance(account.get("id"), int) or not isinstance(account.get("login"), str):
        raise SyncError("github_identity_unavailable")
    identity = GitHubIdentity(
        login=account["login"],
        noreply_email=f"{account['id']}+{account['login']}@users.noreply.github.com",
    )
    _git(config.worktree, "config", "user.name", "Learning Inbox Sync")
    _git(config.worktree, "config", "user.email", identity.noreply_email)
    return identity


def refresh_main(config: SyncConfig) -> None:
    _git(config.worktree, "fetch", "--prune", "origin")
    _git(config.worktree, "checkout", "--force", "main")
    _git(config.worktree, "reset", "--hard", "origin/main")
    if _git(config.worktree, "status", "--porcelain").strip():
        raise SyncError("worktree_not_clean")


def list_open_prs(config: SyncConfig) -> list[dict]:
    """Read every open PR so a stale automation branch cannot be skipped by page size."""
    result: list[dict] = []
    for page in range(1, 101):
        response = _gh_json(
            config,
            "api",
            f"repos/{config.repo}/pulls?state=open&per_page=100&page={page}",
        )
        if not isinstance(response, list):
            raise SyncError("invalid_pr_list")
        if not response:
            return result
        result.extend(pr for pr in response if isinstance(pr, dict))
        if len(response) < 100:
            return result
    raise SyncError("open_pr_pagination_limit")


def open_sync_pr(config: SyncConfig) -> dict | None:
    return select_open_sync_pr(list_open_prs(config), config.branch_prefix)


def list_pr_files(config: SyncConfig, number: int) -> list[dict]:
    """Read every changed file before granting the automation merge capability."""
    result: list[dict] = []
    for page in range(1, 101):
        response = _gh_json(
            config,
            "api",
            f"repos/{config.repo}/pulls/{number}/files?per_page=100&page={page}",
        )
        if not isinstance(response, list):
            raise SyncError("invalid_pr_file_list")
        if not response:
            return result
        result.extend(file for file in response if isinstance(file, dict))
        if len(response) < 100:
            return result
    raise SyncError("pull_request_file_pagination_limit")


def validate_pr_payload(
    pr: dict,
    files: Sequence[dict],
    repo: str,
    expected_login: str,
    expected_branch: str,
) -> str:
    """Fail closed unless the exact trusted data-only PR is still mergeable."""
    base = as_mapping(pr.get("base"))
    head = as_mapping(pr.get("head"))
    author = as_mapping(pr.get("user"))
    head_repo = as_mapping(head.get("repo"))
    head_owner = as_mapping(head.get("user"))
    sha = head.get("sha")
    if (
        pr.get("state") != "open"
        or base.get("ref") != "main"
        or head.get("ref") != expected_branch
        or head_repo.get("full_name") != repo
        or head_owner.get("login") != expected_login
        or author.get("login") != expected_login
        or not isinstance(sha, str)
        or len(sha) != 40
        or any(character not in "0123456789abcdef" for character in sha.lower())
    ):
        raise SyncError("untrusted_pull_request")
    for file in files:
        filename = file.get("filename") if isinstance(file, dict) else None
        previous = file.get("previous_filename") if isinstance(file, dict) else None
        if not isinstance(filename, str) or not only_generated_paths([filename]):
            raise SyncError("untrusted_pull_request_path")
        if previous is not None and (not isinstance(previous, str) or not only_generated_paths([previous])):
            raise SyncError("untrusted_pull_request_path")
    if not files:
        raise SyncError("empty_pull_request")
    return sha


def validate_pull_request(
    config: SyncConfig,
    number: int,
    identity: GitHubIdentity,
    expected_branch: str,
) -> str:
    pr = _gh_json(config, "api", f"repos/{config.repo}/pulls/{number}")
    if not isinstance(pr, dict):
        raise SyncError("invalid_pull_request")
    return validate_pr_payload(pr, list_pr_files(config, number), config.repo, identity.login, expected_branch)


def merge_pr(config: SyncConfig, number: int, branch: str, identity: GitHubIdentity) -> bool:
    sha = validate_pull_request(config, number, identity, branch)
    response = _gh_json(
        config,
        "api",
        "--method",
        "PUT",
        f"repos/{config.repo}/pulls/{number}/merge",
        "-f",
        "merge_method=squash",
        "-f",
        f"commit_title=chore(data): sync Learning Inbox (#{number})",
        "-f",
        f"sha={sha}",
    )
    if not isinstance(response, dict) or response.get("merged") is not True:
        raise SyncError("pull_request_not_merged")
    readback = _gh_json(config, "api", f"repos/{config.repo}/pulls/{number}")
    if not isinstance(readback, dict) or readback.get("merged_at") is None:
        raise SyncError("pull_request_merge_readback_failed")
    _git(config.worktree, "push", "origin", "--delete", branch)
    return True


def changed_paths(worktree: Path) -> list[str]:
    """Return filenames from standard porcelain output, rejecting odd rename records."""
    output = _git(worktree, "status", "--porcelain=v1", "--untracked-files=all")
    paths: list[str] = []
    for line in output.splitlines():
        if len(line) < 4 or line[2] != " ":
            raise SyncError("unexpected_git_status")
        path = line[3:]
        if " -> " in path:
            raise SyncError("unexpected_git_rename")
        paths.append(path)
    return paths


def create_and_merge_sync_pr(config: SyncConfig, identity: GitHubIdentity) -> tuple[int, int] | None:
    exporter = config.worktree / "scripts" / "export_from_learning_inbox.py"
    if not exporter.is_file():
        raise SyncError("exporter_missing")
    _run(
        [
            sys.executable,
            str(exporter),
            "--source-records",
            str(config.source_records),
            "--output",
            str(config.worktree / "data" / "learning-inbox"),
        ],
        cwd=config.worktree,
    )
    paths = changed_paths(config.worktree)
    if not paths:
        return None
    if not only_generated_paths(paths):
        raise SyncError("unexpected_publish_path")
    _git(config.worktree, "add", "--", "data")
    _git(config.worktree, "diff", "--cached", "--check")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    branch = sync_branch_name(config.branch_prefix, timestamp)
    _git(config.worktree, "checkout", "-b", branch)
    _git(config.worktree, "commit", "-m", f"chore(data): sync Learning Inbox {timestamp}")
    _git(config.worktree, "push", "--set-upstream", "origin", branch)
    _gh(
        config,
        "pr",
        "create",
        "--repo",
        config.repo,
        "--base",
        "main",
        "--head",
        branch,
        "--title",
        "chore(data): sync Learning Inbox",
        "--body",
        "Automated export of saved Learning Inbox evidence and derived summaries into the Learning Inbox collection. Raw evidence, database files, delivery state, and credentials are excluded.",
    )
    pr = _gh_json(config, "pr", "view", branch, "--repo", config.repo, "--json", "number")
    if not isinstance(pr, dict) or not isinstance(pr.get("number"), int):
        raise SyncError("pull_request_create_readback_failed")
    if not merge_pr(config, pr["number"], branch, identity):
        return None
    return pr["number"], len(paths)


@contextmanager
def sync_lock(worktree: Path) -> Iterator[None]:
    lock_path = worktree.parent / f".{worktree.name}.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("w", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        yield


def synchronize(config: SyncConfig) -> str | None:
    """Resume a prior PR if needed, then publish and merge one fresh data update."""
    with sync_lock(config.worktree):
        ensure_worktree(config)
        identity = configure_commit_identity(config)
        pending = open_sync_pr(config)
        if pending is not None:
            number = pending.get("number")
            branch = pending.get("head", {}).get("ref") if isinstance(pending.get("head"), dict) else None
            if not isinstance(number, int) or not isinstance(branch, str):
                raise SyncError("invalid_pending_pull_request")
            if not merge_pr(config, number, branch, identity):
                return None
            refresh_main(config)
            return None
        refresh_main(config)
        created = create_and_merge_sync_pr(config, identity)
    if created is None:
        return None
    number, files = created
    return f"Learning Inbox knowledgebase synced and merged: PR #{number}; {files} generated data file(s)."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="cduplex/learning-inbox")
    parser.add_argument("--source-records", type=Path, required=True)
    parser.add_argument("--worktree", type=Path, required=True)
    parser.add_argument("--github-bin", default="gh")
    args = parser.parse_args()
    config = SyncConfig(
        repo=args.repo,
        source_records=args.source_records.resolve(),
        worktree=args.worktree.resolve(),
        github_bin=args.github_bin,
    )
    try:
        message = synchronize(config)
    except SyncError as error:
        print(f"Learning Inbox knowledgebase sync failed: {error}.")
        return 1
    if message:
        print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
