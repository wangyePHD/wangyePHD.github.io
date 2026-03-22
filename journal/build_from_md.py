#!/usr/bin/env python3
"""Build journal.html from journal/entries/YYYY-MM-DD.md (newest date first).

Used locally after: pip install -r journal/requirements.txt
On GitHub: workflow runs this on every push that touches entries.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Install dependencies: pip install -r journal/requirements.txt", file=sys.stderr)
    raise SystemExit(1) from None

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = Path(__file__).resolve().parent / "entries"
JOURNAL = ROOT / "journal.html"
START = "<!-- JOURNAL_ENTRIES_START -->"
END = "<!-- JOURNAL_ENTRIES_END -->"
DATE_FILE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")


def inject_entries(html: str, merged: str) -> str:
    i0 = html.index(START)
    i1 = i0 + len(START)
    while i1 < len(html) and html[i1] in "\r\n":
        i1 += 1
    j0 = html.index(END, i1)
    end_line_start = j0
    while end_line_start > i1 and html[end_line_start - 1] != "\n":
        end_line_start -= 1
    end_prefix = html[end_line_start:j0]
    return html[:i1] + merged + "\n" + end_prefix + html[j0:]


def human_date(ymd: str) -> str:
    dt = datetime.strptime(ymd, "%Y-%m-%d")
    return f"{dt.strftime('%B')} {dt.day}, {dt.year}"


def md_to_html(text: str) -> str:
    md = markdown.Markdown(
        extensions=["extra", "sane_lists"],
        output_format="html",
    )
    return md.convert(text)


def wrap_article(ymd: str, inner_html: str) -> str:
    display = human_date(ymd)
    body = inner_html.strip()
    return (
        f'<article class="journal-card" id="entry-{ymd}">\n'
        f'    <header class="journal-card__head">\n'
        f'        <time class="journal-card__time" datetime="{ymd}">{display}</time>\n'
        f"    </header>\n"
        f'    <div class="journal-card__body prose">\n'
        f"{body}\n"
        f"    </div>\n"
        f"</article>"
    )


def main() -> None:
    if not ENTRIES.is_dir():
        raise SystemExit("Missing journal/entries/")

    files = sorted(p for p in ENTRIES.iterdir() if p.is_file() and DATE_FILE.match(p.name))
    files.reverse()

    blocks: list[str] = []
    for p in files:
        raw = p.read_text(encoding="utf-8").strip()
        if not raw:
            continue
        ymd = p.stem
        blocks.append(wrap_article(ymd, md_to_html(raw)))

    merged = "\n\n".join(blocks)

    html = JOURNAL.read_text(encoding="utf-8")
    if START not in html or END not in html:
        raise SystemExit(
            "journal.html must contain JOURNAL_ENTRIES_START / JOURNAL_ENTRIES_END markers."
        )

    JOURNAL.write_text(inject_entries(html, merged), encoding="utf-8")
    print(f"Wrote {len(blocks)} entr(y/ies) into journal.html (newest first).")


if __name__ == "__main__":
    main()
