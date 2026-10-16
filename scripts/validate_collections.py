#!/usr/bin/env python3
"""Validate collection boundaries and Muse card structure in this knowledgebase."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit


REQUIRED_MUSE_SECTIONS = (
    "## Source",
    "## Tags",
    "## Core components",
    "## Derived summary",
    "## Practical takeaways",
    "## Notes",
)
SENSITIVE_URL_KEYS = {
    "access_token", "api_key", "apikey", "api-key", "auth", "authorization",
    "key", "password", "secret", "secret_key", "signature", "token",
    "x-amz-credential", "x-amz-security-token", "x-amz-signature",
}
MUSE_CARD_FILENAME = re.compile(
    r"^\d{4}-\d{2}-\d{2}--[a-z0-9]+(?:-[a-z0-9]+)*--[a-z0-9][a-z0-9_-]*\.md$"
)
URL_RE = re.compile(r"https?://[^\s<>\])}]+", re.IGNORECASE)
TOKEN_PATTERNS = (
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\b(?:sk|rk|pk)_[A-Za-z0-9_-]{16,}\b", re.IGNORECASE),
    re.compile(r"\bAIza[\w-]{20,}\b"),
    re.compile(r"(?i)\b(?:bearer|token)\s+[A-Za-z0-9._~-]{20,}\b"),
)


def safe_url(value: str) -> bool:
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return False
    if parsed.username is not None or parsed.password is not None:
        return False
    for key, _ in parse_qsl(parsed.query, keep_blank_values=True):
        if key.lower().replace("-", "_") in {item.replace("-", "_") for item in SENSITIVE_URL_KEYS}:
            return False
    for key, _ in parse_qsl(parsed.fragment, keep_blank_values=True):
        if key.lower().replace("-", "_") in {item.replace("-", "_") for item in SENSITIVE_URL_KEYS}:
            return False
    return True


def canonical_muse_reel_url(value: str) -> str | None:
    """Normalize an Instagram Reel URL so its source-derived ID is reproducible."""
    parsed = urlsplit(value)
    host = (parsed.hostname or "").lower()
    parts = [part for part in parsed.path.split("/") if part]
    if host not in {"instagram.com", "www.instagram.com"} or len(parts) != 2:
        return None
    if parts[0] not in {"reel", "reels"} or not re.fullmatch(r"[A-Za-z0-9_-]+", parts[1]):
        return None
    return f"https://www.instagram.com/reel/{parts[1]}/"


def muse_source_id(canonical_url: str) -> str:
    return hashlib.sha256(canonical_url.encode("utf-8")).hexdigest()[:12]


def allowed_collection_file(relative: str) -> bool:
    return (
        relative == "data/learning-inbox/INDEX.md"
        or (
            relative.startswith("data/learning-inbox/cards/")
            and relative.endswith(".md")
            and relative.count("/") == 3
        )
        or relative == "data/muse-instagram/INDEX.md"
        or relative == "data/muse-instagram/reels/.gitkeep"
        or (
            relative.startswith("data/muse-instagram/reels/")
            and relative.endswith(".md")
            and relative.count("/") == 3
        )
    )


def validate_changed_paths(paths: list[str], branch: str) -> list[str]:
    if branch.startswith("sync/learning-inbox-"):
        allowed = lambda path: path == "data/learning-inbox/INDEX.md" or (
            path.startswith("data/learning-inbox/cards/") and path.endswith(".md")
        )
    elif branch.startswith("sync/muse-instagram-"):
        allowed = lambda path: path == "data/muse-instagram/INDEX.md" or (
            path.startswith("data/muse-instagram/reels/") and path.endswith(".md")
        )
    else:
        return []
    return [f"publisher_changed_path_not_allowed:{path}" for path in paths if not allowed(path)]


def unsafe_content_errors(relative: str, text: str) -> list[str]:
    errors: list[str] = []
    if any(not safe_url(match.group(0)) for match in URL_RE.finditer(text)):
        errors.append(f"unsafe_content_url:{relative}")
    if any(pattern.search(text) for pattern in TOKEN_PATTERNS):
        errors.append(f"token_shaped_content:{relative}")
    return errors


def source_url(card: str) -> str | None:
    in_source = False
    for line in card.splitlines():
        if line == "## Source":
            in_source = True
            continue
        if in_source and line.startswith("## "):
            return None
        if in_source and line.startswith("- Original: "):
            return line.removeprefix("- Original: ").strip()
    return None


def validate_repository(root: Path) -> list[str]:
    data = root / "data"
    errors: list[str] = []
    expected_indexes = (
        data / "INDEX.md",
        data / "learning-inbox" / "INDEX.md",
        data / "muse-instagram" / "INDEX.md",
    )
    for index in expected_indexes:
        if not index.is_file():
            errors.append(f"missing_index:{index.relative_to(root)}")
    for collection in (data / "learning-inbox", data / "muse-instagram"):
        if collection.is_dir():
            for item in collection.rglob("*"):
                if item.is_file() and not allowed_collection_file(item.relative_to(root).as_posix()):
                    errors.append(f"unexpected_collection_file:{item.relative_to(root).as_posix()}")
    for markdown in data.rglob("*.md"):
        relative = markdown.relative_to(root).as_posix()
        if relative == "data/INDEX.md" or allowed_collection_file(relative):
            errors.extend(unsafe_content_errors(relative, markdown.read_text(encoding="utf-8")))
    if (data / "cards").exists():
        errors.append("legacy_shared_cards_directory")

    muse_index = data / "muse-instagram" / "INDEX.md"
    muse_index_text = muse_index.read_text(encoding="utf-8") if muse_index.is_file() else ""
    reels = data / "muse-instagram" / "reels"
    if not reels.is_dir():
        errors.append("missing_muse_reels_directory")
        return errors
    for card_path in sorted(reels.glob("*.md")):
        if not MUSE_CARD_FILENAME.fullmatch(card_path.name):
            errors.append(f"muse_card_invalid_filename:{card_path.name}")
            continue
        if f"reels/{card_path.name}" not in muse_index_text:
            errors.append(f"muse_card_missing_from_index:{card_path.name}")
        card = card_path.read_text(encoding="utf-8")
        if not card.startswith("# ") or any(section not in card for section in REQUIRED_MUSE_SECTIONS):
            errors.append(f"muse_card_missing_required_sections:{card_path.name}")
            continue
        original = source_url(card)
        if original is None or not safe_url(original):
            errors.append(f"muse_card_unsafe_source_url:{card_path.name}")
            continue
        canonical = canonical_muse_reel_url(original)
        if canonical is None:
            errors.append(f"muse_card_non_instagram_source_url:{card_path.name}")
            continue
        source_id = card_path.stem.rsplit("--", 1)[-1]
        if source_id != muse_source_id(canonical):
            errors.append(f"muse_card_source_id_mismatch:{card_path.name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).parents[1])
    parser.add_argument("--branch", default="")
    parser.add_argument("--changed-paths-file", type=Path)
    args = parser.parse_args()
    errors = validate_repository(args.root.resolve())
    if args.changed_paths_file is not None:
        paths = [line.strip() for line in args.changed_paths_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        errors.extend(validate_changed_paths(paths, args.branch))
    if errors:
        print("Knowledgebase collection validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Knowledgebase collection validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
