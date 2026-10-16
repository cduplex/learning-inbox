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
        (root / "data" / "muse-instagram" / "reels" / "2026-10-16--test--abc123.md").write_text(
            "# Test\n\n"
            "## Source\n- Original: https://www.instagram.com/reel/abc123/\n- Platform: Instagram Reel\n\n"
            "## Tags\nAI, workflows\n\n"
            "## Core components\n- Example\n\n"
            "## Derived summary\nA supported summary.\n\n"
            "## Practical takeaways\n- Apply carefully.\n\n"
            "## Notes\nDerived from a private Muse record.\n",
            encoding="utf-8",
        )
        self.assertEqual(validator.validate_repository(root), [])

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
