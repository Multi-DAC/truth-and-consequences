# SCAN-003 — cross-chapter citation rot, first run

**Day 192 · 2026-08-11 · `tools/crossref_rot.py` · closes R-148 (instrument), opens R-151 (finding)**

Raw output: `SCAN-003-day192-crossref-rot-raw.txt` (`--all`, 992 lines).

---

## What was measured

For every chapter-to-chapter reference in the book, whether the chapter it cites acquired a
**corrective endnote after the citing line was last written**. The test is temporal and it comes
out of `git blame`, not out of a similarity score:

> the citing line's last commit date **<** the corrective note's commit date
> ⇒ the citation was drafted against an uncorrected body.

Lexical overlap appears only as a `*` ranking mark inside the flagged set. It never gates. Gating
on overlap is precision eating recall — a defect already on file — and a threshold tuned by the
author is a threshold tuned until it agrees with the author.

## The numbers

| | |
|---|---|
| chapters in corpus | 69 (67 + coda 2) |
| excluded as *prose about chapters* | `DRAFT-LOG.md` (2052 dotted refs), `REVISION-QUEUE.md` (922) |
| references resolved | **490** — 337 dotted, 92 *previous chapter*, 38 *next chapter*, 23 descriptive |
| endnotes defined | 353, of which **58 corrective** (37 by ⛔, 21 by lexicon) across 23 chapters |
| **TIER 1** — citation predates a ⛔ note in the chapter it cites | **55** |
| TIER 2 — predates a lexicon-corrective note, no ⛔ | 6 |
| TIER 3 — every corrective note predates the citation | 137 |
| unmeasured (missing blame date) | 0 |

**It did not read zero, and R-148 predicted it would.** The row was filed with the warning *"it
reads `0` the day it is written and that is not evidence of health."* It read 61. The positive
control is still what licenses the number — without it a zero and a sixty-one would be equally
uninterpretable.

**POSITIVE CONTROL: PASS.** IV.10:268 → IV.9 [^12], *"two confident numbers"* — cited 2026-08-07,
note landed 2026-08-10. The pair the row was filed from is caught by the gauge built from it.

## Where the rot is

| direction | flagged citations |
|---|---|
| **IV → IV** | 37 |
| **V → IV** | **12** |
| VII → IV | 4 |
| III → III | 3 |
| VII → III | 2 |
| VI → VIII, IV → VIII, II → II | 1 each |

Most-cited chapters carrying corrections newer than their citers: **IV.7 (20), IV.6 (11), IV.8 (8),
IV.10 (7), IV.9 (7), III.5 (5)**.

★ **R-148's prediction was directionally right and numerically over.** It said *"Book V will cite
Book IV forty times and every one of those references is being drafted against uncorrected bodies."*
Measured: **12 flagged**, out of a larger V→IV reference population most of which lands in tier 3.
The mechanism was real; the magnitude was an estimate wearing a count's clothes.

## Discrimination — is the test doing any work?

A fair objection: every Book IV body dates 2026-08-07 and every Book IV note dates 08-10/08-11, so
does the temporal test just re-report *"the retrofit happened after the drafting"*?

Partly, and the honest ratio is **61 flagged : 137 not**. It separates roughly 2.4 to 1, so it is
not degenerate — but its resolution **within a single retrofitted book is low**, and the `*` term
overlap is the only thing ordering the 37 IV→IV rows. Treat the ranking as a reading order, not a
severity scale.

## What it cannot see

- Citations phrased without a resolvable handle — *"as we saw earlier"*, *"the atlas"* — are
  invisible. 490 is what it can resolve, not what exists.
- 10 title tokens are **ambiguous** across chapters (`census` → IV.1 *and* IV.10; `tunnel` → II.5,
  VI.6, VI.8) and are skipped rather than guessed. Reported, not dropped silently.
- The test asks **when**, never **what**. A citing line touched after the note landed — for a typo,
  a rewrap, an unrelated edit — leaves tier 1 silently and forever.
- **Books I and V carry zero endnotes**, so no reference *into* them can ever flag. That is an
  absence of instrument, not an absence of rot. Book V's own pass has never run.

## The one that was read

`V.9>IV.10:a3823532` — hand-checked, and it is not clean. **Filed as R-151.**
