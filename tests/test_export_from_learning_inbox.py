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


if __name__ == "__main__":
    unittest.main()
