import unittest
import os
import json
import re

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.md_files = []
        self.json_files = []
        self.all_files = []

        for root, _, files in os.walk(self.repo_root):
            if '.git' in root:
                continue
            for file in files:
                filepath = os.path.join(root, file)
                if file.endswith('.md'):
                    self.md_files.append(filepath)
                    self.all_files.append(filepath)
                elif file.endswith('.json'):
                    self.json_files.append(filepath)
                    self.all_files.append(filepath)
                elif file.endswith('.py') or file.endswith('.yml') or file.endswith('.yaml') or file.endswith('.sh') or file.endswith('.txt'):
                    self.all_files.append(filepath)

    def test_no_hardcoded_secrets(self):
        """Check for hardcoded secrets or credentials in all files."""
        # Simple patterns to catch common exposed secrets
        secret_patterns = [
            r'AKIA[0-9A-Z]{16}', # AWS Access Key
            r'ghp_[a-zA-Z0-9]{36}', # GitHub Personal Access Token
            r'(?i)password\s*[:=]\s*["\'][^"\']+["\']', # password assignment
            r'(?i)api[_-]?key\s*[:=]\s*["\'][^"\']+["\']', # api key assignment
        ]

        for filepath in self.all_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                for pattern in secret_patterns:
                    match = re.search(pattern, content)
                    self.assertIsNone(match, f"Potential secret found in {filepath}: {match}")

    def test_no_script_tags(self):
        """Ensure no <script> tags exist in markdown files (basic sanitization check)."""
        for filepath in self.md_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertNotIn('<script>', content.lower(), f"Script tag found in {filepath}")

    def test_secure_urls_in_json(self):
        """Ensure all URLs in JSON files are HTTPS."""
        for filepath in self.json_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

                def check_urls(obj):
                    if isinstance(obj, dict):
                        for k, v in obj.items():
                            check_urls(v)
                    elif isinstance(obj, list):
                        for item in obj:
                            check_urls(item)
                    elif isinstance(obj, str):
                        if obj.startswith('http://') and "localhost" not in obj:
                            self.fail(f"Insecure HTTP URL found in {filepath}: {obj}")

                check_urls(data)

if __name__ == '__main__':
    unittest.main()
