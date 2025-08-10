import unittest
from parser import parse_case_details  # example function

class TestParser(unittest.TestCase):
    def test_parse_valid_html(self):
        with open("sample_response.html", "r", encoding="utf-8") as f:
            html = f.read()
        data = parse_case_details(html)
        self.assertIn("petitioner", data)
        self.assertIn("respondent", data)

if __name__ == "__main__":
    unittest.main()
