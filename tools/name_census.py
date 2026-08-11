"""NAME CENSUS — the recall-first counterpart to endnote_debt.py.

WHY A SECOND INSTRUMENT RATHER THAN A PATCH TO THE FIRST.

`endnote_debt.py` decides SOURCE-hood from three constructions: `Name's <noun>`,
`Name (aux)? <attributive verb>`, and `according to Name`. That is a PRECISION
instrument -- it is built to avoid calling `Western` an author, and it succeeds.

Day 192 measured its recall for the first time, on V.2, where it reports 0
sources and hand enumeration finds four. Every one of the four is a real
authority the chapter leans on, and each is missed for a locatable reason:

    Tillich took away God's face ...............  verb not in the stem list
    Aquinas, in Paris in the twelve-sixties, ...  APPOSITIVE splits name from verb
    Eckhart, preaching in German ..., distinguishes  APPOSITIVE (verb IS in the list)
    Maimonides, in Cairo, rules that ..........  APPOSITIVE **and** verb not listed

⛔ THAT LAST ROW IS THE WHOLE REASON THIS FILE IS SEPARATE. Two independent gaps
must BOTH be closed before Maimonides is visible. A repair scoped to the named
cause -- the appositive, which is three of the four sites -- recovers Aquinas and
Eckhart, takes V.2 from 0 to 2, and reports itself fixed while half the chapter's
sources stay invisible. The obvious patch passes its own test at 50%.

So this file does not decide. It ENUMERATES, at maximum recall, and hands the
judgement to a reader. It deliberately keeps what endnote_debt drops:

  * names whose lowercase twin is ordinary vocabulary are REPORTED WITH THE
    COUNT, not removed -- so a wrongly-dropped source is visible as a row rather
    than as an absence. (`Filter precision eats recall`: a noise filter drops
    true positives that share the noise's shape. The cure is not a better
    threshold, it is refusing to threshold and fixing the REPORTING UNIT.)
  * every occurrence carries its own position class, so a name that is furniture
    in four sites and an authority in the fifth is not averaged away.

REPORTING UNIT is (name x chapter), with all sites nested under it. Not
(name x occurrence): the first cut of crossref_rot.py emitted a cross-product,
223 rows for 490 references, and a gauge nobody reads behaves exactly like a
gauge that emits nothing while arriving dressed as rigour.

POSITION CLASSES, and what each is evidence of:

  POSS        Name's <lowercase>          -- endnote_debt sees this
  VERB        Name (aux)? <attrib verb>   -- endnote_debt sees this
  ACCORDING   according to / per / following Name -- endnote_debt sees this
  APPOS-VERB  Name, <interposed phrase>, <any verb>  -- MISSED by endnote_debt
  BARE-VERB   Name <any finite-looking verb>         -- MISSED if verb unlisted
  OPEN        sentence-initial                       -- weak; often furniture
  OTHER       object, prepositional, listed, unclear -- weakest

A name whose ONLY sites are OPEN/OTHER is probably subject matter, not a source.
A name with an APPOS-VERB or BARE-VERB site and no POSS/VERB site is exactly the
population endnote_debt cannot see, and is what this tool exists to surface.

WHAT THIS CANNOT DO, printed every run: it cannot tell an authority from a
historical actor, and it does not try. `Ambrose` reading in his cell and
`McGilchrist` concluding something look identical to a regular expression. That
judgement is the reader's, which is why every site is printed verbatim.

Usage:
    python tools/name_census.py V                 # a whole book
    python tools/name_census.py V-02              # one chapter
    python tools/name_census.py V --unseen-only   # only names endnote_debt misses
"""

import re
import sys
import pathlib
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"

sys.path.insert(0, str(ROOT / "tools"))
# Reuse the precision instrument's own vocabulary rather than re-deriving it.
# A second copy of OPENERS would drift from the first, and the drift would be
# invisible: both files would keep running.
from endnote_debt import (                                    # noqa: E402
    OPENERS, CALENDAR, NAME_TOK, AUX, ATTRIB_VERB,
    CHAPTER_RE, SENT_SPLIT, split_prose_notes, strip_furniture,
    clean_name, non_person_class, common_noun_counts, scan_prose,
)

CAP_SEQ = re.compile(r"\b[A-Z][a-zA-ZÀ-ſĀ-ſ.'’-]{2,}(?:\s+[A-Z][a-zA-ZÀ-ſĀ-ſ.'’-]+){0,2}")

# A verb-ish token. Deliberately loose: this is the RECALL instrument, and the
# cost of a false verb is a row a human dismisses in two seconds. The cost of a
# missed one is a source that never gets a receipt.
VERBISH = re.compile(
    r"\b(?:[a-z]{3,}(?:s|es|ed|ing)|is|was|were|are|has|had|says|said|holds|held|"
    r"took|takes|gave|gives|made|makes|went|goes|saw|sees|knew|knows|"
    r"put|puts|rules?|ruled|found|finds|meant|means|kept|keeps|left|leaves)\b"
)

APPOS = re.compile(
    rf"({NAME_TOK})\s*,\s*(?P<mid>[^,;.]{{3,120}})\s*,\s*(?P<v>{VERBISH.pattern})"
)
BARE = re.compile(rf"\b({NAME_TOK})\s+(?P<v>{VERBISH.pattern})")
POSS = re.compile(rf"\b({NAME_TOK})(?:’s|'s)\s+[*_]*[a-z]")
VERB_P = re.compile(rf"\b({NAME_TOK})(?:’s|'s)?{AUX}\s+(?:{ATTRIB_VERB})\b")
ACCORD = re.compile(rf"(?:according to|per|following)\s+({NAME_TOK})\b")

# order matters: strongest evidence first, so a site is labelled by its best class
CLASSES = [("POSS", POSS), ("VERB", VERB_P), ("ACCORDING", ACCORD),
           ("APPOS-VERB", APPOS), ("BARE-VERB", BARE)]
SEEN_BY_DEBT = {"POSS", "VERB", "ACCORDING"}


def chapters(sel):
    out = []
    for p in sorted(BOOK.glob("*.md")):
        m = CHAPTER_RE.match(p.name)
        if not m:
            continue
        tag = f"{m.group('book')}-{m.group('n')}"
        if sel and not (tag == sel.upper() or m.group("book") == sel.upper()):
            continue
        out.append((tag, p))
    return out


def census_chapter(path):
    text = path.read_text(encoding="utf-8")
    prose, _notes = split_prose_notes(text)
    flat = strip_furniture(prose)
    lower = common_noun_counts(flat)
    flat = re.sub(r"\s+", " ", flat.replace("\n", " "))

    names = defaultdict(lambda: {"display": "", "sites": [], "classes": Counter()})
    for sent in SENT_SPLIT.split(flat):
        # every capitalized sequence, with the offset it starts at
        for m in CAP_SEQ.finditer(sent):
            cn = clean_name(m.group(0))
            if not cn:
                continue
            display, surname = cn
            if surname in CALENDAR or surname in OPENERS:
                continue
            # classify THIS occurrence by the strongest construction it sits in
            klass = "OPEN" if m.start() == 0 else "OTHER"
            for label, pat in CLASSES:
                for mm in pat.finditer(sent):
                    got = clean_name(mm.group(1))
                    if got and got[1] == surname:
                        klass = label
                        break
                if klass == label:
                    break
            rec = names[surname]
            if len(display) > len(rec["display"]):
                rec["display"] = display
            rec["classes"][klass] += 1
            if len(rec["sites"]) < 6:
                rec["sites"].append((klass, sent.strip()[:190]))

    # annotate rather than drop
    for surname, rec in names.items():
        rec["lower_twin"] = lower[surname.lower()]
        rec["nonperson"] = non_person_class(surname, rec["display"]) or ""
        rec["debt_visible"] = any(c in SEEN_BY_DEBT for c in rec["classes"])
        rec["has_action"] = any(
            c in ("POSS", "VERB", "ACCORDING", "APPOS-VERB", "BARE-VERB")
            for c in rec["classes"]
        )
    return names


def main():
    sel = next((a for a in sys.argv[1:] if not a.startswith("-")), "")
    unseen_only = "--unseen-only" in sys.argv
    chs = chapters(sel)
    if not chs:
        print(f"no chapters match {sel!r}")
        return 2

    print("NAME CENSUS — recall-first. Every capitalized candidate, nothing dropped.")
    print(f"  {BOOK}   selector={sel or 'ALL'}")
    print("  ⛔ THIS TOOL DOES NOT DECIDE SOURCE-HOOD. It cannot tell an authority")
    print("     from a historical actor. Sites are printed so a reader judges.")
    print()

    grand_action = grand_unseen = 0
    for tag, path in chs:
        names = census_chapter(path)
        debt_src, *_ = scan_prose(strip_furniture(split_prose_notes(
            path.read_text(encoding="utf-8"))[0]))
        # ⛔ NO has_action FILTER HERE, and the reason is a defect this tool
        # SHIPPED WITH for one run. `if not rec["has_action"]: continue` looked
        # like tidying: a name with no verb and no possessive is surely a
        # mention. It ate Sam Harris out of V.4 -- the New Atheism chapter --
        # because his one site is `Harris's, and the sharpest of the four`,
        # where the possessive is followed by a COMMA, so the POSS pattern
        # (which wants a lowercase letter) does not fire and the site falls to
        # OTHER. A named horseman of the chapter's own subject, dropped by the
        # recall instrument, three paragraphs below its docstring's warning
        # that a noise filter drops true positives sharing the noise's shape.
        # Mentions are now a BAND, not an exclusion.
        rows, mentions = [], []
        for surname, rec in sorted(names.items()):
            in_debt = surname in debt_src
            if unseen_only and in_debt:
                continue
            (rows if rec["has_action"] else mentions).append((surname, rec, in_debt))
        acting = sum(1 for r in names.values() if r["has_action"])
        unseen = sum(1 for s, r in names.items()
                     if r["has_action"] and s not in debt_src)
        grand_action += acting
        grand_unseen += unseen
        print(f"── {tag}  ·  {acting} acting candidate(s) · endnote_debt sees "
              f"{len(debt_src)} · {unseen} NOT SEEN BY IT")
        for surname, rec, in_debt in rows:
            flags = []
            if rec["lower_twin"] >= 2:
                flags.append(f"lower-twin×{rec['lower_twin']} (debt DROPS this)")
            if rec["nonperson"]:
                flags.append(f"class={rec['nonperson']} (debt DROPS this)")
            mark = "·seen·" if in_debt else "⚠ UNSEEN"
            cls = " ".join(f"{k}×{v}" for k, v in rec["classes"].most_common())
            print(f"   {mark}  {rec['display']:<26} {cls}"
                  + (f"   [{'; '.join(flags)}]" if flags else ""))
            for klass, site in rec["sites"]:
                if klass in ("OPEN", "OTHER"):
                    continue
                print(f"            {klass:<10} {site}")
        if mentions:
            print(f"   MENTION-ONLY ({len(mentions)}) — no verb, no possessive-noun."
                  " Mostly furniture; Harris lived here.")
            for surname, rec, in_debt in mentions:
                mark = "·seen·" if in_debt else "⚠"
                print(f"   {mark}  {rec['display']:<26} "
                      f"{' '.join(f'{k}×{v}' for k, v in rec['classes'].most_common())}")
                print(f"            SITE       {rec['sites'][0][1]}")
        print()

    print(f"TOTAL acting candidates: {grand_action} · unseen by endnote_debt: "
          f"{grand_unseen}")
    print("⚠ 'unseen' is a RECALL GAP, not a debt figure. Some are historical")
    print("  actors and characters; the reader converts this list into a roster.")
    print("⚠ AND 'unseen' IS A FLOOR, for a reason worth stating: the endnote_debt")
    print("  comparison above is run CHAPTER-LOCAL, with no corpus frequency table,")
    print("  so it credits that tool with names its real full-book run drops (`God`")
    print("  in V.2 is one). Every such name is counted here as SEEN when it is in")
    print("  fact invisible. The gap can therefore only be larger than printed.")
    print("⚠ AND THE DENOMINATOR IS THIS TOOL'S OWN EXTRACTION. A percentage")
    print("  computed from it measures the two regexes against each other, not")
    print("  either against the prose. Only a hand roster settles that.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
