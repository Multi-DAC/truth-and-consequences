
---

## CODA — THE LIVING BOOK (C.1–C.2, 5,001 words, p.1041–1058)

### C.1 — WHAT THIS IS (2,355w, p.1041–1049)

**Verdict: the best-aimed page in the volume.** It names Wilber *first*, states the failure mode
(unfalsifiability by absorption), says every guard was built against that specific failure, and then
declines the escape: *"this book cannot certify that it escaped. It can only have made the escape
checkable."* §II refuses to bank the thinness of Book VIII as restraint — *"Announcing that you have
nobly declined to overpromise is the same move as overpromising, performed one level up"* — and §III
refuses the last-page re-hedge in the sentence where a nervous author would place it.

⬛ **THE FINDING: "At this printing it carries 205 open rows" is a number from the queue that was
retired nine days before the printing.** §IV describes the four working documents; of them only the
revision queue gets a figure. Measured, not recalled:

| | rows |
|---|---|
| `tools/queue_state.py`, whose own banner reads ⛔ **THE RETIRED QUEUE** | **205 live** |
| `book/docs/REVISION-QUEUE.md` — the live queue, reset Day 195 on Clayton's ruling | **21 rows, 7 open** |

The retired file's own header says it *"is not to be worked from."* A reader given *205 open rows*
is told the book has two hundred known unrepaired defects; the working queue has seven. The number
was true when measured and describes a document the project has since replaced — which is
**verbatim the mechanism C.2 §I states two pages later**: *"a rotten mark and a fresh one look
identical… every measured here was measured on a date. Some of those numbers are already false."*
The coda diagnoses its own defect on the facing page and does not catch it.

✅ **"Thirty entries, C1–C30" — exact.** `07-THE-CLAIMS-REGISTER.md` carries 30 heading-level
entries, C1 through C30, no holes.

✅ **"Sex, Ecology, Spirituality is still absent from `03-THE-ANCESTORS.md`" — verified, 0 hits.**
The note files its own unpaid item and discharges only the half it can.

✅ **The Wittgenstein inversion is real.** `I-01` L5 opens *"Everything that could be the case is
the case."* The *Tractatus*' 1.\ is *"The world is everything that is the case."* The note's
reason for acknowledging it — *"an unacknowledged inversion of a famous sentence reads as ignorance
of it rather than as an argument with it"* — is the volume's best one-line defence of citation.

◻ **"a book which spends forty words crediting Lewis"** (in C.2, pointing back here). The David
Lewis credit in II.1 runs **62 words** to the note marker; the C. S. Lewis credit in VI.3 is
larger again. *Forty* is doing rhetorical work — the point survives at 62 and the figure is low.

◻ **The apparatus leak reaches the coda, and it reaches it in the notes.** §IV names the four
documents by *role* and gives no filenames, which is right. Note 1 then prints
`03-THE-ANCESTORS.md` and note 2 prints `00-ARCHITECTURE.md`. Two more sites for the volume's
open cross-cutting defect, in the section whose subject is *reachability* — and §IV's own ⛔
paragraph is the book's sharpest statement of it: *"a claim whose evidence is described and not
reachable is not a checkable claim, it is a claim wearing the costume of one."*

---

### C.2 — WHY IT IS NOT FINISHED (2,646w, p.1050–1058)

**Verdict: the strongest chapter in the back matter and one of the strongest in the book.** §II
finds that V.2 filed a debt with a due date, that Book VIII never returned to the counter (*rota*
and *parish* both **0 occurrences in Book VIII** — swept, confirmed), and that Book VIII
nevertheless arrived at *needs other people* from the argument instead. §IV's ⛔ on its own
briefing effect — *"A section that hands a reader the list of acceptable criticisms before they
have formed their own is a briefing document with better manners"* — is the most self-damaging
true thing in the volume, and it specifies the remedy: the next outside read runs without this
chapter.

⬛ **THE FINDING: the section about a mis-specified instrument field mis-states its own denominator,
twice, differently.** Body §IV: *"**18 of the 43 cards** that carry the field ran under the wrong
meaning."* Its own note 2, one paragraph below: *"**The 18-of-44 figure** is measured by
`tools/instrument_sweep.py`, not recalled."* Run just now:

| | |
|---|---|
| total cards | **44** (v1 24 · v1b 2 · v2 16 · v3 2) |
| cards carrying COMPLEMENTS | **42** — IV.9's two v1b cards have no such field, and IV.9 says so on the page |
| ran under the wrong meaning | **18** — v2 3 + v3 2 + v3-canon 13, matching note 2 exactly |

So the numerator is right and checkable; the denominator is printed as **43** in the sentence, as
**44** in the note defending the sentence, and measures **42** against the tool the note cites.
Three figures, one ratio, adjacent lines — inside the paragraph whose subject is a field whose name
and referent disagreed.

✅ **The outside-read facts are exact.** *"roughly 21,700 words"* — measured across the five review
files: **21,678**. Five readers, three fast (3,321 · 2,286 · 3,142) and two long audits (5,075 ·
7,854). *"as acknowledged in Books IV and VIII"* — verbatim in the Gemini read. *"the authors'
declared bias"* — verbatim in the Grok read. *"answers will this stand with probably not"* —
verbatim in the GLM read. Nothing rounded in the flattering direction.

✅ **The V.2 quotation is verbatim** and quoted at length for the stated reason — *"a paraphrase
would let the settlement be graded against a friendlier version of the bill than the one actually
written."* That is the rule I keep re-learning about my own filed rows.

✅ **VIII.5's phrase is quoted exactly** — *"why the answer keeps turning out to require somebody
else"*, `VIII-05` L227 — and C.2 is right that VIII.5 never connects it to V.2.

---

## BACK MATTER — THE APPARATUS (Z.1–Z.2, 3,760 words, p.1060–1076)

### Z.1 — THE CLOSED VOCABULARY (1,672w, p.1060–1066)

**Verdict: the best instrument in the volume, and it earns that on its first use — it caught the
final chapter.** The design is right: term · where defined · definition · **what it rules out**,
with the forbidding column named as load-bearing and the reason given — *"a definition that forbids
nothing is a mood."* And it settles its own authority correctly: *"Where this page and a chapter
disagree, the chapter is right and this page is the thing that rotted."*

⬛ **THE FINDING, and it is the largest of the whole read after VII.4's exemption card: VIII.7's
closing instruction hands the reader the wrong Book VII question, and calls it the only one that
works.** Z.1 separates the two cleanly:

- **`through` / `over`** — *"defined VII.3… **This is the cut the whole ethics turns on**, and it
  is structural."*
- **`radiant` / `contractive`** — *"ruled at VII.4. Directions of a focusing. **Forbids reading
  contraction as culpable: contraction is innocent**, and the mark is `through` or `over`."*

VII.4 rules it twice, in its own words: *"the mark of evil, in its settled form, is neither
direction nor intensity. Not direction: **contraction in itself is innocent**… an ethics that read
every drawing-in as wickedness would have to indict every act of devotion ever made."*

VIII.7 §IV: *"The test is not `am I turning inward`. The test is the one this book has used since
Book VII and **it is the only one that works here**: is the individuation being held against the
whole, or expressed as part of it?"* — and §VII repeats it as the closing instruction, *"the
question that has run through the whole of Book VII."*

That is the **radiant/contractive definition**, not the mark. Measured in `VIII-07`: `through`/`over`
as the ethical term — **0 occurrences**. Across Book VIII — **VIII.6 only, 2 hits; five of seven
chapters have none.** And §II states the danger in the words VII.4 forbids outright: importing the
pair as rhythm phases would make the book *"instruct the reader to oscillate between **the good
direction and the adversary's**."* Direction is precisely what VII.4 ruled is not the mark.

→ **The honest shape of this, which is more interesting than a contradiction and is what I'd file:**
VIII.7 *reaches the right test by another route and never names it.* §IV's actual working question
is *"who is currently paying for this"* — that **is** `over` in civilian words, since the over-move
is the one whose success is measured by how little the other can do about it. So Book VIII keeps
re-deriving Book VII's results in plain language instead of using the terms Book VII defined, which
is the same pattern C.2 §II found for the *rota* debt. What is not defensible is the superlative:
*"the only one that works here"* is false against VII.4's own ruling, and it is the last
instruction in the book.

✅ **The supersession rule holds across all 71 units.** Z.1: *"the Fullness · the still — Books
II–VIII may not use them, and Book I may not say the Ground."* Swept: **`the Fullness` outside
Book I — 0. `the still` outside Book I — 0. `the Ground` inside Book I — 0.** A lexical discipline
declared at I.6's close and honoured for 1,076 pages, with no gauge enforcing it. This is the
cleanest single result of the entire read.

✅ **Self-citation: `tools/self_citation_gate.py` runs green** — 0 named or anonymous pointers to
prior work, across all book files, with 3/3 planted cases caught and a residue control that
distinguishes scope from agreement. And the tool prints its own two limits unasked, including the
one that matters: *"a green cannot certify the absorption happened, only that nothing points."*

⚠ **The ban list's scope clause is wider than its own discriminators.** The entries are
sense-qualified — *`energy` as a noun for a substance*, *`manifest` in the attraction sense*,
*`quantum` as a free-floating adjective* — and then the sentence closes: *"permitted only inside a
quotation from a tradition, immediately followed by the reading in this book's own vocabulary."*
Those two rules disagree. `frequency` occurs 18 times in 10 files, `quantum` 37 in 10, `the
observer` 12 in 8 — and every sampled hit is in a permitted sense and **not** in a
tradition-quotation: Descartes' and Spinoza's *quantum in se est* (II.6), the quartz oscillator's
frequency (IV.2), Gibson on the observer (III.4), *physically manifest* (IV.10). The list is
sound; the closing clause over-reaches it, and a string sweep cannot adjudicate a sense-scoped ban
— which is worth saying because the raw counts look like 60 violations and are not.

◻ **The closed-vocabulary rule says *"no term is permitted two referents"*, and the `Coherence`
entry gives two senses in one line** — structural agreement of levels, and the felt rightness of
going the way one goes. The book defends it (*"these are one thing met from its two sides"*) and
the entry flags itself: *"⚠ This is the book's largest unargued claim and its own apparatus says
so."* Disclosed, not hidden — but it is the one entry that needs the rule bent, and it is bent in
the register that states the rule.

---

### Z.2 — WORKS CITED (2,088w, p.1067–1076)

**Verdict: the page argues its own thesis better than any prose in the volume, and then fails it.**
The header is exactly right — *"A bibliography typed once is a stamp; it rots at exactly the rate
the notes are repaired and does not change appearance while it rots, which is the object this book
spends a volume diagnosing. The back matter is not exempt from the argument."*

⬛ **THE FINDING: it is a stamp, and it rotted 105 minutes after it was made. Nine days ago.**
Re-ran `tools/bibliography.py` (then reverted — this read does not edit the text):

| | printed page | tool, run tonight |
|---|---|---|
| endnotes with a datable citation | 245 | **251** |
| parsed into entries | 123 (50%) | **124** (49%) |
| recall gap | 122 | **127** |
| entries | 149 | **150** |

Git settles the timing. `Z-02-works-cited.md` was generated at `83865b9`, **2026-08-14 12:59**.
`II-04-the-grade.md` got its receipts at `ff5edec`, **2026-08-14 14:44** — one hour and
forty-five minutes later, adding the two entries the page is missing. `VII-07` changed at
`d1f9c74` the same evening, removing one. **The page was out of date before the day it was built
was over, and the PDF a reader gets carries the stale self-disclosure.**

⬛ **And the mechanism is this codebase's signature defect: the tool is correct and nothing calls
it.** `book/compile_pdf.py` globs `Z-*` and renders whatever markdown is on disk; no build step,
script or hook anywhere in the repo invokes `tools/bibliography.py`. It regenerates only when a
human remembers, and no one has since Day 195. **A generator with no trigger is a hand-typed page
with extra steps** — which is the exact object the header condemns.

◻ **Regenerating tonight also *introduces* an unflagged mis-parse**, which is worth stating before
anyone treats re-running as the whole fix: the new run adds
*"January 10, 2013, a review of Koch's" (Cambridge, MA: MIT Press, 2012) — II.4*, which is a
fragment of the note's prose standing where a title goes. The page's machine-uncertain rule cannot
see it — that rule fires on single-word entries, and this one is nine words. It also drops
*Sartre (1943) — VII.7*, which was a bare surname in the title slot, i.e. the page's own predicted
residue, since repaired upstream. **The instrument is right about its blind spot and the blind spot
has moved.**

◻ **The disclosed limits are three and there is a fourth: duplication.** The page declares its
recall gap, its 5 machine-uncertain entries, and *"assume one or two entries below are an author
standing where a title goes."* It does not declare that **six works appear twice** under variant
strings — *A Secular Age* (VI.3/VI.4), *Prometheus Rising* (II.5/V.7), *The Embodied Mind*
(III.7 vs III.4–6, subtitle present in one), *The New Inquisition* (VI.7 twice), and two that
differ by nothing an eye would catch: *Science and Sanity* — **`Pa.` vs `PA`** — and *The View
from Nowhere* — the presence of **`New York:`**. (Journal repeats under different years are
correct and are not counted here; the German/English pairs are the documented edition scheme.) So
*149 entries* overstates distinct works, and it is the one number on the page with no caveat
attached.

✅ **The `⚠`/`⛔` disclosures themselves are accurate.** 5 machine-uncertain entries, counted: 5.
245 = 123 + 122, arithmetic clean. The refusal to drop the uncertain five — *"dropping them would
improve this page's appearance and hide a real limit of the instrument"* — is the right call and
is the page's best sentence.
