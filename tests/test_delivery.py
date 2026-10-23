import unittest
import json
import os

class TestProjectDelivery(unittest.TestCase):

    def setUp(self):
        self.repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_checklist_parsing(self):
        """Validates delivery checklist parsing from RESULT-TEMPLATE.md."""
        filepath = os.path.join(self.repo_root, 'RESULT-TEMPLATE.md')
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        expected_keys = [
            "- 日期：",
            "- 成果標題：",
            "- 我想幫助的人與問題：",
            "- 本輪可投入的時間：",
            "- 完成條件：",
            "- 我做了什麼：",
            "- 可公開的成果連結：",
            "- 回饋與下一步："
        ]

        for key in expected_keys:
            self.assertIn(key, content, f"Missing expected key '{key}' in RESULT-TEMPLATE.md")

    def test_milestone_tracking(self):
        """Validates milestone tracking phases in SKILL.md."""
        filepath = os.path.join(self.repo_root, 'SKILL.md')
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        expected_milestones = [
            "## 定義本輪成果",
            "## 安排責任與容量",
            "## 執行短迭代",
            "## 交付與回顧"
        ]

        for milestone in expected_milestones:
            self.assertIn(milestone, content, f"Missing expected milestone '{milestone}' in SKILL.md")

    def test_signoff_validations(self):
        """Validates sign-off configurations in skill-book.json and SKILL.md."""
        json_filepath = os.path.join(self.repo_root, 'skill-book.json')
        with open(json_filepath, 'r', encoding='utf-8') as f:
            skill_book = json.load(f)

        # Verify JSON keys
        expected_json_keys = ["format", "id", "title", "version", "guild_key", "entry", "execution", "repository", "license"]
        for key in expected_json_keys:
            self.assertIn(key, skill_book, f"Missing key '{key}' in skill-book.json")

        self.assertEqual(skill_book["id"], "freedom-skill-project-delivery")
        self.assertEqual(skill_book["entry"], "SKILL.md")

        # Verify sign-off section in SKILL.md
        md_filepath = os.path.join(self.repo_root, 'SKILL.md')
        with open(md_filepath, 'r', encoding='utf-8') as f:
            skill_md_content = f.read()

        self.assertIn("## 完成時交付", skill_md_content, "Missing sign-off section '## 完成時交付' in SKILL.md")
        self.assertIn("- 目標與驗收例子", skill_md_content)
        self.assertIn("- 責任與待辦", skill_md_content)
        self.assertIn("- 交付物與回顧", skill_md_content)

if __name__ == '__main__':
    unittest.main()
