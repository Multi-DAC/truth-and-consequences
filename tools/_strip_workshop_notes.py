#!/usr/bin/env python3
"""Fourth pass: the grade notes lose their workshop framing and their archive pointers. D205.

TWO THINGS ARE BEING SEPARATED HERE, and the separation is the whole judgement.

  WORKSHOP — "*The standing note on grade, owed here as in VI.1 through VI.6.*", and the
  eighteen footnote-bolted pointers reading "See the standing note on grade above". That is
  apparatus naming apparatus, and a debt-to-a-maintainer written into shipped text. It goes.

  GRADE — "named from general knowledge and standard reference scholarship, not quoted,
  carrying no receipt." That is not workshop. It tells the reader how far to trust the page,
  which is the discipline the whole volume is built on. It stays.

And the archive pointer inside the grade sentence — "none of their texts is in this
repository" — becomes "none was consulted at first hand". Identical information about the
grade of the claim; no pointer at a tree the reader cannot open.
"""
import re
import pathlib

BOOK = pathlib.Path(__file__).resolve().parent.parent / "book"

LINE_RULES = [
    # the memo's own title line: drop the apparatus name and the owed-here-as-in ledger
    (r"\*The standing note on grade, which V\.1 opened for this book and which is owed here more than\nanywhere\.\*",
     "*On the grade of the names below, which this book owes here more than anywhere.*"),
    (r"\*The standing note on grade,[^*]*\*", "*On the grade of the sources above.*"),
    (r"\*The standing note on grade\.\*", "*On the grade of the sources above.*"),

    # the eighteen bolted pointers
    (r"\s*\*\*See the standing note on grade above\*\*, which states at what level this chapter's attributions are made and which of them are flagged for reading\.",
     ""),
    (r"\s*See the standing note on grade above\.", ""),

    # archive pointers inside grade sentences — the grade survives, the address goes
    (r"None of their texts is in this repository", "None of their texts was consulted at first hand"),
    (r"Not one of their texts\n?is in this repository", "Not one of their texts was consulted at first hand"),
    (r"neither text is in this repository", "neither text was consulted at first hand"),
    (r"Neither text is in this repository", "Neither text was consulted at first hand"),
    (r"None of these papers is in this repository", "None of these papers was consulted at first hand"),
    (r"no text in this repository", "no text consulted at first hand"),
    (r"no texts in this repository", "no texts consulted at first hand"),
    (r"[Nn]ot in this repository", "Not consulted at first hand"),
    (r"is in this repository", "was consulted at first hand"),
    (r"in this repository", "at first hand"),
    (r"held in this repository", "held at first hand"),
]

# whole-file substitutions that span a wrap
SPAN_RULES = [
    ("None of their texts is in this\nrepository, and nothing above is a quotation",
     "None of their texts was consulted at first\nhand, and nothing above is a quotation"),
    ("Not one of their texts\nis in this repository, and nothing above is a quotation",
     "Not one of their texts\nwas consulted at first hand, and nothing above is a quotation"),
    ("None of their texts is in this repository, and nothing\nabove is a quotation",
     "None of their texts was consulted at first hand, and nothing\nabove is a quotation"),
    ("`corpora/` holds four literary",
     "the chapter's own shelf holds four literary"),
]

touched = 0
for path in sorted(BOOK.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    orig = text
    for old, new in SPAN_RULES:
        text = text.replace(old, new)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        # ⚠ Only lines that actually match are touched. An earlier draft of this loop ran
        # the whitespace collapse over EVERY line in every file, which would have eaten
        # markdown's trailing-double-space line breaks across the whole volume in a diff
        # far too large to read.
        if not re.search(r"standing note|repositor|corpora/", line):
            continue
        indent = re.match(r"^\s*", line).group(0)
        body = line[len(indent):]
        for pat, rep in LINE_RULES:
            body = re.sub(pat, rep, body)
        body = re.sub(r"[ \t]{2,}", " ", body).strip()
        lines[i] = (indent + body).rstrip() if body else ""
    text = "\n".join(lines)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        touched += 1

print(f"{touched} file(s) rewritten.")

# report what is left
left = []
for path in sorted(BOOK.glob("*.md")):
    for i, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        if re.search(r"standing note|repositor", line, re.I):
            left.append(f"  {path.name}:{i}  {line.strip()[:150]}")
print(f"{len(left)} line(s) still carry 'standing note' or 'repository':")
print("\n".join(left))
