#!/usr/bin/env python3
"""Export safe, readable knowledge cards from Learning Inbox evidence records.

The source records retain raw evidence and must remain outside this Git repository.
This exporter emits only source metadata, derived notes, practical applications, and
up to five brief evidence anchors. It skips credential-bearing source links and
redacts token-shaped strings in emitted text.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlsplit

STRUCTURED_EVIDENCE = re.compile(
    r"## Structured evidence\s+```json\s*(.*?)\s*```\s*$", re.DOTALL
)
PASSAGE_REFS = re.compile(r"\s*\[p\d+(?:-p\d+)?(?:,\s*p\d+(?:-p\d+)?)*\]")
TIMESTAMP_EVIDENCE = re.compile(r"^\[([0-9:.]+)\]\s+(.+)$")
TOKEN_PATTERNS = (
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\b(?:sk|rk|pk)_[A-Za-z0-9_-]{16,}\b", re.IGNORECASE),
    re.compile(r"\bAIza[\w-]{20,}\b"),
    re.compile(r"(?i)\b(?:bearer|token)\s+[A-Za-z0-9._~-]{20,}\b"),
)
SENSITIVE_QUERY_KEYS = {
    "access_token", "api_key", "apikey", "api-key", "auth", "authorization",
    "key", "password", "secret", "secret_key", "signature", "token",
    "x-amz-credential", "x-amz-security-token", "x-amz-signature",
}
URL_RE = re.compile(r"https?://[^\s<>\])}]+", re.IGNORECASE)


def is_safe_url(value: object) -> bool:
    if not isinstance(value, str) or not value.startswith(("http://", "https://")):
        return False
    parsed = urlsplit(value)
    if not parsed.netloc or parsed.username or parsed.password:
        return False
    for key, _ in parse_qsl(parsed.query, keep_blank_values=True):
        if key.lower().replace("-", "_") in {x.replace("-", "_") for x in SENSITIVE_QUERY_KEYS}:
            return False
    for key, _ in parse_qsl(parsed.fragment, keep_blank_values=True):
        if key.lower().replace("-", "_") in {x.replace("-", "_") for x in SENSITIVE_QUERY_KEYS}:
            return False
    return True


def scrub_text(value: object) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n")
    for pattern in TOKEN_PATTERNS:
        text = pattern.sub("[redacted]", text)

    def replace_url(match: re.Match[str]) -> str:
        url = match.group(0)
        return url if is_safe_url(url) else "[unsafe URL omitted]"

    return URL_RE.sub(replace_url, text).strip()


def scalar(value: object) -> str:
    return scrub_text(value).replace("\n", " ").strip()


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    return normalized[:72] or "untitled"


def parse_record(path: Path) -> dict[str, Any]:
    match = STRUCTURED_EVIDENCE.search(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"missing structured evidence: {path}")
    return json.loads(match.group(1))


def quoted_bullets(values: object, limit: int | None = None) -> list[str]:
    if not isinstance(values, list):
        return []
    output = []
    for value in values[:limit]:
        cleaned = scrub_text(value)
        if cleaned:
            output.append(f"- {cleaned}")
    return output


def evidence_anchors(values: object, limit: int = 5) -> list[str]:
    if not isinstance(values, list):
        return []
    output = []
    for value in values:
        cleaned = scrub_text(value)
        match = TIMESTAMP_EVIDENCE.match(cleaned)
        if not match:
            continue
        timestamp, quote = match.groups()
        output.append(f"- [{timestamp}] {quote}")
        if len(output) >= limit:
            break
    return output


def render_card(record: dict[str, Any]) -> tuple[str, str, list[str]]:
    metadata_value = record.get("metadata")
    derived_value = record.get("derived")
    source_value = record.get("source")
    metadata: dict[str, Any] = metadata_value if isinstance(metadata_value, dict) else {}
    derived: dict[str, Any] = derived_value if isinstance(derived_value, dict) else {}
    source: dict[str, Any] = source_value if isinstance(source_value, dict) else {}
    title = scalar(metadata.get("title")) or "Untitled source"
    canonical_url = source.get("canonical_url") or metadata.get("url")
    safe_url = canonical_url if is_safe_url(canonical_url) else None
    summary = PASSAGE_REFS.sub("", scrub_text(derived.get("summary")))
    tags = [scalar(tag) for tag in derived.get("tags", []) if scalar(tag)]
    author = scalar(metadata.get("author") or metadata.get("creator"))
    published = scalar(metadata.get("published_at") or metadata.get("createdAt"))
    source_type = scalar(source.get("source_type") or metadata.get("type"))
    applications = quoted_bullets(derived.get("applications"))
    anchors = evidence_anchors(derived.get("key_evidence"))

    lines = [f"# {title}", "", "## Source"]
    if safe_url:
        lines.append(f"- Original: {safe_url}")
    else:
        lines.append("- Original: omitted because the saved URL was unsafe or unavailable")
    if source_type:
        lines.append(f"- Type: {source_type}")
    if author:
        lines.append(f"- Creator: {author}")
    if published:
        lines.append(f"- Published: {published}")
    if tags:
        lines.extend(["", "## Tags", ", ".join(tags)])
    lines.extend(["", "## Derived summary", summary or "No derived summary is available."])
    if applications:
        lines.extend(["", "## Practical applications", *applications])
    if anchors:
        lines.extend(["", "## Evidence anchors", *anchors])
    lines.extend([
        "",
        "## Notes",
        "This card is derived from a private Learning Inbox evidence record. Verify important claims against the original source.",
        "",
    ])
    return title, "\n".join(lines), tags


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-records", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.source_records.is_dir():
        parser.error(f"source records directory does not exist: {args.source_records}")

    output = args.output.resolve()
    cards_dir = output / "cards"
    if cards_dir.exists():
        shutil.rmtree(cards_dir)
    cards_dir.mkdir(parents=True, exist_ok=True)

    cards: list[tuple[str, str, list[str], str]] = []
    skipped: list[str] = []
    for path in sorted(args.source_records.glob("*.md")):
        try:
            record = parse_record(path)
            title, card, tags = render_card(record)
        except (OSError, ValueError, json.JSONDecodeError) as error:
            skipped.append(f"- `{path.name}`: {error}")
            continue
        item_id = scalar(record.get("item_id"))
        filename = f"{slugify(title)}-{item_id[-8:] if item_id else path.stem[-8:]}.md"
        (cards_dir / filename).write_text(card, encoding="utf-8")
        derived_value = record.get("derived")
        derived = derived_value if isinstance(derived_value, dict) else {}
        status = scalar(derived.get("status"))
        cards.append((title, filename, tags, status))

    lines = ["# Learning Inbox Index", "", f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} from {len(cards)} saved records.", ""]
    for title, filename, tags, status in cards:
        details = ", ".join(tags[:6]) if tags else "untagged"
        status_text = f" · {status}" if status else ""
        lines.append(f"- [{title}](cards/{filename}) · {details}{status_text}")
    if skipped:
        lines.extend(["", "## Skipped records", *skipped])
    lines.append("")
    output.mkdir(parents=True, exist_ok=True)
    (output / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Exported {len(cards)} cards to {cards_dir}")
    if skipped:
        print(f"Skipped {len(skipped)} malformed records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
