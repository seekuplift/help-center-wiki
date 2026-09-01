import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from setup_algolia import (  # noqa: E402
    public_js_body,
    read_existing_search_mode,
)


class SearchModeTests(unittest.TestCase):
    def test_default_when_missing(self):
        self.assertEqual(read_existing_search_mode("window.__ALGOLIA_DOCSEARCH = {};"), "askAi")

    def test_reads_keyword(self):
        text = public_js_body("APP", "search-key", "agent-id", "keyword")
        self.assertEqual(read_existing_search_mode(text), "keyword")
        self.assertIn('"searchMode": "keyword"', text)
        self.assertIn('"assistantId": "agent-id"', text)

    def test_reads_lunr(self):
        text = public_js_body("APP", "search-key", "agent-id", "lunr")
        self.assertEqual(read_existing_search_mode(text), "lunr")

    def test_rejects_unknown_mode(self):
        with self.assertRaises(ValueError):
            public_js_body("APP", "search-key", "agent-id", "off")

    def test_body_is_assignment_of_json(self):
        text = public_js_body("APP", "search-key", "agent-id", "askAi")
        self.assertTrue(text.startswith("/*"))
        self.assertIn("window.__ALGOLIA_DOCSEARCH = {", text)
        self.assertTrue(text.rstrip().endswith("};"))
        self.assertNotIn("ALGOLIA_ADMIN", text)


if __name__ == "__main__":
    unittest.main()
