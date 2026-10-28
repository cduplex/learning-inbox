import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "export_from_learning_inbox.py"
SPEC = importlib.util.spec_from_file_location("learning_inbox_export", MODULE_PATH)
assert SPEC and SPEC.loader
exporter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = exporter
SPEC.loader.exec_module(exporter)


class ExportSafetyTests(unittest.TestCase):
    def test_card_filename_cannot_escape_cards_directory_from_untrusted_item_id(self):
        filename = exporter.card_filename("Useful title", "../../outside")
        self.assertEqual(filename, "useful-title-outside.md")
        self.assertNotIn("/", filename)
        self.assertNotIn("\\", filename)
        self.assertNotIn("..", filename)


class LearningGuideCardTests(unittest.TestCase):
    def record(self, **derived):
        return {
            "metadata": {"title": "Guide"},
            "source": {"canonical_url": "https://example.com/a", "source_type": "webpage"},
            "derived": {"summary": "Notes.", "applications": ["Suggestion: old."], **derived},
        }

    def test_learning_guide_renders_before_notes_and_replaces_flat_applications(self):
        guide = "**The arc**\nWhy it matters.\n\n**Try this first:** do it."
        _, card, _ = exporter.render_card(self.record(learning_guide=guide))
        self.assertIn("## Learning guide\n**The arc**", card)
        self.assertLess(card.index("## Learning guide"), card.index("## Derived summary"))
        self.assertNotIn("## Practical applications", card)

    def test_legacy_record_keeps_practical_applications(self):
        _, card, _ = exporter.render_card(self.record())
        self.assertIn("## Practical applications\n- Suggestion: old.", card)
        self.assertNotIn("## Learning guide", card)

    def test_learning_guide_is_scrubbed(self):
        guide = "**The arc**\nSee https://x.test/?token=abc123 now.\n**Try this first:** x"
        _, card, _ = exporter.render_card(self.record(learning_guide=guide))
        self.assertNotIn("abc123", card)


if __name__ == "__main__":
    unittest.main()
