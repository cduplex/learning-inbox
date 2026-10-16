#!/usr/bin/env python3
"""Validate collection boundaries and Muse card structure in this knowledgebase."""

from __future__ import annotations

import argparse
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
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).parents[1])
    args = parser.parse_args()
    errors = validate_repository(args.root.resolve())
    if errors:
        print("Knowledgebase collection validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Knowledgebase collection validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
