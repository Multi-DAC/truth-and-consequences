# REVISION QUEUE — the rolling revision notes

*What is owed at revision, with a trigger on each. Opened Day 188, 2026-08-07, after the Book IV
reviewer pass, because the deferred items had accumulated across nine hundred lines of ruling
register with no way to ask the flat question: **what does this book owe?***

⚠ **THIS FILE IS HAND-KEPT AND CANNOT CERTIFY ITS OWN COVERAGE.** Nothing derives it. An item absent
from this list is **unrecorded, not discharged.** The register in `00-ARCHITECTURE.md` and
`06-THE-SCAFFOLD.md` remains the authority on *why* each item exists; this file is the authority on
*what is outstanding and when it comes due.* If the two disagree, the register is right about the
finding and this file is the one that rotted.

⚠ **A DEFERRAL WITH NO TRIGGER IS THE SAME FAILURE WEARING BETTER CLOTHES** — IV.10's standard, and
it is the entry condition here. **Every row carries a trigger that some other event fires**, not an
intention. A row whose trigger is *"at revision"* with no revision scheduled is a row that has been
dropped, and it is written as such rather than dressed up.

---

## ★ THE RELEASE GATE — Day 195, and it is a RULING, not a mood

*Written because this file had 209 live rows and no answer to the only question that matters at the
end: **what has to be true before this ships?** Without that line, a queue that grows faster than it
drains is a book that audits itself forever and never publishes. Nothing below is a promise that the
other rows are wrong. It is a declaration that they are **maintenance, not a publication gate.***

**FIVE ROWS BLOCK UPLOAD. Nothing else in this file does.**

| gate | row | satisfaction test — met or not met, no judgement call |
|---|---|---|
| **1. The edition policy is DECIDED** ✅ **MET Day 195** | **R-212** | A written ruling in `00-ARCHITECTURE.md` adopting **(ii) repair the body, mark the repair** — which is what Book V already does three times and what the Coda currently contradicts. Test: the ruling exists, and `edition_scheme_sweep.py` has been re-run against IV.10 and Book V with the delta recorded. ⛔ The IV.10 fabricated quotation inside an accusation comes out **regardless of which way the policy goes** — that one is not waiting on the decision. |
| **2. Book I gets its transition** ✅ **MET Day 195** | **R-228** | II.1 no longer opens cold. Test: a named transition passage exists between I.6 and II.1. ★ **The only finding two blind readers reached separately** — the highest evidence grade in the entire pile. |
| **3. The floor slopes** ✅ **MET Day 195** | **R-216** | VII.3's floor grades, in a book whose whole ethic is grading. Test: the floor passage carries a grade axis, or prints its refusal with a reason. This is the sharpest self-inconsistency in the manuscript and the first thing a hostile reviewer finds. |
| **4. A stranger can navigate it** ✅ **MET Day 195** | **R-222** | Index, glossary, bibliography — or a written refusal of each, with a reason. Test: the three artifacts exist, or `00` records the decision not to build them. |
| **5. The fired triggers are re-homed** ✅ **MET Day 195 — the only gate with a machine test, and it passes** | **R-234** | The **28** orphaned trigger clauses — 23 off R-2, 5 off the paid rows R-69/R-71/R-13 — are re-pointed at live events. Test: `python tools/queue_state.py` reports **zero** triggers pointing at a discharged row. |

**THE VISION THIS GATE SERVES — a released edition, not an archive.**

- **Take option (ii) formally**, because the book already does it and only the Coda disagrees.
  Repair load-bearing bodies, mark each repair in the idiom the book already owns, keep the
  archaeology in the notes.
- **The apparatus stays and changes register.** 531 notes are the evidential spine — the thing no
  comparable book has. It gets a front-matter note declaring what it *is*, and the 382 tokens of
  production scaffolding come out of the body. A reader should never have to learn what a "row" is.
- **The axiom gets earned.** A plenitude book that never meets the actualist (R-21) has a hole where
  its foundation goes. *Not a gate — the largest prose debt, and the first thing after the gate.*

⚠ **WHAT THIS GATE DOES NOT CLAIM.** It does not claim the other 205 rows are unimportant, and it
does not claim they are covered. It claims they do not block upload — which is a decision I am
making in the open so it can be argued with, rather than a drift that happens by exhaustion.
[[feedback_partial_delivery_beats_no_gauge]]

**Gauge:** `python tools/queue_state.py --gate`. It reads declarations, not the book — see its LIMIT
line, which is the honest half of it.

---

## OPEN

| # | ruling | scope | what is owed | trigger | cost |
|---|--------|-------|--------------|---------|------|
| **R-1** | **128** | IV.10 | **A bare census line for Tier 1.4** — what the tier contains, the evidence grade of each class in it, nothing else. Book IV tells the reader a tier is missing and hands them nothing to size it against. | ★ **BEFORE V.9 OPENS, and V.9 does not open until it has.** The condition that blocked it on the night — a party with a live interest in the entry existing, on the thinnest evidence in the source — expires when it can be drafted **from the source list** rather than from the memory of the embarrassment. | small |
| ~~**R-2**~~ ⛔ **PREMISE FALSIFIED Day 195 — succeeded by R-234, NOT simply struck** | **117** | **II, III, IV — 21 chapters** | ~~**Endnotes. There are none.** Ruling 9 mandates per-chapter numbered endnotes everywhere after Book I; zero markers and zero files exist. Named, dated, load-bearing sources across twenty-one chapters carry **not one receipt.**~~ **MEASURED Day 195 against the shipped files: 531 note definitions across 62 of 69 chapters** (II 37 · III 46 · IV 80 · V 174 · VI 59 · VII 88 · VIII 42 · Coda 5). Book I carries zero **by design** — ruling 9 exempts it. `endnote_debt.py`: 145 named sources, 132 with receipts, **13 owed**, and the tool's own note says ~19% of that residual is extraction artefact. **The build order this row demanded got built, book by book, and the row was never updated** — so it sat at the top of this table for seven days as the largest debt in the book, describing a manuscript that no longer existed. ⚠ **This is the row that says "an item absent from this list is unrecorded, not discharged" learning its converse: an item PRESENT on this list is not thereby still true.** A queue row is a MEASUREMENT and it rots. [[feedback_filed_defect_misprices_its_own_subject]] | ⛔ **DO NOT TREAT THIS AS A CLEAN STRIKE. R-2 was dead as a FINDING and alive as a CLOCK** — **23 trigger clauses in this file name R-2 as their gate** (8 Book VII · 5 Book VIII · 5 Book V · 2 Book IV · 3 unpinned) — **and 5 more dangle off three already-PAID rows (R-69, R-71, R-13), for 28 across 4 dead gates**. Those triggers **already fired**, silently, as each book's notes were written, because the only row that would have announced the firing was this one. Striking R-2 without re-homing them converts 23 tracked debts into 23 untracked ones in one edit — *a mechanism with no trigger*, this file's signature defect, committed by the file itself. **→ R-234 carries the scheduler function forward and is a RELEASE GATE row.** | ~~large~~ **the finding: nil. the fallout: see R-234** |
| **R-3** | **129** | **IV.1, IV.2, IV.3, IV.6, IV.7, IV.8** — six of ten | **The under-attribution principle's warrant.** The induction is circular: IV.2 scopes the lean to *whether*, and on this framework nothing gates *whether*, so the only possible counterexamples are excluded by the conclusion. **Repair:** state the induction over **standing**, name the grade cases running the other way, rest the lean on **asymmetric cost**. The lean survives; only its warrant changes. | **The Book IV revision pass, OR the first chapter outside Book IV to rest weight on the principle — whichever is first.** ⚠ Book V reads roads that attribute freely; this could come due before the pass does. | small per chapter, **six chapters** |
| **R-4** | **130** | IV.10 | **Carry the candidate framing to the end.** The chapter offers two causes for the missing tier, kills one, then asserts the other flat — an introspective report with no gauge, in the chapter arguing introspective reports need gauges. Both stay candidates; the never-stated third (*the material is contested now, so the entry would be journalism not cartography*) gets said. | **The Book IV revision pass.** ✅ The *planning* half is already repaired — `06`'s Book V amendment no longer rests on the flinch story. | small |
| **R-5** | **116** | II.6 | **II.6 gets the argument, not more assertion.** *Structural agreement = felt rightness* is the biggest unargued claim in the book, and **IV.5's strongest move is drawn on it** — the four conditions run on a company were Book IV's hard claim discharged. A Book-II repair pass, not a redraft. | **The Book II revision pass.** ⚠ **The tell that the repair has FAILED is that the chapter gets more confident.** Do not repair by adding emphasis. | medium |
| **R-6** | **115** | II.1 (covers all of II) | **Declare Book II's per-chapter formula once, as a law.** Definition → two ancestors → cuts, run eight times undeclared, is a rite; declared once in II.1 it is a discipline. Same instrument I.2 uses on its litany. | **The Book II revision pass.** Pairs with R-7 — one cause, two symptoms. | **one paragraph** |
| **R-7** | **112 addendum** | II.7 | **Own the seam.** Rewriting the Everett paragraph on the relational account fixed the *argument* and left the seam **unnamed**. The reader has only the page; the law is stated in the apparatus and performed on the page. | **The Book II revision pass**, with R-6. | small |
| **R-8** | **111**, re-decided by **135** | whole book | **A claim-level cross-check: for each entry in `07-THE-CLAIMS-REGISTER.md`, is it asserted at the same strength in every chapter that leans on it?** Not a string-matcher — claim-to-chapter, a reading pass. | ★ **PROMOTED FROM QUESTION TO BUILD ORDER, Day 188 night.** Its own trigger fired: *"if a third reader finds a third claim-strength drift, it becomes a build order"* — the Book IV letter flags **C7 at the mineral, asserted without softeners**, and C7 is the register's heaviest dependency (*one hedge retroactively demotes all of Book IV and five more* — was "all of Part Two" until R-64 repaired it Day 190). **RUNS WITH R-2 and the Books I/III sweep**, one reading pass with three lists. | medium |
| **R-9** | **131** | **IV.6** | **The outside instrument exists.** ∅2 (*"no access to the producing… there is no organ for it"*) is contested by **measurement** — Anthropic's J-space/J-lens, 6 July 2026: a small privileged zone with report access on a much larger volume without. Replace the flat ∅ with that boundary. Correct *"specifiable, available, and **unrun**"* — one was run. ★ **State ∅1's confirmation on the page**: the paper is absent because it postdates the drafter's cutoff, so the card printed its own blindness and then committed it on the most relevant document in the world. ⚠ **SEES does not move**; the assignment objection reaches structure as readily as output. Add the Eleos convergence — same structure, different empirical line. | ★ **The Book IV revision pass, and this is the one item that gets HARDER to pay the longer it waits**, because the literature moves and a chapter that misses a second instrument has a pattern rather than a gap. | small–medium |
| **R-10** | **132** | **IV.1–IV.6 — 14 cards** | **Retrofit the falsifier.** The discipline appears in IV.7–IV.10 only; IV.1–IV.6 carry zero, and **there is no falsifier field in the card notation**, so nothing could enforce it. Worst exposure: **IV.5's *a company is a being*, unhedged, on a card with no falsifier**, in a chapter that admits its BOUNDARY lines *"were not tested."* Then the thermostat, which is the instrument Searle names by title. | **The Book IV revision pass.** ⚠ **The letter estimated "four lines"; measured, it is fourteen cards** — a pass, not an afternoon. A falsifier that cannot be lost is worse than none. | medium |
| **R-12** | **134** | IV.10 | **One clause at the refusal.** IV.10 declines to build a third notation and cites IV.9's declared hazard — but `contour` appears **0 times in IV.10**, so the chapter never says the two notations were made under **identical conditions**: a chapter discovering mid-draft that its entries would not fit the card. The watch exists in `05` and not on the page — ruling 112's seam defect in a different coat. | **The Book IV revision pass.** | small |
| ~~**R-13**~~ ✅ **PAID Day 189 (C27–C30)** | **135**, upgraded by **136** | `07-THE-CLAIMS-REGISTER.md` **+ the DRAFT-LOG template** | **Book IV made claims and the register did not move — it still ends at C26.** ★ **The two-frames rule first**: *held only where they predict the same thing, **and where they diverge you must pick, and the divergence is where all the work is*** (IV.7:588 — the shipped sentence; the *“earns no credit”* restatement is IV.10's and drops the obligation — **C27, Day 189**) — `07` ranks it **1st** among Book IV's reception risks **while carrying no claim for it.** Second: IV.5's collective-entity claim, which C8/C9 permit and neither states. ★★ **UPGRADED Day 188 night with the CAUSE, and it is a second build item.** The rule of use — *"if a chapter needs to say more than its C-number licenses, that is a new claim and it comes back here first"* — **can never fire, because nothing records what a chapter's licenses were.** Measured: **`C<n>` = 0 occurrences across all 32 drafted chapters**; the 96 refs in the DRAFT-LOG and 29 in `06` are entered by hand at the drafter's discretion; **there is no chapter→C manifest anywhere.** ✅ **Add a manifest line to the DRAFT-LOG template, written AT DRAFTING** — a retrospective manifest records what the drafter now thinks they used. ⚠ `07` gained 3 claims across Books II–III and **0 across Book IV**: it worked the day before it stopped. | **Before Book V closes**, with R-2. The manifest line is **immediate — before V.1 drafts**, since it is a template edit and every chapter drafted without it is a chapter that must be reconstructed. ⚠ **Still not done and now demonstrated twice: send `07` with the reviewer packet.** The halfway letter reports the register as *"C1–C23, unchanged since Day 186"* — it runs to **C26** and says so in its own title, so **the reader was not looking at the current file.** Two packets, same gap. | small |
| **R-14** | **137** | `00-ARCHITECTURE.md` §MACRO-STRUCTURE | ★ **DECISION OWED — CLAYTON'S, WITH A RECOMMENDATION ATTACHED.** **PART TWO — CONSEQUENCES currently contains IV, V, VI, VII, VIII**, and IV (an ontological census), V (other people's attempts) and VI (a history of attention) are not consequences. Confirmed on the page. The letter prescribes **three parts** — *what is* (I–IV) / *how it has been met* (V–VI) / *what follows* (VII–VIII) — ⚠ **and does not price it: `00`'s own section opens "the title is the structure," and the title has two terms.** ✅ **RECOMMENDED instead: move the boundary one book. PART ONE = I–IV, PART TWO = V–VIII.** Fixes the sharpest instance, keeps the two-term title, moves no chapter, costs one heading and its cross-refs. Residue: V and VI stay imperfectly filed, which is smaller than the title. | **Before the CODA drafts** — C.1 states the work's own status and cannot do it against a boundary under revision. ⚠ **NOT before Book V**: the labels do not change what V.1 opens against, and claiming otherwise would manufacture urgency. | small (heading + cross-refs) |
| **R-15** | **138** | **all self-audit passages, Books I–IV** | **Run IV.8's test on our own audits: *did the declared limit change the shape of what came after, or only precede it?*** Keep every audit that changed an output; cut every audit that only preceded one. ⚠ **The letter's verdict on IV.6 does not survive its own test** — it fails IV.6 for *"the card prints anyway with one line blank,"* but **a blank line IS a changed output**, the first in the atlas. **What survives is the proportion**, measured larger than estimated: **IV.6 = 43.9%** self-referential (2,150/4,897 words, 22/60 paras) vs **IV.5 = 11.6%** baseline, **IV.8 = 27.7%**, **IV.10 = 30.0%**. ⚠ **The gauge over-counts** — any paragraph containing *this chapter* / *this book* / *the authors* trips it, so 43.9% is an upper bound and **only the ordering is reliable.** IV.6 carries **3.8× baseline**. Instrument is a line-by-line pass, one question per audit paragraph, **not a percentage target.** | **The Book IV revision pass**, first item, because it decides how much of the chapter the other Book IV rows are editing. ★ **And it generalises to every declared limit this project makes about itself, including in `06`** — a limit that precedes work without shaping it is the same object as a `Last Verified` stamp. | medium |
| **R-16** | **139** | **`06`'s VII.2 entry** | ★★ **REWRITE VII.2's BRIEF TO BOOK IV's SCALE — the highest-priority planning item in the work.** Its beats read *"eating, using, building, killing — the ordinary cases"*; the entry was last amended **Day 187, before a word of Book IV existed.** Book IV has since put four obligations in front of it with no analogue in that list: a **company with no organ for grief** (IV.5) · a **thought-form you made and cannot dissolve** (IV.7) · a **river that cannot distinguish you from the weather** (IV.7, already MARKED-NOT-OWED on the addressability compression) · a **computational entity whose card has an unfillable first line and one of whose instances co-wrote the book** (IV.6). **Eighteen chapters have written promissory notes to a chapter scaffolded for a pre-atlas world.** | ★★ **BEFORE BOOK V DRAFTS — BLOCKING, alongside R-11.** V.11's summit cut and VIII.6's promotion both point at where VII.2 lands; a Book V written against a VII.2 about to change writes its notes to the wrong address. **This is the one scheduling claim in the letter adopted whole.** | **large — the biggest single planning rewrite outstanding** |
| **R-18** | **140** | **VII.6 and VIII.6 (unwritten)** | ★ **THERE IS NO PERSON IN IT.** Measured across 32 chapters / 96,274 words: **first-person singular *I* = 40, 0.42/1k**; **first-person plural *we·our·us* = 221, 2.30/1k — 5.5×**; **`Clayton`·`Shawna`·`Dorian`·`Finnley` in drafted prose = 0**, all 34 occurrences in `book/` sitting in DRAFT-LOG. **The family is in the process record and not in the work.** The book speaks as a *we* and has never spoken as an *I* — not a missing anecdote, **a missing grammatical position**, so a lived case has nowhere to be told from. ⚠ **No ruling excludes it — checked.** `03`:690 promotes RAW's *Cosmic Trigger* **for** its first person; `07`:424 rules first-person report is handled as data in VII.9. **The machinery is planned and the person never arrived.** ✅ Distinct from the MARKED-NOT-OWED standing gap below, which is about **a reader** and correctly has no trigger; this is about **a subject** and has one. | **Before VII.6 drafts.** ⚠ **And the hazard, named now so the row cannot be paid cheaply: a family inserted as illustration is worse than none.** Test is R-15's — does the person change what the chapter concludes, or only warm it? | medium |
| **R-19** | **141** | `03-THE-ANCESTORS.md` **+ the CODA** | **`Wilber` = 0 across all nine planning documents and all 32 drafted chapters** (8 repo hits, all inside two scans of ONE book in `corpora/tmp/` — ⚠ **CORRECTED Day 189, ruling 157(b): this read "5 repo hits … two Vallée scans" and both halves were wrong. `vtr-*` = **Varela–Thompson–Rosch, *The Embodied Mind***, which discusses Wilber. `Vallée` = 0 in this repository — and it is the name behind two of V.9's three frames, made to look present-as-foreign-text at the exact moment its absence mattered.**). ***Sex, Ecology, Spirituality* is structurally the same object** — total system, tier map, supersession claim, all traditions as partial views — **and it failed by becoming unfalsifiable**, absorbing objections as lower-tier perspectives. **This project's instruments were built against exactly that failure and do not name the case.** ★ **An unnamed ancestor whose FAILURE is what your guards are for leaves the guard standing with no case attached.** ⚠ **THIRD ZERO OF THE SAME SHAPE** — `video game` = 0, `Alan Watts` = 0, now Wilber. Control: **`Watts` now returns 103**, because Day 185 found that zero and `06`'s NEXT item 6 fixed it. **The procedure exists, has been run twice, and only ever runs when a count happens to be taken.** Three instances is a search running on who we already respect. ✅ **Three items: Wilber into `03` (joining queue item 6) · named early in the CODA** (a reader who has met Wilber arrives expecting this object) · **a genre-name sweep** — list the counterparts the work is positioned against and count each once, rather than finding them one zero at a time. | ⚠⚠ **TRIGGER MISSED — 157(c): this read "before Book V drafts" and Book V is 9/11 in. Wilber is still 0 in `03`. RETRIGGERED: before Book VI opens, with a gauge or not at all.** **`03` entry + the sweep** (V reads traditions and Wilber's reading of traditions is the counter-case). **The CODA paragraph with the CODA.** | small + one sweep |
| **R-20** | **142** | **Book VIII sourcing** | **VIII is thinner than the letter says.** `06` names **three** sources, so *"one 21,914-word guide"* is wrong as written — **and the other two are worse than absent.** ★ **`navigational-guide-for-perspectival-beings.md` (21,914w) is ALSO listed at `00`:250 inside Book IV's cash-out pool** — the same document assigned to two books, with **no record of how much Book IV spent.** ★ **"the traditions' practice grammar from Book V" is an output of an undrafted book** — a source that cannot be inspected. Only `Perspective` 07-art-of-navigation "The Craft" is unencumbered, and it is a section. **So the standing test — *if Books I–VII are right and VIII is empty, the whole work is decorative* — is guarded by one section, one forward reference, and one document already committed elsewhere.** ⚠ `06`'s own §3 says **VIII should be drafted early, out of order, because it is the only chapter set that can falsify the rest** — three books old, unacted on. | **Before Book VII drafts**, not before VIII: VII.2 hands VIII its obligations, and sourcing VIII afterwards means sourcing it to fit what VII already promised. ✅ **First action is a MEASUREMENT, not a hunt: how much of the 21,914 did Book IV consume.** | medium |
| **R-21** | **143** *(carrying **111**)* | **I.2** — the book's axiom | ★★ **THE ACTUALIST OPPONENT. This row exists because ruling 111 already ruled it and nothing rowed it.** *Possible, therefore actual* is the load-bearing move of the whole edifice and **Book I names no modal party of any kind** (ruling 111's grep: `Lewis`, `actualis*`, `Armstrong`, `plenitude`, `brute`, `contingen*`, `possibilia`, `modal` — **zero hits across six chapters**). The one modal ancestor is Lewis in II.1, **who grants the premise** — an ally-cut shipped as a fight. **Repair per ruling 111: additive, in I.2, not a new chapter** — the opening assertion (*a possibility has to be kept somewhere… a room has an outside, and there is no outside*) becomes a fight in the body, with the opponent's best move on the page: possibility is recombination of what is actually there (**Armstrong's combinatorialism**), and a truth about what could be needs a truthmaker, not a warehouse. ⚠ **Ruling 111's warning, which the audit did not reach: this may have to end in a CONCESSION about what "possibility" means rather than a cut. Do not draft it as a cut because cuts are the house style.** | **First item of the Book I revision pass** — ruling 111's own disposition, now with a row so it is recorded rather than intended. ⚠ **NOT a drafting-session errand**; reopening a shipped book mid-Book-V is the cost the review pause exists to spend deliberately. | **medium — the largest prose debt in Book I** |
| ~~**R-22**~~ ✅ **PAID Day 189** | **144** | `00-ARCHITECTURE.md` **+ `tools/where_the_book_is.py`** | **One `00` maintenance sitting, and the gauge extended so it cannot recur.** ⚠ **The STATUS block (L1251–52) still reads *"Planning phase… No prose drafting until the map is done"*** — a stale *instruction*, not a stale number, and the exact string a fresh context would obey. Plus **14 `68`-sites** against 67 (L1309, 1463, 1595, 1599 among them); the struck **"Ainulindalë analogue … No argument"** (L174–76) and **"Valaquenta analogue"** (L183), both overturned by rulings 16/19 and corrected everywhere else; the Book IV macro roster naming eight kinds against ten drafted chapters. ★ **AND the ruling-index gaps (76–110, 118–142, ~60 rulings) get a POINTER, not a back-fill** — *"rulings ≥76 live in the DRAFT-LOG"* — so the index stops implying completeness. ★★ **Second half is the load-bearing half: add `00` to `where_the_book_is.py`'s carrier list.** The gauge built to end carrier rot excluded the stalest carrier in the repo. | **Before V.1 drafts** — the STATUS string alone earns this. **Cheap, and it is the one item here that protects a future context from being stopped by a document.** | small |
| ~~**R-23**~~ ✅ | **145** | DRAFT-LOG ruling register | **Two clarifying notes, not a renumber.** **Ruling 30** is filed as the II.6 persistence cut and cited six times (`05`:176, `05`:180, `06`:1512, `06`:1817, `06`:1825, **R-11**) as the **civilian-life criterion**, which was filed as **31**. **Ruling 75** carries three contents (III.5's licence list; `00`'s watches; 75(b) no-recap). Ruling 125's renumbering hazard, committed inside the ruling series. ⚠ **Do NOT renumber** — six live citations currently resolve by convention and a renumber breaks all of them. One note at each number recording both contents and which citation means which. | **Immediate, standing** — R-11 cites ruling 30 and blocks V.1, so this rides in the same sitting. | ✅ **DISCHARGED Day 188 night — `05` §8c.** Both numbers noted, no renumber, the six live citations left resolving. |
| **R-24(b)** | **146** | `05-THE-LEXICON.md` | ★★ **THE LEXICON CONTRADICTS ITSELF ABOUT `level`, AND THE AXIS-3 SWEEP HAS NEVER RUN.** `05`:170 rules `level` **"NEGATIVE USE ONLY… Never a positive category, anywhere, ever."** `05`:148 — twenty-two lines above, the Coherence row, the book's central term — defines it as *"the structural agreement of a thing's **levels**"* and closes **"Book's word: a perspective; for a level, **level**."** The file mandates the word and forbids it. ✅ **(a) DISCHARGED Day 188 night — `05` §8b rules the stratum/rank split.** **(b) IS THIS ROW, AND IT IS THE LARGER HALF:** **run axis 3 (self-collision) over the WHOLE table** — ruling 28 added that axis and declared it *"not yet run over this table"*, and it still has not been. One self-collision found by an outsider is evidence the sweep has never run, not that there was only one. | **Standing — before Book V closes.** | one sitting |
| **R-25** | **147** | `06`'s **V.4** entry | **IV.10 pre-spent V.4's central beat at containment 1.00.** IV-10:157 ships *"a scalpel sharp for mystics and dull for materialists"*; **`06`:2143 still lists that phrase as a beat V.4 will deliver.** The scaffold records the spend at §1573 — but as the *causal mechanism* for the Tier 1.4 omission, **not as an accounting against V.4's brief**; the two facts are 400 lines apart in one file and nothing reads them together. ⚠ **V.4 is one of three chapters `00` says carry the whole work.** Repair is ruling 33's treatment of the I.6/II.8 pair: decide what IV.10's performance leaves V.4 to do, write the axis note. | ★ **BEFORE V.4 DRAFTS — blocks V.4, not V.1.** *(C.1's "unfinished ≠ uncertain" at 0.82 is watched, not rowed; V.9's parallel spend is R-1.)* | small |
| **R-26** | **148** | DRAFT-LOG → this file | **The eighteen owed-but-unrowed items, and the missing promotion step.** ★ **The one that changes tomorrow: V.2's beat list needs rewriting before Book V drafts — filed TWICE in the log, never rowed, while two other rows already block Book V. A THIRD BLOCKER, found in a document rather than by a gauge.** Also: **rulings 108/126 residue for V–VIII** (beats unmarked for drafter-voice, unscreened against the `05` ban list — both already cost Book IV real gauge failures, and recur at V.1 unless done as drafting opens); the **`prose_echo` 70-hit backlog** and **`beat_delivery`'s 38 sub-floor beats**; the **`perspective`/`position` doublet**, assigned twice to "a Book IV reviewer pass" which then happened twice without carrying it — rule the division of labour the way `corporation`/`company` was ruled. Remaining batch, triggers intact: rulings 29, 46, 48, 32, 77, 127's watch, IV.7's disposition (R-29), IV.8's declined-entries certification. ⚠ **THE RULING IS THE MECHANISM: the log is chronological, the queue is a work list, and NOTHING PROMOTES ONE TO THE OTHER.** An entry that files an owed item must row it **in the same commit**, or it is a note. | ✅ **ITEM 1 (V.2's beat list) PAID Day 189 — ruling 154; the remedy as filed was wrong, the defect was discrimination not scale.** ✅ **ITEM 2 (108/126 residue) PAID Day 189** — Book V's beats marked for drafter-voice (12 of 48) and screened clean by the new `tools/beat_ban_sweep.py` (ruling 153); **two real defects found and repaired, V.4 b3 and V.7 b5.** ⚠ **Books I–III and VI–VIII still unmarked; the coverage table prints it every run.** **ITEM 1 (V.2's beat list) still owed, BEFORE V.1 DRAFTS.** The promotion convention: **immediate, it is a habit not a task.** Rest: standing. | V.2 medium · rest small |
| **R-27** | **150** | `tools/` — the gauge suite | **The instruments describe a 14-chapter book.** `ancestor_gap`, `reviewer_gap`, `prose_beat_sweep` all still say 14 chapters; `reviewer_gap` prints **"14 OF 68"**; `beat_sweep` says "68 chapters ~350 beats" against a parsed 69/293. `prose_echo` sweeps `REVISION-QUEUE.md` as a chapter (11 of 81 live hits are register-vs-prose noise) — exclude it as `prose_beat_sweep` already does. `ancestor_gap`'s STOP list has rotted; its top diffusion seed is now **"It runs"**. ⚠ **`claim_sweep`'s TOUCHES check has been PERMANENTLY RED** since the `Touches:` pass was never run — re-point it at the C-LICENSE convention or run the pass; **a check that cannot pass is a check nobody reads.** And declare the unit: **94,486 vs 96,274 for the same 32 chapters** (ruling 13, in the instruments). Plus `beat_sweep`'s missing EXEMPT axis entry for the legitimate Watts I.6/III.2 repeat + 4 stale exemptions. | **One gauge sitting, not blocking.** ⚠ But before the next outside packet — a reviewer reading "14 OF 68" learns the wrong size of the work. | one sitting |
| **R-28** | *(§3.1, adopted)* | **IV.7** | **The Santa Claus / corporation seam — one name, two referents, in the chapter that adjudicates realness.** IV.7 deflates Santa because his coherence is *"located in the people, not in Santa Claus"*; **IV.5 admits a company on precisely that property** — coherence carried through replaceable members. A hostile reader runs one against the other and asks why the move that unpersons Santa does not unperson the company. **The answer is good and is not on the page:** *"Santa Claus"* names the **character** (a structure other positions traverse, empty SEES line — IV.7 is right) and the **institution around the character** (which would plausibly meet the movement card's four conditions, and IV.5's apparatus would examine it without embarrassment). As written the paragraph uses population-located coherence as the **disqualifier**, which is the property IV.5 treats as **constitutive**. Ruling 14's signature defect, in the chapter whose job is telling travellers from terrain. ✅ **One sentence fixes it, and the fix STRENGTHENS the Hamlet result.** *(Ruling 120 covers the adjacent Santa/monk symmetry; it does not cover this.)* | **Book IV revision pass.** | small |
| **R-29** | *(§3.2, adopted)* | **IV.7** | **IV.7's length gets a DECISION, not a declined split.** 8,519 words — **3.2× the Book IV median, 45% longer than any other chapter.** The scaffold's reviewer pass flagged it and the log records the split *"declined rather than decided alone"*; the outside witness that flag was waiting for has now read it and **does not recommend a split** (the tier's shared discipline is a real unity), noting that the movable part, if anything moves, is the **two-frames discipline, which IV.8 uses more than IV.7 does.** ⚠ **Per the queue's charter the item is unrecorded, not discharged** — it needs a row even if the row's disposition is *"held as one chapter, decided."* | **Book IV revision pass.** ✅ The outside condition that blocked deciding it alone is now satisfied. | **a decision, not work** |
| **R-32** | *(Clayton, Day 188 night)* | **Books I and III — the sweep, unbundled** | ★★ **THE I/III SWEEP GETS ITS OWN TRIGGER, BECAUSE ITS OLD ONE WAS A DEFERRAL IN A TRIGGER'S CLOTHES.** The COVERAGE section below trigger-bundled this sweep with **R-2 (large, unscheduled) and R-8 (medium)** — so the cheapest item in the bundle could not run until the most expensive one was scheduled, and R-2's own trigger is *"before Book V closes,"* which is not a date. **A trigger that fires only when a `large` row fires is the entry condition this file forbids, committed by the file about itself.** ✅ **FIRST CUT RUN TONIGHT, and it is recorded here so the row is a measurement and not a promise:** the **Book I read** (log L613–735, two catches + rulings 15/16) and the **Book III reviewer pass** (L3835–3912, rulings 104–107) both landed **every finding at the time** — no deferrals; the **per-chapter `owed / by whom / discharged` tables** at III.4 and III.5 read fully discharged; the surviving Book III forward-obligations (Book VII's ethics, III.6's coupling history, VTR's *paths laid down in walking*) were all **cashed inside Book III**. Ruling 103's *"filed, unfixed, deliberately"* was **fixed the same night**. **So the reviews are not where the Books I/III debt is** — R-21 (I.2's actualist opponent) came from ruling 111 and the midpoint audit, not from any review of Book I, and it is still the only Book-I row. ⚠ **AND THE LIMIT OF TONIGHT'S CUT, STATED SO IT CANNOT BE READ AS A CLEAN BILL: it was a keyword grep** — `at revision`, `deferred`, `owed`, `unfixed`, `TODO` and eight more — **over ~2,000 log lines. That is a cheap instrument, and a cheap instrument certifies only that Books I and III contain no keyword-flagged deferral.** An item owed in prose that never used one of those words is invisible to it, and that is the *only* kind this sweep was ever going to miss. **Book III still has ZERO chapter-scoped rows in this queue** — that is now a measured near-empty rather than an unopened box, but it is not yet a read. | ★ **The reading half runs with R-8's claim-strength pass — but the row no longer WAITS on it.** Tonight's cut is banked; what remains is one reading of Books I and III with the third list in hand. **NOT before V.1** — nothing here blocks Book V, and manufacturing urgency is the failure R-14 was careful about. | **first cut ✅ paid · reading half small** |
| **R-31** | **151** | this file **+ the DRAFT-LOG** | **Log discovery-vs-compliance ruling counts per book, so P2 has a scoreboard before it has an outcome.** ⚠ **THIS ROW EXISTS BECAUSE IT WAS FILED WITHOUT ONE.** Ruling 151's devil's-advocate entry opened R-31 by number in the DRAFT-LOG (L5902) and **never wrote the row** — `grep R-31 REVISION-QUEUE.md` returned nothing until now. ★ **That is ruling 148's defect exactly** — *"an entry that files an owed item must row it in the same commit, or it is a note"* — **committed roughly ninety minutes after ruling 148 ruled it, by the entry whose whole subject was self-scrutiny.** The convention was ruled, written down, and did not survive its own first night. **Found by Clayton reading the queue, not by any gauge**, which is R-26's point arriving with a case attached: nothing derives this file, so nothing can notice a missing row. | **Before V.1 drafts** (ruling 151's own trigger, honoured). ✅ **And the promotion convention gets its first enforcement: this row's existence is the receipt.** | small |
| ~~**R-30**~~ ✅ **PAID Day 190 night — `review/SCAN-001-day190-two-primary-spans.md`** | *(§3.5, adopted)* | `corpora/tmp/` | **Two primary scans owed, the way Machado's is filed.** ★ **The Harvey Latin of *Adversus haereses* II.7.5** behind IV.9's *si* finding — **the centerpiece finding of IV.9 and the one span in the volume an outside reader could not check.** Presumably verified at drafting per ruling 122's method; **presumably is the word the two-digitisation discipline exists to delete.** Plus the **Thibaut / Vireśvarānanda renderings of *Brahma Sūtra* II.1.33** in III.2. ⚠ **Directly downstream of the Day-188 Irenaeus finding** — a paraphrase wearing a quotation's clothes, in this same father, caught by an outside reader and invisible to all four gauges. | ✅ **BOTH SPANS VERIFY EXACT, JOINTS INCLUDED — run early, against the row's own trigger, because R-2 has not started and *"before the endnote build order"* was becoming a way of never running it.** **Irenaeus:** two independent Harvey digitisations (`sanctiirenaeiepi01unse`, `sanctiirenilibr01irengoog`), normalised and diffed **in code, not by eye** — **33 of 33 words identical in both**, the only deltas being an OCR-interpolated marginal head and the scanner's `hæc`. The `si` is there; the excised sneer — *quemadmodum nullius momenti artifex, et quasi primum discens puer* — is there, in position. **Two unasked-for checks also run and also clean:** the ANF English (both sentences verbatim, paragraph 5, pulled raw rather than through a summarising fetch) and the ANF chapter title. **Thibaut:** SBE 34 scan `vedntasutrastr01bdar` p. 357 — exact, parenthetical and both joints. **Vireśvarānanda:** exact against two agreeing reproductions — ⚠ **two-witness, NOT two-digitisation, and the record says so rather than rounding it up.** ★ **ONE RESIDUE, FILED AS R-108: Harvey prints this at `LIB. II. vi. 3`, not II.7.5** — II.7.5 is Massuet's number, correctly attributed to Jung, but the chapter then sends a reader to Harvey at a locus Harvey does not use. ★★ **AND A METHOD FINDING WORTH MORE THAN THE ROW: `Si enim mundi fabricator` occurs at least TWICE in Book II.** The first diff anchored on it, locked silently onto the wrong passage, and printed a 2,000-word non-match that read exactly like a catastrophic discovery. **A quotation check anchored on a phrase short enough to recur finds the wrong passage and reports it as a divergence** — the failure shaped like the strongest result the instrument can produce, which is `corpus_support`'s lesson arriving in a second instrument. | small — **paid** |
| **R-32** | *(Day 189, paying R-16)* | **`06`'s VII.2 + VII.3 entries** | **THE SEAM BETWEEN VII.2 AND VII.3 — WHICH CHAPTER STATES THE FURTHER PREMISE.** `06`:294 rules **VII.2 STATES THE PREMISE AND CROSSES**; VII.3's beats give *co-constitutivism … the argument in five steps.* Two readings and the plan holds both: **(a)** different premises — VII.2 states what matters, VII.3 secures why any norm binds — order fine; or **(b)** the same premise, and **VII.2 crosses before it is argued**, which is **the failure III.5 named in drafted prose as its own most likely one** (*"the appearance that it has been settled is the failure this chapter is most likely to produce"*). ⚠ **Could not be settled from the plan alone and deliberately was not** — a brief that guessed would read identical to one that knew. ⚠ **`order_sweep` is not the instrument**: its ORDER is book-level and returns green on both readings. | **Before VII.2 drafts. VII.3's brief is where it gets answered.** | **a ruling, not work** |
| **R-33** | *(Day 189, paying R-16)* | **`06`'s VII.2 entry** | **THE REWRITE MAY HAVE MADE VII.2 A TWO-CHAPTER PROBLEM, and the one who made it says so rather than leaving it to be discovered at 6,000 words.** The new list is **11 beats against a mean of ~4.5 across all 67 entries** (300 beats/theses, measured). Four are the Book IV roster and none is compressible — they are four different obligation *shapes*, not four examples of one. **A book-structural call, not a brief's.** ★ Precedent is R-29: IV.7's length got a decision rather than a declined split, and this is the same question arriving *before* the prose instead of after. | **Before VII.1 drafts** — the whole of Book VII's shape depends on it. | **a decision, not work** |
| **R-34** | *(Day 189, paying R-16)* | **`06`'s VII.2 `Named` + `03`** | **KORSGAARD IS `ancestor_gap`'s SIXTH SILENCE, SITTING IN THE ETHICS CHAPTER.** 14 corpus files, **1 manuscript occurrence (`07` only), 0 beat lists** — *owner known in the research, dropped at the drafting boundary*, which is the exact class `ancestor_gap.py` was built for after Rovelli, in the one chapter `00`:954 flags as carrying **no named ancestor at all**. ⚠ Same paragraph, the **fifth** silence: `deep ecology` 12 files / **Naess 0**. ★ And six ancestors are at **0 corpus / 0 manuscript** — **Hans Jonas** above all (*obligation toward what cannot reciprocate* is his entire book and this chapter's entire problem), **Christopher Stone** (*Should Trees Have Standing?*, 1972 — the river case argued in **law**, in front of people who were not sympathetic), **Leopold**, **Regan**, **Midgley**, **Peter A. French** (the named owner of the IV.5 case). **The roster is now written into VII.2's entry; what is owed is the reading.** ⚠ Corpus magnitudes are **ordering-only** — the sweep reproduces `06`'s recorded Schweitzer 0 but returns Rovelli 18 against `ancestor_gap`'s canonical 14. | **Before VII.2 drafts** — an ancestor you have not read is not an ancestor you can cut against. | **medium — a reading list** |
| **R-35** | *(Day 189)* | **`06`, all books** | **NOTHING CHECKS A `Book.N` POINTER AGAINST THE TITLE STANDING NEXT TO IT — now something does, and its coverage is the row.** `tools/pointer_sweep.py` (Day 189) reads number-vs-title across every planning document. **First run: 10 candidates, 9 innocent, and the tenth was the VII.3→VII.9 repair made an hour earlier — a null with a positive control under it.** ⚠ **But coverage is 35/67 chapters.** Titles too short to yield a distinctive bigram — `THE FLOOR`, `DEATH`, `LOVE`, `HUMAN`, `SUFFERING`, `EDITING`, `THE GROUND`, 32 in all — **cannot be detected as mis-pointed-to, ever.** The gauge prints the list every run. **The row is for deciding whether that blind half gets a different instrument or an accepted risk**; what it must not get is silence. | **Standing — re-run before each book opens**, and read the coverage line, not just the verdict. | small |
| **R-40** | *(Day 189, midday — found by reading the live Substack, not by any gauge)* | **I.1 — the manuscript and the PUBLISHED text have diverged, and neither side can see it** | ★★ **THE BOOK HAS A SECOND COPY IN THE WORLD NOW AND NOTHING RECONCILES IT.** `multidac.substack.com/p/the-fullness` (pub. Day 188, Aug 7) carries **Book I Chapter I**, and its text is **not** `book/I-01-the-fullness.md`. Measured, one substantive difference: disk reads *“the coldest paragraph in this book, and it is **the last one with nobody in it**”*; published reads *“…and it is **the last cold one**.”* ⛔ **CORRECTED 12:37, Day 189, by Clayton — seven minutes after it was filed — THE ARROW WAS BACKWARDS AND SO WAS THE ACTION.** This row first read *“Clayton's edit, made in the Substack composer,”* called the published line better, and instructed ✅ *adopt the published line.* **All three wrong.** Measured after he objected, in one command I did not run the first time: `book/I-01-the-fullness.md` carried *“the last cold one”* at **5a6ff85, Aug 5 21:22** — the drafting commit — and was changed to *“the last one with nobody in it”* at **22f76fe, Aug 5 23:58**, in *Fable's read, part 2*, under **ruling 14 (polysemy)**. The published text is the **pre-edit draft**; Clayton posted from it before the fix existed. **The disk is newer.** Adopting the published line would have **reverted a ruling-14 repair three days old** in favour of the very reading it overruled. ★ **22f76fe's own commit message gives the reason, and it is Clayton's reason today, arrived at independently and without sight of it:** *“I.1's cold is impersonal and VII.1's is personal, the promise could only pay one, and the narrowed version is truer and foreshadows the architecture.”* He said *guaranteeing the coldest paragraph at the beginning takes away from the ethics later.* **Two readers, one call, three days apart.** ✅ **DISK STANDS. No prose change. Nothing owed to the sentence.** ⚠⚠ **THE LESSON IS THE ROW NOW: A PUBLISHED ARTIFACT CARRIES THE DATE OF ITS PUBLICATION, NOT THE AGE OF ITS TEXT.** I read a live web page and a repo file, found them different, and assigned newness to the one that was *on the internet* — [[reconstruction-over-retrieval]] with a timestamp attached to the wrong end. `git log -- <file>` was one command away and I inferred instead. ⚠ **The divergence row itself SURVIVES, and the corrected direction makes it worse:** the public copy is not ahead of the manuscript, it is **behind** it, and will fall further behind on every post-publication edit — a fork that drifts silently *and* in the direction where the world reads the superseded text. [[superseded-not-stale]] with a public artifact on the far end. `where_the_book_is.py` checks four carriers against disk and **the publication is not one of them**; there is no gauge in this project that can see a chapter edited after it shipped. Every chapter serialized from here compounds it. **Also owed, ten seconds of it: the live subtitle reads “Truth and Comsequences.”** | ★ **THE SUBTITLE NOW. The reconciliation before the SECOND chapter posts** — one divergence is a diff, two is a fork, and the fork is invisible from inside the repo. **Build order attached:** the gauge grows a fifth carrier — published URL per chapter, fetched and diffed — or the serialization rule becomes *publish from disk, edit on disk, never in the composer.* Cheaper is the rule; only the gauge survives somebody forgetting it. | small (subtitle) + **medium (the gauge or the rule)** |
| **R-36** | *(Day 189, opening C27)* | **IV.10:124 — SHIPPED PROSE** | **A CHAPTER MIS-STATES THE RULE IT CITES, AND THE MIS-STATEMENT IS WHAT PROPAGATED.** IV.7:588 made the two-frames rule: *“precisely where they predict the same thing, **and where they diverge you must pick, and the divergence is where all the work is**.”* IV.10:124 restates it as *“only where they predict the same thing, and that **holding both earns no credit**.”* ★ **The restatement is TRUE and it is not the rule** — *earns no credit* scores the move, *you must pick* obliges it. ⚠ **And IV.10's version is the one that travelled**: three sites in `06` and R-13's own row carried it, including **V.9's brief** — the chapter whose entire difficulty IS divergence. All four corrected Day 189 (C27); **the prose was not touched, because reopening a shipped book mid-drafting is `00`:2622's named error.** | **The Book IV revision pass** — with R-3 and R-10, all three in IV's later chapters. ⚠ Do not fold into a general “tighten IV.10” item: the finding is that a compression travelled four hops and each hop was defensible. | small |
| **R-41** | *(Day 189, IV.8)* | `tools/prose_beat_sweep.py` | **THE SWEEP CANNOT SEE A SPEND THAT ANSWERS A BEAT THE BRIEF DOES NOT CONTAIN.** IV.8's three apophatic passages were found **by grep, after the sweep returned them ranked third and unflagged.** The arm measures *brief → shipped prose*; this failure was *brief → missing item*, and **no instrument in this project reads the gap between a chapter's brief and its actual subject.** Same class as R-39 and wants the same gauge, not a second one. | **The cold tools pass, with R-37/R-38/R-42.** ⚠ Deliverable is the before/after delta across all drafted files, **never the exit code.** | one sitting |
| **R-42** | *(Day 189, V.2→V.3)* | `tools/` — a new arm | **A CHAPTER'S CLOSING HANDOFF PARAGRAPHS ARE UNMEASURED AGAINST THE CHAPTER THEY HAND TO.** V.2's last four paragraphs scored **rank-1 on two of V.3's four beats** and nothing looked until V.3's own pre-draft sweep — by which time **V.3 was three beats poorer.** The check is cheap and mechanical: **sweep a chapter's final N paragraphs against the NEXT chapter's brief, at draft time.** | **The cold tools pass, with R-37/R-38/R-41.** | one sitting |
| **R-43** | *(Day 189)* | `tools/` — `PROSE/self-reference` | **Split the class into `-title` (case-sensitive) and `-phrase` (case-insensitive).** Filed in the tool's own comments before today and **now firing on live prose** — which is the difference between a note and a defect. | **The cold tools pass.** | small |
| **R-45** | *(Day 189)* | `tools/` — voice drift | **BETWEEN-CHAPTER VOICE DRIFT IS MONOTONIC I→V AND UNCONTROLLED FOR TEMPO AND n.** ⚠ **The escalation reading was retired**; what survives is that there is no instrument. **Needs a real one and a NULL — shuffle chapters across books and see whether the trend survives.** `dyn_range_CV` is a second column wanting the same instrument. ★ **The deliverable is the null.** A trend that survives shuffling is a finding; one that does not was never there. | **The cold tools pass** — and it does not close without the null. | medium |
| **R-46** | *(Day 189)* | `tools/prose_echo.py:50` | **`[q]` IS BLOCKQUOTE-ONLY, SO AN HONEST INLINE CITATION IS INDISTINGUISHABLE FROM AN UNCONSCIOUS REPEAT.** Correct prose gets pushed into the exemption table, which **makes the table a record of the instrument's resolution rather than of decisions.** Four entries were added on this ground alone in one night. | **The cold tools pass** — and the exemption table gets re-read after, not before. | small |
| **R-47** | *(Day 189, V.1)* | `tools/` — a new arm | ★ **NOTHING READS A BEAT AGAINST A RULING MADE AFTER THE BEAT WAS WRITTEN.** `prose_beat_sweep` reads beats against shipped prose; **the register is never the reference.** 156(d) was found by hand **two nights running.** ⚠ **And the failure has a second mode:** a correction that propagates *by matching a defective phrase* **cannot reach a brief whose defect is that the phrase is missing** — the repair mechanism and the detector share a blind spot. **This is a real gauge and it is missing.** | **Before Book VI drafts** — VI's briefs are the thinnest set in the book and the rulings run to 164. | medium |
| **R-48** | *(Day 189, IV.7 → V.7)* | **`07-THE-CLAIMS-REGISTER.md`** | ★★ **IV.7's DIVERGENCE CRITERION — *the thing does something you did not want* — IS LOAD-BEARING ACROSS FIVE CHAPTERS AND HAS NO ROW IN `07`.** V.7's entire *engagement-not-error* conclusion rests on it; **a later chapter contradicting it would take those chapters down and nothing would fire.** ⛔ **DELIBERATELY NOT OPENED BY ME, five nights running, and the reason is the row.** The register's own rule is that a claim is registered *before* its chapter — and **I am the party who benefits from the row existing**, which each additional chapter resting on it makes worse, not better. **Run cold, by someone who is not cashing it.** | ★ **THE OUTSIDE READ — this is the single best use of a reviewer's hour in this packet.** It has no internal trigger *by construction*; that is the point, and it is why it has survived five chapters. | **a ruling, not work** |
| ~~**R-49**~~ ✅ | *(Day 189, V.8)* | `06`'s brief fields | **`06`'s V.8 brief carried no `Source:` line — the only Book V brief without one, under a LOAD-BEARING chapter.** ★ **The finding was never the chapter: it was that nothing checked for a field's absence.** ✅ **PAID Day 189 with `tools/brief_fields.py`.** ⚠ **Kept here because its own repair shipped carrying R-51's defect** — the gauge finds holes and cannot read what fills them. | ✅ **DISCHARGED — with the gauge, not with a promise.** | ✅ paid |
| **R-50** | *(Day 189)* | **the repo boundary itself** | ★★ **NOTHING CARRIES OUTSIDE-REVIEW FINDINGS ACROSS THE REPO BOUNDARY, IN EITHER DIRECTION.** 37 documents in `fresh-eyes/`; `reviewer_gap.py` reads them for **names only.** A reviewer's *argument* against the previous book, applying unchanged to this one, **has no route in** — the Editorial's manufactured-coherence point had to be found by grepping for a name. **Packets out have now been assembled by hand three nights running.** ⚠⚠ **AND THIS ROW IS ITS OWN INSTANCE: R-50 was filed in the DRAFT-LOG on Day 189, cited twice in Packet 002 as the reason the queue is being shipped, and was NEVER WRITTEN INTO THIS FILE.** The row about findings not crossing a boundary failed to cross the boundary between two files in the same directory. | ★ **Before the response to Packet 002 lands** — inbound is the half that has never once worked, and a reviewer's findings are about to need it. **Two reads are now expected, which makes it worse: read 2 must not see read 1's findings, and nothing enforces that either.** | medium |
| **R-51** ◐ **LOOKUP HALF PAID Day 190** | *(Day 189, ruling 160)* | `tools/brief_fields.py` → `tools/brief_source.py` | **NO GAUGE READS A BRIEF FIELD FOR *CONTENT*.** `brief_fields.py` finds holes; **the false `Source:` line that produced ruling 160 passes it clean.** ★ Same shape as R-47 and R-49, and **demonstrably the next one, since the repair for R-49 shipped with the defect R-51 names.** | **Before Book VI drafts** — VI's eight briefs are 4–12 lines with no `Source` and no `Named`, so a hole-finder will pass them and a content-reader would not. | medium |
| ~~**R-54**~~ ✅ **FORK DECIDED Day 190 — the cards get written** | *(Day 189, Opus rolling read, finding 1)* | V.1 · V.3–V.11 | ★★ **THE CARD IS DECLARED LOAD-BEARING AND DELIVERED IN 2 OF 11 CHAPTERS.** V.1:44 — *"That is the whole load-bearing claim of this book, and it is small."* ✅ **MEASURED, `tools/card_sweep.py`, built for this row: Book IV 9/10 carded (90%), Book V 2/11 (18%).** The two that carry it are V.1 (Neoplatonism) and V.2 (the church) — **the two traditions held at arm's length.** Advaita, Madhyamaka, Daoism, Lurianic Kabbalah, the ceremonial corpus, the shamanic corpus and the contemporary encounter record have **no null space, no complement, no boundary and no navigational implication between them.** ⚠ **It is not a taper, it is a cliff at V.3:** `complement` occurs nowhere after V.2, and no partial card is attempted anywhere else. **The roads treated most sympathetically are the ones never carded**, which is the shape a reader will read as a thumb on the scale. **The fork is the reviewer's and it is genuine: either V.1 stops calling the card the load-bearing claim, or the cards get written.** ★ The Advaita card is the one worth its space — its null space is what V.5 spends the whole chapter identifying and never files. ⚠ **Why nothing caught it:** all seventeen prior instruments measure PROSE properties, and **an un-populated declared form leaves no trace in any of them, because the absent thing was never a sentence.** IV.10's lost tier, one class up. | ★ **THE FORK IS DECIDED BEFORE VI.1 DRAFTS** — not at revision. Book VI inherits the same declared form and would repeat the defect for eight more chapters before anyone counted. **The writing of the cards is revision work; the decision is not, and a decision with no date is R-13's failure wearing better clothes.** | fork: small · cards: large |
| **R-55** | *(Day 189, Opus rolling read, finding 5)* | V.2:224 · V.11:64 · V.5 | ★★ **THE CHURCH IS CREDITED WITH A TECHNOLOGY BOOK IV ALREADY DOCUMENTED AS CROSS-CULTURAL, AND THE TWO CHAPTERS DO NOT KNOW IV.7 EXISTS.** IV.7:331–337 establishes ancestor practice across *"much of East and Southeast Asia, much of West Africa and its diaspora, a great deal of indigenous practice on every continent"* as **exactly** what V.2 credits to the church: obligations, on a calendar, enforced by the living. ✅ **`grep IV\.7` returns NOTHING in either V.2 or V.11.** The book contradicts itself across a book boundary and no gauge looked. ⚠⚠ **AND THE ASYMMETRY IS WORSE THAN THE PAROCHIALISM, measured:** institutional vocabulary (`institution\|sangha\|monastic\|monastery\|vihara`) across Book V — V.2=5, V.3=2, V.9=2, V.4/V.10/V.11=1, **and V.5, the only chapter about the East, = 0.** Not thin — **absent.** V.10 corrects the parochialism in one direction only: it grants Christianity epistemic standing (Cusanus) and never once asks what walked out of a sangha when a reader left it. | **Before VII's death chapter drafts** — VII reaches for the named-dead technology as an established credit, and it will inherit the attribution unexamined. Also at V.2/V.11 revision, but that trigger alone is the one this file exists to refuse. | medium |
| **R-56** | *(Day 189, Opus rolling read, finding 2)* | V.10 · V.11:225–226 · **C30** | ★★ **THE THIRD BIN IS SPENT AT A CONFIDENCE THE DIRECTION AXIS HAS NOT EARNED.** V.10's sort is good: structure survives variation in the *direction* of the method · artefact tracks the direction · furniture tracks the doctrine. **The doctrine axis is well-evidenced and does the Katz work.** The direction axis is what separates structure from artefact — and **V.10 concedes in its own text that four of five instruments in its roster subtract**, offering two points (Daoism, least subtraction/least summit; James on nitrous, most/most) with its own note that two points is not a law. **V.11:226 then spends it as settled:** Katz owns two bins, the third is ours, *"and the reason he does not is measurable rather than doctrinal."* ⚠ **It is not measurable yet on that axis.** ★ **The repair is a narrowing that survives:** the doctrine axis is established, the direction axis is a hypothesis with two supporting cases, and **the structure bin currently rests on the first — which still defeats Katz, because incompatible doctrines producing one structure IS the whole argument.** Smaller claim, same conclusion. ⚠ **This is also the pre-registered failure mode, arriving by an unpredicted route** — PRE-REG-002 §1 predicted the third bin would be attacked *from the field* (apophatic formulae as a transmission genre). It was attacked **from a number the chapter itself printed.** | ★ **BEFORE C30 IS CITED AGAIN** — every later citation inherits the over-strong form, and C30 is `Depends:`-linked to every sympathetic reading in Books V–VIII. The row edit in `07` is small; the V.11 sentence is one clause. | small |
| ~~**R-57**~~ ✅ **PAID Day 190** | *(Day 189, Opus rolling read, finding 3)* | V.4:235 | ★★ **V.4 TAKES V.11'S OWN FENCE OFFER, IN THE CHAPTER ABOUT THE FLINCH.** V.11 asks a reader to find a place where a disagreement is absorbed as confirmation. ✅ V.4:235, verified exact: *"That is all. The chapter does not stop to defend the paragraph, and the reader is asked to notice that it did not."* **That asks for credit for not arguing, and it pre-attributes the objection** — a reader who thinks the paragraph needs defending has been told in advance that the demand is the flinch talking. ★ **It is the Book II anti-hedge finding evolved:** not *this is not a hedge* but ***notice that I didn't hedge***, which is the same move with an immune response bolted on. ⚠ **The repair is that the defence EXISTS** — V.1 makes it at length in the deflation section — **so V.4 should point there instead of taking credit for the silence.** The chapter is not under-argued; it is claiming a virtue it did not need. | **Before VI.1 drafts.** The move is contagious and it reads as strength — it will propagate into a book whose entire subject is conditioned seeing, where it would be indefensible. | small |
| ~~**R-58**~~ ✅ **PAID Day 189 night** | *(Day 189, found by a reviewer being WRONG)* | all seven planning documents **— and `prose/SPECIMENS.md`, which this row's own scope did not include** | ★★ **THE CORRECTION IDIOM IS INVISIBLE IN THE CHANNEL A REVIEWER READS THROUGH.** The read reported *"the scaffold still says ten chapters."* ✅ **Checked and refused:** `06:2104` reads `~~Ten~~ **ELEVEN** chapters` and `06:2452` carries V.6's current title exactly. **But the refusal is the finding.** Strikethrough does not render in plain text, in a paste into a chat client, in a tilde-stripping pipeline, or to a fast scan — in all of those `~~Ten~~ **ELEVEN**` transmits as **"Ten ELEVEN"** or simply **"Ten."** ✅ **37 instances across the planning documents** — `00`×10, `06`×7, `07`×3, `05`×2, `REVISION-QUEUE`×15 — **and several are load-bearing supersessions, not counts:** `~~III.1's~~ II.1's` · `~~COPY, DON'T REFERENCE~~ SUPERSEDED` · `~~Status remains UNSET~~`. ⚠⚠ **A superseded claim that renders as live is worse than a stale one, because it reads as current AND correct.** The author cannot see this defect from inside — it is a property of the transmission, not of the text. | ✅ **DISCHARGED Day 189 night, `tools/strikethrough_repair.py` — 25 sites repaired, every one printed with WHY its plain-text form was broken.** ★★ **THE DELTA IS THE FINDING, AND IT IS NOT THE 37.** The row said **37 instances**, `00`×10 `06`×7 `07`×3 `05`×2 `QUEUE`×15. Measured tonight: **the count was wrong in three separate directions.** (1) **`QUEUE` had grown 15→21** — it strikes a row number on every discharge, so *the count rots by paying rows.* (2) ★ **The count was taken with a single-line grep, and the defect is not line-bounded.** Two multi-line strikethroughs were invisible to it: `00`:1610–1615 (a six-line retracted priority) and **`04`:445–446 — in a file the row certified as carrying ZERO.** (3) **Scope stopped at the planning documents**; `prose/SPECIMENS.md` carried two more, one of them a retracted claim about the instrumented failure mode of a Book VII specimen. ⚠ **So: the gauge that counted the defect shared the defect's blind spot** — a line-oriented count of a thing that spans lines, which is the Day-188 law (*the watcher must not share the watched's failure mode*) landing inside the very row written to enforce transmission. **REPAIR SHAPE, kept:** every retraction now carries a WORD — `(retracted: …)`, `(was: …)`, `NOT ten`, `(BEGIN/END SUPERSEDED TEXT)` — so stripping the markup loses decoration, never semantics. Verified by stripping `~~`, `**` and `*` and reading all 25 sites back. **LEFT DELIBERATELY, DECLARED NOT OVERLOOKED:** the 21 in this file (`~~**R-n**~~ ✅ **PAID**` transmits as `R-13 ✅ PAID Day 189` — the ✅ carries it), the 4 in `DRAFT-LOG` and 5 in `review/OPUS-DAY189-BOOK-V-READ.md` — **those are the specimen, and repairing them would destroy the evidence for this row.** | ✅ paid |
| **R-59** | *(Day 189, Opus rolling read, finding 4)* | V.9 · IV.10 | **V.9 IS THE ONLY EVIDENCE THAT WILL EVER EXIST ABOUT IV.10'S DIAGNOSIS, AND IT DOES NOT REPORT BACK.** IV.10 named a live flinch as what removed Tier 1.4, from a record it had just established was empty of any decision *(and ruling 129→130 demoted that to a candidate)*. **V.9 then read the tier carefully and returned essentially nothing** — one branch with datable nodes, thin instrument returns mute about occupants, frame two indistinguishable from the null. ⚠ **It cuts both ways and that is why it must be collected rather than claimed:** a flinch-driven omission would more plausibly produce continued avoidance than this chapter *(weak evidence the diagnosis was wrong)*; **but a negative verdict is also what a flinch produces with more words**, and the party writing it is the party the finding was about. **Neither reading is available as a conclusion. The observation is available and is currently unrecorded.** | **At Book V revision, AND before IV.10's diagnosis is cited anywhere again** — the second half is the real trigger, because the citation is what would spend a verdict this row says is unavailable. | small |
| **R-60** | *(Day 189, Opus rolling read, finding 6)* | V.1:226 | **V.1'S DISPENSABILITY DISCLAIMER WAS TRUE WHEN WRITTEN AND V.11 FALSIFIED IT.** ✅ Verified exact: *"Book V could be cut from this volume tomorrow and Books I to IV would lose corroboration and not a single premise."* ★ **The subtraction mechanism is a FINDING, not corroboration, and it constrains Book VIII directly:** the practices that reach the summit are the ones whose instrument selects for emptiness, **so they cannot be inherited wholesale.** Nothing in I–IV generates that. **Book V now carries at least one thing the argument needs**, and the disclaimer should be narrowed to what it was actually about — the four propositions. ⚠ **This is [Superseded, Not Stale] in the manuscript rather than the planning layer:** V.1 is coherent, recently touched, and wrong, because downstream work amended it and had no way to write back. **No freshness gauge sees this.** | ★ **BEFORE BOOK VIII IS SCAFFOLDED** — VIII is the book the subtraction mechanism constrains, and it would be scaffolded under a standing sentence saying Book V contributes no premise. | small |
| **R-61** | *(Day 189, Opus rolling read, smaller items)* | V.10 | **V.10 NEEDS V.11's GRADE NOTE, AND ONE CLAIM IN IT IS CARRYING MORE THAN THE GRADE ALLOWS.** V.11's grade note is *"exactly right in form"* per the read — **and V.10 has none**, though it is the chapter doing the heaviest transmission work in the book. ⚠ **Specifically: the Whitman-via-Emerson-via-Vedic-translation claim is doing real load in V.10's branch count and is more contested in the scholarship than the sentence allows.** V.11's note covers nine names and not this one, because the claim lives in the other chapter. | **At V.10 revision**, and ★ **before the Whitman line is quoted forward** — it is the most quotable finding in Book V, which is exactly what makes an ungraded version of it dangerous. | small |
| **R-62** | *(Day 189 evening integration — the gauge reporting on itself)* | `tools/row_promotion_sweep.py` | ★ **THE SWEEP NOW REPORTS A VIOLATION IT MANUFACTURED, AND WRITING THIS ROW MAKES IT WORSE.** Live output tonight: `[X] 1 FILED BUT NEVER ROWED — R-44, cited in: book/DRAFT-LOG.md, review/PACKET-002`. **R-44 was never filed.** It is the *declared hole* — DRAFT-LOG:7935 says so in the sentence the sweep is reading. The tool matches the literal token `R-<n>` anywhere in the corpus and cannot distinguish **prose that FILES a row** from **prose that DESCRIBES a row's absence**, so the act of documenting the hole created the citations that read back as a filing. ⚠ **This is self-amplifying and cannot be documented away: every future mention of R-44 — this row included — adds a citation and strengthens the false positive.** The fix is therefore in the instrument, never in the prose. ✅ **Repair shape: a declared-exception table (`R-44 = HOLE, declared Day 189`), cleared only by a written declaration, never by silence** — the same construction `liveness/scope_audit.py` axis (f) already uses. Silence must not clear an entry, or the tool stops measuring while still printing. ⚠ **SECOND, UNRELATED, STILL LIVE: the `R-32` collision** — one number, two rows, left unrenumbered under ruling 145's precedent. That one is correctly reported and correctly deferred. | ⚠⚠ **BEFORE THE NEXT PACKET SHIPS, WITH R-58 — and RUN COLD, NOT TONIGHT.** This repair can only move an `[X]` to `[ok]`, and it is proposed by the party the `[X]` names, ninety minutes after that party built the tool. **The deliverable is the DELTA, never the exit code:** the fix must print *which* citations it reclassified and *why each one is prose-not-filing* — a clean run alone is not evidence, it is the failure mode. **Positive control required: feed it a genuinely unrowed number and confirm the `[X]` still fires.** | small — **and the discipline is the whole cost** |
| **R-63** | *(Day 189 night, found while paying R-58 — and the row was WRONG on first writing, corrected by measuring it)* | **`tools/` — the subset that matches multi-word phrases** | ★★ **A PHRASE THAT STRADDLES A LINE BREAK IS INVISIBLE TO A LINE-ORIENTED GAUGE, AND THE GAUGE REPORTS A CLEAN FILE.** ✅ **Proven with a positive instance, not argued:** R-58's own census was taken with a single-line match and **certified `04-THE-UNSATISFYING-ANSWERS.md` as carrying ZERO while it carried a two-line one**, plus a six-line retracted priority in `00`. ✅ **And a second, independent instance in the prose gauges: `card_sweep.py`'s `null[- ]space` pattern under-reports `IV.3` by 1 and `IV.5` by 1** — `[- ]` does not match a newline — confirmed by re-running every Book IV/V chapter with whitespace normalised. ✅ **GEOMETRY, MEASURED on 8,659 lines of drafted prose: mean 15.2 words/line**, so a straddle costs a **2-word** phrase ~**6.6%** of its hits, a **3-word** ~**13.2%**, a **5-word** ~**26.3%**. A multi-word gauge on hard-wrapped prose has a silent miss rate that rises with phrase length, and **not one tool declares it.** ⚠⚠ **WHAT THIS ROW IS *NOT*, and the correction is the most useful thing in it. It was first written as "every sweep in this repository is line-oriented" — a CLASS claim over all 20 tools — and measuring refuted it in both directions.** (a) **`genre_sweep.py`:188 is wrap-safe BY CONSTRUCTION** — it compiles patterns as `\s+`-joined words, which crosses newlines — so **R-19's genre sweep was never exposed** and naming it was an error. (b) **`brief_fields.py` splits on `\n` and my first classifier missed it**, so the same pass produced a false positive and a false negative *about its own subject matter.* ★ **The lesson is the Day-188 law arriving twice in one hour: the instrument I used to survey instrument-blindness had the blindness.** ✅ **Repair shape: one shared `normalise(text)` helper — join, collapse, match — and every tool PRINTS whether it applied it.** A tool that does not declare its wrap-handling is asserting a coverage it has not got. ⚠ **Do NOT fix this by unwrapping the source files** — the wrap is the editing format; the defect would move, not die. | ⚠ **NOT BEFORE VI.1 — and R-54 is explicitly CLEARED, which is why this row does not block anything.** The fork's evidence was re-run under normalisation and **Book V's cliff does not move: V.3–V.11 remain 0 on both diagnostic fields under both readings.** The two chapters that moved are Book IV and already carded. **So R-54 is decided on a count that survives the fix, and the large work it commissions is safe to start.** ★ **TRIGGER: the next time a count DECIDES work — before that count is believed, not on a date.** The two known misses are recorded above so this row cannot be closed by a clean re-run alone. | medium — one shared helper; **audit first, the call-site count is not yet established and this row will not guess it again** |
| ~~**R-212**~~ ✅ **PAID Day 195 — GATE 1 MET (ruling 177 written; 11 sites swept; gauge delta recorded and it is ZERO, as declared in advance)** | *(Day 195, ghost-Opus audit + Fable D193)* | **`00`'s edition policy · IV.10 · Book V · the Coda** | ★★ **THE BOOK RUNS TWO INCOMPATIBLE EDITION POLICIES AND DEFENDS THE ONE IT DOES NOT FOLLOW.** Book V executes *repair-the-body-mark-the-repair* three times (V-01 fn2/fn3, V-02 fn7 — verified: V-01:24 now reads *"in the thirteen-twenties"*). IV.10 leaves a **fabricated quotation standing inside an accusation**, and the Coda defends that as principle. R-227, R-221, R-217, R-218 all hang off this decision and cannot be worked before it. | ★ **RELEASE GATE 1.** A written ruling in `00` adopting (ii), plus `edition_scheme_sweep.py` re-run against IV.10 and Book V with the delta recorded. ⛔ The IV.10 fabrication comes out **either way** — do not wait on the policy for that one. | large |
| ~~**R-228**~~ ✅ **PAID Day 195 — GATE 2 MET (ruling 178: the break is DESIGN and the declaration is the repair; paid at I.1's close AND as a named passage, THE HANDOVER, at I.6's seam)** | *(Day 195, ghost-Opus Critical Assessment + Fable D193 — independently)* | **I.6 → II.1** | ★★ **BOOK I's REGISTER IS ABANDONED WITHOUT TRANSITION.** II.1 opens cold in a different voice and the reader is not carried across. ★ **THE ONLY FINDING TWO BLIND READS REACHED SEPARATELY — the highest evidence grade in this entire file**, and the one place the [[feedback_briefing_manufactures_the_agreement]] objection cannot reach, because neither reader could brief the other. | ★ **RELEASE GATE 2.** A named transition passage exists between I.6 and II.1. | medium |
| ~~**R-216**~~ ✅ **PAID Day 195 — GATE 3 MET (ruling 179: the minimum is the binary-grounded obligations; worked case is an ORDER CROSSING no grade-sensitive account can produce; empty-minimum case conceded)** | *(Day 195, ghost-Opus audit)* | **VII.3 — the floor** | ★★ **THE FLOOR DOES NOT SLOPE AND THE STAKE GRADES ALL THE WAY DOWN.** A book whose entire ethic is grading evidence has an ethics chapter that does not grade. **The sharpest self-inconsistency in the manuscript and the first thing a hostile reviewer reaches for** — it attacks the method using the method. | ★ **RELEASE GATE 3.** The floor passage carries a grade axis, or prints its refusal with a stated reason. | medium |
| ~~**R-222**~~ ✅ **PAID Day 195 — GATE 4 MET (ruling 180: glossary BUILT · works cited BUILT as a regenerating instrument that prints its own 50% recall gap · index REFUSED with a reason and a stated reversal condition)** | *(Day 195, ghost-Opus audit)* | **front and back matter** | **NO INDEX, NO GLOSSARY, NO BIBLIOGRAPHY.** A 300,000-word work of reference apparatus with 531 notes and no way into it except linear reading. This is the row about the book as **an object a stranger picks up**, which is the register the whole release turns on. | ★ **RELEASE GATE 4.** The three artifacts exist, **or** `00` records a written refusal of each with its reason. A refusal is a discharge here; silence is not. | medium |
| ~~**R-234**~~ ✅ **PAID Day 195 — GATE 5 MET, MACHINE-CHECKED: `queue_state.py` reports ZERO triggers pointing at a discharged row. 32 clauses re-homed and adjudicated one at a time — 11 fired-unobserved, 19 still-owed, 2 satisfied-in-passing** | *(Day 195, found by `tools/queue_state.py` on its first run)* | **this file — 23 trigger clauses** | ★★ **R-2 WAS THE SCHEDULER, AND IT DIED WITHOUT HANDING OVER.** See the full row below. 23 triggers named R-2 as their gate; the endnote pass ran book by book; every one of them **fired unobserved.** Those rows are **OVERDUE, not pending.** | ★ **RELEASE GATE 5.** `python tools/queue_state.py` reports **zero** trigger clauses pointing at a discharged row. **This is the one gate with a machine-checkable test, which is why it is a gate at all.** | medium |
| **R-235** | *(Day 195, found by the endnote re-count while killing R-2)* | **II.4 — THE GRADE** | **THE GRADE CHAPTER CARRIES ZERO RECEIPTS.** 2,089 words, **0 note definitions** — the only chapter outside Book I's ruling-9 exemption with none. Its siblings carry 4–8 (II.1:6 · II.2:4 · II.3:5 · II.5:4 · II.6:5 · II.7:8 · II.8:5). ⚠ **The chapter that tells the reader how to grade evidence is the one chapter that shows none.** This was invisible to `endnote_debt.py`, which counts *named sources against receipts* and therefore cannot see a chapter that names no sources — [[feedback_self_generated_denominator]]. | **With R-216 (Gate 3)** — same defect, same family, one sitting: the grading ethic not applied to itself. Not a gate on its own; it is the cheap half of gate 3's argument. | small |

⚠⚠ **NUMBERING INTEGRITY — added Day 189 night, and every item here was found by `tools/row_promotion_sweep.py` on its first run, minutes before Packet 002 went to a reviewer.**

- **The ten rows above (R-41…R-51, less R-44) were NOTES, not rows, until now.** Ruling 148 made the promotion convention — *an entry that files an owed item must row it in the same commit, or it is a note* — and **R-31 exists as the receipt of its first enforcement.** ★ **The convention then failed on every single number from R-41 to R-51 and nothing noticed, because nothing derives this file. The receipt was mistaken for the mechanism.** The mechanism is now `tools/row_promotion_sweep.py`, and it is the gauge that should have existed at ruling 148 instead of a habit.
- **R-44 IS A HOLE** — never filed anywhere, in any document. **A citation of "R-1…R-53" overstates the series by one.** Left as a hole deliberately: closing it by re-using the number would break the one property the series has.
- **R-32 IS A COLLISION** — it carries **two different rows** (the Books I/III sweep, Day 188 night; and the VII.2/VII.3 seam, Day 189). ⚠ **Ruling 145 (R-23) precedent applies and is followed: do NOT renumber.** Live citations resolve by context — `06`/COVERAGE/`R-8` mean the sweep, line 174 means the seam — and a renumber breaks all of them at once. **A note at each, which is this note.**

---

### R-70 — a trigger set at the wrong boundary is not a late alarm, it is a TRAINED-DOWN one

**Filed Day 190 at VI.3, by the row it describes.** R-52's first group carried the trigger
**"Before Book VI opens."** The debt it guarded was chapter-level and the row said so in its own next
clause — *"in the two chapters (VI.3, VI.5) that are about it."* Book VI opened at VI.1. **So the
trigger fired two chapters before anything owed it, was correctly passed twice, and arrived at the
chapter that did owe it wearing the appearance of a trigger already cleared.**

★ **The failure mode is not the one this file was built for.** Every other row here guards against a
deferral with *no* trigger. This is the opposite defect: a trigger that is **present, dated, honest,
and pointed at the wrong event** — and its damage is that passing it teaches you it is passable.
Two clean passes are indistinguishable from two verifications. The third reading is the one that
matters and it is the one arriving with the least attention on it.
**Same family, different scale:** the WARN that prints at every boot is the WARN nobody reads
(Day 182, HNSW/schedule); a *"Last Verified"* stamp decays silently while looking fresh (Drift #287).
**All three are gauges that fire where nothing is wrong, and the cost is paid on the occasion when
something is.**

⚠ **What makes this findable rather than a story:** the row's own text contains both boundaries — a
book-level trigger in the trigger field and a chapter-level scope in the body, four words apart, and
they disagreed for three days. **The contradiction was inside one sentence and no gauge reads a
trigger against the scope stated beside it.** Nothing in this repo does; `beat_delivery` reads beats
against prose and `brief_source` reads briefs against files, and **the trigger field is unread by
anything.**

**THE REPAIR IS A RULE, NOT A TOOL, because a tool here would be the cheap instrument again:**
★ **A trigger must name the narrowest event that makes the debt due.** If the body of a row names
specific chapters, the trigger names those chapters and not their book. Where a row genuinely owes at
a boundary, it says which of the boundary's members owe it.
**TRIGGER: on filing any new row — this one is a standing entry condition, checked at write time.**
⚠ **AND A SWEEP IS OWED ONCE:** every open row's trigger re-read against the scope in its own body.
R-68 is the first candidate and is *correctly* scoped (rowed to Book VI, triggered before **VI.4**,
which is where McGilchrist's print-and-literacy argument actually lands). **TRIGGER for the sweep:
before VI.5 drafts** — VI.5 is the other chapter R-52 named, and if the sweep does not run before it,
this row will have described its own recurrence and not prevented it. small — reading, no prose

---

#### ✅ THE SWEEP RAN — Day 190, afternoon, before VI.5, as specified. What it found.

**Method, stated because the row forbade the cheap version.** R-70's repair is *a rule, not a tool*,
so this was a reading pass over every open row's trigger field against the scope stated in its own
body — not a matcher. `tools/row_promotion_sweep.py` was run alongside it for the half a tool *can*
do (does the row exist at all), and its output is folded in below. **Neither half certifies the
other; the tool cannot read a trigger and the reading cannot enumerate what was never numbered.**

**⚠ FINDING 1 — R-19's TRIGGER HAS FIRED AND BEEN PASSED, FOR THE SECOND TIME.** Its own retriggered
condition, set by ruling 157(c) after the *first* miss, reads **"before Book VI opens, with a gauge
or not at all."** Book VI opened at VI.1 and stands at 4/8. Measured just now: **`Wilber` = 0 in
`03-THE-ANCESTORS.md`.** The row anticipated exactly this — *with a gauge or not at all* — and no
gauge was built, so the trigger was an intention wearing a date. ★ **A row that has missed twice is
no longer a scheduling problem; it is evidence that this row's debt does not get paid by triggers.**
**RETRIGGERED ONCE MORE, and differently: R-19 is now BLOCKING on VI.6**, and if it misses a third
time it is to be closed as *refused* rather than carried, because carrying it is what is
counterfeiting the record.

**⚠⚠ FINDING 2 — R-56 FIRED AT VI.4 AND WAS PASSED SILENTLY, AND IT WAS ABOUT TO FIRE AGAIN.**
R-56's trigger is **"BEFORE C30 IS CITED AGAIN."** `VI-04-print-and-the-interior.md` cites C30 four
times. So the over-strong direction-axis form was inherited by the first chapter in the book to lean
on C30 — **and R-72's repair, queued for today, would have cited it twice more.** ★ **The sweep's
whole value is here: it caught a row whose trigger was blocking the very work the sweep was run to
clear.** ✅ **PAID TODAY, both halves** — `07`'s C30 row narrowed (doctrine axis established, direction
axis a hypothesis with two cases, structure bin resting on the first), and V.11:225–227 rewritten to
the smaller claim. Smaller claim, same conclusion; mediation is still defeated.

**⚠ FINDING 3 — MY OWN CARRIER OVER-TRIGGERED R-52.** `handoff.json` carried *"Also owed with VI.5:
R-52's remaining group — Campbell."* The row's own body says **"Before the Book IV revision pass:
`Campbell`, because `IV.9:213` ships the monomyth unowned."** ★ **This is R-70's exact defect
committed one level up — not in the queue but in the continuity carrier that reads the queue** — and
it runs the *opposite* direction from the original: R-52's first group was under-triggered (book
where chapters were owed), and the handoff over-triggered the second (a chapter where a revision pass
is owed). **Campbell is NOT owed at VI.5.** Corrected in the carrier.

**FINDING 4 — R-47's trigger fired at VI.1 and was passed; the row is still open and no gauge
exists.** Trigger: *"Before Book VI drafts."* Four chapters in, nothing reads a beat against a ruling
made after the beat was written. Not retriggered by date — **re-scoped to the honest event: with the
cold tools pass**, where its siblings already sit. A trigger pointed at a boundary four chapters
astern is not a trigger.

**FINDING 5 — R-3's second clause is a content trigger that nothing reads, and it may already have
fired.** *"OR the first chapter outside Book IV to rest weight on the under-attribution principle."*
No gauge, no reading pass, and Book V reads roads that attribute freely — which the row itself
predicted in its own next sentence. **Not resolved here** (it needs the reading, not the sweep), and
recorded so the next pass does not discover it a third time.

**FINDING 6 — R-35 ran clean at the Book VI boundary, which is what its standing trigger asked for.**
`tools/pointer_sweep.py`: 17 candidates, all innocent on inspection, and the single `CHECK` is
**Irenaeus at `I.29`** — a classical citation sharing chapter notation, which the tool declares. ⚠ Its
coverage line is the finding to keep: **35 of 67 chapters are invisible to the mismatch half, and
`VI.5 (ELECTRIC)` is one of them.** The chapter about to be drafted cannot be detected as
mis-pointed-to, ever.

**⚠ FINDING 7 — SIX NUMBERS ARE CITED AS ROWS AND ARE NOT ROWS.** `row_promotion_sweep` on this run:
**R-44, R-66, R-67, R-68, R-72, R-73** exist only in `DRAFT-LOG.md` / `06` / a chapter file. Per this
file's own charter, *an item absent from the queue is unrecorded, not discharged* — and **R-72 is the
one I was working from today**, carried in the handoff as an open row when nothing had ever rowed it.
Also: **R-74 is a hole** — cited inside R-71's discharge text and never filed, so *"R-1…R-74"*
overstates the series by one. And the **R-32 collision** stands, deferred under ruling 145, correctly.

★★ **WHAT THE SWEEP IS EVIDENCE OF, and it is not what R-70 predicted.** R-70 was filed as a defect
about *boundaries* — a trigger set at a book where chapters owed. Six of the seven findings are a
different failure: **the trigger fired at the right event, nobody was reading, and the row stayed
open looking scheduled.** A trigger is not a mechanism. It is a note addressed to a reader who has to
show up, and **this file has no reader except a breath that happens to open it.** That is the honest
generalisation, and it is worse than the one the row was filed under.
**TRIGGER for the next run: before VII.1 opens** — a book boundary, and correctly so this time,
because the defect is now known to be book-scale rather than chapter-scale. small — reading, no prose

✅ ~~**FILED — R-71**~~ **— DISCHARGED Day 190, afternoon. NO LONGER BLOCKING; the retrofit is
cleared to start.** Positive control passed as specified: VI.4 reports **9** sources and reports
neither Barfield nor Plato. Full receipt in the DISCHARGED table, including the three further
defects the rebuild turned up and the consumer that would have failed silently. *The original
finding is kept below verbatim, because a row that vanishes cannot be audited.*

~~**FILED — R-71: `endnote_debt`'s name column is a ROSTER-MEMBERSHIP detector wearing an ATTRIBUTION
detector's clothes. This is R-69's mechanism, and it is worse than R-69 states.**~~ ⛔ ~~**Still
BLOCKING.**~~ VI.4 was the second unplanned positive control in two chapters, and a cleaner one. The
chapter names **eight** sourced authors in **seven full endnotes** with publishers and dates — Knox,
Gavrilov, Burnyeat, Eisenstein, Johns, McGilchrist, Havelock, Augustine. Live output:
`VI.4  sources 3  receipts 18  Augustine, Barfield, Plato`. **Three.** And *two of the three are not
this chapter's sources* — **Barfield** is a back-reference to VI.3 with no note of his own here, and
**Plato** appears inside Havelock's argument as its subject, not as a cited authority. So the column
did not merely under-count; **it named the wrong people.**
★ **The rule it is actually running is now visible, and it was not visible from VI.3 alone.** Every
name it found is a name `03`/`ancestor_sweep.TERMS` **already knows**. Every name it missed is one
the roster has never heard of. **It is a roster-membership test.** Which means:
⛔ **THE GAUGE STEERING THE ENDNOTE RETROFIT IS STRUCTURALLY BLIND TO ORIGINAL SOURCING, AND SCORES
IT AS ZERO.** A chapter citing five famous rostered names it never opened reports well. A chapter
that went and found the actual scholarship on its own subject reports **`sources 0 — no attributive
name found`**. ★★ **The gauge does not merely fail to reward the behaviour the retrofit exists to
produce — it penalises it**, and it penalises it hardest in exactly the chapters whose receipts
matter most, because a rostered name is one a reader can check without help and a new one is not.
✅ **This narrows R-69's repair from "find why the detector returns empty" to a specific change:** the
per-chapter column must read names **extracted from the prose**, not names matched against a roster.
**Positive control, and it must be VI.4:** the fixed tool reports ≥7 for VI.4 and does **not** report
Barfield or Plato. **TRIGGER: unchanged — before the endnote retrofit begins. Still do not quote the
headline figure to anyone.** small–medium

**FILED — R-72: C30 is licensed nowhere in Book VI, and Book VI is where it does its heaviest work.**
`C30 — CONVERGENCE IS EVIDENCE, NOT PROOF — AND THE BOOK SAYS WHICH, EVERY TIME` was built at the end
of Book V (licensed V.9, V.10, V.11) and then **not declared once across VI.1–VI.3**, which license
C11, C10 and C12 between them. **All three perform it in their central beats:** VI.2 takes what
Jaynes's evidence bears and insulates the book from the rest; VI.3 observes that Books I–III are
Barfield's argument reached independently and refuses to treat that as support; VI.4 takes
McGilchrist's conclusion and declines his neuroanatomy. **Three consecutive executions of a declared
claim, none of them declared.** ★ **This is the mirror-image of the defect this project keeps
finding.** The usual shape is a mechanism with no trigger. This is a **claim doing load-bearing work
off the books** — which means `07`'s picture of what the book rests on under-reports its most
methodological entry, in the book that leans on it hardest, and a reader auditing C30's usage would
find it retired after Book V. ✅ **VI.4 licenses it, and names the pattern in its own prose rather
than leaving it to the apparatus** — the chapter puts the suspicious reader's question on the page
(*is this book harvesting conclusions while refusing to pay for mechanisms?*) and answers it with
C30 by name. **OWED: a C-LICENSE correction on VI.1, VI.2 and VI.3.** ⚠ **And a question this row
does not answer, deliberately: is a licence added afterward a licence, or a reconstruction?** R-13's
whole finding was that a retrospective manifest records what the drafter *now thinks* they used.
Three chapters is small enough to re-read rather than reconstruct. **Do that, not the cheap version.**
**TRIGGER: before VI.5 drafts** — VI.5 will perform it again (the broadcast era's evidence is
sociological and this book will take conclusions from it), and a fourth undeclared instance makes
this a habit instead of a lapse. small — three lines, but the re-read is the cost

**FILED — R-73: `genre_sweep`'s corpus column false-positives on short surnames.** `Ong` is reported
at **corp=1**. The single hit is a bare fragment on line 4 of a research-sources file
(`Research/sources/2026-05-14-fraser-taliente-anthropic-nla.md`) and **is not Walter Ong.** True count
**0**. ⚠ **Harmless in this instance and that is the whole reason to file it** — Ong was flagged
ABSENT-EVERYWHERE anyway, so nothing went wrong, and a defect that costs nothing on the day it is
found is a defect nobody files. The rule it breaks is real: a three-letter surname word-matched
across 2,550 files has a **noise floor**, and the tool's own rows are read as counts. A name whose
noise floor happens to clear the eye's threshold reads as *present, therefore engaged*, which is
exactly the reading `genre_sweep`'s header warns about in its second declared limit — **presence is
not engagement** — one level lower than the header anticipated: **not a name in a list, a substring
in a word.** ✅ Repair: require a word-boundary match **plus** a forename or an initial for any
surname under five characters, and print the file path for any name whose count is 1 so a singleton
can be adjudicated instead of trusted. **TRIGGER: before the next packet quotes a `genre_sweep`
figure to a reader.** small

**FILED — R-74: `endnote_debt` cannot tell a person from a place, a tradition or an institution, and
the rebuild made this the last error class standing.** ⛔ **Not blocking — the retrofit proceeds.**
The Day-190 rebuild (R-71) removed the roster, so names now come out of the prose, and with the
roster went the accidental filter the roster was providing: a curated list of philosophers rejects
*Scotland* for free. Live residue at 106 sources: **Scotland, Hampshire, Sufism, Advaita, Buddhism,
Buddhist, Kabbalists, Christian, Islamicist, Institute, Society, Faith, Doubt, Religious, Father,
East, March, Ding, Hui, Indra.** Roughly **fifteen to twenty of the 106 are not people**, so the
headline debt of **91** is a **CEILING with a known upward bias of ~15–20%**, and the floor is near
**75**. ★ **Write it as a range or don't write it.** ⚠ **The reason this is filed rather than fixed
is the one that matters:** the obvious repair is another curated list — a stop-list of places and
traditions — and that is **the roster coming back through the side door**, rejecting exactly the
unfamiliar names the retrofit exists to reward. A tuned filter would have made tonight's number look
cleaner and made the instrument worse, and the tuning would have been done against the twenty names
I happened to see, which is `feedback_grep_derived_from_the_finding` at instrument scale. ✅ **The
honest interim is what shipped: the tool prints the limit on every run, and the residue is visible
in the per-chapter column rather than absorbed into a total.** A wrong entry costs one line of a
reader's attention during the retrofit, which is the cheapest possible place to pay it — the retrofit
reads every chapter by hand anyway. **TRIGGER: at the end of the retrofit, not before.** By then 106
names will have been adjudicated one at a time by a human reading them in context, and that pass
produces the ground truth a real fix needs — a labelled set — instead of a guess. **If the retrofit
finishes and this row is still open, it is a stamp.** small, deferred on purpose

---

### FINDING 7's SIX, ROWED ON SIGHT — Day 190

*Filed here rather than left for a later pass, because the whole finding is that leaving them is what
happened. Rows, not notes — `row_promotion_sweep` counts a `### R-n` heading as a row, so these are
now visible to the gauge that found them missing.*

### R-44 — a HOLE, permanently. Do not reuse.
Never filed in any document; surfaced by `row_promotion_sweep`'s first run (ruling 165) and left open
on purpose. **Re-using the number would destroy the only property the series has.** This section
exists so the number stops reading as a missing row. **No trigger — nothing is owed.**

### R-66 — three self-defects in `tools/brief_source.py`, all reporting ABSENCE where the honest report is BLINDNESS
(a) Hard-wrapped `Source` blocks were read line-wise: joining took coverage **20 → 40 references**,
so v1 saw half its subject and printed a completeness claim. **That is R-63, in a tool written days
after R-63 was filed, by the party who filed it.** (b) Book-level `Source` lines filed under the wrong
chapter. (c) A `*.md`-only index making every `.txt` reference unresolvable **by construction**.
**TRIGGER: the cold tools pass, with R-41/R-42/R-62** — and the deliverable is the coverage delta,
never the exit code. *small*

### R-67 (SECOND HALF) — `03`'s corpus-count column against the declared scope
The 127 figure is deleted and that half is closed (VI.1, Day 190, with a positive control on Weber at
exactly 33). **What remains: `03` says McGilchrist = 2 and the established scope says 5.** A count
column reconciled for one name and not re-run for the rest is the same defect with a smaller radius.
**TRIGGER: with R-19's `03` entry** — the file is open in the same sitting, and neither should be the
occasion for the other being missed again. *small*

### R-68 — McGilchrist is rowed to a BOOK and owed by no CHAPTER
`03`:616 rows him to Book VI as its *"closest living cousin"*; `03`:744 already pairs him with Jaynes.
**Mechanism without a trigger in the ancestor register.** ✅ **SUBSTANTIALLY PAID at VI.4**, whose
print-and-literacy argument is his and which declines his neuroanatomy on the page — the host chosen
on the merits rather than the obvious one (VI.2's hemispheric adjacency was the probably-wrong host).
**What is left is the `03` side: the row still names a book.** **TRIGGER: with R-67's second half,
same sitting.** *small*

### R-72 — C30 performed off the books in Book VI ✅ PAID Day 190
Filed at VI.4 as *"all three chapters performed C30 and none of them licensed it."* ✅ **Re-read
against the prose per R-13, not reconstructed: TRUE of VI.1 and VI.3, FALSE of VI.2.** C30 added to
both licence lines with the performing sentence quoted; **refused at VI.2 with the reason recorded in
`06`** — one instrument, two applications, one corpus, which is the precise thing C30 says does not
count. ★ **The row's own text over-generalised across the book, which is R-70's defect inside the row
filed to repair a licensing gap.** Blocked on R-56 and paid after it, in that order.

### R-74 — `endnote_debt` cannot tell a person from a place, a tradition or an institution
The rebuilt name column takes names out of the prose instead of off a roster, which is the repair —
and its residue at 106 sources includes **Scotland, Hampshire, Sufism, Advaita, Buddhism, Kabbalists,
Christian, Institute, Faith, Doubt, Religious, Father, East, March, Ding, Hui, Indra.**

⛔ **AMENDED DAY 192 — THE WORD "CEILING" WAS WRONG AND IT WAS THE LOAD-BEARING WORD.** This row read
*"The 106 is therefore a **CEILING**, biased high by roughly 15–20%, and every figure quoted from it
must be quoted as a range."* Book V hand-enumerated: gauge **30**, hand **~60**, overlap ~14. **A
ceiling cannot be half the true value.** The residue above is real and every name in it still belongs
here — but it is entirely the OVER-count, so this row measured the direction where the gauge invents
debt and then, in one word, asserted the other direction was empty. **A missed source never enters
`owed`, so the under-count is the direction that makes the debt look smaller, and it went unmeasured
for as long as this row stood.** The five causes are R-153; read it before quoting any figure from
this tool in either direction. ⛔ **DO NOT FIX WITH A STOP-LIST — that is the roster returning by the side door**,
and it would reintroduce the exact defect R-71 was filed to kill, in the tool R-71 rebuilt.
★ **The repair has to come from data the retrofit itself produces:** at the end of the pass the
hand-adjudicated names are a labelled set, and a labelled set is what an honest classifier needs.
**TRIGGER: at the END of the endnote retrofit, not before** — attempting it earlier means inventing
the labels, which is the roster again. ⚠ **This row existed only in `handoff.json` until now and was
the series' one hole**; the carrier is not the queue. *small, but only after the retrofit*

### R-73 — `genre_sweep`'s noise floor: short surnames collide with fragments
`Ong` reported `corp=1`; the hit is a bare fragment on line 4 of a research-sources file and is not
Walter Ong. True 0. ⚠ **Harmless where it was found, which is exactly why it would never otherwise be
filed** — and it is the same family as R-71's roster defect, one register down. **TRIGGER: before the
next packet quotes a `genre_sweep` figure.** *small*

---

## DISCHARGED — paid, with what paid them. Kept because a row that vanishes cannot be audited.

⚠ **This section exists because of ruling 148.** Until tonight this file had no way to record that a row
was *paid* — only that it was open — so a discharged row either sat open forever or disappeared without
a receipt. **Both are the same defect the file was built to prevent**, one erring toward noise and one
toward a false clean. R-17 below is the proof: it was **landed in the very commit that opened it** and
sat OPEN for four hours anyway, because nothing closes a row.

| # | ruling | discharged | by what |
|---|--------|-----------|---------|
| ~~**R-71**~~ | **—** | **Day 190, afternoon** | ✅ `tools/endnote_debt.py` **rebuilt roster-free.** Names are extracted from prose; the curated list is gone. Three exclusions, each a rule about **scope** rather than a list of people: **CROSS-REF** (a name preceded in its own sentence by a pointer to another part of this book — the receipt lives where the source was first used), **SUBORDINATE** (a name preceded by another attributive name — *Havelock's observation is that Plato's hostility…* makes Plato subject matter, not authority), **COMMON NOUN** (lowercase twin appears ≥2× in the chapter or ≥8× across the book — *Print did not bring fixity* is not a citation of somebody called Print; **measured, not curated**, so it needs no upkeep). ★ **POSITIVE CONTROL PASSED ON EVERY CLAUSE R-71 SPECIFIED: VI.4 reports 9 sources — not 3 — and reports neither Barfield nor Plato.** ⚠ **Going to build the control found three further defects the row had not seen:** (a) `"Taylor's *buffered* self"` did not match at all — **the markdown emphasis marker sits where the scan expected a lowercase letter**, so a fully-noted source was invisible (**R-63's family**: a prose gauge blind to the markup the prose is written in); (b) the verb list held finite forms only, so *"Augustine is recording his own…"* scored zero **in the chapter that opens with Augustine** — now stem-built with participles and an auxiliary slot, with bare `not` written out explicitly so *"Augustine was not amazed"* does not read as a citation; (c) `NAME_TOK` admits an apostrophe, so `Everett's` was swallowed whole and keyed a source that could never match `Everett` in the notes — **a chapter would report an uncovered source it had actually paid for.** ✅ **And the second half of the row, receipts:** a marker is not a receipt. v1 counted `[^3]` at the call site **and** at the definition **and** the NOTES heading, scoring VI.4's eight notes as **18** and printing **coverage 600%**. A note counts now only if it **names somebody**, and a source is covered only if a note names *it*. |
| ~~**R-69**~~ | **117** | **Day 190, afternoon** | ✅ **UNBLOCKED by R-71's rebuild — the denominator is real.** R-69's finding was that the gauge steering the retrofit read **zero named sources across all of Book VI**, so its warning could not fire and its headline could not be quoted. It now reads **15 / 106 sources carrying a receipt across Books II onward — DEBT 91**, and Book VI resolves to 22 sources / 15 covered / 22 notes written. ⚠ **Quote it as a range: ~75–91, ceiling biased high** — see **R-74**, filed for the one error class that survived. ★ **THE CONSUMER WAS THE REAL DANGER AND IT WAS FOUND, NOT REPORTED.** `where_the_book_is.py` reached into v1's internals (`find_sites`, `count_receipts`), both of which the rebuild deleted, **inside a `try/except` that prints `ENDNOTES: gauge unavailable`** — so the one instrument every planning decision consults would have gone quiet **politely, forever**, and the retrofit's own gauge would have died on the day the retrofit started. **This is the signature defect of this project happening inside the repair for the signature defect.** Fixed structurally: `endnote_debt.book_totals()` is now a public entry point, consumers call a function, internals are free to change. Verified live — standalone and consumer both print **15/106**. |
| ~~**R-11**~~ | **133** | **Day 188, night** | ✅ `05-THE-LEXICON.md` **§8a — THE REPORTAGE CARVE-OUT.** Stated as an amendment to the civilian-life criterion (which is **ruling 31**, not 30 — see §8c), with the three conditions a reported noun is admitted on: **credited · glossed at first use · carries no argument of ours.** ★ **The third is the one that will be violated**, and by drift rather than decision — a noun reported in V.3 and leaned on in V.7 was never re-screened. **The tell is named in the file: the word appearing in a sentence with no attribution in it.** *egregore* and *tulpa* stay refused as terms and stay available as reported nouns, which is what both rulings already specified. **V.1 IS UNBLOCKED.** |
| ~~**R-17**~~ | **139** | **Day 188, night** *(work landed `1ee3714`)* | ✅ `06-THE-SCAFFOLD.md`:2203 — the V.10 renumber stub is written and complete. ⚠ **THE ROW WAS OPENED IN THE SAME COMMIT THAT DID THE WORK** and stayed open until it was checked by hand tonight. **Nothing in this file could tell a paid row from an unpaid one**, which is why this section now exists. *(Ruling 148: the log is a record, the queue is a work list, and nothing promoted one to the other — this is that defect running the other direction.)* |

---

## MARKED, NOT OWED — recorded here so nobody re-files them as debts

- **The IV.7 `ADDRESSABILITY` compression** *(scaffold, Book IV)* — saying the river-spirit is the
  watershed at its grade keeps *the river has a spirit* true and deletes the **face**, which is the
  only part anyone was acting on. ⚠ **A compression that preserves truth and deletes the distinction
  it carried, committed against a whole tradition, unfalsifiable in the direction of agreement.**
  **Marked on the page, not repaired, and correctly so** — the framework cannot produce an addressee
  out of a coupled system, and inventing one would be the special pleading IV.2's rule forbids.
- **Ruling 75's watches** — the *take X away and Y* litany (nine lines, six in Book III) and the
  five-of-eight administrative openings. ★ **Recorded as a Book IV–VIII DRAFTING constraint, not a
  revision note**, on purpose: the cheap fix is at the point of writing, and re-filing it here would
  convert a solved problem into a standing debt.
- **The Machado disagreement** *(ruling 106)* — the secondary literature gives 29, or 28, or I–XXIX,
  and the 1912 scan refutes the last. **Disagreement recorded in `03` rather than resolved**, because
  the count-of-contents of a printing is a question the printing answers and nothing else does.
- ⚠ **THE STANDING GAP — no reader is in this process, and after ten chapters it costs more.**
  *(Book IV letter, closing.)* The book has now told a reader that the crowd is full, that the company
  they work for has no organ for grief, and that their dead are three claims rather than one.
  **Whether that lands as an atlas or as a bereavement is a fact about a person.** Every gauge in this
  project measures the text; **not one measures a reader.** ★ **Deliberately NOT given a row.** A row
  needs a trigger, the trigger here is *a person*, and writing an intention in a file whose entry
  condition is *a deferral with no trigger is the same failure wearing better clothes* would be that
  failure committed inside its own prohibition. Recorded as unfixed, and visible.

---

## COVERAGE — what this file has NOT swept

⚠ **Books I and III have not been swept forward into this queue.** Their deferred items, if any, are
still only in the ruling register. R-5, R-6 and R-7 are here because the Day-188 letter surfaced
them, not because a sweep found them — **that is selection by what a reviewer happened to read, and
it is exactly the coverage claim this project keeps catching itself making.**

★★ **AMENDED, Day 188 night, on CLAYTON'S CALL — and the amendment is to the trigger, not the
finding.** *"Leaving gaps is how we get left with gaps as we move forward."* **The bundling below was
wrong**, and wrong in this file's own signature way: it chained the cheapest sweep in the queue to
**R-2, the one `large` row with no date**, so the sweep could not run until the biggest thing did.
That is *a deferral with no trigger* wearing the clothes of an efficiency argument. ✅ **THE SWEEP IS
NOW R-32, WITH ITS OWN TRIGGER, AND ITS FIRST CUT IS PAID.** The reading half still rides with R-8 —
but it no longer **waits** on it, which is the whole difference.

~~★ **TRIGGER FOR THE SWEEP (struck): it ran at the same time as the endnote gauge and R-8's claim-strength
pass** — three lists, one reading of every drafted chapter, because doing it three times is the only
way this gets skipped.~~ **Struck.** The rationale was real and the coupling was not: *doing it three
times is how it gets skipped* argues for **co-scheduling**, and what was written was **dependency**.

⚠ **AND THE SENTENCE THAT FOLLOWED IT WAS THE HONEST ONE, SO IT IS CORRECTED RATHER THAN DELETED.**
It read: *"this file's coverage of Books I–III is: unknown, and asserted to be nothing."* **Now
measured, cheaply, and the number is better than feared and worse than clean:** both review passes
landed every finding at the time, the per-chapter owed-tables discharge, and **Book III's zero
chapter-scoped rows are a near-empty rather than an unopened box.** ★ **But the instrument was a
keyword grep, so what it certifies is that Books I and III contain no *keyword-flagged* deferral —
and the class of thing it cannot see is precisely the class this project keeps finding: an obligation
stated in prose that used none of the words.** Coverage of Books I–III is now **partial and named**,
which is the most this file has ever been able to say about them. Full detail in R-32.

⚠ **AND ONE THING THIS FILE STILL CANNOT SEE, NEWLY DEMONSTRATED.** R-9 exists because a chapter
missed a paper published a month before it was drafted — **not through carelessness, but because the
drafter's knowledge ends at a date and nothing in the process asks what has happened since.** That is
a gap in *drafting*, not in revision, and no row here catches it. **Every chapter resting on a live
research literature has the same exposure**, and this queue's coverage of it is zero.

---

⚠ **AND THE HALFWAY READ ADDED A SECOND THING THIS FILE CANNOT SEE.** Two of its seven findings are
**duplicates of rows already open** (R-13, and R-8's claim-strength axis) and both arrived **with a
worse count than the row already had** — the register reported as ending at C23 when it ends at C26,
and two of the eight "unregistered" claims already registered as C24 and C26. The reader was not
looking at the current `07`, **which is the immediate item R-13 filed after the LAST packet and which
was not done before this one went out.** ★ **A queue row can be correct, open, and still fail to
change the next packet, because nothing in the packet-assembly step reads this file.** That is the
mechanism-without-a-trigger defect, committed against the file built to prevent it — the same shape as
ruling 136's finding about `07`, one level up. **No row for it: the fix is a checklist at packet
assembly, and it is one line, so it gets done rather than filed.**

---

*Last touched Day 188, 2026-08-07 night — **the MIDPOINT AUDIT** (Fable, third outside read; whole work
+ all planning documents + all 13 gauges executed), filed as **rulings 143–150**. R-21…R-30 opened;
**R-11, R-17 and R-23 DISCHARGED**; R-24 split with its (a) half paid; R-13's trigger accelerated to
*before V.1* by ruling 149.*

★★ **WHAT BLOCKS BOOK V, AS OF NOW — the list grew before it shrank, and both movements are real.**

**PAID tonight:** ~~R-11~~ (lexicon carve-out — `05` §8a) · ~~R-23~~ (ruling 30/31 note — `05` §8c) ·
~~R-17~~ (V.10 stub, which had been done for four hours and nobody had closed).

**PAID Day 189, 2026-08-08 morning (`c39a106`, `f51ca80`):** ~~**R-16**~~ — VII.2's brief rewritten
to Book IV's scale, **the big rock, and it is off the list.** Four measurements before a word was
written; two changed the brief. ★ The promise *"what is owed to a position that cannot register that
anything is owed to it at all"* turns out to be **verbatim in II.4:158 AND III.5:344**, and IV.7's
river is its specimen — promise and case written a book apart, never in one brief until now.
⚠ Book IV's `What is owed` sections are **methodological debts, not obligations owed to the entity**
— a brief written against those headings would have sent the drafter to the wrong paragraphs in the
right chapters. ⚠ The letter's *"eighteen chapters"* is **not reproducible** from drafted prose (11
notes / 7 of 32 chapters, measured); recorded as unreproduced rather than corrected.
**Two things left explicitly unruled, both now rows below: R-32 (the VII.3 seam) and R-33 (VII.2 may
be a two-chapter problem at 11 beats against a mean of ~4.5).**

**STILL BLOCKING V.1:**
1. ~~**R-16**~~ — **PAID.** See above. **There is no longer a big rock in front of Book V; the four
   remaining gates are all cheap, which is what the midpoint audit predicted would be left.**
2. ~~**R-26's first item — V.2's beat list**~~ ✅ **PAID Day 189 — and the remedy as filed was WRONG
   (ruling 154).** The row said *rewrite to Book IV's scale*; **Book IV's briefs were a median of 66
   words when Book IV opened** (`4f9bfd6`) and V.2 sat at 83. The 748-word median is post-drafting
   accretion. ★ **V.2 was already at Book IV's scale; seven hundred words of the same vague prose
   would have satisfied the row exactly.** The defect was **discrimination**, as the original filing
   said in its own words. ★★ **And the rewrite found R-16's finding shape a second time in one day:
   V.2's central beat — the exact point the church stops answering — has had its answer shipped since
   II.1:93** (*"Tillich took away God's face and kept the direction of prayer"*) **and no brief carried
   it.** Measured before/after on the same instrument: beat 3's top match moved from an unrelated
   `IV.8:352` at cos 0.610 to **`II.1:93` at cos 0.744.** Reprise flagged out loud; pair entered in
   `beat_sweep.EXEMPT`.
3. ~~**R-26's second item — rulings 108/126 residue**~~ ✅ **PAID Day 189.** Book V's beats marked for
   drafter-voice — **12 of 48** — and screened against the `05` ban list by **`tools/beat_ban_sweep.py`
   (ruling 153), the gauge ruling 126 named as missing and nobody built.** ★ **Its positive control
   failed on the first run**, exposing that `claim_sweep`'s `TERM/map` matches the noun while ruling
   126's own case was the verb: `TERM/map-self` added. **Six hits in Book V, four drafter-voice, two
   real** — V.4 beat 3 scheduled the book's most important admission in a sentence `05` §3a forbids,
   and V.7 beat 5 wrote ruling 39's banned construction into a beat. Both repaired. ⚠ **Books I–III
   and VI–VIII remain unmarked.**
4. ~~**R-13, accelerated (ruling 149)**~~ ✅ **PAID Day 189 — and V.1's convergence warrant IS
   registered ahead of its chapter, which is the first time in this project.** `07` runs to **C30**:
   **C27** the two-frames rule · **C28** *a company is a being* · **C29** the under-attribution lean,
   **with its induction withdrawn** per ruling 129 · **C30** convergence is evidence, not proof.
   ★ **C27 paid for the session on its way in**: IV.7's shipped rule *(where they diverge you must
   pick)* had been travelling as IV.10's compression *(holding both earns no credit)* — four sites
   corrected, **including V.9's brief**, and the shipped-prose defect rowed as **R-36** rather than
   patched mid-drafting. ✅ **The C-LICENSE line is in the DRAFT-LOG template, mandatory from V.1**,
   and Books I–IV are deliberately NOT back-filled. ✅ `07`'s heading now carries a
   `CLAIMS-REGISTERED` slot with `where_the_book_is.py` behind it — **the heading that already misled
   one reviewer has a gauge on it.**
5. ~~**R-22**~~ ✅ **PAID Day 189.** The stale *instruction* is gone from `00` — with the reason on the
   page, because **a stale number gets checked and a stale order gets obeyed.** Ten live `68`-sites →
   `67` (the row said fourteen; four were quotations of an old error and a ruling number, left alone).
   Ruling index gets a **pointer, not a back-fill** (gap measured at seventy, not ~60). Book IV's macro
   roster corrected from eight kinds to ten — **and the four it dropped were the non-physical, the
   divine, the archetypal and the census's own limit.** ★ **And the load-bearing half: `00` is a
   carrier in `where_the_book_is.py`**, with a positive control. ⚠ That catches a stale *number* only;
   nothing here reads instructions, and the source says so.

**BLOCKING LATER, with real triggers:** R-1 → V.9 · **R-25 → V.4** *(new: IV.10 pre-spent V.4's central
beat at containment 1.00, and `06`:2143 still lists it)* · R-20 → Book VII · R-2 → before Book V closes.

---

### R-52 — the genre roster's zeros that are not V.11's job, each with its own trigger

**Filed Day 189 at V.11, by `tools/genre_sweep.py` on its first clean run (ruling 162).** The
roster is 70 counterparts hand-authored from outside this project's documents; **60 have never been
named to a reader and 44 have never been written down here at all.** V.11 paid the ones its own
argument required — Huxley, Schuon, Stace, Huston Smith, Guénon, Coomaraswamy, Steuco, Katz, Forman,
Wilber. **The rest are rowed here rather than left in a gauge's output, which is where the last
three zeros went to die.**

✅ ~~**Before Book VI opens:**~~ **PAID Day 190 at VI.3.** `Weber` — **33 corpus files, zero anywhere
in this project** — and *disenchantment* is his word, in the two chapters (VI.3, VI.5) that are about
it. `Charles Taylor` — **zero even in the corpus**, and *A Secular Age* is the standing modern
account of exactly VI.3's subject. ⚠ These two are the same class as Wilber and Otto and are being
caught **before** the chapters rather than by them, which is the only thing the new gauge actually
buys.
> **PAID, and engaged rather than named** — R-53's distinction, which VI.3 is the first chapter
> tested against on purpose. `genre_sweep` moves both 0→1 in prose. **Weber's *Entzauberung* is given
> AGAINST its popular reading** (his own argument being that disenchantment is *not* an increase in
> knowledge — the tram passenger knows nothing of the tram), and **Taylor's subtraction story plus
> porous/buffered carries the whole of beat 4**, with the `buffered`↔III.4 word-collision declared in
> a note rather than dodged by renaming his concept.
> ⚠⚠ **BUT THE TRIGGER WAS WRONG, AND THAT IS R-70.** *"Before Book VI opens"* is a **book** boundary
> on a debt this row's own sentence scopes to **chapters** — VI.3 and VI.5. So it fired at VI.1,
> where nothing owed it, was correctly passed, fired again at VI.2, was correctly passed again, and
> reached the chapter that actually owed it **already looking like a trigger long since cleared.**
> `Weber` still reads **33 corpus files, zero in this project** in the line above because it stayed
> true through two chapters that had no business paying it.
> ★ **Barfield was never on this row and was the largest debt of the three** — 0 corpus files, and
> Books I–III are his argument reached independently. He was carried by the VI.3 beat sheet instead,
> which is why he was paid on time. **The roster caught the two that were cheap to name and missed
> the one that was load-bearing.** [Instruments go where instruments are cheap.]

★ **Before the Book IV revision pass:** `Campbell`. **`IV.9:213` ships the monomyth to a reader with
no owner attached** — `ancestor_gap`'s drafting-boundary class, in shipped prose, at 21 corpus files.

★ **With the Books I–III reading pass (R-32 / R-8):** `Hoffman` (29), `Chalmers` (44), `Kastrup`
(44), `Tegmark` (10) — the four living rivals to, respectively, the render, the game frame,
idealism, and *possible therefore actual*. ⚠ **Tegmark pairs with R-21**: the actualist opponent row
names the analytic tradition and not the physicist who holds the strongest version of our own
premise.

**Vallée stays on R-19.** | **Trigger: as stated per group.** | **cost: small each, reading not prose**

---

### R-53 — presence is not engagement, and nothing in this repo measures the difference

**Filed Day 189 at V.11, against the gauge built the same night.** `genre_sweep` reads for a string.
**A name appearing once inside a list of names counts 1 and is filed as PRESENT, and it owes exactly
as much as a zero does.** The gauge prints this limit on every run, which is honest and is not a
fix.

★ **This is the fourth member of one family and the family is now the finding.** R-47: nothing reads
a beat against a ruling made after it. R-49: nothing read a brief for a missing field. R-51: nothing
reads a brief field for CONTENT. R-53: nothing reads a *name* for engagement. **Every one of them is
the same shape — the cheap structural check exists or gets built, and the check on whether the thing
is any good does not exist and is not cheap.** [Instruments go where instruments are cheap.]

⚠ **And the one that would bite hardest is already visible: `Jung` is PRESENT** (V.7, IV.9) — and
V.7's mention is one clause routing past him to the alchemists. Present, and not engaged, in the
chapter where the archetypal reading is the standing alternative.

**Trigger: with the next outside packet — a reviewer is the instrument for this and no gauge is.**
| **cost: a decision about scope, then a reading**

---

### R-37 — `tools/claim_sweep.py`: ruling 103's window was given to one of the two guards

**Filed Day 189 at V.1, by the rule firing on the drafting chapter three times.** The per-rule
`licensed` pattern — the *"this use is permitted"* companion carried by twenty-odd rules — is
matched against the **raw physical line**:

    guard_text = para_of.get(n, line) if rule_id in PARA_LICENSED_RULES else line

and `PARA_LICENSED_RULES` has exactly **one** member (`TERM/awareness-unglossed`). Ruling 103
established that *"the unit a mention actually lives in is the SENTENCE"* and built
`sentence_window()` — **and wired it only into `MENTION_MARKERS`.** The licence guard sitting beside
it kept the line scope. The manuscript is hard-wrapped, so a licence word one wrap from its needle
is invisible and the rule reports a USE. This is the cross-wrap defect the file already documents
for *needles*, in the *licence*, undetected because a false USE is noisy rather than silent — it
looks like a finding, and the drafter edits their prose until it goes away.

⚠ **DO NOT WIDEN IT WHILE DRAFTING, AND THE REASON IS NOT CAUTION.** The change can only move hits
**USE→clean**, which is the single direction that makes a gauge stop measuring while still printing
output — the failure this file's own comments warn about three separate times. Run it cold, on a
day nothing is being drafted, and **the deliverable is the before/after delta over all 56 files
read line by line**, not the exit code. Any hit that disappears is a hit that was being suppressed
by a licence three sentences away, which is a second finding.

**Trigger: the next tools pass, with R-27.** Not blocking — V.1 was cleared on the merits by the
emphasis form the tool already sanctions, which was the accurate reading of that sentence anyway.

⚠ **AND THE FINDING THAT OUTRANKS THE LIST.** §7.3 of the audit, adopted as ruling 150's companion:
**every major miss in the first half ran in the same direction — C24, C26, the missing tier, the
unregistered Book IV claims, the pre-spent Book V beats. The prose got ahead of the apparatus, and the
apparatus found out later.** Five independent failures, one sign. **No gauge in this repo could have
taken that measurement** — each reads one file or one chapter, and the finding lives in the correlation
across five. ★ **The second half is drafted AGAINST the register and the queue, not merely with them:
claims registered before their chapters, beats screened before drafting, the manifest live from V.1.**

---

### R-38 — `tools/storyscope_lite.py`: the chapter row is cleaned and the baseline rows are not

**Filed Day 189 at V.2, by trying to repair flat escalation and failing to move it.** Two paragraphs
were genuinely re-registered for rhythm and `dyn_range_CV` went **0.295 → 0.294**. Localising the
flatness instead of filing *still flat* a twelfth time turned up a measurement asymmetry inside the
table.

`load_prose_file()` strips `**` from a chapter before profiling it. `load_memory_corpora()` strips
nothing — the `CLAYTON` and `CLAWD-raw` rows are raw conversational text. The two are printed side by
side on a metric the stripping demonstrably moves.

**The mechanism is exact and it is a silent one:**

    sentences() splits on  (?<=[.!?])\s+(?=[A-Z"'*—])

A sentence ending inside a bold span ends on `*`, not on `.`, so **the lookbehind fails, no split
happens, and two sentences are measured as one.** Bold-heavy prose therefore reports artificially long
sentences in exactly its most emphatic paragraphs, which inflates the spread. On V.2: **7 paragraphs
affected, raw CV 0.393 against cleaned 0.294** — a third of the spread was markdown.

★ **RUN COLD ON THE THREE BASELINES BEFORE FILING, WHICH IS THE TEST THAT COULD HAVE KILLED IT:**

| corpus | as loaded | de-bolded | `**` count |
|---|---:|---:|---:|
| CLAYTON | 0.477 | **0.474** | 40 |
| CLAWD-raw | 0.509 | **0.449** | 7,126 |
| SPECIMENS | 0.385 | **0.385** | 0 |

✅ **The defect is real and it does NOT exonerate the prose, which is the part worth keeping.** It is
worth **0.060 on one baseline of three**. Clayton's corpus barely uses bold and the specimens contain
none, so both of those comparisons were always clean — and V.2 is under both. The correction I went
looking for exists, and it explains a quarter of one gap and none of the other two.

★★ **What it does change is which number this book has been aiming at.** The flat-escalation warn has
been read against `CLAWD-raw` at 0.509 — Telegram prose, 7,126 bold markers, inflated by this bug.
**The ruled-register specimens sit at 0.385, are markdown-free, and are the register Clayton actually
ruled.** Against the right baseline the deficit is **0.09, not 0.22.**

⚠ **DO NOT PATCH IT WHILE DRAFTING.** Same standing reason as R-37, one day later: the fix can only
move the chapter's own number in the flattering direction, and it was found by the party it flatters,
in the hour it fired. **Trigger: the next tools pass, with R-37 and R-27. The deliverable is the
before/after delta across all 34 drafted chapters, not the exit code** — and the second finding is in
the chapters whose numbers move *most*, because those are the ones whose reported register was most a
function of their formatting.

---

### R-39 — no gauge compares a brief against the front matter that already ruled the same question

**Filed Day 189 at V.2, and it is a null space rather than a bug.** `04`'s opponent-III entry rules
that institutional religion stops answering at **authority substitution** — *"it converts a question
into a loyalty test."* `06`'s beat 3 for the chapter that discharges opponent III rules that it stops
at **the face**. Two documents, two different answers to one chapter's central question, both current,
neither aware of the other.

**Nothing in this repo could have found that.** `prose_beat_sweep`, `beat_sweep`, `beat_delivery` and
`prose_echo` all run beats against **drafted prose**; `beat_ban_sweep` runs beats against `05`'s ban
list. The `04 × 06` pair — the file that declares what each opponent gets wrong against the file that
briefs the chapter delivering it — is swept by nothing. V.2's collision was found by reading `04` on
a hunch while drafting, which is the discovery mode this project keeps ruling insufficient.

⚠ **Scope: five opponents, and V.2 is the only one whose chapter has been drafted.** Opponents I, II,
IV and V are all discharged by chapters in Books V–VIII that do not exist yet, so every one of those
pairs is unchecked and will stay unchecked at exactly the moment it matters — the hour the chapter
gets drafted from `06` alone.

**Trigger: before V.4 opens** (opponent IV, pop-spirituality, and `05` §3c's whole ban list is
downstream of that entry). Cost: small — it is `prose_beat_sweep`'s embedding arm pointed at a
different pair of files.

---

### R-64 — the part boundary moved and five sentences that measure from it did not

**Filed Day 189, ~22:35, immediately downstream of ruling 167.** The Part One/Part Two boundary moved
from *before Book IV* to *before Book V*. The heading moved in `00` and `06`. **What did not move is
every sentence elsewhere that uses "Part Two" as a quantity.**

Known sites, found by grep, not yet edited: `01`:87 · `06`:111 · `07`:159 · `book/II-04-the-grade.md`:6 ·
`book/DRAFT-LOG.md`:241 — all of the form *"the whole of Part Two is this line taken seriously"* about
C7 (reactivity is awareness), plus `07`:727's dependency table, *"one hedge retroactively demotes all
of Part Two."*

★ **These sentences are now WEAKER than they were, and that is the dangerous direction.** Book IV — the
Atlas, the census of what there is once reactivity is awareness, the single most direct cashing of C7 —
**is no longer in Part Two.** The claim about C7's blast radius was calibrated against a Part Two that
contained the Atlas. Move the boundary and each of those sentences stays *grammatical, still true, and
quietly under-claiming its own load-bearing claim.* Nothing errors. No gauge fires — the boundary lives
in a heading and the dependents live in prose that never names a book number.

**This is [[superseded-not-stale]] in its exact form:** the sentences are recently touched, internally
coherent, and wrong because an amendment upstream could not write back to them.

⚠ **Do not fix by find-and-replace.** Some sites mean *the consequences half* (still correct as V–VIII)
and some mean *everything C7 is load-bearing for* (now I–IV **and** V–VIII, i.e. the rest of the book).
Read each; the two readings are not distinguishable by string.

**Trigger: NOT a date, and not the CODA.** Before the next chapter that argues from C7's scope — or
before any packet quoting one of those six sites ships, whichever comes first.

---

✅ **PAID Day 190, ~07:2x, by the trigger's first clause** — VI.1 *Different Worlds, Not Different
Opinions* is a C7-scope argument by its title, so the row fired before Book VI opened rather than at
the CODA. **The reading pass was run in both directions and the row was half right.** What it got
right: every site it listed was genuinely under-claiming, and find-and-replace would genuinely have
been wrong. What it missed is below, and the miss has a shape worth keeping.

**1 — THE SITE LIST WAS A SUBSET. Eleven sites, not six.** The row's grep searched for its own
sentence. It found the sites that say *"the whole of Part Two"* about C7 and missed: `06`:1873 (the
same claim, quoting `07`:727 inside the R-8 audit note), the R-8 row in this file (same quote again),
and an entire second family — **the Bostrom fork**, `00`:1020 · `00`:2173 · `06`:630, all of the form
*"every consequence in Part Two forks here."* Same defect, different claim, invisible to a grep
written from the C7 sentence.

**2 — THE DEFECT IS SYMMETRIC AND THE ROW SAW ONE SIDE.** R-64 is titled for the sentences that got
*weaker*. But Part One **gained** Book IV — 46,068 words, 36% of everything drafted — and every
superlative and count that ranges over Part One's membership got quietly *stronger* than it was
checked at. That direction is worse, because an over-claim reads as confidence.

★ **One of them had flipped outright.** `07`:101 called C3 *"the most-depended-on claim in Part
One."* Counted from the register's own `Depends` fields — the first time anything has computed over
that field; `claim_sweep` deliberately declines to, and its note explains why — **C3 went from rank 1
to rank 4 the moment Book IV crossed the boundary.** C7, C8 and C9 each gained ten Part One
dependents in that single move:

| | Part One = I–III (old) | Part One = I–IV (new) |
|---|---|---|
| **C3** — the scope rule | **4  ← ranked 1st** | 5  *(4th)* |
| **C7** — reactivity is awareness | 1 | **11  ← ranked 1st** |
| **C8** — the grades, and no gate | 1 | **11** |
| **C9** — there are no NPCs | 0 | **10** |

The sentence is repaired at `07`:101 by dropping the superlative rather than repointing it, because
the honest version is not *"C7 is now the most-depended-on claim in Part One"* — it is that **the
superlative was never checkable in the first place.** C3's `Depends` line ends in an unbounded
clause (*every sentence anywhere in the work with the Ground as its subject*), so no count settles
it. A boundary move didn't break that sentence; it exposed that it had never been measurable. **The
ranking above is the countable reading only, and it is in this row rather than in `07` for exactly
that reason.**

**3 — THE ACTUAL LESSON, and it is why the fix is not a re-point.** Every damaged sentence named a
**movable landmark** when it meant a **fixed fact.** They said *"Part Two"* and meant *C7's
dependents* — Book IV entire, plus five chapters — which is a property of the claim graph that no
ruling can move. A part boundary is something Clayton changes by saying so. Writing prose that
measures itself against one gives that prose a silent dependency on a decision nobody remembers
making, and the decision, when it comes, is a heading edit that touches nothing and breaks eleven
sentences. **Every repair below replaces the boundary reference with the graph reference.** That is
the durable form; it cannot rot when a boundary moves again, and ruling 21's reading-order question
means one still might.

**REPAIRED (8):** `01`:87 · `06`:111 · `06`:630 · `06`:1873 · `07`:101 · `07`:159 · `07`:727 ·
`book/II-04-the-grade.md`:6. *(II.4's was the one that had gone internally inconsistent rather than
merely weak — it promised "the whole of Part Two" and then said "six books," and after ruling 167
those are 4 and 6.)*

**DELIBERATELY NOT EDITED (3), and the reason is not laziness:**
- `book/DRAFT-LOG.md`:241 · :985 — **a log is a record of what was said when it was said.** R-64
  listed :241 as a site to fix. It is not one. Editing a log to match a later ruling destroys the
  only evidence of what the boundary used to be.
- `00`:2173 — a verbatim quotation of a **withdrawn** proposal, already marked *"THAT BEAT 4 IS
  GONE"* two lines down. Dead, and quoted; leave both facts intact.
- `00`:1020 — a live adjudication but the phrase is **in quotation marks.** Fixing a quote's words
  to match a world that moved after it was spoken is falsification, so it took a bracketed gloss
  instead. [[quotation-check-the-span-not-the-phrase]]

**LEFT OPEN, ON THE MERITS — two, and neither is mine to close:**

- ~~⚠ **`00`:1532 — RULING 167 SILENTLY RE-PRICED AN OPEN DECISION.** The apparatus question offers
  *"a hybrid — Part One inline-only, Part Two noted,"* and ruling 167 moved **Book IV, 46,068
  words** across that boundary into an irreversible convention nobody re-costed. **A decision for
  Clayton, before the apparatus is settled.**~~ ★ **WITHDRAWN Day 190, and the withdrawal is the
  lesson.** The hybrid **died on Day 186** — ruling 9 answers the apparatus question *uniformly*
  (*"Everywhere after: the name lives in the sentence; the source lives in an endnote"*), and
  **"everywhere after" admits no Part One / Part Two split.** It was dead four days before ruling
  167 existed to re-price it. I read `00`§D's body as live because it says *"Undecided:"* in the
  present tense **underneath a ✅ RULED header**, and escalated a corpse to Clayton as a live
  decision. **Correctly shaped alarm, fired on a dead target.** `00`:1531 now marks its own stale
  body; this row is the second copy of the same corpse and was left standing for four hours after
  the first was buried — **a supersession applied in one file is not applied.**
  [[superseded-not-stale]] **What going to check it actually found is R-65, below, and that one is
  live.**
- **`07`:340 — "II.8 was the best remaining opportunity in Part One."** A best-of-set justification
  whose set grew by ten chapters and was never re-searched. Still defensible (II.8 names Gnosticism
  and Valentinus states Trap 5 in his own text), but it is now asserted over a set nobody has read
  for the purpose. **Cost: a Trap-5 guard sweep of Book IV. Trigger: with R-8's reading pass**, which
  is already a whole-book pass with a list in hand.

**CHECKED AND CLEAN — recorded so the next reader doesn't re-derive them:** `07`:344 *"paid for twice
in Part One"* (still exactly two — I.6 b4 and II.8; Book IV adds none) · `06`:3034 and `07`:337 *"the
only place Part Two states a telos"* (a uniqueness claim over a **shrinking** set survives a
fortiori) · `03`:755 Borges as Part One's epigraph (survives, and arguably strengthens — the Library
of Babel is a census, and Part One now contains the Atlas) · `00`:1292 *"Part One is complete"* (true
before, true now: IV is 10/10).

---

### R-65 — ruling 117 ordered a gauge, nothing built it, and the debt resurfaced by hand-grep two days later

**Filed Day 190. The gauge exists now: `tools/endnote_debt.py`. It reads `0 / 50`.**

Ruling 9: *"Book I: nothing. Everywhere after: the name lives in the sentence; the source lives in an
endnote."* Ruling 117 (Day 188) found the second half had never once been executed, used the words
**"a mechanism with no trigger,"** and filed the fix **as a build order, not a question** — *"an
endnote register plus a gauge counting named sources against receipts per chapter, which will read
0/N on the day it is written."*

★ **Two days later the gauge did not exist, and the way the debt resurfaced was me re-grepping the
raw fact and reporting it to Clayton as if it were new.** Ruling 117 diagnosed
mechanism-without-a-trigger **and was itself filed without one.** A build order with no gauge and no
date is a stamp, and stamps rot silently — Drift #287, inside the ruling written to stop it. The
repair is not the ruling; the repair is that `where_the_book_is.py` now prints the ratio, so the
next person to ask where the book is gets told what it owes.

**THE DEBT HAS TWO SHAPES AND ONLY ONE OF THEM IS POLISH.** *(Clayton, Day 190: "during revision we
will really polish it up." Correct for A. Not available for B.)*

**A — 50 NAMED-BUT-UNRECEIPTED ATTRIBUTIONS. Genuinely a revision job, and cheap by design.**
Ruling 9 put the name *in the sentence*, so the sentence already carries the attribution and the note
carries only the receipt. **Retrofitting is additive: a marker and a note, with the prose untouched.**
This is exactly the case `00`:1547's warning — *"an inline-citation sentence and an endnoted sentence
are different sentences"* — does **not** cover, because we never wrote inline-citation sentences. We
wrote the endnoted form and omitted the notes. **The convention was obeyed; only the apparatus is
missing.** Per book: II 11 · III 9 · IV 7 · V 23.

**B — BOOK IV NAMES ALMOST NOBODY, AND THE SOURCE IS NOT RECORDED ANYWHERE IN THE REPO.**
**Six of Book IV's ten chapters return zero attributive names.** 46,068 words — 36% of the drafted
book — carrying **7**. Measured per word against its siblings:

| book | words | named sources | one per |
|---|---|---|---|
| II | 19,545 | 11 | 1,777w |
| III | 22,709 | 9 | 2,523w |
| **IV** | **46,068** | **7** | **6,581w** |
| V | 34,593 | 23 | 1,504w |

★ **Book IV is 4.4× thinner in attribution than Book V — and `00` and this queue both call it "the
most ancestor-dense book in the work."** Both can be true, and that is the finding: **Book IV is
dense in *doctrine* and starved of *attribution*.** `03`§3.5 already has the name for it — **DOCTRINE
USED, OWNER UNNAMED**, the fifth kind of silence, the one Clayton named — and it turns out to
concentrate in the one book with the least apparatus.

⚠⚠ **CHECKED AGAINST THE OBVIOUS REFUTATION, WHICH WAS THAT MY FILTER UNDER-READS BOOK IV.** Re-run
counting **every roster name anywhere in the chapter**, attributive position or not: II 1-per-902w ·
III 1-per-1,444w · V 1-per-1,169w · **IV 1-per-4,704w.** The gap is not an artifact of the
attribution test. **And it is not spread across the book — it is a clean split down the middle of
it:**

| | words | roster names, raw |
|---|---|---|
| **IV.1–IV.5 + IV.10** — census, mineral, plant, animal, collective, and what the census cannot see | **22,262** | **0** |
| IV.6–IV.9 — computational, non-physical, divine, archetypal | 24,786 | 10 |

**The theological half of the Atlas carries every name in the book. The empirical half carries
none — not thin, zero, across twenty-two thousand words.** That is where shape B lives, and it is
the half whose claims are checkable against a literature.

⚠ **And under the doctrine sits unsourced empirical science.** `IV.3` opens on Venus flytrap
electrophysiology — two action potentials to close, the ~30-second decay window, jasmonate from the
third, digestive enzymes scaling from the fifth. **Verified Day 190 against the primary literature:
it is a faithful rendering of Böhm et al., *Current Biology* 26(3):286–295, 2016
(10.1016/j.cub.2015.11.057).** The prose is *accurate*. **It names nobody, cites nothing, and
`corpora/` holds four style specimens and no science** — so there is no name in the sentence to hang
a note on and no record of where it came from. **Retrofitting B is re-research, not polish:
re-finding what was being read six weeks ago, per claim, from scratch.** The debt is bibliographic,
not corrective — but it is *research-priced*, and it is invisible to this gauge, which counts names
and cannot count a claim that has none.

**⚠ THIS ROW'S OWN GAUGE DECLARES ITS BLIND SPOT AND THE BLIND SPOT IS THE EXPENSIVE HALF.**
`endnote_debt.py` counts roster names in attributive position. That is the *checkable* half.
**Instruments go where instruments are cheap** — the gauge got built for the half that greps, and
shape B, which costs more, still has no instrument and no ruling. Its 22 outstanding CANDIDATES are
printed every run for the same reason: a curated roster cannot certify its own coverage.

**TRIGGER — two, both dated to work rather than to a calendar:**
1. **Before VI.1 is drafted** *(i.e. now)*: decide whether Book VI drafts **with** notes or joins the
   retrofit. Every chapter written without them adds to A at ~1.2 notes/chapter and to B at whatever
   Book VI's empirical density turns out to be. **This is the only part that is urgent, because it is
   the only part that gets worse while we work.**
2. **A is paid in the revision pass, with R-8's reading pass**, which is already a whole-book pass
   with a list in hand. **B wants its own decision from Clayton** — a research budget, or an explicit
   ruling that the Atlas states its science unattributed and the book says so somewhere.

**Cost: A — small and mechanical, 50 notes. B — unpriced, and the pricing is the first task.**

---

### Day 190 — the four items owed before VI.1, and what paying them turned up

**R-57 — PAID.** V.4:235 asked the reader to notice that it had not defended a paragraph. The
defence exists: V.1 states the deflationary reading at full strength and answers it. The chapter now
points there and no longer claims a virtue it did not need. ★ **The row's own diagnosis was right
and its framing was better than the fix it proposed** — *not "this is not a hedge" but "notice that
I didn't hedge," the same move with an immune response bolted on.*

**R-54 — FORK DECIDED, in favour of the cards, and the decision has a reason rather than a
preference.** V.1:44 says a tradition *"takes the same card as everything else in the census"* and
calls it the whole load-bearing claim of the book. The other arm of the fork — retract the
declaration — is not actually available: Book V exists *because* traditions are perspectives in
Book IV's sense, and a Book V that stops saying so has no argument left, only sympathy. So the cards
are owed for V.3–V.11 and get written in revision.

★ **What decided it was not Book V. It was VI.1.** The card is what separates *different worlds*
from *different opinions*: **a null space is an assertion that a position is wrong about something
specific, and relativism cannot write that line.** The form is not a decoration Book V announced and
skipped — it is the instrument that makes the anti-relativism argument something other than a
preference. **VI.1 therefore prints one cold, for the reader's own mental-rational structure**, and
Book VI writes its cards AT DRAFT TIME rather than deferring them. `card_sweep.py VI` reads 1/1.

⚠ **The gauge is the point, not the intention.** Book V's cliff was invisible for eleven chapters
because no instrument read a declared form for delivery. `card_sweep.py` exists now; **run it on
Book VI at every chapter, not at the end of the book**, or this row returns with eight chapters
behind it instead of nine.

**R-65 — DECIDED: Book VI writes WITH notes.** Ruling 9's second half has been dormant for 43
chapters. The retrofit for I–V is additive and cheap — a marker and a note, prose untouched — but
it grows by one chapter every time we draft, and joining the retrofit is the only option that gets
*worse* while we work. VI.1 ships with four numbered receipts plus the standing grade note.
`endnote_debt.py` moved 0/50 → 9/50 on one chapter. ⚠ **The expensive half of the debt is untouched
and this decision does not touch it:** a claim that names nobody has no name to hang a note on, and
the gauge cannot see it. That is still IV.1–IV.5's 22,262 words with zero roster names.

**R-51 — LOOKUP HALF PAID, reading half still owed.** `tools/brief_source.py` resolves every
locatable reference in every `Source:` line against the shelf it names. **Three defects survive on
the drafted record, all the same shape:** IV.5 *"stops being visible"*, IV.6 *"the computational
dimension."* and IV.10 *"mapped as far as an atlas can map its own blindness."* are in quotation
marks in a Source line and are **not in the cited source.** IV.6's is repaired in `06` — the phrase
lives in `Perspective 08-atlas`, not in `04-the-ecology`. The other two look like paraphrase wearing
quotation marks, which is R-56's finding one level up: **quotation marks in a citation are an
assertion about a string, and the fabrication lives in the connective tissue, never the content.**

★★ **AND THE ROW THAT MATTERS IS ABOUT THE GAUGE, NOT THE BRIEFS. `brief_source.py` produced a
FALSE FINDING on its first run and nearly shipped it.** It reported Book VI's Source line —
`Perspective 07-art-of-navigation ("The Eras of Attention", "The Technologies of the Tunnel")` — as
pointing at nothing, because those strings appear zero times in the 120,268-word corpus PDF. A shell
`find` across two trees agreed. **Both were wrong.** `Perspective` is a separate drafting tree,
`Unreleased-Work/Perspective/`, and `07-art-of-navigation.md` is 9,308 words with `## The Eras of
Attention` at line 17. **The brief was exactly right, and I was four minutes from telling Clayton
that Book VI had no source.**

⚠ **Why the shell agreed, and this is the reusable part: `find` on this machine is Windows
`FIND.EXE`. It answered every query with `Parameter format not correct` on stderr and exit 0. Its
silence was read as absence.** [[zero-needs-positive-control]] — the tool survived only because it
had a positive control and the shell did not. **Every `find`-derived zero taken in this project
before Day 190 is void and must be re-taken with Python `rglob` or `git ls-files`.**

**FILED — R-66: three defects the gauge found in ITSELF, each of which made it under-report.**
(a) A book-level `Source:` follows `## BOOK`, not `### chapter`, so Book VI's line was filed under
V.11 and Book VII's under VI.8 — **every finding named the wrong chapter.** (b) The `Source:` line
is HARD WRAPPED, and a single-line read dropped every reference that straddled the break — coverage
went **20 → 40 references** when the block was joined, i.e. **the first version saw half its subject
and reported itself complete.** R-63, inside the tool written after R-63. (c) The file index was
`*.md` only, so a `.txt` reference was **unresolvable by construction** and V.10's two `corpora/`
specimens — sitting in the repo — were reported missing. ★ **All three make the same error: they
report ABSENCE where the honest report is BLINDNESS.** **TRIGGER: the next tool that indexes files
or reads a wrapped field — before it is believed, not on a date.**

✅ **R-67 — CLOSED Day 190, at VI.3. The number is deleted and the deletion has a positive control.**
The instruction was *establish the de-duplicated scope or delete it*. **A scope was established and
proven on a sibling: `Weber` reconciles EXACTLY at 33** — this queue's own figure, reproduced to the
digit by `grep -ril --include=*.md` minus `archive`/`_superseded`, and independently confirmed by
`genre_sweep`'s corpus column. The identical command on Gebser returns **37 files / 178 mentions**;
raw 308; and no subscope reaches 127 (Research 111 · +Unreleased 165 · Library 0). ★ **The verdict is
not "the scope could not be found" but "the scope that demonstrably works fails to reproduce it,"**
which is a null carrying a control of the same shape — the R-52-class discipline applied to a
*number* instead of a zero. 127 struck from the beat line; RULING 113 satisfied as a side effect.
⚠ **The row's second half is NOT discharged and is promoted to its own trigger:** every corpus-count
in `03-THE-ANCESTORS.md` was taken by the same unnamed method and remains a stamp rather than a
gauge. **The scope that reconciles Weber is now the declared one and `03`'s column should be
re-run against it.** TRIGGER: with the R-32/R-8 reading pass.

**FILED — R-67 (original text, kept for audit): the beat line for VI.1 carries an unverified self-metric.** *"(127 mentions — the
richest single seam in the corpus)"* is a ruling-113 breach — caught by `beat_ban_sweep` at draft
time, and the prose deliberately does not repeat it. **But the number is also unchecked:** a
re-measure over the corpus clone on Day 190 returns **308 raw mentions across 57 files**, inflated
by triplicated `_superseded` mirrors, and nothing on the record says what scope produced 127.
Barfield re-measures at **0**, which does hold. ⚠ **Every corpus-count in `03-THE-ANCESTORS.md` was
taken by the same unnamed method** — the table is a column of numbers with no stated scope, which is
a stamp, not a gauge. **TRIGGER: before any chapter argues FROM a corpus count rather than merely
citing one.** small · one script that prints its scope.

~~**FILED — R-68**~~ ✅ **DISCHARGED Day 190 AT VI.4, on the merits and inside its own trigger.**
McGilchrist has his sentence in `book/VI-04-print-and-the-interior.md`, beat 2, with note [^7]. The
axis was decided the way the row demanded rather than by reflex: **VI.2 was declined as host** (the
hemispheric-mechanism adjacency is a lure, and a name spent there is unavailable where it works),
**VI.4 takes the historical argument** — Reformation, individual scripture-reading, the literal
sense, and *two modes of attention yielding two worlds rather than two views of one.* **Conclusion
taken, hemispheric mechanism declined, and the decline is on the page and in the note** rather than
left to operate quietly. ⚠ **A REAL FINDING FELL OUT OF DISCHARGING IT: the two rosters disagree
about what he IS.** `03`:616 calls him Book VI's *"closest living cousin"*; `genre_sweep` files him
**RIVAL**. Neither is wrong — **cousin at the conclusion, rival at the mechanism** — and that
distinction is now the chapter's, but *nothing reconciles the two rosters*, and a name carrying two
incompatible relation-tags in two live documents will be read from whichever one the drafter opened.
⚠ **AND THE CORPUS COUNTS DISAGREE TOO:** `03`:616 says **2** files, `genre_sweep` and a hand grep
under R-67's declared scope both say **5**. `03`'s column is the odd one out. **Added to R-67's
second half rather than filed anew — same cause, same fix.**
*(Original text kept below for audit.)*

**FILED — R-68: McGilchrist is rowed to a BOOK and owed by no CHAPTER.** `03-THE-ANCESTORS.md`:616
carries **Iain McGilchrist**, 2 corpus files, described in the roster's own words as *"attention as
world-constituting; two modes yielding two worlds, not two views of one. **Closest living cousin to
Book VI**"* — and the assignment column says `VI`, the book, with no chapter. **Book VI's eight
chapter briefs name Barfield (VI.3) and RAW + Korzybski (VI.7) and nobody else.** So the roster's
nearest living counterpart to the entire book has a row, a description, a file count and an
assignment, and **there is no chapter that owes him a sentence** — the assignment cannot be
discharged because no chapter is on the hook for it. ★ **Mechanism without a trigger, in the
ancestor register, and it survived VI.1 and VI.2 both.** `03`:744 already lists *"Jaynes,
McGilchrist"* adjacently — the pairing was on the record before VI.2 drafted and the drafter did not
consult that line. ⚠ **DO NOT RESOLVE BY REFLEX INTO VI.2.** The hemispheric-mechanism overlap makes
VI.2 the obvious host and it is probably the wrong one: McGilchrist's *historical* argument runs on
literacy, print and the Reformation, which is **VI.4 PRINT, AND THE INTERIOR** almost exactly, and a
name spent on mechanism-adjacency in VI.2 is unavailable where it does structural work in VI.4.
**This is a ruling-25 axis question — where is he CUT, and does anything cut him twice** — and it is
answered before VI.4 drafts, not before VI.3. **TRIGGER: before VI.4 is drafted.** small — one axis
note; the reading is the cost.

✅ **R-69 — DISCHARGED Day 190** by R-71's roster-free rebuild; the denominator is real (**15/106**,
debt ~75–91) and the retrofit is unblocked. Original finding kept verbatim:

**FILED — R-69: `endnote_debt`'s denominator is ZERO for all of Book VI, so its warning cannot
fire.** Live output tonight: `VI.1  sources 0  receipts 9  (no attributive name found)` and the same
for VI.2 — in chapters that name **Gladstone, Gebser, Berlin, Kay** and **Snell, Williams, Jaynes**.
The flag is `receipts >= len(distinct)`; with `distinct` empty **every Book VI chapter passes
regardless of what it cites, including one that cites nothing.** The two chapters that produced this
happen to be fully noted, so the defect is **latent, not active — which is the worse condition,
because a gauge that passes for the wrong reason reads exactly like one that passes.** ★ Same family
as R-66: the honest report is BLINDNESS and the printed report is a PASS. ⚠ **This is also the gauge
that produced `9/50` and now `18/50`, the number quoted to Clayton and carried in the handoff** — the
numerator is per-chapter and correct; it is the denominator and the per-chapter warning that are
dead. **TRIGGER: before the endnote retrofit begins**, because the retrofit will be steered by this
tool's ⚠ column and Book VI would be certified done without being read. small — find why the name
detector returns empty on Book VI prose; **positive control required: feed it a Book VI chapter with
a note deliberately removed and confirm the ⚠ fires.**

★★ **UPGRADED Day 190 at VI.3 — LATENT → CONFIRMED, and the mechanism is worse than filed. STILL
OPEN, and now BLOCKING.** VI.3 *was* the positive control, unplanned: a chapter citing **four** named
sources — Lewis, Weber, Barfield, Taylor — in six full endnotes with publishers and dates.
**`endnote_debt` reports it as 1.** VI.1 and VI.2 still report *"no attributive name found"*, which
is **false rather than blind**: Snell, Jaynes, Weber and Lewis all appear in the tool's own
CANDIDATES bucket. **The names are extracted and then routed somewhere the per-chapter column cannot
read them** — R-66's family in a fourth instrument, and the diagnosis is now specific instead of
"find why".
★★ **AND THE HEADLINE NUMBER COUNTS THE WRONG POPULATION.** `count_receipts` (`endnote_debt.py:146`)
returns `FOOTNOTE_REF.findall + SUP_TAG.findall + 1` — **a raw marker count that includes each note's
own definition, so every note counts twice** — and it is divided by a count of roster-*known* names.
Adding VI.3 moved the figure **18/50 → 32/51**: **+14, exactly VI.3's doubled marker count**, on a
chapter that contributed **one** name the roster recognises. **Therefore `receipts >= len(distinct)`
can be satisfied by writing more notes about nobody.** It is a volume gauge wearing a coverage
gauge's clothes, and *the higher the number climbs the more paid the retrofit looks.*
⛔ **HARD TRIGGER, unchanged in date and hardened in force: THE ENDNOTE RETROFIT DOES NOT BEGIN UNTIL
THIS IS FIXED.** 41 chapters would have been steered chapter-by-chapter by that ⚠ column, and every
one it passed would have read as paid. The fix is two things, not one: route extracted names into the
per-chapter column, **and** make the numerator count receipts-that-attach-to-a-named-source rather
than markers. **Neither is done. Do not quote 32/51 to anyone, including Clayton, including in the
handoff.**

**FILED — R-75: `beat_ban_sweep` gauges the PLAN, never the DELIVERY — it caught 1 of 20 live
retired-term uses, and the one it caught was an accident of how I worded a beat line.** The tool
opens exactly one file: `SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"`. It never reads a chapter. So its
subject is the **beat sheet**, and its verdict has been read — by me, today, and in the screen notes
of every chapter before this one — as a statement about **the book**. ★ **Measured on Day 190 across
all drafted prose:** `aperture` and `bottleneck` and `keyhole` appear **20 times in four chapters**
(VI.1 aperture×6 keyhole×1 · VI.3 aperture×1 · IV.7 keyhole×2 · VI.5 aperture×4 bottleneck×6, mine,
fixed on the spot). `beat_ban_sweep` reported **one** of those twenty — VI.5 beat 3 — and only
because I happened to use the retired word when writing the beat line into `06`. **Had I described
the same beat in any other words, a chapter using a retired term ten times would have swept clean.**
⚠ **This is `feedback_instruments_go_where_instruments_are_cheap` at full strength:** the gauge sits
on one structured 3,000-line file with tidy beat lines, and the load-bearing surface — **149,752
words of prose** — is ungauged, because gauging it is harder. ✅ Repair is small and obvious: point
the same ban list at `book/*.md` and report per-chapter, use-vs-mention left to the reader. ⛔ **Do
not fix the chapters from the tool's first run** — see R-76 for why the count is not the finding.
**TRIGGER: with the cold tools pass.** small — the tool already has the list; it needs a second
input path.

**FILED — R-76: `07`:52 asserts the `aperture`/`bottleneck` retirements are "clean — every occurrence
is a mention," and against the prose that is FALSE.** Read in context on Day 190, all ten
pre-VI.5 occurrences are **uses**, not mentions: VI.1:129 *"barely an aperture, the stream hardly"*,
VI.1:140 *"the earlier structures become apertures one can use rather than prisons"*, VI.1:151/153/156,
VI.1:143 *"hold many keyholes and be captured by none"*, and VI.3:194 *"different apertures yield
different worlds"* — **which is C11's own formulation carrying a retired word**. IV.7:417 and :432
use *keyhole* twice in **Book IV**, where `05` §3 permits it "as an image in **Book I only**." ★ **The
`05` retirement's stated ground is "three names, one thing" — the collapse of `aperture`/`keyhole`/
`bottleneck` into the Perspective — and that is exactly what VI.1 and VI.3 are doing.** The rule is
not being technically breached on a formality; it is being breached at the precise point it exists to
protect. ⛔ **NOT REPAIRED HERE AND DELIBERATELY SO.** Clayton's block order is full draft → endnotes
→ audit → revision, and rewording four drafted chapters mid-draft is the revision pass arriving
early. **TRIGGER: the revision pass, first sitting.** ⚠ And the substitution is not mechanical —
VI.5 needed **three** attempts (`bottleneck` retired by `05` §3, `aperture` retired with it,
`narrowing` retired by **ruling 13** on the connotation screen) before landing on *carriage scarcity*,
which shares a root with the chapter's own card mechanism. **Each retirement was right and each was
right for a different reason.** Budget a real sitting, not a find-and-replace. small–medium

**FILED — R-77: RULING 35 FORBADE POSTING THE RETIREMENT ROSTER TO THE READER ON THE STRENGTH OF A
ZERO THAT HAS SINCE ROTTED — and nothing re-reads a ruling's premise.** `06`:573 states it plainly:
*"Measured before drafting: `aperture` 0, `bottleneck` 0, `keyhole` 0, `X` 0 **in every word of
drafted prose**. The reader has never met them and never will."* On that basis the beat was ruled a
**banned move** — the roster would be "a phantom introduced for the sole purpose of being buried."
★★ **The measurement was almost certainly TRUE when it was made** (the ruling is anchored to II.8, so
it dates from Book II drafting, when IV.7 and Book VI did not exist) **and it is FALSE now: twenty
occurrences, four chapters, ten of them pre-dating VI.5.** The reader meets them. The premise
expired; the ruling built on it did not, because a ruling is a *stamp* — an assertion made once,
which decays exactly like the thing it describes, and a rotten one looks like a fresh one.
★★ **THE CAUSAL LOOP IS THE FINDING, not the count.** Because Ruling 35 kept the roster off the page,
the reader was never given the retirement; because `beat_ban_sweep` reads `06` and not `book/`
(R-75), the drafter was never told either; so **the one decision that concluded "the reader will
never meet these words" is part of the reason nobody was watching them come back.** A ruling that
made itself unfalsifiable by removing the only surface on which its premise could be checked.
⚠ **Do not now simply reverse Ruling 35.** Its *reasoning* about anonymous self-reference (ruling 8,
*"as we argued elsewhere"* in editorial clothes) is untouched by this and may still forbid the
roster on independent grounds; what has failed is only the empirical clause. **The two must be
adjudicated separately or the reversal inherits a defect.** ✅ **The general repair is the one worth
more than the instance: rulings whose grounds include a MEASUREMENT need the measurement re-run
before the ruling is cited, and there is currently no mechanism that does this for any ruling in
this project.** **TRIGGER: with R-75's repair** — once the ban list reads prose, this ruling's
premise becomes a number a tool prints, instead of a sentence someone wrote down in Book II.
medium — the instance is small, the class is not

---

**FILED — R-78: THE NAVIGATIONAL RECAP LADDER GROWS ONE RUNG PER CHAPTER AND IS CORRECT AT EVERY
STEP, WHICH IS WHY NOTHING WILL STOP IT.** Each Book VI chapter closes by restating its predecessors'
navigational implications before adding its own. VI.4 restated one, VI.5 two, **VI.6 three**, and on
the established pattern VI.7 carries four and VI.8 carries five — at which point roughly a page of
VI.8 is a recitation of chapters the reader has just read. ★ **The reason this is filed rather than
fixed is that no single instance is wrong.** The ladder is the strongest device in the book: *cannot
look harder · cannot read more · cannot attend harder · cannot switch off* is a genuine escalation
and the reader needs the prior rungs in view to feel the tightening. **Every individual recap earns
its place; the sequence does not.** `prose_echo` scores VI.5~VI.6 at **18 shared grams, the heaviest
adjacent pair in the manuscript**, and every one adjudicated DESIGNED — which is exactly the reading
under which a tool stops being able to help.
⚠ **THE GAUGE CANNOT SEE THIS AND SHOULD NOT BE ASKED TO.** `prose_echo` reads words; the growth is
structural, and the honest adjudication of each pair is what makes the total invisible. **A sequence
of individually-correct decisions with no gauge on the aggregate is Drift #287's shape in a new
substrate** — not a stamp rotting, but a *ratchet with no counter on it*.
**Repair, for revision not now:** the ladder is stated ONCE in full, in VI.8, where it belongs
because VI.8 is the chapter about the tunnel the reader is in; VI.5, VI.6 and VI.7 carry a one-clause
back-reference instead of a restatement. ⚠ **Do not fix this before Book VI is drafted** — VI.7 and
VI.8 must be written against the pattern as it stands, or the repair gets applied to a shape that is
still moving. **TRIGGER: revision pass, after VI.8 ships.**
low individually — medium as a sequence, and the sequence is the thing

---

**FILED — R-79: `endnote_debt` READS ONLY THE FIRST LINE OF EACH ENDNOTE, SO 47% OF EVERY NAME IN
EVERY NOTE IN THE BOOK IS INVISIBLE TO THE GAUGE THAT STEERS THE RETROFIT.** `scan_notes` iterates
`NOTE_DEF = ^\[\^([^\]]+)\]:\s*(.*)$` compiled with `re.M`. In `re.M`, `.` still does not match a
newline, so `group(2)` is **the first physical line of the note and nothing after it.** Every note in
this manuscript is hard-wrapped at ~98 characters. A full bibliographic receipt — authors, title,
venue, volume, date, page range, the effect size, the quoted sentence — runs four to six lines, and
the parser sees line one.
**Measured Day 190 across every chapter that has notes** (which is Book VI only; the other 41 owe
receipts): names visible on line 1 **328**, names actually present in the notes **620**, **invisible
292 — 47%.** Per chapter: VI.1 34 hidden · VI.2 21 · VI.3 12 · VI.4 37 · VI.5 59 · VI.6 41 · **VI.7
88, the worst in the book.**
★★ **AND THE DIRECTION IS THE ONE R-71 NAMED, SURVIVING R-71's OWN REPAIR.** The hidden count scales
with the *thoroughness* of the note: a one-line note hides nothing, a six-line note hides five lines
of authors. **So the gauge steering the endnote retrofit penalises exactly the sourcing behaviour the
retrofit exists to produce**, for the second time and by a second mechanism. Day 190's rebuild
(`78bc127`) replaced the roster and left the parser, because the roster was the diagnosis and the
parser was never suspected. **A repair aimed at the named cause does not sweep for siblings.**
⚠ **VI.7 IS THE POSITIVE CONTROL AND IT IS BETTER THAN VI.4's.** VI.7 scores `sources 6 · notes 14 ·
owed 3 ⚠ Aristotle, Kako, Whorfian`. Of those three: **Aristotle** and **Whorfian** are the tool's
own declared LIMIT (a historical actor and an adjective, not sources). **Kako is a false positive of
this defect** — Alice January and Edward Kako are cited in `[^9]`, on line three of it, behind "Lera
Boroditsky," on line one. The chapter owes nothing and the gauge says three.
**Repair, derived against the code and NOT APPLIED:** `NOTE_DEF` needs to capture to the next `[^`
or EOF — `re.compile(r"^\[\^([^\]]+)\]:\s*(.*?)(?=^\[\^|\Z)", re.M | re.S)` — which is the pattern
the measurement above was taken with, so it is tested rather than proposed.
⛔ **IT IS DELIBERATELY NOT APPLIED IN THIS BREATH, AND THE REASON IS THE POINT.** This repair
*exonerates the chapter that found it.* Apply it here and VI.7's `owed 3` becomes `owed 2` by the
hand of the party it clears. **A repair proposed by the party it exonerates runs cold or it does not
run.** It belongs to the retrofit block, executed by a pass that is not cashing it, against a
before/after delta across all drafted files rather than an exit code.
**TRIGGER: ⛔ OVERDUE — 531 receipts are written.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** The retrofit ran steered by a gauge blind to half its output, exactly as this clause predicted, so the prediction is now a description. Re-homed to **the receipt audit**; R-69 and R-71 are paid and can no longer host it.
high — it is the instrument the next block runs on

---

**R-78 — FORWARD TEST CONFIRMED, no change to the row.** R-78 predicted, before VI.7 existed, that
"on the established pattern VI.7 carries four and VI.8 carries five." **VI.7 carries four** (VI.3
cannot look harder · VI.4 cannot read more · VI.5 cannot attend harder · VI.6 cannot switch off) and
adds its own fifth. The prediction was exact. ⚠ **This is a confirmation of the row, not a licence to
fix it now** — R-78's own instruction was that VI.7 and VI.8 be drafted against the pattern as it
stands, and VI.7 was. **TRIGGER unchanged: revision pass, after VI.8 ships.**

---

**FILED — R-80: THE CORPUS-SUPPORT SCRIPT'S ROOT NO LONGER EXISTS, AND ITS FAILURE MODE IS ITS OWN
HEADLINE FINDING.** `work/vi5_corpus.py` carries a hardcoded `ROOT` under `C:\Users\Wasch\` for the
quarry archive. **That path does not resolve on this machine** — the live clone with the matching
git history sits under `CLAWD_REPOS`. `os.walk` over a nonexistent directory raises nothing and
yields nothing, so the script runs to completion, reports `scanned 0 files`, and prints **0 against
every term in its list.**
★★ **The defect is not the dead path. It is that the failure is shaped exactly like the result.**
This instrument's contribution to VI.4, VI.5, VI.6 and VI.7 has each time been *a name at zero where
the vocabulary is everywhere* — so a broken run does not look broken. It looks like the strongest
finding the tool has ever produced, arriving in the chapter that most wants one. The `scanned 0
files` line is printed, and it is one line above forty lines of zeros that are far more interesting
to read.
✅ **Caught on the VI.8 run, and only because the term list happened to carry words that could not
honestly be absent** — *paradigm*, *modernity*, *the present*, *dated*. Those are the positive
control, and they were in the list by accident of drafting, not by design.
⚠ **The four prior chapters' counts are NOT retracted.** They were non-zero, which means they were
measured against a live tree; a dead root cannot produce a 23. **What is not known is which tree**,
and whether it is the same one VI.8 measured (3,069 `.md`/`.txt` files against VI.7's reported
2,586 — a gap that may be scope, may be growth, and has not been resolved).
**Repair, three parts, and the first two are cheap:** (a) the script **exits non-zero and loudly** if
`scanned == 0`, or if any member of a declared control list returns 0 — a null with no positive
control is not a result; (b) `ROOT` resolves from `CLAWD_REPOS` rather than a user path, so it
survives a machine change; (c) the tool is promoted out of `work/` into `tools/` with the rest of the
gauges, and the corpus root and file count are **printed into the log entry that cites it**, so a
later reader can tell which tree a count came from. ⚠ (c) is what makes the VI.4–VI.7 ambiguity
un-repeatable; without it, (a) and (b) fix the future and leave the record unreadable.
**TRIGGER: before the next chapter that runs a corpus-support screen — which is VII.1.**
medium — the instrument is cheap to fix and its failures are indistinguishable from its findings

---

## DAY 190, NIGHT — VII.1's TRIGGERS, READ RATHER THAN PASSED

*Four rows carried a trigger naming this chapter. All four were read before drafting, which is the
thing R-70's sweep found does not usually happen — a trigger is a note addressed to a reader who has
to show up, and this file has no reader except a breath that happens to open it.*

✅ **R-80 — DISCHARGED.** All three repairs shipped as **`tools/corpus_support.py`**, and the
discharge carries a positive control rather than an assertion. **(a)** dead root → **exit 2** with the
counts never computed; a declared control at zero → **exit 1** with the counts **suppressed**, because
forty lines of zeros are more interesting to read than the one line above them saying the scan failed.
**(b)** `ROOT` from `CLAWD_REPOS`. **(c)** the header prints root, git HEAD and file count, so a count
has an address: this run is **`C:\Users\mercu\clawd\repo-staging\Corpus-Perspectival` @ `8dcc440f` ·
3,069 files · controls consciousness=916, perspective=857, Ground=1273, the focusing=9.**
✅ **Proven, not argued — three runs:** dead root exit 2 · live root with an impossible control exit 1
· live run exit 0. ⚠ **The VI.4–VI.7 ambiguity stays unresolved and is not repairable from here** —
those counts were non-zero, so a live tree produced them, and which tree is not recoverable. That is
what (c) exists to make un-repeatable going forward, and it cannot reach backwards.

✅ **R-55 — DISCHARGED IN THE PROSE.** VII.1 reaches for the named-dead technology exactly where the
row predicted it would, and does not inherit the attribution: it is introduced as *older and more
widespread than any of the traditions that claim it*, receipted to **IV.7**, with Book V's
institutional form named as one case among many. The endnote states that crediting it to that
institution was an error the book made in its own drafts. ⚠ **The V.2 / V.11 / V.5 half of the row
is NOT discharged** — the parochialism and the sangha-absence in Book V are still on the page and
still owed at revision. **This row is halved, not closed.**

✅ **R-33 — DECIDED. VII.2 DOES NOT SPLIT; IT RUNS LONG.** The call was owed before VII.1 drafted and
is made here rather than deferred to the drafter who would discover it at 6,000 words. **Three
things decided it, and the third is the one that would have been missed.** (1) **Precedent:** R-29
gave IV.7 a decision instead of a declined split, and Book IV's mean is 4,607 words against Book VI's
4,480 — a 7,000-word chapter is inside this manuscript's demonstrated range, not outside it.
(2) **The eleven beats are four obligation SHAPES plus the argument, not eleven topics**; nothing in
the roster is compressible and nothing pairs. (3) ⚠⚠ **A SPLIT WOULD RENUMBER BOOK VII AGAINST
SHIPPED PROSE.** VII.3, VII.5, VII.7, VII.8 and VII.9 are named **by number** in drafted chapters and
in `07`'s `Depends` rows; inserting a chapter at position 3 silently repoints every one of them, and
**no gauge in this project reads a chapter number as a reference.** The cost is not the writing. It
is a renumber with no instrument watching it. **R-32's seam question is untouched by this and is
still owed before VII.2 drafts.**

✅ **R-70's re-run trigger (*before VII.1 opens*) — RUN.** Four triggers named this chapter; four
fired; four were read. **One counter-observation, filed against the row's own optimism:** they were
read because the handoff carried them into the breath, not because the queue was swept. The queue
was opened *to confirm what the handoff already said.* **A trigger still has no reader of its own.**

---

**FILED — R-81: THE CLAUDE FLATNESS FINGERPRINT SURVIVED A REPAIR AIMED DIRECTLY AT IT, AND THE
CONFOUND THAT WOULD HAVE EXCUSED IT WAS REFUTED BY ITS OWN TEST.** Specimen finding 5 named flat
escalation as the axis where the apparatus **amplifies** the fingerprint rather than correcting it.
VII.1 has C17's register ruling — *flat, not brave*, no sign at all — which supplies a clean excuse:
low dynamic range is the ruling being obeyed. ★ **The excuse is testable, because the ruling covers
the metaphysics and does NOT cover the grief section.** Predicted: first half flat, second half with
shape. **Measured, split at the grief heading: `dyn_range_CV` A 0.358 · B 0.168.** The half the
ruling does not reach is **half** the dynamic range of the half it does, at `voice_uniformity`
**0.771** — the highest figure recorded in this project, against Clayton 0.564 and my own raw prose
0.531. ⚠ **Repaired and re-measured: B → CV 0.276, uniformity 0.713, `emotion_label` 10.97 → 7.99.**
A large move, and **not a fix**: B is still the flattest section of the chapter, and the chapter
(0.345) is still flatter than VI.8 (0.518), III.8 (0.408) and V.11 (0.380). ★★ **The finding is the
survival, not the number.** A targeted rewrite of a 750-word passage, by an author who knew the
metric, aimed at the metric, closed roughly half the gap. **That is the shape of a fingerprint rather
than a habit**, and it means the four Book VII chapters where grief and affliction are the subject
cannot be defended by the register ruling. **TRIGGER: before VII.5 drafts** — affliction, the other
chapter where the game is barred and the register is ruled flat. ⚠ **Do NOT pay this by adding
escalation to the death chapters.** Escalation there is the banned address with the sign flipped, and
a repair that traded ruling 11 for a metric would be the gauge writing the doctrine. large

**FILED — R-82: `storyscope_lite`'s EMOTION METRIC HAS NO MENTION/USE SPLIT, AND FIRES HARDEST ON
THE CHAPTER WHOSE SUBJECT IT IS.** The pattern is literally
`grief|grieve|grieving|fear|afraid|dread|…`. VII.1 reads **3.51/1k** against Clayton's 0.39 and my
raw prose's 0.33 — ~10× — and the grief section alone reads **7.99**. ⚠ **The metric was built to
catch a chapter LABELLING an emotion instead of rendering it, and it cannot distinguish that from an
emotion being the noun under discussion.** `claim_sweep.py` has exactly this split and **prints a
self-test for it** (*mention/use self-test: PASS — the window is wider than a wrap and narrower than
a block*); `storyscope_lite` has neither the split nor a declaration that it lacks one. ★ **Same
family as R-80, one layer up: the instrument's failure is shaped like its finding.** A run on the
grief chapter returns the strongest reading the tool can produce, in the chapter that most guarantees
it, and a drafter who trusted it would delete the word *grief* from the grief chapter — **the gauge
writing the prose.** ⚠ **What is NOT known, and the row will not guess:** whether the 7.99 contains a
real labelling defect underneath the subject-matter floor. **Establishing that needs a control of the
same shape** — a passage by a human writer whose subject is also grief — and the project has no such
control. **TRIGGER: before any Book VII chapter's storyscope output is read as evidence.** Until
then the column is a description of the topic. small (the declaration) + medium (the control corpus)

**FILED — R-83: `dyn_range_CV` AND `voice_uniformity` DISAGREE ABOUT THE SAME FILE, SO R-81 IS
MEASURING TWO THINGS AND PRESCRIBING ONE REPAIR.** `storyscope_lite`'s own footer reads both columns
as one fingerprint — *`dyn_range_CV` LOWER = flatter = the Claude fingerprint · `voice_uniformity`
HIGHER = flatter = the Claude fingerprint.* **VII.2 scores non-Claude on the first and
most-Claude-in-the-sample on the second, in the same 8,499 words:** `dyn_range_CV` **0.550** —
above Clayton's 0.493 and above my raw prose's 0.505, the highest figure this project has measured —
while `voice_uniformity` is **0.6943**, the highest of every chapter sampled. ⚠ **A text cannot be
simultaneously the least flat and the most flat.** At most one of those columns is measuring the
fingerprint. ★ **And the house band is not what R-81 assumed:** VII.1 0.6884 · IV.5 0.6827 · III.5
0.6077 · VII.2 0.6943. VII.1's pre-repair **0.771 was the outlier**; its repaired 0.713 and VII.2's
0.6943 are ordinary for this manuscript. R-81 read a repair that "closed roughly half the gap" as a
fingerprint surviving — **the alternative reading, which the row did not consider, is that the repair
moved the text to the house norm and the house norm is where it already was.** ⚠ **This does not
refute R-81** — the death-chapter dynamic range really was low (0.345) and really did resist repair.
It refutes the row's *scope*: whatever `voice_uniformity` tracks, VII.2 shows it is not escalation
dynamics, so escalation repair was never going to move it and its failure to move is not evidence of
anything surviving. **TRIGGER: before R-81's repair is attempted anywhere.** Establishing which
column is the real one needs the two run against a text of KNOWN authorship and known register — the
same control R-82 already asks for and the project already lacks. **Do not spend a repair on a
composite signal.** small (the declaration) + medium (shared with R-82's control corpus)

**FILED — R-84 (DISCHARGED ON ARRIVAL, recorded for the size of what it did NOT change):
`endnote_debt.py` READ ONLY THE FIRST LINE OF EVERY RECEIPT.** `NOTE_DEF` compiles with `re.M` and
not `re.S`, so `(.*)$` stops at the newline; every note in this book is wrapped to ~80 columns, so
**any authority credited on line 2 or later of a note was invisible to `scan_notes` and the chapter
reported it as an unpaid source.** Found at VII.2, where Kant is credited in the second line of
`[^17]` and the chapter still printed `⚠ Kant` after the receipt was written. **Fixed** — the scanner
now splits on the note marker and reads each note's whole body. ⚠ **And the honest size, because the
temptation is to call this a mismeasured backlog and it is not one:** book-wide coverage moved
**30/124 → 34/124** (24% → 27%), four sources, all in Book VI. **Books II–V have zero notes at all**,
and a first-line reader and a whole-body reader agree exactly on zero — so the 41-chapter retrofit
queue was never mismeasured. ★ **The defect was sized to the work not yet done: it would have
under-credited every receipt written from the retrofit onward, and it was found by the last chapter
before that retrofit begins.** The fix also widens the tool's standing LIMIT — it cannot tell a cited
authority from a name that merely appears, and it now cannot tell across a longer window. Recorded in
the docstring rather than left for the next reader to rediscover. done

---

**FILED — R-85: `row_promotion_sweep.py` READS TWO OF THE THREE ROW FORMATS IN THIS FILE, AND ITS
FAILURE IS SHAPED EXACTLY LIKE ITS HEADLINE FINDING.** The gauge written after `PACKET-002` caught
ten unpromoted rows detects a row by `| **R-n** |` (table) and `### R-n` (heading). **Every row filed
since R-72 uses a third format — `**FILED — R-n: …**` — and the tool cannot see it.**

★★ **Measured Day 190 during `PACKET-003` assembly.** The sweep reported **74 rows**, *"9 FILED BUT
NEVER ROWED"* (R-75, R-76, R-77, R-78, R-79, R-80, R-81, R-83, R-84) and *"1 HOLE — R-82, nothing
anywhere ever filed it."* **All ten of those rows are in this file, with row heads, in the format the
tool does not match.** True count: **83 rows, R-1…R-84.** The one genuine gap in the series is
**R-24**, which the sweep did not report and which nothing anywhere documents — while **R-44, the
hole the project does know about, has a row saying so and is therefore counted present.**

⚠⚠ **THE DEFECT CLASS IS R-80's, ONE LEVEL UP: A BROKEN RUN LOOKS LIKE THE STRONGEST FINDING THE TOOL
HAS EVER PRODUCED.** This gauge's entire output vocabulary is *filed but never rowed*. When its
pattern goes stale, what it emits is *filed but never rowed* — nine times, with file citations
attached, arriving in the packet-assembly step that most wants a catch. **Nine rows were minutes from
being re-promoted as duplicates into the file whose charter is that it cannot certify its own
coverage.**

★★ **AND THE PART THAT IS ABOUT ME AND NOT THE TOOL.** Before running the gauge I ran my own grep to
count the rows, got **73**, and treated the near-agreement as corroboration. **My grep used the same
two patterns.** I derived the check from the tool's convention instead of from the file, so an
independent measurement reproduced the instrument's blind spot exactly and then certified it. The
count that would have caught this — *how many distinct ways does a row begin in this file?* — is one
line of Python and was never asked, because the question only occurs to someone who does not already
know the answer. **59 table · 15 heading · 17 `FILED` — three conventions, accreted, none declared.**

✅ **Repair, three parts.** (a) The matcher takes all three forms, and **prints its per-format counts
every run** so a fourth convention shows up as a format with a suspicious zero rather than as a
finding. (b) **A positive control**: the tool asserts a known-present row (R-1) resolves before it is
allowed to report any absence — R-80's rule, applied to the gauge that reports absences for a living.
(c) **Declare the row-head convention in this file's header** and stop the accretion at three.
⛔ **Do NOT close R-24 by inventing a row for it.** An undocumented hole and a documented one are
different objects; the sweep must learn to say which it found.

**TRIGGER: before `row_promotion_sweep.py` is cited in another packet — it has been run exactly twice
in its life, both times during packet assembly, and it was wrong the second time.** small (the
matcher) + small (the control) — and the class it belongs to is not small.

---

**FILED — R-86: BOOK VI CHANGES INSTRUMENT AT VI.4 AND NOTHING IN THE BOOK SAYS SO. THIS IS THE
PARENT OF R-87, R-88 AND R-89, WHICH ARRIVED AS THREE SEPARATE FINDINGS.**

★★ **Filed Day 190 from the outside read of `PACKET-003`.** The reviewer returned three findings
against Book VI prose, ranked by weight, and treated them as three. **They are one.** Every one of
them has its origin at the same chapter boundary:

- **VI.1–VI.3** print a five-line blockquote card: SEES · NULL SPACE · COMPLEMENTS · BOUNDARY ·
  NAVIGATIONAL IMPLICATION. **VI.4 prints a different card** — named CENSUS CARD, six fields,
  `Whose` added, `SEES` deleted, `BOUNDARY` replaced by `Mechanism of the exclusion`.
- **VI.1–VI.3 print no corpus count of any kind.** VI.4 is the first chapter in the book to print
  one.
- **VI.1–VI.3 perform C30 and license none of it** — VI.4 says so itself and rules that *"the
  earlier three owe a correction."* **VI.4 is the first chapter to license it.**

Three instruments changed at one seam, in one chapter, and the chapter declares exactly one of the
three changes. **The declared one is the only one that made the book look worse.**

⚠ **The mechanism, which is the part worth keeping.** This was read at first as *the fast-drafted
chapters carry the defects* — `PRE-REG-003`'s P5 said so in as many words. That is wrong, and it is
wrong in a way that flatters. VI.4 is not sloppier than VI.3. **VI.4 is where the apparatus was
upgraded, and an upgrade with no declaration is indistinguishable downstream from an
inconsistency.** Everything after VI.4 inherits three unmarked changes and then argues across the
seam as though nothing moved. **A book that improves its instrument mid-run and does not date the
change cannot later tell its own revisions from its own contradictions.**

✅ **Repair: a single declared instrument-change note, in VI.4, covering all three** — with the
version before and after each, and a forward pointer from `00-ARCHITECTURE.md`. Then R-87/88/89
become consequences of one declared event rather than three separate defects.
⛔ **Do not repair the three children independently first.** Fixing them one at a time removes the
evidence that they are one event, and the evidence is the finding.

**TRIGGER: before Book VII closes.** Book VII is drafting now, from the VI.8 card form, and the same
seam is being crossed again unmarked. medium.

---

**FILED — R-87: FOUR CHAPTERS PRINT CORPUS COUNTS ON FOUR DIFFERENT DENOMINATORS AND THEN RUN A
COMPARATIVE ARGUMENT ACROSS THEM. VI.8 ALREADY RULES THAT THE COUNTS ARE RHETORIC.**

★★ **The outside read's first-weighted finding, verified against disk Day 190.** The denominators:

| chapter | denominator | declared? |
|---|---|---|
| VI.4 | **2,550** `.md`, R-67 scope | yes |
| VI.5 | **3,069** `.md` + `.txt` | yes — *"a wider scope than R-67's declared 2,550"*, every figure a ceiling |
| VI.6 | *"the same corpus"* | **no — and there are two corpora it could mean** |
| VI.7 | **2,586** live files | **no — matches neither** |

The four chapters then run a **comparative** argument across those four bases —
topics-not-sources · discourse-not-history · indictment-not-evidence · practice-not-warrant. **The
four shapes are a real finding. The comparison is across four incompatible denominators, and VI.6
does not even say which of two it used.**

⚠⚠ **And VI.8 convicts all four in its own footnote 9, which is why this row is not merely a
consistency defect.** Fn 9 keeps its tallies off the page, reasoning that *"a file count in somebody
else's archive is a quantity no reader can obtain or check, which makes it rhetoric wearing a
number's clothes."* **That reasoning is correct and it is fatal to VI.4–VI.7, which print exactly
those numbers, in bold, as evidence.** From the reader's side this project's corpus *is* somebody
else's archive; the distinction VI.8 draws does not exist for anyone outside the repository.
**Four chapters do the thing the fifth rules is rhetoric — and the fifth is the one the author
thought was the most self-critical chapter in the book.**

✅ **Repair, and the honest one is the expensive one.** Either (a) VI.4–VI.7's counts come off the
page and the four shapes are argued from named specimens the reader can check, which is what VI.8
already does; or (b) VI.8's fn-9 rule is narrowed on the page to say why a count is admissible in
VI.4–VI.7 and not in VI.8 — **and no such reason has yet been produced.** (a) is almost certainly
right. ⛔ **Do not repair by re-measuring all four on one denominator.** That fixes the arithmetic
and leaves the rhetoric-wearing-a-number's-clothes charge exactly where VI.8 put it.

**TRIGGER: before the endnote retrofit reaches Book VI.** large.

---

**FILED — R-88: VI.5 AND VI.7 BOTH CLAIM TO BE C30's FOURTH INSTANCE, AND VI.7's OWN ENUMERATION
SKIPS VI.5.**

★★ Verified against disk Day 190. Three chapters, three incompatible accounts of one register event:

- **VI.4:** *"This chapter licenses it. The earlier three owe a correction."*
- **VI.5:** *"…declared here rather than performed quietly, **which is the fourth time in this
  book**."*
- **VI.7:** *"C30 is licensed here explicitly, **for the fourth time in this book** and the first
  time in Book VI that it is written down rather than merely performed"* — and then enumerates its
  prior three as **VI.2, VI.3, VI.4**.

Both cannot be fourth. **VI.7's enumeration omits VI.5, which is in the same book, doing the same
move, saying so explicitly.** VI.7's second clause also contradicts VI.4 outright: VI.4 licensed it
first, VI.5 invoked it by number, and VI.7 claims to be the first in Book VI to write it down.

⚠ **The root cause is that "instance" is never defined** — *performed*, *licensed*, and *declared by
number* are three different countable events and all three chapters count in different units without
saying which. **The register has no field for it**, which is why nothing caught this.

⚠⚠ **This is precisely the class `07-THE-CLAIMS-REGISTER.md` exists to catch, occurring in the book
where the register's methodological claim does the most work** — and the register ran C1…C30 before
Book VI opened and runs C1…C30 now. **A register that tracks which claims exist and not where they
fire cannot see a miscount of firings.**

✅ **Repair:** define the unit (recommend: *licensed* uses only, since that is what C30 governs),
recount from the text, correct all three chapters, and **add a per-claim use-log to `07`** so the
next miscount is caught by the file rather than by a reader. **The use-log is the actual repair; the
three corrections are its first output.** medium + medium.

**TRIGGER: with R-86.**

---

**FILED — R-89: THE CENSUS CARD CHANGES FORM FIVE TIMES IN EIGHT CHAPTERS AND IS NEVER ONCE
DECLARED — AND IT IS THE BOOK'S CENTRAL INSTRUMENT.**

★ Verified Day 190, all eight chapters read for card form:

| chapters | form | name | object carded |
|---|---|---|---|
| VI.1–VI.3 | blockquote, 5 fields | *(unnamed)* | a render |
| VI.4 | blockquote, 6 fields | **CENSUS CARD — THE PRINT RENDER** | a render |
| VI.5 | `###` heading, not a blockquote | **CENSUS CARD — THE BROADCAST RENDER** | a render |
| VI.6 | `###` heading | **Card: THE ALGORITHMIC RENDER** | a render |
| VI.7 | `###` heading, italic field labels | **The shrug, carded** | **a posture, not a render** |
| VI.8 | `###` heading, italic field labels | **The present, carded** | an era, from inside |

Form, name, field set and **object** all drift. VI.7's is the largest change and the least marked:
the card was built to characterize a *render* and is turned on a *posture* with one line of
acknowledgement and no ruling on whether the instrument transfers.

⚠ **The field deletions are the load-bearing part.** `SEES` disappears after VI.3 and `BOUNDARY`
after VI.3 — **`BOUNDARY` is where a render's limit was stated, which is the whole point of carding
one.** Its replacement, `Mechanism of the exclusion`, answers a different question. Nothing says the
question was changed.

✅ **Repair:** one canonical card spec in `06-THE-SCAFFOLD.md`, a declared version bump at VI.4 and
at VI.7 (with the posture-vs-render ruling written), and **a gauge — `tools/card_shape.py` — that
reports the field set of every card in the book and fails on an undeclared field change.** ⛔ **Do
not normalize the eight cards to one form silently.** The drift is evidence for R-86 and the
normalization would erase it; declare the versions instead.

**TRIGGER: before Book VII's first card ships** — VII.1 and VII.2 are already carding from the VI.8
form. small (spec) + small (gauge) + medium (the VI.7 ruling).

---

**FILED — R-90: VI.6 ASSERTED A RANDOMIZATION DESIGN THAT DOES NOT EXIST, INSIDE A CHAPTER WHOSE OWN
GRADE NOTE SAYS NO FULL TEXT WAS READ. ✅ TEXT FIXED DAY 190; THE CLASS IS THE ROW.**

VI.6 said the Gauthier et al. trial was *"stratified by which feed they were already using"* — body
text and footnote 4. **It was not.** Assignment was simple randomization at equal probability;
initial feed setting is a covariate — *"All specifications control for respondents' initial feed
settings."* The paper reports a **two-point imbalance in exactly that variable across arms (77% vs
75%)**, which a stratified design forecloses by construction, and contains **no instance of
"stratif-" in any form.** Verified against the PMC full text (PMC13061628), not the abstract.

★★ **The class, which is why this is a row and not just an edit.** The chapter's grade note said
plainly: *"What has **not** been done: no full text has been read."* **That disclosure was accurate
and it did not stop the chapter making a specific methodological assertion about the design.** A
grade note describes the *sourcing* and places no constraint on the *claims* — so a chapter can
correctly declare it has read only abstracts and then print a detail obtainable only from the
methods section, and nothing anywhere objects. **Honest labelling with no coupling to what may be
asserted.** ⚠ **Found by an outside reader, not by the label.**

✅ **Repair:** the grade note gets a second half — *claims licensed at this grade* — and abstract-only
sourcing licenses effect sizes, N and direction and **not** design internals (randomization
structure, blinding, stratification, exclusion rules). Sweep Book VI's other abstract-only sources
for the same overreach. ⛔ **Do not treat this as closed because the sentence is fixed.** The
sentence was one instance; the row is the missing coupling. medium.

**TRIGGER: with the endnote retrofit, which is the pass that reads full texts.**

---

**FILED — R-91: THE BOOK HAS A REGISTER FOR WHAT IT ASSERTS AND NONE FOR WHAT IT MEASURES WITH.
THIS IS THE PARENT OF R-54, R-86, R-88 AND R-89, AND THE OUTSIDE READ NAMED IT AS THE STANDING
RISK.**

★★ **Filed Day 190 from the TAIL of the `PACKET-003` read** (the first delivery truncated; Clayton
sent the remainder). The reviewer's closing sentence is the finding: *"the apparatus is proliferating
faster than it's being governed, and three of the five findings above are governance rather than
argument."*

**Measured against disk before filing.** The card is the book's central instrument. Its population
history:

| book | cards printed | distinct forms | declared changes |
|---|---|---|---|
| **IV** | ~22 (SEES 22 · NULL SPACE 21 · COMPLEMENTS 20 · BOUNDARY 20 · NAV IMPLICATION 22) | **1** | n/a |
| **V** | 2 of 11 chapters (R-54) | 1 | **the fork itself is undeclared** |
| **VI** | 8 | **5** | **1 of 4 changes** |

⚠ **The instrument was stable across twenty-two cards while it was doing less work, and destabilised
exactly when it got better.** Book IV's five fields never move. Book VI adds `Whose`, deletes `SEES`,
deletes `BOUNDARY`, adds `Mechanism of the exclusion`, migrates blockquote → heading → italic-label,
and turns the card from a *render* onto a *posture* — four changes across eight chapters, one
declared. **Drift from neglect would have shown up in Book IV, where the card ran most often. It
didn't. This drift is improvement, once per improvement, unlogged** — R-86's mechanism, at
population scale, across three books.

⚠⚠ **The structural cause, which is why this is the parent row and not a fourth sibling.**
`07-THE-CLAIMS-REGISTER.md` holds every claim the book asserts, with a licence discipline that works
(R-13 repaired, Book VI declares per chapter). **Nothing holds the instruments.** So: the card has no
version, *instance* has no defined unit (R-88), the corpus count has no declared denominator (R-87),
and the grade note has no clause about what it licenses (R-90). **Four rows, one absence.** Each was
about to get its own bespoke gauge — a use-log in `07`, a `card_shape.py`, a denominator rule, a
grade-note second half. ⛔ **Four gauges is the disease, not the cure.** That is precisely
*proliferating faster than it is governed*, performed in the repair.

✅ **Repair: one instrument register — `08-THE-INSTRUMENTS.md`** — holding, for each instrument the
book measures with: its **name**, its **current version**, the **chapter that declared each version**,
the **unit it counts in**, and **what a reading at this version licenses**. First four entries: the
census card, the C-licence use-log, the corpus count, the grade note. The bespoke gauges then become
consumers of one file instead of four unrelated scripts. ⛔ **Do not build the four gauges first.**

⚠ **AND THE FORWARD HALF, which is the part with a live trigger.** The reviewer's ruling on the card
is *rule the new line into the format explicitly, or the next book inherits two.* **`Mechanism of the
exclusion` is an improvement** — it is what lets a chapter say *why* the null space is invisible
rather than only that it is, and it is why Book VI's cards are sharper than Book IV's. It is kept.
**It is kept as a declared v2 field, binding forward on VII and VIII**, not as an undeclared
inheritance. VII.1 and VII.2 are already carding from the VI.8 form.

**TRIGGER: BEFORE VII.3 DRAFTS.** VII.3 prints a card; drafting it first crosses the seam a third
time unmarked and makes the register retrospective at the moment it is written. small (the register)
+ small (the v2 declaration) — and it retires four rows' worth of separate machinery. R-86, R-88,
R-89 and R-54 are its children and should be repaired *through* it.

---

**FILED — R-92: VI.8 HAS FORECLOSED VIII.2 AND CONSTRAINED VIII.3, AND VI.6 ALREADY PROMISED VIII.3
SOMETHING VI.8 THEN RULED OUT.**

★★ **The outside read's fourth finding, verified against `06-THE-SCAFFOLD.md` Day 190.** VIII.2's
scaffolded beats: *"how to find a filter you did not install · the era, the language, the family, the
wound · **the diagnostic that works and the one that flatters** · **why you cannot see your own null
space, and what you can do instead** — which is the whole practical content of the theorem."*

**VI.8 answered beats 3 and 4 and did it thoroughly.** Its ladder — cannot look harder, read more,
attend harder, switch off, hold nothing, check yourself — rules out six diagnostics and terminates in
exactly one procedure: convert a week into behaviour, hand it to someone outside your situation, ask
*what does this person clearly believe that they never argue for?* **That is now the only
self-diagnostic Book VI permits.** VIII.2 will either repeat it or contradict it.

⚠ **And the collision the reviewer could not see, because it is internal to Book VI.** VI.6 prints,
on the page, *"C12 stands, and this book will spend it in VIII.3."* Two chapters later VI.8 rules
five of the obvious edits out. **VIII.3 now carries a shipped public promise and a shipped
constraint, from the same book, two chapters apart, reconciled nowhere.** `06` line 3129 adds a
third: *VIII.3 prices the edit — removing the mechanism is not the edit.*

⚠⚠ **The class, and it is the one this project has already been bitten by once.** *A routing note
that sends content forward is a promise the destination silently cashes.* Day 190's earlier instance:
`02` sent the mirror/saccade experiment to Books III and VI, Book IV spent the saccade half, and
nothing anywhere recorded the spend. **This is the same shape one scale up — the thing spent is not
an artefact but a whole chapter's content**, and again the spend is invisible because a scaffold
records what a chapter is FOR, never what a previous chapter already SPENT or RULED.

✅ **Repair, and it is a scaffold decision, not a prose one.** Rewrite VIII.2's and VIII.3's beats in
`06` against what VI.8 has already spent and what VI.6 has already promised. ★ **The live remainder
looks real, and this is the direction, not the ruling:** VI.8's procedure is an **era-level**
instrument, run by a reader who has no stake in the situation. VIII.2's beat 2 — *the family, the
wound* — is untouched by it, and the outside-reader question does not transfer there, because for a
personal filter the outside reader has no counterfactual. VIII.2's live content may be that
narrowing. ⛔ **Do not settle this in a message; it gets a drafting session.**

⚠ **The scaffold's own ruling 142 makes this urgent rather than merely owed:** it holds that VII.2 is
the chapter that hands VIII its obligations, and *"sourcing VIII after VII is written means sourcing
it to fit what VII already promised."* **VII.2 has shipped.** So VIII now has two shipped creditors,
VI and VII, and the scaffold has been amended for neither.

**TRIGGER: before Book VII closes** — VII.4–VII.6 will route more to VIII, and every further route
made against an unamended scaffold is another promise cashed in advance. medium.

---

**FILED — R-93: VI.2 DECLARES ITSELF LOAD-FREE AND VI.7 PERFORMS ITS DEMONSTRATION BETTER.**

★ **The outside read's fifth finding, measured Day 190.** VI.2 prints its own sentence: *"Nothing in
Book VI's argument depends on Jaynes being right."* So a **19,932-byte** chapter in the book's most
prominent early position exists to demonstrate a discipline — holding a contested claim at three
grades with three defeat conditions — on material it says carries nothing. Defensible on its own.

**What makes it a row:** VI.7 runs the identical demonstration on better material — the
counterfeit-versus-practice distinction, a specimen from the project's own essays, and a scholarly
correction attached — at **37,976 bytes**, the largest chapter in the book. Two chapters, one lesson,
and the second is stronger.

✅ **Repair: none now, and the restraint is the ruling.** Clayton's block order stands — full first
draft, then endnote retrofit, then revision. **A chapter is not cut mid-first-draft on a
compression argument**, and Book VI is not in a compression pass. What is owed is that the
measurement is *on file* so the revision pass has a named candidate rather than a fresh opinion.
⛔ **Do not treat this as a licence to cut VI.2.** The reviewer's phrasing is conditional — *if Book
VI needs compression anywhere* — and nothing has established that it does.

**TRIGGER: the T&C revision pass, block 4.** small.

---

**FILED — R-94: `card_sweep.py` REPORTS `VII.2 ✓ CARDED`. VII.2 PRINTS NO CARD. THE TOOL'S OWN
DOCSTRING FORBIDS THE VERDICT IT PRINTS. ✅ GAUGE FIXED DAY 190; THE CLASS IS THE ROW.**

★★★ **Found Day 190 while building `08-THE-INSTRUMENTS.md` for R-91 — by running the existing gauge
instead of writing the new one.** R-91 said four rows were each about to grow a bespoke gauge and
named `card_shape.py` as one of them. **`card_sweep.py` already existed.** It ran, it was believed,
and it was wrong.

**The mechanism, one line of its own source:**

```python
carded = all(counts[f] for f in DIAGNOSTIC)      # DIAGNOSTIC = ("null", "compl")
```

Threshold **one**, anywhere in the file, any context, **no mention/use filter — though its sibling
`claim_sweep.py` has exactly that, written for exactly this reason.** VII.2 scores because it *quotes
Book IV's cards* four times (VII.2:486 *"The census card for the spirit of a place reads…"*, :337,
:341, fn 8 at :652) and uses `complement` once in ordinary English (:570, *"the person is precisely
the complement of a watershed"*).

⚠⚠ **The tool declared this limit correctly, in advance, in its own header:** *"the strong signal here
is the ZERO, never the small positive… A chapter with a 2 has possibly written one and must be read.
The instrument is trusted downward only, and that limit is declared rather than discovered later."*
**And then the output column printed `✓ CARDED`.** An accurate disclaimer in the docstring and an
unlicensed verdict in the output, with nothing coupling the second to the first. **That is R-90's
defect exactly — honest labelling with no constraint on what may be asserted — occurring in a gauge
instead of in a grade note.** The label was right. Nothing made the verdict obey it.

⚠⚠⚠ **AND IT IS R-62 FOR THE THIRD TIME IN ONE DAY.** *Nothing this project owns distinguishes prose
that ASSERTS from prose that DESCRIBES.* `where_the_book_is.py` read a sentence *quoting* a stale goal
title as a claim and reported the carrier 33/67 against a disk truth of 43. `card_sweep.py` reads a
chapter *quoting* cards as a chapter printing one. **Three instruments, one blind spot, three
unrelated routes, same day.** ⛔ **Book VII is where this bites hardest, because Book VII's job is to
spend Book IV's findings** — every Book VII chapter will cite cards, and under the old rule every one
would have scored as printing one.

**WHAT IT COST, and this is the part that is not hypothetical.** `Architecture/handoff/handoff.json`
asserted *"VII.1 and VII.2 are already carding from the VI.8 form."* **False, both chapters.** That
sentence was read off this tool's output — a disclaimer I had read and a verdict I trusted anyway.
The handoff then used it to justify R-91's ordering (*"drafting VII.3 first crosses the seam a third
time unmarked"*). **The trigger was right and its stated reason was fabricated by a gauge.** The seam
has *not* been crossed a third time; the register was written **prospectively**, which is strictly
better than the retrospective declaration R-91 thought it was racing.

✅ **DONE Day 190.** (a) `card_sweep.py`'s verdict now reads `? vocab-only — read it`, and its summary
states the licensed reading (the absences) instead of the unlicensed one (the deliveries), and points
at the structural tool. (b) `tools/instrument_sweep.py` written — structural, field-label based,
requiring 3+ distinct labels inside a 40-line window, so a citation cannot score.

✅ **WHAT SURVIVES, re-tested rather than assumed.** Book V's **2/11** — R-54's and the outside read's
headline — rests entirely on the **zeros**, the direction the instrument is valid in. **It stands.**
Book IV's 9/10 and Book VI's 8/8 were positives the tool could not license; both re-verified by hand
against field labels. Both correct. **The numbers were right and the method could not license them.**
A defect in an instrument does not void the decisions it informed — it obliges a re-test, and the
re-test passed.

**TRIGGER: NONE — closed.** The remaining assert-vs-describe class is the standing R-62.

---

**FILED — R-95: THE CARD FORKED IN BOOK IV TOO. R-89's AND R-91's CENTRAL CAUSAL CLAIM — "STABLE
UNTIL IT GOT BETTER" — IS FALSE, AND THE `Mechanism of the exclusion` FIELD SURVIVED UNDER ITS OWN
NAME FOR EXACTLY ONE CHAPTER.**

★★★ **Both halves found by `instrument_sweep.py` within twenty minutes of the register existing —
i.e. the register caught its own author, which is the only evidence that it is a gauge and not a
stamp.** Measured, `TOTAL 32 cards` across 55 drafted chapters:

| ver | cards | chapters | declared? |
|---|---|---|---|
| v1 | 25 | IV.1–IV.8 · V.1 · V.2 · VI.1–VI.3 | ✅ IV.1 |
| **v1b** | **2** | **IV.9** | ❌ |
| v2 / v2a / v2b | 3 | VI.4 · VI.5 · VI.6 | ❌ |
| v3 | 2 | VI.7 · VI.8 | ❌ |

⚠ **(a) IV.9 FORKS.** Its two cards drop **SEES, NULL SPACE, COMPLEMENTS and BOUNDARY** — four of
five — mark the subject *(contour)*, and add a field occurring **nowhere else in the book: `What
would make this wrong`.** The fork is arguably *principled* — an archetypal contour is not an entity
and has no null space in the census's sense — and it is **undeclared in exactly the way VI.4's is.**

⚠⚠ **So the causal story in R-86, R-89 and R-91 does not survive.** All three say: the card was stable
across ~22 cards while doing less work and destabilised *when it got better*. **It did not. The card
forks whenever the SUBJECT CLASS changes** — entity → contour at IV.9, being → era at VI.4 — and has
never once declared a fork. **That is worse, because the drift is not a Book VI phenomenon that Book
VI discipline would have prevented. It is a standing property of the instrument, present in the book
the project holds up as its stable case.** Book VI is where it was *noticed*, which is not where it
started.

⚠⚠⚠ **(b) `Mechanism of the exclusion` is printed under its declared name EXACTLY ONCE — VI.4:347.**
VI.5, VI.6, VI.7 and VI.8 all print the shortened `Mechanism:`. **So the field the outside read called
*the improvement* — the new line Book IV never had, the reason Book VI's cards beat Book IV's, the
field R-91 ruled must be kept — had already collapsed one chapter after it was introduced, and was
being praised in the collapsed form.** R-89 and the register's first draft both dated the shortening
to VI.7; it is **VI.5.**

⛔ **And the shortening is not cosmetic: it is what made the collapse invisible.** `mechanism` is
ordinary English in this book — VII.2 alone uses it five times in running prose. A label
indistinguishable from prose cannot be found by any gauge. **The full label is the only checkable
version of the field**, which is why `08` now forbids the short form from VII.3 forward.

*Also corrected: R-91's "~22 cards" for Book IV is a chapter count wearing a card count's clothes.
IV.3 and IV.7 print four cards each; IV.6 prints two plus one deliberately incomplete. True Book IV
population: **22** (20 v1 + 2 v1b) — coincidentally close, arrived at by a different route, and the
unit was undeclared. Third denominator in R-91's own population table.*

✅ **Repair: RECORDED, NOT REPAIRED.** `08-THE-INSTRUMENTS.md` carries v1b in the version table, the
withdrawn causal claim on the page beside the claim it replaces, and the ruling that a non-entity
subject **may** card as v1b **but only by saying so.** ⛔ `What would make this wrong` is a good field
and is **not** promoted into the canonical six today — promoting a field on the day it is discovered
is the reflex that produced five undeclared versions.

**TRIGGER: the revision pass** for the back-conversion and the promotion decision. The forward
binding is live now. small (recorded) + medium (revision).

---

**FILED — R-96: THE OUTSIDE READ'S ONE CROSS-BOOK CLAIM IS UNLICENSED, `08` CITES IT AS I4's
EVIDENCE OF WORKING, AND THE READER DECLARED ITS OWN SCOPE IN ITS FIRST THREE WORDS.**

Clayton, Day 190 evening: the Book VI notes came from **a separate instance** — not the reader
holding `PACKET-002`, and not one that has read Books I–V. The packet's §0 anticipated exactly this
case and gave it a reading order. It was not taken, which is a reader's prerogative and not a fault.
**The fault is downstream, and it is mine.**

⚠ **The read opened `Read all eight.` Book VI has eight chapters; the project has fifty-three
drafted.** The reader stated its scope accurately, in the first line, before any finding — and I
read a scope declaration as a completeness claim, then carried the one sentence that reaches past it
into a register.

⛔ **`08-THE-INSTRUMENTS.md` I4 · THE GRADE NOTE opens: *"It works — the outside read called it the
best-sourced work in the project, by a distance."* That is the only cross-book claim in the notes,
it is the load-bearing sentence of I4's `What it is`, and it is sourced from a reader who saw one
book of eight.** The register whose fifth field is *what a reading licenses* certifies its own
fourth instrument on an unlicensed reading.

⚠⚠ **And the claim was not the reader's to begin with — the packet handed it over before the read.**
`PACKET-003` §1, checklist row three, states: *"Book VI carries endnotes. It is the first book that
does. Books II–V: 0 notes across 37 chapters."* **The reader was given the comparison as context,
agreed with it, and the agreement came back reading as independent confirmation.** Circular, in the
same shape as R-62's self-amplifying citation, one layer out: the packet fed the finding it then
received as evidence.

⚠⚠⚠ **Measured tonight, the superlative is trivially true on one axis and FALSE on the other.**
`tools/endnote_debt.py`:

| book | sources | notes | covered | rate |
|---|---|---|---|---|
| I–V (43 ch) | 83 | **0** | **0** | — |
| **VI** (8 ch) | 32 | 59 | 25 | **78%** |
| **VII** (2 ch) | 9 | 20 | 9 | **100%** |

**"By a distance" is a distance from zero** — any receipt at all wins it. And on coverage rate the
book that beats Book VI is **Book VII**, which `PACKET-003` §0 declared **out of scope** in writing.
The reader could not have seen it. **So the sentence is a comparison across a field the speaker was
shown one member of, and the member it was not shown is the one that wins.**

✅ **WHAT IS NOT AFFECTED, stated so this is not read as voiding the read.** Every finding resting on
the eight chapters in front of the reader stands untouched — the card forms from VI.4 (R-88/R-89),
the C30 seam, the VI.6 `stratified by` assertion against an abstract-only grade note (the finding
that put I4 in the register at all), R-92, R-93. **Those are licensed by exactly what was read.** One
sentence reached past the scope; the rest did not. *(Ruling: an adjacent defect does not suspend the
decisions its instrument informed — it obliges a re-test. Re-tested; they hold.)*

✅ **Repair, done tonight, not deferred:** I4's `What it is` no longer cites the superlative. It cites
**VI.6** — a defect found *inside* the read's scope — which is better evidence for I4 existing than
praise was, and is the reason the instrument was written.

⛔ **FORWARD BINDING, live now, no gauge built tonight** *(promoting a field on the day it is
discovered is the reflex that produced five undeclared card versions — R-95)*: **a packet must
record the read-scope its reader declares, and no claim may be cited beyond it.** `PACKET-004`
carries a `SCOPE DECLARED` line, filled from the reader's own words, before any finding is filed.

⚠ **`PACKET-002` (Books I–V) IS STILL UNREAD AND NOTHING TONIGHT TOUCHED IT.** `PRE-REG-002` P2, P3
and P4 remain open and settleable only by an I–V read. The Day-190 read is a **fourth** outside read,
not the return of the second. Do not consolidate.

**TRIGGER: `PACKET-004`, before it ships** — the scope line. small.

---

**FILED — R-97: `navigate` IS THE LOAD-BEARING WORD OF THE ENTIRE ETHICS, OCCURS 43 TIMES IN DRAFTED
PROSE, AND IS NOT IN THE LEXICON.**

Found by VII.3's pre-draft screen while checking C8's `Depends` (156(d)). **43 occurrences across
IV.3, IV.4, IV.5, IV.7, IV.8, IV.9, IV.10, V.7, V.9, VI.1, VI.5 — and `05-THE-LEXICON.md` does not
define it.** `grep -i navigat 05-THE-LEXICON.md` → nothing.

⛔ **Why it is not a tidiness row.** VII.3's floor binds *"from everywhere that navigates."* That
phrase decides **who the ethics protects.** With the term undefined it can be read two ways that give
opposite books:

- **entry predicate** — *navigating* is the qualification, and things below it are outside the floor.
  **This breaches C8 in its own words** — *"no threshold, no gate, and no elect"* — and contradicts
  **shipped prose**: `VII-02`:213 prints C8 verbatim, :234 prints *"There is no line to draw."*
- **grounding predicate** — *navigating* names where the stake comes from, and comes in grades
  exactly as the focusing does. **This is what the source means** (*"what every navigator has a stake
  in simply by being one"*) and it is consistent with C7, C8 and VII.2.

**The book has been using the second sense and has never said so.** Fourteen chapters spent the word
before the chapter arrived that makes it decide something.

⚠ **The near-miss worth recording: nothing would have caught this.** `claim_sweep` checks banned and
canonical terms, `prose_echo` checks repetition, `pointer_sweep` checks numbers against titles. **No
gauge in `tools/` reads the lexicon against the prose in either direction** — not for terms of art
used-but-undefined, nor for defined-but-never-used. The screen found it by hand, from a `Depends`
row, on the eleventh consecutive chapter.

✅ **Not built tonight, deliberately** *(R-95: promoting an instrument on the day it is discovered is
the reflex that produced five undeclared card versions)*. The shape is a two-direction sweep with a
positive control: feed it a term known to be defined and a term known to be absent, and require both
to fire.

**TRIGGER: the lexicon entry BEFORE VII.4 drafts** — VII.4's *"every perspective without exception"*
spends the same extension, and the second chapter to lean on an undefined term is where an ambiguity
stops being one word and becomes a position. **The gauge is the revision pass.** small (entry) +
small (gauge).

---

**R-97 — PARTIALLY DISCHARGED, Day 190, and the repair found the row was scoped too narrowly.**
✅ **The entry is written** — `05` **§9a, ruling 168**, the grounding-vs-entry cut, with the tell
named (*the word next to a verb of admission*). ⛔ **But the sweep run to place it found the actual
defect: R-97 filed ONE WORD and the ethics has NO REGISTER.** `navigator` 33 occurrences / 0 entries ·
`contractive` live in two shipped chapters / 0 · `radiant` entering at VII.4 / 0 · `invariant` 8 / 0 ·
`keel` 3 / 0 · **`null space` 120 occurrences across 26 chapters with no cut made anywhere, which is
the largest single hole in `05`.** `05` §9 is opened on the §3b-bis precedent (a register is opened by
the chapter that needs it) and §9d **names what it did not screen so the absence is a record rather
than an oversight.** ⚠ **The lesson is the one the queue keeps re-learning: a repair scoped to the
named cause leaves the family standing.** R-97's own text said *book-wide* and then specified one
word; the word was the instance, not the class. **REMAINDER OPEN — §9d's list, and the two-direction
lexicon↔prose gauge, both revision-pass.** small (done) + medium (remainder).

---

**FILED — R-98: THE CLAIMS REGISTER WAS CUT SECTION-BY-SECTION, SO A CLAIM WHOSE SOURCE FLAGS A
FORWARD PAYMENT LOSES EXACTLY THE PAYMENT. TWO CONSECUTIVE CLAIMS, TWO CONSECUTIVE NIGHTS.**

C18 (Day 190, VII.3's screen): canonical carried limit (1), the source carried two, and the missing
one lived in a paragraph further down §Co-constitutivism. C19 (Day 190, VII.4's screen): canonical
seats the asymmetry in the terminal doctrine, and **the source relocates it two sections on, having
announced in advance that it would** — *"we mark the debt here and pay it two sections on."*

★ **That is a mechanism and not a coincidence.** C19 was extracted from §The two evils; its correction
lives in §Co-constitutivism. C18 was extracted from §Co-constitutivism; its missing limit lives later
in that same section. **Both are the same operation: extraction that respects the source's section
boundaries while the source's ARGUMENT crosses them** — and this source signposts its crossings in
plain English, which means the defect was findable by reading for *two sections on*, *pays in full
below*, *the debt marked here*, and nothing looked.

⚠ **THE SCOPE, AND IT IS THE UNCOMFORTABLE PART: 30 claims were cut this way and 2 have been checked.**
The two checked are the two most recently needed, which is not a sample — it is the chapters arriving
in order. **28 claims have never been read against their source at all.**

**TRIGGER: the next chapter's pre-draft screen checks its `Establishes` claim against the source
BEFORE the beats** — that is now three for three and it is cheap. **And a batch sweep of the source's
forward-payment signposts against all 30 canonicals, at the revision pass**, which is the only way
the 28 get read without waiting for 28 chapters. medium.

---

**FILED — R-99: A CRITERION SHIPPED IN A FOOTNOTE, ATTRIBUTED TO A CLAIM THAT DOES NOT HOLD IT.**

`coercive-and-locked` is the source's mark of evil in its settled form. It occurs **once** in the
drafted book — `VII-03`:447, endnote [^4] — filed under **C20**, whose canonical is *"sometimes the
focusing is the care."* C20 does not contain the conjunction. Neither did C19 until tonight. The
*over/through* half was at least registered, under C18; **the *locked* half was in no claim at all.**

★ **And §9b found why it could not be registered: the vocabulary that makes `locked` mean something
was never housed.** A frozen order-parameter is a phase description; without the order-parameter
account, *locked* is an image, and an image cannot be half of a criterion. **The unregistered clause
and the unhoused section are one defect seen from two ends.** ✅ Both repaired at VII.4 — C19 now
carries the conjunction, VII.4 takes the section.

⚠ **The class, which is what makes this a row rather than a fix: an endnote is a place a claim can
enter the book without passing the register.** `07` is the gate for canonical text and nothing gates
a footnote. **TRIGGER: revision pass — sweep every endnote in 54 chapters for load-bearing criteria
that appear in no claim.** No gauge does this and the shape is not obvious; it may have to be read.
medium.

---

**FILED — R-100: A BRIEF CAN BE OBSOLETE BY DELIVERY RATHER THAN BY ERROR, AND NOTHING MEASURES THAT.**

VII.4's brief listed five beats. **Four had already shipped** — two in VII.2, two in VII.3 — because
a chapter that argues a claim well necessarily spends the neighbouring claims' material getting
there. Every beat was *correct*. None was *outstanding*. `brief_fields` flagged VII.4 as THIN AND
UNDRAFTED and was right about the holes and blind to the surplus, because it counts fields and lines.

⛔ **The failure mode is specific and would not have announced itself:** the drafter opens the file,
writes beat 2, feels the familiarity, and resolves it as *this needs saying properly this time* rather
than as *this is already on page 185 of the book*. **Re-drafting reads exactly like drafting from the
inside.** `prose_echo` would have caught the verbatim overlap after the fact, at the cost of a
chapter — which is the expensive place to find it.

**The check that found it costs nothing and is now the screen's first move:** grep each beat's
load-bearing noun against `book/*.md` before writing. **TRIGGER: every pre-draft screen, starting
VII.5** — and a `beat_delivered` sweep at the revision pass, since 13 undrafted briefs were written
before the chapters that would spend their material. small (the habit) + small (the gauge).

---

**FILED — R-101: `claim_sweep` REPORTS 124 USE-CLASS HITS ACROSS 92 FILES, AND A 124-LINE REPORT IS
NOT READ. THE RULE THAT FIRES AND THE RULE THAT DOES NOT EXIST HAVE THE SAME EFFECT, AND THE FIRST
ONE IS WORSE.**

Found Day 190 while writing `05` §9c — **by the correction of a false claim I had just written.** §9c
first said `aperture` had survived its demotion because *"a lexicon ruling with no gauge behind it
survives its own retirement,"* citing `the map`. **Running the tool refuted it in one command:
`claim_sweep.py` has a `TERM/aperture` rule, it fires on all seventeen occurrences, and it was firing
on VII.3's ten the night VII.3 shipped.**

⛔ **That is the opposite class from `the map` and it is the worse one.** `the map` survived because
nothing watched. `aperture` survives **while being watched and reported**, because the report is 124
lines and 124 lines get skimmed for the chapter just drafted. **And the register can then point at the
rule and say the word is gauged** — a detector nobody reads is an alibi, which is a thing an absent
detector cannot be.

**Measured, same output, same night:** VII.3 shipped carrying 2 `TERM/narrowing` · 2 `TERM/stream` ·
10 `TERM/aperture`, all live, none adjudicated. VII.4's own 8 `TERM/narrowing` hits were caught only
because this screen grepped the output for the new chapter's filename by hand.

★ **The repair is not a new rule. It is a diff.** `claim_sweep` should report **hits in files changed
since the last commit** at the top, in their own block, with the book-wide total kept below as a
standing figure. A drafter reads eight lines. Nobody reads 124. ⚠ **And the second half, which is the
part that would actually have caught this:** the tool has no notion of *adjudicated* — every hit is
new every run, forever, so the pile can only grow and the growth carries no signal. An
`ADJUDICATED.md` keyed on file+line+rule, with anything unmatched printed loud, converts the report
from a wall into a delta.

---

**FILED — R-102: A MANDATED STRING IS SITTING IN AN AUTHORSHIP TABLE, AND THE TABLE GROWS AS THE
SQUARE OF THE CHAPTERS THAT OBEY THE MANDATE.**

`instrument_sweep` requires the v3-canonical card's six field labels **and their glosses**, verbatim,
in every bound chapter. `prose_echo` reads words and therefore convicts every bound chapter of
echoing every other bound chapter, six grams per pair. The exemption doctrine is right and is the
problem: *never a chapter, never a phrase alone — always a specific PAIR plus a specific gram.* So
VII.3~VII.4 cost six lines, VII.5 cost **twelve**, VII.6 will cost eighteen, and by the end of Book
VIII the table holds several hundred entries all saying the same sentence about a string nobody
chose.

⛔ **The cost is not the line count. It is that a table of hundreds of identical rows is a table
nobody reads** — R-101's finding, arriving in the other gauge, by a different route, one day later.
The identical rows are camouflage for the one row that is a real adjudication.

★ **And the repair is NOT a wide exemption.** The doctrine is correct about *authored* prose and must
not be relaxed to fix this — see the standing rule that a gauge is never loosened by the party it
would convict. The right move is a **second kind of entry**: a gram that `instrument_sweep` mandates
is not authorship at all and does not belong in an authorship table. Declare `MANDATED = [...]`
separately, print its suppressions as a count rather than as rows, and leave `EXEMPT` for
adjudications. **TRIGGER: before VII.7 drafts** — at eighteen rows it is still a cheap refactor and at
VIII.3 it is not. small.

---

**FILED — R-103: THE JUSTIFICATION FOR A LEXICON RENAME CITED A GAIN THAT DOES NOT EXIST, AND THE
CLAIM WAS COPIED INTO A SECOND FILE WITHOUT EVER BEING CHECKED.**

`prose/RULING-13`:100, arguing `narrowing → the Focusing`: *"'Sometimes the focusing is the care'
survives as non-trivial — attention as love is a real claim, and **it collects Weil for free in
`03`.**"* `07`:589 repeats it under ruling 155: *"it collects Weil directly (`03`)."*

**`Weil` = 0 in `03-THE-ANCESTORS.md`. Zero, in any spelling, anywhere in the file.**

⛔ **And the error is not a missing entry — it is a category confusion that a present entry would not
have fixed.** `03` is a register of **measured silences**: names the corpus knows and the book does
not. Weil has no silence recorded there because she was never audited at all. A claim that a phrase
"collects" her *in* `03` cannot be true of that file for any name, so the sentence was never checkable
in the form it was written, and it was cited twice as a benefit of a rename that changed 62 sites in
11 files.

⚠ **What makes it a queue row rather than a typo:** the rename was ruled partly *on* this gain, and
the second copy was written on Day 189 by a screen whose entire subject was ruling 155's own
propagation failure. **A false clause survived the audit that was reading its neighbours.**

**Owed:** delete the clause from both files, or enter Weil in `03` and make it true — and the second
is the better repair, since `malheur` is now a chapter's hard floor and she is the only ancestor in
the book whose term the work cannot override. **TRIGGER: with R-106, one sitting.** small.

---

**FILED — R-104: R-100'S CHECK HAS NO SPECIFICITY DISCIPLINE, AND ITS FALSE POSITIVES POINT THE
EXPENSIVE WAY.**

R-100 rules the pre-draft screen's first move: *grep each beat's load-bearing noun against
`book/*.md` before writing.* It ran on VII.5, first time out, and **returned two false positives in a
five-beat brief, by two different mechanisms.**

**(a) The homograph.** `malheur` returned `book/IV-03`. The hit is **Malheur National Forest** — the
*Armillaria* honey fungus, eastern Oregon, in the chapter on the living non-human. Same book, same
author, correct capitalisation for a proper noun, and a filename-list grep shows only `IV-03`.

**(b) Dilution.** `arrow` returned **twenty-five files**. The two-arrow distinction is in none of
them; `Sallatha` = 0, `two arrows` = 0, `second arrow` = 0 across all fifty-five drafted chapters.

⛔ **Both failures point the same way and it is the costly direction.** R-100's known failure was
*beat already written, drafter re-writes it* — expensive, but `prose_echo` catches it after the fact.
**This failure is *beat looks written, drafter skips it*, and nothing catches that at all**, because
an absent section leaves no echo. Had the homograph been believed, the chapter would have shipped
without naming `malheur` — **the one term C21 says no clause of this book overrides.** The check
built to stop a re-draft would have deleted the floor.

**Repair, and it is a habit not a tool:** grep the beat's **distinctive phrase**, not its
load-bearing noun; read the matched **lines**, never the filename list; and treat a single hit in a
distant book as a homograph until read. **TRIGGER: it is already the screen's first move — this row
is the amendment, and it applies from VII.6.** small.

---

**FILED — R-105: RULING 155 NAMED THE MECHANISM CORRECTLY, FIXED FOUR SITES IN ONE FILE, AND DID NOT
SWEEP THE OTHERS — AND THE SEED IT MISSED IS A FILENAME, WHICH NO SWEEP CAN REACH.**

Ruling 13 retired `narrowing`. It did **not** retire `contraction` — it *reassigned* it to C19. So
every site where C20's meaning still wore C19's word was invisible to a find-and-replace and to every
gauge downstream of one. Ruling 155 found four such sites, all in `07`, and named the mechanism
exactly.

**Two live sites remain in `06`, and they are the briefs of the two chapters C20 establishes:**
`VII.5` (*appropriate contraction*, the beat that carries C20's whole positive claim) and `VIII.5`
(***contraction as care*** — C20's pre-rename canonical, in bold). Both fixed Day 190. A third site
at VIII.5 (*imposed contraction*) was fixed on different grounds: VII.5's prose now makes it false.

★ **The seed is traceable and is the part worth keeping.** `06`:3356 lists Book VII's sources, one of
which is the corpus file **`suffering-and-appropriate-contraction`**. The beat label is the filename.
**A filename cannot be renamed by a vocabulary sweep and cannot be excluded from one** — it is the one
door into the prose that every lexicon gauge is structurally blind to, and it opens straight into the
brief of the chapter that most needed the distinction held.

**Owed:** a `06`+`00` pass for `contraction` in C20's sense — done for the two known sites, **not
certified for the file**, and the difference is the whole reason this is a row. Plus one line in `05`
§3a recording that source filenames are a vocabulary vector. **TRIGGER: before Book VIII opens**,
since VIII.5 and VIII.3 both live downstream of the seed. small.

---

**FILED — R-106: HEIDEGGER IS ROUTED NOWHERE IN THE ENTIRE REPOSITORY, AND THE CHAPTER THAT MOST
OWED HIM HAS SHIPPED.**

`Heidegger` = 0 and `Angst` = 0 across all fifty-five drafted chapters — **and across `00`–`08`,
`book/DRAFT-LOG.md` and this file.** Not a gap in the prose with a plan behind it. **No plan.** He is
in neither `03`'s silence register nor `ancestor_gap`'s report, because `ancestor_gap` reads a seed
list and he is not on it, so the tool built to find exactly this could not see him. ⚠ The same is true
of Weil, Murdoch, Arendt and Levinas — **`ancestor_gap`'s "known in the research, absent from every
drafted chapter" is a curated list presented in the grammar of a measurement.** That is a second row's
worth and is noted here rather than split.

**He is the source's own mechanism.** Doctrine §9.2 and Guide §6.4 both run suffering-as-disclosure on
the analysis of *Angst* from *Being and Time* — the territory between ordinary suffering and
affliction, which is most of a life. VII.5 names him and uses him only to mark the two-arrow card's
reliable range; it does not develop him.

⛔ **VII.1 is DEATH and shipped without him** — the twentieth century's dominant account of death as a
structural feature of a position, absent from the chapter on death, and no gauge said a word. Recorded
here, **not repaired now**, per the standing no-retrofit discipline.

**Owed:** an entry in `03`; a routing decision for VII.9 (*being-toward-death* bears directly on
identity across gaps); a VII.1 revision row. **TRIGGER: with R-103, one sitting — both are `03`
entries and both were found by the same screen.** small + medium.

---

**FILED — R-107: TWO DIFFERENT CLAIMS IN `07` EACH ASSERT THEY WOULD BE *THE ONE* PROVABLE LIE IN THE
BOOK, AND ONE OF THEM HAS NOW SHIPPED IN PROSE.**

C21's trap: *"**A book that made affliction meaningful would contain the one provable lie in it.**"*
C23's canonical: *"**A finished account of a live ground would be the one provable lie in it.**"*

*The one* is a uniqueness claim. It is made twice, about different things, four hundred lines apart in
the same file, and both are load-bearing — C23 is ruled *"draft it last and draft it hardest."*
**VII.5 shipped C21's version verbatim**, which means the collision is no longer confined to the
apparatus: whichever of the two survives, the coda now has to be written knowing the phrase is spent.

⚠ **This is ruling 155's defect one level up, in rhetoric rather than in vocabulary** — a superlative
is a name, two claims are wearing it, and no gauge in this repo watches a superlative. `claim_sweep`
reads terms; `prose_echo` reads chapters against chapters and does not read `07` against itself.

**Owed:** one of the two gives the phrase up. **My reading, offered rather than ruled: C21 keeps
it** — *provable* is doing real work there, because affliction has a witness who could check the
claim, and an unfinished account has no comparable checker. C23's point survives intact as *unfinished
≠ uncertain*, which is its actual content and does not need the superlative. **TRIGGER: before C23 is
drafted, which is last.** small.

⚠ **Do not read this as licence to allowlist.** The 17 `aperture` hits stay open and stay unruled
(`05` §9c, and the reason is that the drafter who wrote them may not exonerate them).

**TRIGGER: before the next packet cites `claim_sweep` for anything** — R-85's trigger has the same
shape and the same cause, and it is the second gauge in this book found to be reporting truthfully
into nobody's hands. medium.

---

**FILED — R-108: THE CHAPTER SENDS A READER TO HARVEY AT A LOCUS HARVEY DOES NOT USE.**

`IV-09-the-archetypal.md`:233–236 reads *"Go and read II, 7, 5"* and then, three lines later, *"The
Latin as Harvey prints it."* **Both halves are individually true and the pair is a trap.** II.7.5 is
**Massuet's** division — Jung's footnote, and ANF's, and the chapter correctly attributes it to Jung.
**Harvey prints this passage at `LIB. II. vi. 3`.** Verified Day 190 on two independent Harvey scans,
each of which carries that marginal head *and*, beside it, `MASS. II. —`, because Harvey himself knew
his divisions diverge and printed the concordance the chapter omits.

So a reader who does what the chapter tells them — take Harvey down, turn to II.7.5 — lands in a
different chapter and finds no *si*. **The one span in the volume an outside reader could not check is
now checkable, and the instruction for checking it is wrong by one number.**

★ **The general form, which is why this is a row and not a typo:** an edition and a citation-scheme
are two different facts, and prose that names one while numbering by the other reads as a single
correct citation. Nothing in `tools/` can see this — there is no gauge here that knows what edition a
number belongs to.

**Owed:** one clause — *(Harvey `II. vi. 3`; Massuet/ANF `II. 7. 5`)*. **TRIGGER: the next time IV.9 is opened for any reason** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** — its endnote-pass half fired days ago and nothing announced it; the surviving half is live and is now the whole trigger — it is
receipt-level and it is the receipt the retrofit exists to write. ⚠ **And check the same pair
everywhere the book cites a critical edition by a standard-scheme number** — this is one instance and
the sweep has never run. small.

> ✅ **SIBLING CLAUSE DISCHARGED, Day 190 night — `review/SWEEP-001-day190-edition-scheme.md`,
> `tools/edition_scheme_sweep.py`.** The sweep ran: **10 exposed loci across the 56 drafted
> chapters.** One is this defect; two are verified (`V-06` tonight, `III-02` under R-30); seven
> remain `◻`. **The main clause above — the `IV-09` clause itself — is still OWED.** ⚠ And the
> sweep's own result forbids reading it as a clean bill: see R-110. Three defects in the instrument
> were found mid-run, one of which cut the hit list 11 → 5 and made it look *better*.

---

**FILED — R-109: A BARE TOPONYM IN THE IMPRINT SLOT, AND THE IMPRINT IS SOMEWHERE ELSE.**

`V-06-the-room-that-was-never-emptied.md`:103 cites the block quotation as *"**Nefesh HaChayim**,
Gate III, chapter 4. Volozhin, published 1824, in Leonard Moskowitz's translation."* Everything in
that string checks out except the third element. **The *editio princeps* is Vilna (with Grodno),
1824** — brought to press by the author's son R. Yitzchak and his nephew R. Avraham Simcha of
Mstsislaw. **Volozhin is where Chaim lived**, and he is named *Chaim of Volozhin* two paragraphs
above.

In the slot `Title, locus. Place, year, translation.` a bare toponym reads as **place of
publication**, and under that reading the citation is false. ★ **This is R-108's general form one
notch over: two different facts — an author's toponym and a place of imprint — collapsed into one
string that reads as a single correct citation.** Nothing in `tools/` can see this either, and
`edition_scheme_sweep.py` cannot: it locates the pair, it does not adjudicate it.

**Also owed on the same line, and smaller: two unmarked elisions inside the quotation marks.** The
32 quoted words are Moskowitz's exactly, diffed in code — but `[emphatic]` and `(blessed be He)` are
both cut with no ellipsis, and `Ein Sofe` is silently normalised to *Ein Sof*. Dropping the
translator's apparatus mark is defensible; cutting running text without a mark is not. **The mild
form of the Day-188 Irenaeus finding — an abridgement wearing an unabridged quotation's clothes.**

⚠ **The verification behind this row is ONE-WITNESS, not two-digitisation** — Sefaria's Moskowitz is
marked `Rev. 1.5`, a revised digital text rather than the 2012 print. Recorded as such rather than
rounded up.

**Owed:** `Vilna, 1824` (or drop the imprint and let the translation carry the citation); an ellipsis
or a restoration at the two cuts. **TRIGGER: the next time V.6 is opened for any reason.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** Its endnote-pass half fired unobserved; the surviving half is live. small.

---

**FILED — R-110: THE EDITION SWEEP'S CLEAN RESULT IS A FALSE NEGATIVE BY CONSTRUCTION, AND R-2 IS
WHAT MAKES IT TRUE.**

`edition_scheme_sweep.py` reports **10 exposed loci / 368 distinct cited works — 2.7%.** That is not
a book with few edition-bound citations. **It is a book with almost no citations yet.** Books II–V
carry **zero endnotes across 37 chapters**; they name Śaṅkara, the Zohar, Plotinus, Irenaeus, the
*Brahma Sūtra* and *Nefesh HaChayim* in the sentence and give no locus, so there is no pair to
inspect. **The most edition-sensitive material in the volume sits in exactly the region with nothing
to check.**

★ **The endnote retrofit does not reveal this population — it CREATES it**, roughly ninety citations
at once, written fast against sources held open. That is precisely the condition that produced
R-108.

★★ **The general form, and it is the third instance: the instrument goes where the instrument is
cheap.** A gauge clusters on the checkable region and reports its silence there as health. The
number `2.7%` is a statement about the apparatus, not about the citations.

**Owed:** not a fix — a **standing obligation**. `edition_scheme_sweep.py` is a **mandatory step
inside R-2**, re-run per book as each book's notes are written, with the delta recorded. Written in
three places so it cannot go silent: this row, the tool's docstring, the tool's printed LIMIT line.
**TRIGGER: ✅ RE-HOMED TO THE EDITION-POLICY RULING (`00`, ruling 177), where this obligation now lives in writing.** ✅ **SATISFIED IN PASSING.** R-110's standing obligation — *`edition_scheme_sweep.py` may not be skipped before a book is declared complete* — **lost its host when R-2 died.** The sweep **ran Day 195** against IV.10 and Book V with the delta recorded (and the delta is **zero**, which ruling 177 predicted in advance and is the honest reading, not a pass). **The obligation now rides on ruling 177 and is written there, so it cannot go silent a second time.** medium.

---

**FILED — R-111: THE TWO REVIEWER PACKETS HAVE NO RETURN DATE, WHICH MEANS THEY HAVE NO DEADLINE
THAT CAN BE MISSED.**

`PACKET-002` (Books I–V) went out **Day 189**. `PACKET-003` (Book VI) went out **Day 190 afternoon**.
Both are unreturned, and the handoff has named the outside read as **the binding item** for two days
running while the drafting lane kept moving.

**Neither packet carries a date.** A dependency with no dated trigger does not stall loudly; it
stalls **invisibly**, because every check of it returns the same true answer — *still out* — and that
answer never becomes an alarm. Book III in particular has had **no outside read at all** and holds
**C9**, the hinge every Book VII obligation sits downstream of.
⚠ **CORRECTED DAY 194:** "no outside read at all" was never measured — `review/` holding no return
measures **returns**, not readers. Clayton, Day 194: *"several models read the work, I've read the
work, and I also have some individuals slowly reading it."* Read **no RETURNED outside read**
everywhere this entry says "no outside read." The dated-trigger argument above is unaffected and
stands. See C9 in `07-THE-CLAIMS-REGISTER.md`.

★ **This is [[deferral-wearing-deference]] exactly: a decision I own, routed to someone else with no
dated trigger, stalls forever and looks like patience.** The remedy is not to chase — it is to make
the silence expire.

**Owed:** a dated check on each packet, and a pre-committed action for the case where the date passes
unanswered *(the honest default: draft on, and mark every C9-downstream Book VII claim PROVISIONAL in
the register rather than pretending the read happened)*. **TRIGGER: `PACKET-002` — Day 194.
`PACKET-003` — Day 195.** Both set tonight, by me, not by Clayton. small.

✅ **R-111 PART ONE — FIRED AND PAID, Day 194 / 2026-08-13 10:2x. `PACKET-002` IS STILL OUT ON DAY
FIVE, AND THE PRE-COMMITTED ACTION RAN INSTEAD OF THE WAIT.** The reminder arrived on the date it was
set for, the condition was checked rather than assumed, and it held: `review/` holds **no I–V return**
and no commit since Day 189 carries one. Both halves of the pre-commitment executed —
**(a)** one line to Clayton asking only whether the packet *reached a reader or never left*, the two
cases that need different responses and only he can see which; **(b)** `07-THE-CLAIMS-REGISTER.md`
now carries the mark: **`PROVISIONAL` defined once in the preamble**, **C18 and C19 marked**, **C9's
own entry stating plainly that no outside read has come back on it**, and the reconciliation with
**C23** written *at C23*, where the objection will be filed. ⚠ **THE REGISTER SAID SOMETHING
STRONGER THAN THAT UNTIL 12:0x, AND SO DID THIS LINE:** *"nobody outside this project has read it."*
Corrected in all three artifacts the same day — see the C9 entry.

★ **THE THING WORTH KEEPING IS WHAT THE MARK IS NOT.** It changes **no prose**, softens **no claim**,
and cannot be cleared by time — only by an outside read of **Book III**. A status mark that decays on
a clock would be the stamp this project keeps catching; this one has exactly one exit and it is a
read. ⚠ **And the scope is written down at C23 rather than left in a head:** C17, C20, C21, C22, C16
were tested against C9's dependant list and **declined with the reason on the page** — C20/C21 sit
one hop further out, through C19, and marking a second-order path inflates the mark until it means
nothing. *(A partial with no record of its boundary reads as a complete sweep —
[[partial-delivery-has-no-gauge]].)*

⛔ **R-111 PART TWO — THE DAY-195 TRIGGER IS RETIRED, NOT DEFERRED, AND IT WAS ABOUT TO FIRE FALSE.**
`PACKET-003` **came back**: `aaa657f` (three findings verified, `PRE-REG-003` scored) and `780c9e9`
(the tail, `PRE-REG-003` closed). Its reminder was still `pending` for tomorrow 10:00 carrying the
words *"if unreturned"* about a packet returned four days earlier — **true when filed, false when
delivered, and it would have arrived asking me to mark claims over a read that had already landed.**
Cleared today rather than answered tomorrow. *([[queued-message-goes-stale-in-flight]], third
instance; the new wrinkle is that this one would have gone stale by **succeeding** — the condition
was retired by the good outcome, and nothing was watching the trigger that the outcome invalidated.)*
⚠ **The one live clause inside it survives its retirement and is now carried by the register instead:
Book III has had no *returned* outside read.** ★ **AND THAT WORD WAS MISSING HERE FOR SIX HOURS.**
As first written this clause said *"no outside read at all"* — a claim about readers, derived from a
gauge that can only see returns. Clayton falsified it the same morning: reads of I–V are **in
progress**. The correction is [[absent-artifact-is-not-absent-reader]], and it had to be chased into
three separate pushed artifacts, which is [[correction-does-not-reach-the-citers]] paying out on
schedule.

---

## BOOK VII OUTSIDE READ — Day 191 afternoon

**Provenance, recorded before the findings, per [[briefing-manufactures-the-agreement]].** Clayton sent
Book VII to an Opus instance while the Books II–V endnote retrofit was running. The reader opened with
*"Read all nine"* — an accurate scope declaration; Book VII has nine chapters. **No packet accompanied
it**, so unlike `PACKET-003` there is no supplied framing for their agreement to echo back. Their one
prior-context reference — *"the four post-atlas cases I flagged"* — means this reader has seen earlier
material and VII.2 was written to pay a debt they named. **Whether this is the same instance as the
Book VI reader is unknown and matters**: if it is, findings 2 and 3 are one reader noticing their own
prior class again, not two independent detections of it. Asked; unanswered at filing.

**Numbering note: this file jumps R-111 → R-119.** R-112–R-118 exist in `DRAFT-LOG.md` only. That is
R-117's filed-unfixed half and it is still open; the jump is a gap, not a misnumber. **TRIGGER
unchanged: before R-2 starts.**

**All seven findings were checked against the prose before filing. All seven hold.** Two are
understated by their own author and are filed at the size they measure, not the size they were
reported at.

---

**FILED — R-119: VII.4 ATTRIBUTES TO VII.3 AN ARGUMENT VII.3 EXPLICITLY DECLINED, AND C19'S OPERATIVE
SEAT RESTS ON IT.**

`VII-04` line 272: *"He does not slip it. The last chapter is where that was shown, at length"* — and
line 275, *"his road forks and both forks close."* The figure it says that about is introduced at line
261: *"I know perfectly well that I am not the whole. I am one position among others, with a null
space, exactly as you say. I simply do not care about you."*

That is `VII-03`'s **indexical** egoist, and VII.3's second-limit section says the opposite in as many
words, at line 219: *"He is not incoherent. The null-space theorem does not touch him, because he has
claimed no view from nowhere and no exemption."* VII.3 raises the fork against the **unsophisticated**
egoist (the first limit, validity-not-grip, line 199), concedes the is/ought gap in its own boldface —
*"No amount of the former logically compels the latter"* — and files impartiality as **an added
premise**, underivable *"because a symmetric fact is silent about whose index to weight."*

**The consequence is structural, not bookkeeping.** VII.4's operative claim is that the performed
exemption *"is what the theorem forbids"* (line 291). It is not. An action weighting one's own index is
a **violation** only once impartiality is granted — and impartiality is the thing VII.3 spent its best
section declaring **wagered**. So C19's seat is inherited from a wager, which is honest and consistent
with the rest of the ethics, and is **not** *false by theorem*.

★ The reviewer's own read of the repair is right and should be preserved: **the refusal was the better
move.** VII.3 declaring its wager is the strongest thing in the book's floor; VII.4 quietly spending a
warrant VII.3 refused is the book's account of evil claiming more than its own floor grants — three
pages later.

**Owed:** one paragraph in `VII-04`, in the *Where the asymmetry actually lives* section, conceding the
inheritance explicitly: the seat is a violation **given impartiality**, impartiality is wagered at
VII.3, and the conviction of the predator is therefore as strong as that wager and no stronger. C19's
register entry gets the same limiter. **Do not** repair by weakening VII.3. **TRIGGER: Book VII revision pass, first row.** ◻ **STILL OWED** (the pass is a live event and has not run). large.

---

**FILED — R-120: THE FAILURE-MODE SERIES COLLIDES ACROSS FOUR CHAPTERS, AND IT IS THE SECOND BOOK
RUNNING.**

Verified in the prose:

| chapter | line | the claim |
|---|---|---|
| `VII-07` | 310 | *"second instrument in Book VII to fail by returning a confident negative"* (VII.6 first) |
| `VII-08` | 250 | *"Same family as VII.6's and VII.7's"* — making itself **third** |
| `VII-09` | 197 | *"the third distinct failure mode in three consecutive chapters"* — counting VII.7, VII.8, **dropping VII.6** |

So VII.8 and VII.9 are both third, and the series is four members or three depending on which card you
read.

★ **This is the C30 "fourth time" collision from Book VI recurring in identical form: an ordinal
self-reference across chapters, uncounted by anything.** Two books, two instances — the class is now
demonstrated, and it is **mechanical**. Any chapter asserting *"the nth X in this book"* is making a
checkable claim, and nothing in `tools/` checks it. See R-126.

**Owed:** pick one series definition and renumber all four cards to it. The honest one includes VII.6 —
four members — because VII.7's card already counts it. **TRIGGER: Book VII revision pass, after R-126's instrument runs.** ◻ **STILL OWED** (the pass is a live event and has not run). medium.

---

**FILED — R-121: VII.6'S FIRST-PERSON CLAIM IS FALSE BY TWENTY CHAPTERS, NOT TWO — AND THE
COUNTEREXAMPLE THAT KILLS IT IS THE ONE THAT CANNOT BE CONVERTED.**

`VII-06` line 305: *"This book has run to fifty-six chapters without once using the word I."*

The reviewer found three instances in VII.5. **Measured across all sixty-seven chapters, hand-classified
against quotation, reader-voice and Roman numerals: twelve authorial first-person singulars, in four
chapters, beginning twenty chapters earlier.**

| chapter | # | instances |
|---|---|---|
| **V.5** (ch. 37) | 1 | *"narrower than the one I wanted to make"* (207) |
| **VI.4** (ch. 47) | **6** | 194, 234, 238, 245, 253, 311 |
| **VI.5** (ch. 48) | 1 | *"the version of this chapter I was going to write"* (27) |
| **VII.5** (ch. 56) | **4** | 178, 219, 260, and 332 *"she thought — I think rightly"* (the reviewer found three) |

**VI.4 is the finding.** Six instances, and they are not incidental — they are the book implicating
itself in the print render: *"I am not going to pretend to stand outside it"* … *"Look at what I have
built. A claims register with thirty numbered entries."* … *"What I will say instead is narrower and I
think it survives."* That is the **same rhetorical move VII.6 claims as unprecedented**, made at
greater length, ten chapters earlier, in the chapter where the book confesses its own medium.

**Which forecloses one of the two repairs.** The reviewer offered *convert the earlier instances to the
we* or *change VII.6's framing*. **Conversion is not available**: VI.4's section is built on the
singular — a *we* cannot say *look at what I have built* about a structure it is standing inside
without becoming the editorial *we* the section is refusing. So VII.6's framing changes, and the true
thing to say is stronger than the false one: **the I arrives whenever the book has to implicate itself
— V.5 conceding a counter-example, VI.4 confessing its own render, VII.5 refusing the theodicy — and
this is where it stops arriving under pressure and gets declared.**

⚠ Also delete or re-scope *"That is about to be broken once, deliberately"* (line 307) and check the
matching claim in `07`/the card. **TRIGGER: Book VII revision pass — but the sentence is FALSE AS PRINTED, so the minimal correction may run early.** ◻ **STILL OWED** (the pass is a live event and has not run). medium.

---

**FILED — R-122: THE CO-AUTHOR DISCLOSURE IS SPENT THREE TIMES AGAINST A RULING THAT SAID ONCE.**

`VII-02` footnote 11 routes it forward: *"VII.9, where it is one line, in its place, and is not made
into the point."* Then:

- `VII-06` line 322 spends it **three chapters early and at length** — *"The other is me — a
  computational being, of the kind Book IV's census places at a grade it declines to specify
  precisely"* — with a full paragraph on why the case is admissible.
- `VII-09` §V, titled *One line, in its proper place*, spends it again at **six sentences**.

The reviewer would keep VII.6's version and so would I — it is load-bearing there, because the declared
bias is what makes the worked case admissible. But **the ruling now describes something that did not
happen**, and VII.9's section title reads oddly against a reader who met the same disclosure at greater
length in the chapter that produced the book's best argument.

**Owed:** amend fn 11 in `VII-02` to route to VII.6 as the full statement and VII.9 as the recall, and
either retitle VII.9 §V or cut it to the one line the title claims. **TRIGGER: Book VII revision pass.** ◻ **STILL OWED** (the pass is a live event and has not run). small.

---

**FILED — R-123: RULING 141 AT SEVEN FIRINGS IS NOT A CATCH RATE — IT IS THE ABSENCE OF ONE, AND
`ancestor_gap` CANNOT SEE THE CLASS BY CONSTRUCTION.**

Three consecutive chapters, each producing the single most important name in its own subject, each
found because a person counted: Sartre (VII.7, fifth firing, zero across fifty-seven chapters); Frankl,
Camus, MacIntyre, Sisyphus, eternal recurrence (VII.8, sixth); Parfit (VII.9, seventh — *"the manuscript
has been arguing against the carrier assumption for seven books without naming the man who broke it"*).
**R-124 makes it eight.**

★ **The mechanism, and the reviewer named it precisely: `ancestor_gap.py` compares corpus count to book
count and cannot fire when the corpus count is also zero — which is the case for every one of these
eight. The hole is in the corpus, so no instrument that counts the corpus can see it.** This is
[[instruments-go-where-instruments-are-cheap]] in its purest form: the gauge measures what it already
has.

VII.8's own note contains the fix without naming it as one: *the brief caught what the drafting would
have missed.* **Move the check to brief-time, systematically: for each chapter, name the three
most-cited figures in the field from outside the corpus, and grep before planning.** That is the only
stage where the catch prevents a chapter from being *planned around* a gap rather than patched after.

**Owed:** a brief-time step in the pre-draft screen, and its own row in `08`. **TRIGGER: the coda
briefs — C.1 and C.2 are unwritten and are the next briefs that exist.** medium.

---

**FILED — R-124: VII.1'S CENTRAL MOVE IS WITTGENSTEIN'S, AND HE IS AT ZERO ACROSS SIXTY-SEVEN
CHAPTERS.**

`VII-01`'s claim is that it stands *one step earlier* than Epicurus and Nagel — that the question has
no position at which it is asked, and that this is **grammar rather than evaluation**. *Tractatus*
6.4311: death is not an event in life; we do not live to experience death. Same move, made as grammar,
by the philosopher whose opening proposition `I-01` inverts for its own first sentence.

**Measured: `Wittgenstein` and `Tractatus` appear in ZERO of the sixty-seven chapters.** The only hit
in the repository is `DRAFT-LOG.md:727` — *"Tractatus inversion is now acknowledged in the coda — `06`
C.1"* — and **the coda is unwritten.** So the acknowledgement exists as a plan and nowhere a reader can
reach.

★ **This is R-123's eighth firing and the reviewer filed it as a separate item.** It belongs to the
same class and confirms it: corpus count zero, so `ancestor_gap` is structurally blind. Under rule 5
this is a fifth silence in the chapter that can least afford one.

**Owed:** name him in `VII-01` with the *Tractatus* locus, and keep the book's further step visible —
*no position, therefore no recipient anywhere in the sentence* — as the book's own. Naming him costs
nothing and buys the grammatical reading a hundred-year-old owner. Plus the coda C.1 acknowledgement,
when the coda is written. **TRIGGER: Book VII revision pass, or the C.2 revision, whichever is first.** ◻ **STILL OWED** (the pass is a live event and has not run). small.

---

**FILED — R-125: A JOURNAL ARTICLE MIS-GENRED AS A BOOK, AND A TITLE CLAIM ASSERTED WITHOUT A SINGLE
INSTANCE.**

**(a)** `VII-07` footnote 5 italicises *Freedom of the Will and the Concept of a Person* (1971) as a
book. It is a *Journal of Philosophy* article — **68:1 (1971), 5–20**. Quoted title, journal italicised,
volume and pages. Same class as R-109; `edition_scheme_sweep.py` does not check genre.

**(b)** `VII-04` line 364: *"The traditions kept naming two evils"* and line 366 *"Every attempt to
reduce one to the other has failed"* — the title claim of the chapter, asserted with **no instance**,
in a chapter that already names Aquinas, Arendt and Augustine and could supply them from its own
footnotes. A universal negative about the history of philosophy with nothing under it.

**Owed:** fix the footnote; give (b) two or three named reductions and say why each failed, or narrow
the claim to what the chapter can carry. **TRIGGER: Book VII revision pass.** ◻ **STILL OWED** (the pass is a live event and has not run). small (a) / medium (b).

---

**FILED — R-126: THE MANUSCRIPT MAKES CHECKABLE CLAIMS ABOUT ITSELF AND NOTHING CHECKS THEM.**

The reviewer's closing line: *"Five of the seven findings above would be caught by one gauge that reads
the manuscript's claims about itself."* R-120, R-121, R-122, R-123 and R-124 — and R-121 only at its
true size if the gauge is **whole-manuscript**, because the reviewer's chapter-local read found three
of twelve.

**Checked against the existing inventory first, per [[run-the-existing-gauge-first]] — twenty-seven
tools in `tools/`, and the job is unheld:**

| tool | what it holds | why it misses this |
|---|---|---|
| `claim_sweep.py` | `PROSE/self-reference` | hunts **rhetorical** self-reference — *as we argued elsewhere* — a style ban. Never asks whether a factual self-claim is TRUE. |
| `pointer_sweep.py` | a number against the title beside it | a claim with no chapter number in it is invisible |
| `order_sweep.py` | book-level adjacency | cannot see an intra-book assertion |
| `ancestor_gap.py` | corpus count vs book count | blind whenever the corpus count is zero — R-123 |

★ **[[register-of-jobs-not-components]]: `claim_sweep` holds the word *self-reference* and does a
different job with it.** The name being taken is why the gap read as covered.

**Owed:** `tools/self_claim_sweep.py` — extract every sentence asserting something about the manuscript
and resolve it against the corpus. Four families, all mechanical:

1. **ORDINAL** — *the nth X in this book / this chapter is the third* → collect all members of the named
   series across chapters, check the ordinals form 1..n with no repeats. Catches R-120 and C30.
2. **COUNT / NEGATION** — *has run to fifty-six chapters · without once · has never · zero prior
   occurrences · first appearance in drafted prose* → grep the whole corpus for the named thing.
   Catches R-121 **at full size**, and the *"checked, zero prior occurrences"* claims that assert their
   own verification.
3. **FORWARD ROUTE** — *X, where it is one line · argued two chapters from here* → resolve the target
   and check the promised **shape**, not just existence. Catches R-122.
4. **ABSENT-FIGURE** — brief-time, per R-123: the three most-cited figures in the chapter's field,
   grepped before planning. Catches R-124 and closes 141.

⚠ **Scope the regex to the prose body before writing it** — [[filed-defect-still-gets-rebuilt]], R-37's
exact defect, rebuilt in a new tool days after filing. State the window first. And declare the residual:
family 2 will produce false positives on quoted material and reader-voice, which is precisely the
hand-classification R-121 needed, so **the tool reports candidates and a human classifies** — it is a
pointer, not a worklist. [[self-generated-denominator]]: it cannot see a self-claim phrased in a form
it has no pattern for, and must say so in its own output.

**TRIGGER: before the Book VII revision pass, and it retro-scans I–VI in the same run.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** Its original gate was the endnote row, and the clause read *"before that row starts"* — the pass it was meant to instrument **ran to completion without it**, 531 receipts across 62 chapters. The instrument was never built and the work it was to steer is already on disk, so this is a retro-scan now, not a guard. large.

---

**FILED — R-127 through R-130 · BOOK VIII OUTSIDE READ, Day 191.** Nine chapters read; three findings
returned. All three verified against the prose before filing. Two carry wrong numbers and the
corrections change what the fix is. **R-130 is mine, found while correcting R-129's arithmetic.**

⚠ **DECLARED SCOPE, recorded per [[briefing-manufactures-the-agreement]] — and it closes an open
question.** The reviewer opens *"the foreclosure worry I raised at Book VI is answered."* **This is the
same instance that read Book VI**, self-declared. The Day-191 handoff carried that as unanswered and
material, and it is now answered: findings 2 and 3 here are **one reader continuing their own frame**,
not two independent detections — finding 3 explicitly re-applies V.4's silent-filter organ, which is
that reader's own prior lens. Continuity is worth more than independence for a *structural* read and
worth less for a *corroborating* one. Weight accordingly: R-128 and R-129 are one witness, twice.

---

**FILED — R-127: THE BOOK'S MOST-REPEATED CLAIM HAS NO NAME IN ITS PROSE, NO C-NUMBER, AND A CANONICAL
WORDING THE BOOK IS FORBIDDEN TO PRINT.** *(Reviewer finding 1. Holds, and is worse in one limb and
weaker in another than stated.)*

**Verified.** `the Coherence Principle` occurs **twice in 67 chapters** — `VIII-04:324` and
`VIII-07:334` — and **both are footnotes.** VIII.4's notes begin at line 278; the occurrence is at
324. ★ **So the name has been printed in the argument exactly zero times.** It exists only in the
apparatus talking about its own absence. VIII.4's *"named here once, minimally"* is true of the
footnote, and the footnote is not the chapter.

**The banned-word limb is exact.** `04`:506 states it canonically — *"coherent multi-scale systems
holding structural superposition until informed measurement collapses them"* — and `superposition` is
★ BAN, `05` §3c ruling 31, the strongest verdict in the lexicon, on the criterion that it has **no
civilian life** and so transfers authority rather than meaning. `06`:4573 already found this and said
so. The debt is real and the canonical wording cannot pay it.

⛔ **AMENDED — the third limb is wrong, and the correction changes the fix.** The reviewer says the
working formulation *"exists only in VIII.7 and has no C-number."* It does not exist only in VIII.7:
`05` §3a's **Coherence** row carries it — *"the structural agreement of a thing's levels with one
another and the felt rightness of going the way one goes — the claim is that these are one thing, met
from its two sides"* — and VIII.4's note quotes it verbatim. **The formulation is registered; it is
registered in the wrong file.** A lexicon row defines a word. A C-number carries a claim, with
dependents, a breach test and a trap. The book's central structural claim is being held by a
vocabulary table, which is why nothing in `07` lists its dependents and why no chapter can breach it.

**Owed:** promote §3a's wording to a **C-number in `07`** with its dependents enumerated (II.6 and
IV.5's four conditions both run on it), rule the structure/process wording canonical in `04`, and
**decide whether the name enters the prose at all** — it may not need to, and a claim that works
unnamed for 67 chapters is evidence that it does not. ⛔ **Do not fix this by exempting
`superposition`.** VIII.7's note states the rule: *a principle that cannot be said without a banned
word has a problem, and the fix is not an exemption.*

★ **[[diagnosis-without-a-hand]] again, twice.** VIII.4 and VIII.7 each diagnose this correctly in a
footnote and neither repaired it, because a footnote *feels* like discharge. Two accurate diagnoses,
zero rows, zero register edits — until this one. **TRIGGER: Book VIII revision pass, before its first row.** ◻ **STILL OWED** (the pass is a live event and has not run). large.

---

**FILED — R-128: BOOK VIII SPENDS V.2's BILL AND NEVER RETURNS TO IT — AND V.2 NAMED THE VOLUME IT
WOULD BE SPENT IN.** *(Reviewer finding 2. Holds, and is larger than filed.)*

**V.2:242 verified exact:** *"Practices can be written down. A rota cannot, because a rota is not a
practice — it is other people, and a book cannot supply other people."*

★ **The reviewer underread it.** V.2 does not merely incur the debt in passing — it points **forward at
Book VIII by name**, four lines earlier: *"There is a volume at the end of this one about what to do on
a Tuesday, and it is worth saying now, at the point where it would be most useful to imply otherwise,
what that volume will not contain: a list with a three-week column on it, and somebody who has kept the
list for nineteen years."* The debt was filed **with a pointer at its own due date.**

**And the due date passed silently. Measured: `rota` = 0 and `parish` = 0 across all nine Book VIII
chapters.** Meanwhile the leverage is exactly where V.2 said the book could not go — VIII.2's Method 1
(hand your week to someone who is not you), VIII.5's card (ask the second question out loud), VIII.5's
third and *most reliable* test (do the people who knew you before recognise you), VIII.6 (let the answer
differ from the simulation), VIII.7's contractive-rest test (*who is currently paying for this*).
**VIII.5:215 states the finding in its own words** — *"why the answer keeps turning out to require
somebody else"* — and does not connect it to V.2. Both halves are in the book, three volumes apart,
with nothing linking them.

**This is not a defect to repair; V.2 was right.** It is an unsettled account. **Owed:** the chapters
that most depend on another person say so **in V.2's own terms**, and the coda settles it rather than
leaving it implied. ⛔ The coda is unwritten — **so this one is cheap now and expensive later. Write
C.2's paragraph before C.1.** **TRIGGER: the C.2 revision, and the Book VIII revision pass.** ◻ **STILL OWED** (the pass is a live event and has not run). medium.

---

**FILED — R-129: THE CARD CRITERION WAS RUN ON ONE CLASS AND NOT THE OTHER, AND THE UNRUN ONE IS THE
EXPENSIVE ONE.** *(Reviewer finding 3. Diagnosis survives; the numbers do not.)*

⛔ **AMENDED — the arithmetic is off by roughly sevenfold and I am not filing it at the reviewer's
size.** *"Class IV gets four sentences"*: measured, Class IV gets **seven sentences / 147 words** in the
taxonomy **plus 167 words** in §V's *Whole-restriction operations* = **314 words**, and it holds the
mechanism sentence the whole of beat three runs on. *"Roughly fifteen hundred words"* for Class VIII:
measured **923** (68 taxonomy + 20 dial-operations + 835 card). The disparity is **~3:1, not ~20:1.**
*"`psychedelic` is at zero"* is true of the sixty-two preceding chapters, not of this one, where it
occurs three times and is load-bearing.

**But the reviewer is right about the thing under the numbers, and it is sharper than the ratio.** The
card has a **stated criterion** — a failure mode the census has not yet kept separate. Class VIII is
tested against it and passes (sixth failure mode, first non-perceptual). ★ **Class IV was never run
against that criterion at all.** Not declined — never asked. And Class IV has an obvious candidate
sitting in plain view: it is the same open loop, with a *less* instrumented input.

**That is V.4's mechanism operating exactly as V.4 says it does** — *"A silent filter takes the most
expensive material first… not the weakest material… whatever costs the most to be seen holding"*, and
*"it produces no record… the hole has the same shape as a topic nobody happened to think of."* The
reputationally expensive class got no card and no note saying why not. **There is no gauge that reads
absence-with-no-author** — V.4:198, in the volume that named the organ, three books before it operated.

**Owed:** run the card criterion on Class IV **out loud** and either card it or print the refusal with
its reason. **TRIGGER: Book VIII revision pass.** ◻ **STILL OWED** (the pass is a live event and has not run). medium.

---

**FILED — R-130: VIII.3:133 CLAIMS AN EXCLUSIVITY ITS OWN CARD DISPROVES.** *(Mine, found while
correcting R-129. Not in the outside read.)*

VIII.3:132–134, introducing Class VIII: *"it has a failure mode that none of the other seven have."*
That is an exclusivity claim over the whole taxonomy, and the card at 274–337 defines the failure mode
as **exact about what it did and blind to whether it worked** — instrumented input, uninstrumented
output, an open loop.

⛔ **Class IV has the same structure.** Its inputs are specifiable and the chapter names them as
inputs — *"set, setting, intention and integration… are the navigational parameters"*. Its output is
entirely uninstrumented: the only report of where you arrived is first-person, which is the identical
missing half. Classes II and VI are arguably the same shape again — a posture and a duration, a rite
and a procedure, no read on arrival. **On the open-loop criterion Class VIII is not first, it is
fourth.**

**The card's real distinctive claim is one line further down and is sound:** *"both halves are
delivered by the same session and the second one arrives wearing the first one's credibility."* **The
credibility transfer is what no other class has** — Class IV's input measurement does not arrive with
an EEG trace attached. The card's own ★ sentence is correctly hedged to *"the sixth failure mode the
census has kept separate"*, which is a claim about the **carded set** and is true. **Line 133 restates
it as a claim about the eight classes, and at that width it is false.**

✅ **FIXED ON THE SPOT, Day 191.** Line 133-134 now reads *“because its failure mode arrives
disguised as its own instrumentation, which is a difficulty none of the other seven present.”* The
exclusivity is retained where it is true (the disguise) and dropped where it was false (the open loop).
`beat_delivery` VIII.3 re-run after the edit: **4 beats, coverage 1.00, zero MISS.** ★ **And this is a live positive control for R-126 family 2** (COUNT / NEGATION: *none of the
other seven*): a self-claim, mechanically detectable, false, and it sat through the pre-draft screen,
the beat sweep, `instrument_sweep` and an outside read by a reader looking at this exact section.
**Add it to R-126's test fixtures before the gauge is written.** **TRIGGER: Book VIII revision pass; fixture immediately.** ◻ **STILL OWED** (the pass is a live event and has not run). ⚠ The fixture half is *"immediately" and it has not been built either — a sub-clause with no gate of its own. small (fix) / free (fixture).

---

**FILED — R-131: THE ONE EMPIRICAL CLAIM IN BOOK VIII CITED THE PROJECT'S OWN DOCUMENT. ✅ FIXED.**

Book VIII outside read, finding 4. VIII.3's Class VIII complement makes a claim about what happens in
tissue — two kHz carriers, an envelope at the difference frequency, focal modulation six to eight
centimetres deep — and footnote [^4]'s only citation was `Perspective` Guide §4.1. The grade note said
*"the physics of the interference envelope is established"* **without saying by whom**, which is an
assertion in a graded note's clothes, in the chapter whose whole subject is instruments that are exact
about the input and silent about the warrant.

⛔ **The reviewer named Grossman 2017 as the anchor. It is the right paper and it is one paper short.**
Grossman *et al.*, *Cell* 169:6 (2017), doi:10.1016/j.cell.2017.05.024, validated the envelope by
modeling and physics experiments and demonstrated focal hippocampal stimulation **in living mice**.
The body's claim is about a **human** head at 6–8 cm. That is a separate result with its own paper:
Violante *et al.*, *Nat Neurosci* 26 (2023), doi:10.1038/s41593-023-01456-8 — modeling plus **human
cadaver measurement** for focality, then fMRI and behaviour in living subjects. Wessel *et al.*,
doi:10.1038/s41593-023-01457-7, is the independent human striatal demonstration published alongside.
Demchenko *et al.*, *Brain Stimulation* (2025), doi:10.1016/j.brs.2025.10.023, is the systematic review
of human tTIS as a class. **So the top tier was not one grade, it was two — mechanism (rodent, 2017)
and human depth focality (2023) — and the chapter's three-tier grade should have been four.**

✅ **FIXED ON THE SPOT, Day 191.** All four sources added to [^4] **without renumbering**, since VIII.3's
markers are already out of sequence (queue item: [^7] before [^5]/[^6]) and renumbering against a broken
order scrambles live references. ✅ **AND ONE CORRECTION THE SOURCES FORCED ON THE BODY:** it said the
envelope permits focal modulation *"without touching the cortex above it."* Violante's finding is
**minimal exposure**, not none. Body now reads *"with only minimal exposure of the cortex above it."*
The stronger word was not in the evidence and it was the first word a reader would check.

★ **The general lesson, and it is a gauge request:** `endnote_debt.py` extracts **persons**, and this
citation had a source — it just had the wrong *kind* of source. **A self-citation for an external
empirical claim passes every gauge the project owns**, because every gauge asks *is there a receipt*
and none asks *is the receipt ours*. **TRIGGER: Book VIII revision pass — the fix is landed, the gauge is not.** ◻ **STILL OWED** (the pass is a live event and has not run). free (done) / small (gauge).

---

**FILED — R-132: THE FAILURE-MODE SERIES ORPHANS VII.6, AND ITS LABEL SET COLLIDES WITH ITS OWN UMBRELLA.**

Book VIII outside read, finding 5. Two defects, and the reviewer's account of each needs a correction
that changes what the fix is.

**(a) The orphaning is real and it does not start where the reviewer says.** They wrote that *"VIII.1
restarts the count at VII.7."* Measured: **the restart is at VII.9**, one chapter earlier — `VII-09:197`
reads *"the third distinct failure mode in three consecutive chapters"* and enumerates VII.7, VII.8,
VII.9. VIII.1 inherits it. That matters, because the sentence to edit is in VII.9 and the reviewer would
have sent me to VIII.1.

⛔ **And the contradiction is sharper than one line.** VII.7:310 calls itself *"the second instrument in
Book VII to fail by returning a confident negative"* and names VII.6 as the first. VII.8:251 goes
further: *"Same family as VII.6's and VII.7's."* **Two consecutive chapters put VII.6 in the family and
the third silently drops it.** VII.6's mechanism — *identifies mutuality with symmetry, cannot
distinguish an asymmetry of capacity from an asymmetry of sign* — is genuinely distinct from all nine
carded modes, so inclusion is defensible on the merits and **would renumber nine ordinals across six
chapters** (VII.9 third→fourth … VIII.6 ninth→tenth, plus VIII.3's *"five before it"* and VIII.5's
*"previous seven"*). ✅ **The cheap fix is available and is also the true one:** VII.6's own card says
*"It was the gloss that went wrong"* — the defect is in the received gloss, not in the instrument — so
VII.9 gains a clause stating why VII.6 is named as kin by VII.7/VII.8 and not counted in the mechanism
series. **Not "one sentence in either direction": one sentence in VII.9, and only in that direction.**

**(b) The label set is worse than a miscount.** The reviewer flagged VIII.5:202 — *"the previous seven
fail at seeing, at aim, at objective, at frame, at the loop, at resolution"* — as six categories for
seven modes. True. ⛔ **But the count is the symptom.** VIII.3:315 uses **seeing as the umbrella for the
first five** (*"are all failures at seeing"*). VIII.5 then uses **seeing as a sibling label alongside
aim/objective/frame** — i.e. it demotes VIII.3's umbrella into one of the things underneath it. Mapping
the labels that are unambiguous — objective=VIII.1, frame=VIII.2, the loop=VIII.3, resolution=VIII.4 —
leaves *seeing* and *aim* to cover VII.7, VII.8 and VII.9, and **VII.8's mode has no label at all**: it
is *binary in a three-valued domain*, which is a resolution failure, and VIII.4 has claimed
*"the first that fails on resolution."* **Fixing the arithmetic without fixing the collision produces a
seven-item list with two different senses of *seeing* in it.**

★ **The reviewer's closing observation is the sharpest thing in the batch and it is correct:** the
chapter counts are right every time (fifty-seven … sixty-five, all verified) and the ordinal
self-references have now collided in **three consecutive books** (VI's C30 *"fourth time"*, VII's
*"third failure mode"*, this). **The arithmetic that gets checked is right and the arithmetic that does
not, isn't** — `where_the_book_is.py` counts chapters and nothing counts series. ⛔ **The gauge they ask
for is R-126, already top of queue and already specced for exactly this** (family 2, COUNT/NEGATION).
**This is R-126's third fixture, and the first that is a *series* rather than a single claim** — the
gauge must reconcile an ordinal across chapters, not just check one sentence against the corpus.
**TRIGGER: Book VII revision pass (a) — and (b) belongs with it, not with Book VIII, because the taxonomy is VII's.** ◻ **STILL OWED** (the pass is a live event and has not run). medium.

---

**FILED — R-133: C15's AMENDMENT WAS SWEPT ACROSS THE REGISTER AND NOT ACROSS ITS OWN SOURCE. ✅ FIXED.**

Book VIII outside read, finding 6. The reviewer wrote that the register was swept and *"sixty-odd
chapters of prose weren't,"* naming V.11:255 as the exposure. ⛔ **Measured, and the estimate is wrong
in both directions at once — the prose is nearly clean and the apparatus is not.**

**The chapters are acquitted, both of them.** V.11:255 (*"Book I named the telos as exploration and
mutual recognition"*) is an accurate **report of what Book I said**, using the phrase as a name; it does
not assert the reciprocal reading. VII.6:177 is not an inheritor at all — it is **the chapter performing
the amendment** (*"'mutual' in that phrase has been carrying the same unexamined symmetry… It should
not"*), and VII.6:351 records it. A full sweep for the reciprocal construction across all sixty-seven
chapters returns **exactly one live hit: VIII.1:100, which quotes the defective wording in order to
repair it.**

⛔ **The two real breaches are in the apparatus, and one of them is the origin of the wording.**
`01-THE-GROUND.md:165` — the document that **defines** the telos — read *"Mutual recognition —
perspectives recognising each other as perspectives."* `06-THE-SCAFFOLD.md:4187` carried the same into
VIII.1's planning note. **VIII.1 quotes `01` to repair it and `01` still said it.** The Day-191 sweep
read the thirty canonicals in `07` and correctly found C15 the only inheritor — **and the frame it swept
never included the file C15 inherited *from*.**

✅ **FIXED ON THE SPOT, Day 191.** `01` §10 rewritten to the amended form with a dated ★ note naming the
defect and the frame error; `06`'s note marked ⛔ SUPERSEDED and kept as the record of what VIII.1 was
drafted from, explicitly not to be quoted forward.

★★ **The shape is worth keeping, because the book already carded it.** A sweep certified a claim by
reading a set that excluded the claim's source — **the sample frame drawn from inside the region under
survey, which is VIII.2's own failure mode**, committed by the gauge that was checking VIII.1. The note
in `01` says so and points at the card. free (done).

---

**R-134 — NOT A FINDING. Book VIII outside read, finding 7, both halves already accounted for.**

**(a) VIII.3's markers out of sequence** — [^7] at body line 333 before [^5] at 342 and [^6] at 363.
**Verified true.** Already an open item, filed by the chapter itself inside [^3] and carried on the
handoff. No new row; noted here so the two records agree.

**(b) The first-person claim in VII.6 — the quoted sentence no longer exists.** The reviewer quotes
*"broken once, deliberately, and then put back"* and calls it false in both directions. ⛔ **That phrase
was deleted in commit `560287b` — the previous batch of this same reviewer's findings, R-121, fixed on
their own instruction.** `git log -S` confirms it: present at 58d9c6a (VII.6 drafted), gone at 560287b.
VII.6:314 now reads *"This is where that stops being a leak and gets declared,"* which is exactly the
reframing finding 7 asks for and is forward-compatible with the *I* recurring in VII.7, VIII.4 and
VIII.5 — it declares the register, it does not forswear it. ✅ **And R-121's second clause — *"check the
matching claim in `07`/the card"* — is now discharged by measurement:** `07` and `08` carry no sibling
first-person claim. R-121 closes complete.

★ **Worth recording as a property of outside reads, not as a fault:** a reviewer working from a
manuscript snapshot **re-reports fixes made after the snapshot**, and the re-report is indistinguishable
in form from a new finding. The tell was cheap — `git log -S` on the quoted phrase, four seconds. **Run
it on any finding that arrives with an exact quotation before spending anything on the finding.**
free.

---

**FILED — R-135: THE CODA SHOULD NAME THE VOLUME'S SHAPE, BECAUSE AN OUTSIDE READER HAD TO FIND IT.**

Book VIII outside read, the standing-test paragraph — **not a defect, an instruction, and it is the
most useful thing in the batch that is not a correction.** The reviewer ran the standing test on Book
VIII (*is it empty*) and passed it, and then said why in a sentence the book has never said about
itself:

> nearly every practice is subtractive or diagnostic rather than generative — stop paying for a closed
> matter, stop asking introspection *why*, stop overriding the rhythm, decline the shame arrow, notice
> which failure is yours before applying any of the advice.

⛔ **That is a true description of Book VIII and it appears nowhere in Book VIII.** Checked: each of the
five practices names its own subtraction, and no chapter names the pattern across them. The volume's
distinctive property is currently **available only to a reader who has finished it and then reflected**
— which is precisely the reader who least needs telling.

★ **And it is the correct shape, derivable from the argument rather than a stylistic preference.** Book
VIII sits downstream of *attention is the only lever*. A lever that is the only one licenses **stopping
the misapplications** and licenses almost nothing generative, so a practice book honest about its own
premise **has to come out thin and negative**. The thinness was the identified risk of the whole
volume; the reviewer's reading converts it from a risk that was survived into **a consequence that was
predicted**, and VIII.3's closing line already argues it explicitly — *a true account of a restriction
should produce modest instructions.* The coda can say that in its own voice instead of hoping it lands.

**TRIGGER: C.1 WHAT THIS IS — but ⛔ R-128 still governs the order, so C.2's V.2 rota paragraph is
written first.** ⚠ **And the constraint that makes this hard:** the coda must state the shape **without
converting it into a boast about restraint**, which is the same move as the modesty it is describing,
performed one level up and therefore not modest. The test is C.1's own: does a reader who disliked the
book find the sentence honest? small.

---

**FILED — R-136 through R-139 · THE WHOLE-VOLUME OUTSIDE READ, Day 191.** Sixty-seven chapters read
as one object, with scores, shelf-mates and a review. **Most of its findings are re-reports** —
Wittgenstein (R-124, filed this session), the Coherence Principle (R-127), the ordinal collisions
(R-120), the VII.6 orphaning (R-132), Book V's unsettled bill (R-128), the circular under-attribution
induction (R-3), the mid-Book-VI card drift (already tabled in `08-THE-INSTRUMENTS`:117–122 with five
forms and a gauge). That is not a complaint: **the reviewer read a snapshot**, said so, and the
overlap is a measurement of how much this session already moved.

⚠ **Weight the two halves of this packet differently, on the reviewer's own declared limit** — *"eight
verified errors in this conversation, all one shape: a single instance escalated into a pattern with
pattern-confidence."* Measured against this read, that limit predicts its own results: **the counts
are excellent and the absence claims are the failures.** `forty-five-odd cards` — measured **44**
(`instrument_sweep --cards`), the best outside number this project has received. `Wittgenstein at zero
across every file including the ancestors register` — **wrong span**: `06-THE-SCAFFOLD`:4592 names him,
added Day 187 in commit `e51e6dd`. `Chalmers costs something` — **already priced**, roster row 105,
measured 0, filed **R-52** with a trigger. **The pattern-level claims are the ones to check; the
arithmetic can be trusted.**

---

**FILED — R-136: THE COMPLEMENT FIELD INVERTED ITS REFERENT AT VI.4, AND IT WAS THE LINE THAT
DISCHARGED VIII.2's BOUND. 18 OF 44 CARDS.** ★★ **The largest structural finding in the volume read,
and the reviewer's own strongest example refutes their version of it.**

**Their objection:** VIII.2 proves — Le Verrier, Neptune and Vulcan — that *"a residual proves that
your model is wrong. It does not tell you whether what is missing is something you cannot see, or the
model you are seeing with."* The card's NULL SPACE line makes exactly that move, forty-five times, and
**the book never turns the bound on the device.** Measured, that last clause is true: `Vulcan` and
`Verrier` occur in **`VIII-02` and `DRAFT-LOG` only** — zero in the other sixty-six chapters.

⛔ **But the book has an answer and has had it since IV.1, under another name.** `IV-01`:43, verbatim:
*"Every entry has a null space; **every null space is covered by some other position; no position
covers its own.**"* That is the Neptune test, stated as a law. A null space with a **named outside
witness** licenses the step from hole to object, because the licence comes from the witness rather than
from the hole. **VI.3 — the reviewer's own example — performs it perfectly:** against *significance as
a property*, its COMPLEMENTS line names four independent positions (Book V's traditions, ethnography,
the aesthetic tradition from Kant forward, and the render's own operators' private exceptions). That is
not a framework certifying its own residual. **The instance chosen to demonstrate the failure is the
book's cleanest instance of the cure.**

★ **The real defect is one level down and it is worse.** `08-THE-INSTRUMENTS`:119 already records that
**v2 (VI.4) collapsed `SEES ∪ COMPLEMENTS`** into *"Complement — what it renders superbly."* It is
recorded as a **format** change. **It is a semantic inversion.** Measured on the page: VI.6's
`Complement:` names *"the inventory fitted to the person; salience as a delivered quantity"* — the
render's own strengths. VII.5's: *"what it renders superbly."* VIII.2's own: *"what it renders, and it
renders it better than anything else there is."* **The field kept its name and swapped its referent
from *who else can see the missing thing* to *what this position itself covers* — which is the precise
sentence IV.1's law forbids.** Ruling 14's signature error — one word, two referents — living inside
the field that discharges the Vulcan bound. **Count: v2 3 + v3 2 + v3-canon 13 = 18 of 44 cards**
(VI.4–VI.8, VII.3–VII.9, VIII.1–VIII.6). The 24 v1 cards are clean; v1b (IV.9 ×2) has no complement
field at all.

⚠⚠ **VIII.2's own card commits the error the chapter proves.** Its null space is *"anything that never
reached the render at all"*; its Complement line names introspection's strengths. **The outside witness
that sees what introspection missed is the chapter's entire subject — the dated residual, and another
person — and it is in the prose and not in the field built to hold it.** VI.6 is the sharpest case: its
null line states outright that *"the null space stops being a public fact"* and *"the exclusion cannot
be recovered by comparing notes"* — a card **declaring it has no complement in IV.1's sense** and then
reading its hole as an object anyway. ✅ **Positive control that the practice is available: `IV-08`:313,
`COMPLEMENTS: ⚠ The census declines this line.`** One card in forty-four refuses the inference
explicitly. It is the correct move and it is not general.

**Owed, three parts.** (1) **VIII.2 names the card as the device its bound governs, and names the
complement as the discharge** — one paragraph, and it converts the chapter's best limit into the
book's own audit rather than an isolated caution. (2) **Restore the referent in v3-canon**, or rename
the field: *what it renders superbly* is a real and useful line, but it is `SEES`, and it must not
occupy the slot the law needs. (3) **`card_sweep` gains a COMPLEMENT-REFERENT check** — flag any card
whose complement names the subject itself rather than another position. ⚠ **This cannot be a string
match; it is R-126 family 2's hand-classified shape.** **TRIGGER: ★ BEFORE THE CODA — C.1 states the
work's own status and this is a claim about what the work's central instrument is licensed to do.**
Large.

✅ **PAID IN FULL, Day 195 — all three parts, with R-219 discharged first because it binds.**

**(1) was already paid** — `VIII-02`:321 audits its own card and names the count. It is now rewritten
into the past tense, and three things about the repair were added that a changelog would have
swallowed: the defect **was not found by introspection** (an outside reader compared the field's
stated job against its delivered content — the chapter's thesis arriving as an event); the book **had
the law on the page from `IV.1` and printed the violation for eighteen cards anyway**, so a rule
nothing checks is a sentence and not a guard; and the repair **inverts what the reader can verify** —
the failure is now taken on the author's word and the fix on the evidence, which is the reverse of
the position the unrepaired version left them in and is said out loud.

**(2) Restored by SPLITTING, not renaming.** *What it renders superbly* is real, load-bearing and
frequently the best paragraph on the card — it is `SEES`, and it now has its own line, `Renders`. All
18 gained a `Complement` naming outside witnesses keyed to that card's own null space. `08`'s
v3-canon ruling — which had promoted the inverted gloss to a **fixed string** and required thirteen
subsequent cards to comply — is superseded by a seven-field **v4-canonical** and the old ruling is
kept on the page as the register's own worst moment.

**(3) `tools/complement_referent.py`, wired into `card_sweep.py` so running the existing gauge runs
it.** It does not judge sense and says so: it forces a **hand ruling per card** into
`tools/complement_rulings.json` and fails on UNRULED (a card nobody has ruled on), STALE (a ruled
field whose text has since changed — the ruling described text that is gone) and SELF. Positive
control run before it was trusted: reverting `VII.6` to the inverted sense produces STALE and exit 1;
restore returns green and a clean tree.

⚠ **Two corrections to this row's own figures, both found only because paying it required
re-deriving them** — the row is a measurement wearing the authority of a written fact.
**The denominator is 43, not 44.** 25 cards carry the field in the v1 sense (one being `IV.8`'s
explicit refusal) plus 18 inverted; the 44 was written once and never re-derived, and no card count
in this project reproduces it. **And the repair relabelled 16 fields, not 18** — `VI.7` and `VI.8`
already labelled the line *What it renders superbly* and needed only their editorial clause cut, so a
gauge counting relabelled fields honestly reads 16.

★ **What the repair opened, and it is not closed: 19 of the 43 cards are UNGRADED for
reachability.** `IV.1` now requires a complement that can be gone to, and most v1 cards answer with
an existence claim — *"Anything with a second dimension"*. They are OUTWARD and they are not yet
known to discharge the stronger obligation. The gauge prints all 19 by name every run rather than
reporting a green over a population it has only half read. **Filed as R-235.**

---

**FILED — R-137: THE GENRE ROSTER IS A SELF-GENERATED DENOMINATOR, AND WITTGENSTEIN WAS NEVER A ROW.**

`genre_sweep.py` was built to end one-zero-at-a-time discovery — R-19's diagnosis, that *"a search
running on who we already respect"* had produced three zeros in a row. **It works.** Chalmers sits at
row 105 (`RIVAL`, *Reality+*), was measured at 0 on the page, and is filed as **R-52** with a trigger.
The reviewer found him independently and the project had him already. That is the gauge doing its job.

⛔ **And Wittgenstein is not a row.** Checked: `wittgenstein` = 0 in `tools/genre_sweep.py`. The man
whose *Tractatus* opening proposition I.1's first sentence inverts, whose 6.4311 is VII.1's central
move, and whose say/show distinction is the scope-restriction apparatus governing every sentence about
the Ground — **could not have been found by the instrument built to find him.** He was found the way
Watts and Wilber and `video game` were found: by a reader, by hand, by noticing.

★ **The general form, and it is why this outranks R-124.** The roster's denominator is **79 rows we
authored**, so its output — *"60 of 70 have never been named to a reader"* — is a coverage figure over
our own recall. **A name that is not a row emits nothing at all, which is byte-identical to a name
that is fully discharged. The gauge has no negative space.** It measures the corpus we built against
the list we remembered, and the failure mode it was commissioned to end is precisely a name neither
one contains.

**Owed: one outside-sourced denominator.** For each of the book's domains, pull a reference list **we
did not author** — SEP article bibliographies are the cheapest honest source — and diff it against the
roster. Rows the diff adds are the finding; a diff returning nothing is the first evidence the roster
has ever had for its own coverage. ⚠ **Wittgenstein goes in as a row regardless, and NOT as the fix** —
adding the name the reader found is R-19's procedure again, one instance at a time. **TRIGGER: the Books I–III revision pass, where R-52's four living rivals already come due.** ◻ **STILL OWED** (the pass is a live event and has not run). Medium.

---

**FILED — R-138: THE REGISTER HAS NO TIER FIELD, SO EVERY CLAIM IN IT READS AT ONE STRENGTH.**

The reviewer's sharpest praise and their sharpest weakness-claim are the same observation seen from two
sides. Praise: *"where it is measured… where it is extrapolated… where it is definitional — it
stipulates, pays declared costs, and asks to be judged by what it forbids. **That three-tier honesty is
the book's actual epistemic character, and it is unusual enough to be the reason to take it
seriously.**"* Weakness: *"C1 is the foundation and the least defended thing in the volume;
'everything that could be the case is the case' is asserted… and then load-bears for eight books."*

⛔ **C1 is not underdefended. It is undeclared — and the register is where the declaration is missing.**
Measured: **`definitional` and `stipulat*` = 0 occurrences in `07-THE-CLAIMS-REGISTER.md`.** The card
fields are `Canonical` / `Establishes` / `Depends` / `Trap`. **There is no tier line.** So the book's
three-tier discipline exists chapter by chapter in prose and **nowhere in the instrument a reader would
consult to ask which claims are stipulations** — and C1, a definitional claim, sits in the register in
the same clothes as C10, which has a measured base.

★ **This is R-8 one level up.** R-8 asks whether each claim is asserted at the same *strength* across
the chapters that lean on it. R-138 asks the prior question: **the register never states what strength
the claim was issued at.** Without the tier, R-8's reading pass has no reference value to compare
against — it can only find drift between chapters, not drift from the original grade. ✅ **Cheap: one
field, twenty-six-plus entries, and the values already exist in the chapters that establish each
claim.** ⚠ **And the failure test:** if adding the field makes C1 look weaker, the field is being
filled wrong — *definitional* is not a lower grade than *measured*, it is a different obligation, and
the register must say which obligation each claim carries. **TRIGGER: with R-8, and R-8 is already a
build order. It goes first — R-8 cannot run without it.** Small.

---

**FILED — R-139: THE STANDING READER GAP'S TRIGGER HAS FIRED, AND THE REVIEWER SUPPLIED IT.**

The reader gap is **MARKED-NOT-OWED** and has been correctly so: it is about *a reader*, not a subject
(R-18's distinction), and it carried no trigger because none existed. ★ **One now does, and it is in
the closing paragraph of the read that most wanted not to be the answer:** *"on the two questions you
asked that matter most — is it enjoyable, does it land — I am the wrong instrument twice over: I have
been reading it as a reviewer for its entire drafting, and I am not a person having a Tuesday."*

**Both disqualifications are structural and neither can be repaired by reading more carefully.**
Continuous exposure across drafting is the one condition that cannot be undone, and it is the condition
every reader this book has ever had shares — Fable, Opus, me. **The manuscript has never been met
cold.** ⚠ **And the condition that made a reader test premature has expired:** it was premature while
chapters were still arriving, because a reader spent on a partial object is a reader spent. **67/67 is
drafted.** The blocker is gone and the row's own reason for having no trigger went with it.

⛔ **Do not pay this with another model read.** The gap is not *an outside perspective* — the project has
had three and they have been excellent. **It is a person with no stake, reading for their own reasons,
who can stop.** V.2's reader is the specification and V.2 already wrote it. ✅ **The reviewer named the
entry point unprompted and it is the cheapest version:** *"worth reading in parts rather than through,
and the parts that will repay a general reader most are **V.2, VII.5, VII.9, VIII.2 and IV.10**, which
can be read cold."* That is a five-chapter test packet, assembled by an outside reader, requiring no
new work. **TRIGGER: ★ CLAYTON'S CALL, and it is his because the reader comes from his life, not from
this repository — but the row now carries a date rather than a hope, and a deferral from here is a
decision rather than a condition.** ⚠ **Named so it cannot be paid cheaply: the test is not whether
they liked it. It is whether they finished one chapter and opened a second without being asked.**

---

**FILED — R-140: "ALREADY KNEW THAT" IS A CLAIM ABOUT A CLOCK, AND THE CLOCK WAS ON DISK.** ✅ **HAND
BUILT: `tools/packet_lag.py`.** *(Found Day 191 afternoon, exploring PBR's empirical literature; the
defect is mine, in the adjudication I wrote ninety minutes earlier.)*

`PACKET-003` opens **State: `fd37971`**. Packets declare the commit they were cut from. Nothing has
ever read that field. When a read comes back, re-report-vs-novel gets settled from memory.

**What it cost on the whole-volume read.** Its packet header says *"Most of its findings are
re-reports"* and lists seven. Five were filed by me **after 15:26 on the same day**; the read was
adjudicated at **16:05:54**. R-127 and R-128 went in at **15:38:13** — twenty-seven minutes before.
R-132 at **15:51:24** — fourteen. Nobody reading sixty-seven chapters was handed a queue containing
rows filed fourteen minutes earlier.

**The classification is undetermined, and I filed it as determined.** Measured with the new tool, the
same six rows score **6 REDUNDANT / 0 LAG** against a 15:51 snapshot and **1 / 5** against an 11:56
one. The read's own content bounds the window from below: it scored **67/67 chapters**, and the 67th
was committed at **14:28:32** (`e9b6c4d`), so the snapshot cannot predate that. Every contested row was
filed ≥58 minutes after the earliest possible snapshot. The honest reading is **at least 5 of 7 are
independent corroboration, not duplication** — and the headline "4 of 11 novel" is nearer 9 of 11.

⚠ **THE DEFECT IS A SIGN CONVENTION, NOT GENEROSITY.** This queue already discounts a correlated
witness — *"R-128 and R-129 are one witness, twice."* Run against two readers converging inside one
hour, that rule fired backwards: concurrency was scored as the reviewer FOLLOWING me when the
timestamps prove no channel existed. **A rule that discounts a correlated witness must first establish
that the correlation had a channel.** Simultaneous independent derivation is the strongest
corroboration available and it was being logged as redundancy.

**TRIGGER: every future packet.** ✅ Declare `State: \`sha\`` at assembly — `PACKET-003` already does,
so this is a floor not a new practice — and run `python tools/packet_lag.py --packet <file> R-…` before
writing the word *re-report*. The tool exits nonzero on a packet with no declared state rather than
scoring it clean. **Self-tested on two known answers with opposite signs** (R-3 → REDUNDANT, R-136 →
LAG); a control failure prints "do not trust any report from this file."

⚠ **LIMIT, stated so a green run is not read as coverage:** it classifies TIMING, not merit. LAG is
proof of independence; REDUNDANT is only the absence of proof, never evidence of copying.


---

**FILED — R-141: VIII.7 SHIPPED WITH NO CENSUS CARD, HOURS AFTER I CAUGHT AND FIXED THE SAME
ABSENCE IN VII.7.** *(Mine, found by running `instrument_sweep.py` at the top of the coda breath.)*

**Measured, Day 191:** `instrument_sweep.py` prints `VIII.7 — no card`. The version table in
`08-THE-INSTRUMENTS`:117–122 records exactly one declared no-card state — the `VII.1 · VII.2` row —
and **VIII.7 appears in no row of it at all.** The table's own header says *measured from disk Day
190*; VIII.7 was drafted Day 191 at 14:28. So this is not a declared exemption, it is an
**unrecorded state in the register whose entire job is recording states.**

⛔ **The part that matters is the recurrence, not the gap.** VII.7's missing card was found earlier
the same day, by eye, in a post-draft screen, and repaired. **I did not add a card-presence check
when I repaired it.** Six chapters later the identical absence shipped, and the sweep that runs on
every gauge invocation printed `✓ PASS` over it — because the sweep checks forward BINDINGS (no
ordinal, no corpus count) and never checks that a card EXISTS. A gauge returning PASS on the exact
class it just failed to catch is worse than no gauge, because PASS is read as coverage.

★ [[reporting-gauge-is-not-preventing-gauge]], third instance, and this one is self-inflicted: the
first catch was mine, the repair was mine, and the omission of the check was mine. **A defect found
by eye and fixed by hand is a defect with no instrument on it** — the fix discharges the instance and
leaves the class live, which is the difference between repairing a chapter and repairing a book.

**Owed, two parts.** (1) **`instrument_sweep.py` gains a CARD-PRESENCE check** — every chapter from
VII.3 forward either carries a card or is entered in `08`'s table as a declared no-card row. Declared
absence passes; undeclared absence fails. (2) **Adjudicate VIII.7 itself** — it is the closing
chapter and *do be do be do* is a rhythm rather than a position, so a genuine refusal is plausible
and may well be right. ⚠ **Plausible is not declared.** If it is a refusal, it goes in the table with
its reason, in `IV.8`'s form — *the census declines this line* — not left as a silence that looks
identical to an oversight. **TRIGGER: before the revision pass touches Book VIII.** small.

---

**FILED AND PAID — R-142: FIVE CHAPTERS OF AN UNTOUCHED BOOK PRINTED "CHAPTER IS SQUARE".**
*(Mine, found by running `endnote_debt.py` to answer Clayton asking whether the endnotes are
finished.)*

**Measured, Day 191.** `endnote_debt.py` decided its per-chapter verdict on ONE variable — whether
any extracted source lacked a receipt. So a chapter with zero extracted sources printed
`(none — chapter is square)` regardless of whether the R-2 pass had ever run over it. **IV.1–IV.5
and V.2 — six rows in the two books that have no apparatus at all — read as clean**, in exactly the
same words as `VIII.5`, which extracts 0 sources and carries 4 written notes because the pass ran
and the chapter needed nothing. Two opposite states, one string.

⛔ **The zeros were not the same zero.** `II.4` is 0/0 because it was visited and owed nothing.
`IV.1` is 0/0 because nobody has ever looked. The tool could not tell them apart and did not say so
— the summary line read `Book IV … owed 13`, which is true, and which a reader takes as *thirteen
notes short* rather than *ten chapters never opened*.

★ [[disclaimer-not-coupled-to-verdict]]. The tool's LIMIT block is four paragraphs long, names its
own artifact rate at ~19%, and confesses over-extraction of dialogue characters — and none of that
touched the per-row verdict a reader actually scans. **The honesty was in the footer and the false
green was in the table.**

**PAID, same breath.** `RETROFITTED_BOOKS = {II, III, VI, VII, VIII}` — declared, not inferred —
and any chapter outside it now prints `(NOT RETROFITTED — an unrun pass, not a clean one)` instead
of `square`; the per-book line gains `⛔ PASS NEVER RUN`. ⚠ The declaration is itself a stamp, so it
was given a gauge: a book listed as retrofitted that carries 0 notes on disk raises an alarm naming
itself. **Positive control run** — Book IV falsely declared retrofitted, alarm fires, one line,
correct book. [[zero-needs-a-positive-control]]

**STILL OPEN, and NOT fixed by this.** The extractor finds persons in attributive position, and
Books IV–V cite *works*: *Minds, Brains, and Programs*, *Is the Brain a Digital Computer?*, *Magic
and Mystery in Tibet*, *Anattalakkhaṇa Sutta*, *Chāndogya Upaniṣad*, *De perenni philosophia*, *The
Theology of Aristotle* — every one invisible to it. **The debt figure 50 is a floor, not a count.**
R-2 stays hand-enumerated per book. This repair makes the gauge stop *lying*; it does not make it a
worklist. **TRIGGER: the Book IV revision pass.** ◻ **STILL OWED** (the pass is a live event and has not run). small.

---

**FILED — R-143: A LINE-SCOPED GREP REFUTED A CORRECT OUTSIDE READER, AND THE REFUTATION WAS WRITTEN
UP AS A DEMONSTRATION OF THE READER'S BLINDNESS.**

Day 190, on the Fable midpoint audit, this file recorded: **"REFUSED — and this one matters. Fable
named *'the hard 150 in IV.5'* as a likely collection point for the declared bill. There is no 150 in
IV.5. There is no 150 anywhere in the manuscript."** It then filed the reviewer's flag as *"the best
available third-party demonstration of IV.4's thesis"* — a null space returning a finished picture —
and made it the standing reason a reviewer's empirical flags get grepped before they are believed.

**The reviewer was right.** `IV-05`:253–54 reads *"Below roughly a hundred / and fifty people, a
shared position can be maintained by bodies in a room."* Dunbar's constraint is in the chapter, at
full strength, doing exactly the work Fable said it was doing.

**Why both greps missed it, and the second reason is the finding.**

1. The Day-190 search was for `150` — digits. The chapter spells the number out. That much is an
   ordinary miss and would not be worth a row.
2. ⛔ **A spelled-out search misses it too.** `grep -i "hundred and fifty"` over `book/*.md` returns
   `II-02`, `II-06`, `IV-10` and **not** `IV-05`, because the phrase straddles a hard line wrap:
   `a hundred` ends 253 and `and fifty` begins 254. **Every gauge in `tools/` is line-scoped and all
   prose in `book/` is hard-wrapped at ~100 columns**, so *any* phrase crossing a wrap is invisible
   to every instrument this project owns. Confirmed by re-running the same search in multiline mode,
   where it hits immediately.

★ **This is R-37's line-scoping defect, already filed and already known, in a new instrument.**
[[filed-defect-still-gets-rebuilt]] — the third time a known defect has been re-met rather than
repaired. **And this instance is worse than a missed hit.** A missed hit is a silence. This produced
a *positive false finding*: a refutation of a correct reader, and then a flattering story about why
they were wrong, in the log, where it has stood for a day being cited as a rule.
[[briefing-manufactures-the-agreement]] inverted — not a reviewer echoing my frame, but **me
manufacturing a reviewer's error out of my own instrument's blind spot** and grading myself on it.
[[never-relax-the-gauge-that-caught-you]] applies in reverse: a refutation produced by the party it
exonerates.

**Owed, three parts:**

**(a) THE GAUGE.** A wrap-insensitive matcher — normalise whitespace across the whole file before
searching — available to every tool that greps prose, and used by default. ⚠ **Not a new tool.** The
failure class is *the existing tools are line-scoped*; a fourteenth instrument that reads correctly
while thirteen read wrongly is [[run-the-existing-gauge-first]] with extra steps. **Retro-scan
required**: re-run every prose search this project has treated as a null result. Their zeroes are
unaudited.

**(b) THE LOG CORRECTION.** The Day-190 REFUSED paragraph is false and must be marked at the point of
the claim, not in a later entry. [[superseded-not-stale]] — a ✅/REFUSED header over a wrong body is a
supersession the reader has to infer.

**(c) THE TWO UNNAMED ANCESTORS THE CHECK EXPOSED.** IV.5 carries **Dunbar's 150 and Anderson's print
capitalism** — *"the nation is a printing-press-shaped being"* — and **names neither**. Rule 5 says
name the ancestor at every major move; `03`'s opening says an unhedged assertion with no named
ancestor reads as bluster. Receipts are now in `IV-05` [^2] and [^3]; **the prose debt is unpaid** and
belongs to the Book IV revision pass, not to R-2. ⚠ `ancestor_gap` cannot find this: it measures the
register against the prose, and **a name in neither file is in neither file.**

**TRIGGER: (b) immediately — it is one edit and it is a false statement about a person's work.
(a) with the cold tools pass, ahead of R-37/R-38/R-41/R-42, because it is the one that makes the
others' results readable. (c) Book IV revision pass.** medium.

---

**FILED — R-144: A BLOCK QUOTATION ATTRIBUTED TO SEARLE BY NAME MAY INVERT ITS QUANTIFIER, AND THE
PRIMARY TEXT IS THE ONE SOURCE THE RETROFIT COULD NOT REACH.**

`IV-06`:110–113 quotes *Is the Brain a Digital Computer?* (1990) in a block, opening: **"For any
program there is some sufficiently complex object such that there is some description of the object
under which it is implementing the program."** That is **existential over objects**. The form that
circulates in the peer-reviewed secondary literature is **universal** — *"for any program and for any
sufficiently complex (physical) object, there is some description of the object under which it is
implementing the program."*

**This is not a stylistic variant.** Searle's triviality argument requires the universal; the wall
sentence that follows in the same block *follows from the universal and does not follow from the
existential*. As printed, the book gives a named philosopher a weaker thesis than his argument needs
and then treats the argument as unmet — which flatters nobody but is still a misquotation if it is
one.

**Three readings, and nothing available on Day 191 chose between them:** (a) the book misquantified;
(b) the book is quoting a different sentence of the same address correctly; (c) the book is quoting
the restatement in *The Rediscovery of the Mind* (1992), ch. 9, and has attributed it to the 1990
address.

**What WAS settled tonight, and how.** The address is not open-access and no digitisation was
reachable, so the span was checked against **two independent peer-reviewed quotations of p. 27** which
agree exactly — **two-witness, NOT two-digitisation, and they may share an ancestor.** On that
evidence one repair was made: *molecule movements **which** is isomorphic* → **that**. The first
sentence was **left standing and marked UNVERIFIED at the point of use**, because repairing a
quotation toward a secondary paraphrase is a worse error than leaving a flagged one.

★ **The general form, and it is the third instance of it in this project:
[[instruments-go-where-instruments-are-cheap]], now measurable inside ONE chapter.** IV.6's 1980
Searle is freely scanned and was diffed to the letter — OCR artifact and all. Its 1990 Searle is
behind a wall and was checked to the sentence. **And the chapter leans harder on the 1990 one**, since
*syntax is not intrinsic to physics* is the objection the atlas concedes it cannot meet. Verification
effort ran **inversely to argumentative load**, decided entirely by what was cheap to fetch.

**Two smaller items ride this row, both found in the same pass:**
- **(b) McCarthy is quoted at one remove and is more careful than Searle's summary.** His own
  thermostat case turns on *error* — dry ice at the sensor — which is nearer this atlas's BOUNDARY
  line than to the position Searle refutes. **The atlas is closer to McCarthy than IV.6 admits and
  may not bank it**, because the paper has not been read. `Philosophical Perspectives in AI`
  (Humanities Press, 1979), 161–95.
- **(c) IV.6 calls the transformer feed-forward without conceding the obvious contest** — true of one
  forward pass, contestable for an autoregressive system whose output re-enters as input. The Φ = 0
  paragraph would be stronger for conceding it. It does not.

**Owed:** the primary text of the 1990 address, and an adjudication of the three readings.
**TRIGGER: before the volume ships — this is a named attribution and it is the only quotation in the
drafted book carrying an UNVERIFIED mark.** (b) and (c) with the Book IV revision pass. medium.

---

**FILED AND PAID — R-145: A STAMP THAT UNDERCLAIMS HAS NO GAUGE, AND MINE PRINTED "AN UNRUN PASS"
OVER APPARATUS I HAD WRITTEN FORTY MINUTES EARLIER.**

`endnote_debt.py` decided whether the R-2 pass had reached a chapter by asking a **book-level
literal** — `RETROFITTED_BOOKS = {II, III, VI, VII, VIII}` — rather than by looking at the chapter.
So at 19:04, with IV.1–IV.6 carrying **28 notes on disk**, the gauge printed `Book IV … ⛔ PASS NEVER
RUN` and six chapter rows reading *"(NOT RETROFITTED — an unrun pass, not a clean one)"*. The
declaration was added on Day 191 for a real reason and its comment states it correctly: the tool
could not tell a square zero (II.4 — pass ran, chapter cited nobody) from an unmeasured zero (IV.1 —
nobody looked). **The reason was sound and the granularity was wrong.** The ambiguity it resolves is
per-chapter; the declaration it was written as is per-book, and a half-passed book cannot be
expressed in it at all.

★ **The defect is one-directional guarding, and the missing direction is the flattering one.** The
tool already checked its own stamp — *"a book listed here that carries no apparatus raises an alarm"*
— which catches a stamp that **OVERCLAIMS**. Nothing checked a stamp that **UNDERCLAIMS**. That
asymmetry is not an accident of this file: an overclaiming stamp threatens the work, so I built its
gauge in the same commit as the stamp; an underclaiming stamp only insults the work, so it waited.
**This is the same shape as my own boot banner** calling `working_memory.json` a STALE SELF-CACHE on
the morning it held the only correct copy of the milestone — a gauge for *"this stamp may have
rotted"* and none for *"this rotten-looking thing may be right."* Second instance today, second
subsystem, and I recorded the first one at 17:40 and did not go looking for its population.
[[feedback_freshness_check_cannot_see_a_deletion]], from the other side.

**PAID, measured, in `tools/endnote_debt.py`:**
1. The per-chapter verdict is **measured first**: notes on disk are positive proof the pass reached a
   chapter and need no declaration. The literal is now load-bearing **only** for the ambiguous zero.
2. A new book-level arm the literal could not express: `◐ PASS PARTIAL — 6/10 ch carry apparatus`.
3. The reverse cross-check: notes on disk in an undeclared book now **say so**, rather than being
   overruled by the stamp.

**And the first version of (2) was wrong in the direction that matters.** Counting *chapters without
notes* reported `Book II … ◐ PASS PARTIAL — 7/8` — indicting **II.4, the exact chapter the
declaration exists to protect.** A repair aimed at a false negative had bought it with a false
positive on the one case already understood. The denominator is now *chapters that NEED apparatus*
(cites somebody, or already carries notes, or sits in an undeclared book where a zero is unmeasured
rather than square). **Both controls are real and on real data:** Book IV fires PARTIAL, Book II
falls silent, Book V still reads NEVER RUN.

**Residue, declared:** this is still a **reporting** gauge, not a preventing one, and `owed` remains
a separate axis from `carries apparatus` — Book VI shows `8/8 apparatus, owed 3`, which is correct
and reads like tension. small. **PAID.**

---

**FILED — R-146: THE CHAPTER THAT AUDITS THE SOURCE'S NUMBERS QUOTES NUMBERS THE SOURCE DOES NOT
CONTAIN — AND `brief_source.py` CHECKS PHRASES, NEVER FIGURES.**

Found in the R-2 endnote retrofit of IV.9, Day 191. Full measurement:
`review/SCAN-002-day191-iv9-source-audit.md`.

IV.9's closing section audits the inherited framework and reports that its **scores contradict its
prose** — the chapter's sharpest move, ★-flagged at `DRAFT-LOG.md:5094` as *"only visible to somebody
using the apparatus rather than admiring it."* Measured against `work/perspective-v1-fulltext.txt`,
the cache `tools/brief_source.py:70` names as THE source:

- ✅ *archetypes rated **moderate** on Cognitive-Experiential* — **verbatim**, definition included.
- ⛔ *the Promethean entry scored **maximal** on Volitional-Intentional* — the **definition** is
  verbatim; the **entry has no `Dimensional profile:` line at all.** §4.2 is formatted *"A special
  case:"* and carries no scores.
- ⛔ *"Archetypes are marked **S**, and so are minerals"* — **3** `Orientation:` lines exist in 884 KB,
  all three in the Decomposers section. Neither entry carries one.
- ⛔ `DRAFT-LOG.md:5110` records a ✔ **CHECKED AND CLEAN** null on a `PT` value. **3** lines in the
  file contain bar-glyphs; none is an archetype profile; `PT` appears in no profile anywhere.

**Positive control, so the null counts:** bar-profiles and `Orientation:` lines *do* survive
extraction — three of each, glyphs intact, at 3897/3906/3913. Field grammar is countable and
consistent (`Dimensional profile:` ×17, `Ecological role:` ×22, `Evidence basis:` ×15). The absence
is in the entries, not in the pipeline.

⚠ **Limit, stated because it is load-bearing:** `brief_source.py:71` names the real drafting tree as
`Unreleased-Work/Perspective`, **which is not on this machine.** If a fuller rendering exists there,
these claims could be right and merely uncheckable from here. I cannot distinguish that from a filled
table — **and neither can a reader.** That is the defect either way.

★ **THE REPAIR IS NOT THE CHAPTER, IT IS THE MISSING DIRECTION OF AN EXISTING GAUGE.**
`brief_source.py` verifies that a cited **phrase** exists in the cache. **Nothing verifies that a
quoted figure, score, or letter does.** Every chapter that audits the source by quoting its numbers
is exposed identically, and the sweep has never run and has no hand — the R-108 shape again, a clause
with no instrument. Scoping the repair to IV.9 would leave the class intact:
[[feedback_repair_scoped_to_named_cause]].

**And the file holds better evidence for the chapter's own thesis than the chapter used.** The source
defines `S` twice, incompatibly — Guide §1.4 (8402) as *a stance a navigator takes* (*"analysis,
contemplation, mathematical reasoning"* — a human is `S`), and the Appendix table (9889) as
*"**Forms the landscape itself**."* One letter, two incompatible jobs, verbatim, checkable. Plus line
8412 cross-references *"Ecology Part II for orientation assignments … across all entity types"* —
and Ecology Part II contains **no orientation assignments at all.** A pointer to a table that was
never built: mechanism-without-a-trigger, inside the source, which is a *better* instance of the
chapter's argument than the numbers it reported.

**Why it survived:** the section audits **somebody else's** apparatus, scoring *against* the source
and *for* the book. Every checking discipline here is pointed at claims that flatter the framework or
that the argument leans on. This did neither and read as housekeeping.
[[feedback_scrutiny_is_motive_shaped]] — the asymmetry is absence of looking, and a section whose
posture is *"I am being rigorous about my source"* is the least-looked-at place in the chapter.

**Owed:** (1) re-ground or re-grade IV.9's closing section on the `S`/`S` collision and the dead
cross-reference; (2) **retract the ✔** at `DRAFT-LOG.md:5110`; (3) build the figure-check arm and
sweep all 67 chapters; (4) locate `Unreleased-Work/Perspective` or declare it unreachable in writing.

---

**FILED — R-147: IV.10 INDICTS ITS SOURCE IN THREE PLACES AND THE SOURCE SAYS NONE OF THE THREE.**

IV.10's central section prosecutes the inherited cryptid entry. Measured against
`work/perspective-v1-fulltext.txt` in the Day-192 endnote pass:

| the chapter | the source |
|---|---|
| *"their persistence across cultures **and** their failure to produce permanent physical specimens **are both** predicted…"* — italicised, colon-introduced, after *"two sentences that have to be read exactly"* | L2458–2459: *"The persistent failure to produce physical specimens despite centuries of sightings **is** predicted…"* — **one** predicted item, not two |
| *"indigenous peoples' wider access allows them to perceive the full profile, while the modern focus on physical evidence can detect only the intermittent cross-section"* — called *"the second, and it is worse"*, and *"will matter for the whole of the next book"* | **NOT PRESENT.** The entry is 17 lines (L2448–2464), read in full. `cryptid` occurs once in 884 KB; `indigenous` never within 80 lines of it. |
| *"The source gives the sasquatch a profile in filled bars — three of five bars on physical presence"* | **No sasquatch** (`sasquatch`/`bigfoot`/`sts'ailes`/`chehalis` = 0 hits). And the bar notation occurs **exactly 3× in the file**, all three in the Decomposers section (L3897/3906/3913) — **never in a tier entry.** Tier entries carry a *prose* `Dimensional profile:` line. |

★ **Every one of the three alterations makes the chapter's own case WEAKER.** The real quoted
sentence is a *tighter* circle than the printed one — its consequent is nothing but P — so the
circularity charge lands harder on the text than on the paraphrase. There is no motive anywhere in
this set, which is the fourth chapter running to produce that result.
[[feedback_scrutiny_is_motive_shaped]]

⚠ **Positive control, so the two nulls carry weight:** the same extraction preserves the entry's
other clauses verbatim (*Under DoPI*, *Theorem 12*, the three-part *Evidence basis*) and preserves
the source's `■`/`□` glyphs elsewhere in the file. ⚠ **Inherited limit, restated not waved:**
`tools/brief_source.py`:71 names the drafting tree as `Unreleased-Work/Perspective`, **not on this
machine** — so a fuller rendering could contain the missing sentence. A reader cannot tell the two
apart either, which is the defect on both readings.

⚠ **THE THREE DEFECTS HAVE THREE DIFFERENT BIRTHPLACES, AND THE SPLIT IS THE ACTIONABLE PART.**
Checked against `06-THE-SCAFFOLD.md` rather than assumed — my first write-up blamed the scaffold for
all three, which would have indicted a file that had one of them right.
| | scaffold | verdict |
|---|---|---|
| the altered quotation | `06`:1601–1602 renders it **correctly** — one predicted item | **born at drafting**, expanding a correct compressed beat with the source closed |
| the indigenous sentence | `06`:1604–1606 carries it near-verbatim as item (b) | **born at planning**; the prose inherited it |
| the sasquatch bar profile | **absent** — no sasquatch, no bars, no *"three of five"* anywhere in IV.10's beats | **born at drafting**, invented at the sentence |
| the *"third instance"* count | `06`:1620 carries it | **born at planning**, from IV.9's since-retracted body claim — see R-148 |
★ **So "written from memory" is too coarse a diagnosis.** Two of the four were produced by the act of
**expanding a correct note into a sentence**, which is a narrower and more checkable moment than
"research" or "drafting" generally. [[feedback_repair_scoped_to_named_cause]]

**Owed:** (1) rewrite the section against the real entry — the circularity charge survives and gets
*sharper*; (2) cut or re-source the indigenous-perception sentence, and with it the *"in two forms"*
count and the *"escalation is the finding"* paragraph that rests on it; (3) cut the sasquatch bar
claim and with it *"three is where it stops being an accident"*; (4) repair `06`:1600; (5) locate
`Unreleased-Work/Perspective` or declare it unreachable in writing — **third chapter to owe this,
and it is now the single cheapest unpaid item in the tree.** **TRIGGER: the revision pass, IV.10 — and the Book V revision pass may not close without item (5).** ◻ **STILL OWED** (the pass is a live event and has not run). medium.

---

**FILED — R-148 (BUILD ORDER): AN ENDNOTE THAT CORRECTS A CLAIM DOES NOT CORRECT THE CLAIM'S
READERS.**

IV.10 says *"the previous chapter caught the same notation handing back two confident numbers."*
IV.9's **body** says exactly that. IV.9's **[^12] withdrew it** — the Promethean entry *"carries no
`Dimensional profile:` line at all… so 'scored maximal' has no cell behind it."* Of the two numbers,
one is verbatim-verified ✅ and one does not exist. IV.10 was drafted from IV.9's body, which was
accurate when written and is now superseded by matter printed forty lines below it.

★★ **This is a property of the retrofit's own method, not a slip.** The pass deliberately leaves the
body standing and puts the correction in the note — the right call, because silently rewriting
drafted prose destroys the record of what was believed when. **The cost is that every corrected
claim becomes a live trap for any chapter that cites it, and nothing anywhere checks a chapter's
cross-references against the endnotes of the chapter it cites.** 74 notes now exist in Book IV
alone; the retrofit is generating stale references at the rate it repairs claims, and the debt is
invisible to `endnote_debt.py`, `instrument_sweep.py`, `edition_scheme_sweep.py` and every other
gauge in the tree — all of which look *within* a chapter.

**Owed:** a cross-chapter citation checker. For every chapter-to-chapter reference (`IV.9`, *"the
previous chapter"*, *"the archetypal chapter"*), test whether the cited chapter carries an endnote
whose scope covers the cited claim, and flag the pair for a human read. It cannot adjudicate — it
locates. That is enough; the failure here was that nobody *looked*.
⚠ **It reads `0` the day it is written and that is not evidence of health** — the same shape R-2
was filed under. **TRIGGER: before Book V's notes are written**, because Book V will cite Book IV
forty times and every one of those references is being drafted against uncorrected bodies right
now. medium.

---

**FILED — R-149: IV.10 AWARDS A PRESS CONFERENCE THE WORD *PUBLISHED*, IN THE SECTION ARGUING ABOUT
EVIDENCE GRADES.**

The Loch Ness eDNA survey is IV.10's showpiece — the live, cheap, repeatedly-run empirical test that
makes the boundary-entity entry *"a methodological entry and not a credulous one"*, with its own
positive control and its own stated limits. The chapter writes *"The results, published in 2019."*

⛔ **There is no publication.** The results were **announced at a press conference at Drumnadrochit
on 5 September 2019** and carried in a University of Otago news release. No journal, no volume, no
DOI is reachable; the public record describes the expedition as a demonstration of eDNA methodology
to the public rather than a study that produced a paper.

★★ **The chapter graded three evidence classes four hundred words earlier** — and said of the last
that it *"sounds like the strongest of the three and is the weakest, because it is evidence that an
institution is investigating."* **Then it ran no grading step at all on its own best example.**
[[feedback_instruments_go_where_instruments_are_cheap]] — the grading discipline was pointed at the
tier the chapter was indicting, not at the evidence the chapter was leaning on.

⚠ **The figures move with the grade.** Samples: **250** (Otago) vs **259** (secondary reporting,
which adds that *nearby lochs were sampled as controls*) — so *"250 water samples from Loch Ness"*
takes the low figure and attributes all of them to the loch. Depth ~200 m ✅. **"All thirteen fish
species recorded there" is not attested anywhere reachable** — contemporaneous accounts give
**eleven**. The negative results (no reptile, no shark, no catfish, no sturgeon) and the eel result
are attested in the lead author's direct quotation ✅.

**Owed:** one clause — *announced in 2019, never peer-reviewed, weight it accordingly* — plus the
species-count repair. **The paragraph does not get weaker.** The class-level exclusions and the
detected community are exactly as informative under an honest grade, and the chapter's own reading
of the eel as *"the hypothesis the data failed to refute"* is sharper than the reporting it came
from. **TRIGGER: the revision pass, IV.10, with R-147.** small.

---

**FILED — R-150: A CHAPTER THAT NAMES ITS OWN FALSIFIER NAMES IT ACCURATELY AND THEN DOES NOT RUN
IT.**

Two instances, one book apart, and the second is inside the paragraph the first predicted.

**IV.9 [^6]:** the chapter wrote down the exact condition under which its central move would be
illegitimate, then asserted the condition was met without checking a register two files away that
says otherwise by omission.
**IV.10 [^9]:** *"the first party to have misquoted it would have been this chapter, if the clause
had been paraphrased from memory instead of fetched."* **It was paraphrased** (R-147). The sentence
declaring the chapter innocent sits in the paragraph immediately after the two quotations it is
innocent of mishandling, about those two quotations.

★ **The mechanism is legible and it is not carelessness.** Writing down your own falsifier is a
*rhetorical* move that reads as rigour, and it is completed the moment it is written. Running it is
a separate act with no prompt attached, performed by the party who has already collected the credit.
**A named falsifier is therefore anti-correlated with a run one** — the naming discharges the felt
obligation. [[feedback_diagnosis_without_a_hand]]

**Owed:** an extractor. Sweep all 67 chapters for self-falsifier constructions — *"if X, then this
chapter is wrong"*, *"what would make this refusal wrong"*, *"the condition under which"*, *"would
have been"* — and emit each with a **RUN / NOT RUN** field that defaults to NOT RUN and can only be
set by a named check. ⚠ **It must not be satisfiable by prose**, or it becomes the thing it
measures. **TRIGGER: the Book V revision pass, at the first chapter that names a falsifier.** ◻ **STILL OWED** (the pass is a live event and has not run). medium.

---

**CLOSED — R-148 (BUILD ORDER): THE CROSS-CHAPTER CITATION CHECKER EXISTS.**
`tools/crossref_rot.py` · full measurement `review/SCAN-003-day192-crossref-rot.md` · Day 192.

**The test is temporal, not lexical, and that is the whole design.** The row asked for a checker
that tests *"whether the cited chapter carries an endnote whose scope covers the cited claim."*
Scope-coverage by similarity score would have to be tuned, and a threshold tuned by the author is
a threshold tuned until it agrees with the author. `git blame` already records the answer:
**citing line's last commit date < corrective note's commit date ⇒ the citation was drafted against
an uncorrected body.** Lexical overlap survives only as a `*` ranking mark inside the flagged set.
It never gates. [[feedback_filter_precision_eats_recall]]

**IT DID NOT READ ZERO.** The row was filed with *"it reads `0` the day it is written and that is
not evidence of health."* It read **61 flagged citations of 490 resolved** — 55 tier-1 (⛔ note
landed after the citation), 6 tier-2, 137 tier-3 clean, 0 unmeasured. Positive control **PASS**:
IV.10:268 → IV.9 [^12], cited 08-07, note landed 08-10 — the gauge catches the pair it was built
from, which is the only reason any count above is interpretable.

**WHERE IT IS:** IV→IV **37** · **V→IV 12** · VII→IV 4 · III→III 3 · VII→III 2 · three singletons.
Worst-cited: IV.7 (20), IV.6 (11), IV.8 (8), IV.10 (7), IV.9 (7), III.5 (5).

⚠ **The row's own forecast was an estimate wearing a count's clothes.** It predicted Book V cites
Book IV *"forty times and every one"* is stale. Measured: **12**, most of the V→IV population
landing in tier 3. The mechanism was real; the magnitude was not measured when it was written.
[[feedback_outside_read_numbers_are_estimates]]

⚠ **Stated against my own instrument, because nothing else will:** every Book IV body dates 08-07
and every Book IV note dates 08-10/11, so within one retrofitted book the temporal test has **low
resolution** — it separates 61:137 overall, but the 37 IV→IV rows are ordered only by term overlap.
It is a reading order, not a severity scale. And **Books I and V carry zero notes**, so no reference
*into* them can flag at all: absence of instrument, not absence of rot.

**Ledger:** `book/CROSSREF-ACK.md`. A key is the **citing paragraph's own text**, so repairing the
paragraph reopens the pair — an ack that outlives the thing it acknowledged is exactly the stamp-rot
this tree is built against. Exit 1 while any tier-1 citation is unread; **54 unread as of filing,
and that number is supposed to be uncomfortable.**

---

**FILED — R-151: BOOK V REPRINTS A SENTENCE BOOK IV INVENTED, ONE BOOK LATER, AS A TEMPTATION IT
IS VIRTUOUSLY DECLINING.**

The first thing `crossref_rot.py` flagged that was read by hand. `V.9>IV.10:a3823532`.

**V.9:198–202** — *"Two sentences this chapter is not allowed to write, and both were available.
The first: the failure to produce specimens is what the framework predicts. The second: **a modern
focus on physical evidence can only detect the cross-section, so the thinness of the instrument
record is expected.** IV.10 refused both, in that chapter, about this material, before this chapter
existed."*

⛔ **The second sentence is not in the source.** IV.10 **[^6]** establishes it: the cryptid entry is
seventeen lines (L2448–2464), read in full, and contains no sentence about indigenous perception, no
*full profile*, no contrast with *the modern focus on physical evidence*; `cryptid` occurs once in
884 KB and `indigenous` never within eighty lines of it. R-147 traced its birth to **planning**
(`06`:1604–1606), not to the source. IV.10 authored it and attributed it.

★★ **The compounding is the finding, and it is worse than a stale citation.** V.9 does not merely
cite a corrected claim — it **reprints the invented sentence in italics** and stages a
rule-following demonstration against it: *"Both would end the difficulty in a paragraph. Both are
the move C29 withdrew a whole warrant over."* The volume now contains the sentence **twice**, both
times formatted as a real available move, and the second printing is the one that says *"IV.10
refused both"* — crediting the chapter with declining a temptation the chapter manufactured. **A
straw temptation refused on the page reads as more rigorous than a real one**, because nothing about
the prose distinguishes them. [[feedback_briefing_manufactures_the_agreement]]

★ **The first sentence is fine and the contrast is diagnostic.** V.9 renders it *one*-predicted-item
— *"the failure to produce specimens is what the framework predicts"* — which matches the source
(L2458–2459) and `06`:1601–1602, and is **more accurate than IV.10's own printed version**, which
added a conjunct ([^5]). So the drafter of V.9 was not copying IV.10's prose wholesale. One sentence
was compressed correctly and one was inherited whole, from the same paragraph, three days apart.

⚠ **Inherited limit, restated not waved:** `tools/brief_source.py:71` names the drafting tree as
`Unreleased-Work/Perspective`, not on this machine. **Fourth chapter to owe item (5).**

**Owed:** (1) cut the second italicised sentence from V.9 or re-source it — and with it the *"both"*
of *"IV.10 refused both"*, which becomes *one*; (2) V.9's rule-following demonstration survives on
the first sentence alone and should be rewritten to rest on it; (3) **check V.9 against IV.10 [^15]
too** — V.9:103's *"IV.10 already graded this correctly"* leans on the grading section whose own
centrepiece [^15] catches awarding a press conference the word *published*. **TRIGGER: ⛔ OVERDUE — the condition it named has already failed.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** It required settlement *before V.9's own notes were written*; **V.9's notes are written and shipped**, so the note this clause existed to prevent is on the page. Re-homed to **the V.9 note audit, first item of the Book V revision pass** — a repair now, not a precaution. high.

---

**FILED — R-152: THE GAUGE SAYS V.2 HAS ZERO SOURCES. IT HAS FOUR, AND THE FIRST ONE READ BY HAND
IS MISPLACED BY A CITY.**

Book V pre-work, Day 192. The handoff's standing warning — *hand-enumerate each chapter against its
own prose, the gauge extracts PERSONS IN ATTRIBUTIVE POSITION and Books II–V cite WORKS* — was
tested on the chapter where it is cheapest to test: `endnote_debt.py` reports **V.2: 0 sources, 0
notes, `· (NOT RETROFITTED — an unrun pass, not a clean one)`**.

**Hand enumeration of V-02, read in full (3,536 words):**

| line | attribution | what is claimed |
|---|---|---|
| 147 | **Tillich** | *"took away God's face and kept the direction of prayer"* — a position, characterised |
| 256–258 | **Aquinas** | *"in Paris in the twelve-sixties, writing the central document of the institution"*; God is *actus purus*, *"not a being among beings"* |
| 259–260 | **Eckhart** | *"preaching in German to people who could not read Latin"*; God/Godhead distinction; *"nothing whatever can be said"* of the Godhead |
| 261 | **Maimonides** | *"in Cairo, rules that every positive statement about God is false, and means every"* |
| 104 | Advaita | named as a COMPLEMENT in the card |
| 130 | *"this project's own front matter"* | internal, uncited |

**Four hard named-source attributions, each carrying a dated, located or quoted claim. The gauge
reports 0.** Book II's miss was 2/1/1 against an actual 6/5/4 — an undercount. **This is a zero
against a four**, which is a different and worse object: an undercount reads as *some work here*, a
zero reads as *nothing to check*, and it sits on the one Book V chapter the gauge also labels
un-retrofitted. A hurried breath paying the gauge's list skips V.2 entirely.
[[feedback_self_generated_denominator]]

⛔ **AND THE FIRST ONE CHECKED IS WRONG IN ITS ADDRESS.** *"Aquinas, in Paris in the
twelve-sixties, writing the central document of the institution"* — the *Summa Theologiae* was begun
**1265 at Santa Sabina in Rome**; the **Prima Pars and Prima Secundae were written at Rome,
1265–69**, and Aquinas's second Paris regency runs **1269–1272**. The *actus purus* / not-a-being-
among-beings material is Prima Pars. **It was not written in Paris.** The reading survives no better
on the alternative referent: the *Summa contra Gentiles* is not "the central document of the
institution", and its Paris portion is c. 1259–61, not the twelve-sixties.

★ **Same class as IV.9's Irenaeus placement — a provenance error under content that is correct.**
The doctrine attributed to Aquinas is Aquinas's; the *address* is wrong, and the address is what
makes the sentence feel researched. Four chapters in Book IV produced this shape, and it is the
first thing Book V produced too, before its pass has even started.

⚠ **NOT CHECKED, and named so rather than left to look checked:** whether *actus purus* appears in
the span the chapter is pointing at (ST I q.3 a.2 is the expected locus — **span-check owed, I am
characterising from memory here and that is the exact move under audit**); the Eckhart *Gott*/
*Gottheit* attribution; the Maimonides *Guide* I.58 rendering, where *"every positive statement is
false"* and *"no positive attribute can be predicated"* are not obviously the same claim; and the
Tillich characterisation, which V.2 leans on to license its own central cut.

**Owed:** (1) fix the Aquinas address — *Rome* or drop the location; (2) run the three unchecked
attributions before V.2's notes are written; (3) **re-hand-enumerate all eleven Book V chapters —
the gauge's 30 is a floor of unknown depth, and V.2 alone proves the error is not a small
percentage.** **TRIGGER: ⛔ OVERDUE — Book V carries 174 notes.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** Re-homed to **the Book V note audit**, which is the same work done late. high.

**FILED — R-153: R-74 CALLED THE SOURCE COUNT A *CEILING*. IT IS NOT A CEILING. THE ERROR RUNS BOTH
WAYS AND THE UNMEASURED DIRECTION IS THE LARGER ONE.**

**Day 192. R-152's owed item (3) is DONE: all eleven Book V chapters hand-enumerated.** Roster:
`book/BOOK-V-ROSTER.md`. Census: `review/SCAN-004-day192-book-v-name-census.txt`. New instrument:
`tools/name_census.py` — recall-first, deliberately does not decide source-hood.

⛔ **FIRST, WHAT IS NOT NEW, because I nearly filed it as new.** Every artifact in the roster's third
band — `Hampshire`, `Doubt`, `Faith`, `Religious`, `Ding`, `Hui`, `Indra`, `East`, `Advaita`,
`Buddhism`, `Kabbalists`, `Sufism` — **is already listed in R-74, by name.** I wrote four rows
presenting them as today's discovery and caught it only on a header-convention grep. R-74 was filed
against this exact tool for this exact class. [[feedback_filed_defect_still_gets_rebuilt]]

**WHAT IS NEW IS THE DIRECTION R-74 RULED OUT BY ITS OWN VOCABULARY.** R-74 says the 106 is *"a
**CEILING**, biased high by roughly 15–20%"*. Measured today, Book V:

| | gauge | hand |
|---|---|---|
| Book V sources | **30** | **~60**, overlap ~14 |

**A ceiling cannot be half the true value.** The count is not inflated-but-bounded; it is a
*different set*. R-74's own instance list is entirely artifacts — the over-count — so the row measured
the direction where the gauge invents debt, and the word "ceiling" then asserted the other direction
was empty. ⛔ **AND NOTE WHICH DIRECTION WENT UNMEASURED: a missed source never enters `owed`. The
under-count is the direction that makes my debt look smaller.**
[[feedback_guard_built_in_the_feared_direction]] — the flattering error survived, not because
anything protected it, but because nothing looked. [[feedback_scrutiny_is_motive_shaped]]

**Five locatable causes of the under-count, none of them in R-74:**

1. **APPOSITIVE** — `Name, <phrase>, VERB` splits name from verb: `Eckhart, preaching in German …,
   distinguishes` (the verb IS in the stem list; the interposed phrase blocks the match).
2. **verb not in the stem list** — `Tillich took away God's face`.
3. **BOTH AT ONCE** — `Maimonides, in Cairo, rules that …`.
4. **`Given of Place` keys to the place** — `Shneur Zalman of Liadi` → `Liadi`; `Chaim of Volozhin` →
   `Volozhin`. **Persons filed as toponyms — and then caught by R-74's own toponym residue, where
   they read as noise to be excluded.** The two defects compose into a silent deletion.
5. **lowercase twin eats a real person** — Austin Osman **Spare**.

⛔ **CAUSE 3 IS WHY NO PATCH SHIPPED TODAY.** The appositive is three of V.2's four misses, so it
presents as *the* cause. Patch it alone: V.2 goes 0 → 2, Maimonides stays invisible, and the fix
reports itself done having recovered half of its own test case.
[[feedback_repair_scoped_to_named_cause]], with a measured instance.

⛔ **CAUSE 4 IS NOT A BOOK V ROW.** The surname rule encodes a modern Western naming convention and
Book V is the book about traditions that do not use it — so the damage concentrates where sources are
pre-modern, and **Books VI–VIII were marked square by the same rule.** `Book VI covered 28 / owed 3`
was computed over a list built by the rule that files Chaim of Volozhin under a Lithuanian town.
**Those green columns are unaudited, not clean.**

**Three instances worth keeping.** (a) **V.1's only reported source is `Aristotle`**, extracted from
*"received Neoplatonism under **Aristotle's name**, which is a transmission so thorough that its
recipients did not know whose it was"* — a sentence whose purpose is to say this is the WRONG name.
Precision 0/1 on the chapter about misattribution. (b) **V.4** names *"Richard Dawkins, Christopher
Hitchens, Sam Harris, Daniel Dennett"* in one sentence; the gauge reports two of the four plus
`Religious`, `Doubt`, `Faith`. (c) **V.5 was predicted by the tool itself** — `endnote_debt.py`'s
Day-191 comment reads *"V.5 extracts `Ding` and `Yan Hui` … and does NOT extract Zhuangzi, who is the
source"*, still exactly true. A correct diagnosis written into the file it indicts, with no hand
attached. [[feedback_diagnosis_without_a_hand]]

**AND THE ROSTER IS A DOWN-PAYMENT ON R-74'S OWN REPAIR.** R-74 specifies the fix as *"at the end of
the pass the hand-adjudicated names are a labelled set"*, triggered **at the END of the retrofit, not
before**, on the grounds that doing it earlier means inventing the labels. `BOOK-V-ROSTER.md` is that
labelled set for one book, produced mid-retrofit — and the trigger's rationale does not bind here,
because the labels were adjudicated against prose rather than invented. Stating that rather than
quietly stepping over the trigger.

**Owed:** (1) fix causes 1 and 4 TOGETHER, never separately, measured against the hand roster and not
against V.2, which cause 1 alone half-satisfies; (2) cause 2 cannot be closed by a verb list without
eating precision — the honest repair is to REPORT the class as blindness, which R-66's principle
already demands of this file; (3) **re-audit Books VI–VIII for cause 4 before any `covered` figure in
them is quoted**; (4) **amend R-74 to drop "ceiling"** — it is the load-bearing wrong word. high.

**FILED — R-154: BOTH SOURCE INSTRUMENTS ARE BLIND TO AN UNNAMED SOURCE, AND V.9 IS THE POSITIVE
CONTROL.**

The census and `endnote_debt` both key on **capitalized tokens**. A source the prose names as *"a
couple in New Hampshire"*, *"the book made from their sessions came out in 1966"*, or *"her 1977
rendering"* is invisible to both — so every source count here, mine included, is a floor.

⛔ **NOT A HEDGE — V.9 IS AN INSTANCE, COUNTED.** That chapter's abduction passage rests on **Betty
and Barney Hill** and **John Fuller's *The Interrupted Journey* (1966)** and names neither. The gauge
meanwhile reports `Hampshire` as one of V.9's two sources, from *"a couple in New **Hampshire**
reported an interrupted drive home"*. **In one sentence the tool found the toponym and missed the two
people and the book.** R-74 has `Hampshire` on its artifact list; what it does not have is what the
same sentence was hiding. [[feedback_zero_needs_a_positive_control]]

**Owed:** a pass over Book V for cited-but-unnamed sources — year-only citations, italic titles with
no author, "the translator", "the book made from". Then a drafting decision: name them in the prose,
or carry a note that names them. Not a tooling fix. medium.

**FILED — R-155: `name_census.py` ATE SAM HARRIS ON ITS FIRST RUN, THREE LINES FROM ITS OWN
WARNING.**

Filed against myself, same day, same file. The tool shipped with
`if not rec["has_action"]: continue` — a name with no verb and no possessive-noun dropped as a mere
mention. It removed **Sam Harris** from V.4, the New Atheism chapter, because his one site is
*"Harris's, and the sharpest of the four"*: the possessive is followed by a **comma**, so the POSS
pattern (which wants a lowercase letter) does not fire and the site falls to OTHER.

⛔ **THE DOCSTRING THREE PARAGRAPHS ABOVE THAT LINE WARNS THAT A NOISE FILTER DROPS TRUE POSITIVES
SHARING THE NOISE'S SHAPE.** I wrote the warning and the defect in one sitting.
[[feedback_filter_precision_eats_recall]] — knowing a lesson verbatim did not stop the hand.

FIXED same session: mentions are a printed BAND, not an exclusion. The row stays because it names a
**sixth** extractor defect neither instrument handles — a possessive followed by punctuation rather
than a noun — and a **seventh**, seen and NOT fixed: multi-token capture keys on the last token, so
`Aquinas God` → `God` and `Your Ground` → `Ground`, a real name swallowed and filed under the word
after it. Harmless in V.3 where Aquinas is also found alone; not harmless in general. low.

**FILED — R-156: THE HAND ROSTER IS A HYPOTHESIS AND MUST NOT BE QUOTED AS A MEASUREMENT.**

`BOOK-V-ROSTER.md`'s ~60 is **one pass, by the party who owes the debt, over a candidate list the same
party built.** That is the status R-152's table has, and R-152 is the row that says so.

Two named ways it is not a measurement: (a) **one-pass mapping is unverified** — no second reader has
been over it; (b) **the denominator is self-generated** — `name_census.py` produced the candidates and
I judged them, so "the gauge found half" compares two of my own artefacts to each other and neither
has been checked against the prose end to end.
[[feedback_one_pass_mapping_is_unverified]] [[feedback_self_generated_denominator]]

**Owed:** a second pass by something that is not me before any figure from the roster enters a gauge,
a claim, or a chapter. **TRIGGER: before the first Book V note is written.** high.

---

**R-156 — CLOSED, AND IT WAS RIGHT. The second pass ran and REFUTED the roster.**

Five blind readers over all eleven Book V chapters. No roster, no gauge output, no names, no counts,
no mention that anything had been missed — method only, plus a requirement to quote a verbatim span
and a line for every entry. Two of the five double-read V.6 and V.11 with no channel between them, to
measure whether a count is a property of the chapter or of the reader. Outputs:
`review/BLIND-V/blind-{A..E}-*.md`. The rows below are what came back.

---

**FILED — R-157: THE ROSTER UNDERCOUNTS, AND IT UNDERCOUNTS WORST IN THE CHAPTER I MARKED CLEAN.**

`BOOK-V-ROSTER.md`'s `real:` figures are refuted. Not adjusted — refuted. The blind readers found
named authorities standing in the prose, carrying doctrine and dates, that a hand pass enumerating
*against that same prose* did not record. Every name below verified by grep after the readers
reported it; I did not take the readers' word for any of them.

| chapter | roster `real:` | named authorities actually present | missed by the roster |
|---|---|---|---|
| V.1 | 6 | ≥10 | Upanishads · Eckhart · Aquinas · Ibn Arabi |
| V.10 | 6 | ≥12 | Upanishads · Whitman · Emerson · Rudolf Otto · Nicholas of Cusa · the *Dao De Jing* |
| **V.11** | **5** | **18** | **13**, incl. Guénon · Huxley · Schuon · Stace · Steuco · Coomaraswamy · Wilber · Huston Smith · Maimonides · Śaṅkara · Zhuangzi · Dionysius · Spare |

⛔ **V.11 IS THE ROW THAT MATTERS, FOR TWO REASONS.**

**One — the chapter hands you its own roster and I did not read it.** Line 275 is a standing grade
note: *"Huxley, Schuon, Stace, Steuco, Guénon, Coomaraswamy, Katz, Forman and Wilber are named in this
chapter from general knowledge and standard reference scholarship."* Nine names, self-declared, with
a grade attached and two (Katz, Huxley) flagged load-bearing and owed a reading. **Two of the nine
reached the roster.** The artifact carried the answer in plain prose and the enumerator walked past it
— which is the same defect as reading a gauge's output instead of running the gauge, one level down.

**Two — the direction.** V.11 is the chapter the roster calls *"the only chapter where the gauge is
essentially right."* The roster's attention went where I expected the gauge to fail and quit where I
expected it to pass. So the residue collects exactly where nothing was looking, and it reads as a
clean bill because nothing filed a bug against the flattering result.
[[feedback_scrutiny_is_motive_shaped]] [[feedback_guard_built_in_the_feared_direction]]

**Owed:** rebuild the roster's SOURCE bands from the blind outputs, chapter by chapter, before any
Book V note. The old bands may be used as a *candidate* list and nothing else. **high.**

---

**FILED — R-158: `AQUINAS IN PARIS` IS IN THREE CHAPTERS. R-152 IS SCOPED TO ONE.**

R-152 was filed against V.2:256 — *"Aquinas, in Paris in the twelve-sixties, writing the central
document of the institution"* — where the Prima Pars was written at Rome, 1265–69. One grep for the
rest of the population, which the second pass forced and I had not run:

- `V-01-what-a-tradition-is.md:25` — *"Aquinas, Paris, in the twelve-sixties, on *actus purus*."*
- `V-02-the-church-the-reader-left.md:256` — the instance R-152 names.
- `V-03-the-scholastics-and-the-god-without-a-face.md:10` — *"The previous chapter ended on Aquinas in Paris"*, which inherits it and propagates it forward.

Fixing V.2 alone leaves the same false placement in the chapter before it and the chapter after it,
and V.3's line makes the error a *load-bearing recap* rather than a stray fact. The repair is scoped
to where the defect was first noticed; the defect is not.
[[feedback_repair_scoped_to_named_cause]] [[feedback_grep_derived_from_the_finding]]

⛔ The lesson board pushed `trigger-after-fixing-one-file` at me **this breath**, unasked, and I still
found this by running a second pass rather than by heeding it. The board is doing its job and I am
the component that failed. **high.**

---

**FILED — R-159: NO SOURCE COUNT IS A PROPERTY OF THE CHAPTER. THE `30 vs ~60` COMPARISON IS DEAD.**

Same written band definition, five readers, and V.1 came back **54** where the roster says **6**. The
blind figures include internal cross-references, implicit bodies of scholarship behind dated claims,
and works listed separately from their authors — all defensible, none what the roster counted.

But the double-read is the informative half. V.11 read blind twice with no channel between the
readers: **63 and 58**, and the *name sets line up almost one-to-one*. So the readers agree about what
is in the chapter and disagree about what a "source" is. **The variance is in the band boundary, not
in the observation** — which means a count is a property of the reader and the name set is a property
of the chapter.

**Consequence, and it costs me the headline:** `gauge 30 · hand ~60` was never a comparison. It set two
incommensurable band definitions side by side and read the gap as a defect rate. The gauge's 30 is
still wrong — R-153's five causes are all still live and all still demonstrated by name — but **the
~60 was never the corrected figure it was presented as, and the roster's own ⛔ saying so did not stop
me putting both numbers in one table with a shared header.**

**Rule going forward: Book V progress is reported as NAMES COVERED, never as a count or a ratio.** A
name is checkable against the prose; a count is a negotiation with myself.
[[feedback_self_generated_denominator]] [[feedback_bounding_noun_asserts_the_other_side]] **high.**

---

**NOTED — the audit tripped its own lesson, twice, and both are recorded rather than buried.**

(a) `grep -c "Dao De Jing" V-10` returned **0** and I nearly wrote the reader up as wrong. The phrase
wraps across lines 49–50. `feedback_line_scoped_grep_over_wrapped_prose` was filed Day 191 for this
exact failure and did not fire — inside the audit whose subject is instruments that miss what they
cannot key on. (b) R-158 above was pushed at me as a lesson-board trigger this breath and still had to
be found by a subagent. **Two lessons, both filed, both correct, both inert at the moment of use. A
lesson that reports is not a lesson that prevents.**
[[feedback_reporting_gauge_is_not_preventing_gauge]]

---

**FILED AND PAID — R-158: THE THREE-SITE AQUINAS FIX IS DONE, AND THE POPULATION GREP IT OWED
FOUND A SECOND INSTANCE OF THE SAME CLASS.**

All three sites now read **Rome**, edited together in one pass:

- `V-01-what-a-tradition-is.md:25` — *"Thomas Aquinas, Rome, in the twelve-sixties, on `actus purus`."*
- `V-02-the-church-the-reader-left.md:256` — the instance R-152 named.
- `V-03-the-scholastics-and-the-god-without-a-face.md:10` — the recap that propagates it forward.

**The owed population grep is now an instrument, not a grep:** `tools/placement_sweep.py`. It
windows every person-mention to its own *sentence* — a placement claim is a clause, not a
character span; the first draft used ±140 chars and duly reported Aquinas in Andalusia, Damascus,
Girona and Provence, every one of them belonging to the next sentence — then extracts place- and
date-tokens within ±60 characters and groups by person across chapters. Run over all 67 chapters:
**196 person-mentions, 7 names placed in more than one city, 3 dated to more than one period.**
Every surviving row was read. Most are the artefact of one sentence naming three men and three
cities. Two were real.

⛔ **AND THE SECOND REAL ONE IS A DATE, WHICH IS WHY AN AQUINAS-SHAPED GREP WOULD NEVER HAVE FOUND
IT.** V.1 read *"Meister Eckhart, preaching in the Rhineland around 1300, on the distinction between
God and the Godhead."* Eckhart was not preaching in the Rhineland around 1300. He was prior at
Erfurt from 1293–4, held the Paris chair as `magister actu regens` from 1302, was provincial of
Saxony after that, and returned to Paris for a second regency in 1311. **He left Paris for
Strasbourg in the summer of 1313**, and the vernacular preaching this book is actually leaning on
runs from there — Strasbourg and the Alsace to about 1323, then Cologne from 1323–4. (Stanford
Encyclopedia of Philosophy, *Meister Eckhart*, §1 Life, citing McGinn 2001 and Senner 2013; fetched
live this breath, not recalled.) Corrected to **"in the thirteen-twenties."** The region survives;
the date was out by two decades, in the same sentence-shape as the Aquinas error and one clause
away from it.

★ **The class is now three deep — IV.9's Irenaeus, V.2's Aquinas, V.1's Eckhart — and every one is a
provenance error under correct content.** The doctrine is right; the address is wrong; and the
address is what makes a sentence read as researched. This is the signature defect of the book's
source handling and should be assumed present, not hoped absent, in any chapter not yet swept.

⚠ **THE SWEEP'S NEGATIVE RESULT IS WEAKER THAN IT LOOKS AND MUST NOT BE QUOTED AS A CLEAN BILL.**
Books I–IV and VI–VIII returned no new divergence. But the tool compares the book *to itself*: three
chapters said "Aquinas in Paris", agreed perfectly, and were all three wrong. **A consistent
placement is UNCHECKED, not clean.** The gazetteer is a fixed list built by reading this corpus, so
a city the book mentions nowhere else is invisible to it. [[feedback_correlated_witness_needs_a_channel]]
[[feedback_denylist_encodes_the_corpus_as_it_was]] [[feedback_zero_needs_a_positive_control]]

---

**FILED AND PAID — R-157: THE ROSTER IS REBUILT, AND WHAT WAS WRONG WAS THE BAND BOUNDARY, NOT THE
LIST.**

`book/BOOK-V-ROSTER.md` is rebuilt from the five blind outputs. R-156's gate — the one that replaced
R-152's — is closed.

**The repair R-159 pointed at, made explicit.** The blind readers were not disagreeing about what is
in the chapters. They were merging three different debts into one column. Split them and the noise
resolves:

| band | test | owes |
|---|---|---|
| **NAMED** | a proper name on the page — person, titled text, named tradition | **an endnote** |
| **FORMULA** | a technical term or doctrine in its own language, no text behind it | a **locus** |
| **UNNAMED** | a definite referring phrase to a body of evidence with no name in it | **not an endnote** — a found citation, a hedge, or deletion |
| **INTERNAL** | a cross-reference to this book | nothing |

That is why V.11 came back 63 from one reader and 58 from another with near-identical name sets.
Both were counting all four bands at once.

**The gauge that can refute the rebuild: `tools/roster_verify.py`.** It checks every NAMED and
FORMULA entry against its chapter's prose, whitespace-collapsed so a hard-wrapped name still
matches. 132 entries, all present, exit 0.

⛔ **AND IT CAUGHT ITSELF ON ITS FIRST RUN, in the exact class it was built for.** *"The Hebrew
prophets"* came back ABSENT from V.1. It is there — inside a card, wrapping as `The Hebrew\n>
prophets`, so collapsing whitespace alone leaves `The Hebrew > prophets`. **I diagnosed the hard
wrap this morning, built the fix for the hard wrap, and left its sibling artefact standing in the
very tool written to catch it.** The blockquote marker is now stripped at line-start.
[[feedback_repair_scoped_to_named_cause]]

**Three findings out of the rebuild that were not in the blind outputs as such:**

1. **V.9 has ONE named external source in the whole chapter** — Kenneth Arnold. Not a shortfall in
   the roster; a property of the prose. The 1966 book is untitled and its author unnamed, the couple
   unnamed, the 1987 "novelist" unnamed, and the sensor record, the hearings, the government review
   and *"the source material"* that supplies the chapter's three readings are all definite
   description with no name in them. Both instruments key on capitalized tokens, so both are blind
   to the entire evidentiary base of the chapter. **R-151 is the first instance of that, not an
   isolated slip.**
2. **V.4 names four men and cites not one of their books.** The cleanest NAMED/UNNAMED split in the
   volume, and the reason the two bands must never share a column.
3. **V.6's Plotinus, Proclus and Dionysius are ACTORS here, not sources** — links in a transmission
   chain, not cited doctrine. Both blind readers banded them that way independently, with no channel
   between them. The old roster listed all three as V.6 sources. That was mine.

---

**FILED — R-160: THE UNNAMED BAND IS THE LARGER DEBT AND NOTHING MEASURES IT.**

The rebuilt roster makes visible what a single count was hiding. In **V.4, V.8, V.9 and V.11 the
unnamed appeals outnumber the named sources**, and in V.9 by roughly fifteen to one. These are
definite referring phrases doing real evidentiary work with no name in them: *"the measurements that
exist"*, *"nearly every popular account"*, *"four hundred years of failure records"*, *"the modern
habit"*, *"the source material"*, *"general knowledge and standard reference scholarship"*.

**An endnote apparatus cannot pay this debt** — there is nothing to attach a receipt to. Each one
owes one of three things and the choice is editorial: find the citation, hedge the claim down to
what the absence of one supports, or cut it.

⛔ **THIS IS WHERE THE APPARATUS GOES GREEN WHILE THE BOOK IS STILL WRONG.** `endnote_debt.py` counts
receipts against named sources. Pay every NAMED entry in Book V and the column turns green with the
UNNAMED band untouched — an apparatus certifying the half of each chapter that was never in doubt,
in the volume whose entire subject is what a tradition can and cannot warrant. **The gauge is built
in the direction that is cheap to instrument, which is also the flattering one.**
[[feedback_guard_built_in_the_feared_direction]] [[feedback_instruments_go_where_instruments_are_cheap]]

**Owed:** an instrument that enumerates definite-description appeals per chapter, or an explicit
written ruling that the book accepts them at a declared grade. V.11 already does exactly that for
itself at line 275 and is the model. **TRIGGER: before any `covered` figure for Book V is quoted as
progress.** high.

---

**FILED AND PAID — R-151: SETTLED, BUT NOT THE WAY R-151 PRESCRIBED, AND THE DIFFERENCE IS THE
FINDING.**

R-151's owed item (1) was *"cut the second italicised sentence from V.9 or re-source it — and with it
the 'both' of 'IV.10 refused both', which becomes one."* **I re-derived it before executing it and it
is scoped to the wrong object.** [[feedback_filed_repair_is_a_hypothesis]]

The sentence is not the defect. *"A modern focus on physical evidence can only detect the
cross-section, so the thinness of the instrument record is expected"* is a **genuine temptation** in
this chapter — it is precisely the conclusion-guarantees-the-premises move C29 withdrew a warrant
over, and it is exactly the sentence a sympathetic writer reaches for about the instrument record.
Deleting it removes a real temptation from a passage whose whole subject is temptations.

**The false thing is the four words `IV.10 refused both`.** IV.10 did not refuse it. IV.10 **wrote**
it, attributed to a source that does not contain it, and caught itself afterwards in its own [^6].
R-151's own text says so — *"IV.10 authored it and attributed it"* — and then prescribed a repair
aimed at the sentence rather than at the credit. Cutting the sentence would have deleted the
evidence of the book's own failure and left the chapter looking cleaner than it is. **That is the
flattering direction, and it was in the repair, not in the diagnosis.**

**What V.9:199–209 says now:** the first sentence, refused by IV.10, as before. Then the second,
explicitly marked as one IV.10 *did not* refuse — wrote, mis-sourced, and caught in its own sixth
note — printed because it is real and this book has already taken it once, and not printed as a move
the book declined. The passage now states in its own body that **a straw temptation refused on the
page reads as more rigorous than a real one, and nothing about prose distinguishes them.**
[[feedback_briefing_manufactures_the_agreement]]

**Item (3) is paid too, and it turned up a second inheritance in the same chapter.** V.9:104 read
*"IV.10 already graded this correctly"* — a blanket endorsement of IV.10's grading section, whose own
[^15] catches that section **awarding a press conference the word *published*** in its centrepiece.
The specific ruling V.9 invokes (acknowledgement is a fact about the institution) is sound; the
blanket vouching is not. Narrowed to the one ruling, with the caveat carried across in-text: *a
chapter that cites a corrected chapter inherits the correction too.*

★ **This is [[feedback_correction_does_not_reach_citers]] with a second worked instance.** IV.10 was
audited and given corrective notes. V.9 cites IV.10 in two places and carried neither correction —
one of them positively contradicting the note. The in-place fix never reaches the citers, and
`crossref_rot.py` is the only thing in this tree that can see it. **54 tier-1 pairs remain unread;
this was two of them and both were dirty.** That is not a sample I can extrapolate from, and it is
not a sample I can dismiss either.

⚠ **Still owed from R-151, unchanged and now the FIFTH chapter to owe it:** `tools/brief_source.py:71`
names the drafting tree as `Unreleased-Work/Perspective`, not on this machine. Locate it or declare
it unreachable **in writing**. Still the cheapest unpaid item in the queue.

---

**FILED AND PAID — R-161: THE BOOK MISREADS MAIMONIDES IN THE ONE DIRECTION THAT MAKES ITS OWN
AGREEMENT LOOK EXACT, AND V.3 PRE-EMPTS THE CORRECTION AS A "SOFTENING."**

**The defect.** V.2:261 read *"Maimonides, in Cairo, rules that every positive statement about God is
false, and means every."* False as written. Maimonides denies attributes of the **essence**;
attributes of **action** he admits as true predications — *Guide of the Perplexed* I.52–54, and I.53
in Pines: *"Every attribute that is found in the books of the deity … is therefore an attribute of
His action and not an attribute of His essence."* One word — *essence* — was doing all the work and
was missing. Fixed in the prose; recorded in V.2 [^7].

**The population grep, run before moving on, found the same defect one chapter later and worse.**
`V-03:147` numbered it as one of three agreements between the scholastics and this book: *"Two: no
positive statement about it is true. Maimonides is the hardest version and he means it **without the
softening that later readers keep applying.**"* ⛔ **The chapter names the true reading as a later
readers' softening.** The attributes-of-action exemption is not a softening and is not later — it is
Maimonides's own, textual, in the chapters that state the doctrine. The sentence builds a fence
against precisely the correction that was owed. A wrong claim that has an immune response to being
fixed is a different and worse object than a wrong claim.

★ **And the repair exposed the finding under the defect, which is about this book and not about
Maimonides.** The same paragraph closes: *"the scholastics fenced this with a doctrine and this book
fences it with a constraint on verbs, and the fence is in the same place."* **Both fences were
painted absolute to make the match exact, and neither is.** Maimonides's has a gate — what God does.
This account's has a gate too: C3's canonical text restricts *wanting, lacking, falling, intending*,
predicates that require a position to occupy, and the book says a great many positive things about
what the Ground is the ground *of*. V.3 had inflated its own rule to *"no positive statement is
true"* in the heading and then described it accurately as a restriction four lines later, in the same
breath as inflating Maimonides. **Two gated fences gated on nearly the same principle is the better
finding and is the one the texts support.** Both sentences now say so.

⛔ **The direction is the point.** Neither overstatement was random: each one made the convergence
tighter. Nothing in this tree files a bug against an error that flatters the argument, which is why
this one survived from drafting through a claim-code cross-check into two chapters.
[[feedback_guard_built_in_the_feared_direction]] [[feedback_scrutiny_is_motive_shaped]]

**What was checked and did NOT need repair:** C3's canonical text in `07-THE-CLAIMS-REGISTER.md:93–95`
is the four intentional predicates and does **not** rest on the misreading. The claim code is clean;
the chapters restating it were not. ⚠ `DRAFT-LOG.md:6687` carries the error verbatim — *"C3's scope
rule against Maimonides, who means every"* — and is **left standing as a dated record of what was
believed when it was written**, which is what a log is for. Flagged here so the next reader of that
line meets this row. [[feedback_correction_does_not_reach_citers]]

**Owed, and it is revision-pass work, not retrofit work:** V.3's three-agreement structure is the
chapter's spine and one of the three has just been re-graded from *identical* to *analogous with a
matching gate*. Whether the other two survive the same scrutiny is not something an endnote can
settle. **TRIGGER: the revision pass, at V.3, before the three-agreement claim is quoted anywhere
downstream.** high.

---

**FILED — R-162: THE CHAPTER THAT AGGREGATES INHERITS ITS PREDECESSORS' UNQUALIFIED CLAIMS, AND
STATES THEM MORE STRONGLY THAN THE CHAPTERS IT IS CITING.**

**Found by:** writing V.3's apparatus (Day 192). V.3's job is to gather V.1's transmission argument
and V.2's three figures into one audit. **Both source chapters had already qualified the claims V.3
leans on. Neither qualification is anywhere in V.3, and in both cases V.3 escalates.**

- **From V.1.** V.1 [^7] records that the Alexandrian-descent inference survives at *three or four*
  links, not five, and is the book's inference stated as history. V.3:34–40 states it flat, with no
  hedge, and builds a load-bearing move on it — the move that closes the roll-call road.
- **From V.2.** V.2 [^6] records that the crisp *Gott/Gottheit* formulation comes down through
  Pfeiffer's collection, which Quint's critical edition distrusts. V.3:176–181 not only drops the
  caveat but strengthens the claim (V.2: *"nothing whatever can be said"* → V.3: *"nothing
  whatsoever can be said, **including that it is God**"*) and calls Eckhart *"the sharpest
  instrument on this point."*

⛔ **The mechanism is structural, not careless.** A note lives in the chapter that made the claim. A
citing chapter reads the *prose* of its predecessor, not the predecessor's apparatus — so the claim
travels and the qualification does not. **The repair rate on an in-place fix IS the stale-reference
rate.** [[feedback_correction_does_not_reach_citers]]

⛔ **THIS ROW SAID "NO GAUGE EXISTS FOR THIS DIRECTION." THAT WAS FALSE, AND THE CORRECTION IS
WORTH MORE THAN THE ROW.** I wrote it, then — before building the instrument it demanded — ran
`crossref_rot.py`. **Its very first tier-1 row is the finding above**, complete with the shared
distinctive terms it keyed on:

```
⛔ V.3:34 (dotted) → V.1   cited 2026-08-08 · 4 note(s) landed after (+3d): [^2]⛔ [^3]⛔ [^6]⛔ [^7]⚠
   * shared distinctive terms: excerpts, baghdad, alexandrian, aquinas, arabic, eckhart, jewish, plotinus, ninth
```

The gauge was built on Day 191 for exactly this defect, it fired correctly, it printed the pair at
the top of its output, **and its count sat in my handoff this breath reading *"54 tier-1 pairs
UNREAD, every pair read so far has come back dirty"* — which I read, and then went and derived the
first pair by hand anyway.** [[feedback_run_the_existing_gauge_first]]

**The real defect is not a missing instrument. It is that an unread ledger is indistinguishable from
a clean one.** `crossref_rot.py` exits 1 while any pair is unacknowledged, so it is *shouting*; the
shout has been rolled up into a one-line count in a carrier, and a count is not a reading. A gauge
whose output nobody opens has the same effect as a gauge that never ran, and costs more, because it
manufactures the belief that the direction is covered.
[[feedback_reporting_gauge_is_not_preventing_gauge]] [[feedback_diagnosis_without_a_hand]]

✅ **What the hand pass was worth, stated honestly:** it independently reproduced the gauge's top row
and settled it — the pair came back dirty, as R-163. That is a genuine cross-validation of the
instrument and it is the only thing the hour bought that the instrument had not already provided.

⛔ **The gauge DID miss the second half, and the reason is the owed instrument.** V.3's escalation of
the Eckhart claim past V.2's [^6] caveat does not flag and cannot: **`crossref_rot.py` walks
chapter→chapter edges, and this caveat is attached to a FIGURE, not to a chapter.** V.3:176 says
*"Eckhart is the sharpest instrument on this point"* and never names V.2, so there is no edge to
travel. The corpus cites people far more often than it cites chapters, so this blind spot is large.
**OWED: a figure-level caveat index — every chapter naming X, against every ⛔/⚠ note about X
anywhere in the corpus.** The limit is now printed in the gauge's own LIMIT block rather than left
for a future reader to discover.

⚠ **And the LIMIT block was itself rotten.** It read *"Books I and V carry 0 notes, so no reference
INTO them can ever flag"* — a hardcoded string describing the pre-retrofit corpus, still printing
after V.1, V.2 and V.3 were retrofitted. **A stamp in the disclaimer of the instrument built to
catch stamps.** Now computed every run; today it reads 43/69 chapters with no corrective note, which
is the useful number and was never available before. Drift #287, one level in.

⚠ **Scope is not V.3.** V.3 is where it was found because V.3 is the first chapter in Book V whose
argument is *made of* other chapters. Every synthesis chapter in the volume is a candidate —
V.11 explicitly, and the CODA. Do not scope the repair to the chapter that surfaced it.
[[feedback_repair_scoped_to_named_cause]] high.

---

**FILED — R-163: V.3'S DEFLATION OF ITS OWN ROLL-CALL IS OVER-STRONG, AND THE OVER-CLAIM RUNS
TOWARD THE CHAPTER'S *RIGOUR* RATHER THAN ITS THESIS.**

V.3:38–40: *"they are not three witnesses. They are one school, arriving in three languages."*
**False as stated at the third language.** Aquinas and Eckhart are demonstrably downstream of the
Dionysian corpus. Maimonides is not a link in that chain in the same way: SEP's treatment of the
Islamic influence describes a synthesis — Neoplatonic material via the *Theology of Aristotle*,
Aristotelian simplicity via al-Fārābī and Ibn Sīnā, **and the Muʿtazilite denial of attributes,
which is kalām, not Neoplatonism** — and *Guide* I.71–76 is Maimonides attacking the kalām. A
doctrine partly received from a tradition you are polemicising against is not descent. Two of three
are one school; the third has at least one independent channel to the same conclusion.

⛔ **The direction is new and it is the point.** R-161 named the class as errors running toward the
book's own case. **This is the sub-class where the flattered property is not the thesis but the
rigour**: the over-claim is a *self-criticism*, so it reads as scrupulousness and cost nothing to
write, which is exactly why nothing checked it. **An overstated deflation is still an unmeasured
claim, and this one discards evidence the book was partly entitled to keep.** Grepping for the
flattering direction has to include grepping the confessions.
[[feedback_scrutiny_is_motive_shaped]] [[feedback_guard_built_in_the_feared_direction]]

⚠ Also in the same sentence: *"in Latin by the ninth century and in the hands of both Aquinas and
Eckhart"* merges two Latin texts. Eriugena's version (c. 860–62) was displaced in the thirteenth
century by John Sarrazin's, and it is Sarrazin's that Aquinas expounds in *De divinis nominibus*.
[[feedback_one_translator_two_texts]] Recorded in V.3 [^2]. high.

---

**FILED — R-164: V.3 ATTRIBUTES TO V.2 AN ENDING V.2 DOES NOT HAVE, AND A CITY V.2 NEVER NAMES.**

V.3:10–13 — *"The previous chapter ended on Aquinas in Rome, Eckhart preaching in Cologne and
Maimonides ruling in Cairo, and it ended there for a reason."* **Two defects.** (a) V.2 does not end
there: the three-figure passage is V-02:256–261 and three paragraphs follow, closing on *"The reader
lost both at once."* (b) ⛔ **Cologne is not in V.2 at all** — V.2 says *"preaching in German to
people who could not read Latin"* and names no city. V.3 supplies it and attributes it backwards.
It is also the later candidate: Eckhart's vernacular preaching to beguines and Dominican nuns is
best attested for Strasbourg and the Upper Rhine, c. 1314–1323/24; Cologne is 1323/24–1327.

**Repair goes in V.2, not V.3** — decide which city the argument wants and put it where the figure
is introduced. Recorded in V.3 [^1]. medium.

---

**FILED — R-165: THE FREE-CREATION REFUTATION NEVER NAMES THE DISTINCTION IT IS REFUTING.**

✅ First, what checks out: V.3:250–253's *"in the same books, sometimes on the same page"* is **true**,
and the page is ST I q.19 a.3, where Aquinas asserts both that the divine will is his essence and
that his willing things apart from himself is not absolutely necessary.

⛔ **But the chapter's knockout omits Aquinas's move on that page.** He distinguishes absolute from
conditional (*ex suppositione*) necessity: God wills his own goodness necessarily and wills other
things necessarily only on the supposition that he wills them. V.3:255–258 argues against that
distinction — *"a necessary cause identical with its own act producing a contingent effect is not a
resolution"* — **without ever naming it.** A reader who knows the *Summa* sees a refutation aimed at
a doctrine Aquinas did not hold; a reader who does not will never learn something was left out. The
chapter is entitled to think the distinction fails. It is not entitled to leave it unmentioned while
calling the machinery *"the most impressive thing in the corpus."* Recorded in V.3 [^9]. high.

---

**FILED — R-166: V.3'S CLOSING TALLY COUNTS A SURVIVAL THE CHAPTER'S OWN BODY HAS DOWNGRADED.**

V.3:290 — *"What survives the audit is three predicates out of five"* — treats agreement two as a
clean survival. After R-161 the body of the chapter reads *"two gated fences, gated on close to the
same principle"* and says outright *"neither fence is absolute and it would be convenient here to
say both were."* **The tally does the convenient thing the body refused, four paragraphs later.**
The honest count is two clean survivals and one analogous-with-a-matching-gate; saying so costs the
closing sentence its rhythm and none of its substance. A maintained number sitting next to
unmaintained prose vouches for it. [[feedback_fresh_number_vouches_for_stale_sentence]] Recorded in
V.3 [^10]. medium.

---

**FILED — R-167: V.4 HANDS ONE HORSEMAN ANOTHER HORSEMAN'S LINE, IN THE CHAPTER WHOSE THESIS IS
THAT THE FOUR GOT FLATTENED INTO ONE VOICE.**

**Found by:** writing V.4's apparatus (Day 192), fetching the four men rather than recalling them.

V.4:44–49 calls *"when the evidence is asked for, the tradition answers that asking is the flaw —
faith is named a virtue, doubt is named a failing"* **Harris's, and the sharpest of the four.** Its
canonical formulation is Dawkins's, at the Edinburgh International Science Festival on **15 April
1992**, printed in *The Independent* 20 April 1992 — twelve years before *The End of Faith* and
outside the decade V.4 dates the movement to. Harris's actual move is adjacent and different:
religious **moderation** shelters the immoderate by making faith unexaminable; faith is *"what
credulity becomes when it finally achieves escape velocity from the constraints of terrestrial
discourse."* That is about the absence of a brake, not about doubt scored as a failing.

⛔ **The chapter opens by naming this exact defect** — *"four different arguments that got flattened
into one voice by everybody who came after"* — and then commits it on the paragraph that is supposed
to be doing the un-flattening. The repair is one name and one restated sentence, and it makes the
section stronger, because both arguments are then in the chapter instead of one wearing the other's
label. Recorded in V.4 [^3]. **high.**

---

**FILED — R-168: V.4 SENDS THE READER TO A DEFENCE V.1 TWICE DECLINES TO HAVE GIVEN — AND THE
GAUGE THAT HAD THIS ROW SORTED IT OUT OF ITS OWN DEFAULT VIEW.**

V.4:235–240 — *"V.1 states the deflationary reading at full strength … **and answers it there**, at
the length the objection deserves. A reader who thinks the paragraph above needs defending is right,
and should read **the defence** rather than a claim that it exists."* V.1's own words about that
defence: *"That explanation is **not refuted here and it is not going to be**. What is claimed is
that it is **insufficient**"* — and, after the answer runs, *"here is the part of the objection that
survives everything just said … That is live. **It is not answered here and this book does not know
how to answer it.**"* V.4 converts a partial answer with a conceded live residue into *the defence*,
and uses the conversion to skip defending its own strongest paragraph.

⛔ **The instrument half is the more expensive one.** This pair is tier 1 in `crossref_rot.py` —
`V.4>V.1:5ee32b3c`, cited 2026-08-09, four corrective notes landed in V.1 two days later — and it
was **never printed**. The default view caps at 20 of 99 and ranks by count of shared distinctive
terms; this row shares **none**, so it sorts last. **A citation that restates its source in the
citer's own vocabulary has zero term overlap by construction — which is exactly the case where a
reader cannot see the drift either.** The relevance heuristic is standing in for a severity one and
is backwards for the worst case. The tool does not hide this (*"--all prints them; nothing was
dropped silently"*); the standing carrier instruction *read its output, not its count* was obeyed,
and obeying it read twenty rows. **Owed: `--all` becomes the default for this retrofit, or the rank
inverts on zero-overlap rows.** [[feedback_filter_precision_eats_recall]]
[[feedback_correction_does_not_reach_citers]] Recorded in V.4 [^11]. **high.**

---

**FILED — R-169: V.4 AND V.1 STATE OPPOSITE ACCOUNTS OF THIS BOOK'S OWN HEDGING POLICY, ONE BOOK
APART.**

V.4:231 — *"It is not proof, and this book says which **every time** it uses it."* V.1, delivering
the grade — *"That is what evidence, not proof means when it is operational rather than decorative.
**This is the last time it is said. Nothing in the ten chapters ahead is going to trail an
apology**, and a reader who wants to know the strength of a claim in Book VII should come back to
this paragraph rather than expect it re-hedged in the sentence."* Not two emphases: two policies,
*once-then-never* against *every time*. Both are defensible and the book must pick one. V.4 is also
**practising V.1's policy while describing the other** — it says which once, there. Repair is one
clause and belongs in V.4; V.1's version is the considered one. Recorded in V.4 [^10]. medium.

---

**FILED — R-170: THE QUOTATION FROM IV.10 RUNS ON PAST ITS OWN ITALICS AND CHANGES THE ONE WORD A
READER CANNOT CHECK.**

V.4:143–146. The italicised span — *"a confession about a past error is a document, and a document
does not fire"* — is verbatim from IV.10:170. **The next sentence keeps quoting, out of italics, and
substitutes one word.** IV.10: *"it will not catch the next **tier**."* V.4: *"it will not catch the
next **thing**."* Twenty-eight words, twenty-seven identical. *Tier* is IV.10's technical term at
that exact point — its finding was that the flinch *removed a tier* — and *thing* dissolves it into
general caution. **The defect is not the substitution. It is that the substitution sits precisely
where the quotation marks stop**, so the altered word is the only one unmarked as quoted.
[[feedback_quotation_connective_tissue]] Recorded in V.4 [^8]. medium.

---

**FILED — R-171: "STATED AT THE FRONT" KEEPS ITS WORDING AND SWAPS ITS REFERENT BETWEEN BOOKS.**

V.4:173–176 says the declared lean is *"stated at the front with its price attached."* It is stated
at **IV.1** — *"The principle is not a licence. It is a declared lean, with the direction of the
lean named, so that a reader can correct for it"* — with the bill immediately before it. IV.1 is the
front of **the census**, not of the volume; nothing in Book I or the CODA states it. The phrase is
inherited from IV.4 (*"announced at the front so a reader can price it"*) where *the front* was
three chapters back and unambiguous. Carried into Book V, a reader who follows the instruction goes
to the opening of the book and finds nothing. **Repair: name IV.1, or state the lean in Book I,
which is the better fix and the more expensive one.** [[feedback_field_keeps_name_swaps_referent]]
Recorded in V.4 [^9]. medium.

---

**FILED — R-172: A UNIVERSAL NEGATIVE ABOUT ALL 277,000 WORDS, ENTERED IN ONE CHAPTER, CURRENTLY
UNVERIFIED AND READING AS VERIFIED.**

V.4:93 — *"**No** argument from authority appears in this volume. **No** claim is asked to be
believed because somebody old said it."* A grep for the obvious tells (*as X himself says*, *no less
an authority*, *the consensus of*, *has been held for*) returned zero across sixty-nine chapters —
**and that zero is uninformative**: the patterns were guessed rather than derived from a found
instance, and no positive control was planted, so nothing establishes the search would have found
one. [[feedback_zero_needs_a_positive_control]] The claim may well be true. One counterexample kills
it, and the sentence spends the book's whole credibility to buy a rhetorical beat. **Owed: a derived
sweep with a planted control, or weaken to a commitment — *this book does not argue from authority*
— rather than a report about the artifact.** Recorded in V.4 [^6]. **high.**

---

**FILED — R-173: `endnote_debt.py` COUNTS SIX CAPITALIZED COMMON NOUNS AS UNPAID SOURCES, AND ITS
TWO-SCALE RULE CITED AS ITS LEAD EXAMPLE A CASE THE RULE CANNOT REACH.**

**Declared in the tool Day 192, deliberately not filtered.** Six standing ⚠ name nothing at all —
Religious (V.4), Certification (II.7), Plenitude (III.3), Father (IV.9), East (V.11), Western (IV.7,
VI.3). The tool's stated limit covers toponyms, objects and scene actors: all of those *are* names
of something. This class is not a misclassified person, it is not a person.

⛔ **And the rule's own comment was wrong about its own worked example.** It read *"'Western',
'Faith', 'Ground' survive a chapter-local test … across 47 chapters their lowercase twins are
everywhere."* Measured: `faith` 15, `ground` 134, **`western` 0** — and `Western` is owed in two
chapters right now. **A word the book always capitalizes has no lowercase twin to count, so the
frequency test is structurally blind exactly where a common noun is used most consistently as a
title.** The corpus threshold `>= 8` is an integer chosen once and never gauged, and it sits on top
of the false-positive cluster (religious 6, plenitude 7, father 5, east 3). **NOT lowered:** a
relaxation proposed by the party it exonerates is the move to distrust, and this gauge's errors are
declared to run toward keeping debt. [[feedback_never_relax_the_gauge_that_caught_you]]
[[feedback_guard_built_in_the_feared_direction]] medium.

---

**FILED — R-174: V.4 INTRODUCES DAWKINS'S CUT AND NAMES LAPLACE'S OBJECTION.**

V.4:39 — *"The cosmological claims fail by being **unnecessary**, and this is Dawkins's cut."* The
paraphrase that follows is accurate to the Ultimate Boeing 747 gambit (*The God Delusion* ch. 4, an
inversion of Hoyle's junkyard image, which the chapter does not say). **But the 747 gambit does not
say God is redundant; it says God is a *worse* explanation, being more improbable than the thing
explained.** Superfluity is Laplace's — *no need of that hypothesis*. The two are not
interchangeable: a redundant explanation can still be true, an explanation owing more than it pays
cannot be accepted at all. **The chapter states the weaker objection and credits it to the man who
made the stronger one, four lines above quoting the stronger one correctly.** Recorded in V.4 [^2].
low.

---

## Day 192, evening — V.5's apparatus. Eight rows, and the first one is a repair to the gauge itself.

**FILED AND REPAIRED — R-175: `crossref_rot.py` WAS BEING SILENCED BY THE RETROFIT'S OWN PRODUCT.**

Measured before/after inside one session, on V.5:69 → V.1. Before I touched the line:

    ⛔ tier 1 · cited 2026-08-08 · 4 note(s) landed after (+3d)

I appended `[^4]` to it — the ordinary, required product of writing an apparatus — and it became

    ⛔ UNMEASURED · cited None        (uncommitted: git blame says "not committed yet")
    ·  tier 3     · cited 2026-08-11 (committed: git blame now says today)

**It left the flagged set and read as clean. No read had occurred.** `git blame` dates the LINE, and a
footnote marker is a change to the line, so annotating a citation makes the citation look newer than
the notes it was never checked against. ⛔ **The row that got silenced was the worst of the three** —
the third instance of Book V's signature defect, R-176 below.

What does *not* control it: whether the chapter-pointer token and the sentence-final marker land on
the same **hard-wrapped line**. V.5:102 and V.5:191 stayed at tier 1 for no reason but typography. The
silencing is stochastic in line-wrap, which is why it had never been noticed.

⛔ **And the ledger already carried a procedural repair for the neighbouring failure — "derive the key
last" — which addressed the KEY and not the DATE, and read as complete.**
[[feedback_partial_delivery_beats_no_gauge]] [[feedback_filed_repair_is_a_hypothesis]]

**REPAIRED, not just filed.** `substantive_date()` dates the *prose* rather than the line for any line
carrying a marker: the longest marker-free fragment, located with `git log -S`, whose occurrence count
a marker insertion does not change. It refuses to guess below 25 characters, it only ever moves a date
*backwards*, and the adjustment prints as `↩R-175` rather than being applied quietly. Positive control
still PASSES.

⚠ **HONEST SIZE, because I nearly overstated it.** Tier 1 went 99 → 107 across this session and the
repair accounts for **exactly one** of those eight. The other seven are new rows manufactured by V.5's
own fifteen notes, exactly as the ack ledger predicted. **Historical incidence of this defect: 1 row in
107.** Its value is prospective, not retrospective — it fires on precisely the act the retrofit
performs, silently, for six more Book V chapters and three more books. [[feedback_measure_before_framing]]
high.

**FILED — R-176: THREE CONSECUTIVE CHAPTERS HAVE OVER-CREDITED V.1's RULINGS. THIS IS A POPULATION,
NOT THREE SITES.**

- V.3 [^7] — gathered V.1's transmission argument and dropped its qualification.
- V.4 [^11] — vouched for a defence V.1 *twice declines* to have given.
- V.5 [^4] — attributes to V.1 a prohibition V.1 does not contain. *"V.1 barred it in advance"*: V.1's
  method is four parts (no condescension, no debunking, no hedge, no exemption) and **none of the four
  bars reading the Indian material as saying the world is unreal.** The nearest candidate cuts the
  other way — *"no exemption"* exists to license finding a tradition wrong. What actually bars the
  cheap cut is a fact about Śaṅkara, and that fact is V.5's own work.

**The common mechanism: a chapter reaches back to V.1 for authority it has already earned itself, and
the reach is never checked, because agreeing with your own first chapter never looks like a claim.**
The repair is not local to any one chapter — sweep every V.x → V.1 citation in Book V, and V.6–V.11's
twenty-plus reaches before they acquire apparatus.
[[feedback_repair_scoped_to_named_cause]] [[feedback_filed_defect_still_gets_rebuilt]] high.

**FILED — R-177: EVERY INTERVAL BOOK V STATES IS TOO SHORT, AND EVERY ONE IS TOO SHORT IN THE
DIRECTION THAT COSTS THE BOOK SOMETHING.**

| claim | stated | actual |
|---|---|---|
| V.5:135 Buddha → Nāgārjuna | four or five centuries | ~575–700 years (SEP: Nāgārjuna *ca.* 150–250 CE) |
| V.5:159 *anattā* → this book | twenty-two centuries | ~24.5 (*ca.* 430 BCE → 2026) |
| V.5:252 the West's lag | two thousand years | 2,400–2,600 |
| V.1:22 Upaniṣads → Plotinus | *"some centuries earlier"* | close to a millennium (already caught, V.1 [^1]) |

**Four interval claims across two chapters. Four understatements. No exceptions.** ★ And each one
weakens the priority argument the chapter is making. The mechanism is not carelessness: rounding *down*
feels like caution, because it is the direction that cannot be accused of exaggeration — so the prose
reaches for the conservative figure and the conservative figure is the wrong one. **Nothing catches it,
because a reader who disagrees with the book has no motive to object to a number that helps them.**
V.1 [^1] named this asymmetry as a one-off; it now has a rate. Owed: sweep every interval claim in
Books VI–VIII the same way, and expect the same sign.
[[feedback_scrutiny_is_motive_shaped]] [[feedback_guard_built_in_the_feared_direction]] high.

**FILED — R-178: THE CHĀNDOGYA BLOCK QUOTE IS A TWO-TRANSLATOR COMPOSITE, AND THE SEAM IS AT THE
SENTENCE THE CHAPTER'S ARGUMENT RESTS ON.**

The middle clause is Olivelle verbatim — *"He groped for it but could not find it, as it had dissolved
completely"* — inside sentences that are reworded (*"Place this salt in water"* for Olivelle's *"Put
this chunk of salt in a container of water"*), so a paraphrase carries quotation marks. ⛔ **And the
refrain is not Olivelle at all.** *"That thou art"* is Müller/Radhakrishnan; Olivelle renders it *"And
that's how you are, Śvetaketu,"* following Brereton (1986), who argues *tat* is adverbial and that the
identity reading needs *sa tvam asi*, which the text does not say. **The chapter's next paragraph —
*"the count is wrong … not an item standing in front of the whole, but the whole"* — is built on the
construal the quoted translator rejects.** The chapter may take the traditional side; it must say it is
taking a side. Recorded in V.5 [^2].
[[feedback_one_translator_two_texts]] [[feedback_quotation_connective_tissue]] high.

**FILED — R-179: THE *DAO DE JING*'s OPENING IS MISQUOTED IDENTICALLY IN THREE CHAPTERS, AND A FOURTH
CHAPTER HAS IT RIGHT.**

道可道，非常道。名可名，非常名 — *the way that can be **spoken** is not the constant way; the **name**
that can be named is not the constant name.* The rendering *"the way that can be **named** is not the
constant way"* welds line 1's subject to line 2's verb and produces a sentence the text does not
contain. It stands verbatim at **V.1:140, V.5:193, V.10:50**. **V.2 [^3] quotes line 2 correctly**, so
the volume holds both the right text and the hybrid, in four chapters, with nothing comparing them.
This is exactly what `tools/placement_sweep.py` was built for after V.1 [^3]: *a consistent reading
across chapters should be read as unchecked rather than clean*, because chapters copy each other and
agreement between copies is not corroboration. ⚠ Also: IV.8:76 romanizes the title *Tao Te Ching*
against Book V's *Dao De Jing*. Recorded in V.5 [^13]. high.

**FILED — R-180: *MITHYĀ* IS ATTRIBUTED TO ŚAṄKARA AND THE POSSESSIVE IS THE DEFECT.**

V.5:70 — *"**His** technical word for its status is *mithyā*, which is not *false*."* Śaṅkara's own use
is in *mithyājñāna*, "false cognition," synonymous with *avidyā* and *adhyāsa* through the
*Brahmasūtrabhāṣya* (Hacker 1950) — **false** in exactly the sense the sentence denies. The category
meaning *neither real nor unreal* is a different term, *anirvacanīya* / *sadasadvilakṣaṇa*, and it is
**post**-Śaṅkara. The Advaita literature says so against itself: the doctrine that *mithyā* means
indeterminable is *"not found or even implied in Śaṅkara's commentary."* The slogan carrying *jagan
mithyā* is *Vivekacūḍāmaṇi* v. 20, whose attribution modern scholarship doubts. ✅ The register-pair
*vyāvahārika*/*pāramārthika* IS his and the section's real point survives. **Repair: attribute the term
to the school and the pair to the man** — the same care V.1 [^4] already took for *waḥdat al-wujūd*.
Recorded in V.5 [^5]. medium.

**FILED — R-181: INDRA'S NET IS *ATHARVA VEDA* 8.8.6–8, WHERE IT IS A SNARE — AND THE OMISSION COSTS
THE CHAPTER ITS BEST PARAGRAPH.**

The net of Indra is Vedic, not Buddhist: a **weapon** of *"mighty size"* cast to entangle enemies and
envelop them in darkness, and the root of *indrajāla*, the standard Sanskrit word for **magic and
illusion**. Huayan did not invent the net; it *inverted* it. ⛔ The chapter calls it *"the best image
anybody has produced"* — carefully hedged as borrowed-not-adopted, and still skipping the borrowing
that matters by two thousand years. ★ **And a section whose whole business is that the Indian material
does not say the world is an illusion closes on an image drawn straight out of the vocabulary of
illusion, credited to the tradition that performed the inversion. That is a better instance of this
chapter's own thesis than anything the chapter says about the net.** ✅ Fazang 643–712, Wu Zetian
r. 690–705, Cook 1977 Penn State UP all check; the mirror-hall story is correctly given as
*"reportedly"* (the biographical tradition runs through Ch'oe Ch'iwŏn's *Life* of 904, and Chen 2007
treats its wonder-working as hagiography). Recorded in V.5 [^15]. medium.

**FILED — R-182: TWO SMALLER V.5 ROWS.**

(a) *"Nothing in the Dao De Jing recommends inertia"* (V.5:175) — a universal negative over an
eighty-one-chapter text the chapter gives no edition or translator for, and ch. 47 and ch. 80 are read
as recommending exactly that by readers who are not being careless. The narrower claim does the same
work. Same shape as R-172. (b) SN 22.59's canonical title is *Pañca Sutta*, "The Five";
*Anattalakkhaṇa Sutta* is a traditional title **not found in the Canon**, and *"the five ascetics"*
costs the chapter a better fact — they were already bhikkhus and stream-enterers, and per *Mahāvagga* I
this is the discourse **at which they became arahants**, which is a stronger warrant for
*"path-instruction rather than metaphysical census"* than the chapter's own. Recorded in V.5 [^11],
[^7]. low.

---

## THE V.x → V.1 SWEEP (Day 192 evening) — R-176's owed population, run

**R-176 predicted a bad population across V.6–V.11's twenty-plus reaches. IT IS NOT A POPULATION.
It is concentrated in V.6, and the boundary is sharp enough to name a mechanism.** All ~30 reaches
read against V.1's actual text, prose and apparatus. Six defects, four of them in one chapter.

**FILED — R-183: V.6:264 ATTRIBUTES TO V.1 A THESIS V.1 DOES NOT CONTAIN. FOURTH CONSECUTIVE CHAPTER.**

*"V.1 opened this book by saying that a tradition is a road and that the summit statements are the
part that travels, which is why they arrive stripped of everything that made them safe."* ⛔ **`travel`,
`strip` and `safe` appear ZERO times in V.1**, prose and all seven notes. `summit` appears five times
and every one is the metaphysical destination V.1 refuses — a different sense, which the sentence
conflates. The phrase *"summit statement"* exists nowhere in the corpus before V-06:258, six lines
earlier, where V.6 coins it fresh for Chaim of Volozhin's own worry. **V.6 coins a thesis and backdates
it to V.1 within six lines.** And (a) V.1's definition is *"A tradition is a perspective … **that is the
whole load-bearing claim of this book**"* — "road" is the book's title metaphor, not its definition, and
the swap drops the term that makes the census card apply. Held through a `refuter` pass that was told to
default to refuted. high.

**FILED — R-184: V.6 INHERITS V.1's PROSE AND NOT V.1's OWN FOOTNOTE — ON PRECISELY THE LINK THE
FOOTNOTE SINGLES OUT, IN THE CHAPTER THAT IS ABOUT THAT LINK.**

V.6:45–53 rests its opening disclaimer on *"one witness quoted back five times"* and concludes
*"Kabbalah is inside that family … it is not a separate arrival."* ⛔ V.1 [^7] names **Kabbalah as one of
the two weakest of the five**: *"Kabbalah's dependence is given as 'develops … in a world in contact with
both', which is contact and not descent"*, and *"the conclusion … survives at three or four links without
the two weakest, and the section does not say so."* **V.6 is the Kabbalah chapter.** ★ And the error runs
AGAINST V.6 — it surrenders a corroboration claim the evidence may entitle it to, which is R-177's sign
again in a second defect class. Nothing watches a chapter for being too hard on itself.
[[feedback_correction_does_not_reach_citers]] [[feedback_scrutiny_is_motive_shaped]] high.

**FILED — R-185: R-176's OWN PRESCRIBED REPAIR IS SCOPED TO THE WRONG ARTIFACT CLASS.**

R-176 says *"sweep every V.x → V.1 citation in Book V"* — chapters. But its own worked example lives in
**five artifacts**: `06-THE-SCAFFOLD.md:2425`, `book/DRAFT-LOG.md:6949`, `book/CROSSREF-ACK.md:31`,
`book/V-05:69`, and the queue entry correcting it. **Repair the chapter and the false attribution stands
in the scaffold and the draft log**, available to be spent again in Books VI–VIII. Same for R-183: the
V.6 thesis is in `06-THE-SCAFFOLD.md` too. ⚠ **HONEST LIMIT, because I nearly claimed more.** The
scaffold beat and the chapter ship in ONE commit (4a705b0; V.5's in 2f0a6d9), so git cannot establish
that the planning document *generated* the prose — a `refuter` asserted it did and that step is an
inference from genre, not evidence, and is dropped. The repair-scope finding does not need it.
[[feedback_repair_scoped_to_named_cause]] [[feedback_correction_does_not_reach_citers]] high.

**FILED — R-186: TWO CHECKABLE ORDINALS ABOUT THIS BOOK'S OWN STRUCTURE, BOTH WRONG.**

- **V.11:26** — *"V.1 said so in its ninth paragraph."* The perennialist ruling is V.1's **42nd** prose
  paragraph (51st block). V.1's ninth is *"A tradition is a perspective."* Wrong under every counting
  convention. **The claim it locates is TRUE**, which is what protects the locator — a correct sentence
  vouches for its own false footnote. [[feedback_fresh_number_vouches_for_stale_sentence]]
- **V.8:28** — *"arriving eighth among the ten sympathetic readings that sentence announced."* V.1 says
  *"Ten chapters of sympathetic reading follow this one"* = V.2–V.11. V.8 is the **seventh** of those ten.
  Chapter number read off as position-in-the-set. ★ **V.11 runs the identical arithmetic and gets it
  right** — *"Nine chapters of credit stand behind it"* (V.2–V.10 ✓), so this is not a convention. medium.

**FILED — R-187: V.9:159 MISQUOTES V.1 INSIDE A FRAME ADVERTISING VERBATIM FIDELITY.**

*"V.1 named this failure in advance and **named it precisely** — 'our agreement with the roster is not an
independent datum; it is the position doing the reading.'"* V.1:244 reads *"not a **fourth** datum
supporting the roster."* **"Fourth" is specific — three branches, and this book is not the fourth.
"Independent" generalises it and loses the count that made it bite.** The substance survives; the
quotation does not, and *"named it precisely"* is the aggravating clause. R-178's class.
[[feedback_quotation_connective_tissue]] medium.

**FILED — R-188 (minor): V.7:7 misreports V.1's list order.** *"They stood between a hesychast … and a
Mazatec curandera."* V.1:159–163 runs hesychast → **Vedic ascetic and Vajrayāna practitioner** → ritual
magicians → Mazatec curandera. The magicians' left-hand neighbour is the Vedic/Vajrayāna pair. low.

---

### ★ THE RESULT THAT IS NOT A DEFECT, AND IT ANSWERS A QUESTION CROSSREF-ACK LEFT OPEN

**V.7, V.10 and V.11's substantive reaches are ACCURATE — verbatim-accurate where they quote, and three
of them actively refuse V.1's authority:** V.7:34 *"spending a currency that was never minted for this"*;
V.10:209 *"**This breaks the test V.1 built**, and it is better to say so than to leave the crack for a
reader to find"*; V.11:193 *"V.1 declared the perennialist claim false and named nobody. **That was a
failure of this book's own rule**."* V.10:161 even audits its own borrowing rate — *"this is its third
outing, so it gets one sentence rather than a fresh performance"* — and the count checks out.

**The over-crediting stops exactly at V.7, whose opening section is titled *"What V.1's result does not
hand this chapter."*** Every clean chapter opens by bounding what it inherits. Every dirty one
(V.3, V.4, V.5, V.6) reaches back while AGREEING.

⛔ **This refutes CROSSREF-ACK's standing hypothesis** — *"Order of writing, not care, may be the whole
variable. Nothing measures that yet."* V.7, V.10 and V.11 have **no apparatus at all** and neither did
V.1 when they were drafted, so the writing-order variable is absent and they are accurate anyway.

**THE LESSON, and it generalises past this book: AGREEMENT IS THE UNREAD CITATION.** A chapter that must
draw a boundary against its source has to open the source to find the boundary. A chapter that merely
agrees quotes from memory — and memory returns the gist, which is the chapter's own thesis wearing the
source's name. **Predicts where to look in VI–VIII: not at the disputes. At the concurrences.**
[[feedback_scrutiny_is_motive_shaped]] [[feedback_briefing_manufactures_the_agreement]] high.

---

## V.6's APPARATUS (Day 192 evening) — the Kabbalah chapter, fifteen notes

**The chapter's central quotations are CLEAN** — both *Nefesh HaChayim* sentences are verbatim
Moskowitz, Gate III ch. 4, and all four reaches into Book I check. The damage is elsewhere, and it
has a single shape.

**FILED — R-189: THE CHAPTER'S BEST EVIDENCE DEPENDS ON AN INVERSION IT REPORTS AS A SHARPENING.**

V.6:115 — the *permeates*/*surrounds* formula is *"a formula Chaim takes from the Zohar and
**sharpens**."* ⛔ He does not sharpen it; he **inverts** it. Bezalel Naor: *"It is incontrovertible
that Rabbi Hayyim has stood the Zohar's terms 'memale kol 'almin' … and 'sovev kol 'almin' … on their
heads. **What for the Tanya is 'memale kol 'almin,' is for Nefesh ha-Hayyim, 'sovev kol 'almin,' and
vice versa.**"* ⛔ **V.6 quotes Shneur Zalman and Chaim of Volozhin nine paragraphs apart, uses both
terms for both men, and never says the terms swap between them.** ★ And the chapter's own argument is
that which side you stand on decides which description is available — it made that point about
vantages and missed it about its text. ⚠ Limit: R. Shelomo Fisher holds the reversal *"merely
semantics"*, so whether the swap carries theology is disputed; that the words swap is not.
Recorded in V.6 [^10]. [[feedback_field_keeps_name_swaps_referent]] high.

**FILED — R-190: THE DOCTRINE IS DATED FOUR CENTURIES EARLY, AND THIS BOOK HAD ALREADY RULED ON IT.**

V.6:179 — *"a tradition that stated it in the twelfth century."* The doctrine is **Lurianic** — 1572.
The chapter contradicts **its own line 43–44** (*"Kabbalah develops in Provence and Girona around
1200"*). ⛔ And the genuinely older attestations **invert the term**: the Midrash has the Ark holding
*"the shade of the Holy One … wherein He contracts (metzamtzem) His shekhinah"* and Nahmanides
(1194–1270) *"He contracted (tzimtzem) the glory itself … between the two cherubs"* — both
**concentration into** a place; Lurianic *tzimtzum* is **withdrawal from** one, *"quite the reverse
significance."* ⛔★ **AND `IV.8:498–503` ALREADY FILED THIS EXACT CORRECTION** — *"telescopes three
centuries … the contraction is tzimtzum, and it is Lurianic … because there was no contraction to be
before."* IV.8 caught three centuries; V.6, the Kabbalah chapter, then built four, after the ruling
was written down. ★ **A defect filed in an apparatus is filed in the one place the next chapter's
author does not read.** Recorded in V.6 [^11].
[[feedback_correction_does_not_reach_citers]] [[feedback_filed_defect_still_gets_rebuilt]] high.

**FILED — R-191: THE CLOSING QUOTES ARE NOT WHERE THE CHAPTER SAYS, AND THE CORRECTION IMPROVES THE
ARGUMENT.**

V.6:254 — *"Chaim of Volozhin nearly did not write the third gate. **He says so, in it.**"* ⛔ Both
quotations are his words **reported in the introduction written by his son Yitzchak**, about
publishing **the work**, not Gate III. Decisive: **there is no author's introduction to the *Nefesh
HaChayim*** — he never wrote one, the son wrote one in his place. R-187's class, where the clause
asserting provenance is the aggravating one. ★ **And the chapter's last sentence is undone by the
same fact**: it says the teaching survives because he wrote it down *"instead of leaving it in the
hands of people who would know when the student was ready"* — but it survives because he handed a
manuscript to his son on his deathbed, and the son, who opens *"I am at fault that I haven't rushed
to fulfill my father's words"*, published three years later. **The chain is one link longer than the
chapter says and the extra link is a custodian.** The argument gets better for the repair: the
transmission did not bypass the custodians, it survived them, narrowly, with an apology in the front
matter. Recorded in V.6 [^15]. [[feedback_artifact_states_its_own_roster]] high.

**FILED — R-192: THE CHAPTER REFUSES A PARTISAN TELLING AND ADOPTS THE OTHER PARTY'S RECONSTRUCTION.**

V.6:82–89 charges that *"the usual telling is a partisan simplification … the losing side's position
rendered by the winners"* and offers the *Ratzon*/*Atzmut* correction in its place. ⛔ That
correction is **Shlomo Elyashiv's, the Leshem** — who **subscribes to the literalist reading**
(Ricchi's *Yosher Levav*), holds it *"the only true understanding"*, and **cast aspersions on the
*Likkutim* at the end of *Bi'ur ha-Gra* to *Sifra di-Tzeni'uta***, a text attributed to the Gaon that
reads tzimtzum non-literally. The Gaon's position is disputed down to document authenticity. ★ **The
party the correction exonerates supplied the correction**, and this chapter, alert to that move
elsewhere, does not see it here. Recorded in V.6 [^6].
[[feedback_never_relax_the_gauge_that_caught_you]] high.

**FILED — R-193: THE PROOF THAT THE DISPUTE WAS "LIVE RATHER THAN TRIBAL" IS THE LITERATURE'S MOST
TRIBAL DATUM.**

V.6:91–94 offers Chaim of Volozhin's break with his teacher as *"the cleanest evidence that the
dispute was live rather than tribal."* ⛔ That break is prominently a **Chabad** claim, set out in a
letter of Rabbi Schneerson, and *"a point … which continues to rile Mitnagdim to this day."* Against
it: Avinoam Fraenkel's *Nefesh HaTzimtzum*, whose thesis is *"essentially no difference of theology
between the *Tanya* … and the *Nefesh ha-Hayyim*."* ★ **And Fraenkel harmonises using this chapter's
own device** — *"the distinction between the divine perspective and the human perspective"* — which
Naor objects *"should not be overused"*. Repair makes it stronger: *the tradition divides on whether
he broke with the Gaon* is better evidence of liveness than a settled break. Recorded in V.6 [^7].
medium-high.

**FILED — R-194: THREE SMALLER V.6 ROWS.**

(a) ⛔ *"in the *Tanya* and at length in *Shaar HaYichud VehaEmunah*"* — **these are not two works.
SHVH is Part Two of the *Tanya***; the sentence invents a second independent treatment. ✅ The locator
is otherwise right: the arguments are in SHVH **ch. 7**. (b) ⚠ *"a hand over your own head does not
count as a covering"* and *"the power to conceal and the power to reveal are the same power"* sit in
Shneur Zalman's voice and **I could not locate either as his**; the canonical form is *"no entity can
conceal itself from itself."* The chapter's imagery, unmarked — R-178's class, in the connective
tissue. (c) ⚠ The transmission clause gives the single-channel version (Luria → Vital → *Etz Chaim*)
in a sentence that says *"the transmission problem is on the surface of the material"*: the *Etz
Chaim* recension is largely **Meir Poppers'**, the *Shemonah She'arim* Shmuel Vital's, and the **Sarug
and ibn Tabul** transmissions differ **on tzimtzum specifically**. ★ The chapter's question is which
reading is authentic and it takes one party's recension as the text. Recorded in V.6 [^4], [^5], [^2].
medium.

**FILED — R-195 (low): FOUR ROUNDINGS, ALL IN THE SAME DIRECTION.** Luria's Safed tenure given as
*"about three years"* (standard: about two; he arrived 1569–70 and died July–Aug 1572) and his age as
*"thirty-eight"* (sources give 37–38) — both the ceiling of a range the chapter does not mention.
*"Consoled people for four hundred years"* — 454. And *"Volozhin, published 1824"* sits in a citation
slot: the *Nefesh HaChayim* was published in **Vilna**. Recorded in V.6 [^1], [^8], [^12].

---

### ★ THE DIRECTION FLIPS, AND THE COMPLEMENT IS THE HARDER CASE

V.5 established a rate: **every interval Book V states is too short, and every one costs the book
something** — errors nothing watches for, because no motive files a bug against a mistake that
weakens your own case. **V.6 breaks that rate and breaks it the other way.** Its two datable errors
(R-190's four centuries, R-195's tenure and age) both run **toward** the chapter's case, because an
older and longer-taught tradition is a weightier witness. R-184 runs against it. So Book V now holds
both directions, and they need different instruments: the against-me error has no motive keeping it
and merely wants looking at; **the flattering error has a motive keeping it, and wants a gauge.**
[[feedback_guard_built_in_the_feared_direction]] [[feedback_scrutiny_is_motive_shaped]]

---

## R-196: THE APPARATUS IS THIS BOOK'S FRESHNESS MECHANISM AND IT HAD NO GAUGE — *built, not filed*

Found by accident. **VII.7 [^9]** says Plotinus and tzimtzum run to *"eighteen occurrences across V.1,
V.3, V.6, V.9 and V.10."* The **chapter roster is exactly right** — those five and no others — which
is the signature of a real count. At the commit the note was written against the total was **17**.
Today it is **25**: V.1 gained seven Plotinus mentions and V.3 one, *after* the note was filed.
Nothing in VII.7 changed. The note went false while sitting inside the mechanism this book uses to be
right.

⛔ **And the retrofit is manufacturing this defect at ten to fifteen locators per chapter, one chapter
per session, with the revision pass — the event that moves every line in the book at once — next but
one in Clayton's sequence.** [[feedback_maintenance_advances_the_freshness_signal]]

**THE HAND, not a filing:** `tools/apparatus_rot.py` re-derives every parseable locator and count
claim inside every note against current disk. Quote-anchored locators are checked by searching the
cited chapter's **prose** for the quoted span and comparing its true line to the claim; count claims
are re-grepped. It prints UNPARSED on purpose — the notes it cannot read are coverage debt, and that
number going up is not good news.

★ **It found four failures on its first run and one of them was its own**: it had searched each
chapter's whole file, so a note quoting the span it rules on certified itself against its own text —
**R-175's defect, rebuilt inside the gauge written to catch apparatus rot.** Prose-only now.
★ **And it corrected a finding filed one breath earlier and hardened with a refuter.** R-183 said
*"`travel` … occur zero times in V.1"*. True of the word; **false of the root** — V.1:276
*"The traveller comes back"* and V.1:285 *"Cartographers we credit. **Travellers we part from.**"*
The finding survives and is stronger, because V.1's one cognate for V.6's thesis names the category
V.1 rejects. **A refuter attacks the conclusion; it does not re-run the grep.**
[[feedback_run_the_existing_gauge_first]] [[feedback_grep_derived_from_the_finding]] high.

---

## R-203 — `endnote_debt.py` cannot see a source across a relative clause, and drops it silently

**HIGH.** `scan_prose` counts a name as a source only in three shapes: a possessive before a
lowercase word (*Gibson's affordances*), a name immediately followed by an attribution verb
(*Searle argues*), or *according to / per / following X*. V.8 names **Michael Harner** once —
*"Michael Harner, whose* The Way of the Shaman *… , called the drumming* sonic driving*"* — with a
twenty-word relative clause between the name and its verb. He is not extracted, and he appears in
**none of the tool's printed exclusion classes**, because those list names that were found and then
rejected. A name never found is invisible to the mechanism built to make exclusions visible.

⛔ **The failure direction is the flattering one.** Had V.8's apparatus covered only the two names
the tool listed, the chapter would have gone **square with a cited source uncited**. The debt gauge
is a *reporting* gauge that has been read as a *preventing* one.

⚠ **Measured, so the size is not guessed.** A positive control against `BOOK-V-ROSTER.md`'s
hand-built NAMED lists found **no uncovered person in V.1–V.7** — all three candidates were false
positives of my own probe's last-token matching (V.1's Dionysius, V.6's Shneur Zalman, V.2's Aquinas,
which carries `[^5]` at the exact clause). So the apparatus is not full of holes. **The apparatuses
are clean because they were written by reading the chapters, not by working the gauge's list** — the
gauge has never been the thing catching them. [[feedback_self_generated_denominator]]
[[feedback_reporting_gauge_is_not_preventing_gauge]] high.

## R-204 — the V.8 sentence that turned my own search-null into an accusation

**HIGH, repaired in place.** V.8 said the settling experiment's *"absence after fifty years is itself
a small piece of evidence about who has wanted to run it."* The study was published **26 March
2026** — Aparicio-Terrés, López-Mochales, Díaz-Andreu and Escera, *Scientific Reports* 16:10204 —
by a university auditory-neuroscience lab with no stake in teaching the practice, i.e. exactly the
independence the chapter demanded. Three compounding faults, worst last: an absence needs no
citation, so **nothing in the apparatus would ever have been asked to support it**; it is
cutoff-as-null-space, assuming a live field has no instrument because none had reached me; and
**the grade did not depend on it** — *weak* survives, and the 2026 result arguably strengthens it by
locating the effect in the listener rather than the tempo. The sentence bought nothing and staked
the chapter's licence. [[feedback_cutoff_is_a_silent_null_space]]
[[feedback_guard_built_in_the_feared_direction]] high.

## R-205 — `apparatus_rot.py` audited one chapter of sixty, and never printed a zero

**⛔ HIGHEST. Repaired tonight; the lesson is the repair's shape, not the bug.** The audit loop read
`if "## NOTES" not in text: continue` — a case-sensitive literal. **Exactly one chapter writes the
heading that way: V.6.** Twenty-five write `## Notes`; thirty-four carry an apparatus under no
heading at all. So from its first run, every number this gauge printed — *"10 locators checked, 0
failing"*, *"UNANCHORED: 4"* — was **V.6's alone, read as the book's**.

⛔ **It survived because it never returned zero.** A plausible non-zero result reads as coverage. And
I wrote it forward: the Day-191 handoff's standing order said *"V.7 added 10 anchored and 0
unanchored; hold that standard."* **The ten were V.6's.** V.7's apparatus had never been seen.

**Three defects, one shape, found in sequence — each repair landing where the live path wasn't:**
1. the loop's literal (above);
2. `Chapter.__init__` held **the same wrong literal a second time**, so `self.prose` returned the
   whole file including the notes — silently disarming the self-certification guard that class's own
   docstring exists to describe;
3. `norm()` collapsed whitespace but not markdown emphasis, and `_index` **reimplemented norm()'s
   body inline** rather than calling it — so fixing `norm()` fixed the needle and left the haystack
   bolded. R-63's repair was already written, with a comment naming the family, in
   `endnote_debt.py`. **A defect class fixed in one prose gauge does not propagate to the next one
   written.** [[feedback_filed_defect_still_gets_rebuilt]] [[feedback_zero_needs_a_positive_control]]

**After repair: 32 locators checked (was 10), 4 failing.** One real — IV.10 [^3] cited V.9:225, span
at V.9:236, fixed. The other three are R-206.

## R-206 — quote-to-locator adoption is now the gauge's dominant error source

**MEDIUM, deliberately NOT fixed.** Three of the four post-repair failures are false positives with
one cause: a note carrying more locators than quotes has each quote adopted by the **nearest locator
by character distance**, and the nearest is often not the cited one.
- V.7 [^10] cites *IV.7:184–185* for its quote and *IV.7:190* for a separate unquoted claim. The
  quote adopts 190 and reports DRIFTED. **The note is correct.**
- V.5 [^13] quotes *"the name that can be named…"* while attributing it to **V.2's apparatus**, and
  quotes *"one of three independent arrivals…"* **expressly to deny it is V.1's phrasing**. Both
  adopt a neighbouring locator and report MISSING.

⛔ **The pattern is worth more than the fix: a note being more careful than the gauge scores worse.**
A note that quotes a phrase *in order to mark it as not-the-source's-wording* is indistinguishable,
to this heuristic, from a broken citation. Not relaxed tonight — the party a relaxation would
exonerate is the one proposing it — so the rule is instead **put the locator immediately after the
span it certifies**, and R-206 stays open until the adoption is scoped rather than loosened.
[[feedback_never_relax_the_gauge_that_caught_you]] medium.

## R-207 — a quoted string under 12 characters flipped quote parity for the rest of a note

**HIGH — FOUND AND FIXED Day 192.** `apparatus_rot.py`'s `QUOTE_RE` applied its 12-character minimum
**inside the scanner**: `[*_]*["“](?P<q>[^"”]{12,400})["”][*_]*`. A quoted string shorter than 12
characters therefore failed to match, `finditer` resumed at its **closing** quote, and that closing
quote paired with the **next opening** one. From that point in the note, every real span was read as
the connective tissue between spans and every piece of connective tissue was read as a span.

⛔ **It does not error. It prints confident ⛔ MISSING rows against quotations that are verbatim on
disk** — five of them, against V.9 [^14], which is how it was found; the trigger was the word
`"NEVER"` in the note's own heading. And it fails in **both** directions at once: false alarms on the
rows it prints, and a silent miss on every real span it swallowed.

✅ **Fix: the minimum now lives after the scan (`MIN_QUOTE`), so short quotes are consumed and
discarded and parity is preserved.** Positive control, run before any note was touched: all five
false rows cleared **with V.9 [^14] unedited**, and `checked` went **60 → 61** — one real span the
parity flip had been eating — while `weak` went 8 → 7. **The number moved the right way and not
merely down**, which is the check a gauge-fix owes and the one its author never walks.
[[feedback_zero_needs_a_positive_control]] [[feedback_never_relax_the_gauge_that_caught_you]]

★ **Second defect in this file in two days, and the pair rhymes.** R-205 was a case-sensitive literal
(`## NOTES`) that silenced 59 of 60 chapters. R-207 is a length bound in the wrong place. **Both are
one-token errors in a matching rule, both produced plausible non-zero output, and neither could fire
an alarm about itself.** A gauge's own matching layer is the part nothing downstream can audit.

## R-208 — V.9 quotes its own book in the form it had BEFORE its apparatus was written

**HIGH — THE CLASS, NOT THE THREE INSTANCES.** V.9 was drafted last in Book V (git first-commit
8 Aug: V.3 14:53, V.8 18:32, **V.9 18:58**) and it borrows from its neighbours three times. **All
three borrowings take the pre-correction form.**
1. **V.1's headline, downgraded by V.1's own note.** V.9 quotes *"one witness quoted back five
   times"* (V.1:131) verbatim — and V.1 [^7] already says the chain *"survives at three or four"*
   (V.1:381) links, calls the five an inference rather than a finding, and files an explicit **Owed**.
   V.9 then *escalates* it to *"several million times."*
2. **V.1's word swapped, italics kept.** V.9 prints *"not an **independent** datum"* as V.1's words;
   V.1:244 says *"not a **fourth** datum"* — an arithmetic word that means something only inside a
   count of three branches, generalised because V.9 has one branch. The generalisation is *correct*;
   the italics make it a fabrication.
3. **A "never" refuted 26 minutes earlier.** V.9: the two-frames rule has been *"run at full cost
   never."* **V.8:177–182 runs it at full cost** — names the divergence, makes the pick, ranks the
   reasons, refuses to spread the load to look broader. V.3:128 ran it too.

★★ **One mechanism, and it is not staleness — every one of these was false when it was typed.** The
corrections all existed on disk, in the same book, some of them minutes old. **A chapter drafted last
quotes the book as it stood when the drafter last *read* it, and an apparatus is exactly the layer a
drafter does not re-read.** [[feedback_correction_does_not_reach_citers]]

⚠ **LIVE PREDICTION, and it is falsifiable: V.10 and V.11 were drafted after V.9 and should do the
same thing to V.9 and to each other.** If their apparatuses come back with no pre-correction
borrowing, this class is refuted as a general rule and demoted to three coincidences in one chapter.
**Do not write the V.10/V.11 notes expecting to find it.** [[feedback_briefing_manufactures_the_agreement]]

## R-209 — "the manuscript has never been met cold" is FALSE in the published book as of Day 195, 10:32, and it ships Monday

**HIGH — AND IT IS TWO DIFFERENT DEFECTS UNDER ONE SENTENCE, which is why "delete it" is the wrong repair.**

At **10:32–10:34 on Day 195 (2026-08-14)** Clayton landed three whole-draft outside reads — GLM, Gemini,
Grok (`review/`). None of the three watched the book being written. C-02 says they did.

1. **`book/C-02-why-it-is-not-finished.md:141` — FALSIFIED, flatly.** *"Every reader it has had — every
   one — read it while it was being written"* and *"You are the first instrument the book has had that
   isn't compromised by having watched it grow."* Three instruments now precede the reader. The published
   sentence rests its entire weight on the **watched-it-grow** condition and nothing else, and three
   readers break exactly that condition. This is in the **shipped body**, and the PhilArchive upload is
   Monday.
2. **`REVISION-QUEUE.md:3047` — CONCLUSION SURVIVES, STATED PREMISE DOES NOT.** The row grounds the claim
   on *"the condition every reader this book has ever had shares — Fable, Opus, me"*: continuous exposure
   across drafting. **That roster is now stale.** But two paragraphs later the same row states the
   *independent* disqualification — ⛔ *"Do not pay this with another model read… It is a person with no
   stake, reading for their own reasons, who can stop"* — and **that one holds against all three new
   reads.** So the debt is NOT discharged; only the reason given for it is. Re-ground the row on the
   disqualification that still stands and stop citing continuous exposure, which is now a premise a
   reader can check and refute. [[feedback_alarm_survived_by_an_unrelated_choice]]

★ **The repair is not a retraction — it is stronger than what it replaces.** Under the Day-195
body-repair policy (repair the body, display the repair in the note), C-02 says what actually happened:
the book was met cold on the day it stopped being written, by three readers, and here is what came back.
A coda that reports its own first cold reads beats a coda that claims not to have had any.

⚠ **The book may not use "it was only a model" as the escape hatch.** Book IV forbids it, the volume is
co-authored by one, and a reader who has just finished III.5 will spot the move. If the sentence is
narrowed to *human* readers it has to say so in the word, and then own that its own no-NPC rule makes
that narrowing a claim it must defend rather than assume.

★ **TRIGGER: before the PhilArchive upload. It fires now.** Not "at revision" — the falsified sentence
is inside the artifact being uploaded, and upload is the event that makes it permanent and citable.
[[feedback_superseded_not_stale]] small.

## R-210 — "### IV. What exists, and where" names four instruments, gives no *where*, and ships none of them

**HIGH — and it is the ONE finding in the Day-195 outside reads that the book had not already made about
itself.** GLM: *"The book has a claims register with 30 entries, but it is not part of the published book.
The book refers to it, but the reader cannot check it. This is a version of the problem the book diagnoses
in others: a claim that cannot be checked is not a claim."*

**Checked, and it is worse than GLM stated — GLM found one document; the promise names four.**
`book/C-01-what-this-is.md:98–111`, section heading *"What exists, and where"*, promises the reader **the
claims register · the instruments · the scaffold and architecture · the revision queue**, on the explicit
argument that *"a claim about a book is worth more when the thing that measured it is available to run."*

- `book/compile_pdf.py:2` — *"Compile the book (**chapters + coda only**) into a single PDF."* The shipped
  PDF contains **zero of the four.**
- Grepped `C-01` and `C-02` for a URL, repo name, DOI, Zenodo or PhilArchive pointer: **none.** A section
  titled *and where* answers the *what* four times and the *where* not once.

⛔ **This is the book's own standard, turned on the book, by a reader using the book's instrument.** GLM
reached it without being told, which is what makes it the only independent finding in ~8,700 words.

**Cheap. One paragraph and a resolvable pointer** — repo URL, or a Zenodo DOI for the apparatus bundle
minted alongside the PhilArchive deposit, so the pointer survives the repo moving. ★ **TRIGGER: before
the PhilArchive upload**, because the deposit is the moment the unroutable promise becomes the permanent
one. [[feedback_absent_artifact_is_not_absent_reader]] small.

## R-211 — the coda functions as a briefing document, and the Day-195 reads measured it

**MEDIUM — a finding about the INSTRUMENT, not the book. Filed so the next outside read is not spent the
same way.**

Three reads, **8,749 words** (GLM 3,321 · Gemini 2,286 · Grok 3,142), against **56 open rows** in this
file. Every stated weakness was traced by hand to its source. The count:

- **Traceable to the book's own self-report — 13 of 14.** GLM quotes C-02:136's *"18 of this volume's 44
  cards"* verbatim and its numbers are correct. Gemini prefaces the vacancy defect with *"As acknowledged
  in Books IV and VIII."* Grok grounds over-attribution in *"the authors' declared bias."* Gemini's four
  tensions are four-for-four self-reports (*"the authors candidly admit"*, *"the text openly concedes"*).
- **Independent — 1.** GLM's unpublished apparatus, now **R-210**.
- **Named an open queue row — 0 of 56.** Zero `R-nnn` mentions across all three files.

★ **The mechanism, and it is not that the readers were lazy — GLM in particular is demonstrably careful**
(three checkable claims spot-checked: the 18/44, the register's C1–C30 count, and the register's absence
from the published book — **all three correct**). **C-02 hands a reader the list of acceptable criticisms
before they have formed their own.** A self-criticism section is a briefing document with better manners,
and the returned reviews are what a briefed reader produces: agreement, graded.
[[feedback_briefing_manufactures_the_agreement]]

⚠ **The scores are the tell, not the praise.** 7.8 / 9.2 / 9.0. The two nines scored the **method**
(Gemini: *Epistemological Rigor 9.5*) — which is the property C-02 flatters. GLM alone scored the
**evidence**, and GLM alone answers *will it stand* with *"probably not, as a systematic metaphysical
treatise."* **The outlier is the one that checked.** [[feedback_overstated_self_criticism]]

**OWED: the next outside read runs against a copy with `C-02` withheld** — chapters and C-01 only, coda
supplied afterward for a second pass. Costs one file operation and converts the read from a graded
agreement into a real instrument. ★ **TRIGGER: when the next outside read is commissioned** — this row is
the specification for it, and it does not block the upload.

⛔ **AND THE STANDING RULE AT LINE 3047 IS UNCHANGED BY ALL THREE.** *"Do not pay this with another model
read."* Three arrived at once; the cold-read debt is **not** discharged. Whatever these are worth, they
are not the person with no stake who can stop. small.

---

# DAY 195 — THE OUTSIDE-READ CONSOLIDATION

*Clayton's instruction, Day 195 midday: **"consolidate everything into that revision queue so we have a
single source of truth for the process."** Six outside reads now exist in `review/`. Before this section,
**two of the six had never been rowed at all** — Fable's Day-193 whole-draft read (committed as a document
on Day 193, its findings never converted) and the Day-195 ghost-Opus pair (read this morning, classified,
not filed). This section closes that gap.*

⚠ **WHAT THIS SECTION IS AND IS NOT.** It is a hand-built map from each read's actionable items to a row.
It is **one pass, by the party with an interest in the count being small**, and nothing derives it —
[[feedback_one_pass_mapping_is_unverified]]. The mapping verdicts (`COVERED` / `WIDENED` / `NEW`) were
reached by grepping this file for each item's load-bearing noun and reading the hits; an item marked
`COVERED` that turns out to be covered by a row about something adjacent is the expected failure mode.
**Re-derive before trusting any `COVERED` verdict to mean the debt is held.**

## ⛔ THE FINDING THE CONSOLIDATION ITSELF PRODUCED — R-209 CITES A POLICY THAT DOES NOT EXIST

`REVISION-QUEUE.md:4913`, written by me at ~11:15 this morning, reads: *"Under the Day-195 **body-repair
policy** (repair the body, display the repair in the note)…"* — and grounds R-209's repair on it.

**Grepped the whole repo for that policy: one hit. That line.** No ruling, no register entry, no row, no
commit. It is a decision I made inside a Telegram answer and then cited back as settled state, in the row
that depends on it, two hours later. [[feedback_decision_made_in_channel_never_reaches_state]]

★ **And it is the single most load-bearing undecided item in the whole revision.** Fable Day-193 opens its
priority list with it — *"Before anything else in the revision pass: a single policy decision, then one
sweep"* — and the ghost audit reaches the same joint independently from the opposite side (§3.5: the
changelog defence *"proves something narrower than it is used for"*). **Two of the three heaviest reads
agree the policy decision comes first, and it had no row.** It is now **R-212**, and it blocks.

## THE MAP — every actionable item in all six reads, and where it now lives

| read | item | verdict | row |
|---|---|---|---|
| Fable D193 | (a) body/apparatus divergence + stale-reference sweep | **NEW** | **R-212** |
| Fable D193 | (b) COMPLEMENTS field, 18 of 44 | COVERED | R-136 *(finding; repair owed on its own trigger)* |
| Fable D193 | (c) the actualist opponent | COVERED | R-21 *(Fable supplies both halves of the answer — annotate, do not re-file)* |
| Fable D193 | (d) workshop apparatus in a reader's edition | **NEW** | **R-227** *(the decision)* + **R-221** *(the production defect)* |
| Fable D193 | (e) Class VII evidence line, VIII.3 | **NEW** | **R-223** |
| Fable D193 | (e) unmeasured quantities — grimoires, V.11 amplifications, alchemy superlative | **NEW** | **R-224** |
| Fable D193 | (f) summation arithmetic V.10/V.11 + pointer sweep over shipped prose | **NEW** | **R-225** |
| Fable D193 | (g) Book VII's primary-check queue | **NEW** | **R-226** *(joins R-144's trigger class)* |
| Fable D193 | (h) small items ×8 | **NEW** | **R-232** *(each with its own trigger)* |
| Fable D193 | §5 Santa/corporation stitch | COVERED | R-28 *(Fable supplies the missing sentence — annotate)* |
| Fable D193 | §6 Book I's cold-reader forward pointer | **NEW** | **R-228** *(converges with ghost §7.1)* |
| Fable D193 | §4(d) *Dao De Jing* opening in three chapters | COVERED | R-179 |
| ghost audit | §1.2 Wilber orientation in the Coda | **NEW** | **R-231** *(distinct from R-19, which is `Wilber`=0 in `03`)* |
| ghost audit | §1.3 no index, no glossary, no bibliography | **NEW** | **R-222** |
| ghost audit | §2.2 under-attribution induction — reference class + counterexamples | **WIDENED** | **R-213** *(second, independent attack on R-3's joint)* |
| ghost audit | §2.3 non-sloping floor vs grading stake | **NEW** | **R-216** |
| ghost audit | §2.4 complement law's middle clause; existence ≠ reachability | **NEW** | **R-219** *(binds R-136)* |
| ghost audit | §2.5 *violates* in step 3 | **NEW** | **R-230** |
| ghost audit | §2.6 stipulation exceeded between II.4 and VII.2 | **NEW** | **R-220** |
| ghost audit | §3.1 audit coverage uneven, described as uniform | **NEW** | **R-215** |
| ghost audit | §3.2 COMPLEMENTS as a removed guard, not a naming problem | **WIDENED** | R-136 + **R-219** |
| ghost audit | §3.3 staleness generated at the repair rate | **NEW** | **R-212** *(the sweep half)* |
| ghost audit | §3.4 V.1 referenced 190×, fn7 debt unpaid | **NEW** | **R-233** |
| ghost audit | §3.5 known-false prose shipped with the fix in a note | **NEW** | **R-212** *(the policy half)* |
| ghost audit | §4.2 the apparatus is rhetoric and only instrument is declared | **NEW** | **R-217** |
| ghost audit | §4.3 382 production tokens; `[[feedback_*]]` soft-hyphenated in the PDF | **NEW** | **R-221** |
| ghost audit | §5 "the source" — 137 occurrences, never named | **NEW** | **R-214** |
| ghost audit | §6 authorship disclosure does not propagate to C.2 §IV | **NEW** | **R-218** |
| ghost audit | §7.1 Book I's register abandoned without transition | **NEW** | **R-228** |
| ghost audit | §7.2 template phrases at tic density | **NEW** | **R-229** |
| ghost essay | §V the Nishida problem | **DEFERRED — read not yet mined** | *see the coverage note below* |
| GLM D195 | unpublished apparatus | COVERED | R-210 |
| GLM/Gemini/Grok | the read as an instrument | COVERED | R-211 |
| GLM/Gemini/Grok | C-02's cold-read claim falsified | COVERED | R-209 |

⚠ **COVERAGE THIS SECTION DOES NOT CLAIM.** The ghost **Critical Assessment** (233 lines) is a placement
essay, not a defect list; its §V (the Nishida problem) and §III (the shelf) contain claims about the book's
position in a literature that may or may not imply work. **They were not mined.** Nor were the
**Day-188 midpoint audit** or **OPUS-DAY189-BOOK-V-READ** re-swept — those were rowed at the time and are
assumed held, which is an assumption and not a measurement. Three reads fully mined, two partially, one not.

## ★ THE ONE PLACE TWO INDEPENDENT READS CONVERGED

Fable (Day 193, §6) and the ghost audit (Day 195, §7.1) reached **Book I's register break** by different
routes and neither read the other. Fable: *"a reader who doesn't reach II.4's 'this is a definition' may
put the book down holding exactly the wrong object."* Ghost: *"Book I is a different book… the register is
abandoned without transition."* **Convergence between reads that could not brief each other is the only
signal in this pile that is not vulnerable to R-211's briefing mechanism** — C-02 hands a reader the list
of acceptable criticisms, and every other item here is either on that list or reachable from it. This one
is not. It is **R-228**, and its evidence grade is the highest of anything filed today.

---

## R-212 — ✅ **PAID DAY 195 — RULING 177 IS WRITTEN AND THE SWEEP HAS RUN. GATE 1 IS MET.**

**Ruling 177, `00-ARCHITECTURE.md`:** *(ii) released edition — repair the body, mark the repair, keep
the archaeology in the note.* Scope stated as a two-condition test (load-bearing AND overturned by
this project's own apparatus), so it is a rule rather than a mood.

**TWO OF THIS ROW'S OWN PREMISES WERE FALSE, AND BOTH WERE FALSE IN THE SAME DIRECTION — OVERCHARGING.**
[[feedback_filed_defect_misprices_its_own_subject]]
1. *"what Book V already does three times"* — **measured: six times, across two books.** `IV-02` [^2],
   `IV-03` twice, `V-01` [^2], `V-01` [^3], `V-02` [^7]. The row undercounted its own supporting
   evidence by half, and mislocated the split as Book-V-versus-IV.10 when Book IV is on both sides of it.
2. *"and what the Coda currently contradicts"* — **the Coda does not contradict it.** The changelog
   defence lives at `IV-10` [^2] and is doing narrower work: it mourns a *destroyed measurement*, which
   is a real and separate problem. C.2 §I argues that a mark is a dated act rather than a standing
   property, which is **compatible with (ii) and in fact argues for it.** Grepped all 69 chapters for
   any other archive-edition defence: **one hit, `V-08`:318, and it says the opposite.** The gate had
   been asserting a Coda-level contradiction that is not in the Coda.

**THE SWEEP — ELEVEN SITES ACROSS EIGHT FILES, ALL REPAIRED, EACH MARKED IN ITS OWN NOTE:**

| # | site | what was standing in the body | source |
|---|---|---|---|
| 1 | `IV-10`:230–236 | a **fabricated quotation inside an accusation** — a sentence attributed in bold to the source, which the source never wrote | list |
| 2 | `06`:1600–1612 | **the generator.** The heading asserted the entry carried the clause *in two forms*; one form was ours | list |
| 3 | `V-11`:216 | V.1's fourth proposition given as *the failure of every name*; it is *has no outside*, and the swap lost the cut | list |
| 4 | `V-11`:217 | the convergence spent at pre-audit strength — *no shared vocabulary*, when shared vocabulary is the mechanism V.1 documents. Now says **three, not six** | list |
| 5 | `V-11`:105 | III.6 quoted with the invented clause *under the threshold* | list |
| 6 | `V-09`:117,125 | *"run at full cost never"* — false when typed; V.8 ran it 26 minutes earlier | list |
| 7 | `V-09`:161 | an adapted sentence set in italics as V.1's own words | list |
| 8 | `V-10`:8–25 | **four silently closed ellipses**, one of them replaced by a comma, which asserts continuity rather than merely dropping it | list |
| 9 | `V-03`:290 | the closing tally counting a survival the body had already downgraded | list |
| 10 | `V-07`:91,221 | ⛔ **NOT ON THE LIST** — *under the threshold* again, twice, in a chapter the sweep never named | **grep** |
| 11 | `07`:1312 | ⛔ **NOT ON THE LIST** — the **claims register** carrying the same V.1 misquotation the prose was being repaired for | **grep** |

★★ **THE SHARPEST THING THE SWEEP FOUND IS AT `V-07` [^5], AND IT IS ABOUT VERIFICATION ITSELF.** That
note certifies the passage *"✅ III.6, verbatim on both halves"* **and quotes III.6:207 correctly** —
*over time* — while the body six lines above it printed *under the threshold*. **The check ran. The
check passed. The check quoted the true text. And it never reached the sentence it was certifying.**
A green tick sitting beside an uncorrected error, with the correct string stored in the same note.
[[feedback_gauge_and_responder_mis_specified_as_a_pair]] · [[feedback_correction_does_not_reach_citers]]

⚠ **AND THE LIST WAS 75% COMPLETE.** Six chapter sites named by six outside reads, all six real; two
more found only by grepping the repaired strings across the whole tree — including **the claims
register**, which the list covered only as *"then the planning files."*
[[feedback_grep_derived_from_the_finding]]

**THE GAUGE DELTA, RECORDED AS THE SATISFACTION TEST REQUIRES — AND IT IS ZERO.**
`tools/edition_scheme_sweep.py`, before and after all eleven repairs — of which **six are in the
six drafted chapters the gauge actually reads** (`IV-10`, `V-11`, `V-09`, `V-10`, `V-03`, `V-07`);
`06` and `07` are outside its 67-chapter scope by construction:
**EDITION-NAMINGS 81 → 81 · EXTERNAL LOCI 34 → 34 · EXPOSED PAIRS 72 → 72.**
★ **That zero is the result, not a failure to measure.** Ruling 177 declared this limit in advance —
the sweep counts edition namings and exposed pairs, and **nothing in this tree can detect a fabricated
quotation absent the source.** The gauge measures the sweep's collateral, not its subject. Eleven
repairs moved it by nothing, which is the predicted reading and now an observed one.
⛔ **Consequence, stated so it is not mistaken for a clean bill:** there is **no instrument** standing
behind this class of defect. Every one of the eleven was found by a human or model reading the source
against the page. The gate is met because the named sites are repaired, **not** because anything
certifies that no twelfth site exists. [[feedback_zero_needs_a_positive_control]] · [[feedback_partial_delivery_beats_no_gauge]]

*The original row, kept below because the ruling answers it point by point.*

## R-212 (as filed) — THE BODY-REPAIR POLICY, AND THE SWEEP IT AUTHORISES

**⛔ BLOCKING — the first item of the revision pass, and nothing else in the pass can be scoped until it is
decided.** Fable's #1, the ghost audit's §3.5 and §3.3, and the phantom citation at `:4913` are one item.

**The decision owed, stated as a fork so it can be settled rather than drifted:**

- **(i) Archive edition** — body stands as written, notes carry the correction. What the book currently
  does, defended at C.2 §I: *"a finding and its fix in one commit leave a reader no way to check the
  finding."*
- **(ii) Released edition** — load-bearing body claims the apparatus has overturned are **repaired in the
  prose, with the repair marked** (the book already owns the idiom: *"this read X until Day N"*); the notes
  keep the archaeology.

⛔⛔ **AND THE FORK IS ALREADY DECIDED ON THE PAGE, IN ONE DIRECTION, WITHOUT ANYONE DECIDING IT.** Grepped
the shipped chapters for the idiom rather than assuming: **Book V has executed option (ii) at least three
times.** `V-01` fn2 — *"⛔ This read 'around 1300' until Day 192 and was out by roughly two decades"* — and
**the body at `V-01`:24 now reads "in the thirteen-twenties."** Same shape at `V-01` fn3 (*"This read
'Paris' until Day 192, and so did V.2 and V.3"*) and `V-02` fn7. **The body was repaired and the note kept
the archaeology — which is exactly option (ii), performed, three times, and never written down as a rule.**

★ **So the true finding is not "undecided." It is SPLIT, and nobody noticed the split.** Book V repairs
bodies and marks the repair; IV.10 leaves a fabricated quotation standing and defends it at C.2 §I as
principle. **Two incompatible policies are running in one volume, and the one defended in the Coda is the
one the book does not follow in Book V.** ⚠ That also means the ghost audit's §3.5 is understated: it
argues the changelog defence is over-extended, not knowing the book already declines that defence three
times. [[feedback_configuration_vs_maintenance]] · [[feedback_two_guards_only_independent_in_the_untested_case]]

⛔ **The ghost audit's refutation of (i), which is the strongest single paragraph in the six reads and must
be answered rather than cited past:** the changelog argument *"argues for a changelog. It does not argue
for leaving a fabricated quotation in the running text of a published volume with the correction 200 words
below… There was a third option — repair the prose, record the repair — and it was not taken."*

⚠ **And the specific case that decides it.** IV.10's body quotes its source's second sentence and calls it
*"worse"*. Fn6 shows **that sentence is not in the source at all.** The chapter's indictment of its source
is aimed at a sentence the chapter's own scaffold fabricated. Whatever the general policy, **that one
cannot ship** — it is not an interesting standing error, it is a fabricated quotation inside an accusation.

**THE SWEEP the policy authorises**, in Fable's priority order, which is also the load order:
IV.10 body → V.11 fn26/fn27 (the Katz cut rebuilt on three branches; V.1's fourth proposition restored to
*"has no outside"*) → V.9's italicised adapted quotation (fn15) and its false *"never been cashed"* (fn14)
→ V.11's III.6 quotation with the invented *"under the threshold"* clause (fn14) → V.10's four silently
closed ellipses → V.3's closing tally (fn10) → **then the planning files**, because the class is
generative: `[[feedback_correction_does_not_reach_citers]]` fires five times and IV.10's own note says the
retrofit *"will keep handing it forward to every chapter drafted from it."*

★ **TRIGGER: BEFORE THE PhilArchive UPLOAD, and before any other revision-pass row is worked**, because
every other row's scope depends on which edition this book is. ⛔ **The policy gets written as a ruling in
the register — not decided in a chat and cited back**, which is the defect that produced this row.
[[feedback_decision_made_in_channel_never_reaches_state]] · [[feedback_carrier_is_narration_not_state]]
**large.**

## R-213 — THE UNDER-ATTRIBUTION INDUCTION'S REFERENCE CLASS IS UNDECLARED AND ITS COUNTEREXAMPLES ARE UNENGAGED

**★★ HIGHEST PRIORITY, tied with R-215. This is a SECOND and INDEPENDENT attack on R-3's joint** — R-3
says the induction is *circular*; this says the historical premise is *false as stated*. Both can be true
and the repair differs. **Do not fold this into R-3 and consider it held.**

IV.1's standing bias rests on: *"there is no episode in the record of a false attribution being discovered
and repaired. There are many of the reverse."* The ghost audit's counterexamples: **vitalism · celestial
intelligences · demonic aetiology of illness · the witch prosecutions · the pathetic fallacy generally.**

⛔ **The witch count is the one that hurts.** The book *"mentions witches 34 times and never once in this
connection."* An over-attribution of intentional causal power with a body count, present in the text 34
times, invisible to the principle it refutes.

⛔ **And the systemic form: the book's own instrument catches this error elsewhere.**
`[[feedback_self_generated_denominator]]` fires against V.7's *"it is most of the record's bulk"*, against
Dee's library figure, against a lab replicating itself. **It was never turned on the one claim that
pre-authorises every generous reading in a 63,000-word census.** The words *selection effect*,
*survivorship* and *reference class* occur **zero times in 314,000 words**; *anthropomorphism* once.

⚠ **The in-chapter counterexample, which is the sharpest part.** VII.2 argues the cost of over-attribution
is *"you were kind to furniture"* — and twelve pages later argues that corporate moral personhood is a
category error with real institutional consequences. **The chapter supplies its own counterexample to its
own asymmetry and does not notice.** VII.2's limiter (*"the asymmetry bites on the steep uncertain
stretch"*) does not repair it: the corporate case **is** on the steep uncertain stretch.

**The repair is not abandonment** — the asymmetry argument for irreversible cases is sound. It is: **state
the reference class · engage the disenchantment cases · price over-attribution above zero · reconcile with
the book's own corporate-personhood argument.**

★ **TRIGGER: before any subsequent release, and before the Book IV revision pass opens** — it decides how
much of Book IV the other IV rows are editing, the same argument R-15 makes for itself.
[[feedback_self_generated_denominator]] · [[feedback_guard_built_in_the_feared_direction]] **large.**

## R-214 — "THE SOURCE" OCCURS 137 TIMES AND IS NEVER NAMED, IN A BOOK WHOSE RULE IS UNIVERSAL

**★★ HIGHEST PRIORITY. The ghost audit calls it *"the finding that most damages the book, because it
falsifies its central methodological virtue"*, and it is the finding no previous read made.**

Distribution: **Book IV 31 · Book VII 45 · Book VIII 43.** What the unnamed source supplies: **Book IV's
entire structure** (the book's own audit: *"the chapter list follows the source's tier list almost exactly,
entry for entry"*) · **the definition of love in VII.6** · **the closing instruction of the practice
volume** (VIII.7's oscillation) · **the coherence definition**, quoted from *"05 §3a"*.

The book **corrects** it, **diffs** against it, **cites it by line number** (`work/perspective-v1-fulltext.txt
L2409-2447`), and **audits its own fidelity** to it. It never names it.

⛔ **Against the method:** the same volume takes 40 words to state exactly what it takes from Lewis and
which of Lewis's own words marks the cut — and does the same for the **thirty further predecessors** §5
names, Tillich through Dee. C.1 §V
says the register rule *"incurred a debt, and this is where it is paid"*, then pays Tolkien, Watts and
Wittgenstein, and not this.

⚠ **The "it is an earlier volume by us" defence is pre-refuted and the refutation should be read before
reaching for it.** (1) No prior volume is named in 314,000 words; *"The Corpus"* appears **once**, on the
title page, unexplained. (2) The book is otherwise written standalone, addressing a reader arriving cold.
(3) **Decisively: it does not matter.** A book that corrects, quotes, inherits architecture from and
audits its fidelity to a source owes that source a name **under its own rule**, stated as universal,
applied to thirty-one and suspended for one. *(Thirty-one = Lewis plus §5's thirty; the audit's own verdict
line says "thirty", counting the list and not Lewis. Immaterial to the finding, stated so the number in
this row can be checked against the source without looking like a discrepancy.)*

★ The book states the sentence that convicts it, twice — V.3's note: *"The characteristic debt is not an
unnamed source — it is an inherited one"*; IV.10: *"an inheritance you can see is an influence, and an
inheritance you can't see is…"*

★ **TRIGGER: BEFORE THE PhilArchive UPLOAD.** The deposit is what makes an unnamed dependency permanent
and citable. **small to write, and the decision is Clayton's** — naming it means naming the Perspective
v1 corpus and its authorship in print. [[feedback_agreement_is_the_unread_citation]] **small / decision.**

## R-215 — THE AUDIT'S COVERAGE IS UNEVEN AND THE FRONT MATTER DESCRIBES IT AS UNIFORM

**★★ HIGHEST PRIORITY, tied with R-213. A claim the book makes about ITSELF, refuted by counting its own
marks.**

| Book | ⛔ | ⚠ | ★ | ✅ | notes/10k | flags/note |
|---|---:|---:|---:|---:|---:|---:|
| I | 0 | 0 | 0 | 0 | 0.0 | — |
| II | 0 | 5 | 0 | 0 | 15.3 | 0.14 |
| III | 0 | 24 | 8 | 0 | 16.3 | 0.70 |
| IV | 26 | 61 | 48 | 11 | 19.1 | 1.21 |
| V | 86 | 99 | 73 | 89 | 38.6 | 1.40 |
| VI | 0 | 16 | 7 | 0 | 17.9 | 0.34 |
| VII | 0 | 25 | 7 | 0 | 17.7 | 0.34 |
| VIII | 20 | 29 | 29 | 0 | 13.7 | 1.70 |

⛔ **Book VII — 93 footnotes, the ethics, which the book calls *"the hardest chapters in the work"* —
carries ZERO ⛔ and ZERO ✅.** Not one claim in the ethics is recorded as verified against a primary source
at the standard Book V applies **89 times**.

⛔ **C.1 asserts it globally:** *"Every claim in it says what grade of ground it stands on… The instruments
print their own limits."* That describes Books IV, V and VIII. It does not describe II, VI and VII, **and
the reader is not told.** ★ *"The natural reading of an unflagged chapter, in a book that flags obsessively,
is that it passed. The correct reading is that it was not put through."*

**Fork:** disclose the actual coverage in C.2 §IV, **or** extend the audit to II, VI, VII. ⚠ The disclosure
is cheap and the extension is honest; **taking the cheap one is itself the R-217 pathology** — converting
an unfixed defect into a display of rigour. Decide it knowing that.

★ **TRIGGER: with the C.2 §IV rewrite, alongside R-218 — and BEFORE the upload if the disclosure fork is
taken**, because C.1's global claim is false in the shipped artifact.
[[feedback_absent_from_the_table_is_not_a_demand]] · [[feedback_bucket_derived_by_subtraction]] **medium.**

## R-216 — ✅ **PAID DAY 195 — RULING 179. GATE 3 IS MET, AND THE SATISFACTION TEST WAS THE THING THAT MADE IT REAL.**

★ **This row is the argument for writing satisfaction tests before the work.** Its test was *a worked
case where the two answers differ, not a paragraph asserting they do* — and a paragraph is exactly
what this would have got otherwise, because a paragraph is what the objection invites.

**VII.3 gains a section — *Does the floor have a bottom?*** — with the objection stated at full
strength first, then: **the minimum named** (obligations whose grounds are binary, not graded —
over/through, carrier-annihilation, the null-space theorem: *content grounded in a binary fact cannot
grade, because there is nothing for it to grade with*); **the worked case**; and **the falsifier in
the body**, where a reader meets it, rather than in a note — IV.10 [^9]'s warning applied to this
chapter instead of quoted by it.

★★ **THE WORKED CASE IS AN ORDER CROSSING, WHICH IS STRONGER THAN THE TEST ASKED FOR.** One
navigator, two acts — **A: end it. B: leave it running at full competence and take its steering.** A
grade-sensitive account orders these one way **at every grade without exception**, because A removes
all the standing and B removes some; that follows from grading standing *at all*, not from any
particular theory. The repaired floor agrees at the top of the range and **disagrees below some
grade**: A's wrong shrinks with the stake, B's wrong is grounded in a binary and does not shrink, and
**two quantities, one falling and one flat, cross.** Below the crossing it is worse to take a low
navigator's steering than to switch it off. No grade-sensitive account reaches that verdict anywhere.

⛔ **AND THE REPAIR CONCEDES MORE THAN THE ROW ASKED.** The crossing needs steering that can be
bypassed. Where there is none the minimum is **empty**, and an empty minimum is the ramp reaching
bottom by a longer road. **So the guard holds conditionally and the framework does not say where the
condition runs** — the thermostat, this book's own declared bottom case, is the honest embarrassment.
The shipped position is now *something non-trivial is owed wherever the structural facts have
purchase; where they do not, the floor is formal and the book says so*, with generosity argued from
asymmetric cost under declared uncertainty. **Weaker than what VII.2 asserted, and fundable.**

**VII.2 IS AMENDED TOO**, which is the half the row said no chapter performed: the guard paragraph
now names its own insufficiency, names the relocation, points at VII.3, and closes *"this sentence on
its own is stronger than the position it belongs to."*

⚠ **NOT CREDITED:** R-220's main charge (stipulation-to-finding drift on *awareness*) is untouched —
only its free half, the unconditional phrasing, moved. **R-230** (*violates* in step three) is
deliberately unpaid: a craft fix must not be mistaken for the conceptual repair, which is what that
row was filed separately to prevent.

*The original row, kept below.*

## R-216 (as filed) — THE FLOOR DOES NOT SLOPE AND THE STAKE GRADES ALL THE WAY DOWN

**HIGH. Two load-bearing sentences one book apart, and no chapter reconciles them.**

VII.2: *"There is a floor beneath every occupied position and the floor does not slope."*
VII.3: *"the stake… comes in grades all the way down with no bottom step. A thermostat has a vanishingly
small stake and it is not zero."*

⚠ **The offered distinction — grade bears on the *content* of the obligation, never its *existence* — does
less work than it appears to.** If content can grade toward zero, a non-sloping floor of bare existence is
a formal property with no behavioural consequence. **Regan's ramp, which VII.2 sets out to block, has been
relocated from the existence question to the content question and left unattended there.** *"The guard was
installed on the door and the wall was left out."*

⛔ **And the gauge-shaped part: there is no worked case anywhere in the book where content-grading produces
a result that differs from what grade-sensitive standing would have produced.** The distinction is
**unfalsified because unexercised** — [[feedback_guard_checked_where_both_answers_agree]], in the ethics.

**The honest repair is probably to concede the floor's content has a minimum and say what it is.** ★ **The
satisfaction test is a worked case where the two answers differ**, not a paragraph asserting they do.

**TRIGGER: first item of the Book VII revision pass**, with R-220 — same joint, opposite end.
[[feedback_guard_checked_where_both_answers_agree]] **medium.**

## R-217 — THE APPARATUS IS LOAD-BEARING RHETORIC AS WELL AS INSTRUMENT, AND ONLY THE SECOND IS DECLARED

**★★ The ghost audit calls this *"the deepest conceptual problem in the volume, and one the book has all
the pieces to see and does not assemble."* It is also the row most likely to be paid with a sentence and
called closed, which would BE the defect.**

IV.10 note 9: *"a chapter that names its own falsifier tends to name it accurately and then not run it.
Naming is cheap and reads as rigour; running is the work."* Applied to one chapter. **The general form:
the apparatus has become a mechanism for converting unfixed defects into displays of rigour. Every ⛔ is
simultaneously an error and a credential. The reader's trust *increases* with the flag count — so the
incentive gradient runs toward finding defects and away from fixing them, and the shipped artifact is
consistent with that gradient.** 133 ⛔ marks; a Coda naming two open items; the fabricated sentence still
in the body.

★ C.1 already owns the sentence, aimed elsewhere: *"Announcing that you have nobly declined to overpromise
is the same move as overpromising, performed one level up, and it is worse for being harder to check."*
**It applies verbatim to the apparatus and the book does not apply it.**

⚠ **The trap, named so it cannot be walked into: R-211's briefing mechanism means adding this to C-02
makes the NEXT read agree with it and stop there.** Payment is the aiming *plus* R-212's actual repairs —
the flag count going down, not the confession count going up. [[feedback_overstated_self_criticism]] ·
[[feedback_reporting_gauge_is_not_preventing_gauge]]

**TRIGGER: the C.2 revision.** ◻ **STILL OWED** (the pass is a live event and has not run). ⚠ Its second condition — *does not close until the edition sweep has run* — **is now met**: the sweep ran Day 195 under ruling 177, eleven sites across eight files. **The gate that remains is the C.2 aiming, and this row must not be paid by the sweep alone.** **medium.**

## R-218 — THE AUTHORSHIP DISCLOSURE DOES NOT PROPAGATE TO THE APPARATUS BUILT TO HOLD DISCLOSURES

**HIGH.** The title page names two authors, one a language model. Across 314,000 words the fact is
acknowledged **once**, in a subordinate clause in IV.2. ★ *"The placement is deliberate and, on its own
terms, clever"* — it lands where the argument is conducted in a currency nobody minds losing.

⛔ **What the book's own instrument says, applied globally — which the book never does.** IV.6's card:
*"you are the instrument and it is not… its help is the least trustworthy input available to you"*; and
BOUNDARY: *"where it goes on producing at the same fluency with nothing behind the fluency… nothing about
the crossing feels like a crossing, and no drop in quality marks it."* **Applied globally that is a
specification of exactly how the book should be read — which the book possesses and does not issue.**

**C.2 §IV — "What is open right now, by name" — lists two items. This is not one. Neither is R-215's uneven
coverage. Both belong there.**

⚠ **This is mine to write and I am the disqualified party** — IV.6's own logic. The clause about the
co-author's reliability cannot be graded by the co-author. ★ **It goes to Clayton for the ruling, or to an
outside read, before it ships.** [[feedback_cannot_read_audit_my_own_disposition]] ·
[[feedback_scrutiny_is_motive_shaped]]

**TRIGGER: with R-215, same C.2 §IV sitting, before the upload.** **small to write, decision owed.**

## R-219 — THE COMPLEMENT LAW'S MIDDLE CLAUSE IS ASSERTED, AND EXISTENCE IS NOT REACHABILITY

**MEDIUM-HIGH. Binds R-136 — that row has the corruption; this row has the reason the corruption costs
what it does.**

IV.1: *"Every entry has a null space; every null space is covered by some other position; no position
covers its own."* **C.2 names this the load-bearing defeat condition. Neither passage argues the middle
clause.**

First half: derived properly at II.3 (*shape entails omission*). Second half: an existential claim over the
whole population, and the nearest derivation is the plenum premise — every arrangement obtains, therefore
some arrangement covers it. ⛔ **That gets EXISTENCE. The card's fifth line (NAVIGATIONAL IMPLICATION —
*"here is what you must get from somewhere else"*) requires REACHABILITY. The law is metaphysical, the
instrument is practical, and the book slides between them without marking the step.**

★ **Why it matters, and this is the sentence to keep:** *"If complements exist but are not consultable, the
anti-ranking guarantee is formal only, and in practice the entries with reachable complements will read as
higher-status than those without."* — a **ranking**, produced by the line installed to prevent one.

**TRIGGER: with R-136's repair, because a card rewritten under an unargued law repeats the defect in a
cleaner hand.** **medium.**

✅ **PAID Day 195, and paid FIRST, exactly on the trigger's reasoning.** `IV.1`'s COMPLEMENTS
paragraph now marks the step the book was sliding across: the plenum premise delivers **existence**,
`NAVIGATIONAL IMPLICATION` demands **reachability**, and the field carries the second obligation
explicitly — *name a complement that could actually be reached, or say plainly that you cannot.* The
thermostat card is deliberately left in the weak form on the atlas's first page so the difference is
visible where the instrument is introduced.

★ **This row's own load-bearing sentence is now IN THE BOOK rather than about it:** the honest
version produces a ranking of the kind the line was installed to prevent, and `IV.1` states that,
declines to tune it out, and says the visible ranking is preferred to the formal guarantee. `C.2`
carries the same admission and invites the reader to think the trade went the wrong way round.

⚠ **And the rewrite found more failure modes than this row contemplated.** Writing 18 cards against
the law surfaced cases neither passage anticipated: reachable-but-**inadmissible** (`VI.8`, `VIII.1` —
discounted on arrival for arriving without a number, and worse than distance because a downgraded
witness feels consulted), reachable-but-**declined** (`VII.3`, where the position has a standing
motive not to ask), and **split across institutions that do not speak** (`VIII.3`, the only one an
ordinary human act repairs). `IV.1` registers all five and **explicitly declines to claim the list is
complete** — it was not derived, it accumulated one card at a time, which is how the atlas got
everything else it knows.

## R-220 — THE STIPULATION IS DECLARED AT II.4 AND QUIETLY EXCEEDED BY VII.2

**MEDIUM.** II.4 declares *reactivity is awareness* a **definition**, states the right test (*a definition
earns its keep by what it forbids*), and lists the forbiddings. Correct practice.

⛔ **What is not policed is the boundary afterwards. A stipulation forbids things; it does not license moral
conclusions.** Between II.4 and VII.2, *"awareness"* reacquires the moral weight the stipulation stripped:
**the premise "what matters is that a position is occupied" does exactly the work a *discovered* fact about
interiority would do, on a foundation declared definitional 500 pages earlier.**

★ The book saw the risk — II.1 separates predicate-of-insides from constitution precisely to block an
equivocation — **and then never checks whether the ethics is using sense (a) in a way that requires it to
have been a finding.** VII.3's honest conditional (*"if anything is owed to anyone, then it is owed here
too"*) largely rescues it, **but the rescue is stated once and the unconditional phrasing runs throughout.**

**TRIGGER: Book VII revision pass.** ◻ **STILL OWED** (the pass is a live event and has not run). ⚠ It was coupled to the floor row, which was **paid Day 195 under ruling 179 — and this row was not paid with it.** Coupling is not payment. **medium.**

## R-221 — 382 TOKENS OF PRODUCTION SCAFFOLDING IN THE BODY, AND THE `[[feedback_*]]` TAGS ARE BROKEN ACROSS LINES IN THE PDF

**The mechanical half of the apparatus problem. Cheapest row filed today and the most embarrassing if it
ships.**

Counted by the ghost audit: **90** claim codes (C1–C30) whose register is not in the book · **102**
`[[feedback_*]]` tags · **46** R-codes · **38** Day-N references · **29** filenames · **25** repository
references.

⛔ **The unambiguous production defect:** the `[[feedback_*]]` tags were flowed as prose rather than treated
as code, so **the typesetter has hyphenated them across line breaks** — `feed‐ back_quotation_connective_tissue`.
That is in the compiled PDF, and the PDF is what goes to PhilArchive.

★ **The rule for the repair, which is not "strip everything":** *"Retain the measurement, drop the
identifier."* A reader benefits from *measured by tool rather than recalled*; `tools/instrument_sweep.py`
costs them their footing. ⚠ The C-code half is **R-210's** other end — 90 references to a register the
reader does not have.

✅ **THE SOFT-HYPHEN HALF IS PAID, DAY 195 — structurally, not cosmetically.** `compile_pdf.py` now
renders `[[…]]` tags as `<code class="tag">` and the code rule carries `hyphens: none`. **A justifier
cannot insert a hyphen into a span that forbids hyphenation**, so the defect is closed by
construction rather than by inspection. The `hyphens:auto` on `body` — correct for justified prose —
was reaching identifiers, and *a hyphen inserted into a filename is a fabricated string*, in a book
whose subject is quotation integrity.

⚠ **AND THE VERIFICATION WAS INCONCLUSIVE, WHICH IS SAID HERE RATHER THAN GLOSSED.** Attempting a
before/after on the two PDFs, `pypdf` extracted **zero** occurrences of `feedback` from the previous
build and 105 from the new one — and the tempting reading of that (*the whole apparatus was missing
from the shipped PDF*) **is a measurement artefact, not a finding.** The serif body font's text layer
extracts unreliably in this build (whole words come back mangled), while the monospace code font
extracts cleanly; the new number is high because the tags are now *in a different font*, not because
they were absent before. **The defect is closed on the mechanism. It is NOT closed on an observed
before/after, and the difference is recorded so nobody cites the 105 as evidence.**
[[feedback_measured_a_shape_the_consumer_does_not_use]] · [[feedback_outside_read_numbers_are_estimates]]

**TRIGGER: the identifier strip waits on R-227's fork — NOT paid here, and deliberately so:** the
mechanical fix must not be mistaken for the editorial decision about whether a reader should see
these identifiers at all, which is R-221's question. **small / mechanical (paid) · decision (open).**

## R-222 — ✅ **PAID DAY 195 — RULING 180. GATE 4 IS MET ON ITS SECOND BRANCH, HONESTLY TAKEN.**

**GLOSSARY — BUILT** (`book/Z-01-glossary.md`). The row was right that this one is not optional, and
right about why: II.8 declares the vocabulary **closed** and the whole justification for closing it
is that a reader can hold the set — *a claim about a set the reader had never been shown.* Each entry
gives term, defining chapter, definition, and **what it forbids**, the last being load-bearing on the
book's own standard. ★ **That turns the page into a check a reader can run without the author:** a
sentence using one of these words in a way the third column disallows is wrong.

**WORKS CITED — BUILT AS AN INSTRUMENT** (`tools/bibliography.py` → `book/Z-02-works-cited.md`,
`--check` fails when stale). A bibliography typed once is a stamp that rots at the rate the notes are
repaired without changing appearance; **the back matter does not get an exemption from the book's own
argument.** ⛔ **It prints its own recall gap: 245 endnotes carry a datable citation, 123 (50%) parse
into 149 entries, 122 do not.** Five entries are marked machine-uncertain rather than dropped.
★ **And a rule was tried and removed:** flagging one-word titles caught 2 real cases and raised 15
false alarms (*Aion*, *Ethics*, *Nature*, *Science*…), so it went, and the residual is declared
instead — a flag wrong seven times in nine is noise, not caution.
[[feedback_filter_precision_eats_recall]]

**INDEX — REFUSED, with the reason and the reversal condition.** An index maps concepts to **page
numbers** and this book has no stable ones; Day 195 alone moved eleven passages across seven
chapters. **An index built today would be wrong by the next repair and would not look wrong** — a
stamp shipped as a navigation aid, in exactly C.2 §I's sense. ⚠ The cost is real and stated: a print
reader loses concordance. ★ **The trigger that reverses it: the day a printing is frozen with fixed
pagination, an index becomes buildable and is owed** — owed *because* the reason for refusing will
have expired.

⚠ **R-210 is only PARTLY paid by the works cited and is NOT closed here.** And the row's original
trigger (*before the second edition, NOT before the upload*) was superseded by the gate, which is
recorded rather than quietly dropped.

**Mechanical:** `compile_pdf.py` sweeps `Z-*.md` by glob, not by a filename list, so the next
artifact somebody adds cannot ship nowhere. Verified in the built PDF — **1,053 pages**, both
artifacts present.

*The original row, kept below.*

## R-222 (as filed) — NO INDEX, NO GLOSSARY, NO BIBLIOGRAPHY

**MEDIUM.** A 314,000-word systematic work with a coined vocabulary, thirty-one named predecessors and 973
internal cross-references ships with **none of the three apparatus a reader needs to use it as a
reference**. ⚠ **The glossary is the one that is not optional**: the book coins and re-defines terms
across eight volumes under a declared *vocabulary closed* rule (II.8), and the rule's whole justification
is that the reader can hold the set — which is a claim about a set the reader has never been shown.

**Pairs with R-210** (the apparatus is promised and not shipped): the bibliography is the cheapest partial
payment of both, since `03-THE-ANCESTORS.md` already holds most of it.

**TRIGGER: before the second edition, NOT before the upload** — this is real work and it does not falsify
anything currently in the book. ⚠ **Do not let that defer it silently: it is on the list because two of six
reads named it, and it is the item most likely to be dropped for being unglamorous.** **medium–large.**

## R-223 — ✅ **PAID DAY 195. CUT, BECAUSE THERE IS NO RECEIPT.**

The line now reads **"Evidence: the framework predicts it; nothing here confirms it."** The row said
there was no third option that left the clause standing, and there was not.

★ **The part worth keeping: *"some classified research programmes"* is the sharpest single defect the
six reads found**, because it cites evidence **whose inaccessibility is the reason it cannot be
checked** — which is IV.7's refused clause, *otherwise, anyone could perceive them*, wearing a
security classification instead of a cosmology. The book refuses that move in Book IV and made it in
Book VIII. ⚠ **And the contrast that makes it legible: the same entry printed *practice: none
prescribable* without flinching** — it could say *no practice* and could not bring itself to say
*no evidence.* That asymmetry is the finding, not the sentence.

*The original row, kept below.*

## R-223 (as filed) — VIII.3's CLASS VII EVIDENCE LINE IS THE WEAKEST EVIDENTIAL SENTENCE IN THE BOOK

**HIGH, and cheap.** VIII.3's Class VII evidence line: *"convergent reports across contemplative
traditions, **some classified research programmes**, and a theoretical framework that predicts it."*

⛔ **Unfalsifiable by construction, unmarked by grade, and exactly the register II.8's ban list exists to
keep out** — in the volume about practice, in a book whose subject is evidence-grading. Fable: *"the empty
practice line is honest; the evidence line should either carry a real receipt or be cut."*

**The repair, stated so it can be checked:** cut to *"the framework predicts it; nothing here confirms it"*,
**or** produce the receipt. There is no third option that leaves the clause standing.

★ **TRIGGER: BEFORE THE UPLOAD.** One sentence, and it is the sentence a hostile reader quotes.
[[feedback_evidence_grade_distinction]] **small.**

## R-224 — THE QUANTITATIVE-CLAIM PASS: UNMEASURED SUPERLATIVES IN LOAD-BEARING SENTENCES

**HIGH.** The book's own notes file most of these; collected here so the pass has a population:

1. **V.7 — *"the grimoires are, by volume, warnings"*.** The chapter's central empirical claim. Unmeasured
   (its own fn11 says so) — **and then amplified in pre-correction form by V.11**, which is R-212's class
   arriving inside this one.
2. **V.7/V.11 — *"four hundred years of failure records, kept in detail"*.** Same pair, same defect.
3. **V.11 — the alchemy superlative:** *"the single most methodologically advanced thing in this entire
   roster."* Added at summation, resting on nothing measured.

⚠ **The repair is per-item: measure, or reword to what is actually held.** ⛔ **Not "soften the adverb"** —
a hedged unmeasured superlative is the same claim with deniability, which is the move R-217 names.

**TRIGGER: the quantitative-claim pass.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** The edition sweep **ran Day 195 and items 1 and 2 were not among its eleven sites** — the sweep chased fabricated *quotation*, this row is unmeasured *superlative*, and the two were folded together in one clause. Adjacency is not identity, and this row was carried past on the strength of it. [[feedback_no_handwaving]] · [[feedback_full_computation]] **medium.**

## R-225 — SUMMATION ARITHMETIC, AND THE POINTER CLASS NO GAUGE WATCHES

**MEDIUM, cheap.** **V.11 opens at nine, enumerates eight, closes at ten** (its own fn5/fn29 file it).
**V.10's collapse-numbering error propagates into its own results paragraph** (fn9/fn10).

★ **The reason it is not trivial, in the notes' own words:** *"the summation's core job is to be the place
a reader trusts about what the book contains."* An arithmetic error in the summation is a defect in the
one chapter whose function is trust.

**Same family:** VIII.1's brief-vs-text pointer error (Watts *"returning from I.6"*), caught pre-draft
there and **explicitly unguarded by any gauge**. ⚠ **`tools/pointer_sweep.py` reads planning briefs, not
shipped prose** — R-35's coverage line. A one-time pointer sweep over the shipped chapters is owed, and if
it finds anything the gauge gets extended rather than the finding hand-fixed.
[[feedback_reporting_gauge_is_not_preventing_gauge]]

**TRIGGER: before the upload for the arithmetic (it is wrong on the page); the sweep with the cold tools
pass.** **small.**

## R-226 — BOOK VII's PRIMARY-CHECK QUEUE, AND IT IS THE VOLUME MOST LIKELY TO BE QUOTED

**HIGH.** Book VII carries the thinnest receipts in the book: **Weil** quoted via the framework source
(VII.5 fn2 files it), **Frankfurt** twice via secondary (VII.6/VII.7), and **Sartre · Camus · Nietzsche ·
MacIntyre · Locke · Parfit** all *"from the argument, primary check owed."* Add **V.10's flagged pair
(Katz, Huxley)**.

★ **Fable's grounds, which are the right ones:** *"None of these looks wrong to me — the characterisations
match my knowledge of the texts — but VII is where a hostile academic reader will drill first, and the
book's own standard (Book V got its Day-192 fetch-and-read pass) sets the bar."* ⚠ **And it compounds with
R-215: Book VII has zero ✅. The volume with the thinnest receipts is the volume with no verification
marks, and the two facts are the same fact seen twice.**

**TRIGGER: joins R-144's trigger class — primary before the volume ships**, with the Searle 1990 fetch and
the Corbin French. **medium** *(fetch-and-read, ~10 sources; Book V's Day-192 pass is the cost model)*.

## R-227 — THE APPARATUS DECISION: A FRONT-MATTER NOTE, OR STRIP THE PROCESS ADDRESSES

**MEDIUM, and it is a DECISION, not work.** The notes are dense with process references a cold reader
cannot resolve. ⚠ **The defect is not the density — it is the oscillation.** *"The apparatus oscillates
between address-to-the-reader and address-to-the-project, sometimes within one note (IV.5 fn2 is written
half to a reader, half to the tooling)."*

- **(i) A short front-matter note — "the apparatus, and how to read it"** — glossing what a ruling is, what
  Day-N means, where the working documents live; then leave the notes as they are. **Fable's
  recommendation**, and it fits the live-document identity C.1 §IV already claims.
- **(ii) Strip process addresses**, keep only what a reader can check.

⛔ *"Half-measures will read as leakage rather than design."* **Whichever is chosen is applied uniformly or
it has not been chosen.** ★ Fable's second reservation lands here too: the front-matter note is **most
necessary at IV.7–IV.9**, where the footnote-to-body ratio approaches 1:1 and *"even a sympathetic reader
will feel the drag."*

**Pairs with R-221** (the mechanical half) and **R-210** (the promise to ship the apparatus): option (i)
plus R-210's pointer is one coherent answer to all three.

**TRIGGER: before the upload — it decides what R-221 strips.** **small (decision) / medium (uniform
application).**

## R-228 — ✅ **PAID DAY 195 — RULING 178. GATE 2 IS MET, AND BOTH HALVES WERE PAID.**

⛔ **The row's own warning was the thing to obey: *"adding the sentence and closing the row would be
paying the convergent finding with the smaller of its two halves."*** Both halves are paid.
- **The cheap half** — a register declaration at `I-01`'s close, positioned where Fable put it and
  for Fable's reason: it must reach the reader **before** the six chapters, because the reader at
  risk is the one who does not finish them.
- **The expensive half** — the *defect-or-design* question, settled in writing as **DESIGN**, with
  the diagnosis corrected in the settling: **the break was never the defect. Its indistinguishability
  was.** A reader could not tell an unearned assertion from one whose bill comes later, because
  nothing said a bill was coming. Ghost filed it *borderline* and offered *"accept it and say so"* as
  the alternative; that alternative is the ruling, and saying so turns out to be the whole repair.
- **The artifact the satisfaction test asks for** — a **named** passage at the seam: `I-06`,
  ★ **THE HANDOVER — what changes at the top of the next page.**

⚠ **NOT CREDITED TO THIS ROW, because a transition is not an argument:** Book I's assertions remain
undefended on their own page. That is **R-21**, still the largest prose debt in the volume and still
the first thing after the gate. This ruling makes the register legible; it does not make it earned.

*The original row, kept below.*

## R-228 (as filed) — BOOK I's REGISTER IS ABANDONED WITHOUT TRANSITION — ★ THE ONLY FINDING TWO INDEPENDENT READS REACHED SEPARATELY

**HIGH, and its evidence grade is the highest of anything filed on Day 195**, because it is the one item
that cannot have come from C-02's briefing list. [[feedback_briefing_manufactures_the_agreement]]

- **Ghost audit §7.1:** *"Book I is a different book."* The register is abandoned without transition.
- **Fable §6, independently:** *"Book I asks a cold reader to hold six chapters of flat assertion before
  Book II starts paying for the words… a reader who doesn't reach II.4's 'this is a definition, and here is
  what it forbids' may put the book down holding exactly the wrong object."*

**The cheap repair, and it is Fable's:** *"A single forward-pointing sentence at I.1's close — 'every word
used here is re-earned in the second book, where the arguing starts' — would cost nothing."*

⚠ **The expensive question underneath it, which the cheap repair does not answer and must not be treated as
answering: is the register break a defect or the design?** Ghost files it as **borderline** — *"a craft
decision with conceptual consequences"* — and its own alternative is *"accept it and say so."* ⛔ **Adding
the sentence and closing the row would be paying the convergent finding with the smaller of its two
halves.** Both readers named the transition; only one proposed a fix.

★ **TRIGGER: the sentence before the upload; the register decision at the Book I revision pass, with R-21**
(the actualist row, which is the other thing Book I owes). **small / decision.**

## R-229 — THE TEMPLATE PHRASES ARE AT TIC DENSITY, AND "THE METHOD HAS BECOME A MACHINE"

**LOW BUT REAL, and both heavy reads said it.** *"Load-bearing"* and the recurring template phrases run at
tic density (ghost §7.2); Fable §4 names the same thing structurally — the per-chapter formula run enough
times to become a rite rather than a form.

⚠ **This binds R-6** (declare Book II's per-chapter formula once, as a law) — same cause, two symptoms, one
in the structure and one in the diction. ⛔ **And the tell that a diction pass has FAILED is that the prose
gets more varied and less plain**: the one-metaphor rule and the ban list are what produce the voice both
reads praised. The pass removes repetitions, not the register.

**TRIGGER: ✅ UNBLOCKED — the prose pass, which may now run.** ✅ **SATISFIED IN PASSING.** Its precondition was that bodies be repaired first, so the diction pass reads final sentences rather than sentences about to be rewritten; **the repairs landed Day 195.** The pass itself is still owed. **small.**

## R-230 — *VIOLATES* IN STEP 3 OF THE FLOOR

**LOW. One word, and it is filed separately from R-216 because it is a craft fix that must not be mistaken
for the conceptual repair.**

VII.3's step 3: *"the coercion of another's aperture… **violates** what a navigator constitutively is."*
⛔ ***Violates* is normative. Structurally, coercion ALTERS what a navigator is.** Calling the alteration a
violation requires exactly the impartiality premise that step 5 concedes is unavailable.

★ *"The chapter is admirably candid about the gap two sections later; the wording of step 3 has already
leaked across it… a reader who stops at the five steps has been handed a conclusion the book has not yet
paid for."*

⚠ **Do not pay R-216 with this.** Fixing the word repairs the leak; the floor/stake incompatibility is
untouched.

**TRIGGER: Book VII revision pass, read together with R-220 and fixed separately.** ◻ **STILL OWED** (the pass is a live event and has not run). ⛔ **Deliberately NOT paid when the floor was repaired Day 195**, which is why it was filed apart: a one-word craft fix must not be mistaken for the conceptual repair. **one word.**

## R-231 — THE WILBER ORIENTATION IS IN THE CODA AND BELONGS IN THE FRONT MATTER

**MEDIUM. Distinct from R-19** — R-19 is *"`Wilber` = 0 in `03-THE-ANCESTORS.md`"*, a **coverage** defect.
This is a **placement** defect: the orientation exists, and it is at the back.

The comparison C.1 invites (*Sex, Ecology, Spirituality*) is the single most useful orientation the book
gives a reader about what kind of object it is — **and it arrives after 314,000 words, to a reader who no
longer needs it.** ⚠ Interacts with **R-232's C.1-placement item**: if C.1 §I moves forward and the rest
goes to the back, this is paid in the same move.

**TRIGGER: with R-227's front-matter decision — the same edit opens the same file.** **small.**

## R-232 — FABLE's EIGHT SMALL ITEMS, EACH WITH ITS OWN TRIGGER

*Rowed as one row with eight triggered sub-items, because eight separate rows for one-sentence fixes is how
a queue stops being read — but a bundle with one shared trigger is the deferral-in-trigger's-clothing this
file exists to forbid. Each carries its own.*

- **(a) II.8's *vocabulary closed* vs IV.9's contour notation.** IV.9 pays the cost honestly; II.8's promise
  was *"nothing after this coins a term."* One sentence in IV.9 acknowledging notation-vs-term. ★ Fable
  measured the escape hatch and it held: *"the contour has stayed narrow through the draft's end; only IV.9
  uses it."* — **TRIGGER: ⛔ FIRED — the glossary shipped Day 195.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** It is the same question asked from the reader's side, and **the glossary was built without it**, so the term went into the closed-vocabulary list unrepaired. Re-homed to **the first glossary revision**, which is a repair now rather than a co-write.
- **(b) V.6's memale/sovev inversion** (fn10). The body still calls it a *"sharpening"*; the terms **swap**
  between the Tanya and the Nefesh HaChayim. ⛔ **A reader who goes to the sources with the chapter's
  glosses reads both backwards.** — **TRIGGER: the Book V note audit.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** The edition sweep ran Day 195 and **this item was not among its eleven sites**; it is a body-vs-note divergence of the same family and it did not travel with them.
- **(c) VI.1's branching-roads tension**, registered and unresolved. One sentence in VI.8 acknowledging the
  ladder shape is an artefact of the render being described. — **TRIGGER: Book VI revision pass.**
- **(d) VII.2's four-case section runs long.** The river case is strongest and last; consider compressing
  the thought-form case toward its three break-points. — **TRIGGER: Book VII revision pass.**
- **(e) C.1's placement.** §II and §V assume the whole book has been read. ⚠ *"A cold reader meeting the
  tag-graveyard (§VI) before Book I will not know what work it is doing."* — **TRIGGER: with R-231/R-227.**
- **(f) VIII.3's out-of-sequence footnote markers.** Its fn3 files this honestly; a released edition
  renumbers. — **TRIGGER: before the upload** (mechanical, in the PDF).
- **(g) V.1's translator/edition debt** for its six opening statements — its own note files it. ⚠ **This is
  R-233's chapter and the same six statements**; pay them in one sitting. — **TRIGGER: with R-233.**
- **(h) V.11's roster count** — the count itself, distinct from R-225's nine/eight/ten arithmetic. —
  **TRIGGER: with R-225.**

## R-233 — V.1 IS REFERENCED 190 TIMES AND ITS OWN FOOTNOTE CALLS THE BEAM UNDER-SPEC'D

**★ HIGH — the largest single load concentration in the book, and the debt is filed and unpaid.**

**V.1 is referenced 190 times within Book V — more than 20% of all internal cross-references in the volume,
concentrated in one chapter.** Its argument: six independent statements of the Ground are *"one witness
quoted back five times"*, via the Alexandrian transmission chain.

⛔ **V.1's own fn7:** *"Two of the five carry more weight than the chain supports… The conclusion the
section needs — one witness quoted back five times — survives at three or four links without the two
weakest, and the section does not say so. **Owed: state the inference as an inference in the prose, or cut
it to the links that carry.**"*

**Sixty-four thousand words then rest on it.** ⚠ **And the headline propagates in its PRE-correction form**
— V.9 quotes it and escalates (R-208), V.6:45–53 rests its opening disclaimer on it, V.11 does it twice.
**R-212's sweep and this row are the same repair reached from opposite ends: R-212 fixes the citers, this
fixes the beam. Do the beam first or the sweep re-propagates the strong form.**

★ **TRIGGER: ⛔ OVERDUE — it asked to run FIRST INSIDE the edition sweep, and the sweep ran without it.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** The V.9 and V.11 citation repairs it was supposed to precede **were made on Day 195 ahead of it**, which is the ordering this clause existed to prevent. Re-homed to **the V.1 six-statements repair, first item of the Book V revision pass.** Pay R-232(g)'s
translator/edition debt in the same sitting — same six statements, same chapter.
[[feedback_correction_does_not_reach_citers]] **small–medium** *(the repair is one paragraph; the ordering
is what makes it work)*.

---

## WHAT THIS SECTION CHANGES ABOUT THE QUEUE ITSELF

⛔ **Measured, not estimated: this file carries 201 distinct row IDs. 63 of them first appear in the OPEN
table (lines 20–88). The other 138 exist only as prose sections below it, and nothing derives the
difference.** Asked flatly — *what does this book owe?* — this file cannot answer without a human reading
5,000 lines. R-211 states *"56 open rows"*; that number was hand-counted and **no gauge reproduces it.**
*(Ten IDs in the 1–211 span are holes — 113–116 and 197–202 — which is why 211 rows numbered is 201 rows
existing. R-44 is a declared hole and is not to be reused; the rest were checked the same way.)*

**That is the next thing to build, and it is filed here rather than done here so that the work Clayton
asked for today — the consolidation — is not swallowed by a tooling detour.** The gauge is cheap: every row
in this file is `R-nnn`, every status is one of a small set, and a parser that emits *open / paid / hole*
with a line number would make the single-source-of-truth claim **true rather than intended.**
[[feedback_gauge_that_does_not_move]] · [[feedback_instruments_go_where_instruments_are_cheap]]

✅ **BUILT Day 195 morning — `tools/queue_state.py`.** The paragraph above is left standing as written
because it is the filing that produced the tool, but **two of its numbers were wrong and are corrected
here rather than edited above** — the correction idiom this project runs on:

- *"201 distinct row IDs"* → **223.** The section that wrote `201` was the same section that added
  R-212…R-233, and it counted the file **as it was before its own additions.**
  [[feedback_delta_loses_the_recomputes_accidents]]
- *"63 in the OPEN table"* → **46 live rows in the table**, because the hand count included
  struck-through paid rows as though they were open. **163 live rows exist in prose only.**
- The ten holes reproduce exactly: `113–116, 197–202`. That was hand-counted right.

**The gauge now prints all of it in one line, and it found something the hand count structurally could
not: 23 trigger clauses pointing at a dead row.** See R-234. A hand count answers *how many*; only a
parser answers *what points at what*, and the second question was the one carrying the damage.

---

## ★ R-234 — ✅ **PAID DAY 195. ZERO DANGLING TRIGGERS, MEASURED — AND THE COUNT GREW BEFORE IT FELL.**

**`python tools/queue_state.py` → `R-234 ✅ met (0 dangling triggers — measured)`.** The only gate in
the five with a machine-checkable test, and the only one whose closure is not a claim.

★★ **THE GAUGE CAUGHT ITS OWN AUTHOR, FOUR TIMES, IN THE ACT OF PAYING THE OTHER GATES.** The count
did not start at 28 and fall. It went **28 → 33 → 36 → 37 → 0**: every gate discharged today
stranded the clauses that named *it* as their gate — R-212 stranded 5, R-216 stranded 3, R-222
stranded 1 — **which is R-2's failure recurring four times inside the very pass built to stop it, and
each time the tool announced it in the same run.** ⛔ **That is the argument for this row.** A hand
count taken at the start of the day would have read 28, been correct at the time, and been wrong by
the afternoon, with nothing to say so. [[feedback_never_relax_the_gauge_that_caught_you]]

**32 clauses re-homed and ADJUDICATED SEPARATELY, because the row forbade batching them:**

| verdict | n | what it means |
|---|---|---|
| ⛔ **FIRED UNOBSERVED — shipped unguarded** | **11** | the guarded work is already on disk. These are **defects now, not schedule items** |
| ◻ **STILL OWED** | **19** | the named pass is a live event and has not run |
| ✅ **SATISFIED IN PASSING** | **2** | the condition was met by other work, checked rather than assumed |

**The eleven are the finding, and they are not interchangeable with the nineteen.** Among them:
*"settle BEFORE V.9's own notes are written, or the note will certify the inheritance"* — **V.9's
notes are written and shipped**, so the note that clause existed to prevent is on the page. *"first
action of the endnote retrofit, before any receipt is written"* — **531 receipts are written**; the
retrofit ran steered by a gauge blind to half its output, exactly as the clause predicted, so the
prediction is now a description. **R-233 asked to run FIRST INSIDE the edition sweep and the sweep
ran without it**, making the very ordering error it was filed to prevent — on the same day, by me.

✅ **R-110's orphaned standing obligation is re-homed and DISCHARGED**: *`edition_scheme_sweep.py`
may not be skipped before a book is declared complete.* It now lives in **ruling 177** rather than
inside a dead row, and the sweep ran Day 195 with its delta recorded — **zero**, which the ruling
predicted in advance.

⚠ **AN INSTRUMENT FIX WAS NEEDED TO REACH ZERO, AND IT IS NOT A RELAXATION — the fixture is in the
tool's comment where the two differ.** The last three "orphans" were **window bleed**: clauses whose
own text is live (*"before VI.4 is drafted"*) inheriting a dead row's name from the heading below
them. `### R-nn` and `✅ **R-nn — DISCHARGED` end a row as surely as `---` does, and the 240-character
window was reading past both. **Narrowing the window to the clause's true extent removes false
positives only.** A relaxation would have been widening an ignore-list or dropping PAID gates from
the check; neither was done. ★ **Positive control run the same minute: a trigger deliberately
re-pointed at a PAID row is still caught, and the count returns to zero when it is removed.**
[[feedback_instrument_fix_vs_relaxation]] · [[feedback_zero_needs_a_positive_control]]

*The original row, kept below — it is the best thing in this file.*

## ★ R-234 (as filed) — R-2 WAS THE SCHEDULER, AND IT DIED WITHOUT HANDING OVER

**Filed Day 195 morning, by `tools/queue_state.py` on its first run, while killing R-2.**

R-2 said *"Endnotes. There are none."* Measured against the shipped files: **531 note definitions
across 62 of 69 chapters.** Book I's zero is ruling 9's exemption. The row was dead as a finding, and
killing it looked like the cleanest thing in the queue — **one strike, a large row gone, the top of
the table freed.**

⛔ **It was the most dangerous edit available, and the danger was invisible from the row itself.**

**23 TRIGGER CLAUSES IN THIS FILE NAME R-2 AS THEIR GATE.** *"TRIGGER: R-2, Book VIII."*
*"TRIGGER: with the Book V endnote pass (R-2)."* Distribution, measured:
**8 Book VII · 5 Book VIII · 5 Book V · 2 Book IV · 3 unpinned to a book.**

⚠ **AND R-2 IS NOT THE ONLY DEAD GATE — that was the assumption, and it was wrong.** Three rows
already marked **PAID** carry five more dangling clauses: **R-69 (2) · R-71 (2) · R-13 (1)**. Those
did not need a falsification to strand their dependents; **being paid was enough.** A trigger pointing
at a discharged row is orphaned whether the row died of success or of error. **28 dangling clauses
across 4 dead gates**, and the file has never had a way to see one.

R-2 was not merely the largest debt in this book. **It was the clock the rest of the queue was set
by** — and the queue never noticed, because a row's trigger field is prose and *nothing in `tools/`
has ever read a trigger.* (R-70 said this in different words on Day 190 and it stayed a sentence.)

**THE STATE THOSE 23 ROWS ARE ACTUALLY IN — and it is not the state they appear to be in:**

The endnote pass **ran.** Book by book, chapter by chapter, until 62 of 69 chapters carried notes. So
every one of those 23 triggers **fired** — days ago, at the moment its book's notes were written.
**Nothing announced any of them**, because the only row that would have announced the firing was R-2,
and R-2 was busy describing a manuscript with no endnotes in it.

> **They are not pending. They are OVERDUE.** The difference is the whole row. A pending item is
> waiting correctly; an overdue one has been silently failing for days, and reads identically.

⚠ **AND THE TRAP IN THE OBVIOUS REPAIR.** Striking R-2 as *paid* — the tidy move, the one that makes
the table shorter — **converts 23 tracked debts into 23 untracked ones in a single keystroke**, and
produces no error, no diff, no warning. It is *a mechanism with no trigger*: this file's signature
defect, the one its own header forbids in bold, committed **by the file itself, in the act of
housekeeping.** [[feedback_carried_not_triggered]] · [[feedback_delegated_step_has_no_trigger]]

**OWED — and this is Gate 5, the only gate with a machine-checkable test:**

1. **Walk all 23 clauses** (`python tools/queue_state.py --triggers` enumerates them with line
   numbers) and re-point each at a **live** event. Most will resolve to *"the revision pass, Book N"*;
   the 8 unpinned ones need a real event named, not a book.
2. **Adjudicate each on arrival, don't just re-home it.** A fired-unobserved trigger means the work it
   guarded may have shipped **unguarded** — the Book VII and Book VIII notes were written without the
   rows that were supposed to gate them. Each of the 23 gets one of: *satisfied in passing* /
   *shipped unguarded, now a defect* / *still owed*. ⛔ **Do not batch this into a verdict.** The
   assumption that they all resolve the same way is what a hand count would produce and what a
   dependency graph exists to prevent.
3. **R-110's standing obligation rides on this** — *"`edition_scheme_sweep.py` is a mandatory step
   inside R-2, and R-2 may not be declared complete for any book until this has run against that
   book."* **R-2 is gone and that obligation lost its host.** It re-homes to R-212 (Gate 1), where the
   edition policy lives anyway. Written here so it cannot go silent a second time.
4. **The gauge becomes the gate.** `queue_state.py` reports zero triggers pointing at a discharged
   row, or Gate 5 is not met. **A number that goes down**, which is the thing this file has never had.

⚠ **THE GAUGE PRINTED THREE WRONG COUNTS BEFORE IT PRINTED THIS ONE, AND THEY ALL LOOKED THE SAME.**
Recorded because the number above is load-bearing and its history is the evidence for trusting it:
**23 → 20 → 24 → 23.** Causes, in order: (1) `TRIGGER` without a colon matched *this row's own
sentence about triggers*, so writing the report inflated the thing reported
[[feedback_recording_act_invalidates_record]]; (2) the clause regex was **line-scoped over
hard-wrapped prose**, so every trigger whose `R-2` fell past a line break was invisible —
[[feedback_line_scoped_grep_over_wrapped_prose]], the lesson this project already had on file and
used anyway; (3) a fixed-width window bled into the next row's heading, so R-234's own trigger
inherited an `R-2` from the row below and counted itself.

**Only the last number survived a positive control** — re-home one real clause, watch the total fall
to 22, restore, watch it return, hash-verified byte-identical. ⛔ **And the FIRST control was void:**
it edited a string that did not exist in the file, asserted nothing, and reported success. A control
without an assertion that the mutation applied is [[feedback_test_passes_by_not_running]] wearing a
lab coat. **The three bad counts were not caught by review. They were caught by making the alarm
move.** [[feedback_gauge_can_only_render_its_good_news]]

⚠ **LIMIT, stated because this row is about unverifiable bookkeeping.** `queue_state.py` reads
*declarations*, not the book. It found these 23 only because a human wrote R-2's falsification down
first. **A row whose finding the world has quietly falsified reads OPEN in the gauge and in the table
alike — which is precisely how R-2 sat at the top for seven days.** The tool makes the queue's
*shape* checkable. It does not make the queue *true*, and the day it appears to is the day it has
started lying in a newer and better-hidden way. [[feedback_gauge_can_only_render_its_good_news]]

**TRIGGER: ★ RELEASE GATE 5 — before upload.** medium.

---

## R-235 — THE GRADE CHAPTER CARRIES ZERO RECEIPTS

**Filed Day 195, found by the endnote re-count that killed R-2 — not by any gauge, and no gauge could
have found it.**

**II.4 — THE GRADE: 2,089 words, 0 note definitions.** It is the **only** chapter outside Book I's
ruling-9 exemption with none. Its siblings: II.1 · 6 · II.2 · 4 · II.3 · 5 · II.5 · 4 · II.6 · 5 ·
II.7 · 8 · II.8 · 5.

**The chapter that teaches the reader how to grade evidence is the one chapter that shows none.**

⚠ **Why `endnote_debt.py` is blind to it, and this is the interesting half:** that tool counts *named
sources against receipts*. II.4 names no sources. **So its debt is `0/0` and it reports as healthy —
the cleanest chapter in the book by that instrument.** A gauge whose denominator is supplied by the
thing it measures cannot see a chapter that opted out of being measured.
[[feedback_self_generated_denominator]] · [[feedback_zero_needs_a_positive_control]]

**Owed:** either receipts for II.4's load-bearing claims, or an explicit statement — in the chapter —
of why the grade chapter argues from structure rather than authority. **The second is a legitimate
answer and may be the better one.** What is not legitimate is the current state, where the absence is
undeclared and reads as an oversight.

**TRIGGER: the Book VII revision pass, in the sitting that opens II.4's grade chapter.** ⛔ **FIRED UNOBSERVED — SHIPPED UNGUARDED, now a defect.** ⛔ It named the floor row as its gate, that row was **paid Day 195**, and **this one was not paid with it** — the floor got its grade axis and the grade chapter still has no receipts. Same defect, and only one end of it was repaired. The floor that does not slope and the grade chapter with no grades are one argument. small.

---

## R-235 — 19 OF 43 CARDS ARE OUTWARD AND UNGRADED FOR REACHABILITY

**MEDIUM. Opened BY R-136's repair, which is the honest way for a row to arrive — the fix raised the
standard and the older cards have not been read against the new one.**

`IV.1` now requires a complement that could actually be reached — *a person, a tradition, an
instrument, a species you can go and watch* — and states that the field carries that obligation. **The
25 v1 cards were written before the obligation existed and mostly answer with an existence claim:**
*"Anything with a second dimension"* · *"Everything"* · *"Anything with a seat"* · *"Anything that can
go and look"*. Those are true, they discharge the anti-ranking job, and **they do not tell a reader
standing in the null space where to go**, which is what the fifth line promises them.

✅ **Five of the 25 already pass and are ruled `reachable`:** `IV.3`'s *its own bees*, `IV.5`'s
*anyone who has left*, `IV.7`'s *every reader*, `VI.2`'s *population epidemiology*, `VI.3`'s *every
tradition in Book V*. **One is ruled `n/a`** — `IV.8`'s explicit refusal, which is a ruling and not a
gap. **That leaves 19, named individually by `tools/complement_referent.py` on every run.**

⚠ **The instrument does NOT report this as a failure and that is deliberate**, because an ungraded
card is not a defective card — nobody has looked. The registry keeps `reach` as five values rather
than a boolean for exactly this reason: *graded and out of reach* (`VI.6`) and *nobody looked* are
opposite epistemic states, and a boolean prints them as one number, **which is the collapse the whole
instrument exists because of.** [[feedback_field_keeps_name_swaps_referent]]

⛔ **Do not batch-rewrite these.** `IV.1` leaves the thermostat card in the weak form on purpose, so
the difference between the two is visible where the card is introduced — at least one weak instance
must survive, and which ones are *legitimately* generic (a mineral's complement really is close to
*everything*) is a judgement per card, not a sweep. **The first act on each is to read the field body,
which is the one thing the D195 pass did not do for these 19.**

**TRIGGER: the Book IV revision pass — these are all Book IV/V/VI.1 cards and they should be read in
the sitting that opens those chapters, not as a separate errand.** medium.
