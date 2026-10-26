import unittest
import time
import json
import os

class TestPerformance(unittest.TestCase):
    def test_latency_result_template(self):
        # We benchmark reading and simulating template generation since there is no background logic.
        # AGENTS.md mentions "目前是文件技能書，沒有背景服務、會員登入或自動平台同步。"
        # However, a user or AI might process this programmatically.
        start_time = time.time()
        with open("RESULT-TEMPLATE.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Simulate simple parsing / replacement
        content = content.replace("日期：", "日期：2023-10-27")
        end_time = time.time()

        latency = (end_time - start_time) * 1000  # in ms
        self.assertLess(latency, 50, "Latency for reading RESULT-TEMPLATE.md exceeded 50ms")

    def test_latency_skill_md(self):
        start_time = time.time()
        with open("SKILL.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Simulate extracting a checklist
        checklist = [line for line in content.split("\n") if line.strip().startswith("- ")]
        end_time = time.time()

        latency = (end_time - start_time) * 1000
        self.assertLess(latency, 50, "Latency for processing SKILL.md exceeded 50ms")

    def test_latency_skill_book_json(self):
        start_time = time.time()
        with open("skill-book.json", "r", encoding="utf-8") as f:
            content = json.load(f)
        end_time = time.time()

        latency = (end_time - start_time) * 1000
        self.assertLess(latency, 50, "Latency for parsing skill-book.json exceeded 50ms")

if __name__ == "__main__":
    unittest.main()
