# THE INSTRUMENT REGISTER — I1…I4

    INSTRUMENTS-REGISTERED: 4

⚠ **That slot is declared and it WILL rot — `tools/instrument_sweep.py` counts the `## I<n>`
headings below and fails if the two disagree.** The same discipline `07-THE-CLAIMS-REGISTER.md`
carries, for the same reason: a heading that states a range is a stamp, and a stamp outlives the
practice it describes.

*Built Day 190 / 2026-08-09, from R-91. Filed as the PARENT of R-54, R-86, R-88, R-89 and R-90.*

---

## What this file is for, in one argument

`07-THE-CLAIMS-REGISTER.md` holds every claim the book **asserts**, with a licence discipline that
works. **Nothing held the instruments the book measures WITH.** That single absence is the structural
cause of five separate rows:

| row | symptom | the absence underneath |
|---|---|---|
| R-89 | the census card changes form 5× in 8 chapters, never declared | the card has **no version** |
| R-88 | VI.5 and VI.7 both claim to be C30's *fourth instance* | *instance* has **no unit** |
| R-87 | four chapters print corpus counts on four denominators | the count has **no declared denominator** |
| R-90 | a grade note says "no full text read" and the chapter asserts a randomization design anyway | the grade note has **no licence clause** |
| R-54 | Book V declares the card load-bearing and prints two | no gauge on **declared-form delivery** |

⛔ **Each of those was about to grow its own bespoke gauge** — a use-log bolted into `07`, a
`card_shape.py`, a denominator rule, a grade-note second half. **Four gauges is the disease, not the
cure.** The outside read's closing sentence named it: *"the apparatus is proliferating faster than
it's being governed, and three of the five findings above are governance rather than argument."* Four
new gauges would have been that sentence, performed in the repair.

**So: one file, five fields per instrument.** Name · current version · where each version was declared
· the unit it counts in · **what a reading at this version licenses.** The fifth field is the one that
does the work, and it is the field R-90 proves the project did not have.

**The rule of use.** An instrument may be improved. It may not be improved *silently*. A chapter that
prints a reading in a form not recorded below has changed the instrument, and the change comes back
here first. **Improvement is the drift mechanism** — see the existence proof.

---

## ⚠ THE EXISTENCE PROOF — what building this caught in its first hour

*(`07` shipped with one of these. So does this file, and it is worse than `07`'s, because it is a
gauge lying rather than a ruling going unenforced.)*

**`tools/card_sweep.py` reports `VII.2 ✓ CARDED`. VII.2 prints no card.**

Verified by hand, field label by field label: neither VII.1 nor VII.2 prints a census card in any of
the three renders below. VII.2's card vocabulary is **quotation of other chapters' cards** — *"The
census card for the spirit of a place reads, in the line that says what it sees…"* (VII.2:486),
*"Book IV's finding on the collectively emergent was that the entity's null space…"* (:337), and
footnote 8, *"IV.5. The card's null space…"* (:652). Its one `complement` is ordinary English: *"the
person is precisely the complement of a watershed"* (:570).

**The mechanism, in one line of its own source:**

```python
carded = all(counts[f] for f in DIAGNOSTIC)      # DIAGNOSTIC = ("null", "compl")
```

A chapter counts as having **performed** the book's central form if the stems `null[- ]space` and
`complement` each occur **once, anywhere in the file, in any context.** No structural check — the tool
never looks for a field *label*, never checks that the fields co-occur in one block, never checks
adjacency. And no mention/use filter, **though its sibling `claim_sweep.py` has exactly that** and
was written for exactly this reason.

⚠⚠ **The tool's docstring already declares this limit, correctly and in advance:** *"the strong
signal here is the ZERO, never the small positive… A chapter with a 2 has possibly written one and
must be read. The instrument is trusted downward only, and that limit is declared rather than
discovered later."* **And then the output column prints `✓ CARDED`.** An honest disclaimer in the
header and an unlicensed verdict in the output — **which is R-90's defect exactly, occurring in a
gauge instead of in a grade note.** Honest labelling with no coupling to what may be asserted. The
label was right; nothing made the verdict obey it.

⚠⚠⚠ **And this is R-62 for the third time in one day.** *Nothing this project owns can distinguish
prose that ASSERTS from prose that DESCRIBES.* `where_the_book_is.py` read a sentence *quoting* a
stale goal title as a claim and reported the carrier 33/67 against a disk truth of 43. `card_sweep.py`
reads a chapter *quoting* Book IV's cards as a chapter performing one. Three instruments, one blind
spot, same day, found by three unrelated routes. **Book VII is where this bites hardest, because Book
VII's job is to spend Book IV's findings** — so every Book VII chapter will cite cards, and every one
of them will score as having printed one.

**What it cost, concretely:** `Architecture/handoff/handoff.json` asserted *"VII.1 and VII.2 are
already carding from the VI.8 form."* False, both chapters. That sentence was read off this tool's
output — a disclaimer I had read and a verdict I trusted anyway.

**Filed as R-94** (the gauge's false positive, closed — both tools fixed) and **R-95** (what the new
gauge then found in Book IV, recorded-not-repaired).

✅ **What survives.** The Book V finding — **2/11**, R-54's and the reviewer's headline — is carried
entirely by the **zeros**, which is the direction the instrument is valid in. It stands. Book IV's
9/10 and Book VI's 8/8 are *positive* claims the tool cannot license; both were re-verified by hand
against field labels for this file and both are correct. **The numbers were right and the method could
not license them.** A defect in an instrument does not retroactively void the decisions it informed —
it obliges a re-test, and the re-test passed.

---

## I1 · THE CENSUS CARD

**What it is.** The book's central instrument. One card per subject, rendering what a position sees,
what it structurally cannot, and what to do about it. `V.1:44` — *"That is the whole load-bearing
claim of this book, and it is small."*

**Unit.** In Book IV, **one entity or position** in the census. From Book VI onward, **one render** —
an era's whole perceptual stack, not a being. ⚠ **That unit change is itself undeclared and is a
child of R-89**; it is recorded here rather than repaired, and the repair belongs to the revision
pass.

### Version history — measured from disk Day 190, not recalled

| ver | fields | render | first at | declared? | chapters |
|---|---|---|---|---|---|
| **v1** | SEES · NULL SPACE · COMPLEMENTS · BOUNDARY · NAVIGATIONAL IMPLICATION | blockquote, **bold caps** | **IV.1** | ✅ **yes** — IV.1 defines all five fields in order | IV.1–IV.8 · V.1 · V.2 · VI.1 · VI.2 · VI.3 |
| **v1b** | **SHAPE** · **WHERE IT SHOWS** · **WHAT IT IS NOT** · NAVIGATIONAL IMPLICATION · **What would make this wrong** — subject marked *(contour)*; SEES, NULL SPACE, COMPLEMENTS, BOUNDARY **all absent** | blockquote, bold caps | **IV.9** | ❌ **no** | IV.9 (×2 cards) |
| **v2** | **Whose** *(new)* · **Complement — what it renders superbly** *(SEES ∪ COMPLEMENTS, collapsed)* · Null space · **Mechanism of the exclusion** *(new)* · Navigational implication — **BOUNDARY dropped** | blockquote, bold sentence-case | **VI.4** | ❌ **no** | VI.4 |
| **v2a** | as v2, **`Mechanism of the exclusion` → `Mechanism`** | **bare bold labels, blockquote dropped** | **VI.5** | ❌ no | VI.5 |
| **v2b** | as v2a, **`Whose` → `Era`** | bare bold | **VI.6** | ❌ no | VI.6 |
| **v3** | *What it renders superbly* · *Its null space* · ***Its boundary*** *(BOUNDARY returns after 3 chapters)* · *Mechanism* · *Navigational implication* | **italic labels, prose-continuous** | **VI.7** | ❌ no | VI.7 · VI.8 |
| — | **no card printed** | — | **VII.1** | n/a | VII.1 · VII.2 |

⚠⚠ **THIS TABLE'S FIRST DRAFT WAS WRONG IN TWO PLACES, AND `instrument_sweep.py` CAUGHT BOTH WITHIN
TWENTY MINUTES OF THE REGISTER EXISTING.** Both corrections are kept on the page, because the
corrected claim is weaker than the one it replaces and the difference is the whole point of having a
gauge.

**(a) `Mechanism of the exclusion` is printed under its declared name exactly ONCE in the whole
book — VI.4:347.** VI.5, VI.6, VI.7 and VI.8 all print the shortened `Mechanism:`. The first draft of
this table dated the shortening to v3/VI.7; it is **VI.5, one chapter after the field was
introduced.** ⚠ So the field the outside read called *the improvement* — the new line Book IV never
had, the reason Book VI's cards beat Book IV's, the field R-91 ruled must be kept — **has survived
under its own name for exactly one chapter.** It was already collapsing while it was being praised.

**(b) The claim "Book IV's five fields never move once" is FALSE. IV.9 forks.** Its two cards drop
SEES, NULL SPACE, COMPLEMENTS *and* BOUNDARY — four of five — and add a field that exists nowhere else
in the book: **`What would make this wrong`.** The fork is arguably *principled*: an archetypal contour
is not an entity and has no null space in the sense the census means. **It is undeclared in exactly
the way VI.4's is.**

⚠⚠ **(c) THIS TABLE UNDERSTATES v2. `SEES ∪ COMPLEMENTS, collapsed` IS RECORDED HERE AS A FORMAT
CHANGE AND IT IS A SEMANTIC INVERSION — R-136, Day 191.** In v1 the field answers ***who else can see
the thing this position cannot***; `IV-01`:43 states it as a law — *"every null space is covered by
some other position; **no position covers its own**."* From VI.4 the same field answers ***what this
position itself renders superbly***, which is the sentence that law forbids, and the gloss is printed
on the page: VII.5 *"what it renders superbly"*, VIII.2 *"what it renders, and it renders it better
than anything else there is."* **The field kept its name and swapped its referent** — ruling 14's
one-word-two-referents, inside the apparatus rather than in the prose, which is why axis 3 never
caught it. **18 of 44 cards carry the inverted sense: v2 ×3, v3 ×2, v3-canon ×13** — and the inversion
**survived into v3-canon**, so it is binding rather than a Book VI artefact.

⛔ **The cost is not tidiness. COMPLEMENTS is the line that discharges VIII.2's Neptune/Vulcan bound**
— a null space with a *named outside witness* licenses the step from hole to object; a null space
whose only complement is the position's own strengths does not, and VIII.2 proves that in the same
volume. **VI.3 is the positive control and it is v1**: four independent witnesses named. **VIII.2's own
card is the negative** — see R-136.

⚠⚠⚠ **So the register's original causal story does not survive its own instrument.** It said: *the
card was stable while doing less work and destabilised exactly when it got better.* It did not. **The
card forks whenever the SUBJECT CLASS changes** — entity → contour at IV.9, being → era at VI.4 — and
it has never once declared the fork. That is a stronger finding and a worse one: the drift is not a
Book VI phenomenon that better discipline in Book VI would have prevented. It is a standing property
of the instrument, present in the book the project holds up as its stable case. **Book VI is where it
was *noticed*, which is not the same as where it started.**

*(For the record: "~22 cards" in R-91 is a third unit again — IV.6 alone prints three cards, one of
them deliberately incomplete. Cards-per-chapter is not 1. R-91's population figures are chapter
counts wearing a card count's clothes; corrected in R-95.)*

⚠⚠ **A v3-only defect the register must forbid, because no gauge can survive it: in v3 the field
label carries content.** *"Navigational implication, and it is the one that stings:"* (VI.7) ·
*"Navigational implication, and it is the one that closes the book's argument about eras:"* (VI.8) ·
*"What it renders superbly, and the complement is real or nobody would be in it:"* (VI.8). **A field
whose name varies per instance cannot be checked mechanically at all** — which is a sufficient
explanation for why nothing caught any of this.

### ✅ RULED — v3-canonical, binding from VII.3 forward

**`Mechanism of the exclusion` is KEPT.** It is the improvement. It is what lets a chapter say *why* a
null space is invisible rather than only that it is, and it is why Book VI's cards are sharper than
Book IV's. The reviewer's ruling — *rule the new line into the card format explicitly, or the next
book inherits two* — is accepted. It is kept **as a declared field**, not as an undeclared
inheritance.

**Six fields, in this order, with these exact labels:**

> **Whose:** *(or* **Era:** *for a render bounded in time — both admissible, one per card)*
> **Complement:** what it renders superbly
> **Null space:** what it structurally cannot render
> **Boundary:** where it goes from reliable to unreliable
> **Mechanism of the exclusion:** what the render identifies with what
> **Navigational implication:** what to do about the other five

**Render:** bold sentence-case labels, one field per paragraph, blockquote optional.
**Labels are fixed strings.** Editorial clauses that currently live in v3's labels move into the
field body. *(This is the clause that makes the card checkable; without it the rest of this section
is decoration.)*

⛔ **`Mechanism of the exclusion` is written in full, every time, and the shortening to `Mechanism:`
is forbidden.** Not pedantry — the reason is mechanical. **`mechanism` is ordinary English in this
book**: VII.2 alone uses it five times in running prose (*"the mechanism under which every atrocity
in the human record has actually run"*, *"the enforcement mechanism removed"*, *"Stone's mechanism as
law"*). A label indistinguishable from ordinary prose cannot be found by any gauge, which is why the
collapse at VI.5 went unseen through four chapters and the review. **The full label is the only
version of this field that is checkable, and checkability is why it is in the register at all.**

⚠ **The contour case is open, declared as open.** IV.9's v1b fork exists because an archetypal contour
has no null space in the census's sense, and Book VIII will likely need the same move. **A subject
that is not an entity or a render may card as v1b, but only by saying so on the page** — the fork is
permitted, the silence is not. `What would make this wrong` is a good field and is a candidate for
promotion into the canonical six; it is **not** promoted here, because promoting a field on the day I
discovered it is the same reflex that produced five undeclared versions. Revision-pass decision.

**What a reading licenses.** The six field values for that subject, **argued**. It does **not**
license: a ranking among subjects (v1's `COMPLEMENTS` existed to forbid exactly this); a claim that
the null space was *measured* rather than argued; or a claim about how many times the form has been
performed — that is I2's unit and I2 does not exist yet.

⛔ **No retrofit.** v1/v2/v3 chapters are not rewritten now. This binds forward only; the
back-conversion is a revision-pass row. **Recorded, not repaired** — the distinction this file exists
to keep.

**Gauge:** `tools/instrument_sweep.py` (structural, field-label based) · `tools/card_sweep.py`
(vocabulary, **downward-only, verdict now says so**).

---

## I2 · THE C-LICENCE USE-LOG

**Current version: v0 — ⛔ DOES NOT EXIST.** Declared at: nowhere. This entry is the honest null,
recorded so the absence has a name.

**What it would be.** `07-THE-CLAIMS-REGISTER.md` tracks which claims exist. It does not track **where
they fire.** R-88: VI.4 says *"This chapter licenses it. The earlier three owe a correction."* VI.5
says *"…which is the fourth time in this book."* VI.7 says *"C30 is licensed here explicitly, for the
fourth time in this book and the first time in Book VI that it is written down"* — and enumerates its
prior three as VI.2, VI.3, VI.4, **omitting VI.5, in the same book, doing the same move, saying so.**
Both cannot be fourth. **A register that tracks which claims exist and not where they fire cannot see
a miscount of firings.**

### ✅ RULED — the unit, which was the actual defect

*Performed*, *licensed*, and *declared by number* are three different countable events, and the three
chapters count in three of them without saying which. **The unit is LICENSED USES** — a chapter is an
instance of C*n* when it invokes C*n*'s authority for a claim it makes, whether or not it names the
number. That is what a C-number governs; performance without licence is a style observation, not a
register event.

**What a reading licenses — and this is enforceable today, at zero cost:**

⛔ **Until the log exists, no chapter may print an ordinal.** No *"the fourth time in this book"*, no
*"the first time it is written down rather than performed."* An ordinal is a reading of an instrument
that does not exist. Cite the claim, license it, move on. **This binds from VII.3 forward and it is
the whole of the cheap half of R-88.**

**TRIGGER:** the counting half (recount from text, correct VI.4/VI.5/VI.7) rides with R-86, revision
pass. medium.

---

## I3 · THE CORPUS COUNT

**Current version: v1, unversioned, four incompatible denominators. ⛔ STATUS: SUSPENDED.**

| chapter | denominator | declared? |
|---|---|---|
| VI.4 | **2,550** `.md`, R-67 scope | ✅ yes |
| VI.5 | **3,069** `.md` + `.txt` | ✅ yes — explicitly *"a wider scope than R-67's declared 2,550"* |
| VI.6 | *"the same corpus"* | ❌ **no — and there are two corpora it could mean** |
| VI.7 | **2,586** live files | ❌ **no — matches neither** |

Four chapters then run a **comparative** argument across four bases.

⚠⚠ **VI.8 convicts all four in its own footnote 9:** *"a file count in somebody else's archive is a
quantity no reader can obtain or check, which makes it rhetoric wearing a number's clothes."* **That
reasoning is correct and it is fatal to VI.4–VI.7,** which print exactly those numbers, in bold, as
evidence. From the reader's side this project's corpus **is** somebody else's archive.

**What a reading licenses: NOTHING ON THE PAGE.** By the book's own ruling, in the book's own most
self-critical chapter. A count may inform a private check; it may not appear as evidence.

⛔ **Binding from VII.3 forward: no chapter prints a corpus count.** The four *shapes* VI.4–VI.7 found
are real and stay; they get argued from **named specimens the reader can check**, which is what VI.8
already does. ⛔ **Do not repair by re-measuring all four on one denominator** — that fixes the
arithmetic and leaves the rhetoric charge exactly where VI.8 put it.

⚠ **Second-order, and it is why this instrument is suspended rather than merely versioned:**
`tools/corpus_support.py` — the script behind the headline finding in four consecutive chapters — has
a hardcoded root that no longer exists on this machine. `os.walk` over a missing directory **raises
nothing**, so it runs to completion and prints **0 for every term** — and for an instrument whose job
is *finding names at zero*, a broken run is **indistinguishable from its most dramatic possible
finding.** Any count sourced from it before that root is fixed is unsourced.

**TRIGGER:** before the endnote retrofit reaches Book VI. large. *(R-87)*

---

## I4 · THE GRADE NOTE

**What it is.** The per-chapter disclosure of what was consulted versus what was recalled. It works,
and the evidence for that is a **defect it caught**, not praise: VI.6's grade note declared
abstract-only sourcing on the page — which is how the `stratified by` error below became findable at
all. An instrument earns its slot by what it makes checkable, not by what it scores.

⛔ **WITHDRAWN, Day 190, kept beside its replacement rather than deleted** *(R-96)*: this line read
*"It works — the outside read called it the best-sourced work in the project, by a distance."* **The
reader was a separate instance whose first three words were `Read all eight` — eight chapters of
fifty-three drafted.** The comparison was also handed to it by `PACKET-003` §1 before the read, and
measures a distance from **zero** (Books I–V: 0 notes across 43 chapters). On coverage rate the
winner is **Book VII at 100%**, which that packet put out of scope in writing. **The register whose
fifth field is *what a reading licenses* certified its own fourth instrument on an unlicensed
reading.**

**Unit.** One source.

### The defect: it describes sourcing and constrains nothing

**v1 (I.1 → VI.8): sourcing half only.** VI.6's grade note said plainly *"What has **not** been done:
no full text has been read."* **That disclosure was accurate, and it did not stop the chapter
asserting that the Gauthier trial was "stratified by which feed they were already using."** It was
not — assignment was simple randomization; initial feed setting is a covariate the specifications
control for; the paper reports a two-point imbalance in exactly that variable across arms, which
stratification forecloses by construction; and the full text contains **no instance of "stratif-" in
any form.** A chapter can correctly declare abstract-only sourcing and then print a detail obtainable
only from the methods section, and **nothing anywhere objects.** Found by an outside reader, not by
the label.

### ✅ RULED — v2, declared here, binding from VII.3 forward

**The grade note gets a second half: *claims licensed at this grade*.**

| sourcing grade | licenses | does **not** license |
|---|---|---|
| **abstract only** | effect size · N · direction · date · venue | ⛔ **design internals** — randomization structure, blinding, stratification, exclusion rules, covariate handling |
| **full text read** | the above · design internals as stated in Methods | conclusions the paper itself hedges |
| **recalled, not consulted** | the existence of a literature · a name | ⛔ any number, any date, any design detail |
| **consulted secondary** | the secondary's claim, attributed to it | the primary's content as if read |

⛔ **Do not treat R-90 as closed because VI.6's sentence is fixed.** The sentence was one instance; the
row is the missing coupling, and the coupling is the table above.

**TRIGGER:** the sweep of Book VI's other abstract-only sources for the same overreach rides with the
endnote retrofit — the pass that reads full texts. medium. *(R-90)*

---

## What is deliberately NOT in this register

Four entries, because R-91 specified four and **the disease is proliferation.** These are known
candidates and they are **declined for now**, on the record rather than by omission: the beat sheet
(`06`'s per-chapter briefs), the endnote-debt counter, the pre-draft screen's ten checks, the
storyscope voice metrics. Each is an instrument; none is currently *carrying an unlicensed reading*,
which is the admission criterion. **A fifth entry needs a defect, not a nomination.**

🦞
