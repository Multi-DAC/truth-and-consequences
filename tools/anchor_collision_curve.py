"""
ANCHOR COLLISION CURVE — how long must a verification anchor be, in THIS text?

WHY IT EXISTS. Day 190, R-30: IV.9's Irenaeus Latin was diffed against two Harvey
scans, anchored on the four-word string `Si enim mundi fabricator`. That string
occurs at least twice in Adversus haereses. The check landed on the wrong passage
and reported it as the divergence it was hunting. The ruling that came out of it
said "verification anchors must be unique" — which is true and unactionable, since
you cannot know a string is unique without already having searched.

WHAT IT MEASURES. P(an n-word anchor drawn from this text occurs more than once in
it), for a ladder of n. That is the chance-match rate of a locator, and it is a
property of the CORPUS, not of the anchor. Measured over the four source texts in
corpora/: Kempis at n=5 collides 4.7%, James at n=5 collides 1.1% — a factor of
four between two prose texts of comparable size. To buy James's n=5 safety inside
Kempis you need n around 12. There is no universal "long enough".

HOW TO USE IT. Run it on the text you are about to anchor INTO (the source, not the
book), read the row, and pick the smallest n whose collision rate is under your
tolerance. For patristic polemic — formulaic, built on repeated refutation
formulae — expect Kempis-like numbers, i.e. a four-word anchor is a coin-flip's
cousin, not an address.

WHAT IT DELIBERATELY DOES NOT DO. It does not tell you an anchor is safe. It tells
you the rate at which anchors OF THAT LENGTH are unsafe in that text; your specific
string can still be the one that repeats. It also cannot see across editions: two
scans of the same work may differ in exactly the passage that makes your anchor
non-unique. And it normalises punctuation and case away, so it is a floor on the
collision rate, never a ceiling.

Provenance: LC70, palace/basement/README.md (carapace). Companion finding:
search_memory reports a similarity with no zero-point — same defect, other domain.
"""

import re
import sys
from collections import Counter
from pathlib import Path

LADDER = [3, 4, 5, 6, 8, 10, 12]


def collision_curve(text: str, ladder=LADDER):
    """Return {n: P(a randomly drawn n-gram occurrence sits on a repeated string)}."""
    words = re.findall(r"[a-z']+", text.lower())
    out = {}
    for n in ladder:
        grams = Counter(tuple(words[i:i + n]) for i in range(len(words) - n + 1))
        total = sum(grams.values())
        out[n] = (sum(c for c in grams.values() if c > 1) / total) if total else 0.0
    return len(words), out


def main(argv):
    targets = [Path(a) for a in argv[1:]]
    if not targets:
        targets = sorted((Path(__file__).parent.parent / "corpora").glob("*.txt"))
    if not targets:
        print("no texts given and corpora/ is empty", file=sys.stderr)
        return 1

    print(f"{'text':24s} {'words':>8s} " + " ".join(f"n={n:<3d}" for n in LADDER))
    print("-" * 80)
    for p in targets:
        if not p.exists():
            print(f"{p.name:24s}   MISSING")
            continue
        w, curve = collision_curve(p.read_text(encoding="utf-8", errors="ignore"))
        print(f"{p.stem[:24]:24s} {w:8d} " + " ".join(f"{curve[n] * 100:5.1f}%" for n in LADDER))
    print("\nread: P(an n-word anchor drawn from this text occurs MORE THAN ONCE in it)")
    print("pick the smallest n under your tolerance. no exit code, no opinion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
