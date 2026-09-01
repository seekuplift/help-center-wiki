import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from algolia_records import (  # noqa: E402
    block_plain,
    parse_nav_lvl0,
    records_for_page,
    slugify,
    strip_includes_and_chrome,
)


FIXTURE = """# Getting started

--8<-- "includes/test-banner.md"

Intro paragraph with a [link](wallets.md).

## 1. First launch

On a fresh install the app shows a short welcome.

!!! warning "PUBLIC TEST — NOT PRODUCTION"
    This should not be indexed.

## Connect a wallet

You can browse Home without a wallet.
"""


class SlugTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(slugify("1. First launch"), "1-first-launch")

    def test_punctuation(self):
        self.assertEqual(
            slugify("What does Launch cost 0.013 SOL mean?"),
            "what-does-launch-cost-0013-sol-mean",
        )


class StripTests(unittest.TestCase):
    def test_drops_snippet_and_admonition(self):
        cleaned = strip_includes_and_chrome(FIXTURE)
        self.assertNotIn("8<--", cleaned)
        self.assertNotIn("PUBLIC TEST", cleaned)
        self.assertIn("Intro paragraph", cleaned)

    def test_plain_keeps_link_text(self):
        self.assertEqual(
            block_plain("see [Wallets](wallets.md) now"),
            "see Wallets now",
        )


class RecordTests(unittest.TestCase):
    def test_nav_lvl0(self):
        nav = [
            {"Home": "index.md"},
            {
                "Using the app": [
                    {"Getting started": "getting-started.md"},
                    {"Wallets": "wallets.md"},
                ]
            },
        ]
        mapping = parse_nav_lvl0(nav)
        self.assertEqual(mapping["index.md"], "Home")
        self.assertEqual(mapping["getting-started.md"], "Using the app")
        self.assertEqual(mapping["wallets.md"], "Using the app")

    def test_keyword_and_markdown_records(self):
        keyword, markdown = records_for_page(
            markdown=FIXTURE,
            md_name="getting-started.md",
            nav_title="Getting started",
            lvl0="Using the app",
            site_url="https://seekuplift.github.io/help-center-wiki/",
        )
        self.assertTrue(keyword)
        self.assertTrue(markdown)
        types = {r["type"] for r in keyword}
        self.assertIn("content", types)
        self.assertTrue(any(r["hierarchy"]["lvl0"] == "Using the app" for r in keyword))
        self.assertTrue(any(r["hierarchy"]["lvl1"] == "Getting started" for r in keyword))
        urls = {r["url"] for r in keyword}
        self.assertTrue(any("/getting-started/" in u for u in urls))
        self.assertTrue(any(r["url"].endswith("#1-first-launch") for r in keyword))
        texts = " ".join(r["text"] for r in markdown)
        self.assertIn("fresh install", texts)
        self.assertNotIn("PUBLIC TEST", texts)
        self.assertNotIn("8<--", texts)
        self.assertTrue(all(r["lang"] == "en" for r in markdown))


if __name__ == "__main__":
    unittest.main()
