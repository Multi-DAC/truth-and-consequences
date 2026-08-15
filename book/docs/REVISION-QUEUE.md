# REVISION QUEUE — Truth and Consequences

**RESET Day 195 / 2026-08-14, on Clayton's ruling.** The previous queue is retired whole at
`book/docs/archive/REVISION-QUEUE-RETIRED-D195.md` — 6,391 lines, 229 rows, 206 of them live. It is
kept, it is searchable, and **it is not to be worked from.**

---

## WHY IT WAS RETIRED RATHER THAN SPLIT

Clayton's words: *"instead of splitting the old queue, we retire it and start a new one on fresh
reads of the updated PDF. Then we will know what is actually left to do."*

The reason that is right, stated so it survives being forgotten: **a queue row is a measurement, and
it rots.** Eleven rows were closed on Day 195 and nearly every one had a working machine underneath
a stale description — a row citing *"goal rows ranked 14–19"* where the store returned nothing at
all, a docstring promising a guarantee no longer in the file, a test called hanging that finished in
99 seconds against a number somebody typed once. Every one was true when written. None was true when
read. **A row that has rotted looks exactly like a fresh one**, and a 206-row backlog is 206 chances
to spend an evening repairing a defect that is no longer there.

⛔ **AND RETIRING IT REALLY DOES DROP THINGS.** This is a cost, not a free move. The rows below are
carried by hand because a fresh read of the prose is *structurally incapable* of recovering them —
their subject is not in the book. Anything else in the archive that a reader cannot find is gone,
and that is the trade being made deliberately: **for a volume about to ship, reader-visible is the
standard.** [[feedback_freshness_check_cannot_see_a_deletion]]

---

## COVERAGE — THE GAUGE THAT COMES BEFORE THE FIRST FINDING

⛔ **AN EMPTY QUEUE READS EXACTLY LIKE A FINISHED BOOK.** There is no visual difference between
*nothing is wrong* and *nobody has looked*. So coverage is measured before anything is filed:

```
python tools/fresh_read.py            # coverage, and the UNREAD list is the loud half
python tools/fresh_read.py --read IV.10 --by clawd
python tools/fresh_read.py --carry    # the archived rows a fresh read cannot re-find
```

**As of the reset: 0 of 71 chapters read. 323,746 words. Nothing has been looked at yet.**

The unit is the **compiled PDF**, not the markdown — the reader gets the volume, so the read is
against `book/pdf/Truth-and-Consequences.pdf` (1,074 pages, built 2026-08-14 20:59) and the chapter
map is parsed from that PDF's own table of contents, page numbers included. Reading the markdown is
a different act with different findings and does not count.

⚠ **The map is checked in BOTH directions** — every chapter file must appear in the PDF and every
TOC entry must exist on disk — and coverage is **refused**, not reported, when they disagree. That
control has already earned itself: the first run of the parser silently dropped the seven chapters
whose titles are long enough to wrap across two lines in the rendered contents, and it was the
control that caught it rather than a reader, because a one-directional check would have printed
62/71 and looked fine.

⚠ **What the gauge cannot do:** it cannot tell an attentive read from a careless one. It records
that a chapter was marked read, by whom, on what date, and **against which PDF build** — a read
against a superseded build is flagged, because it is not a read of the current artefact.

---

## RELEASE GATES — CARRIED FORWARD UNCHANGED. THESE BLOCK UPLOAD; NOTHING ELSE DOES.

| # | Gate | Row | State |
|---|------|-----|-------|
| 1 | Ruling 177 written and the sweep has run | R-212 | ✅ discharged |
| 2 | Ruling 180, second branch | R-222 | ✅ discharged |
| 3 | — | R-216 | ✅ discharged |
| 4 | — | R-228 | ✅ discharged |
| 5 | Zero dangling triggers | R-234 | ✅ met — **measured** |
| 6 | The volume stands on its own | R-238 | ✅ met — `tools/self_citation_gate.py` exits 0, **run not read** |

⚠ **Gate 6 is met and its green is narrower than it sounds.** It measures **pointing**, not honesty
about inheritance; an absorbed debt is invisible to it by construction. Its scope list for the bare
`the source` family is hand-drawn, so a *new* chapter that quarries prior work falls outside it
silently. Both limits print on every green run.

---

## CARRIED ROWS — NOT RECOVERABLE BY READING

Four, moved by hand from the archive. **Each is live, each names a defect whose subject is a tool or
a structural property rather than a sentence, and no amount of reading the PDF would surface any of
them.** Full text is in the archive under the same number.

| Row | Finding | Why a fresh read cannot find it |
|-----|---------|--------------------------------|
| **R-205** | `apparatus_rot.py` audited one chapter of sixty and never printed a zero | A gauge's coverage is invisible in its output |
| **R-207** | A quoted string under 12 characters flips quote parity for the rest of a note | Parser behaviour; the rendered page looks correct |
| **R-225** | Summation arithmetic, and a pointer class no gauge watches | Cross-file arithmetic, not a passage |
| **R-237** | 19 of 43 cards are OUTWARD and ungraded for reachability | A property of the card set, distributed across 43 chapters |

⚠ **`--carry` returns 11 candidates and four are carried.** The other seven are either already PAID
(R-212, R-222, R-238, R-239) or judged reader-findable after all (R-221's production scaffolding in
the body, R-233's under-specified beam, R-235's receipts) — **and those three are deliberately NOT
carried**, because carrying them would prejudge the fresh read they are supposed to be tested by. If
a read does not find them, that is a finding about them. [[feedback_briefing_manufactures_the_agreement]]

---

## FINDINGS — filed as `R2-nnn`

New numbering on purpose: `R2-` cannot collide with the retired `R-nnn`, so a row number in a commit
message, a docstring or a chapter note is unambiguous about which queue it belongs to, forever.

**0 of 71 chapters read.** The first finding and the coverage number are read together or neither
means anything.

---

### R2-001 — THE ABSORPTION SWAPPED AN EXTERNAL POINTER FOR AN IMPLIED **INTERNAL** ONE ✅ FIXED

**Found by the first fresh read, four hours after the defect was introduced, by the party who
introduced it. Filed anyway and in full, because a defect caught by its author is still a defect and
the interesting thing here is the mechanism.**

R-239 absorbed 83 anonymous references. At two sites the absorption removed the citation and **kept
the grammar of citation**, replacing *the source* with **`this framework's own earlier statement`**
and **`this account's own earlier statement`**. Read cold at `VII.8` p.885, that sentence says the
reader is being told about an earlier passage of **this book** — and it comes with coordinates:
*"Its culminating section"*, *"Four subsections later"*, *"under a heading reading Reintegration"*.
There is no such section. **A reader who goes looking finds nothing, which is strictly worse than
the pointer it replaced**: the old form at least implied an outside document.

⛔ **THE MECHANISM IS THE PART WORTH KEEPING.** *this account's own* is a possessive that asserts the
referent is INSIDE. The repair was aimed at the noun (*source*) and never checked the determiner,
so it removed the thing that pointed outward and left the thing that points inward. Repairing the
named cause is not the same as repairing the sentence. [[feedback_repair_scoped_to_named_cause]]

✅ **AND THE CORRECTION RUNS AGAINST MY OWN TALLY, WHICH IS WHY IT IS WORTH WRITING DOWN.** The first
read of the grep suggested the recast vocabulary was a coinage introduced last night across a dozen
chapters. It is not. **`the inherited material` was already this book's established idiom** — `IV.7`
(2), `IV.8` (4), `IV.9`, `IV.10` and `VI.8` all carry it in prose written well before D195, and none
of those files were touched by the sweep. So the DISCLOSE recast matched the volume's register
instead of inventing one, and the defect is **two sites, not a class**.

**Repaired in the same pass, to the idiom already in the book:** `VII.8` §I (×2 plus two
*earlier material* → *inherited material* for consistency) and `VIII.1` §the-summit. Gate 6 re-run,
exit 0.

⚠ **`VII.8` IS NOT MARKED READ AND THAT IS DELIBERATE.** The read covered the body through §II and
did not cover §III onward or the endnotes. Marking it read would put a green on the coverage gauge
for a pass that did not happen, on the gauge's first use, which is the exact failure the gauge was
built to prevent. **Coverage stays 0/71.**
