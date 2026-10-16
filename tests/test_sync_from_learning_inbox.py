import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "sync_from_learning_inbox.py"
SPEC = importlib.util.spec_from_file_location("learning_inbox_sync", MODULE_PATH)
assert SPEC and SPEC.loader
sync = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = sync
SPEC.loader.exec_module(sync)


class SyncSafetyTests(unittest.TestCase):
    def test_only_generated_knowledge_paths_are_publishable(self):
        self.assertTrue(sync.only_generated_paths(["data/INDEX.md", "data/cards/one.md"]))
        self.assertFalse(sync.only_generated_paths(["README.md"]))
        self.assertFalse(sync.only_generated_paths(["data/cards/one.md", "scripts/tool.py"]))
        self.assertFalse(sync.only_generated_paths([]))

    def test_selects_exactly_one_open_automation_pr(self):
        prs = [
            {"number": 8, "headRefName": "docs/manual-edit"},
            {"number": 9, "headRefName": "sync/learning-inbox-20261016T120000Z"},
        ]
        self.assertEqual(
            sync.select_open_sync_pr(prs, "sync/learning-inbox-"),
            {"number": 9, "headRefName": "sync/learning-inbox-20261016T120000Z"},
        )

    def test_rejects_multiple_open_automation_prs(self):
        prs = [
            {"number": 9, "headRefName": "sync/learning-inbox-one"},
            {"number": 10, "headRefName": "sync/learning-inbox-two"},
        ]
        with self.assertRaises(sync.SyncError):
            sync.select_open_sync_pr(prs, "sync/learning-inbox-")

    def test_generated_branch_name_is_remote_safe_and_unique_to_timestamp(self):
        branch = sync.sync_branch_name("sync/learning-inbox-", "2026-10-16T12:34:56Z")
        self.assertEqual(branch, "sync/learning-inbox-20261016T123456Z")


if __name__ == "__main__":
    unittest.main()
