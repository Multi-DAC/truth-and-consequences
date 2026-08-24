#!/usr/bin/env python3
"""One-shot: remove process-row IDs (`ruling 177`, `R-144`) from book prose. D205.

These are pointers into a queue no reader has. Nothing in the volume defines them —
not Z-01, not Z-02 — so on the page they read as a scholarly cross-reference apparatus
for a body of rulings that does not exist.

The rule applied here is NOT "delete the sentence." An endnote that says a thing was
repaired is still telling the reader something true about the text in front of them.
What goes is the *pointer* — the row ID, and the filing verb that only makes sense if
you have the row. What stays is the claim.

Only tight patterns are handled here. Everything this leaves behind is printed at the
end and gets hand-worked; a regex that rewrites English is how you ship a sentence
nobody read.
"""
import re
import pathlib

BOOK = pathlib.Path(__file__).resolve().parent.parent / "book"
PROCID = re.compile(r"\b(?:[Rr]uling\s+\d+|R-\d+)\b")

# (pattern, replacement). Applied in order, per line.
RULES = [
    # --- filing clauses: the whole clause is queue-talk, not a claim about the text
    (r"\s*\*\*Filed with R-\d+\*\*", " Filed"),
    (r"\s*Filed with R-\d+'s trigger:\s*", " Filed for "),
    (r"\s*Filed with R-\d+ for the revision pass\.", ""),
    (r"\s*Filed with R-\d+ under the\b", " Filed under the"),
    (r"\s*Filed with R-\d+\.", ""),
    (r"\s*Filed as R-\d+\.", ""),
    (r"\s*Filed Day (\d+) as \*\*R-\d+\*\*\.", r" Filed Day \1."),
    (r"\s*Filed Day (\d+) as R-\d+, with", r" Filed Day \1, with"),
    (r"\s*filed as \*\*R-\d+\*\*\.", "."),
    (r"\s*\bR-\d+\.\s*$", ""),

    # --- "under ruling N" / "(ruling N)": the authority pointer, not the fact
    (r"\s*\(ruling \d+\)", ""),
    (r",\s*ruling \d+\b", ""),
    (r"\bunder ruling \d+,\s*", ""),
    (r"\bunder ruling \d+\b", ""),
    (r"\bUnder ruling \d+,?\s*", ""),
    (r"\bRuling \d+'s pattern\b", "That pattern"),
    (r"\bruling \d+'s pattern\b", "that pattern"),
    (r"\bruling \d+ describes\b", "described above"),
    (r"\bRuling \d+ records it\b", "The record has it"),
    (r"\bRuling \d+ banned the term\b", "The term was banned"),
    (r"\bruling \d+'s sweep list\b", "that sweep's list"),
    (r"\bDAY (\d+), ruling \d+\b", r"DAY \1"),

    # --- bare ID as the subject of a sentence: give it an English subject
    (r"\bR-\d+'s (shape|class|mechanism|neighbourhood|line-scoping|condition)\b",
     r"the same \1"),
    (r"\bR-\d+ is the standing finding\b", "The standing finding is"),
    (r"\bqueue row R-\d+\b", "an earlier pass"),
    (r"\bR-\d+ named\b", "An earlier pass named"),
    (r"\bR-\d+ found\b", "an earlier pass found"),
    (r"\bR-\d+ filed that\b", "An earlier pass filed that"),
    (r"\bR-\d+ predicted\b", "An earlier pass predicted"),
    (r"\bR-\d+ prescribed\b", "That pass prescribed"),
    (r"\bR-\d+ was filed against\b", "The finding was filed against"),
    (r"\bR-\d+ called for\b", "the earlier pass called for"),
    (r"\bthe settled form of R-\d+\b", "the settled form of that finding"),
    (r"\bthe half of R-\d+\b", "the half of that finding"),
    (r"\bas \*\*R-\d+\*\* by the ghost audit\b", "by the ghost audit"),
]

CLEANUP = [
    (r"[ \t]{2,}", " "),
    (r"\s+([.,;:!?])", r"\1"),
    (r"\*\*\s+", "** "),
    (r"\s+\*\*", " **"),
    (r"\.\s*\.", "."),
]

touched, residual = [], []
for path in sorted(BOOK.glob("*.md")):
    lines = path.read_text(encoding="utf-8").splitlines()
    out, changed = [], False
    for i, line in enumerate(lines, 1):
        if not PROCID.search(line):
            out.append(line)
            continue
        orig = line
        # indent is held out of every substitution — see the note in _strip_slugs.py;
        # the same collapse ate 73 footnote continuation indents there.
        indent = re.match(r"^\s*", line).group(0)
        body = line[len(indent):]
        for pat, rep in RULES:
            body = re.sub(pat, rep, body)
        line = indent + body
        if line != orig:
            for pat, rep in CLEANUP:
                body = re.sub(pat, rep, body)
            line = (indent + body.strip()).rstrip()
            changed = True
            touched.append((path.name, i, orig.strip(), line.strip()))
        if PROCID.search(line):
            residual.append((path.name, i, line.strip()))
        out.append(line)
    if changed:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")

for name, ln, before, after in touched:
    print(f"{name}:{ln}\n  -  {before[:190]}\n  +  {after[:190]}")
print(f"\n{len(touched)} line(s) rewritten.")
print(f"{len(residual)} line(s) STILL CARRY AN ID — hand-work these:\n")
for name, ln, line in residual:
    print(f"  {name}:{ln}\n      {line[:200]}")
