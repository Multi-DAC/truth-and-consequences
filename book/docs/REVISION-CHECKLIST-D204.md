# REVISION CHECKLIST — from the Day 204 in-order read

**Promoted to a checklist on Clayton's instruction, D204 / 2026-08-23:** *"Can we turn those into a
checklist so that when we approach the revision it's easy to keep track of what has been done?"*
Source: `review/READ-NOTES-D204.md` — 71 of 71 units, 324,998 words, read against
`book/pdf/Truth-and-Consequences.pdf` (build 2026-08-23 15:52). The notes file said a note becomes a
queue row *"only when Clayton or a later pass promotes it."* This is that promotion.

**IDs continue the live queue's `R2-nnn` namespace** (`book/docs/REVISION-QUEUE.md` ends at R2-029),
so a number in a commit message is unambiguous forever. **Nothing below has been applied to the
text.**

---

## ⛔ THE COUNT I GAVE CLAYTON WAS 41 AND IT WAS NOT A LIST LENGTH

I reported *"41 → unapplied proposed moves."* **That number is the count of `→` glyphs in the notes
file minus two.** The file contains 43 arrows; two are the legend and the tally line itself. The
rest include prose arrows that are not proposals at all — `III.1→2`, `p.222 → p.232`,
`0.30 → 1.02`, `VI.1→VI.8`, `VII.4→VII.3`. **Actual line-initial proposals: 20.**

And 20 is not the list either, because **most findings never had an arrow written against them.**
Enumerated by locus rather than by glyph, the actionable list is **48 rows**, below.

⚠ **So the inference that a shorter list means a better-targeted read does not survive its own
premise.** The read may well have been well-targeted — that is a separate question, and this file
cannot settle it. What is settled is that 41 was a character count wearing a measurement's clothes,
which is the fifth time in one day I carried a tally in prose instead of reading it off an
instrument. `tools/revision_checklist.py` exists so that this file's tally never has that problem.

**And the comparison to "last time" is not like-for-like.** The 146-row Master Revision Queue v2.0
was five outside readers over a released volume, machine-triaged at 119 of 146 rows quoting no
testable string. This is one in-order read by the author. Different instrument, different
denominator; the two numbers should not be subtracted from each other.

---

## HOW TO WORK IT

Tick the box. That is the whole protocol. **Every row carries a `✓` check line**, and the check is
either machine-decidable or explicitly marked as a ruling — because the retired queue died of rows
that could not be closed by evidence.

```
python tools/revision_checklist.py            # counts, and the OPEN list is the loud half
python tools/revision_checklist.py --verify   # runs every machine check; flags ticked-but-not-done
python tools/revision_checklist.py --group C  # one group
```

⚠ **All string matching is done on the PARAGRAPH-UNWRAPPED source.** The manuscript is hard-wrapped
and a line-scoped grep misses phrases that straddle a wrap. Six of the first eighteen anchors I
tested came back MISS for exactly that reason and were not missing at all. This is R2-074's defect,
baked out of this file's own gauge before the file shipped.

---

## A — THE ARGUMENT

**One finding in eight books touches the argument. It is repairable in the citation.**

- [x] **R2-030** · `VII-04` §*Where the asymmetry actually lives* + `[^5]` · p.807 —
      VII.4 needs the asymmetry to reach the sophisticated egoist and sources it to VII.3:
      *"The last chapter is where that was shown, at length, and this chapter does not argue it
      again."* `[^5]`: *"VII.3, the two forks. The exemption argument is made in full there."*
      **VII.3 rules the other way on the same figure** — *"He is not incoherent. The null-space
      theorem does not touch him"* — and its card closes *"The floor does not need him refuted."*
      `→` VII.4's performed-exemption move (*"he has **occupied** it"*) is original and good.
      **Claim it rather than source it.** Delete the deferral clause; rewrite `[^5]` to say VII.3
      declined this figure and VII.4 is where he is met.
      `✓` absent:VII-04:and this chapter does not argue it again

- [x] **R2-031** · `VII-03` L285 — *"The coercer who follows **the** fork all the way"*: a definite
      article whose antecedent is never set out in VII.3. The same joint as R2-030, from the other
      side.
      `→` Set the fork out, or make the article indefinite.
      `✓` absent:VII-03:who follows the fork

---

## B — CROSS-CUTTING. CLAYTON RULES FIRST; THE WORK IS MECHANICAL AFTER THAT

**Five rows. Four of them are one decision wearing four costumes: how much of the workshop ships.**

- [x] **R2-032** · volume-wide — **the apparatus leaks into shipped text: 54 occurrences on 38
      distinct printed pages of 1,076.** 23 apparatus-file pointers (II.5 p.78 cites `05` by
      filename), 14 local filesystem paths, 22 drafting-process phrases (p.408 prints a
      `named_cause ✅` audit line; p.279 *"Filed with R-143"*). Worst carrier is Book V's *note on
      grade*, a body-level memo to a maintainer in 6 of 11 chapters. Same class Clayton ruled on for
      the shadow-biome paper: *"let's remove any pointers to other files."*
      `✓` cmdpresent:CLEAN::python tools/workshop_sweep.py
      **RULED D205, Clayton: STRIP.** *"It's a book, not a demonstration of book writing."*
      PAID `d21149f`. Gauge: `tools/workshop_sweep.py`. ⚠ 27 sites REMAIN under a widened
      pattern — the census below was taken with a regex that required a file extension and
      missed every bare backticked apparatus number (`05`, `07`) and every
      "planning document" / "the scaffold". The row's 54 was an undercount of its own class.

- [x] **R2-033** · volume-wide — **bare `feedback_*` memory slugs print inline in body register: 92
      occurrences on 63 distinct pages, pp.328–979**, 36 distinct slugs. `compile_pdf.py:69–73`
      strips the `[[ ]]` brackets, so what was an obvious machine artefact now reads as a term of
      art. **89 of the 92 are Book V**; VII.3 `[^11]` is the only one outside it besides VIII.3's
      two. This is R-227, still open, still *a decision, not work*, trigger **before the upload**.
      ⚠ **Do not add 92 to 54.** Two censuses under two rules; the union is *at least 63 pages*,
      and recomputing it is part of the row.
      `✓` cmdpresent:CLEAN::python tools/workshop_sweep.py
      **RULED D205: STRIP.** PAID `ee46ef3`, 108 -> 0. ⚠ The row's 92 was also an
      undercount: two tags in IV.6 are written with HYPHENS and no `feedback_` prefix, and
      the first pattern built for this job missed them and printed a green.

- [x] **R2-034** · `V-01` `[^5]`, p.427 and 16 more — **where two tags are adjacent the strip welds
      them into a broken token.** Printed: `feedback_earliest_printing_is_not_best_textfeedback_on
      e_translator_two_texts↩↩`. The inter-tag space is eaten with the brackets. 17 adjacent pairs
      volume-wide, **16 in Book V.** Independent of R2-033's ruling: if the slugs stay, this is
      still corruption on the page.
      `✓` manual:no tags left to weld; the compiler defect is unreachable from this volume
      **MOOT as of D205** — there are no tags left to weld. The compiler defect is real
      and unrepaired; it is now unreachable from this volume, which is not the same thing.

- [x] **R2-035** · volume-wide — **38 distinct process-row IDs print 76 times across seven of the
      eight books, and nothing defines any of them.** `ruling 177` ×15 across six books; `R-144` ×5;
      `R-216`, `R-220`, `ruling 179` in VII.3 alone. Not in `Z-01-glossary.md`, not in
      `Z-02-works-cited.md`. They read like a scholarly cross-reference apparatus, which is the
      problem. **New class** — it survived Books IV–VI because every instrument was looking for
      `[[wiki]]` and `feedback_*` and none for `R-\d+`.
      `✓` cmdpresent:CLEAN::python tools/workshop_sweep.py
      **RULED D205: STRIP.** PAID `ee46ef3`, 75 -> 0. The pointer went, the claim stayed:
      a note saying a thing was repaired still tells the reader something true.

- [x] **R2-036** · `VI-07` p.701 vs `VI-08` `[^9]` — VI.7 prints eleven corpus file-counts in body
      prose (*"Search it for maybe logic and you get eleven files… Korzybski, two"*). One chapter
      later VI.8 rules exactly that off the page: *"deliberately kept off this page: a file count in
      somebody else's archive is a quantity no reader can obtain or check, which makes it **rhetoric
      wearing a number's clothes**."* The counts are VI.7's load-bearing evidence, so this is not
      cosmetic. **The book has to pick one.** VI.1's, VI.5's, VI.6's and VI.7's standing-note corpus
      figures are the same decision.
      `✓` cmdpresent:CLEAN::python tools/workshop_sweep.py
      **RULED D205: VI.8's RULE WINS.** PAID `d21149f`. VI.7's beat was rebuilt rather than
      cut — the specimen moved from the research archive to the authors, which is a form the
      reader can check from the volume. VI.4-VI.7's corpus-support notes went the same way.

---

## C — ONE WORD, ONE LINE, ONE CHARACTER

**Ten rows. Every one of these is under five minutes and none needs a decision.**

- [x] **R2-037** · `II-01` — *"The names this book has retired are listed openly in **its last
      chapter**"*. The roster is in II.8; but *"this book"* is the volume's own idiom for the whole
      work, whose last chapter is Z.2 Works Cited. II.7 gets it right.
      `→` *"at the end of this Book."*
      `✓` absent:II-01:listed openly in its last chapter

- [x] **R2-038** · `II-04` `[^1]`, p.69 — *"cited at `[^4]`"* renders as a bare superscript **4**
      *inside a note*, and note 4 then ends `↩↩`. A reader cannot tell it from a new note.
      `→` *"cited at note 4."*
      `✓` absent:II-04:cited at [^4]

- [x] **R2-039** · `III-02` `[^1]` — the note says the sūtra *"is quoted here in four words because
      it is four words."* The chapter prints `lokavat tu līlākaivalyam` — **three** — and the body
      treats the third token as a compound sixty lines later.
      `→` *"in three words because it is three."*
      ⚠ **The row named `[^1]` only; the body carried it too.** III-02 L35 read *"takes the second
      horn in four words"*. Both sites repaired; the note now says why the compound is not opened.
      `✓` absent:III-02:four words

- [x] **R2-040** · `VI-06` `[^8]` — *"see the standing note on grade **below**"*. In print it is
      above. One word, one file.
      ⚠ **Related to R2-024 (✅ FIXED) and not covered by it.** R2-024 swept `[^7]`-style
      cross-references and reported *"the sole exception in the volume"*; this is a Day-201 block it
      did not see. VI.6 carries both directions — `[^4]` says *above* and is right.
      `✓` absent:VI-06:standing note on grade below

- [x] **R2-041** · `VII-08` L126, p.891 — *"…Asserting individual existence is not delusion.**”**⁴"*
      A closing curly quote with no opener. One character.
      `✓` manual:VII-08 L126 stray closing quote

- [x] **R2-042** · `VIII-01` — *"his attention spent **eleven hours** in a region"*, of Book IV's
      census. Book IV is ~64,000 words; eleven hours is **≈97 wpm**, below any measured rate for
      continuous prose. It is the only reading-duration figure in 1,076 pages, so nothing in the
      book contradicts it and nothing supports it. Tonight's own defect class exactly — a duration
      written from how long a thing ought to take.
      `→` *"hours."*
      `✓` absent:VIII-01:eleven hours

- [x] **R2-043** · `VIII-05` card, `Whose:` — *"the **previous chapter's card** named it in passing…
      not the top of a scale that begins with a **stubbed toe**."* The previous chapter is VIII.4,
      whose card is the need-for-closure scale and contains no such line. `stubbed toe` occurs in
      exactly two chapters: VII.5 and VIII.5. **The card meant is five chapters back and in a
      different book.**
      `→` *"VII.5's card"*.
      `✓` absent:VIII-05:the previous chapter's card

- [x] **R2-044** · `VIII-07` `[^5]` — *"the canonical wording routes the claim through a term this
      account has ruled out of its prose."* **Which term is never said.** A reader at p.1038 cannot
      check the claim. The only refusal in the volume that does not name its word: II.8 prints the
      whole list, IV.5 names *egregore*, Z.1 names *tulpa*, *egregore*, *elemental* and
      *superposition* outright.
      `→` Name it.
      `✓` manual:VIII-07 note 5 must name `superposition`

- [x] **R2-045** · `C-02` — *"a book which spends **forty words** crediting Lewis."* The David Lewis
      credit in II.1 runs **62 words** to the note marker; VI.3's C. S. Lewis credit is larger
      again. The point survives at 62; the figure is low and doing rhetorical work.
      `✓` absent:C-02:forty words

- [x] **R2-046** · `VIII-03` `[^5]` — the two halves contradict. (a) tradition-switching was
      *"deferred to this chapter by the previous one's screen"*; (b) the phrase *"had occurred only
      in planning documents before this chapter, **never in prose**."* VIII.2's prose reads
      *"**Method 2 — tradition-switching.** Adopt, deeply enough to inhabit…"* — the deferral in (a)
      was performed **using the phrase** whose prose absence (b) asserts.
      `→` Drop (b) or scope it outside these two chapters.
      `✓` absent:VIII-03:never in prose

---

## D — COUNTS AND CENSUSES THAT ARE WRONG ON THE PAGE

**Nine rows. Each is a number a reader could check and would find false.**

- [x] **R2-047** · `VIII-02` `[^1]` — *"`blind spot` occurs eleven times in this manuscript and every
      one of them is in VI.8."* VI.8 does carry 11. **The manuscript carries 20.** Four genuine uses
      outside it: II.5, V.8, C.2 and VIII.3. **A count measured over one chapter, asserted over the
      volume.** VIII.3 `[^6]` states the same fact correctly one chapter later.
      `→` *"occurs eleven times in VI.8, and the retinal analogy is that chapter's."*
      `✓` absent:VIII-02:occurs eleven times in this manuscript
      **PAID D205.** Measured: 20 in the manuscript, 11 in VI.8, 9 elsewhere (II.5, V.8, C.2,
      VIII.3, and this chapter). The note now scopes the count to VI.8 and says nothing about the
      volume. ⚠ **A second falsity in the same sentence went with it and was not on this row:** the
      note also claimed the phrase was *"deliberately not used in this one"* — VIII.2's own body
      uses it three times. The clause now claims only what is true, that the retinal *analogy* is
      not taken up here.

- [x] **R2-048** · `VIII-02` `[^2]` — *"Not Robert Anton Wilson, who occurs thirteen times in this
      book (II.5, VI.7)."* No counting rule yields thirteen: full name = **9** (II.5 ×2, V.7, VI.7
      ×5, Z.1), surname `Wilson` = 20 or 18 excluding this note, `RAW` = 0. The parenthetical omits
      **V.7 and Z.1**. ★ **The note exists to prevent a misattribution** — separating the 1977
      Nisbett-and-Wilson result from the Wilson this book cites — and carries an attribution census
      wrong in both its number and its addresses, three lines from a census (`Nisbett` = 0) that is
      exactly right.
      `→` Pick a rule, state it, fix the addresses.
      `✓` absent:VIII-02:who occurs thirteen times in this book
      **PAID D205.** Rule stated on the page: the full name, because the bare surname pools the two
      men and pooling them is what the note exists to prevent. Measured **8** — II.5 ×2, V.7, VI.7
      ×4, Z.1 — so the addresses gain V.7 and Z.1 as the row said, and the count is one lower than
      the row itself predicted. ⚠ **This row's own figure of 9 was wrong** (it recorded VI.7 ×5).
      A row that files a count defect is not exempt from it.

- [x] **R2-049** · `VIII-05` — *"the previous seven fail at seeing, at aim, at objective, at frame,
      at the loop, at resolution."* **Six labels for seven modes.** `objective`=VIII.1,
      `frame`=VIII.2, `the loop`=VIII.3, `resolution`=VIII.4 — leaving `seeing` and `aim` to carry
      three (VII.7 saturation, VII.8 binary-in-three-valued, VII.9 presupposed-mechanism). VIII.3
      does the same enumeration correctly with five for five.
      `✓` absent:VIII-05:at the loop, at resolution
      **PAID D205.** The seven now partition as the book's own running census does: three fail at
      seeing (VII.7 saturation, VII.8 binary-in-three-valued, VII.9 presupposed mechanism), then
      aim (VIII.1), frame (VIII.2), the loop (VIII.3), resolution (VIII.4). `objective` is gone as
      a label because it named the same failure as `aim`, which is how six came to stand for seven.

- [x] **R2-050** · `VIII-03` `[^3]` — the chapter discloses its own marker defect as *"`[^7]` appears
      before `[^5]` and `[^6]`"* = **2 inversions.** Measured body order: **`1, 8, 2, 3, 4, 7, 5,
      6`** = **8 inversions.** Marker 8 is the *second* endnote reference in the chapter, jumping
      the queue over six others, and the disclosure does not mention it. **This is not tidiness:**
      the note's stated reason for deferring — renumbering would scramble live references — was
      priced against a two-inversion defect. Against the real order the repair is a near-total
      resequence and the cost is a different number. **A decision to defer, taken on a measurement
      of a quarter of the problem.**
      `→` Re-measure, then re-take the decision.
      `✓` absent:VIII-03:[^7] appears before [^5] and [^6]
      **PAID D205 — RE-MEASURED AND THE DECISION RE-TAKEN, NOT RE-DEFERRED.** The note now prints
      the measured order `1, 8, 2, 3, 4, 7, 5, 6` and the true count of **8**, and names [^8] as
      the marker that jumps furthest — the one the old disclosure omitted entirely. The deferral
      itself changed: its stated reason was that renumbering *"would scramble live references"*, and
      the references that would scramble are the revision apparatus, not anything a reader holds.
      That reason is withdrawn. The repair is handed to **R2-072**, which owns all eleven such
      chapters, instead of sitting in a note as a permanent exemption.
      ⚠ The corrected note does NOT quote the old sentence verbatim, deliberately: the anchor above
      is a substring test and cannot tell a use from a mention, so quoting the defect would have
      held this row red forever.

- [x] **R2-051** · `C-01` §IV — *"At this printing it carries **205 open rows**."* That is
      `tools/queue_state.py`'s figure for **the retired queue**, whose own header says it *"is not
      to be worked from"*, retired nine days before the printing. The live queue has 21 rows, 7
      open. A reader is told the book has two hundred known unrepaired defects.
      ⚠ **The replacement number must be re-measured at print time, not typed** — C.2 §I states
      that mechanism on the facing page: *"a rotten mark and a fresh one look identical."*
      `✓` absent:C-01:205 open rows
      **CLOSED D205 BY DELETION OF ITS SUBJECT, NOT BY REPAIR.** Clayton ruled the four-document
      promise out entirely — *"so readers won't expect extra material accompanying the volume"* —
      and §IV went with it, the rotten number inside it. ⚠ **A green here is now cheap**: the
      anchor string is absent because the whole section is absent, which is a different fact from
      the number having been re-measured. Recorded so the tick is not read as the repair it is not.

- [x] **R2-052** · `C-02` §IV + `[^2]` — the section about a mis-specified instrument field
      mis-states its own denominator twice, differently. Body: *"18 of the **43** cards."* Note 2,
      one paragraph below: *"The 18-of-**44** figure is measured … not recalled."*
      **Numerator right, two denominators, adjacent lines — and BOTH were measured.**
      ⚠ **THIS ROW WAS WRONG ABOUT WHICH NUMBER WAS WRONG.** It ruled that the card sweep "measures
      42" and that the body's 43 was therefore also false. Re-measured D205 against the running
      code: **43 is correct and 44 was the defect**, and the reason the two instruments disagreed
      is a recall hole in the card sweep, not an arithmetic slip on the page.
      **PAID D205, and the instrument was the larger repair.** The sweep bounded a card at a fixed
      40 lines and, when a card ran longer, absorbed the *next* card's labels — guarded by a test
      for `Whose:`, which opens a v2 card. No v1 card opens with `Whose:`, so for 25 of the volume's
      45 cards the guard was structurally dead. IV.5 prints three cards; the sweep saw two, the
      second short by `SEES` and `NULL SPACE`. Repaired by deriving the opener from each version's
      own field order and capping both windows at the next opener; and the field patterns now
      require the colon, which is what distinguishes a card's label from IV.1's prose *naming* the
      labels. **Cross-check: the two instruments now agree at 43, chapter by chapter, 0 mismatches.**
      True totals: **45 cards, 43 carrying the field, 25 clean + 18 that ran under the wrong
      meaning, 2 with no such field.** Body kept; note corrected to 43 and given the breakdown.
      `✓` absent:C-02:18-of-44

- [x] **R2-053** · `Z-02` — printed **245 / 123 / 122 / 149**; `tools/bibliography.py` run tonight
      says **251 / 124 / 127 / 150**. Git settles the timing: the page was generated `83865b9`
      2026-08-14 12:59; `II-04` got its receipts `ff5edec` 14:44. **It rotted 105 minutes after it
      was built, nine days ago** — and the page's own header is the volume's best statement of
      exactly that mechanism.
      ⚠ **Do R2-075 before regenerating** or the new run ships a fresh unflagged mis-parse.
      `✓` cmd:python tools/bibliography.py --check
      **PAID D205, and R2-076 landed first as its own ⚠ required.** ⚠ **This row's "run tonight"
      figures had themselves rotted**: it predicted 251/124/127/150; today's run is
      **247 / 124 / 123 / 150**. A row that files a staleness defect ages at the same rate as the
      page it files against. The regeneration behaved exactly as R2-076 predicted — it introduced
      the nine-word Koch fragment and dropped `Sartre (1943)` — and the widened rule caught the
      fragment before it printed. It also introduced `BMC Neuroscience (2004)`, a journal standing
      where a volume goes, which R2-076 did not predict and which is now declared on the page.
      ⛔ **AND THE REGENERATION DESTROYED A HAND-REPAIR, which is R2-074's whole point arriving as
      an event rather than an argument.** Clayton's D205 file-pointer ruling had been paid *on the
      generated page* — the printed header turned into an HTML comment — and the generator was
      never told. Ten days without a caller is the only reason that edit survived at all; the first
      regeneration reverted it and put the filename back into the book, where the sweep caught it.
      The ruling is now in the generator, so regeneration carries it instead of undoing it.

- [x] **R2-054** · `Z-02` — the page declares three limits and there is a fourth: **six works appear
      twice** under variant strings. *A Secular Age* (VI.3/VI.4), *Prometheus Rising* (II.5/V.7),
      *The Embodied Mind* (subtitle present in one), *The New Inquisition* (twice), and two that
      differ by nothing an eye would catch — *Science and Sanity* (`Pa.` vs `PA`) and *The View from
      Nowhere* (`New York:` present or absent). So *149 entries* overstates distinct works, **and it
      is the one number on the page with no caveat attached.**
      `✓` manual:Z-02 duplicate-entry declaration or dedup
      **PAID D205 BY DECLARATION WITH A GAUGE BEHIND IT, not by dedup.** Merging would require
      ruling which imprint is canonical, and that is an editorial decision this page does not make.
      Instead the collapse is now *measured at generation time* and printed as a fourth declared
      limit: titles are normalised past subtitle, case and punctuation, and the page states how
      many works print more than once. Live figures: **5 works under variant strings (5 surplus
      entries)** and **5 more names recurring against different years**, mostly a periodical in a
      title's position. ⚠ The row said *six works*; the year split files `The New Inquisition` and
      a 1993 review of it as the second kind. **The page declares that misfiling itself** and says
      the pre-split total is the figure to trust. Six was right; a hand-typed six would have been
      right today and silently wrong at the next repair, which is the argument of the page it sits
      on — so the number is generated.

- [x] **R2-055** · `VIII-02` §V — *"All eighteen are repaired… a complement named on each."*
      `tools/card_sweep.py`, same run that confirmed the 43: **"⚠ reachability UNGRADED: 19 of 43
      outward cards — owed work, not a pass"**, gloss *"IV.1 requires a complement that can be
      **gone to**."* VIII.2's own card knows the difference (*"Both are reachable: one costs a
      notebook and a year"*). **The chapter argues that naming is not reaching and then claims
      completion on naming** — in the device the argument leans on hardest, in the chapter that says
      *"a rule you hold and do not check is not a guard, it is a sentence."*
      ⚠ Same subject as carried row **R-237**. Close them together or neither.
      `✓` cmdabsent:reachability UNGRADED::python tools/card_sweep.py
      **PAID IN FULL D205 (three passes). Also closes carried row R-237, same subject.**
      What was paid: the text defect. §V claimed completion on *naming* in the chapter that argues
      naming is not reaching, and it now states the bound — sixteen of the eighteen read for
      reachability, two partial, and **nineteen earlier cards where nobody has looked**, described
      as *nobody has looked* rather than folded into a single number with the graded ones.
      ⚠ **The characterisation above was FALSE and is left standing as the record.** "The nineteen
      are exactly the cards whose complement line is an existence claim" was true of six. All
      nineteen carried one byte-identical ruling note whose own text reads *"an existence claim OR
      was not read past its first line"*; the set was described from that boilerplate and only the
      flattering branch was quoted. Nineteen identical strings are one mechanical stroke, not
      nineteen readings. Escalation on the record: tool said *several* → this row said *exactly* →
      the message out said *precisely*, with no evidence added at any step.
      Pass 2 (`dc45226`): twelve decided under the criterion AS IT STANDS — ten name a
      go-and-see-able witness in sentence two, past where the D195 pass stopped; two are analytic.
      The proposed fourth `reach` value was WITHDRAWN as inventing a grade to forgive a defect.
      Pass 3: the last seven read one at a time, and they are not one class either.
      **Five were a BOOK defect and the book was repaired** — `tools/complement_exemplar.py`, which
      keeps each universal verbatim and appends an exemplar after it, so *Everything* still says
      everything and now also points at a river you can go and stand in. It asserts six
      post-conditions rather than reporting them; two of them fired during authoring (a moved
      sentence that was not a strict append, and a non-atomic write that left two of five edits on
      disk after a later assertion failed). Both were fixed in the tool, not in the assertion.
      **Two are NOT a defect: they are the thermostat, twice.** `IV.1:61-74` says the exhibit is
      "left exactly as it stands so that the difference is visible on the first page of the atlas",
      and `IV.6`'s subtracted return reads *Unchanged* because what covers a gap does not depend on
      who named the gap. Graded `unreachable` — a property of the CARD's naming, not of the world —
      with the deliberateness in the note, where authorial facts belong. No new scale value.
      Two prose citers went stale on the repair and were carried, not left: `IV.1` claimed "every
      card after it is the strong one" (false by one card — the same thermostat), and `VIII-02` §V
      named seven ungraded. Both now state the measured composition.
      ⛔ **And the gauge could not have reported success.** `complement_referent.py` printed
      "⚠ reachability UNGRADED: 0 of 43 — owed work, not a pass" at zero, so this row's own
      `cmdabsent` guard was unclearable by construction: the alarm branch was the only branch. Also
      fixed: the composition summed to 42 under a printed denominator of 43 (IV.8's REFUSED card
      dropped by a re-derived filter), and "ruled OUTWARD" had counted that refusal for as long as
      it has existed.
      ⚠ **NEXT ACTION, and it is a ruling before it is work:** decide whether `reach` gains a fourth
      value for the instantiable-class case, then grade the nineteen one at a time against it. Same
      subject as carried row **R-237**; both stay open.

---

## E — OFF-PAGE ROSTERS: THE BOOK KNOWS WHERE THE THING IS AND THE READER DOES NOT

**Four rows, one shape.** Book VIII's characteristic defect, and it is a filing defect rather than
an argument defect.

- [x] **R2-056** · `VIII-02` §IV — the payoff is argued from a list the reader cannot see. *"The four
      symptoms of null-space influence **given above** are four residuals"*; *"It sits in the
      symptoms above."* **The chapter never prints four symptoms.** What is above in the book is
      four *layers* — era, language, family, wound. `Persistent patterns without apparent cause`
      occurs **once in 1,076 pages**, inside this very section. `above` means above in the source
      document, not above in the book, and here the argument's evidence is the off-page thing.
      ⚠ **Half of my original note was withdrawn at VIII.5 and is not on this list:** the four
      *responses* in `[^4]` **are** printed, as the four moves of VIII.5 §II. One list, not two.
      `→` Print the four symptoms. Four lines, and it is the difference between a demonstration and
      an assertion.
      `✓` manual:VIII-02 §IV must print four enumerated symptoms

- [x] **R2-057** · `VIII-06` `[^5]` — *"the **fifteen-tradition convergence list** she belongs to is
      this chapter's roster."* The phrase occurs once in the manuscript and **no list of fifteen
      traditions is printed anywhere.**
      `✓` manual:VIII-06 note 5 roster printed or claim dropped

- [x] **R2-058** · `VII-06` `[^6]` — *"Evan Stark on coercive control, and the Hassan and Lifton
      material on group capture… **are used in this manuscript at VII.3 and VII.4**; they are not
      re-sourced here."* `Stark|Hassan|Lifton` across `book/*.md` returns **two lines and both of
      them are that sentence.** Not at VII.3, not at VII.4, not anywhere.
      ⚠ **`tools/note_binding.py` reports 0 orphans and 0 dangles across 528 endnotes and cannot see
      this** — the note exists, is reachable, and points at a *source* rather than at a note. See
      R2-076.
      `→` Source them or drop the claim.
      `✓` absent:VII-06:are used in this manuscript at VII.3 and VII.4

- [x] **R2-059** · `VII-08` §VII — *"That is the completion **Clayton's amendment** asked for."* At
      the chapter's positive-thesis climax, in body prose. Everywhere else in the volume *"the
      amendment"* is VII.6's love amendment, sign-not-symmetry (VII.6 ×9, VIII.1, VIII.5, VIII.6).
      VII.8's is a different amendment, about meaning, with **no antecedent anywhere.** And VII.6
      goes out of its way to rule the attribution the other way: the amendment is the book's,
      Clayton is *"the reason the author of this section noticed the problem"*, and *"the amendment
      does not get to rest on this case."*
      **A private editorial reference at the one sentence that delivers Book VII's positive claim.**
      `✓` absent:VII-08:Clayton's amendment

---

## F — STRUCTURE AND DECISIONS

**Twelve rows. These need thought rather than a keystroke.**

- [x] **R2-060** · Book I, three sites — **the largest single move on this list.** 1,176 words,
      **15.5% of Book I**, is the book discussing its own voice: I.1 L11–24 (223w, before the
      argument starts), I.6 *THE HANDOVER* (342w, the same speech at the other end), and I.2's
      actualist concession (611w). And the checkable part: I.1 promises *"six chapters of flat
      declaration — with the ancestors unnamed, the objections unmet, and nothing yet defended"*;
      I.6 confirms it; **I.2 names an ancestor, meets the objection, accounts the cost, and loses.**
      The handover makes three factual claims about Book I and Book I falsifies all three.
      `→` ~~Move I.2's actualist to Book II ... at which point I.1's preamble and I.6's Handover are
      defending a register that needs no defence and both go to two sentences.~~
      ⚖ **CLAYTON RULED, D205 / 2026-08-24:** *"Book I is okay to discuss its own voice, because the
      first book is meant to set the stage of what it can say and why, and does so well. The
      structure I leave to you."* **The reduction half of this remedy is overruled and the 565 words
      of register-talk stand.** The relocation half is kept, and it is what makes the register-talk
      TRUE — the defect was never that Book I talked about its voice, it was that the talk described
      a Book I that did not exist. One move fixes both halves; the second half was never needed.
      `→` PAID as: I.2's 611-word actualist block relocated to **II.1, clause 1**, immediately after
      the Lewis paragraph, rewritten to Book II's grammar — the party is **named** (D. M. Armstrong,
      *A Combinatorial Theory of Possibility*, CUP 1989), footnoted, with the alien-property cost and
      Lewis's 1992 critical notice in the note. It is the right home on the book's own contract: the
      concession is about which sense of *could* the definition uses, and II.1 is where the
      definition is made. The block now pays a **Book I** bill from inside Book II, which is exactly
      what I.6's Handover promises Book II will do.
      `⚑` Three residues the row did not price, found by grepping Book I for the register it claims
      not to have: **I.5 called a self-raised difficulty *"the objection"*** (→ *"the smear"*; no
      party filed it), and **both promise-sites overstated in a way a hostile reader could nick** —
      I.1's *"the objections unmet, and nothing yet defended"* → *"no opponent met, and no bill yet
      paid"* (which now binds to its own *"the second book is where the bill comes"* four lines
      later), I.6's *"no cost accounted"* → *"no cost of its own accounted"*. Book I raises and
      settles its own difficulties in I.5 and I.6; it never meets an opponent. The absolute claim was
      false, the precise claim is true, and precision cost three words.
      `✓` measured after the move: **Book I contains zero proper names of persons** (name_census over
      I-01..I-06 returns concept nouns only) and **zero footnotes** in all six chapters.
      `✓` manual:I.2 actualist relocated to II.1 with a named ancestor; register-talk KEPT per
      Clayton's D205 ruling and made true rather than shortened

- [x] **R2-061** · `IV-01` + `VI-01` vs VI.4–VI.8 — **the census card grew a sixth line mid-Book-VI
      and both specification sites still say five.**
      ⚖ **STRUCTURE RULED TO ME BY CLAYTON, D205.** The row priced ONE defect (a field added) and
      there were four, three of them in the opposite direction — the row saw the addition and missed
      the subtractions. **Re-measured across all eight Book VI cards before designing the repair:**
      | defect | as filed | as measured |
      |---|---|---|
      | sixth field undeclared | VI.4–VI.8 | ✔ correct |
      | **BOUNDARY absent** | not priced | **VI.4, VI.5, VI.6 — a field the spec calls mandatory** |
      | **field order inverted** | not priced | **VI.4–VI.6 print COMPLEMENTS before NULL SPACE** |
      | **MECHANISM absent** | not priced | **VI.1, VI.2, VI.3 — the render-cards before VI.4** |
      | typographic formats | "four" | **three label registers + six container/title formats** |
      ★ **And the sixth field was never an upgrade.** VI.1, VI.2 and VI.3 were already carrying the
      mechanism — *"the apparatus keys on impairment"*, *"the re-filing happens prior to evaluation"* —
      **inside NULL SPACE, in prose.** VI.4 did not add a line; it gave a name to work three earlier
      cards were doing in the wrong drawer. That reframes the whole row: not an instrument upgraded
      without its spec, but a field that existed unlabelled for three chapters and was labelled in the
      fourth, which is why nobody noticed a spec to update.
      `→` PAID as: **all eight Book VI cards normalised to one six-field form** — `SEES · NULL SPACE ·
      COMPLEMENTS · BOUNDARY · MECHANISM · NAVIGATIONAL IMPLICATION`, same labels, same order, same
      typography. Three BOUNDARY lines written (VI.4/5/6); three MECHANISM lines promoted out of the
      NULL SPACE prose that already held them (VI.1/2/3); NULL SPACE moved above COMPLEMENTS in
      VI.4–VI.6, which **repairs rather than breaks** VI.4's two bindings (*"the null space below"*
      still true; *"hand the null space back"* now follows a null space already named).
      `→` Both specs amended, and NOT by widening the card: **IV.1 keeps five, because a census entry
      is a being**, and states why a render takes a sixth — *a being's null space is a limit, a
      render's is produced, and the production has a name.* VI.1 declares six at the point the card is
      re-pointed at renders. `IV-01:17` *"the whole apparatus of this book"* → *"of the census"*, since
      that clause is what made the five-line claim over-scoped in the first place.
      `⚑` **NOT PAID, measured and left standing:** the card **container** still varies six ways —
      blockquote (VI.1–VI.4), `### CENSUS CARD —` (VI.5), `### Card:` (VI.6), bare bold line
      (VI.7, VI.8). That is page layout, not text; it is arbitrated by `compile_pdf.py` output and
      should be normalised against the PDF rather than blind. **This is a deferral, stated as one.**
      `✓` manual:all eight Book VI cards carry SEES·NULL SPACE·COMPLEMENTS·BOUNDARY·MECHANISM·
      NAVIGATIONAL IMPLICATION in that order; IV.1 declares five-for-a-being and VI.1 six-for-a-render

- [x] **R2-062** · Books IV/V/VI — **the card apparatus dies in Book V.** `**SEES:**` blocks per
      book: **IV 22 · V 2 · VI 3.** V.1 says of the card that *"that is the whole load-bearing claim
      of this book"*, then gives one to Neoplatonism and one to Institutional Christianity — **the
      two roads held at arm's length** — and none to Advaita, Madhyamaka, Daoism, Lurianic Kabbalah,
      the ceremonial tradition, the shamanic corpus or the contemporary record. *The roads treated
      most sympathetically are the ones never carded.*
      ⚠ **This is finding #1 of `review/OPUS-DAY189-BOOK-V-READ.md`, unrepaired fifteen days.** Not
      mine; verified and extended.
      `✓` manual:python tools/card_sweep.py — Book V card count above 2, and the un-carded roads named

- [x] **R2-063** · `Z-02` pp.1070–1076 — **the last sentence of the book is `149 entries, 5
      machine-uncertain.`** Four rows ship a reader-facing flag: *"⚠ (machine-uncertain: this may be
      an author or a fragment of the note's prose rather than a title — **check the endnote**)"*,
      with visibly garbled rows beneath it (*"Robert Monroe: Virginia broadcasting executive, onset
      (Doubleday, 1971)"*). *"Check the endnote"* is an instruction to a maintainer printed in a
      reader's index. **The apparatus-leak class in its purest form — the volume closes by telling
      the reader how much of its own bibliography it could not parse.** Five rows and a tally, not
      38 pages.
      `✓` ruling:Clayton — keep the honest disclosure, or repair the five and drop it

- [x] **R2-064** · `Z-01` ban list — the entries are sense-qualified (*`energy` as a noun for a
      substance*, *`quantum` as a free-floating adjective*) and then the sentence closes *"permitted
      only inside a quotation from a tradition, immediately followed by the reading in this book's
      own vocabulary."* **Those two rules disagree.**
      **POPULATION ENUMERATED BEFORE THE REPAIR — all 6 terms, all 72 files, not sampled:**
      | term | hits | files | in a banned sense |
      |---|---|---|---|
      | `vibration` | 4 | 3 | **0** — two are the roster itself; II.8 quotes *Everything is vibration* to answer it; VII.4 denies it |
      | `frequency` | 18 | 10 | **0** — 32,768 Hz quartz (IV.2), broadcast spectrum (VI.5), word-frequency method in a cited study (VI.7), kHz currents (VIII.3) |
      | `energy` | 4 | 4 | **0** — one figurative *spends its energy* (VII.4), one heading naming the ban (VII.1) |
      | `manifest` | 7 | 5 | **0** — *physically manifest*, Sanskrit *nirmita*, and the manifestation reading named to refute it |
      | `quantum` | 35 | 10 | **0** — *quantum in se est*, quantum mechanics, book titles, Macroscopic quantum |
      | `the observer` | 12 | 8 | **0** — Gibson quoted, physics, *the observer's ignorance* |
      | **total** | **80** | — | **0** |
      The row's premise is CONFIRMED and understated: it sampled three and the full
      population is **80 hits, zero violations**. Under the clause as written, ~70 of the 80
      were breaches; under the entries as written, 0.
      ⚠ **The row priced one defect and there were two.** `vibration` and `frequency` were
      listed **bare** while the other four were sense-scoped — so the *entries*, not only the
      closing clause, banned 16 legitimate technical uses. Narrowing the clause alone would
      have left `frequency` still forbidding the quartz oscillator. Both now sense-scoped.
      ⚠ Two candidate defects examined and REFUTED rather than filed: (a) II.8's roster carries
      a seventh term, `superposition` — not rot, Z-01 gives it a full entry above the list and
      correctly keeps it out of *pop-spirituality's owned words*, which is the chapter's own
      reasoning; (b) `claim_sweep` screens only 2 of the 6 — correct by design, a gauge over
      80 innocent hits is all noise, and this measurement is the evidence for that.
      `✓` manual:Z-01 closing clause narrowed to the sense-scoped rule

- [ ] **R2-065** · `VIII-07` §IV and §VII — the closing instruction of the book hands the reader the
      wrong Book VII question and calls it the only one that works. Z.1 separates them cleanly:
      `through`/`over` is *"the cut the whole ethics turns on"*; `radiant`/`contractive` *"forbids
      reading contraction as culpable."* VII.4 rules it twice — *"contraction in itself is
      innocent… an ethics that read every drawing-in as wickedness would have to indict every act of
      devotion ever made."* VIII.7 offers *held against the whole, or expressed as part of it* as
      *"the only one that works here"* — **that is the radiant/contractive definition, not the
      mark.** `through`/`over` as an ethical term: **0 in VIII.7, 2 in all of Book VIII.**
      ⚠ **The operational content still lands** — *who is currently paying for this* **is** `over` in
      civilian words. **What fails is the superlative**, and it is the last instruction in the book.
      `✓` absent:VIII-07:the only one that works here

- [ ] **R2-066** · `VIII-07` §VI — **the Coherence Principle is restated without the half the book
      kept a word for.** VIII.4 deferred the full statement here. Canonical wording: *"coherent
      multi-scale systems holding structural **superposition** until **informed measurement
      collapses** them."* `superposition` is banned in prose, so a restatement was required — and
      `06-THE-SCAFFOLD.md` named the two words reserved to pay for it: **VIII.4's `open`** and
      **II.7's `collapse`, which kept its word precisely for this.** What §VI delivers uses neither.
      Measured in the chapter: `measurement` 0, `informed measurement` 0, `collapse` 1 and in the
      other sense one section above. **The canonical claim has a terminator; the delivered one is a
      static coupling.** Note 5 claims the substitute *"carries the same content"* — the terminator
      is a subtraction and it is not disclosed.
      `→` *Coherent multi-scale systems hold matters open until informed measurement collapses
      them* — one line, in words the book owns, with the structure/process sentence kept beside it
      as the gloss it actually is.
      `✓` manual:VIII-07 §VI restatement carries the terminator

- [ ] **R2-067** · `VIII-07` — `card_sweep` reports the closing chapter carries **no census card**
      (`null=0`, partial). Probably deliberate; flagged so it is a decision rather than an omission.
      `✓` ruling:Clayton — deliberate or restore

- [ ] **R2-068** · `V-10` L27–28, p.564 — the chapter narrates its own repair in body prose in its
      fourth paragraph: *"Four passages, and four of the gaps in them were closed on the way here.
      They are open again now, and the marks are James's, restored."* A reader has no idea what was
      closed, by whom, or when. **The sentence is doing real work** — the chapter's argument is
      about what a report loses in transmission and it is right that it must not smooth its own —
      but the work is being done in the maintainer's register.
      `✓` manual:V-10 opening repair narration recast for a reader

- [ ] **R2-069** · `III-06` — the one chapter in Book III that receives a handoff and passes none.
      Six of eight close by naming what comes next; III.6 ends on priority and hands off to nothing,
      and III.7 then opens by reaching back **past** it to III.3 (*"Four chapters ago…"*). III.7's
      own ending is deliberately an ordinary-life close and needs no handoff, so the break is
      one-sided and it is III.6's exit.
      `✓` manual:III-06 closing handoff

- [x] **R2-070** · `VIII-03` — two incompatible *"failure mode"* numberings collide in one chapter.
      The Complements field says *"the **fifth** failure mode IV.1 registers"*; three pages later
      the card says *"This is the **sixth** failure mode the census has kept separate."* Two lists,
      two counters, same phrase, no signal to the reader that they are different registers.
      **BOTH REGISTERS ENUMERATED BEFORE THE REPAIR — every `failure mode` in all 72 files:**
      | register | owner | counts | sites |
      |---|---|---|---|
      | **complement-reachability** | `IV.1` L92–102 | 5: cannot exist · out of reach · inadmissible · declined · **split between institutions that do not speak** | `VI.6`, `VI.8`, `VII.3`, `VIII.1`, `VIII.3` L302 |
      | **instrument failure, running series** | the chapters themselves | 7: saturation (VII.7) · binary in a three-valued domain (VII.8) · presupposed mechanism (VII.9) · wrong objective function (VIII.1) · sample frame inside the region (VIII.2) · open loop (VIII.3) · trait instrument on a state question (VIII.4) | `VII.9` L211, `VIII.1` L232, `VIII.2` L140, `VIII.3` L326, `VIII.4` L217 |
      ⚠ **The row priced the collision as one chapter's and it is two.** `VIII.4` L217 carries the
      identical mis-attribution — *"a seventh mode **the census** has kept separate"* — and the row
      never looked past `VIII-03`.
      ⚠ **The mechanism is not "two counters with no signal." It is one counter wearing the other's
      name.** `VIII.3` L326 and `VIII.4` L217 are the running instrument series, and both attribute
      themselves to *the census*. Worse, `IV.1` L106 explicitly promises *"a sixth mode is likelier
      than not"* about the complement register — so a reader arrives at `VIII.3`'s **sixth** with
      that promise in hand and reads it as the fulfilment. It is not.
      ⚠ Third, unpriced: `VII.9`, `VIII.1` and `VIII.2` each attribute all prior entries to their
      chapters; `VIII.3` alone stripped the attributions, which is half of why it read as a
      different register. Restored.
      **Repair:** both sites now use the series' own formula (*Nth distinct failure mode in N
      consecutive chapters*), `VIII.3` names `IV.1`'s register explicitly and says the two count
      different things — what a card cannot reach vs. what an instrument cannot see — and `IV.1`'s
      open sixth is stated as still open.
      `✓` manual:VIII-03 two counters disambiguated

- [ ] **R2-071** · 18 chapters — **the standing-note pointer is bolted to an arbitrary footnote.**
      It lands on `[^1]` in five chapters and on `[^2]`, `[^3]`, `[^4]`, `[^5]`, `[^7]` and `[^12]`
      in the others; **IV.9's is welded to the end of `[^12]`, the note about the sasquatch
      bar-profile.** A reader meets a general disclaimer about the whole chapter's grading appended
      to one specific citation and reads it as a caveat on *that* citation. The distribution is what
      an automated append looks like when it targets the wrong node.
      ⚠ Distinct from R2-040 and from R2-024 — this is *where* the pointer attaches, not which
      direction it points.
      `✓` manual:standing-note pointer attachment normalised

---

## G — ENDNOTE MARKER ORDER: ONE CLASS, ELEVEN SITES

- [x] **R2-072** · **11 of 63 units with endnotes print their markers out of sequence — 17.5%.**
      Cause found at III.8 and correct: `compile_pdf.py` uses Python-Markdown's footnotes extension,
      which numbers by **definition** order, not appearance order. Repair per chapter is mechanical:
      swap the `[^n]:` definitions and the body markers to match reading order. No prose changes.
      **VII.4 is the worst in the volume by a distance** — 21 inversions across 10 notes.
      ⛔ **THE READ SAID TWELVE AND THE TWELFTH WAS WRONG.** `V-06` was on that list; its markers
      run 1..15 in both orders, zero inversions, nothing uncited. The read's first sweep returned
      13, was corrected to 12, and the answer is **11** — a second error introduced *inside* the
      correction of the first. `tools/endnote_order.py` was written to settle this and carries the
      adjudicated set as a control, so the next disagreement is loud instead of inherited.
      ⚠ **And "VIII.7 is the cheapest to fix" was a superlative over a tie.** Four chapters sit at
      one inversion: III.8, IV.6, VII.6, VIII.7.
      - [x] `III-08` — `1·2·4·3`, 1 inversion; in print note 4 lands two pages before note 3
      - [x] `IV-06` — `2·1·3·4`, 1
      - [x] `VII-06` — `1·2·3·4·5·7·6`, 1
      - [x] `VIII-07` — `1·2·3·5·4`, 1
      - [x] `V-10` — `…9·11·12·10·13…19·21·20·22`, 3 across 22 notes
      - [x] `V-08` — `2·3·4·5·1·…`, 4 across 17 notes
      - [x] `VI-06` — `1·2·3·8·4·5·6·7`, 4; confirmed in print over pp.680–690
      - [x] `VII-03` — `1·2·3·4·5·11·6·7·8·9·10`, 5; note 11 is the falsifier note, cited mid-chapter
      - [x] `VII-05` — `1·2·4·7·5·6·3`, 6
      - [x] `VIII-03` — `1·8·2·3·4·7·5·6`, 8; see **R2-050**, the disclosure understates it fourfold
      - [x] `VII-04` — `3·2·9·10·7·4·5·1·6·8`, **21**, the whole-volume worst
      **PAID D205 / 2026-08-24 — all eleven in one pass by `tools/endnote_resequence.py --apply`,
      89 notes, 46 renumbered; `endnote_order.py` now reads 63 of 63 in order.** Written as a tool and
      not as eleven edits because VII.4 alone is a ten-note resequence, and eleven hand-swaps is how
      ten land and the eleventh reads as finished.
      ⛔ **"No prose changes" above was wrong, and the gauge could not have told me.** `endnote_order.py`
      measures BODY PROSE ONLY — everything above the first `[^n]:` line — which is correct for
      measuring and blind for repairing. IV.6 and VI.6 close with an unnumbered *On the grade of the
      sources above* footer that sits AFTER the last definition and cites notes by number (*"[^1] is
      two-digitisation-grade"*, *"Liu et al. [^8]"*). A renumber that ignored those would have left the
      gauge green while pointing a reader at the wrong source, and a naive tail-sort would have filed
      the footer into the middle of the notes. Both are handled and both are asserted, not reported.
      ⚠ **VIII.3 also disclosed its own disorder in prose** and that disclosure went false the moment
      the repair landed. Rewritten past-tense — and the receipt it was told it could not have,
      *"cannot have its own note without renumbering"*, now has one: the constraint the note recorded
      was lifted by the pass, so the note was split and the Ignatius receipt sits at the schedule claim.
      ⚠ **The control in `endnote_order.py` inverted on success.** "Reproduces the adjudicated set
      exactly" is a passing control before the repair and a permanent false alarm after it — it fired
      the instant the book was correct. Rebuilt as a REGRESSION control (nothing repaired comes back,
      nothing unadjudicated appears) plus a synthetic positive case, because zero out-of-order chapters
      is also exactly what a silently-broken parser reads.
      `✓` cmd:python tools/endnote_order.py

- [x] **R2-073** · `V-07` — a related but different finding, kept separate so it is not folded into
      the twelve. V.7's Notes **headnote** cites `[^1] [^2] [^3] [^5] [^10] [^14]` while discussing
      the apparatus, and `[^1]` is cited **nowhere in V.7's body prose** — its only pointer is
      inside the note block it belongs to. The reader meets note 1 only in a sentence about the
      notes. **Not an ordering defect**; 1 unit of 63, 1 note of 16.
      ⚠ Recorded because the same gauge run with a sloppier boundary returned **13** and would have
      handed Clayton a corrected count that was itself wrong. **The correction of a superlative is
      where a second error is cheapest to introduce.**
      ⛔ **WITHDRAWN D205 — THE PREMISE IS FALSE. `[^1]` IS cited in V.7's body prose**, on the
      chapter's seventh line, as the first note reference in the chapter: *"a roster assembled to make
      one point[^1]: that instruments sharing nothing but a target return convergent readings."* Two
      instruments agree — `note_binding.py` reports 0 orphans volume-wide with its synthetic control
      detecting a planted one, and `endnote_resequence.py` refuses any chapter with an uncited note and
      passed V-07 clean. I do not know how the read produced this row; what I can say is that it was
      hand-made and never run against `note_binding.py`, which was already in the repo and already
      green. ⚠ **The row warns in its own last line that "the correction of a superlative is where a
      second error is cheapest to introduce" — and is one.** The satisfaction condition below,
      *note 1 given a body pointer*, was already met by the text when the row was written.
      `✓` manual:V-07 note 1 given a body pointer or folded

---

## H — TOOLS: THE FOUR REPAIRS THAT STOP THE RECURRENCE

**These are not text edits and none of them is visible to a reader. Each one is the reason a row
above exists, or the reason the next one will.**

- [x] **R2-074** · `tools/bibliography.py` **has no caller anywhere in the repo.** `compile_pdf.py`
      globs `Z-*` and renders whatever markdown is on disk. It regenerates only when a human
      remembers, and no one has since Day 195. **A generator with no trigger is a hand-typed page
      with extra steps** — which is the exact object Z.2's own header condemns. This is why R2-053
      exists and why it will exist again.
      `→` Wire it into the build, or add a release gate that fails when the generated page differs
      from the page on disk.
      `✓` manual:bibliography.py invoked by the build or gated
      **PAID D205 — BOTH HANDS, because the build one cannot fire in this body today.**
      `book/compile_pdf.py` now runs the generator BEFORE it globs `Z-*`, and aborts the compile
      on a non-zero exit rather than rendering a page it knows it could not rebuild. Verified
      end-to-end, not asserted: the compile ran, printed `regenerated works-cited: RECALL GAP
      122`, and wrote **1,073 pages** (HEAD's committed build was 1,076 — the three pages are
      today's deletions; text at p.501 is byte-identical, font resources unchanged).
      ⛔ **AND IT ONLY RAN UNDER WSL.** WeasyPrint's Windows import is dead in this body —
      `OSError: cannot load library 'libgobject-2.0-0'`. It built fine yesterday (`3d92dfe`,
      15:52). The only `libgobject-2.0-0.dll` on the Windows side now lives inside a **OneDrive
      version directory** that auto-updates its own name, so whatever made the import resolve was
      never a declared dependency. **A build hand that works by borrowing a dll from an
      auto-updating application is a trigger with a clock on it.**
      → So the second hand is the one that matters: **gate 7, `R-240`**, in the live queue's
      release table, measured by `bibliography.py --check`, exit code IS the verdict.
      `release_gates.py`'s `MEASURED` map now carries an **argv tail** rather than a filename —
      bare `bibliography.py` REWRITES the page, so a gate calling it would pass by doing the work
      instead of finding it done. [[feedback_instrument_fix_vs_relaxation]]
      **BOTH BRANCHES EXERCISED, in the state where the answer differs:** current page → gate 7
      MET, `release_gates.py` exit 0. Planted stale page → `⛔ OPEN — bibliography.py --check
      exit 1`, *"1 gate(s) OPEN — upload is blocked"*, exit 1. Restored → green.
      ★ **The row's premise was proved as an event while I was closing it.** `--check` said STALE
      on a page R2-053 had regenerated **at 14:44 today**. Today's Book-VIII repairs made one more
      citation parseable — *Spiritual Exercises* (VIII.3) — and the page went 150 entries to 151,
      124 parsed to 125, **with nothing saying so**. Ten days of drift was the headline; the real
      number is **three hours**.

- [x] **R2-075** · `tools/relative_ref_sweep.py` **is line-scoped against a hard-wrapped
      manuscript**, so **26 sites (12.6%, across 18 chapters) are invisible to it — including
      R2-043's**, the one that is actually wrong. My first diagnosis (missing possessive vocabulary)
      was wrong and I tested it; `PAT_ADJ` matches the possessive fine. The mechanism is that `the`
      sits on line 174 and `previous chapter's card` on line 175. The run prints `resolvable:
      157/169`; **169 is a denominator the tool generated for itself and it is short by 26.** The
      docstring is scrupulous about two *precision* limits it knows. This third one is a **recall**
      hole and nothing declares it.
      `→` Unwrap single newlines within a paragraph before matching. Then re-run and read the 26.
      `✓` manual:relative_ref_sweep.py unwraps paragraphs and its denominator reaches 206
      **PAID D205 — AND 206 WAS NEVER THIS TOOL'S NUMBER.** The unwrap is done and it is worth
      exactly what the row said: **169 → 188, nineteen sites that had never been seen whole.**
      But the gate is unclearable as written, and the reason is in this row's own source. The
      D204 table reads *"visible line-scoped, as the tool reads: **180**"* — and the run it
      quotes four lines later prints **169**. **An 11-site gap between the hand-pattern and the
      tool, line-scoped, in adjacent paragraphs, unremarked.** So 26 was never the wrap's size;
      it was the wrap plus a vocabulary difference, two defects wearing one number.
      [[feedback_self_generated_denominator]]
      Diffing the unwrapped tool against a loose hand-pattern found the rest, and the class is
      **bigger than either count**: bare adverbial (*stated last chapter*, no article, 4) ·
      numeral-infix spans (*the next nine chapters*, 13) · postpositive counts (*four chapters
      after it*, 7) · out-of-vocabulary numerals (7) · the vague class (*a later chapter*, 13,
      declared out-of-scope rather than left silent). **169 → 232.**
      ⛔ **AND THE WIDENING EXPOSED A TRAP THE OLD TOOL WAS ALREADY FALLING INTO.** `seven`
      matches inside *fifty-seven*, because a hyphen is a word boundary — so *"the fifty-seven
      chapters before this one"* resolved as **SEVEN BACK**, a confident wrong answer in the
      same face as a right one, which is the single thing this tool's header says it must never
      do. Guarded, and the guard's own hole — an unparseable count silently dropped — closed in
      the same edit by printing it unresolved.
      ★ **The book defect is in the closing chapter.** `VIII-07` §the-borrowed-word endnote said
      the fence was knocked down *"four chapters after it was built"*. It was built in **VII.4**;
      the final chapter is **twelve** later. Invisible to this gauge for its whole life, in the
      last chapter of the volume. → `twelve`. Controls added for all four traps, plus a
      regression control that **fails on the Day-204 code**, and a negative fixture checked to
      fire when joined so it is not green by construction.
      ⚠ **Declared residue, because it is unmeasured rather than absent:** structure is not
      joined, so a reference straddling a heading, list item or table row is still invisible.
      The tool now says so on every run.

- [x] **R2-076** · `Z-02`'s machine-uncertain rule **fires on single-word entries only.**
      Regenerating tonight introduces *"January 10, 2013, a review of Koch's" (Cambridge, MA: MIT
      Press, 2012) — II.4* — a nine-word fragment of the note's prose standing where a title goes,
      and the rule cannot see it. It also drops *Sartre (1943) — VII.7*, the page's own predicted
      residue, since repaired upstream. **The instrument is right about its blind spot and the blind
      spot has moved.**
      ⚠ **This must land before R2-053** or the regeneration ships a new unflagged mis-parse.
      `✓` manual:machine-uncertain rule widened past single-word entries
      **PAID D205 — AND THE ROW'S PREMISE WAS WRONG WHILE ITS PREDICTION WAS EXACT.** The rule does
      not "fire on single-word entries only"; that rule was *removed* before this row was written,
      for measured cause (2 true positives against 15 false alarms). What the rule actually held
      was a list of *specimens* — five literal prose fragments, each added the day it was met. The
      Koch fragment escaped because nobody had met it yet, which is the failure mode of every
      instance list. Widened to name SHAPES: a span that opens on a date, ends on a possessive, or
      carries a reviewing connective. Controls held — `Aion`, `Angst`, `Ethics`, `Nature` all
      unflagged. 6 of 150 flagged, and the Koch fragment is one of them. **The page's declared
      residue was also stale** — it described the deleted rule's blind spot, not the one it has —
      and now declares both survivors, the bare surname and the journal name.

- [x] **R2-077** · **no gauge in this repo watches citation-forwards.** `tools/note_binding.py`
      audits marker→note in both directions and reports **0 orphans, 0 dangles across 528
      endnotes** — and is structurally blind to R2-058, R2-047 and R2-048, because those notes
      exist, are reachable, and point at a *source* rather than at a note. Three chapters running in
      Book VIII carried a provenance note that got the provenance wrong.
      `→` A name-census gate over *"spent earlier"* / *"used at"* / *"occurs N times"* claims,
      run over the unwrapped source.
      `✓` manual:citation-forward gate exists and runs
      **PAID D205 — `tools/citation_forward.py`, wired as release gate 8 (`R-241`), and it is
      OPEN, correctly.** 14 self-census claims across 67 chapters: **9 agree · 1 DISAGREES ·
      0 unread · 4 acknowledged by hand.** The DISAGREES is **R2-058** — *"used in this manuscript
      at VII.3 and VII.4"*, and the gate prints `⛔ EMPTY ROOM(S): VII.3, VII.4`. The row that
      asked for the gate is the row the gate finds.
      ⚠ **THE FIRST VERSION WAS A NOISE GENERATOR AND WOULD HAVE BEEN WORSE THAN NOTHING.** On
      its first live run it reported 13 of 15 claims wrong. Four of those were a 240-character
      quotation adopted as a "subject"; the rest were **scope**: it counted the whole volume for
      every claim, so it flagged `blind spot` at VIII.2 — **against the sentence R2-047 had already
      repaired**, which correctly says *in VI.8*. It committed R2-047's error while checking for
      R2-047. A gate that cries wolf trains its reader to skip it.
      ⛔ **AND THE END-TO-END CONTROL CAUGHT A SECOND ONE THE REGEX ASSERTS COULD NOT.** Scope was
      resolved by pattern precedence, so R2-047's original — *"occurs eleven times **in this
      manuscript** and every one of them is **in VI.8**"* — resolved to VI.8, counted 11, and
      **PASSED**. Fixed to earliest-stated-scope-wins; that in turn read *"in the manuscript
      before this line"* as the whole volume and falsely flagged `philia` at VII.6, so a narrowing
      qualifier now beats position while two rival scopes are still decided by position. Both
      fixtures are in the control and both are built where the two rules DISAGREE.
      ⛔ **Writing the acknowledgement file put the gate inside its own corpus** — `book/*.md`
      picked up `CENSUS-ACK.md` and the claim total went 14 → 16 the instant it was saved. The
      corpus is chapter files now, asserted.
      ★ **`occurs` and `is used` are not the same claim.** Aquinas is NAMED 23 times and USED as a
      source four; both sentences are true. Sense verbs are routed to a human, never counted.
      **The four unreadable claims are adjudicated in `book/CENSUS-ACK.md`**, by hand, with the
      measurement where one exists — `Watts` really is absent from I.6, `summit` really is ×5 in
      V.1 — because a gate whose alarm branch is its only branch is unclearable by construction.

---

## NOT ON THIS LIST, ON PURPOSE — SO IT IS NOT RE-FOUND

**61 items were raised and cleared during the read.** They are in `review/READ-NOTES-D204.md` under
`✅` and they are kept there for exactly this reason. The four that a later pass is most likely to
re-file:

- **The standing note reading *"above"* is CORRECT in print, in all 18 sites.** I filed it as a
  17-file repair after Book IV and **withdrew it at Book VI**: in the markdown the standing note
  sits below the definitions, and Python-Markdown hoists the definitions to the end, which inverts
  them. I read the source and the reader gets the PDF. **No repair is owed.** (R2-040 is the one
  genuine inverse site.)
- **The detached `1. 2. 3. 4.` cluster at the foot of every notes block is a PyMuPDF text-ordering
  artefact**, present identically in passed and suspect chapters. Rasterised and checked: markers
  sit correctly beside their items. The instrument, not the book.
- **The missing blank line before `[^6]:` in `VII-08` does not fold Camus into note 5.** Counted
  printed backlink glyphs rather than reading the markdown: VII.8 defines 11 and prints 11. The
  extension tolerates it. Candidate refuted.
- **Book IV's body prose does not leak — 0 occurrences in 47,923 body words.** The Book II repair
  was correctly scoped away from Book IV; it is Book V that reverses it, not Book IV.

**And the volume's clean results, which a defect list of 48 rows will otherwise misrepresent:** the
supersession rule holds across all 71 units with no gauge enforcing it; self-citation is 0 sites
with a live detector that catches 3/3 planted cases; VIII.4 is seven checkable claims and seven
verified; the VII.8 ↔ VIII.7 handshake closes in both directions; every outside-read fact in C.2 §IV
is exact, including *"roughly 21,700 words"* against a measured 21,678, rounded away from the
flattering direction.

---

## SHAPE OF THE WORK

| group | rows | what it is |
|---|---|---|
| **A** — the argument | 2 | the only finding that touches the argument, plus its other side |
| **B** — cross-cutting | 5 | one ruling from Clayton, then mechanical |
| **C** — one word / one line | 10 | under five minutes each, no decision needed |
| **D** — counts on the page | 9 | a reader could check these and find them false |
| **E** — off-page rosters | 4 | print it, or drop the claim that rests on it |
| **F** — structure | 12 | needs thought; R2-060 is the largest |
| **G** — endnote order | 2 | one known cause, eleven mechanical sites |
| **H** — tools | 4 | invisible to a reader; each is why a row above exists |
| **total** | **48** | R2-030 … R2-077 |

⚠ **This table is checked, not trusted.** `python tools/revision_checklist.py --verify` re-counts the
rows and **fails** if any cell here disagrees with the file. I typed `5` and `49` into it on the
first pass and the numbers were 4 and 48 — a hand-typed tally inside the very document arguing
against hand-typed tallies. The gauge is there because I made the mistake, not in case someone else
does.

⚠ **R2-072's twelve chapter sub-boxes count as one row here** and are reported separately by the
tool.
