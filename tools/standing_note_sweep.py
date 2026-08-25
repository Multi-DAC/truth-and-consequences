"""standing_note_sweep.py — the source-grade standing note, measured as the reader gets it.

R2-071 filed this as "the standing-note pointer is bolted to an arbitrary footnote", counted
18 chapters, and listed the footnote numbers it lands on ([^1] in five, then [^2] [^3] [^4]
[^5] [^7] [^12]). Every part of that was wrong, and it was wrong in a way that mattered:

  * The block is never inside a footnote. It sits at column 0, which ENDS the preceding note
    under Python-Markdown's `footnotes` extension. Nothing is welded to a citation.
  * It never lands on [^1]. It lands after the chapter's LAST note, uniformly, in every
    chapter that carries it. The list of numbers in the row was just each chapter's note count
    read back as if it were a placement.
  * 17 chapters carried it, not 18. The 18th, VI.8, carried none at all despite ten sourced
    notes — a coverage hole the placement framing hid, because a row about WHERE a thing sits
    cannot see a chapter where it does not sit.

The defect that was actually there is only visible AFTER rendering, which is why reading the
markdown could not find it: the `footnotes` extension HOISTS every note definition out of the
body and into a trailing `<div class="footnote">`. That leaves the chapter's own closing rule
adjacent to the standing note's rule, and the two collapse together into a stacked `<hr><hr>`.
Measured across the volume it produced three different renderings of one block — 12 chapters
with two rules, 3 with one, 2 with none.

So this sweep measures the RENDERED shape, not the on-disk separator. The on-disk separator is
not the thing the reader meets, and checking it is how the defect survived being looked at.

Exit 1 if the rendering is not uniform, or if a sourced Book IV / Book VI chapter carries no
standing note at all.
"""
import glob
import os
import re
import sys

MARK = "*On the grade of the sources"
BODY = "On the grade of the sources"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# every chapter of the two books whose apparatus carries external sources
SOURCED = re.compile(r"(IV|VI)-\d\d-")


def render(text):
    import markdown

    md = markdown.Markdown(
        extensions=["extra", "footnotes", "sane_lists", "smarty"],
        extension_configs={"smarty": {"smart_dashes": False}},
    )
    return md.convert(text)


def measure(path):
    text = open(path, encoding="utf-8").read()
    if MARK not in text:
        return None
    html = render(text)
    i = html.find(BODY)
    notes_div = html.find('class="footnote"')
    rules = len(re.findall(r"<hr\s*/?>", html[max(0, i - 260):i]))
    return {
        "name": os.path.basename(path),
        "rules": rules,
        "before_notes": i < notes_div if notes_div >= 0 else None,
    }


def main():
    chapters = sorted(glob.glob(os.path.join(REPO, "book", "*.md")))
    rows = [r for r in (measure(p) for p in chapters) if r]

    print("STANDING NOTE — source-grade block, measured AFTER rendering")
    print("  (the markdown separator is not what the reader meets; the hoisted output is)")
    print()
    print(f"  {'chapter':<50}{'rules':>7}{'before Notes':>14}")
    for r in rows:
        flag = "" if r["rules"] == 1 else "   <-- not uniform"
        print(f"  {r['name']:<50}{r['rules']:>7}{str(r['before_notes']):>14}{flag}")

    print()
    print(f"  CARRYING THE NOTE          : {len(rows)}")
    dist = {}
    for r in rows:
        dist[r["rules"]] = dist.get(r["rules"], 0) + 1
    print(f"  RENDERED RULE COUNTS       : {dict(sorted(dist.items()))}")

    sourced = [p for p in chapters if SOURCED.search(os.path.basename(p))]
    missing = [
        os.path.basename(p)
        for p in sourced
        if MARK not in open(p, encoding="utf-8").read()
    ]
    print(f"  SOURCED CHAPTERS (IV + VI) : {len(sourced)}")
    print(f"  CARRYING NO NOTE           : {len(missing)}")

    ok = True
    if len(dist) != 1 or 1 not in dist:
        print("\n  ⛔ ONE BLOCK, MORE THAN ONE RENDERING. Expected exactly 1 rule everywhere.")
        ok = False
    if missing:
        print(f"\n  ⛔ COVERAGE HOLE — no standing note in: {', '.join(missing)}")
        ok = False
    if any(r["before_notes"] is False for r in rows):
        print("\n  ⛔ a copy renders AFTER the Notes section; 'the sources above' is then false.")
        ok = False

    if ok:
        print(f"\n  ✅ {len(rows)} chapters, one rendering, no sourced chapter without one.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
