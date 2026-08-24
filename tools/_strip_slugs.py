#!/usr/bin/env python3
"""One-shot: strip [[lesson_slug]] tags from book prose. D205, Clayton's ruling.

Deletes the tag and repairs the joint it leaves: leading/trailing separators, doubled
spaces, a line that becomes empty inside a wrapped paragraph (delete the line, do not
leave a blank that splits the paragraph).

Reports every line it touched. Six sites are grammatically load-bearing and are repaired
by hand afterwards — this script does not try to write English.
"""
import re
import pathlib
import sys

BOOK = pathlib.Path(__file__).resolve().parent.parent / "book"
SLUG = re.compile(r"\[\[[a-z0-9][a-z0-9_-]{4,}\]\]")

touched = []
for path in sorted(BOOK.glob("*.md")):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=False)
    out = []
    changed = False
    for i, line in enumerate(lines):
        if not SLUG.search(line):
            out.append(line)
            continue
        orig = line
        indent = re.match(r"^\s*", line).group(0)
        body = line[len(indent):]
        s = SLUG.sub("", body)
        # collapse the debris the tags leave behind.
        # ⚠ The whitespace collapse runs on the BODY, never on the line. The first
        # version ran it on the whole line and ate the 4-space continuation indent
        # of every footnote line that opened with a tag — 73 of them, silently, in
        # a pass whose report showed only the text it had changed and not the margin.
        s = re.sub(r"[ \t]{2,}", " ", s)
        s = re.sub(r"\s+·\s*(?=\s|$)", " ", s)          # orphaned middot separator
        s = re.sub(r"(?<=\S)\s+·\s+(?=[.,;:])", "", s)
        s = re.sub(r"\s+([.,;:!?])", r"\1", s)           # space before punctuation
        # the tag was the thing a colon or dash introduced; the introducer goes too
        s = re.sub(r"\s*[:;,—–]\s*([.,;!?])", r"\1", s)
        s = re.sub(r"^[·—–-]\s*", "", s)                 # body now opens with a separator
        s = re.sub(r"\s*[·—–]\s*$", "", s)               # body now ends with a separator
        s = s.strip()
        if s == "":
            # the line was nothing but tags: drop it rather than leave a paragraph break
            changed = True
            touched.append((path.name, i + 1, orig.strip(), "<LINE DELETED>"))
            continue
        s = indent + s
        if s != orig:
            changed = True
            touched.append((path.name, i + 1, orig.strip(), s.strip()))
        out.append(s)
    if changed:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")

for name, ln, before, after in touched:
    print(f"{name}:{ln}")
    print(f"  -  {before[:160]}")
    print(f"  +  {after[:160]}")
print(f"\n{len(touched)} line(s) touched.")
