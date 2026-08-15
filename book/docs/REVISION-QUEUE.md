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

## INBOUND REGISTER — Clayton, Day 196: a 146-item synthesis, machine-triaged

**What arrived.** *TRUTH AND CONSEQUENCES — MASTER REVISION QUEUE, v2.0 (Full Synthesis)*, 146
numbered rows, 31 KB, stamped 15 August 2026. Held at
`carapace/Architecture/data/telegram_docs/doc_32133221.txt`.

⛔ **IT DOES NOT KNOW THE QUEUE WAS RETIRED.** Its items 001–076 are marked `[CARRIED] from internal
v1.0` — that is the register this repo retired the night before, at `fc52b0f`, for the stated reason
that **a queue row is a measurement and it rots.** A synthesis of a rotted register inherits the rot
and adds a fresh date stamp on top of it, which is strictly worse than the original: the file now
*looks* current. Adopting it wholesale would have re-opened the exact backlog Clayton's own ruling
closed. So it is triaged as an INBOUND SOURCE, alongside the archive — **not promoted to the queue.**

**The triage is machine-run, not read.** `tools/inbound_triage.py` ignores what each row claims about
its own status and instead takes the row's *quoted target string* to the chapter files, asking
whether that string is still in the **body**, survives only in the **apparatus**, or is gone.

| | count | meaning |
|---|---|---|
| **LIVE** | 6 | the defect text is still standing in body prose |
| **PAID** | 6 | the row's own prescribed replacement is already printed |
| **PAID?** | 1 | defect text survives only inside an endnote — body repaired, note kept |
| ABSENT | 13 | quoted target found nowhere in the named chapter |
| **NOQUOTE** | **119** | **the row quotes no testable string at all** |
| NOLOCUS | 1 | no resolvable chapter |

⚠ **THE HEADLINE IS 119, NOT 6.** Eighty-one per cent of the register is prose that names a defect
without quoting the text that carries it — *"disclose the edition marker"*, *"confirm the receipt"*,
*"maintain strict demarcation."* Those rows cannot be checked, cannot be closed by evidence, and
cannot rot visibly. **A row no instrument can decide is a row that will read OPEN forever**, which is
how a 206-row backlog happened the first time.

⚠ **AND THE MEASURED SET IS 13 OF 146.** Everything outside LIVE/PAID/PAID? is *undecided by this
instrument*, not clean. It is reported in its own buckets and folded into neither answer.

⚠ **THE PAID COLUMN HAS AT LEAST ONE KNOWN FALSE POSITIVE.** Row 083 scored PAID off *"do be do be
do"* in `VIII.7`; the row is actually about adding Whitehead to `03-THE-ANCESTORS.md`, and the locus
resolver took the wrong file. Hand-checked: **Whitehead is present (6 mentions) — Wilber and
MacIntyre are absent (0), so rows 042 and 073 are LIVE and the tool missed them.** Row 127 is
likewise not trustworthy at PAID and needs a hand read. The instrument's controls prove it can
separate repaired from standing; they do not prove it resolves a locus correctly.

**THE CONTROL, which failed twice before it passed.** Four rows hand-grepped against the chapter
files *before the parser existed* — 130 and 018 and 021 LIVE, 096 PAID?. Run 1: control mis-specified
(085 quotes nothing; the instrument was right and the control was wrong). Run 2: the register
punctuates American-style, so `run at full cost,` carries a comma the book does not print. Run 3
exposed the defect that mattered — **`Replace "A" with "B"` puts the OLD text after the verb**, so
the first parser scored *"twelfth century"* as prescribed-and-present and called a standing
CRITICAL defect PAID. Three constructions invert a plain `Defect:`/`Action:` split and all three are
in this register.

**Disposition: the fresh-read loop stays primary.** Coverage was 0 of 71 when this was written and that number governs.
The six LIVE rows below are entered because they are machine-confirmed against body text, not because
a register asserted them.

| R2 | Register row | Locus | Defect text still in the body |
|----|----|----|----|
| R2-002 | 018 / 085 CRITICAL | `V.6:178` | *"stated it in the twelfth century"* — Lurianic *tzimtzum* is 1572. `[^11]` already rules on it |
| R2-003 | 021 / 091 CRITICAL | `V.7:191` | *"gave the rest of his life"* — the conferences ran 1582–1589. `[^14]` already rules on it |
| R2-004 | 090 MODERATE | `V.6:12` | *"about three years"* — Luria taught ~2. `[^1]` already rules on it |
| R2-005 | 014 CRITICAL | `IV.10` | Loch Ness eDNA graded *"published paper"*; it is a 2019 institutional release |
| R2-006 | 095 MAJOR | `V.9` | *"Very few"* multi-sensor tracks, no published denominator |
| R2-007 | 130 MAJOR | `V.7:147` | *"The grimoires are, by volume, warnings"* — `[^11]` says nothing has measured it |
| R2-008 | 042 / 073 MAJOR | `03-THE-ANCESTORS.md` | Wilber and MacIntyre absent (hand-checked, 0 mentions) |
| R2-009 | 041 / 144 CRITICAL | `C.1:127` | No DOI minted. `C.1` prints *"Until that line carries a DOI…"* — a **release gate**, not a backlog row |

★ **FIVE OF THESE NINE ARE ALREADY DIAGNOSED IN THE BOOK'S OWN ENDNOTES.** The note says the body is
wrong; the body still says it. That is not a discovery the register made — it is a **standing debt
the volume prints against itself**, and it is machine-enumerable: 140 ⛔ flags across 27 chapter
files, concentrated in Books IV, V and VIII. **The register found by hand a subset of what a sweep
over ⛔ would enumerate whole.** That sweep does not exist yet and is worth more than the other 137
rows combined. [[feedback_instruments_go_where_instruments_are_cheap]]

⚠ **DUPLICATION.** The 146 are not 146 distinct findings. At minimum sixteen pairs are the same
defect filed twice under the v1.0/v2.0 merge — 018↔085, 021↔091, 025↔086, 008↔102, 009↔103, 011↔104,
041↔144, 069↔145, 010↔084, 022↔078, 024↔080, 065↔082, 073↔083, 001↔016↔077, 023↔079↔094. The total
is a merge artefact, and the severity ledger inherits it: a CRITICAL counted twice is not two
criticals. [[feedback_self_generated_denominator]]

---

## FINDINGS — filed as `R2-nnn`

New numbering on purpose: `R2-` cannot collide with the retired `R-nnn`, so a row number in a commit
message, a docstring or a chapter note is unambiguous about which queue it belongs to, forever.

**2 of 71 chapters read — VI.2 and VI.4, both whole, both from the PDF, Day 196.** The findings and
the coverage number are read together or neither means anything. **8,893 of 323,904 words. 2.7%.**

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

---

## READ SESSION 1 — Day 196, VI.2 and VI.4, whole, from the PDF

**Chapters chosen by measurement, not by interest.** SCAN-005 found the ⛔ register is a photograph
of where the audit went: 0.47 stop-marks per endnote in IV/V/VIII/C, **0.004 across the 235 endnotes
of II/III/VI/VII.** Book VI carries more endnotes than Book VIII (59 vs 43) and 21 fewer stop-marks,
and all eight books were last touched the same day — so the asymmetry is *unswept*, not *clean*. The
first fresh reads therefore go into the unswept half. VI.2 and VI.4 specifically because SCAN-005
named them as the two places an outside reader had checked something the book could not tell it.

⚠ **THE POSITIVE CONTROL ON MY OWN READ, STATED FIRST BECAUSE IT IS THE PART THAT COULD HAVE GONE
BADLY.** A read that finds only structural defects and no factual ones is indistinguishable from an
inattentive read. So the citations were checked rather than admired — **and they held.** Gladstone
1858 → Snell 1946 is exactly the "eighty-eight years" the first sentence claims. Knox, *GRBS* 9
(1968), 421–435 ✓. Gavrilov, *CQ* 47 (1997), 56–73 with Burnyeat's postscript at 74–76 in the same
volume ✓ — **and Burnyeat's neglected evidence really is Ptolemy**, which is the kind of specific
detail a bluffing paragraph gets wrong. *altruism* first attested 1853 ✓. Williams, Sather 57, 1993
✓. Wernicke, *Der aphasische Symptomencomplex*, 1874 ✓. Augustine at Milan 384, and 384 → the press
is *"more than a thousand years"* ✓. Eisenstein 1979 2 vols. CUP ✓, Johns 1998 Chicago ✓, Havelock
1963 Belknap ✓, Taylor 2007 Belknap ✓, McGilchrist 2009 Yale ✓. **Fifteen checks, fifteen good.**
The defects below are therefore about *grade and placement*, not about facts — and one candidate
died under checking: VI.4's *"roughly four hundred years after the press"* looked short for radio
(1450 → 1920 is 470), until VI.5 turned out to open by **giving simultaneity back to print**. The
chapter that would have been wrong argues against my reading of it. Not filed.

---

### R2-010 — THE VOLUME'S GRADE DISCLOSURES SIT IN THE ONE PLACE THE VOLUME SAYS THEY MUST NOT ⛔ OPEN

**Locus: 18 chapters — IV.1–IV.10, V.11, VI.1–VI.7. The rule it breaks is printed in VI.2, p.623.**

VI.2 states the book's disclosure discipline in three numbered parts, and part two is unambiguous:

> **Two: say where the mechanism is open, in the open, at the moment you use the claim** — not in a
> footnote, **not in a caveat paragraph at the end that the reader has already learned to skip.**

Eighteen chapters then carry their entire grade disclosure in *the standing note on grade* — an
unnumbered italic paragraph, terminal, immediately before the Notes heading. **It is a caveat
paragraph at the end.** That is the placement the book names and forbids, and it is not an
occasional slip: it is the volume's standard apparatus for exactly this job.

⛔ **AND IT IS UNREACHABLE, WHICH IS THE HALF THAT MAKES IT A DEFECT RATHER THAN A STYLE CHOICE.**
Machine-counted across all 18: the phrase *standing note* occurs **exactly once** in seventeen of
them — the note itself. **Nothing points at it.** Those seventeen chapters carry **146 numbered
endnotes between them, and not one of them routes a reader to the grade.** A reader who does the
thing the apparatus is built to reward — follow the superscript, check the source — lands on the
flat attribution and is never told what grade it was asserted at. The disclosure is only found by
reading to the end of a chapter you have finished.

**VI.4 is the sole exception in the volume**, where `[^7]` closes *"See the standing note below."*
One cross-reference in 147. **And VI.4 is the one chapter where the two notes disagree** — see
R2-011. The single link that exists is at the single site where following it changes the answer,
which is the strongest possible argument that the other 146 need it too.

**Fix, and it is small:** one clause per chapter, either at the point of use or in the numbered note
— *"named from standard reference scholarship; see the standing note."* Seventeen edits. No prose
moves. [[feedback_gauge_reachable_from_its_own_subject]]

⚠ **What this row does NOT claim:** that any attribution is wrong. Fifteen citation checks in these
two chapters held. It claims the volume's own stated rule about *where* a grade lives is broken by
the volume's own standard apparatus, at scale, and that the fix is a pointer rather than a rewrite.

---

### R2-011 — `VI.4`: THE SAME ATTRIBUTION IS GIVEN TWO DIFFERENT GRADES, AND THE READER REACHES THE STRONGER ONE FIRST ⛔ OPEN

**Locus: `VI-04-print-and-the-interior.md`, `[^7]` vs the standing note. PDF p.649, p.660, p.662.**

Body, p.649: *"McGilchrist's historical argument … reaches a conclusion this book agrees with almost
word for word."* The numbered note the reader follows says:

> `[^7]` … the account of the Reformation given here — individual scripture reading and literal
> sense strengthening a rule-bound, text-driven, univalent mode, and the rejection of image and
> metaphor removing the other mode's food — **is his.**

The standing note, two pages earlier in the flow and unnumbered, says of the same passage:

> **McGilchrist's Reformation chapter specifically**, because this chapter attributes to him a
> historical argument … and **the summary above was assembled from secondary accounts of a very long
> book** … **the route he takes to it is the part reported thinnest.**

**`is his` and `assembled from secondary accounts` are different claims about the same sentences.**
The first asserts the argument as McGilchrist's, flatly, at the point of use. The second says the
book has not read the argument in the primary text and is reporting a route at second hand — and the
standing note's own header confirms it: *"None of their texts is in this repository."*

⚠ **THE ORDERING IS THE DEFECT.** The stronger claim is the one wired to the sentence. The weaker
and truer one is the one nothing links to except, by luck, this very note. A reader checking the
Reformation attribution stops at `[^7]`, because `[^7]` answers the question it was asked.

**Fix:** three words in `[^7]` — *"is his, reported here from secondary accounts; see the standing
note."* The standing note already carries the honest version; it just has to arrive at the door
where the reader knocks. [[feedback_audit_the_last_clause]]

---

### R2-012 — `VI.2`: THE CHAPTER'S HIGHEST-GRADE SENTENCE IS ITS ONLY SECOND-HAND ONE ⛔ OPEN

**Locus: `VI-02-the-voices.md`, PDF p.622 against p.626.**

VI.2's whole architecture is a grading exercise performed in public on Julian Jaynes — three claims,
three grades, three sentences, each with its falsifier named. It is the best thing in the chapter.
Rule One is stated and then demonstrated:

> **One: say what the evidence carries, at the grade it carries it, in a sentence with no softener
> in it.** The *Iliad*'s psychological lexicon differs from the *Odyssey*'s in the ways Snell
> describes. That is not *arguably*. **It is countable, it has been counted, and anyone may recount
> it.**

Four pages later, in the standing note:

> **Snell's lexical claim**, because beat one is **load-bearing for the whole of Book VI** and is
> **reported here at second hand. The counts are checkable and should be checked.**

⛔ **THE GRADING DISCIPLINE IS APPLIED TO THE CLAIM THE CHAPTER IS ARGUING WITH AND EXEMPTED FOR THE
CLAIM IT IS RESTING ON.** *"It has been counted"* is true — Snell counted. What the sentence lets a
reader take is that the count is *available and checked here*, and it is neither: no count is
reproduced, Snell's text is not in the repository, and the chapter's own apparatus says so. This is
the sentence the chapter uses as its fallback position — *"if Jaynes is wholly false … the work he
was going to do was already done, four pages ago, by a word-count."* **The load-bearing beat of Book
VI is the one beat in VI.2 whose grade is not stated where it is used.**

Two further instances of the same shape in the same chapter, both self-declared in the standing note
and neither marked in the body: right-temporal involvement in AVH given as *observed* with no study
(p.620), and the population-prevalence-above-diagnosis-rate line in the census card given with no
number (p.624) — which the note itself calls *"the thinnest thing in this chapter."*

**Fix, and it costs the chapter nothing rhetorically:** *"It is countable, and Snell counted it —
at second hand here, and checkable by anyone."* That is still a sentence with no softener in it. It
is Rule One obeyed on the chapter's own premise. [[feedback_evidence_grade_distinction]]

---

⚠ **WHAT SESSION 1 SAYS ABOUT THE ⛔ REGISTER, AND IT IS THE REASON TO KEEP READING.** Book VI
carries **zero** stop-marks across 59 endnotes. Two chapters of it, read whole, produced three open
rows — one of them volume-wide and structural. **The 0.004 was never a measurement of cleanliness.**
Neither R2-010 nor R2-011 nor R2-012 could have been found by the inbound register's quoted-string
triage, because nothing here is misquoted; and none could have been found by a ⛔ sweep, because Book
VI has no ⛔ to sweep. They required a person reading a chapter to the end. That is the argument for
the gauge, made by the gauge's first two rows. **69 chapters and 315,011 words remain unread.**
