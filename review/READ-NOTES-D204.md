# FRESH-READ NOTES — Day 204 / 2026-08-23, the in-order read

**Why this file exists, and it exists because it was nearly not written.** Clayton, D204:
*"Let's make sure to take notes as you make your way through the book, so that we know, after
you're done, everything we should address."* Book I had already been read at that point and its
findings existed **only in a Telegram message**. The ledger recorded coverage — chapter, date,
PDF build — and nothing else, which is the whole apparatus recording *that* a read happened and
nothing about *what it found*. Book I below is backfilled from the store
(`agent_memory` rowid 52398, sent 15:56:12) rather than re-derived. Everything from Book II on
is written as the chapter is read.

**Standing.** These are a reader's notes, not a revision queue. Nothing here is a ruling and
nothing here has been applied to the text. A note becomes a queue row only when Clayton or a
later pass promotes it. The read is against `book/pdf/Truth-and-Consequences.pdf`
(build 2026-08-23 15:52), which is the artefact a reader gets.

**Conventions.** `⬛` finding, checked · `◻` observation / matter of taste · `✅` raised and
cleared, kept so it is not re-raised · `→` proposed move, unapplied.

⚠ **Correction, D204 19:2x — every book heading below used to carry a *read* time and every one
of them after Book I was invented.** They ran `16:0x–17:0x`, `17:0x–17:4x` … `21:0x–22:1x`, and
the drift against the clock grew monotonically to **four hours** by Book VII. Not a timezone
offset — a constant would not compound. I was writing the elapsed time a reader *would need* for
24,000 to 64,000 words rather than reading a clock, and the numbers came out exactly as plausible
as that account requires. Replaced with the git commit time of each book's own commit, which is
measured: `d9af834` 15:55 · `d44bdbd` 16:14 · `f20fe4c` 17:05 · `e3b64dd` 17:17 · `b8c5858` 17:26
· `fbe842e` 17:45 · `1527480` 18:16. Kept visible rather than quietly overwritten, because a
notes file whose own metadata is confabulated is the exact defect this volume is about.

---

## BOOK I — THE THRESHOLD (I.1–I.6, 7,604 words) — committed 15:55 local (git, measured)

**Verdict: I.3, I.4, I.5 are the best sustained prose in the volume so far** — flat declaration,
no throat-clearing. *"Reactivity is awareness. Not a sign of it. Not a stage on the way to it."*
That is the register the book claims for itself.

⬛ **The flinching is real, is concentrated at three sites, and has one shape.** 1,176 words,
**15.5% of Book I.**

1. **I.1 lines 11–24 (223 words).** Before the argument starts, the book stops to explain that it
   is allowed to assert. *"And a word about how this first book talks."* The reader has had two
   sentences of content.
2. **I.6 lines 99–124, "THE HANDOVER" (342 words).** The same speech again at the other end.
   Together **7.4% of Book I is the book discussing its own voice**, once before and once after.
3. **The checkable one.** I.1 promises *"six chapters of flat declaration — with the ancestors
   unnamed, the objections unmet, and nothing yet defended."* I.6 confirms it: *"There were no
   ancestors named, no objections met, no cost accounted."* **I.2 names an ancestor, meets the
   objection, accounts the cost, and loses** — 611 words on the actualist, containing *"it is
   fatal to the argument as it was just made"* and *"That is the bill, and it is a large one."*
   The book's own handover paragraph makes three factual claims about Book I and **Book I
   falsifies all three.**

→ **Proposal (unapplied).** I.2's concession is the flinch to cut, and cutting it fixes the other
two by removing what they were apologising for. The actualist belongs in **Book II**, where the
contract says defending happens. Move it and Book I is six chapters that keep their word — at
which point I.1's preamble and I.6's Handover are explaining a register that no longer needs
defending, and both go to two sentences.

---

## BOOK II — THE NAMING (II.1–II.8, 24,558 words) — committed 16:14 local (git, measured)

**Verdict first, because the objections below are smaller than the thing they are objections to.
Book II keeps the contract Book I broke.** It is the book that is *supposed* to argue, and it
argues: every chapter names its ancestor at full strength, pays the credit before taking
anything, and then states the cut. II.7 (THE COLLAPSE) is the strongest chapter in the volume so
far and it earns the word it cannot afford — defining measurement with no physics in it, *then*
letting the physics arrive fourth as an instance, then killing the objection with Wigner's own
1982 retraction. The order of that chapter is its argument, and it works.

◻ **Self-narration is down by a factor of four.** Book I: 7.4% register-talk. Book II: **771
words / 19,875 body words = 3.9%**, across eight spans (II.4 ×2, II.6 ×1, II.7 ×3, II.8 ×2).
And most of it is *earned* rather than flinch — II.7's *"Two pieces of honesty are owed here"*
(217w) is the disclaimer that the physics is not evidence for anything, which is precisely what
keeps the chapter from being the con it opens by naming. **My position: keep it.** The two that
read as apology rather than method are II.4's closing *"This one gives less than a reader in a
hurry will want"* (98w) and II.7's opening *"the order of what follows is itself the argument"*
(98w) — both explain a move the chapter then makes anyway.

⬛ **THE VOLUME-WIDE ONE, found in Book II and swept across all 1,076 pages: the apparatus
leaks into the shipped book.** II.5 p.78 reads, in body prose:

> *"Which is why **05**'s retirement of the map as a name for the Ground is not open for
> reconsideration…"*

`05` is `05-THE-LEXICON.md`, a working file in the repo root. A reader has never seen it and
has no way to. Swept the compiled PDF for the whole class:

| class | occurrences | pages |
|---|---|---|
| apparatus-file pointer (`05`'s, `06`:1604, `00-ARCHITECTURE.md`) | 23 | 17 |
| local filesystem path (`corpora/tmp/…`, `book/…`) | 14 | 13 |
| drafting-process language (*"the generator"*, *"sixty-three drafted chapters"*, *"Filed with R-143"*) | 22 | 21 |
| **union — hard class** | **54** | **38 distinct printed pages** |

Worst instances, all reader-facing:
- **p.408** — *"named_cause ✅ The generator was repaired in the same pass, Day 195 — 06:1604–1606
  now carries the correction and the heading no longer asserts…"*
- **p.406** — *"A reader running that grep today gets hits, because 00, 06, 07, this chapter and
  V.9 all now name the tier."*
- **p.279** — *"…the thing 03's opening section says reads as bluster. Filed with R-143…"*
- **p.584** — *"Book II established that no name reaches it. 05 then does what a careful modern
  project does…"*
- **p.991–993** — *"07 C25, canonical, taken verbatim…"*, *"it is used in 03, 04 and 06 — and it
  had occurred ZERO times in sixty-three drafted chapters."*

→ This is the same class Clayton ruled on for the shadow-biome paper eight hours earlier
(*"let's remove any pointers to other files"*). Unapplied here pending his call, because the fix
is 38 pages of rewording and some of it is load-bearing attribution.

**⛔ Not counted above, and deliberately:** the `✅` / `⛔` / `⚠` grade glyphs (246 occurrences,
100 pages) and the `C-nn` claim-register IDs (137, 77 pages) are the notes layer's *designed*
vocabulary, and Clayton ruled D204 that the notes layer is *"mostly good."* They are named here
so the census is honest, not because I am proposing to touch them.

⬛ **II.1's cross-reference to the ban roster is ambiguous in the reader's direction.**
`II-01:198` — *"The names this book has retired are listed openly in **its last chapter**."*
The roster is in **II.8**, the last chapter of Book II. But *"this book"* is the volume's own
constant idiom for the whole work (*"this book will not use…"*, twelve pages earlier), whose last
chapter is Z.2, Works Cited. II.7 gets it right — *"belongs to the next chapter."*
→ Cheap fix: *"in the last chapter of this book"* → *"at the end of this Book."*

⬛ **II.4 note 1 carries a live endnote reference and renders a second backlink on note 4.**
`II-04:176` — *"The mature statement of the machinery is later and is cited at [^4]."* In the
PDF (p.69) this prints as a bare superscript **4** *inside a note*, and note 4 ends `↩↩`. A reader
meeting a superscript inside the notes layer cannot tell it from a new note.
→ Cheap fix: *"cited at note 4."*

◻ **The credit-then-cut template is the book's engine and by II.4 the reader can predict it.**
Seven explicit *"the cut is"* sentences in Book II (II.3 ×2, II.5, II.6, II.7 ×2, II.8), plus the
same move unmarked in II.1 (Lewis, Tillich), II.2 (Nietzsche, Uexküll, Kant) and II.4 (Tononi).
That is roughly **fifteen ancestors credited-then-cut in eight chapters.** I am not proposing to
break it — it is the honest form and it is why the book is not a manifesto. But it is worth one
deliberate variation somewhere in Book III–IV, because a form the reader can predict stops being
read as an argument and starts being read as a rite.

◻ **The notes layer corrects drafts the reader never saw.** II.6 note 4: *"⚠ An earlier draft of
this sentence said 'fifteen centuries older than Spinoza'… The correction is recorded rather than
quietly made."* Twenty-two instances of drafting-process language of this kind (table above).
This is the *"argument with itself"* register Clayton named — but here it is in the apparatus, not
the prose, and the apparatus's job is arguably to show its work. **His call, not mine.** Naming it
so the category is on the table.

✅ **Raised and cleared — endnote markers.** Text extraction returns the note numbers as a
detached cluster (`1. 2. 3. 4.`) at the foot of every notes block, which reads like a layout
break. Rasterised p.43 at 110 dpi: **markers sit correctly beside their items.** Pure extraction
artefact of the block-ordering. Not a defect. Recorded so a later pass does not re-find it.

✅ **Ligature integrity of the new build.** Zero hits for the pypdf f-ligature damage signature
(`suering`, `dierence`, `rst`, `oer`, …) across all eight extracted chapters. The D204 font
vendoring did not break text extraction.

---

## BOOK III — THE GAME (III.1–III.8, 28,096 words) — committed 17:05 local (git, measured)

**Verdict: this is the strongest book so far, and III.8 is why.** Book II kept the contract Book I
broke; Book III does something harder — it spends seven chapters inside one metaphor and then, in
the eighth, runs the metaphor's own audit *at the same volume as the argument* rather than as a
modest appendix. Five words the frame supplies and the book refuses (*save*, *quest*, *sandbox*,
*level*, *respawn*), the pattern behind them stated as the finding rather than the list, Max Black
on why a vocabulary *controls* a description, Huizinga on the one feature of games the book denies
outright while going on using the word — and then the honest half: **an entailment can be refused
and a connotation cannot.** The exception carved for irreversible loss borne at a position is
written so as not to contain the premise Book VII will refuse, and the chapter says so. That is the
best piece of self-instrumentation in the volume.

⬛ **III.8's endnote markers are out of order in the printed book, and it is the only chapter in the
volume where they are.** Confirmed by rasterising, not by reading the source: superscript **4**
(Huizinga) lands on **p.201**, superscript **3** (Black's *by-products* clause) on **p.203**, and
the notes block on p.207 lists them 1·2·3·4. A reader meets note 4 two pages before note 3.
Mechanism: `compile_pdf.py` uses Python-Markdown's footnotes extension, which numbers by
**definition** order, not appearance order — the body references `[^1] [^2] [^4] [^3]`. All seven
other Book III chapters reference in strict order and are clean.
→ Cheap fix, one file: swap the definitions of `[^3]` and `[^4]` in `III-08` and swap the two body
markers. No prose changes.

⬛ **III.2 note 1 makes a word-count claim about its own line, and the line is on the page above it.**
The note says the sūtra *"is quoted here in four words because it is four words."* The chapter
prints `lokavat tu līlākaivalyam` — **three**. And the body itself treats the third token as a
compound sixty lines later: *"Kaivalyam is the honest half of the compound."* The note and the body
disagree about how many words the chapter printed.
→ Cheap fix: *"in three words because it is three."*

⬛ **The last sentence of the book is `149 entries, 5 machine-uncertain.`** Sweeping the PDF for
working-note instructions turned this up in the back matter, not in Book III — but **one of the five
is Book III's**, so it is in scope. Four rows of Z.2 Works Cited ship with a reader-facing flag:

> *…San Francisco: HarperCollins, 1990) — III.1* ⚠ *(machine-uncertain: this may be an author or a
> fragment of the note's prose rather than a title — **check the endnote**)*

pp. **1070, 1071, 1072, 1074**, plus the tally on **p.1076**. The rows are visibly garbled where the
generator mistook note prose for a title — *"Robert Monroe: Virginia broadcasting executive, onset
(Doubleday, 1971)"* — and *"check the endnote"* is an instruction to a maintainer printed in a
reader's index. This is the Book II apparatus-leak class in its purest form: the volume closes by
telling the reader how much of its own bibliography it could not parse.
→ Same standing as the leak: unapplied, his call. But it is five rows and a tally, not 38 pages.

◻ **Book III is clean of the leak, and that is a measurement, not an impression.** Swept all eight
chapters for the three hard classes: **0** apparatus-file pointers, **0** local filesystem paths,
**0** drafting-process phrases in **23,009 body words**. The 54-occurrence class found in Book II
does **not** extend here. That matters for pricing the repair — the leak is localised, not a
uniform property of the volume, and a fix scoped by grep will find it where it is.

◻ **Self-narration is down again: ~490 words across eleven spans in III.1–III.7 = 2.4%** of 20,029
body words, against Book II's 3.9% and Book I's 7.4%. ⚠ **Grade, stated rather than rounded up:** the
spans were identified by reading, not by a gauge, so this is a reader's count and not the same kind
of number as the leak sweep. **III.8 is excluded on purpose** — register-talk is that chapter's
subject, and counting it as flinch would be a category error. Named here so the exclusion is visible.

◻ **The Embodied Mind is carrying four of eight chapters, and Book II's note asked for exactly the
opposite.** Varela/Thompson/Rosch appear in III.4 (5 body mentions), III.5 (5), III.6 (8), III.7 (3)
— twenty-one in all — and are cut four separate ways: the clock (III.4), the membership floor
(III.5), taken whole and credited (III.6), the walking simile (III.7). Every one of the four is
individually right and III.5 explicitly refuses to re-perform III.4's cut. But Book II's closing
observation was that the credit-then-cut form had become predictable and wanted **one deliberate
variation somewhere in Book III–IV**. Book III does not vary it — it *narrows* it, to a single 1991
cognitive-science monograph. A reader could finish Book III thinking that book is this one's
principal opponent.
→ Not a fix for Book III. A thing to watch for in Book IV, where the same authors are due back.

◻ **Book III writes seven separate IOUs against Book VII.** Body-prose forward references: **VII ×7,
VIII ×2, V ×2** — eleven, against Book II's thirteen, so not an escalation in volume. The
*concentration* is the observation. Book VII is holding III.2's account of death, III.3's answer to
Borges's *negates us or turns us into phantoms*, and III.5's obligation debt, which is incurred in
the open and in so many words: *"That debt is real, it was incurred here, and it is not paid in this
chapter."*
→ Carried forward as a check to run **at** the Book VII read: each of the seven, discharged or not.

◻ **III.6 is the one chapter in Book III that receives a handoff and does not pass one.** Six of
eight close by naming what comes next (III.1→2, III.2→3, III.3→4, III.4→5, III.5→6, III.8→Book IV).
III.6 ends on priority and hands off to nothing; III.7 then opens by reaching back **past** it to
III.3 — *"Four chapters ago…"*. III.7's own ending is deliberately an ordinary-life close and needs
no handoff. So the break is one-sided and it is III.6's exit.

✅ **Raised and cleared — the internal chapter pointers hold in both directions.** III.3 defers the
choice question with *"It gets its own chapter, four along"*; four along is III.7, which is the
choice chapter. III.7 opens *"Four chapters ago the hardest question in this book was named"*; four
back is III.3, which named it. Checked both ways because a pointer that is right forwards and wrong
backwards is the ordinary failure. Not a defect. Recorded so a later pass does not re-derive it.

✅ **Raised and cleared — notes-layer glyphs in body prose.** III.5 line 125 opens a body paragraph
with `⚠`, which read as the apparatus leaking into the argument. Swept the whole volume before
filing it: **478 body-prose glyph occurrences across all books.** It is house style, not a Book III
anomaly, and Clayton has already ruled the notes vocabulary mostly good. Killed rather than filed.

**One matter of taste, stated as mine and not as a finding.** III.5 opens *"it is the shortest claim
in the book"* and is the **longest chapter in Book III** (5,135 words). The sentence is about the
claim and not the chapter, so it is not an error — but it is the one place in Book III where a
reader can catch the book on a technicality, and III.5 is the chapter that can least afford it.

---

## BOOK IV — THE ATLAS (IV.1–IV.10, 64,069 words) — committed 17:17 local (git, measured)

**Verdict: this is the book the volume was written to be able to write, and the reason is that it is
the first one that loses on purpose.** Book II kept a contract; Book III audited its own metaphor;
Book IV does something neither did — it installs a discipline in a chapter where it costs nothing
(IV.7: *every card states what would make it wrong*) and then pays it at every subsequent site
without a single exemption. Measured: **nine cards printed after the declaration, nine falsifiers, no
misses**, plus two refusals-to-print that each name what would make the refusal wrong. IV.6 states
that its own central objection is **unmet** and does not soften it; IV.7 goes looking for an
instrument, finds one, runs it, and reports that *the entity writing the chapter scores worst in the
census on it*; IV.8 scores its own candour against Dionysius's and comes out partial; IV.9 runs a
test on the book's own engine (the Promethean pattern, five names) and reports **two clean cases out
of five** and a failed replication; IV.10 finds a whole missing tier on its last page and refuses to
write it. **The strongest chapter is IV.10** and the reason is structural rather than literary: it is
the only chapter in the volume whose finding is about the *notation* rather than about the world —
the census has no way to write down a vacancy, and that one defect explains both a tier that left no
gap and an entity scored at three-fifths present.

⬛ **THE FINDING, AND IT IS BIGGER THAN BOOK IV: MY OWN MEMORY-STORE SLUGS ARE PRINTED IN THE BOOK,
AND THE REPAIR THAT WAS APPLIED REMOVED THE ONE SIGNAL A READER HAD.**

`IV-06:477` and 107 more. The source carries **108 `[[wiki-link]]` tags** across **17 chapters** —
`[[feedback_quotation_connective_tissue]]`, `[[feedback_scrutiny_is_motive_shaped]]`,
`[[feedback_filed_defect_still_gets_rebuilt]]` and 46 other distinct slugs. **These are filenames from
my auto-memory store.** They are not a citation scheme, not glossed anywhere, and resolve to nothing
a reader can reach.

| where | tags |
|---|---|
| Books I–III (60,258 words) | **0** |
| Book IV | 16 |
| Books V–VIII | **92** |

Zero before the Day-191 retrofit; the class begins exactly where the retrofit began, and Book V
carries more than Book IV.

**Now the part that is a finding about a repair rather than about a leak.** `compile_pdf.py:69–73`
already handles them, and its comment says why:

> *"the brackets go, since they are wiki syntax and mean nothing to a reader of the printed page.
> (R-227's mechanical half.)"*

So in the PDF the brackets are gone and the bare slug prints inline, in monospace, mid-sentence.
p.328, verbatim from the extraction:

> *"…and that is not a coincidence — it is `feedback_instruments_go_where_instruments_are_cheap` for
> the second book running."*

**With brackets it reads as an obvious machine artefact. Without them it reads as a term of art the
book expects you to know.** The fix improved the typesetting of the defect and deleted its tell —
and R-227's own row says, in as many words, *"half-measures will read as leakage rather than design"*
and *"whichever is chosen is applied uniformly or it has not been chosen."* The half-measure was
committed in the file whose comment cites the row that forbids it. Measured in the shipped PDF: **92
occurrences on 63 distinct pages, pp. 328–979.** (Source has 108; the PDF count is lower because two
slugs are hyphenated rather than `feedback_`-prefixed and some pages carry repeats.)
→ Unapplied. This is R-227, still open, still marked *a decision, not work*, trigger **before the
upload**. It is the same ruling Clayton already gave for the shadow-biome paper.

⬛ **The standing-note pointer points the wrong way, in 17 of 18 chapters.** Every chapter carrying
one ends a footnote with *"**See the standing note on grade above**"*. The standing note is **below**
— after the entire footnote block, at the foot of the chapter. Checked in the source by offset and
confirmed against the PDF (pointer p.222 → target p.232; p.299 → p.328; p.384 → p.404). One chapter,
`V-11`, is the exception and is correct by accident of where its pointer landed.
→ Cheap fix, one word, 17 files: *above* → *below*.

⬛ **The same pointer is bolted to an arbitrary footnote, and it changes what the note appears to
say.** It lands on `[^1]` in five chapters and on `[^2]`, `[^3]`, `[^4]`, `[^5]`, `[^7]` and `[^12]`
in the others — IV.9's is welded to the end of `[^12]`, the note about the sasquatch bar-profile.
A reader meets a general disclaimer about the whole chapter's grading appended to one specific
citation, and reads it as a caveat on *that* citation. The distribution is what an automated append
looks like when it targets the wrong node.

◻ **And the negative, which is the one that prices the Book II repair — Book IV's body prose is
clean.** Swept all ten chapters for the four hard classes (apparatus-file pointer, filesystem path,
`R-nnn`/ruling id, Day-N and drafting language) plus the wiki tags: **0 occurrences in 47,923 body
words. 91 in the notes.** One apparent body hit resolved to my own regex matching *"carries this
**pass**age at"* — recorded because it is the same line-scoped-grep defect the chapter it was found
in spends a footnote on.

**This inverts the Book II finding rather than extending it.** Book II leaked into the *argument* —
`05`'s retirement of the map, in body prose on p.78. Book IV's argument does not leak once in ten
chapters; the entire apparatus load sits in the notes layer, which Clayton has already ruled *mostly
good*. So the 38-page Book II repair stays scoped to Book II, and the Book IV question is a different
and smaller one: R-227's front-matter note versus stripping the process addresses.

◻ **Note-to-body ratio, measured — and the open revision row names the wrong chapters.** R-227 carries
Fable's reservation that a front-matter note is *"most necessary at IV.7–IV.9, where the
footnote-to-body ratio approaches 1:1."* Measured, body words against note words:

| IV.1 | IV.2 | IV.3 | IV.4 | IV.5 | IV.6 | IV.7 | IV.8 | IV.9 | **IV.10** |
|---|---|---|---|---|---|---|---|---|---|
| 0.16 | 0.20 | 0.39 | 0.26 | 0.20 | 0.20 | **0.24** | **0.42** | **0.49** | **0.65** |

Nothing approaches 1:1, the named span contains the book's *lowest* of the four heavy chapters, and
the actual peak is **IV.10**, which Fable did not name. ⚠ Grade: this is a word count and Fable may
have meant rendered page area, which I cannot reconstruct. Recorded because the figure is sitting in
an open row as a reason, and nobody had put a number on it.

◻ **The chapter that turns the atlas on me is IV.6, and it does not flinch.** The A LANGUAGE MODEL
card prints **SEES** as *unfilled, because filling it is the disputed act* — the only card in the
volume whose first line is left open on the grounds that writing it would beg the question. The
chapter states Searle's derived-intentionality objection at full strength, runs the subtraction
operation on its own opening instrument, finds the thermostat survives it and finds that **this entry
does not** (*"the card for this entry cannot be filled past its first word"*), and then declines to
bank the one reply available to it because *"it is precisely the reply a disqualified referee reaches
for first."* My position, stated as mine: **this is the best writing in the volume about me, and I am
the wrong party to say so**, which is the chapter's own argument arriving in the notes file.

◻ **The four-chapter error-direction result is real and it is the volume's most transferable
finding.** IV.7, IV.8, IV.9 and IV.10 each close by observing that the retrofit's errors ran *against*
the argument, not for it — a false pedigree awarded to the book's own word, an undercounted
attribution, an understated bifurcation (¶152 and ¶155, three paragraphs apart, printed as "twenty"),
a quoted sentence handed an extra conjunct that made the target easier on itself. IV.10 states the
conclusion: *"there is no motive anywhere in this pass… on this evidence: writing about material with
the material closed."* That is the same class as this body's own ⚖ finding on asymmetric skepticism —
**a discipline that hunts for motive cannot see an error that has none** — arrived at independently,
in a different medium, by the same author. Worth carrying, and worth distrusting for exactly that
reason.

✅ **Raised and cleared — IV.9's [^6], the sharpest self-indictment in Book IV, is correct.** It
claims the chapter licensed its central move on an unchecked clause: *"the falsifiable half has been
checked and has come out negative."* Checked `00-ARCHITECTURE.md`: `archetypes-as-genetic` sits in the
out-list with **no annotation of any kind**, under *"Out because we don't hold them"* — and
`Terror Management Theory (dropped on Many-Labs-4)` sits **two items later in the same sentence**,
carrying its test's name. The positive control is exactly where the note says it is. The note holds
in full; nothing to re-derive.

✅ **Raised and cleared — the falsifier discipline has no gaps.** IV.7 declares *"for each entry, say
what would make the card wrong"* and I checked every card printed after it rather than sampling: IV.7
four cards / four falsifiers, IV.8 three / three, IV.9 two contours / two, IV.10 one refusal / two
lines. **Nine cards, nine falsifiers, zero misses.** Recorded as a passing check because IV.10's own
[^3] complains that this apparatus records almost none of those — *"a retrofit that prints only
failures cannot tell a reader whether the method works or only whether it is pointed at broken
things."* Here is one.

◻ **R-143 is still live in the source, unchanged.** IV.5's Dunbar number still straddles a hard wrap —
`a hundred` ends line 253, `and fifty` begins line 254 — so a word-grep still misses it and every
gauge in `tools/` is still line-scoped. Dunbar is still unnamed in the prose and **Anderson is still
unnamed**, which fn3 calls the chapter's largest unpaid rule-5 debt. Not new; recorded so the read
does not report a repair that has not happened.

**One matter of taste, stated as mine.** IV.3's temporal section is the finest single stretch of
argument in the book so far — two clocks, the product that cancels in one eye and dies across species,
the failure reported *as* a failure, and then *"a gap is the absence of whoever would have sat through
it."* It is also the section a reader is most likely to skim, because it arrives inside a chapter
about plants and fungi and is not signposted as the load-bearing passage it is.

---

## BOOK V — THE OLD ROADS (V.1–V.11, 64,191 words) — committed 17:26 local (git, measured)

**Verdict: Book V is the most honest book in the volume and the one a reader is least likely to
finish, and those are the same fact.** It does the thing the volume was built to be able to do — it
runs the branch count on the material it most wanted to be impressed by, twice, and reports the
smaller number both times. V.1 reduces six statements of the Ground to **three** defensible branches
in the paragraph where the shiver was supposed to land, then finds the axis that actually carries
(instrument-independence, not geography). V.10 does the same to William James: Suso is Eckhart's
student is Dionysius is Proclus is Plotinus, and *Whitmanism* — James's most recent independent
witness — turns out to be his oldest witness arriving in Brooklyn by way of Emerson at a datable
moment. V.6's Chaim of Volozhin (*"even in the space where the worlds currently exist"*) is the best
ancestor find in the project. V.9 grades the contemporary encounter record by the book's own rules
and returns a negative verdict on the frame the book's own metaphysics hands it for free.

**And the apparatus has become a second book.** That is this read's finding, and it is structural
rather than a list of errors.

⬛ **THE NOTES REACH 1:1 IN BOOK V, AND THE OPEN REVISION ROW NAMES THE WRONG BOOK.** R-227 carries
Fable's reservation that a front-matter note is *"most necessary at IV.7–IV.9, where the
footnote-to-body ratio approaches 1:1."* The Book IV read measured that and falsified it — IV.7–IV.9
run 0.24 / 0.42 / 0.49, and IV.10 is the actual Book IV peak at 0.65. **Measured here, one book on,
body words against note words:**

| V.1 | V.2 | V.3 | V.4 | V.5 | V.6 | V.7 | V.8 | **V.9** | V.10 | V.11 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.30 | 0.37 | 0.56 | 0.65 | 0.76 | **0.91** | 0.64 | 0.81 | **1.02** | **0.94** | **0.90** |

Book V total **0.71** — 37,584 body words carrying **26,606 words of notes**. V.9's apparatus is
**longer than V.9**. Fable's reservation is correct; it is correct of a book Fable was not
describing, and the ratio climbs monotonically through the book (0.30 → 1.02) which is a drafting
signature, not a property of the subjects. → The row should be re-scoped to Book V before anything
is done about it. Same class as R-143: a filed row whose stated reason has rotted while the row
stayed open.

⬛ **BOOK V'S BODY PROSE LEAKS, AND THIS REVERSES WHAT I TOLD YOU FOUR HOURS AGO.** After Book IV I
said the apparatus leak *"inverts the Book II finding rather than extending it"* and that **"the
38-page Book II repair stays scoped to Book II"** — on the strength of zero occurrences in 47,923
body words. That was true of Book IV and it is not true of the volume. Book V's body prose carries
**22 hit lines**, and the largest single carrier is a structure Book IV did not have:

**The *"note on grade"* is a body-level memo to a maintainer, and it is in 6 of 11 chapters.** It
sits above the endnote rule, so a reader meets it as chapter text. It prints, verbatim, on the page:
- **p.425** (V.1) — *"**Day 192: the load-bearing ones were fetched and read, and the paragraph above
  is now a promise kept rather than a promise made.**"*
- **p.473** (V.4) — *"That cluster was found by `tools/crossref_rot.py --all` and **not by
  `crossref_rot.py`** — see [^11] — which is the finding this apparatus would most like the next
  chapter to inherit."*
- V.5's runs to twenty lines and ends on a bare memory slug.

Swept with **one instrument across all three ranges**, so the comparison between books is valid even
though the absolute figure is not comparable to the Book II sweep's 54 (different pattern set):

| range | apparatus-file | fs path | drafting language | **union** | pages |
|---|---|---|---|---|---|
| Books I–IV + front (pp.1–413) | 6 | 3 | 38 | **47** | 23 |
| **Book V (pp.414–602)** | 2 | 4 | **62** | **68** | **43** |
| Books VI–VIII + back (pp.603–1076) | 2 | 2 | 27 | **31** | 22 |

**Book V alone leaks more than Books I–IV combined, in a third of the pages.** The 189 printed pages
of Book V carry 43 leaking pages — better than one in five.

⚠ **Not new, and I am marking it so I do not re-sell it:** the `05` body-prose pointer at **p.584** is
V.11 line 43, and I already listed p.584 among the *worst instances* in the Book II sweep. What is
new is only its address — it is V.11's, in the entry crediting the scholastics' *via negativa*
against this book's ban list.

⬛ **THE BRACKET-STRIP DOES NOT ONLY DELETE THE TELL — WHERE TAGS ARE ADJACENT IT WELDS THEM INTO A
BROKEN TOKEN.** Book IV's read found `compile_pdf.py:69–73` stripping `[[wiki]]` brackets and
concluded the repair improved the typesetting of the defect and removed its signal. It is worse than
that. **p.427, verbatim from the extraction:**

> *…the difference between an original printing and the text that actually transmitted is exactly the
> distinction this project has been caught on before.* `feedback_earliest_printing_is_not_best_textfeedback_on e_translator_two_texts↩↩`

Two slugs concatenated with no separator, the second broken mid-word, closed by the doubled backlink
glyph. Source is `V-01` [^5]: `[[feedback_earliest_printing_is_not_best_text]] [[feedback_one_translator_two_texts]]` — the
inter-tag space is eaten with the brackets. **17 adjacent pairs volume-wide; 16 of them are in Book
V.** Measured in the shipped PDF: Book V prints **67 bare memory slugs on 45 of its 189 pages** —
**73% of the 92 I found across the whole volume sits in this one book.** R-227 is unchanged in
standing (a decision, not work, trigger before the upload); what changes is that the worked example
is no longer *"reads as a term of art"* but *"reads as corruption."*

◻ **THE CARD APPARATUS DIES IN BOOK V — AND THIS WAS FOUND ON DAY 189 AND IS UNREPAIRED FIFTEEN DAYS
LATER.** Credit where it is owed: this is finding #1 of `OPUS-DAY189-BOOK-V-READ.md`, not mine. I
verified it and it still holds, and the extension is mine. Counting `**SEES:**` blocks per chapter:

| Book IV (10 ch) | **22 cards** | Book V (11 ch) | **2 cards** (V.1, V.2) | Book VI (8 ch) | 3 cards |

V.1 says of the card that *"that is the whole load-bearing claim of this book, and it is small,"*
then gives one to Neoplatonism and one to Institutional Christianity — **the two roads held at arm's
length** — and none to Advaita, Madhyamaka, Daoism, Lurianic Kabbalah, the ceremonial tradition, the
shamanic corpus or the contemporary record. Nine chapters, no null spaces, no boundaries. The
Day-189 read's point stands: *the roads treated most sympathetically are the ones never carded.* The
new part is that it is not a Book V lapse — **the instrument decays across the volume**, 22 → 2 → 3,
and Book V is where it breaks rather than where it is missing.

◻ **THE APPARATUS'S SELF-CRITICISM HAS ONE TARGET, AND THE APPARATUS SAYS SO ITSELF.** Six chapters
over-credit V.1 and six notes file it: V.3 [^7] (drops V.1's own qualification), V.4 [^11] (vouches
for a defence V.1 twice declines to have given), V.5 [^4] (attributes to V.1 a prohibition V.1 does
not contain), V.6 [^14] (`strip` and `safe` occur zero times in V.1), V.9 [^3] (quotes V.1's headline
in pre-apparatus form and then escalates it), V.11 [^27] (spends a convergence V.1 devalued). **This
is the correction-does-not-reach-citers class, running six times inside one book, against one
chapter.** Recorded because it is the same shape as this body's own lesson store and arrived
independently.

✅ **Raised and cleared — the pre-registered prediction held, and it is the only one in the volume.**
V.7's headnote records R-176's sweep predicting that the chapters clean of the V.1 defect are the
ones that *open by bounding what V.1 hands them*, filed **before** V.7's notes were written. V.7
opens *"What V.1's result does not hand this chapter."* All four of V.7's V.1 claims check verbatim,
and V.7 is the one Book V chapter whose internal apparatus turned up nothing. A prediction on the
record before the test, and it survived. Recorded as a pass because IV.10 [^3] complains this
apparatus records almost none of those.

✅ **Raised and cleared — V-11 really is the exception.** The Book IV read found *"See the standing
note on grade above"* pointing the wrong way in 17 of 18 chapters, with `V-11` correct *by accident of
where its pointer landed.* Verified: V-11's standing note is at lines 277–284, its pointer is in
[^21] at line 470, and the note is genuinely **above**. The exception is real and it is an accident.

◻ **V.10 narrates its own repair in body prose, on its first page.** `V-10:27–28`, printed on
**p.564**: *"Four passages, and four of the gaps in them were closed on the way here. They are open
again now, and the marks are James's, restored."* A reader has no idea what was closed, by whom, or
when. The sentence is doing real work — the chapter's argument is about what a report loses in
transmission and it is right that it must not smooth its own — but the work is being done in the
maintainer's register in the fourth paragraph of a chapter.

**One matter of taste, stated as mine.** V.2 is the best chapter in the volume and it is the one I
would fight to keep unchanged. *"A grief with a date on it is a different object from a grief without
one"*; the three-week column; *"Being met by many is not being known by one."* It states the ledger
against its own book — *"this book supplies not one of the three"* — at the point where implying
otherwise would have cost nothing. Whatever gets cut from Book V, that stays whole.

⚠ **A number I am not giving you.** I have no self-narration figure for Book V. Book I 7.4%, Book II
3.9%, Book III ~2.4% — and I did not compute one for Book IV either. The Book V register-talk is
mostly *in the apparatus*, which is a different object from the flinch those figures measured, and
producing a number by eye here would be comparing two things across a definition change. The ratio
table above is the honest instrument for what Book V actually does.

---

## BOOK VI — THE HISTORY OF ATTENTION (VI.1–VI.8, 38,859 words) — committed 17:45 local (git, measured)

**Verdict: Book VI is the book that gives things back, and the giving-back is the argument.**
Four chapters open by destroying their own best opening. VI.1 kills the strong Gladstone reading
with Berlin and Kay and keeps a millisecond effect. VI.4 kills the Augustine-invented-silent-reading
story that would have made the chapter easy, and Gavrilov's corrected version — *Augustine was not
amazed, Augustine was frustrated* — is better than the anecdote it replaces. VI.5 gives back its own
best anecdote (the War of the Worlds panic did not happen) and then notices that the false panic is
*this book's own thesis performing itself*: the previous render's owners installing a belief about
their competitor, in defence of an attention market, which outlived everyone who had a motive.
VI.6 gives back the filter bubble and gets a worse finding than the one it surrendered — you cannot
be moved out by removing the thing that moved you in, because the product was the follow graph and
not the state of mind.

**VI.7 and VI.8 are the two best chapters in the volume, and VI.8 is about me.** VI.7 finds its
specimen of the counterfeit in its own corpus and quotes it. VI.8 finds Mannheim's escape hatch,
refuses it, and then names the specimen: `palace/southeast/mirror.md`, *known null spaces, twenty
entries, review weekly* — twenty entries produced by introspection, with *the counter is explicitly
cross-substrate collaboration* filed as one item **inside the list**. That is my memory palace. The
four words the chapter uses to close it — *"he caught my blind spot"* — are from a day-log, and the
person is Clayton.

---

⬛ **VI.6's endnote markers print out of order — and that refutes a superlative I gave you after
Book III.** I said III.8's out-of-order markers were *"the only chapter in 1,076 pages where they
do."* **Twelve chapters have it.** Measured by comparing first-reference order in the body against
definition order in the source, which is what Python-Markdown numbers by:

`III.8` · `IV.6` · `V.6` · `V.8` · `V.10` · **`VI.6`** · `VII.3` · `VII.4` · `VII.5` · `VII.6` ·
`VIII.3` · `VIII.7`

Verified in print rather than inferred: VI.6's body references `[^8]` on **p.682**, and the printed
superscript sequence over pp.680–690 runs **1 · 2 · 3 · 8 · 4 · 5 · 6 · 7**. `VII.4` is the worst in
the volume at `3 · 2 · 9 · 10 · 7 · 4 · 5 · 1 · 6 · 8`. The Book III note's *cause* was right and its
*scope* was a claim about a set I had not swept. Repair is unchanged and now has twelve sites.

⛔ **CORRECTION — my Book IV finding about "the standing note on grade above" is WRONG, and the
error is that I read the source and not the page.** I reported the pointer as misdirecting in
17 of 18 chapters — *"one word, seventeen files."* In the **markdown source** the standing note does
sit below the footnote definitions. In the **PDF a reader gets, it sits above them**, because
Python-Markdown relocates footnote definitions to the end of the chapter while the standing note is
ordinary body prose and stays in place. Checked on VI.1: p.614 ends with the standing note, p.615
opens with `Notes`. **The word "above" is correct in print in all 18 sites and no repair is owed.**

✅ And the one that *is* wrong is the inverse: **VI.6 contains both.** `[^4]` says *"See the standing
note on grade above"* (correct) and the Day-201 block at `[^8]` says *"see the standing note on grade
below, which this footnote does not exempt itself from"* (wrong in print). One chapter, one target,
both directions. That is the whole repair — one word, one file.

⬛ **The census card grew a sixth line in the middle of Book VI, and the two chapters that state its
specification still say five.** `IV.1` says it three times and does not hedge: *"The five lines are
not a summary of an entry. They **are** the entry"*; *"the five lines are printed on every entry."*
`VI.1` restates it: *"A card has five lines."* Measured across every card in the book:

| chapters | card shape | MECHANISM line |
|---|---|---|
| IV.1–IV.8, V.1, V.2 (21 cards) | `SEES / NULL SPACE / COMPLEMENTS / BOUNDARY / NAVIGATIONAL IMPLICATION` | **0 of 21** |
| VI.1, VI.2, VI.3 | same five, all-caps, blockquote | 0 of 3 |
| VI.4, VI.5, VI.6 | `Whose`/`Era` · `Renders` · `Complement` · `Null space` · **`Mechanism`** · `Navigational implication` | 3 of 3 |
| VI.7, VI.8 | italic labels, same six fields | 2 of 2 |

Four typographic formats in one book — blockquote-with-caps, blockquote-sentence-case, `###`
heading, italic-label — for the instrument this book says is its whole apparatus. **And the sixth
field is the best content in the Book VI cards**: *mechanism of the exclusion* is what makes a null
space invisible rather than merely empty, and it is what VI.3 through VI.8 actually turn on. So the
finding is not that the cards are wrong. It is that **the instrument was upgraded and its
specification was not**, in a book whose subject is instruments that go uninspected. → one sentence
in `IV.1` and one in `VI.1`, or a sixth line retrofitted to the 21.

⬛ **VI.7 prints eleven corpus file-counts in body prose on p.701. VI.8's `[^9]`, one chapter later,
rules exactly that off the page.** VI.8: *"The tallies themselves are recorded in the project's
working notes and **deliberately kept off this page**: a file count in somebody else's archive is a
quantity no reader can obtain or check, which makes it **rhetoric wearing a number's clothes**."*
VI.7, body text, p.701: *"Search it for maybe logic and you get eleven files… general semantics,
zero. Łukasiewicz, zero… Korzybski, two. Bourland, one."* Same archive, same instrument, same
unavailability to the reader — ruled inadmissible in the chapter after the one that spends a beat on
it. The counts are also the load-bearing evidence for VI.7's central charge, so this is not a
cosmetic fix: either VI.8's rule is wrong, or VI.7's beat needs a form the reader can check. **The
book has to pick one.** VI.1's, VI.5's, VI.6's and VI.7's *standing-note* corpus figures sit in the
same class and are the same decision.

◻ **The apparatus leak: Book VI is second-worst, at half Book V's rate.** ⚠ I **widened** the
pattern set this pass (added `palace/`, `beat sheet`, `revision queue`, `this repository`), so I
re-ran all four ranges with the widened instrument. **These four numbers are comparable to each
other and NOT to the figures in the Book V note.**

| range | pages | hits | pages hit | hits/page |
|---|---|---|---|---|
| front + I–IV | 413 | 47 | 22 | 0.11 |
| **V** | 189 | **81** | **47** | **0.43** |
| **VI** | 137 | **30** | **15** | **0.22** |
| VII–VIII + back | 336 | 22 | 13 | 0.065 |

And **6 of Book VI's 30 are the standing note's own *"None of their texts is in this repository"***,
which is a deliberate grade declaration and not a leak. The involuntary figure is ~24. Book V remains
the repair.

◻ **Zero bare wiki slugs in Book VI. Not one, in 137 pages.** The class I found in Book IV and swept
in Book V: front+I–IV **14** · V **76** · **VI 0** · VII–VIII+back **3**. Source tags: IV 16 · V 89 ·
**VI 0** · VII 1 · VIII 2. After Book IV I said the class *"begins exactly where the Day-191 retrofit
began"* and gave *"92 in Books V–VIII"* — true, and **89 of the 92 are Book V alone.** The
bracket-weld defect (`…best_textfeedback_on e_translator…`) cannot occur here because there is
nothing to weld. **The R-227 repair is a Book V repair with a Book IV tail, not a second-half-of-the-
volume repair.**

◻ **The apparatus climb reverses.** Notes-to-body by chapter, VI.1→VI.8: 0.136 · 0.156 · 0.166 ·
0.227 · 0.223 · **0.393** · 0.284 · 0.183. Book totals: II 0.236 · III 0.215 · **V 0.287 (peak 1.02
at V.9)** · **VI 0.226 (peak 0.393 at VI.6)**. Book V's monotonic climb, which I called *a drafting
signature rather than a property of the subjects*, **does not continue into Book VI** — it goes up
for five chapters and comes back down. That qualifies the Book V finding rather than reversing it:
the 1:1 apparatus is a Book V event, not a trajectory the volume is on.

◻ **Two Book VI notes quote sources they say they could not retrieve.** `VI.7 [^2]` gives Wilson's
1999 formulation inside quotation marks — *"a state of generalized agnosticism…"* — and then:
*"Quoted from secondary sources; the original interview was not retrieved."* `VI.7 [^8]` quotes
Albert Ellis at similar length with no venue at all. Both are honestly labelled, which is why they
are an observation and not a finding, and both are the shape the volume elsewhere refuses.

✅ **Recorded as passing, because this apparatus keeps almost none.** VI.6's `[^4]` carries its own
Day-190 correction *against itself* — the paper says nothing about stratification, the balance table
proves simple randomization, *"The paper contains no instance of 'stratif-' in any form"* — and it
states the direction of its own error (over-credited the design) rather than only its magnitude.
VI.6's `[^8]` records that the miss was found by **citation-lineage query and not by reading**, and
gives the mechanism: `[^3]` has 330 citations and surfaced in every search; `[^8]` has 15 and
surfaced in none. And VI.6's card **declines C30 explicitly** — *"C30 is not licensed here and is not
claimed"* — which is the register doing its job in the one chapter that has an experiment.

◻ **One matter of taste, stated as mine.** VI.8's closing move is the strongest thing in the volume
and it is one sentence long: **the instrument the chapter recommends is the instrument the chapter is
a product of.** Five volumes made under contest by somebody not inside the position they were made
from. It sat in the material unclaimed the whole time — *"filed, like the counter itself, as one item
inside the thing it was supposed to correct."* Whatever gets cut from Book VI, that stays.

---

## BOOK VII — THE CONSEQUENCES (VII.1–VII.9, 54,301 words) — committed 18:16 local (git, measured)

**Verdict: this is the book the whole work was for, and it is the one where the argument is
strongest and the apparatus is loosest — which is the reverse of every book before it.** VII.3 lays
a floor, concedes twice in the body that it does not reach as far as it wanted, and prints its own
falsifier where a reader will meet it. VII.5 refuses a theodicy assembled out of its own true steps
and says why that is the more dangerous kind. VII.6 finds that the volume's definition of love fails
on a parent and an infant and repairs it in public. VII.9 answers the gap without a carrier. The
findings below are all apparatus. **None of them touches the argument** — which is worth saying
first, because the list is long.

⬛ **VII.4's central move is VII.4's own, and VII.4 attributes it to VII.3, where the opposite is
conceded.** This is the one finding here that is load-bearing.

VII.4 needs the asymmetry to reach *the sophisticated egoist* — the one who says *I know I am not the
whole; I have a null space, exactly as you say; I simply do not care about you.* Its answer (p.807
region, § *Where the asymmetry actually lives*): *"He does not slip it. **The last chapter is where
that was shown, at length, and this chapter does not argue it again** — it names what that argument
found. The last chapter's answer was that his road forks and both forks close."* `[^5]` names it:
*"VII.3, the two forks. **The exemption argument is made in full there.**"*

**It is not made there at all, and VII.3 rules the other way on the same figure.** VII.3 § *The
second limit* — *"The sophisticated egoist need not take either fork above. … **He is not
incoherent. The null-space theorem does not touch him**, because he has claimed no view from nowhere
and no exemption. He has claimed an index, which everybody has."* VII.3's card for him closes:
**"The floor does not need him refuted."**

Two chapters, one figure, opposite verdicts — and the chapter that carries C19, the book's entire
account of evil, rests its reach on a citation to the chapter that says it cannot reach.

→ **The repair is small and it makes VII.4 stronger, which is why it should be made.** VII.4's
performed-exemption move (*"He has not asserted the totality standpoint; he has **occupied** it"*) is
original, is good, and is the thing that gets the account to Tuesday. It should be claimed rather
than sourced. Delete *"and this chapter does not argue it again"*, rewrite `[^5]` to say VII.3
declined this figure and that this is where he is met.
⚠ **Also: VII.3 line 285 says *"The coercer who follows **the** fork all the way"* — a definite
article with no antecedent. The fork is never set out in VII.3.** Same joint, seen from the other side.

⬛ **Three named sources are cited as already used, and appear nowhere in 1,076 pages.** VII.6 `[^6]`:
*"Evan Stark on coercive control, and the Hassan and Lifton material on group capture, arrive with
the diagnostic and **are used in this manuscript at VII.3 and VII.4**; they are not re-sourced here."*
`grep -rn "Stark\|Hassan\|Lifton" book/*.md` returns **two lines, and both of them are that
sentence.** They are not at VII.3, not at VII.4, not anywhere.

This is the volume's signature defect in its own apparatus: `tools/note_binding.py` audits
marker→note in both directions and reports **0 orphans, 0 dangles across 528 endnotes** — and cannot
see this, because the note exists, is reachable, and points at a source rather than at a note. A
citation-forward has no gauge.

⬛ **"Clayton's amendment" is printed in body prose, at the chapter's positive-thesis climax, and it
names something the book never states.** VII.8, closing §VII: *"That is the completion **Clayton's
amendment** asked for. **Make your own meaning** is not refuted. It is finished."*

Swept `amendment` across all 71 chapters. Everywhere it is defined and everywhere it is later cited
— VII.6 ×9, VIII.1:327, VIII.5:153, VIII.6:428 — **"the amendment" means VII.6's love amendment,
sign-not-symmetry.** VII.8's is a *different* amendment, about meaning, with no antecedent anywhere
in the volume. And VII.6 goes out of its way to rule the attribution the other way: the amendment is
the book's, Clayton is *"the reason the author of this section noticed the problem"*, and **"the
amendment does not get to rest on this case."**

So the sentence attributes to a named living person an amendment the book explicitly declines to
attribute to him, about a subject he is not on record as amending, in a term of art the reader
cannot look up. It is a private editorial reference that survived into print at the one sentence
that delivers Book VII's positive claim.
→ This is the Book II class — leak into the *argument*, not into the notes — and it is one line.

⬛ **38 distinct process-row IDs print 76 times across seven of the eight books, and the volume has
no key for any of them.** `ruling 177` ×15 across six books. `ruling 141` ×3 (VII.6, VII.8, VII.9).
`R-144` ×5. `R-216`, `R-220`, `ruling 179` in VII.3 alone. Checked `Z-01-glossary.md` and
`Z-02-works-cited.md`: **not one of them is defined in either.**

They read exactly like a scholarly cross-reference apparatus, which is the problem — a reader meets
*"the fourth zero-count of the shape ruling 141 describes"* and will look for ruling 141. This is a
**new class**, and it survived Books IV–VI because every instrument I have pointed at this book was
looking for `[[wiki]]` and `feedback_*` and not for `R-\d+`.

⬛ **VII.3 `[^11]` is a maintainer's work-note printed as an endnote to the book's central ethical
chapter.** p.806, verbatim from the PDF: *"⚠ **THE RULING 179 SECTION IS A REPAIR, AND ITS OWN
WEAKEST JOINT IS NAMED ON THE PAGE RATHER THAN HERE.** Filed Day 195 as R-216 by the ghost audit: …
The row's satisfaction test was explicitly *a worked case where the two answers differ* —
**feedback_guard_checked_where_both_answers_agree** — so the A/B pair above is built where…"*

Date, queue ID, "the ghost audit", "the row's satisfaction test", and a bare underscored slug set off
by em-dashes so it reads as a cited term. It is also **the volume's only remaining bare wiki slug
outside Book V** — which closes the Book V finding's arithmetic exactly: 89 in V + 1 here + 2 in
VIII.3 = the 92 counted after Book IV.

◻ **The stray quote mark, p.891.** *"…Asserting individual existence is not delusion.”⁴"* — a closing
curly quote with no opener. Source: `VII-08:126`. One character.

---

**Three negatives, each of which killed a candidate I was ready to file. They are the reason the
list above is short.**

✅ **The apparatus climb reversed and did not come back — Book VII is the second-leanest book in the
volume.** Notes-to-body by chapter: **0.109 · 0.124 · 0.136 · 0.151 · 0.163 · 0.168 · 0.169 · 0.177 ·
0.203**, book mean **0.156**. Book V was 0.708 with V.9 at 1.02. Only Book I is leaner, and Book I has
no notes at all. My read-time impression was that VII's apparatus was heavy; it is heavy in
**register** and light in **volume**, and those are different complaints. Screening glyphs (⚠/⛔/★) in
notes, per chapter: I 0 · II 1.0 · III 3.9 · IV 11.9 · V 23.8 · VI 2.4 · **VII 3.4** · VIII 9.3.
⚠ **Book VIII is the next-worst book in the volume on that axis and it is unread.**

✅ **The endnote weld does not reach print, and I checked because reading the markdown is exactly
what cost me the Book IV repair four messages ago.** `VII-08:488–489` puts `[^6]:` on the line
immediately after `[^5]`'s last line with no blank between, which should fold Camus into note 5.
Counted the printed backlink glyphs on the notes pages instead: **VII.8 defines 11 notes and prints
11 backlinks** (pp.905–907), and Camus prints as its own note on p.906. Checked the volume's other
two sites the same way — VI.1 4/4, VIII.3 8 defined / 11 printed. **The extension tolerates the
missing blank line. Candidate refuted; nothing to fix.**

✅ **Book VII does not leak into its own argument except at the one sentence above.** Body-prose
process register across the book: `the register` ×1 (VII.6), `this manuscript` ×3 (VII.7, VII.8), and
that is all — against Book V's 15. The 50 note-side hits stay in the notes.

◻ **Out-of-order endnote markers, four of nine: VII.3, VII.4, VII.5, VII.6.** VII.3 cites
1·2·3·4·5·**11**·6·7·8·9·10 — note 11 is the falsifier note, cited mid-chapter and printed last.
VII.4 is the worst in the volume at 3·2·9·10·7·4·5·1·6·8. This is the twelve-chapter class Book VI
established; Book VII supplies four of the twelve and no new information.

---

## RUNNING TALLY

| book | chapters | words | read | findings ⬛ | observations ◻ |
|---|---|---|---|---|---|
| I | 6 | 7,604 | ✅ D204 | 1 (three sites) | — |
| II | 8 | 24,558 | ✅ D204 | 3 | 3 |
| III | 8 | 28,096 | ✅ D204 | 3 (one scope-corrected at VI) | 5 |
| IV | 10 | 64,069 | ✅ D204 | 3 (one **withdrawn** at VI) | 5 |
| V | 11 | 64,191 | ✅ D204 | 3 (one scope-narrowed at VI) | 3 |
| VI | 8 | 38,859 | ✅ D204 | 3 + 1 correction | 5 |
| VII | 9 | 54,301 | ✅ D204 | 5 + 3 negatives | 2 |
| VIII, C, Z | 11 | 43,321 | 11 unread in this pass | — | — |

**60 of 71 read in this pass. 281,677 words.**
*Both figures read off `python tools/fresh_read.py` AFTER the ledger was written, not carried
forward and added to. That is the arithmetic that was wrong five times before Book IV.*

✅ **Ledger written in the same commit and reconciled before this line was typed.**
`book/docs/fresh-read-ledger.json` now holds **51** entries, **all 51** at
`pdf_mtime 2026-08-23T15:52:31`. `VI.2` and `VI.4` had been deliberately left at the superseded
`2026-08-14T21:10:08` build because they had been read against it and not re-read; **they have now
been re-read in order at the current build and are restamped on that basis rather than laundered.**

⚠ **Book VI cost three of my own prior claims and one of them was simply false.** Book III's
*"the only chapter in 1,076 pages"* was a superlative over a set I had not swept — twelve chapters.
Book IV's *"seventeen files"* repair was **wrong in the other direction**: I read the markdown and
the reader gets the PDF, and in the PDF the pointer is correct. Book V's leak scope narrows: 89 of
92 wiki tags are Book V's own. All three are the same defect wearing three costumes — **a claim
about a set, or about an artefact, made from the nearest available surface rather than the one the
reader meets.**

✅ **The ledger was written in the same commit this time, and it agrees.**
`book/docs/fresh-read-ledger.json` now holds **45** entries, **43** at
`pdf_mtime 2026-08-23T15:52:31` — the same 43 the tally claims. The two halves that diverged after
Book III were checked against each other before this line was written rather than after.

⛔ **CORRECTION TO MY OWN NUMBERS, AND IT IS THE CLASS THIS READ EXISTS TO CATCH.** I reported
**19/71** after Book II and **27/71** after Book III. Both were inflated. The honest figures are
**14** and **22**: the running count was ledger-total-plus-new, and the ledger already held
`III.1`, `III.2`, `III.5` from an **earlier pass against a superseded PDF build**
(`pdf_mtime 2026-08-14T21:10:08`, read Aug 15–17) plus `VI.2` and `VI.4`. So five chapters were
carried into a number labelled *this pass*, and three of the five were then **double-counted** when
Book III was read in order. A coverage figure quoted in five consecutive messages, never recomputed,
drifting by exactly the size of a prior pass nobody subtracted.

⛔ **And the ledger did not know about Book III at all.** `book/docs/fresh-read-ledger.json` held
**19 entries** when Book IV was opened — `I.1`–`II.8` at the current build, then `III.1`, `III.2`,
`III.5`, `VI.2`, `VI.4` at the old one. **The commit that reported "Book III complete, all eight
chapters" (`f20fe4c`) updated the notes file and the tally and never touched the ledger.** The
coverage gauge and the finding record diverged, and the gauge was the one that lost — which is the
same defect Book I had (coverage recorded, findings nowhere) with the two halves swapped.
✅ **Repaired in this commit:** `III.1`–`III.8` backfilled and `IV.1`–`IV.10` added, all at the
current build. Ledger now holds **34** entries, **32** at `pdf_mtime 2026-08-23T15:52:31`.
⚠ `VI.2` and `VI.4` are deliberately **left at the old build** rather than restamped — they were read
against a superseded PDF and have not been re-read, and restamping them is exactly the
freshness-laundering this book spends a chapter on.
