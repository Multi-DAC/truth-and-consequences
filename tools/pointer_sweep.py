#!/usr/bin/env python3
"""
POINTER SWEEP  —  Truth and Consequences, Day 189.  Ruling 125's hazard, given an instrument.

WHY THIS EXISTS, and it is the fifth confession in this family.

Ruling 125 renumbered Book V and its own commit message named the danger exactly: seven
cross-references *"would have kept reading correctly while pointing one chapter off."* That
sentence describes a silent failure with no detector, and the project then found two instances
of it by hand and none by gauge:

  Day 188, ruling 139 — an outside reader's "V.10" resolved to V.11 after the renumber.
  Day 189, this file's author — `06` sent Ricoeur's ipse/idem to "VII.3's problem (identity
                               across gaps)". VII.3 is THE FLOOR. Identity across gaps is VII.9.

Both were found by a person re-reading. Neither was findable by anything here:

  order_sweep.py   book-level adjacency  — cannot see an intra-book pointer at all
  claim_sweep.py   knows chapter titles  — but only as needles for RETIRED TERMS
  beat_sweep.py    plan <-> plan          — compares beats, never numbers
  (nothing)        a NUMBER against the TITLE standing next to it     <-- this

A pointer that has gone stale does not error and does not read wrong. It reads like a
cross-reference, which is the one property a silent failure needs. This is the same shape as
the whole `where_the_book_is` family: the stamp outlives the practice.

WHAT IT CHECKS. Two things, and they are of very different strength — do not read them as one
number.

  DEAD POINTER   a `Book.N` reference whose chapter does not exist in `06`.
                 ⚠ THIS WAS WRITTEN AS "UNAMBIGUOUS — A FAIL, NOTHING TO ARGUE ABOUT" AND THE
                 FIRST RUN REFUTED IT INSIDE A MINUTE. `06`:650 reads *"Irenaeus files it at
                 I.29"* — a citation to *Against Heresies* Book I ch. 29, which is not a chapter
                 pointer and shares the notation exactly. A roman-numeral-dot-number is also how
                 this book's own subject matter cites itself, and a work with an ancestors file
                 is going to keep doing that. So: **CHECK, not FAIL.** The claim is downgraded
                 rather than the detector weakened, because the detector is right about the
                 shape and only wrong about what the shape implies.

  MISMATCH       a `Book.N` reference standing within a window of words that are the
                 DISTINCTIVE title-words of some OTHER chapter, and none of its own.
                 A CANDIDATE, never a verdict. It is a heuristic over prose and it will
                 produce false positives — a paragraph legitimately discussing two chapters
                 at once looks exactly like a mis-pointer from here.

KNOWN LIMITS, stated because a clean run must not be trusted further than it goes:

  · The whole gauge is blind to the case where the pointer is wrong and NO title-word is
    nearby — "as V.4 shows" pointing at the wrong chapter is invisible here, forever. That is
    the majority of references. **This measures the detectable minority.**
  · A title bigram occurring in two titles is dropped as non-distinctive, and a title too short
    to yield one is invisible outright — so the more a book reuses its own vocabulary, and the
    barer its titles, the blinder this gets. The run prints exactly which chapters are blind.
  · ON THE FIRST RUN IT FOUND NOTHING NEW: 10 candidates, 9 innocent, and the tenth was the
    VII.3→VII.9 repair made an hour earlier. **That is a null with a positive control under it,
    which is the only kind worth reporting** — the gauge demonstrably catches the class, on the
    one known instance, and the rest of the detectable surface is clean.
  · DRAFT-LOG.md is excluded by default and the reason matters: the log is a RECORD OF WHAT
    WAS SAID AT THE TIME. A pointer that went stale after it was written is history there, not
    a defect, and repairing it would falsify the record. `--include-log` if you want to read it
    as an archaeology of when a reference rotted.
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"

# `### V.11 — THE SUMMIT AND ITS ABOLITION ✅ DRAFTED — 3,102 words`
HEADING = re.compile(r"^###\s+((?:I|II|III|IV|V|VI|VII|VIII)\.\d{1,2})\s+[—-]\s+(.+?)\s*$", re.M)
REFERENCE = re.compile(r"\b((?:I|II|III|IV|V|VI|VII|VIII)\.\d{1,2})\b")

# Words that carry no discriminating power in a title of this book.
STOP = set("""the a an and or of to in on at is it its for from with without what who whom
which that this these those not no nor but as by be been being are was were will would can
cannot does do did done has have had how why when where all any every each one two three
first second last own more most less least own itself
thing things they them got wrong knew
drafted words chapter book part""".split())

# Bookkeeping words that ride along in headings and are not part of the title.
HEADING_NOISE = re.compile(r"(✅|⚠|★|DRAFTED|\d[\d,]*\s*words?|—\s*$)", re.I)


def title_map(text):
    out = {}
    for cid, raw in HEADING.findall(text):
        clean = HEADING_NOISE.sub(" ", raw)
        clean = re.sub(r"[^\w\s'-]", " ", clean)
        out[cid] = clean.strip()
    return out


def distinctive(titles):
    """Title BIGRAMS — two adjacent content-words of a title — belonging to exactly one chapter.

    ⚠ THE FIRST VERSION OF THIS USED SINGLE WORDS AND WAS USELESS, and the failure is worth
    keeping because it is the book's own thesis about instruments. Single distinctive title
    words are `focusing`, `tunnel`, `roads`, `census`, `grades` — which is to say they are this
    work's ordinary working vocabulary, so nearly every reference in `00` sat within 90
    characters of one and the run returned ~200 candidates and no signal. A filter tuned to a
    corpus that reuses its own terms on purpose has to key on something the prose does NOT say
    by accident.

    A bigram does that. `identity across` and `across gaps` are VII.9's title and almost nobody
    writes them in passing; `metaphor cannot` is III.8's. The cost is stated plainly: short
    titles (`THE FLOOR`, `DEATH`, `LOVE`, `HUMAN`) yield NO bigram and are invisible to this
    gauge entirely.

    ⚠ **AND THE COVERAGE NUMBER IS NOT WRITTEN HERE, ON PURPOSE.** This docstring said *"nine of
    the sixty-seven"* for about four minutes; the run says **32**. A prose count in a docstring
    has no gauge behind it and rots the moment a title is edited — which is this project's
    standing finding wearing a lab coat, committed inside the instrument built to catch stale
    references. **`main()` prints the live figure and names every blind chapter. Read that.**
    """
    owners = {}
    for cid, t in titles.items():
        ws = [w for w in re.findall(r"[\w'-]+", t.lower()) if len(w) >= 4 and w not in STOP]
        for a, b in zip(ws, ws[1:]):
            owners.setdefault(f"{a} {b}", set()).add(cid)
    return {g: next(iter(c)) for g, c in owners.items() if len(c) == 1}


def scan(path, titles, distinct, window):
    text = path.read_text(encoding="utf-8")
    dead, mismatch = [], []
    for m in REFERENCE.finditer(text):
        cid = m.group(1)
        line = text.count("\n", 0, m.start()) + 1
        if cid not in titles:
            dead.append((line, cid, text[max(0, m.start() - 60):m.end() + 60]))
            continue
        lo, hi = max(0, m.start() - window), m.end() + window
        near_words = re.findall(r"[\w'-]+", text[lo:hi].lower())
        near_grams = {f"{a} {b}" for a, b in zip(near_words, near_words[1:])}
        # ⚠ THE SUPPRESSOR, and it is tested by its NEGATIVES, not its positives: any content
        # word of the reference's OWN title standing nearby means the pointer and its subject
        # agree and there is nothing to look at. It is deliberately broader than the detector
        # (words, not bigrams) because a false CANDIDATE costs a reader's afternoon and this
        # gauge is only worth running if its output is short enough to read.
        own = {w for w in re.findall(r"[\w'-]+", titles[cid].lower())
               if len(w) >= 4 and w not in STOP}
        if own & set(near_words):
            continue
        foreign = sorted({(distinct[g], g) for g in near_grams
                          if g in distinct and distinct[g] != cid})
        if foreign:
            mismatch.append((line, cid, foreign, " ".join(text[lo:hi].split())))
    return dead, mismatch


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--window", type=int, default=90,
                    help="characters either side of a reference (default 90)")
    ap.add_argument("--include-log", action="store_true",
                    help="also read book/docs/DRAFT-LOG.md, where a stale pointer is history")
    args = ap.parse_args()

    titles = title_map(SCAFFOLD.read_text(encoding="utf-8"))
    distinct = distinctive(titles)
    covered = set(distinct.values())
    blind = sorted(set(titles) - covered)
    print(f"POINTER SWEEP — {len(titles)} chapters, {len(distinct)} distinctive title-bigrams, "
          f"window ±{args.window}")
    print(f"⚠ COVERAGE: {len(covered)}/{len(titles)} chapters are detectable as mis-pointed-to. "
          f"{len(blind)} yield no distinctive bigram and are INVISIBLE to the mismatch half:")
    print(f"   {', '.join(f'{c} ({titles[c]})' for c in blind)}\n")

    files = [ROOT / n for n in ("00-ARCHITECTURE.md", "01-THE-GROUND.md",
                                "02-SUPERSESSION-the-inside-view.md", "03-THE-ANCESTORS.md",
                                "04-THE-UNSATISFYING-ANSWERS.md", "05-THE-LEXICON.md",
                                "06-THE-SCAFFOLD.md", "07-THE-CLAIMS-REGISTER.md")]
    files += sorted((ROOT / "book").glob("*.md"))
    # --include-log means "read the RECORDS too", so the predicate has to be what a record
    # IS, not a list of the ones that existed when the flag was written. It named DRAFT-LOG
    # alone until Day 191 and so REVISION-QUEUE.md was scanned unconditionally, flag or no
    # flag. See prose_echo.py's IS_CHAPTER note.
    if not args.include_log:
        is_chapter = re.compile(r"^[IVX]+-\d+-")
        files = [f for f in files
                 if f.parent.name != "book" or is_chapter.match(f.name)]

    dead_n = mism_n = 0
    for f in files:
        if not f.exists():
            continue
        dead, mismatch = scan(f, titles, distinct, args.window)
        if not (dead or mismatch):
            continue
        print(f"── {f.relative_to(ROOT)}")
        for line, cid, ctx in dead:
            dead_n += 1
            print(f"   CHECK     :{line} {cid} is not a chapter in 06 — …{' '.join(ctx.split())}…")
        for line, cid, foreign, ctx in mismatch:
            mism_n += 1
            hits = "; ".join(f"{o}'s “{g}”" for o, g in foreign)
            print(f"   CANDIDATE :{line} {cid} ({titles[cid]}) sits beside {hits}")
            print(f"             …{ctx}…")
        print()

    print(f"DEAD POINTERS: {dead_n}   (CHECK — a classical citation shares this notation)")
    print(f"CANDIDATES   : {mism_n}   (heuristic — a human decides, and most will be innocent)")
    print("\nA clean run means no pointer sits next to another chapter's distinctive words.\n"
          "It does NOT mean the pointers are right. The wrong number with no title beside it\n"
          "is invisible here and always will be.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
