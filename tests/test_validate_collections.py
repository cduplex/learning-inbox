import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "validate_collections.py"
SPEC = importlib.util.spec_from_file_location("knowledgebase_validator", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class CollectionContractTests(unittest.TestCase):
    def make_root(self) -> Path:
        root = Path(tempfile.mkdtemp())
        (root / "data" / "learning-inbox" / "cards").mkdir(parents=True)
        (root / "data" / "muse-instagram" / "reels").mkdir(parents=True)
        (root / "data" / "INDEX.md").write_text(
            "# Knowledgebase Index\n\n"
            "- [Learning Inbox](learning-inbox/INDEX.md)\n"
            "- [Muse Instagram Reels](muse-instagram/INDEX.md)\n",
            encoding="utf-8",
        )
        (root / "data" / "learning-inbox" / "INDEX.md").write_text(
            "# Learning Inbox Index\n", encoding="utf-8"
        )
        (root / "data" / "muse-instagram" / "INDEX.md").write_text(
            "# Muse Instagram Reels Index\n", encoding="utf-8"
        )
        return root

    def test_accepts_empty_muse_collection_with_required_indexes(self):
        self.assertEqual(validator.validate_repository(self.make_root()), [])

    def test_rejects_legacy_shared_cards_directory(self):
        root = self.make_root()
        (root / "data" / "cards").mkdir()
        self.assertIn("legacy_shared_cards_directory", validator.validate_repository(root))

    def test_rejects_muse_card_missing_required_sections(self):
        root = self.make_root()
        (root / "data" / "muse-instagram" / "reels" / "2026-10-16--test--abc123.md").write_text(
            "# Test\n\n## Source\n- Original: https://www.instagram.com/reel/abc123/\n",
            encoding="utf-8",
        )
        errors = validator.validate_repository(root)
        self.assertIn("muse_card_missing_required_sections:2026-10-16--test--abc123.md", errors)

    def test_accepts_muse_card_with_safe_source_and_contract_sections(self):
        root = self.make_root()
        (root / "data" / "muse-instagram" / "reels" / "2026-10-16--test--bd0c1402e605.md").write_text(
            "# Test\n\n"
            "## Source\n- Original: https://www.instagram.com/reel/abc123/\n- Platform: Instagram Reel\n\n"
            "## Tags\nAI, workflows\n\n"
            "## Core components\n- Example\n\n"
            "## Derived summary\nA supported summary.\n\n"
            "## Practical takeaways\n- Apply carefully.\n\n"
            "## Notes\nDerived from a private Muse record.\n",
            encoding="utf-8",
        )
        (root / "data" / "muse-instagram" / "INDEX.md").write_text(
            "# Muse Instagram Reels Index\n\n"
            "- [Test](reels/2026-10-16--test--bd0c1402e605.md) · AI · Instagram Reel · saved\n",
            encoding="utf-8",
        )
        self.assertEqual(validator.validate_repository(root), [])

    def test_rejects_muse_card_with_source_id_not_derived_from_canonical_url(self):
        root = self.make_root()
        filename = "2026-10-16--test--aaaaaaaaaaaa.md"
        (root / "data" / "muse-instagram" / "reels" / filename).write_text(
            "# Test\n\n"
            "## Source\n- Original: https://www.instagram.com/reel/abc123/\n- Platform: Instagram Reel\n\n"
            "## Tags\nAI\n\n## Core components\n- Example\n\n"
            "## Derived summary\nA summary.\n\n## Practical takeaways\n- Apply carefully.\n\n"
            "## Notes\nDerived from a private Muse record.\n",
            encoding="utf-8",
        )
        (root / "data" / "muse-instagram" / "INDEX.md").write_text(
            f"# Muse Instagram Reels Index\n\n- [Test](reels/{filename}) · AI · Instagram Reel · saved\n",
            encoding="utf-8",
        )
        self.assertIn(
            f"muse_card_source_id_mismatch:{filename}",
            validator.validate_repository(root),
        )

    def test_rejects_duplicate_muse_source_id_across_cards(self):
        root = self.make_root()
        source = "https://www.instagram.com/reel/abc123/"
        first = "2026-10-16--first--bd0c1402e605.md"
        second = "2026-10-17--second--bd0c1402e605.md"
        content = (
            "# Test\n\n"
            f"## Source\n- Original: {source}\n- Platform: Instagram Reel\n\n"
            "## Tags\nAI\n\n## Core components\n- Example\n\n"
            "## Derived summary\nA summary.\n\n## Practical takeaways\n- Apply carefully.\n\n"
            "## Notes\nDerived from a private Muse record.\n"
        )
        reels = root / "data" / "muse-instagram" / "reels"
        (reels / first).write_text(content, encoding="utf-8")
        (reels / second).write_text(content, encoding="utf-8")
        self.assertIn(
            "duplicate_muse_source_id:bd0c1402e605",
            validator.validate_repository(root),
        )

    def test_rejects_muse_card_missing_from_collection_index(self):
        root = self.make_root()
        (root / "data" / "muse-instagram" / "reels" / "2026-10-16--test--abc123.md").write_text(
            "# Test\n\n"
            "## Source\n- Original: https://www.instagram.com/reel/abc123/\n- Platform: Instagram Reel\n\n"
            "## Tags\nAI\n\n## Core components\n- Example\n\n"
            "## Derived summary\nA summary.\n\n## Practical takeaways\n- Apply carefully.\n\n"
            "## Notes\nDerived from a private Muse record.\n",
            encoding="utf-8",
        )
        self.assertIn(
            "muse_card_missing_from_index:2026-10-16--test--abc123.md",
            validator.validate_repository(root),
        )

    def test_rejects_muse_card_with_non_deterministic_filename(self):
        root = self.make_root()
        (root / "data" / "muse-instagram" / "reels" / "notes.md").write_text(
            "# Test\n\n"
            "## Source\n- Original: https://www.instagram.com/reel/abc123/\n- Platform: Instagram Reel\n\n"
            "## Tags\nAI\n\n## Core components\n- Example\n\n"
            "## Derived summary\nA summary.\n\n## Practical takeaways\n- Apply carefully.\n\n"
            "## Notes\nDerived from a private Muse record.\n",
            encoding="utf-8",
        )
        self.assertIn("muse_card_invalid_filename:notes.md", validator.validate_repository(root))

    def test_learning_inbox_card_character_limit(self):
        for size in (10_000, 10_001, 25_000, 100_000, 100_001):
            with self.subTest(size=size):
                root = self.make_root()
                relative = "data/learning-inbox/cards/detailed.md"
                (root / relative).write_text("x" * size, encoding="utf-8")
                expected = [f"oversized_card:{relative}"] if size > 100_000 else []
                self.assertEqual(validator.validate_repository(root), expected)

    def test_muse_card_character_limit_remains_10000(self):
        for size in (10_000, 10_001):
            with self.subTest(size=size):
                root = self.make_root()
                filename = "2026-10-16--test--bd0c1402e605.md"
                relative = f"data/muse-instagram/reels/{filename}"
                content = (
                    "# Test\n\n"
                    "## Source\n- Original: https://www.instagram.com/reel/abc123/\n\n"
                    "## Tags\nAI\n\n## Core components\n- Example\n\n"
                    "## Derived summary\nA summary.\n\n"
                    "## Practical takeaways\n- Apply carefully.\n\n## Notes\n"
                )
                (root / relative).write_text(
                    content + "x" * (size - len(content)), encoding="utf-8"
                )
                (root / "data/muse-instagram/INDEX.md").write_text(
                    f"# Muse Instagram Reels Index\n\n- [Test](reels/{filename})\n",
                    encoding="utf-8",
                )
                expected = [f"oversized_card:{relative}"] if size > 10_000 else []
                self.assertEqual(validator.validate_repository(root), expected)

    def test_detailed_learning_inbox_cards_still_reject_unsafe_content(self):
        cases = (
            ("https://token@example.com/private", "unsafe_content_url"),
            ("https://example.com/?access_token=private", "unsafe_content_url"),
            ("ghp_" + "a" * 30, "token_shaped_content"),
        )
        for content, error in cases:
            with self.subTest(error=error, content=content):
                root = self.make_root()
                relative = "data/learning-inbox/cards/detailed.md"
                (root / relative).write_text(
                    "# Detailed study notes\n" + "x" * 25_000 + "\n" + content,
                    encoding="utf-8",
                )
                self.assertEqual(
                    validator.validate_repository(root), [f"{error}:{relative}"]
                )

    def test_rejects_unsafe_url_inside_learning_inbox_card_body(self):
        root = self.make_root()
        (root / "data" / "learning-inbox" / "cards" / "bad.md").write_text(
            "# Card\n\n## Derived summary\nSee https://token@example.com/private\n",
            encoding="utf-8",
        )
        self.assertIn(
            "unsafe_content_url:data/learning-inbox/cards/bad.md",
            validator.validate_repository(root),
        )

    def test_rejects_nested_muse_reel_markdown(self):
        root = self.make_root()
        nested = root / "data" / "muse-instagram" / "reels" / "nested"
        nested.mkdir()
        (nested / "raw.md").write_text("unvalidated", encoding="utf-8")
        self.assertIn(
            "unexpected_collection_file:data/muse-instagram/reels/nested/raw.md",
            validator.validate_repository(root),
        )

    def test_rejects_non_card_files_inside_owned_collections(self):
        root = self.make_root()
        (root / "data" / "learning-inbox" / "runtime.sqlite").write_text("not allowed", encoding="utf-8")
        (root / "data" / "muse-instagram" / "private-session-cookie.txt").write_text("not allowed", encoding="utf-8")
        errors = validator.validate_repository(root)
        self.assertIn("unexpected_collection_file:data/learning-inbox/runtime.sqlite", errors)
        self.assertIn("unexpected_collection_file:data/muse-instagram/private-session-cookie.txt", errors)

    def test_rejects_muse_card_with_non_instagram_source_url(self):
        root = self.make_root()
        (root / "data" / "muse-instagram" / "reels" / "2026-10-16--test--abc123.md").write_text(
            "# Test\n\n## Source\n- Original: https://example.com/reel/abc123/\n\n"
            "## Tags\nAI\n\n## Core components\n- Example\n\n"
            "## Derived summary\nA summary.\n\n## Practical takeaways\n- Apply carefully.\n\n"
            "## Notes\nDerived from a private Muse record.\n",
            encoding="utf-8",
        )
        self.assertIn(
            "muse_card_non_instagram_source_url:2026-10-16--test--abc123.md",
            validator.validate_repository(root),
        )


    def test_rejects_muse_card_with_unsafe_source_url(self):
        root = self.make_root()
        (root / "data" / "muse-instagram" / "reels" / "2026-10-16--test--abc123.md").write_text(
            "# Test\n\n"
            "## Source\n- Original: https://token@example.com/reel/abc123/\n\n"
            "## Tags\nAI\n\n## Core components\n- Example\n\n"
            "## Derived summary\nA summary.\n\n## Practical takeaways\n- Apply carefully.\n\n"
            "## Notes\nDerived from a private Muse record.\n",
            encoding="utf-8",
        )
        self.assertIn("muse_card_unsafe_source_url:2026-10-16--test--abc123.md", validator.validate_repository(root))


if __name__ == "__main__":
    unittest.main()
