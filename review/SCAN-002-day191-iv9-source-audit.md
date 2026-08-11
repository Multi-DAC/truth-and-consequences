# SCAN-002 — IV.9'S SOURCE AUDIT, AUDITED

**Day 191, 2026-08-10, night. Found during the R-2 endnote retrofit of IV.9.**
Source of record: `work/perspective-v1-fulltext.txt` (884 KB), the cache `tools/brief_source.py:70`
names as THE source. Chapter's declared Source line: *"ecology Tier 4.1–4.2"* (`06-THE-SCAFFOLD.md`).

---

## §0 — WHAT THIS IS

IV.9's last section — *"Where the inherited apparatus cannot decide, and it is legible in its own
numbers"* — is the chapter's sharpest move: it audits the framework material the book inherits and
reports that the source's **own scores contradict its own prose**. `DRAFT-LOG.md:5094` files it under
a ★ and calls it *"only visible to somebody using the apparatus rather than admiring it."*

**One of its three numbers is verbatim correct. The other two are not in the source file, and neither
is the ✔ CHECKED-AND-CLEAN null recorded beside them.**

This is not a claim that the chapter's conclusion is wrong. It is a claim that the conclusion is
**resting on evidence that cannot be checked against the source this project holds** — while a
better version of the same evidence sits in the file, unused.

---

## §1 — THE THREE CLAIMS, MEASURED

| # | Chapter's claim (`IV-09`) | Measured against the cache | Verdict |
|---|---|---|---|
| 1 | Archetypes rated **moderate** on the dimension defined as *"coherence with subjective experience, awareness, phenomenal consciousness"* | §4.1 profile line reads `moderate Cognitive-Experiential`; the definition at line 2286 is **verbatim** as quoted | ✅ **CONFIRMED** |
| 2 | The **Promethean entry** is scored **maximal** on the dimension defined as *"the dimension that distinguishes entities that navigate from entities that are navigated through"* | The **definition is verbatim correct** (Volitional-Intentional, line 2346–2348). But **§4.2 carries no `Dimensional profile:` line at all** — it has no scores of any kind. §4.1 does not score Volitional-Intentional either. | ⛔ **NOT IN SOURCE** |
| 3 | *"Archetypes are marked **S**, and so are minerals."* | **3** `Orientation:` lines exist in the entire 884 KB file; all three are in the **Decomposers** section (Divine `V`, Trickster `N`, Intimate `S`). Neither §4.1 (Archetypes) nor §1.1 (Mineral/Elemental) carries one. | ⛔ **NOT IN SOURCE** |
| 4 | `DRAFT-LOG.md:5110`, recorded as a checked null: *"the same profile prints `PT` at maximum beside prose reading zero Physical-Spatial"* | **3** lines in the whole file contain bar-glyphs (`■`/`□`), all three in Decomposers. The string `PT` appears in no profile. **§4.1 has no bar-profile to print anything.** | ⛔ **NOT IN SOURCE** |

### The positive control, because a null is worthless without one
Bar-profiles and `Orientation:` lines **do survive** into the cache — three of each, intact, glyphs
and all, at lines 3897 / 3906 / 3913. So their absence from §4.1 and §4.2 is not an extraction
artefact of *that notation*. The field grammar is also consistent and countable: `Dimensional
profile:` ×17, `Ecological role:` ×22, `Evidence basis:` ×15, `Orientation:` ×3. §4.2 is one of the
entries with **no** profile line — formatted deliberately as *"A special case:"* rather than as a
scored entry.

### What this does NOT establish
`brief_source.py:71` names the real drafting tree as `Unreleased-Work/Perspective`. **That tree is
not present on this machine** (searched both user roots and the repo store). If a fuller rendering
exists there with per-entity bar-profiles and orientation letters, claims 2–4 could be correct and
merely *uncheckable from here*. I cannot distinguish "the drafter read a fuller table" from "the
drafter filled a plausible one" — and that is precisely the point: **neither can a reader.**

---

## §2 — THE FINDING IS TRUE, AND THE FILE HOLDS BETTER EVIDENCE FOR IT

The chapter says: *"One letter is doing two incompatible jobs."* **It is** — and the collision is not
between two entity-assignments (which do not exist). It is between the source's **two definitions of
the letter itself**:

> **Guide §1.4, line 8402:** *"Structural (S): Orientation toward the architecture of the space itself
> rather than toward expansion or contraction. Not moving through the landscape but understanding its
> topology. In human experience: analysis, contemplation, mathematical reasoning, systematic
> investigation."*

> **Appendix table, line 9889:** *"S (Structural) — **Forms the landscape itself**."*

The first is a **stance a navigator takes**: a human doing mathematics is `S`. The second is **being
terrain**, which is not a navigator at all. One letter, two incompatible jobs — the chapter's exact
claim, verbatim from the source, in a form a reader can check.

**And the pointer that goes nowhere.** Line 8412:

> *"See also: **Ecology Part II for orientation assignments (E+, E−, V, N, S) across all entity
> types**"*

Ecology Part II — the Taxonomy of Beings, lines 2357 ff. — **contains no orientation assignments at
all.** The cross-reference promises a table that was never built. That is
*mechanism-without-a-trigger* — this codebase's signature defect and this book's recurring one —
sitting inside the source the book inherits, and it is a **better** instance of the chapter's thesis
than the numbers the chapter used: the apparatus could not report that the assignment was missing,
so it cited it instead.

---

## §3 — WHY THIS SURVIVED A DRAFT AND A LOG ENTRY

The section audits **somebody else's** apparatus. Every discipline this book has built for checking
quotations is aimed at claims that *flatter the framework* or that the chapter *depends on*. This one
did neither — it scored against the source, in the book's favour, and read as housekeeping.

That is [[feedback_scrutiny_is_motive_shaped]] exactly: the asymmetry is not that flattering errors
survive, it is that **unlooked-at** errors survive, and an error inside a section whose whole posture
is "I am being rigorous about my source" is as unlooked-at as they come. The ★ and the ✔ in the log
are the tell — a finding was graded, and the grading was of the *argument*, never of the *lookup*.

⛔ **And the ✔ is the worst part.** `DRAFT-LOG.md:5110` records a **null as verified** — *"CHECKED AND
CLEAN, recorded because a null needs saying"* — for a `PT` value that is not in the file. A
false negative wearing a measurement's clothes is worse than an unchecked claim, because it
retires the question. See [[feedback_zero_needs_a_positive_control]].

---

## §4 — WHAT IS OWED

1. **IV.9's last section must be re-grounded or re-graded.** The `S`/`S` collision and the dead
   cross-reference (§2 above) replace claims 2–4 with checkable ones and make the section *stronger*.
   Filed as a REVISION-QUEUE row, not repaired here — the retrofit's job is the note, not the rewrite.
2. **Retract the ✔ at `DRAFT-LOG.md:5110`.** It certifies a measurement that did not happen.
3. ★ **Generalise, because this is a class, not an instance.** Every chapter that audits the inherited
   source by quoting its *scores* is exposed the same way. `brief_source.py` checks that a cited
   phrase EXISTS in the cache; **nothing checks that a quoted NUMBER does.** A sweep for
   score-quotations across the 67 chapters has never run and has no hand. That is the R-108 shape
   again — a clause with no instrument.
4. **Locate `Unreleased-Work/Perspective` or declare it unreachable in writing.** The project cites a
   tree it does not hold. Until then every source-score claim in the book is assertion-grade at the
   level of a table nobody can open.
