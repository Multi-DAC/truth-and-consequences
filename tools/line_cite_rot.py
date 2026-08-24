#!/usr/bin/env python3
"""line_cite_rot.py — a chapter:line citation is an address, and addresses move.

WHY THIS EXISTS. The endnotes cite our own chapters by LINE NUMBER — `V.1:382`, `IV.7:588-589`,
104 of them. A line number is the most brittle pointer in the volume: it is invalidated by any
edit ANYWHERE ABOVE IT in the target file, including edits that have nothing to do with the
cited sentence. Nothing in this tree looked. `crossref_rot.py` asks WHEN a citation was written
against WHEN a note landed; `pointer_sweep.py` asks whether a chapter pointer sits near the
right words. Neither reads the number.

Found on Day 205 by the audit Clayton asked for after a day of revision passes: 20 of 104 line
citations pointed at the wrong line, and 2 of those 20 were broken THAT DAY by an edit three
paragraphs upstream in V.1.

WHAT THE TEST IS. Strictly one shape, and the strictness is the point:

    *"the quoted span"* (X.Y:N)

quote, then the citation in parentheses, nothing intervening. The span is normalised, looked up
in chapter X.Y, and the line it actually starts on is compared with N.

WHY ONLY THAT SHAPE. The first version of this check paired each citation with the NEAREST
PRECEDING quoted span within three lines. That heuristic is fine for LOCATING and fatal for
REPAIRING: it mis-paired `(V.1:178-186)` — a range pointer with no quote of its own — with the
previous line's quotation and moved it thirteen lines. A locator was used as a repairer and it
wrote a wrong number into the book. Hence: this gauge only adjudicates citations that carry
their own quote, and it PRINTS the ones it cannot decide rather than guessing at them.

WHAT IT CANNOT DO. Range pointers, bare chapter references, and citations whose span it cannot
find are reported as UNDECIDED, never as clean. An UNDECIDED count above zero means a human
still has to read. There is no configuration in which this tool's silence licenses a claim that
every line citation in the book is correct.

USAGE
    python tools/line_cite_rot.py            # report
    python tools/line_cite_rot.py --fix      # rewrite only the decidable, quote-adjacent ones

EXIT CODE: 1 if the POSITIVE CONTROL fails, or if any decidable citation is wrong. 0 otherwise.
"""

from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIR = re.compile(
    r'\*"(.{20,400}?)"\*\s*\(((?:VIII|VII|VI|IV|V|III|II|I)\.\d{1,2}):(\d{1,4})\)', re.S
)
CITE_ANY = re.compile(r'\b((?:VIII|VII|VI|IV|V|III|II|I)\.\d{1,2}):(\d{1,4})(?:[–—-]\d{1,4})?\b')


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", s.lower())).strip()


def chapters(book_dir):
    out = {}
    for f in glob.glob(os.path.join(book_dir, "*.md")):
        m = re.match(r"([IVX]+|C|Z)-(\d\d)-", os.path.basename(f))
        if m:
            out[f"{m.group(1)}.{int(m.group(2))}"] = f
    return out


def lines_of(path):
    return [norm(re.sub(r"\*\*|\*", "", x)) for x in open(path, encoding="utf-8").read().splitlines()]


def locate(target_lines, span):
    """Return the 1-based line on which the span BEGINS.

    An earlier version scanned three-line windows and returned the window's first line, which is
    off by up to two whenever the span starts on the window's second or third line — inside the
    gauge's own tolerance, so the gauge certified its own error. Offsets are exact; windows are not.
    """
    probe = norm(re.sub(r"\*\*|\*|…", "", span))[:70]
    if len(probe) < 25:
        return None
    joined, starts, pos = [], [], 0
    for line in target_lines:
        starts.append(pos)
        joined.append(line)
        pos += len(line) + 1
    hay = " ".join(joined)
    idx = hay.find(probe)
    if idx < 0:
        return None
    lo = 0
    for i, s in enumerate(starts):
        if s <= idx:
            lo = i
        else:
            break
    return lo + 1


def scan(book_dir, fix=False):
    chap = chapters(book_dir)
    wrong, undecided, ok = [], [], 0
    for f in sorted(glob.glob(os.path.join(book_dir, "*.md"))):
        src = os.path.basename(f)[:-3]
        txt = open(f, encoding="utf-8").read()
        decided_spans = set()
        out, cursor = [], 0

        # Rebuild the text span by span. A global str.replace would be wrong: two distinct
        # citations can share the same token — `(IV.10:549)` appears twice pointing at different
        # sentences — and a global replace gives both the first one's answer, then silently finds
        # nothing to do for the second. The anchor has to be the match position, not the text.
        for m in PAIR.finditer(txt):
            span, cid, n = m.group(1), m.group(2), int(m.group(3))
            decided_spans.add((cid, n))
            replacement = m.group(0)
            if cid not in chap:
                wrong.append((src, cid, n, None, "target chapter does not exist"))
            else:
                actual = locate(lines_of(chap[cid]), span)
                if actual is None:
                    undecided.append((src, cid, n, "quoted span not found in target"))
                elif actual == n:
                    ok += 1
                else:
                    wrong.append((src, cid, n, actual, norm(span)[:52]))
                    if fix:
                        replacement = m.group(0)[: m.start(2) - m.start(0)] + f"{cid}:{actual})"
            out.append(txt[cursor : m.start()])
            out.append(replacement)
            cursor = m.end()
        out.append(txt[cursor:])
        changed = "".join(out)

        for m in CITE_ANY.finditer(txt):
            cid, n = m.group(1), int(m.group(2))
            if (cid, n) not in decided_spans:
                undecided.append((src, cid, n, "no quote of its own — range or bare pointer"))

        if fix and changed != txt:
            open(f, "w", encoding="utf-8").write(changed)
    return ok, wrong, undecided


def positive_control():
    """Plant a citation off by twenty and confirm the gauge says so. Without this a zero is nothing."""
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "book"), exist_ok=True)
        tgt = os.path.join(d, "book", "I-01-synthetic.md")
        body = ["filler"] * 40 + ["the planted sentence that the citation points at"] + ["filler"] * 10
        open(tgt, "w", encoding="utf-8").write("\n".join(body))
        cit = os.path.join(d, "book", "I-02-synthetic.md")
        open(cit, "w", encoding="utf-8").write(
            'A note quoting it: *"the planted sentence that the citation points at"* (I.1:21).\n'
            'And one that is right: *"the planted sentence that the citation points at"* (I.1:41).\n'
        )
        ok, wrong, _ = scan(os.path.join(d, "book"))
        caught = [w for w in wrong if w[2] == 21 and w[3] == 41]
        return len(caught) == 1 and ok == 1


def main():
    fix = "--fix" in sys.argv
    print("POSITIVE CONTROL — one citation planted twenty lines off, one planted correct:")
    if not positive_control():
        print("  [BROKEN] the control did not come back as expected. A zero below means nothing.")
        sys.exit(1)
    print("  [ok] the wrong one is caught and the right one is not.\n")

    ok, wrong, undecided = scan(os.path.join(ROOT, "book"), fix=fix)
    print(f"LINE-CITATION ROT — {ok + len(wrong)} decidable, {len(undecided)} undecidable\n")
    for src, cid, n, actual, why in wrong:
        arrow = f"-> {cid}:{actual}" if actual else ""
        print(f"  {'FIXED ' if fix else '⛔ WRONG'} {src}: {cid}:{n} {arrow}   |{why}")
    if not wrong:
        print("  ✅ every quote-adjacent line citation resolves to the line it names.")
    print(f"\n  UNDECIDED: {len(undecided)} citation(s) carry no quote of their own.")
    for src, cid, n, why in undecided[:12]:
        print(f"      {src}: {cid}:{n} — {why}")
    if len(undecided) > 12:
        print(f"      … and {len(undecided) - 12} more.")
    print(
        "\n  LIMIT — UNDECIDED is not clean. A range pointer or a bare reference is invisible\n"
        "  to this test, and the one time a heuristic was allowed to guess at them it wrote a\n"
        "  wrong number into the book. Those rows need a reader, not a gauge."
    )
    sys.exit(1 if wrong and not fix else 0)


if __name__ == "__main__":
    main()
