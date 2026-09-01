#!/usr/bin/env python3
"""Push wiki markdown into Algolia keyword + Ask AI indexes.

Requires ALGOLIA_ADMIN_API_KEY or ALGOLIA_WRITE_API_KEY in the environment.
Never prints or writes that key.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from algolia_http import (  # noqa: E402
    KEYWORD_INDEX,
    KEYWORD_SETTINGS,
    MARKDOWN_INDEX,
    MARKDOWN_SETTINGS,
    env_app_id,
    env_write_key,
    replace_all_objects,
    set_index_settings,
)
from algolia_records import build_all  # noqa: E402


def main() -> int:
    app_id = env_app_id()
    write_key = env_write_key()
    keyword, markdown = build_all(ROOT)
    set_index_settings(app_id, write_key, KEYWORD_INDEX, KEYWORD_SETTINGS)
    set_index_settings(app_id, write_key, MARKDOWN_INDEX, MARKDOWN_SETTINGS)
    replace_all_objects(app_id, write_key, KEYWORD_INDEX, keyword)
    replace_all_objects(app_id, write_key, MARKDOWN_INDEX, markdown)
    print(
        f"Indexed {len(keyword)} keyword records into {KEYWORD_INDEX} and "
        f"{len(markdown)} markdown records into {MARKDOWN_INDEX}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
