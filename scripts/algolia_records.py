"""Build Algolia records from the wiki markdown source.

Produces:
  - DocSearch v3 keyword records for `help_center`
  - Markdown chunks for `help_center_markdown` (Ask AI / Agent Studio)
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

SNIPPET_RE = re.compile(r"^--8<--[^\n]*\n?", re.M)
ADMONITION_RE = re.compile(
    r"^!!![^\n]*\n(?:[ \t]+.*\n|\s*\n)*",
    re.M,
)
DETAILS_RE = re.compile(
    r"^\?{3}[^\n]*\n(?:[ \t]+.*\n|\s*\n)*",
    re.M,
)
TAB_OPEN_RE = re.compile(r'^===\s+"[^"]+"\s*$', re.M)
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`([^`]+)`")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
EMPHASIS_RE = re.compile(r"[*_]{1,3}([^*_]+)[*_]{1,3}")
HTML_RE = re.compile(r"<[^>]+>")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
SLUG_STRIP_RE = re.compile(r"[^\w\- ]+", re.UNICODE)

KEYWORD_INDEX = "help_center"
MARKDOWN_INDEX = "help_center_markdown"
MAX_CHUNK_CHARS = 4000

# Matches Python-Markdown's default toc permalink slugs closely enough
# for this wiki's headings (ASCII, no collisions).
def slugify(value: str, separator: str = "-") -> str:
    value = SLUG_STRIP_RE.sub("", value).strip().lower()
    return re.sub(rf"[{re.escape(separator)}\s]+", separator, value).strip(separator)


def page_url(site_url: str, md_name: str) -> str:
    base = site_url.rstrip("/") + "/"
    stem = Path(md_name).name
    if stem == "index.md":
        return base
    return f"{base}{Path(stem).stem}/"


def strip_includes_and_chrome(markdown: str) -> str:
    text = SNIPPET_RE.sub("", markdown)
    text = ADMONITION_RE.sub("", text)
    text = DETAILS_RE.sub("", text)
    return text


def strip_inline(text: str) -> str:
    text = IMAGE_RE.sub("", text)
    text = LINK_RE.sub(r"\1", text)
    text = INLINE_CODE_RE.sub(r"\1", text)
    text = EMPHASIS_RE.sub(r"\1", text)
    text = HTML_RE.sub("", text)
    text = text.replace("**", "").replace("__", "")
    return re.sub(r"[ \t]+", " ", text).strip()


def block_plain(text: str) -> str:
    text = FENCE_RE.sub(lambda m: m.group(0).replace("```", "\n"), text)
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if TAB_OPEN_RE.match(line):
            continue
        if line.startswith("|") and line.endswith("|"):
            cells = [strip_inline(c) for c in line.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells if c):
                continue
            lines.append(" ".join(c for c in cells if c))
            continue
        if re.match(r"^[-*+]\s+", line) or re.match(r"^\d+\.\s+", line):
            line = re.sub(r"^[-*+]\s+", "", line)
            line = re.sub(r"^\d+\.\s+", "", line)
        if line.startswith(">"):
            line = line.lstrip("> ").strip()
        line = strip_inline(line)
        if line:
            lines.append(line)
    return "\n".join(lines).strip()


def parse_nav_lvl0(nav: list[Any]) -> dict[str, str]:
    """Map markdown filename -> section title (DocSearch lvl0)."""
    mapping: dict[str, str] = {}

    def walk(items: list[Any], section: str) -> None:
        for item in items:
            if isinstance(item, str):
                mapping[Path(item).name] = section
            elif isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str):
                        mapping[Path(value).name] = section or title
                    elif isinstance(value, list):
                        walk(value, title)

    walk(nav, "Help Center")
    return mapping


def _empty_hierarchy() -> dict[str, str | None]:
    return {f"lvl{i}": None for i in range(7)}


def _heading_sections(markdown: str) -> list[dict[str, Any]]:
    """Split a page into heading-delimited sections."""
    lines = markdown.splitlines()
    sections: list[dict[str, Any]] = []
    current = {"level": 1, "title": "", "lines": []}
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            if current["title"] or current["lines"]:
                sections.append(current)
            current = {
                "level": len(m.group(1)),
                "title": strip_inline(m.group(1) and m.group(2) or ""),
                "lines": [],
            }
            current["title"] = strip_inline(m.group(2))
        else:
            current["lines"].append(line)
    if current["title"] or current["lines"]:
        sections.append(current)
    return sections


def _chunk(text: str, size: int = MAX_CHUNK_CHARS) -> list[str]:
    text = text.strip()
    if not text:
        return []
    if len(text) <= size:
        return [text]
    chunks: list[str] = []
    remaining = text
    while remaining:
        if len(remaining) <= size:
            chunks.append(remaining)
            break
        cut = remaining.rfind("\n", 0, size)
        if cut < size // 2:
            cut = size
        chunks.append(remaining[:cut].strip())
        remaining = remaining[cut:].strip()
    return [c for c in chunks if c]


def records_for_page(
    *,
    markdown: str,
    md_name: str,
    nav_title: str,
    lvl0: str,
    site_url: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    cleaned = strip_includes_and_chrome(markdown)
    url = page_url(site_url, md_name)
    sections = _heading_sections(cleaned)
    if not sections:
        return [], []

    keyword: list[dict[str, Any]] = []
    markdown_recs: list[dict[str, Any]] = []
    stack: list[tuple[int, str]] = []
    position = 0

    page_title = nav_title
    if sections[0]["level"] == 1 and sections[0]["title"]:
        page_title = sections[0]["title"]

    for section in sections:
        level = max(1, min(section["level"], 6))
        title = section["title"] or page_title
        body = block_plain("\n".join(section["lines"]))

        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))

        hierarchy = _empty_hierarchy()
        hierarchy["lvl0"] = lvl0
        hierarchy["lvl1"] = page_title
        for lvl, heading in stack:
            if lvl == 1:
                hierarchy["lvl1"] = heading
            else:
                # h2 -> lvl2, h3 -> lvl3, ...
                hierarchy[f"lvl{lvl}"] = heading

        anchor = slugify(title) if level > 1 else None
        rec_url = f"{url}#{anchor}" if anchor else url
        rec_type = f"lvl{level}" if not body else "content"
        if level > 1 and not body:
            rec_type = f"lvl{level}"
        elif body:
            rec_type = "content"

        position += 1
        keyword.append(
            {
                "objectID": rec_url if rec_type != "content" else f"{rec_url}::{position}",
                "url": rec_url,
                "url_without_anchor": url,
                "anchor": anchor,
                "content": body if rec_type == "content" else "",
                "type": rec_type if rec_type != "content" else "content",
                "hierarchy": hierarchy,
                "hierarchy_radio": {k: v for k, v in hierarchy.items()},
                "lang": "en",
                "language": "en",
                "weight": {
                    "pageRank": 0,
                    "level": 100 - level * 10,
                    "position": position,
                },
            }
        )
        if rec_type == "content" and title and title != page_title:
            # Also emit a heading record so the h2 itself is searchable.
            heading_id = f"{url}#{anchor}" if anchor else url
            keyword.append(
                {
                    "objectID": heading_id,
                    "url": heading_id,
                    "url_without_anchor": url,
                    "anchor": anchor,
                    "content": "",
                    "type": f"lvl{level}",
                    "hierarchy": hierarchy,
                    "hierarchy_radio": {k: v for k, v in hierarchy.items()},
                    "lang": "en",
                    "language": "en",
                    "weight": {
                        "pageRank": 0,
                        "level": 100 - level * 10 + 1,
                        "position": position,
                    },
                }
            )

        heading_for_md = title
        for part_i, chunk in enumerate(_chunk(body)):
            object_id = url if level == 1 and part_i == 0 else f"{url}#{anchor or slugify(title)}:{part_i}"
            markdown_recs.append(
                {
                    "objectID": object_id,
                    "url": rec_url,
                    "title": page_title,
                    "heading": heading_for_md,
                    "text": chunk,
                    "lang": "en",
                }
            )

    return keyword, markdown_recs


def load_mkdocs(repo_root: Path) -> dict[str, Any]:
    import yaml

    with (repo_root / "mkdocs.yml").open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def build_all(repo_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    cfg = load_mkdocs(repo_root)
    site_url = cfg.get("site_url") or ""
    nav = cfg.get("nav") or []
    lvl0_by_file = parse_nav_lvl0(nav)
    docs_dir = repo_root / (cfg.get("docs_dir") or "docs")

    nav_titles: dict[str, str] = {}

    def titles(items: list[Any]) -> None:
        for item in items:
            if isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str):
                        nav_titles[Path(value).name] = title
                    elif isinstance(value, list):
                        titles(value)

    titles(nav)

    keyword: list[dict[str, Any]] = []
    markdown_recs: list[dict[str, Any]] = []
    for md in sorted(docs_dir.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        lvl0 = lvl0_by_file.get(md.name, "Help Center")
        nav_title = nav_titles.get(md.name, md.stem.replace("-", " ").title())
        k, m = records_for_page(
            markdown=text,
            md_name=md.name,
            nav_title=nav_title,
            lvl0=lvl0,
            site_url=site_url,
        )
        keyword.extend(k)
        markdown_recs.extend(m)
    return keyword, markdown_recs
