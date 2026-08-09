#!/usr/bin/env python3
"""
ANCESTOR GAP  â€”  Truth and Consequences, Day 187.  Ruling 40's instrument.

THE GAP NO EXISTING TOOL LOOKS AT.

  ancestor_sweep.py  counts names in the CORPUS  (2,550 research files)
  claim_sweep.py     sweeps terms in the BOOK    (43 drafted chapters of 67; R-27, Day 189)

Nothing compares the two, and the boundary between them is where an ancestor is
lost. Found Day 187 by Fable, reading II.7: the chapter states relational quantum
mechanics as its own doctrine and never names Carlo Rovelli.

Fable's conjecture was that the corpus count "would presumably show him at or near
zero." IT DOES NOT. Rovelli is at **14 files** â€” better attested than Peirce (3),
Zeh (3), Everett (5). The name was known, read, and written down fourteen times,
and did not survive the transfer into the manuscript.

So this is NOT the fifth silence of `03` Â§3.5 (doctrine used, owner never known).
It is a sixth, and it is the one a research-heavy project should have expected:

  â˜… OWNER KNOWN IN THE RESEARCH, OWNER DROPPED AT THE DRAFTING BOUNDARY.

Â§3.5 is blind to it by construction. That section ranks names by how THIN they are
in the corpus, so a name the corpus knows well is exactly what it filters OUT â€” it
sorts Rovelli to the bottom of the list of things to worry about, on the strength of
the same 14 that make him damning. An instrument pointed at our ignorance cannot see
a failure of our memory.

KNOWN LIMIT, stated because it is the whole honest boundary of this file: the seed
list is names SOMEBODY ALREADY WROTE DOWN as ancestors. A figure who is in neither
`03` nor `ancestor_sweep.TERMS` is invisible here no matter how load-bearing. That
class is found by an outside reader who knows the field, and by nothing else we own.
Fable found this one. The tool is the cheaper second pass, not the replacement.

CONTRACT: inherits ancestor_sweep's exactly (root, glob, case-insensitivity,
UNIT = files containing the string). Book side = book/*.md drafted chapters only.
"""
import io, re, sys, pathlib, contextlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):     # its import prints its own sweep
    import ancestor_sweep as A

REPO = HERE.parent
CHAPTER = re.compile(r"^[IVX]+-\d\d-.*\.md$")
STOP = {"the", "and", "zero", "this", "that", "book", "one", "two", "not", "but",
        "capture", "his", "our", "not defective", "thin"}


def seed_names():
    """Names somebody already nominated: 03's bolded table cells + ancestor_sweep.TERMS."""
    names = set()
    for group in A.TERMS.values():
        for t in group:
            if t[:1].isupper() and len(t) > 3:
                names.add(t)
    anc = REPO / "03-THE-ANCESTORS.md"
    if anc.exists():
        for m in re.finditer(r"\*\*([^*]{4,40})\*\*", anc.read_text(encoding="utf-8")):
            s = m.group(1).strip().strip("â€”Â·").strip()
            for part in re.split(r"\s*[Â·/]\s*", s):
                part = part.strip().strip('"â€œâ€')
                if (part and part[0].isupper() and part.lower() not in STOP
                        and not part.isupper() and len(part.split()) <= 3
                        and not re.search(r"\d", part)):
                    names.add(part)
    return sorted(names)


def main():
    book = {}
    for p in sorted((REPO / "book").glob("*.md")):
        if CHAPTER.match(p.name):
            book[p.name] = p.read_text(encoding="utf-8").lower()
    print(f"CORPUS : {len(A.live)} .md (archives excluded)   ROOT {A.ROOT}")
    print(f"BOOK   : {len(book)} drafted chapters\n")

    rows = []
    for name in seed_names():
        n = name.lower()
        c = sum(1 for t in A.live if n in t)
        b = sum(1 for t in book.values() if n in t)
        rows.append((c, b, name))

    gaps = sorted([r for r in rows if r[1] == 0 and r[0] >= 3], reverse=True)
    print("â˜… KNOWN IN THE RESEARCH, ABSENT FROM EVERY DRAFTED CHAPTER  (corpus >= 3, book = 0)")
    print("  corpus  name")
    for c, _, name in gaps:
        print(f"  {c:6d}  {name}")
    print(f"\n  {len(gaps)} names. This is a work-list, not a verdict: a name belongs in the")
    print("  book only where a chapter actually owes it. Absence is a question, not a defect.")

    present = sorted([r for r in rows if r[1] > 0], reverse=True)
    print(f"\n  (for contrast: {len(present)} seeded names DO appear in at least one chapter)")

    # ---- DIFFUSION -------------------------------------------------------
    # The failure the section above cannot see, found Day 187 by Opus reading
    # Book III: Varela/Thompson/Rosch, *The Embodied Mind*, in FOUR chapters
    # with four different relationships â€” adopted in III.6, cut on duration in
    # III.4, cut on membership in III.5, the source of III.7's central image â€”
    # and no consolidated accounting anywhere. That is Rovelli INVERTED: not a
    # silence but a diffusion. `book == 0` is exactly the wrong test for it; a
    # name in four chapters sorts into "present" above and is never looked at
    # again. Presence in both corpus and book is what this file checks, so it
    # passes the defect by construction.
    #
    # NO THRESHOLD AND NO VERDICT, on purpose. A rule for "is this accounted
    # for" would be a rule fitted to the one instance that provoked it. The
    # honest instrument here EXPOSES the class and makes the human judgement
    # cheap: everybody the book leans on in three or more places, with the
    # places named, so the question "where is this relationship consolidated?"
    # can be asked once per row instead of never.
    # âš  DELIBERATE DIVERGENCE FROM THE INHERITED CONTRACT, scoped to this section
    # so every number above stays byte-comparable with previous runs. The sweep
    # matches SUBSTRINGS; here that put "Mach" at the top of the list with ten
    # chapters, on the strength of *Machado*, *machine* and *machinery*. A short
    # list whose first row is garbage is a list that gets skipped, and a gauge is
    # spent the first time it is disbelieved â€” so this section matches on word
    # boundaries. It is the narrower test, and it can therefore MISS (an ancestor
    # named only inside a hyphenated compound), which is the right way for a
    # work-list to fail.
    spread = []
    for name in seed_names():
        pat = re.compile(r"\b" + re.escape(name.lower()) + r"\b")
        where = [f.replace(".md", "") for f, t in book.items() if pat.search(t)]
        if len(where) >= 3:
            spread.append((len(where), name, where))
    spread.sort(reverse=True)
    print("\nâ˜… DIFFUSED â€” leaned on in 3+ chapters (is the relationship consolidated ANYWHERE?)")
    print("  chaps  name")
    for k, name, where in spread:
        print(f"  {k:5d}  {name}")
        print(f"         {' Â· '.join(sorted(where))}")
    print(f"\n  {len(spread)} names. Many rows here are fine â€” a term used everywhere needs no")
    print("  dossier. The row to worry about is the one where the book takes a DIFFERENT")
    print("  position each time and never says so in one place.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
