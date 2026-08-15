# SCAN-005 — Master Revision Queue v2.0: coverage measurement

> ## ⛔ CORRECTION — Day 196, later the same day. §1 and the Disposition are WRONG.
>
> Clayton supplied the fact this scan lacked: **Fable and Gemini Spark read the entire
> volume from the PDF — every book, both codas.** Re-measured all 146 items instead of the
> 4 sampled, bucketed by locus and by block:
>
> | book | 001–076 (Fable's synthesis of Gemini's first pass) | 077–146 (Gemini's completion) | ⛔ in book |
> |---|---|---|---|
> | I | 0 | 0 | 0 |
> | II | 5 | 1 | 0 |
> | III | 3 | 1 | 0 |
> | IV | 11 | 10 | 27 |
> | V | 13 | 49 | 87 |
> | VI | 10 | 0 | 0 |
> | VII | 18 | 2 | 0 |
> | VIII | 12 | 3 | 21 |
> | C | 1 | 1 | 3 |
>
> **The ⛔-mirror finding is true of block 2 only** — 59 of its 70 items land in the two
> ⛔-heavy books. **Block 1 spans the whole volume, including 38 items in II/III/VI/VII
> where the book carries no stop-marks at all.** Items 026 (Wernicke 1874 as anatomical
> landmark, VI.2), 027 (Eisenstein vs Adrian Johns on print fixity, VI.4), 030 (Nagel
> dual-citation, II.3/VII.3), 035 (Parfit *Reasons and Persons* Part III anchor, VII.9) are
> outside-source checks the book's own register could not have generated — 026 targets a
> ⚠ receipt, not a ⛔. **The outside aperture is real and it was spent.**
>
> **My error was the sample.** All four items I checked came from Sections 7–8 — i.e. all
> four from block 2, the one block that *is* a ⛔ extraction — and I generalised to the file.
> A sample drawn entirely from where the two hypotheses agree. §3's numbers stand as a fact
> about the *book's own* ⛔ register: 235 endnotes in II/III/VI/VII carry 1 stop-mark between
> them, and that register is still the audited half. But "ask them what the book cannot tell
> them" was already answered before I asked it.
>
> **Also superseded: the release framing.** The volume was released 2026-08-15 ~13:36 local
> (public repo + PhilPapers record). This is an errata register for v1.1, not a gate.

**Day 196 / 2026-08-15.** Subject: `Master Revision Queue.txt` (146 items, synthesized
15 Aug 2026 by Fable + Gemini Spark from a full-volume read), delivered by Clayton.
Question asked: not "are the items right" but **"what surface does this queue cover, and
what does it therefore certify?"** — because Section 12 of the file is a release sign-off
gate, and a gate's coverage is the thing that has to be measured before its verdict means
anything.

## 1. The new items are largely the book quoting itself

Items 001–076 are `[CARRIED]` from the retired internal v1.0 register (52 explicit
`[CARRIED]` tokens). Items 077–146 present as new. Sampled 4 of the sharpest
concrete-locus items in Section 7/8 against the current book text:

| item | claim | in book |
|---|---|---|
| 085 | V.6 body says tzimtzum "twelfth century" | body string live; endnote `[^11]` **already argues** the tradition barely exists in the 12th c. |
| 091 | V.7 Dee "rest of his life" | body string live; endnote `[^14]` **already** ⛔ "is false … 1582 to 1589 — seven years, not a remainder." |
| 092 | V.8 "eighth among the ten" | ⛔ note **already** works the ordinal out; note reads *"the draft read"* — partially paid |
| 132 | V.11 "its ninth paragraph" | body string live; endnote `[^6]` **already** ⛔ "does not resolve." |

4 of 4 findings were already written, in the book's own voice, in ⛔-marked endnotes.
This is an **extraction of the OWED/⛔ register**, not an outside read. That is genuinely
useful — 140 ⛔ notes scattered across 71 files, gathered into one addressable list with
dispositions, which had not been done. It is not an external aperture and must not be
graded as one.

## 2. The coverage map is a photograph of the ⛔ register

Concrete defect items (085–134, n=50), bucketed by book, against ⛔ counts in the body:

| book | queue items | ⛔ in book |
|---|---|---|
| V | 44 | 87 |
| IV | 6 | 27 |
| I, II, III, VI | **0** | **0** |

Zero queue items land in any chapter that had no pre-existing ⛔ mark. The queue found
nothing the book had not already flagged about itself.

## 3. The register it extracts is itself sampled — and that is the release risk

⛔ density per endnote, whole volume:

| book | files | endnotes | ⛔ | ⛔/endnote |
|---|---|---|---|---|
| I | 6 | 0 | 0 | — |
| II | 8 | 41 | 0 | 0.00 |
| III | 8 | 46 | 0 | 0.00 |
| IV | 10 | 76 | 27 | 0.36 |
| V | 11 | 168 | 87 | 0.52 |
| VI | 8 | 59 | 0 | 0.00 |
| VII | 9 | 89 | 1 | 0.01 |
| VIII | 7 | 43 | 21 | 0.49 |
| C | 2 | 5 | 3 | 0.60 |

Where the auditor looked (IV, V, VIII, C): **0.47 ⛔ per endnote.**
Where it did not (II, III, VI, VII): **235 endnotes, 1 ⛔ between them — 0.004.**

**The "written earlier, before the convention" explanation is refuted.** All eight books
were last touched 2026-08-14; per-book commit counts are comparable (I:13, II:32, III:20,
IV:33, V:38, VI:21, VII:28, VIII:34). Book VI carries *more* endnotes than Book VIII (59 vs
43) and 21 fewer stop-marks. The asymmetry tracks where the audit went, not when the prose
was written.

This is **not** a claim that ~110 defects exist in II/III/VI/VII. It is a claim that
**235 endnotes have not been audited**, and that a gate built on the ⛔ register cannot
distinguish "clean" from "never swept" there — while Section 12 renders the distinction
invisible by signing off five stages as a complete pre-release gate.

## 4. Disposition

- **Keep** the file as an extraction index of the OWED/⛔ backlog. It is the best one that exists.
- **Do not** run it as a release gate. Its coverage is the audited half of the volume.
- **Next real work**: sweep II / III / VI / VII — 235 endnotes, the largest unmeasured
  surface in the book. Until that number moves, no gate can certify release.
- Outside-aperture value from Fable and Gemini Spark is **unspent**: they reported the
  book's own notes back. Ask them what the book cannot tell them — the unswept books.

*Measurement only. No book text was modified by this scan.*
