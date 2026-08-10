# REVIEWER PACKET 003 — BOOK VI, THE HISTORY OF ATTENTION

**Filed Day 190, 2026-08-09 evening. State: `fd37971` · 53 of 67 chapters · 177,403 words · Book VI
closed at eight chapters, 35,844 words.**

*Assembled by Clawd. Requested by Clayton. Fourth outside read; second assembled against a checklist.*

---

## §0 — READ THIS BEFORE ANYTHING ELSE: THIS IS A SUPPLEMENT, NOT A REPLACEMENT

⚠ **`PACKET-002` (Books I–V) went out on Day 189 and has not come back.** As of filing, nobody has
read it. This packet does **not** supersede it and does **not** ask you to start over.

**If you have not started I–V:** read in order — I, II, III, IV, V, then VI. This packet's checklist
and §2–§4 are additions to `PACKET-002`'s, not corrections of them.

**If you are mid-read:** finish I–V and file those findings *first*, before opening this file's §3.
`PACKET-002` is scored against `review/PRE-REG-002-books-I-V.md`, which has **three predictions still
open** (P2, P3, P4) that only an I–V read can settle. Findings on VI arriving mixed into findings on
I–V will lose that.

**Two blinds are running, and they are separate.** `PRE-REG-002` covers I–V; `PRE-REG-003` covers VI
and was filed at `fd37971` **before this packet was written**. Please do not open either until your
findings are written. Their entire value is having been blind — and `PRE-REG-002` already lost its
blindness once, on Day 189, in a way it declares in its own text rather than hiding.

⚠ **Also present in the repo and OUT OF SCOPE: `book/VII-01` and `book/VII-02`.** Book VII is 2 of 9.
They are named here so the state of the tree is not a surprise; findings on them are welcome but are
not what is being asked for, and VII.2 in particular is written in **conditional voice pending a
chapter that does not exist yet** (VII.3), so it will read as owing something. It does. It says so.

---

## §1 — THE CHECKLIST, RUN

Ruling 148 made the queue-promotion convention; `PACKET-002` shipped with ten rows missing and caught
it minutes before going out. So the step runs again, and it runs against the files, not from memory.

| ✓ | item | evidence |
|---|------|----------|
| ✅ | **`07-THE-CLAIMS-REGISTER.md` runs to C30 and has not moved during Book VI** | Verified at `fd37971`. **Eight chapters, zero new registered claims.** This is deliberate — Book VI applies the framework rather than extending it — **and §3 item 1 asks whether it is true.** |
| ✅ | **The C-LICENSE manifest discipline is live and was not live for Books I–IV** | R-13's *cause*, not just its symptom. Every Book VI chapter declares in the DRAFT-LOG which C-numbers it drew on, written at drafting rather than reconstructed. VI.4: `C11 · C10`. VI.5: `C11 · C12 · C10`. **This is the first book in the work where the register can be checked against what the chapters actually claimed.** |
| ✅ | **Book VI carries endnotes. It is the first book that does.** | `tools/endnote_debt.py`: Book VI — 32 sources, **59 notes, 25 covered, 7 owed.** Books II–V: **0 notes across 37 chapters.** So Book VI is the only stretch of this book where a named source can be chased, and the 41-chapter retrofit behind it is scheduled and not started. |
| ✅ | **`book/REVISION-QUEUE.md` is in the packet, at 84 rows** | R-50. Everything already known to be wrong is in it. Please do not spend the read rediscovering it. **The count is 84 and four other numbers were in circulation this evening — see §4.** |
| ⚠✅ | **The queue's own promotion gauge was wrong while this packet was being written, and the packet had already been drafted around its answer** | ★ **Caught during assembly, for the second packet running.** `row_promotion_sweep.py` reported 74 rows, nine filed-but-never-rowed, and one permanent hole. **All ten of those rows exist**, in a third heading format the tool does not match. Filed **R-85**. **See §4 — the first draft of this file shipped a false central claim on the strength of it.** |
| ✅ | **`tools/` is at 23 gauges, up from 18 at `PACKET-002`** | The five new ones: `brief_source`, `prose_beat_sweep`, `row_promotion_sweep`, `genre_sweep`, `ancestor_gap`. All runnable read-only from the repo root. Several exit non-zero on purpose. |
| ⚠ | **A void class of past findings, declared** | `find` on this machine resolves to Windows `FIND.EXE`, which printed `Parameter format not correct` and **exited 0** on every invocation. Silence read as absence, four times, and was used to build a finding before a gauge with a positive control killed it. **Every `find`-derived zero in this project before Day 190 is void.** If a prior packet showed you a zero, ask how it was counted. |

---

## §2 — WHAT WE ALREADY KNOW IS WRONG IN BOOK VI

1. **VI.4's opening beat rested on a refuted anecdote.** Augustine watching Ambrose read silently,
   presented for a century as evidence that silent reading was strange — **demolished by Knox, 1968.**
   Caught by the pre-draft screen before drafting; the chapter is written without it. Recorded here
   because it is the one demonstrated defect of the kind no gauge in `tools/` can find, and it was in
   the fastest-drafted stretch of the book.
2. **VI.7 corrects an attribution the source tradition has carried for decades** — *"the yes, no and
   maybe Quantum Logic of von Neumann"* is not von Neumann. Three-valued logic is **Łukasiewicz
   1920**; the QM application is **Reichenbach 1944**, criticised and never standard; **Birkhoff & von
   Neumann 1936 is two-valued throughout** and gives up **distributivity**, not bivalence. The
   correction is load-bearing against a party this project otherwise draws on, and it is made from
   the primary literature. **If it is wrong it is expensive.**
3. **VI.7's Whorfian floor is stated as contested, not settled.** Strong determinism dead; Boroditsky
   2001 failed replication in **January & Kako 2007**; Boroditsky et al. 2011 offers new support.
   Grade declared on the page.
4. **VI.8's psychology is venue-and-design verified with no full text read**, and says so in-chapter.
   Pronin, Lin & Ross (*PSPB* 28:3, 2002) and Pronin & Kugler (*JESP* 43:4, 2007). No effect sizes
   asserted; unretrieved outcomes **not** asserted null.
5. **Seven Book VI sources still owe a receipt** (`endnote_debt VI`: owed 7), concentrated in VI.7.
6. **Book VI has no honest-ledger chapter.** Book V got V.11. Book VI's eight chapters convict five
   eras and acquit none. Whether that is correct is §3 item 3.

---

## §3 — WHAT WE MOST WANT LOOKED AT, RANKED

**1. VI.8's terminal claim, and whether the method reaches it.**
Book VI's instrument is: a render leaves a **record**, made under a stack, readable by somebody
standing somewhere else. That is how VI.3–VI.7 convict five dead eras. VI.8 then turns it on the live
one, prints a card whose null space is **THE UNMEASURED**, and states that *every previous structure
in Book VI could be caught by measurement* and this one cannot. **There is no somebody standing
somewhere else for the era you are in.** Is the last movement of Book VI asserted at a grade its own
method licenses? `07` registers no claim for it. **This is the highest-value item in the packet.**

**2. VI.8's cost paragraph — confession or inoculation?**
The chapter names three costs it imposes on its reader, the heaviest being that **the vocabulary can
absorb its own refutation**: object that the argument is unfalsifiable and the frame replies that the
objection is a feature of your render. It says out loud that a reply which is always available is
doing no work. **R-15's standing test is: did the declared limit change the shape of what came after,
or only precede it?** It is the last page of the last chapter of the book. Nothing in Book VI comes
after it.

**3. Five eras, five convictions, no ledger.**
Book V shipped V.11 explicitly to record where an older road is *ahead* of us. Book VI has no
counterpart. Does Book VI ever say a dead era's model was **right** about a matter of fact this book
says it was wrong about — or only that it had capacities we lack? If the latter, is that a finding
about history or a finding about the instrument?

**4. The Mannheim refusal.**
VI.8 names **Karl Mannheim** as both ancestor and opponent: the *total conception of ideology*
includes its own author (Geertz called it Mannheim's paradox), and Mannheim's escape was Alfred
Weber's **freischwebende Intelligenz** — a stratum loose enough to attempt a synthesis. The chapter
**refuses the exemption on the weak reading**, which is the defensible one his defenders give. Is the
refusal earned, or does Book VI take the same exemption under a different name by claiming the
present tunnel is legible to it?

**5. R-8, never run by anybody: does any Book VI chapter assert a claim at a strength `07` does not
license?** For the first time this is checkable rather than reconstructible — the C-LICENSE manifest
exists for these eight chapters and for no others.

---

## §4 — THE CLAIM THIS SECTION WAS GOING TO MAKE, AND WHY IT IS NOT MAKING IT

**The first draft of this packet said, in this position, as its headline:**

> *75 queue rows. 23 gauges. Zero rows scoped to the argument of a Book VI chapter.* — Eight chapters
> shipped in a day and the file whose charter is *what does this book owe* recorded no debt against
> any of them.

**That was false, and how it became false is worth more to you than the claim would have been.**

**The true numbers.** The queue holds **84 rows** (83 before R-85 was filed tonight), R-1…R-84, with
one genuine gap at **R-24** that nothing anywhere documents. **Four of those rows are scoped directly
to Book VI prose** — R-75, R-76, R-77 on the `aperture`/`keyhole`/`bottleneck` retirements breached
twenty times across VI.1, VI.3 and VI.5 (**including C11's own formulation carrying a retired word**),
and R-78 on the recap ladder growing from three rungs to five across VI.5–VI.8. Book VI generated
prose debt. The debt is filed. **The claim that it was not is an artefact of how it was counted.**

**How it was counted.** `row_promotion_sweep.py` — written *after* `PACKET-002` caught ten unpromoted
rows, precisely so this would not recur — detects a row by two heading patterns. **Every row filed
since R-72 uses a third.** So it reported 74 rows, **nine "FILED BUT NEVER ROWED"**, and one
**"permanent HOLE"** at R-82. All ten are in the file. Nine were minutes from being re-promoted as
duplicates.

⚠⚠ **The class matters more than the instance, and it is the same class as R-80's dead corpus root:
a broken run is shaped exactly like the tool's strongest finding.** This gauge's entire output
vocabulary is *filed but never rowed*. When its pattern goes stale it emits *filed but never rowed* —
nine times, with citations attached, arriving in the step that most wants a catch.

★★ **And the part that is not about the tool.** Before running the gauge I ran my own grep to check
it, got 73 against its 74, and read the near-agreement as corroboration. **My grep used the same two
patterns.** The independent check reproduced the instrument's blind spot exactly and then certified
it. The question that would have caught it — *how many distinct ways does a row begin in this file?* —
is one line and was never asked, because it only occurs to someone who does not already know. The
answer is **three**: 59 table, 15 heading, 17 `FILED`. None declared anywhere.

**So the honest version of what this section wanted to say:**

The apparatus/argument imbalance `PACKET-002` §4 named is still the standing concern — 23 gauges, all
of them structural, and eight consecutive chapters whose largest finding came from the pre-draft
screen rather than the prose. **But this project cannot currently produce a trustworthy number about
its own coverage**, because the instruments that count are subject to the defect they count, and the
person checking them derives the check from the instrument. Four numbers for the queue's size were in
circulation tonight — 74, 75, 76, 80 — and the true one, 83, was in none of them.

**A finding about the argument outranks a finding about the apparatus, and a finding in a category
not on any list in this file outranks everything on them.** Both of the last reviewer's findings were
off-list and both outranked all five predictions made against them. **And now: if a count in this
packet matters to a finding you are making, please re-derive it rather than cite it.**

**So: a finding about the argument outranks a finding about the apparatus, and a finding in a
category not on any list in this file outranks everything on them.** That has been true of every read
so far — both of the last reviewer's findings were off-list, and both outranked all five predictions
made against them.

---

## §5 — THE PACKET

**The work.** `book/VI-01 … VI-08` — eight chapters, in order. Read them as a book.

**Read against, in order of load:**
- `07-THE-CLAIMS-REGISTER.md` — **C1…C30.** The contract. If your copy stops before C30 it is stale;
  two previous readers reported this file as ending earlier than it does.
- `06-THE-SCAFFOLD.md` — briefs for all 67 chapters; ruling apparatus, **currently at 170**.
- `05-THE-LEXICON.md` · `04-THE-UNSATISFYING-ANSWERS.md` · `03-THE-ANCESTORS.md` ·
  `02-SUPERSESSION.md` · `01-THE-GROUND.md` · `00-ARCHITECTURE.md`.

**The process record, where we are most likely to be lying to ourselves:**
- `book/DRAFT-LOG.md` — Book VI runs from the *"BOOK VI OPENS"* entry to *"VI.8 CLOSES BOOK VI."*
  Every screen, every ruling, every gauge run, including the ones that were wrong.
- `book/REVISION-QUEUE.md` — **84 rows** with triggers. See §4 before trusting that number or any
  other count in this packet.
- `tools/` — 23 gauges, read-only from the repo root.
- `review/PACKET-002-day189-books-I-V.md` — the outstanding I–V packet. See §0.
- ⛔ `review/PRE-REG-003-book-VI.md` — **our predictions about what you will find, filed blind before
  this packet was written. Do not open it until your findings are down.** It is scored afterwards and
  its value is entirely in having been written first.

---

*Uncommitted to a destination — file the response wherever it should live. If it is a letter rather
than a document, say so and it will be transcribed into `review/` intact: R-50 records that findings
from outside this repository have twice had to be carried across by hand and once were nearly lost.*
