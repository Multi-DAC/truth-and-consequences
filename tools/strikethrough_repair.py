#!/usr/bin/env python3
"""R-58 — repair the correction idiom so it survives plain text.

WHY: `~~Ten~~ **ELEVEN**` renders correctly in a Markdown viewer and transmits as
"Ten ELEVEN" — or, through a tilde-stripping pipeline, simply "Ten" — in a paste
into a chat client, a plain-text packet, or a fast scan. A superseded claim that
renders as live is worse than a stale one: it reads as current AND correct.

The defect is a property of the TRANSMISSION, not the text, so the author cannot
see it from inside. The repair is therefore not cosmetic: every retraction gets a
WORD carrying its semantics, so that stripping the markup loses decoration only.

DELIVERABLE IS THE DELTA. This script prints every substitution it makes and
refuses to run if any pattern does not match exactly once. A silent success is
the failure mode.

SCOPE, DECLARED: the four planning documents only. book/docs/REVISION-QUEUE.md's own
20 strikethroughs are `~~**R-n**~~ ✅ **PAID**` row-discharge markers, which
transmit correctly in plain text because the ✅/PAID token carries the semantics;
and four of them sit INSIDE R-58's own text, where they are the specimen. Editing
those would destroy the evidence for the row. Left deliberately, not overlooked.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (file, old, new, why-the-plain-text-form-was-broken)
REPAIRS = [
    # ---- 00-ARCHITECTURE.md ----------------------------------------------
    ("00-ARCHITECTURE.md",
     "the fork is ~~III.1's~~ II.1's.",
     "the fork is II.1's, NOT III.1's.",
     "SUPERSESSION: read as 'the fork is III.1's II.1's' — two owners, no winner"),

    ("00-ARCHITECTURE.md",
     "~~III.1~~ **II.1**",
     "**II.1** (NOT III.1 — superseded)",
     "SUPERSESSION x2: read as 'III.1 II.1'"),

    ("00-ARCHITECTURE.md",
     'for a player to be returned to ~~— the player is one of the states the whole game contains~~."*',
     'for a player to be returned to."*  **The cut clause, kept here as the record of the deletion:**\n*"— the player is one of the states the whole game contains"*',
     "EXCISION INSIDE A QUOTATION: the deleted clause read as part of the shipped quote — "
     "the worst instance, because the prose two lines up says 'One deletion, no replacement'"),

    ("00-ARCHITECTURE.md",
     "1. ~~Book II's vocabulary~~ — **DONE**",
     "1. Book II's vocabulary — ✅ **DONE**",
     "DONE-MARKER: safe in plain text, normalised for one convention"),

    ("00-ARCHITECTURE.md",
     "2. ~~The per-book chapter maps~~ — **DONE**",
     "2. The per-book chapter maps — ✅ **DONE**",
     "DONE-MARKER: safe in plain text, normalised"),

    ("00-ARCHITECTURE.md",
     "6. ~~Add Watts and Borges to `03-THE-ANCESTORS.md`~~ — **DONE.**",
     "6. Add Watts and Borges to `03-THE-ANCESTORS.md` — ✅ **DONE.**",
     "DONE-MARKER: safe in plain text, normalised"),

    ("00-ARCHITECTURE.md",
     "C17, DEATH — ~~the next doctrinal ruling~~ → REASSIGNED",
     "C17, DEATH — *(retracted: “the next doctrinal ruling”)* → REASSIGNED",
     "RETRACTION: read as a live designation followed by its own reassignment"),

    ("00-ARCHITECTURE.md",
     "~~Mechanical, one sitting.~~ It is what turns",
     "*(retracted estimate: “Mechanical, one sitting.”)* It is what turns",
     "RETRACTED ESTIMATE, no marker word on the line: read as a live cost estimate"),

    ("00-ARCHITECTURE.md",
     "⚠ ~~**COPY, DON'T REFERENCE.**~~ **SUPERSEDED Day 186 by ruling 8.**",
     "⚠ **SUPERSEDED Day 186 by ruling 8** — *the retracted heading read “COPY, DON'T REFERENCE.”*",
     "RETRACTED IMPERATIVE: read as a live standing instruction. Named in R-58 as load-bearing"),

    # ---- 05-THE-LEXICON.md ------------------------------------------------
    ("05-THE-LEXICON.md",
     "| ~~**the Narrowing**~~ | **RETIRED**",
     "| **the Narrowing** | **RETIRED**",
     "TABLE CELL: adjacent RETIRED cell carries it; tildes are decoration only"),

    ("05-THE-LEXICON.md",
     "## 7. ~~OPEN — Clayton's to rule~~ → **CLOSED, Day 185.**",
     "## 7. *(was: OPEN — Clayton's to rule)* → **CLOSED, Day 185.**",
     "HEADING: read as 'OPEN ... CLOSED' — a section that is both"),

    # ---- 06-THE-SCAFFOLD.md -----------------------------------------------
    ("06-THE-SCAFFOLD.md",
     "**the fork is ~~III.1's~~\nII.1's**",
     "**the fork is II.1's, NOT III.1's**",
     "SUPERSESSION ACROSS A LINE BREAK: read as 'the fork is III.1's II.1's'"),

    ("06-THE-SCAFFOLD.md",
     "~~Ten~~ **ELEVEN** chapters",
     "**ELEVEN** chapters (NOT ten — amended)",
     "SUPERSEDED COUNT: read as 'Ten ELEVEN chapters'. THE INSTANCE THAT FOUND THE ROW — "
     "a reviewer read it as 'the scaffold still says ten chapters' and was right about the channel"),

    ("06-THE-SCAFFOLD.md",
     "**2. ~~Three~~ FOUR chapters carry the whole work",
     "**2. FOUR chapters — not three — carry the whole work",
     "SUPERSEDED COUNT: read as 'Three FOUR chapters'"),

    ("06-THE-SCAFFOLD.md",
     "- **~~III.1~~ II.1** — lose the reader",
     "- **II.1, NOT III.1** — lose the reader",
     "SUPERSESSION: read as 'III.1 II.1'"),

    ("06-THE-SCAFFOLD.md",
     "1. ~~Book II's vocabulary~~ → **DONE**",
     "1. Book II's vocabulary → ✅ **DONE**",
     "DONE-MARKER: safe in plain text, normalised"),

    ("06-THE-SCAFFOLD.md",
     "2. ~~Per-book chapter maps~~ → **DONE**",
     "2. Per-book chapter maps → ✅ **DONE**",
     "DONE-MARKER: safe in plain text, normalised"),

    ("06-THE-SCAFFOLD.md",
     "3. ~~**III.1 in full** — the highest-priority single paragraph in the plan~~ → **SUPERSEDED",
     "3. *(was: **III.1 in full** — the highest-priority single paragraph in the plan)* → **SUPERSEDED",
     "RETRACTED PRIORITY: read as a live top-priority item that is also superseded"),

    # ---- 07-THE-CLAIMS-REGISTER.md ----------------------------------------
    ("07-THE-CLAIMS-REGISTER.md",
     "~~**Status remains UNSET. What changed is the instrument, not the answer.**~~",
     "**[SUPERSEDED Day 186 — the ★ ruling immediately below replaces this]** "
     "*Status remains UNSET. What changed is the instrument, not the answer.*",
     "SUPERSEDED STATUS, NO MARKER ON THE LINE: read as the live status of the claim. "
     "Named in R-58 as load-bearing"),

    ("07-THE-CLAIMS-REGISTER.md",
     "~~The next doctrinal ruling the work needs.~~ **REASSIGNED",
     "*(retracted: “The next doctrinal ruling the work needs.”)* **REASSIGNED",
     "RETRACTION: read as a live designation"),

    ("07-THE-CLAIMS-REGISTER.md",
     "3. ~~**★ The C6 × C7 collision has no home.**~~ **CLOSED Day 187",
     "3. **★ The C6 × C7 collision has no home.** — **CLOSED Day 187",
     "DONE-MARKER: CLOSED carries it; tildes are decoration only"),
]


def main():
    apply = "--apply" in sys.argv
    print("=" * 78)
    print("R-58 — STRIKETHROUGH REPAIR" + ("  [APPLYING]" if apply else "  [DRY RUN]"))
    print("=" * 78)

    bodies, failures, applied = {}, [], 0
    for fname, old, new, why in REPAIRS:
        path = ROOT / fname
        if fname not in bodies:
            bodies[fname] = path.read_text(encoding="utf-8")
        n = bodies[fname].count(old)
        if n == 0:
            failures.append(f"NO MATCH  {fname}: {old[:60]!r}")
            continue
        bodies[fname] = bodies[fname].replace(old, new)
        applied += n
        print(f"\n[{n}x] {fname}")
        print(f"   WHY : {why}")
        print(f"   WAS : {old[:100]!r}")
        print(f"   NOW : {new[:100]!r}")

    print("\n" + "-" * 78)
    if failures:
        print("REFUSING TO WRITE — patterns did not match:")
        for f in failures:
            print("   " + f)
        return 1

    print(f"{applied} substitution(s) across {len(bodies)} file(s).")

    if apply:
        for fname, body in bodies.items():
            (ROOT / fname).write_text(body, encoding="utf-8")
        print("WRITTEN.")
        # residual count, stated
        for fname in bodies:
            rest = (ROOT / fname).read_text(encoding="utf-8").count("~~")
            print(f"   residual ~~ tokens in {fname}: {rest // 2}")
    else:
        print("Dry run. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
