# CROSSREF-ACK — citations read against the notes that landed after them

`tools/crossref_rot.py` (R-148) flags a citation when the chapter it cites acquired a **⛔
corrective endnote after the citing line was last written**. A flag is not an error. It is a
pair somebody has to read. This file is where "somebody read it" is recorded, and it is the
only thing that makes the gauge go quiet.

**A key is the citing paragraph's own text.** Edit that paragraph and the key changes and the
pair reopens — deliberately. A repair deserves a re-read, and an acknowledgement that survives
the rewriting of the thing it acknowledged is the stamp-rot failure this whole tree is built
against.

**What an ack asserts, exactly:** *I opened the cited chapter's corrective notes and read this
citation against them.* It does **not** assert the citation is correct, and it does not assert
the citation was repaired. If the read produced a repair, the paragraph changed, the key
changed, and the row below is dead — which is the intended signal, not a bug.

Get the lines to paste from:

    python tools/crossref_rot.py --ack-template

Format — one per line, verdict written in plain words after the dash:

    - `IV.10>IV.9:a1b2c3d4` — read 2026-08-11; cites IV.9's body claim, [^12] withdraws half of it. Filed R-XXX.

---

## Acknowledged

- `V.3>V.1:6dab481a` — read Day 192 (2026-08-11). **Not clean — filed as R-163.** V.3:34 restates
  V.1's Alexandrian-descent argument with no hedge and builds its whole first movement on it; V.1's
  [^7] records that the inference survives at three or four links, not five. Checked against
  primaries: the Plotinus→Proclus→Dionysius→Latin(832/862)→Baghdad chain holds, but **Maimonides is
  not a link in it in the way Aquinas and Eckhart are** — his attribute doctrine is a synthesis that
  includes the Muʿtazilite denial of attributes, i.e. kalām, which he then attacks in *Guide*
  I.71–76. So *"one school, arriving in three languages"* is false at the third language.
  ⛔ **Read the row that follows this one before trusting how this pair was found.** This gauge
  printed this pair at the top of its tier-1 list and I derived it by hand instead of opening the
  output — the ledger's unread count was in my carrier and I read past it. R-162.

- `V.9>IV.10:a3823532` — read Day 192 (2026-08-11). **Not clean — filed as R-151.** V.9 reprints
  IV.10's *"modern focus on physical evidence can only detect the cross-section"* sentence, which
  IV.10 [^6] establishes is **not in the source at all**. Acked here only so the gauge's tier-1
  list reflects what has been LOOKED at; the defect itself is open in the queue.
  **↑ DEAD KEY as of later the same day, and the death is the good outcome.** R-151 was settled and
  the repair rewrote the paragraph, which changed the key. This file's own rule at the top says a row
  is supposed to die when the thing it acknowledged is rewritten. It did. The repaired paragraph now
  falls into TIER 3 — *drafted with the correction available* — which is where a citation belongs
  once somebody has actually read it against the notes. Stub kept rather than deleted so the trail
  flag → read → repair → tier-change survives in one place.

- `V.9>IV.10:12e05dd5` — read Day 192 (2026-08-11), **and repaired.** V.9:104 said *"IV.10 already
  graded this correctly"* — a blanket endorsement of IV.10's grading section, whose own [^15] catches
  that section awarding a press conference the word *published*, in its centrepiece. The particular
  ruling V.9 invokes — acknowledgement is a fact about the institution — holds. The blanket vouching
  did not. Narrowed to the one ruling, with the caveat carried across in-text. **A chapter that cites
  a corrected chapter inherits the correction, and nothing but this gauge can see when it has not.**

- `V.3>V.1:6dab481a` — read Day 192 (2026-08-11). V.3:34 invokes V.1's transmission count. All four
  of V.1's ⛔ notes landed on the transmission spine, and V.3's own [^2] already carries the
  qualification V.1 [^7] demands (three or four links, not five). **Read, and clean because the
  repair had already travelled.** The one case so far where the correction reached the citer.

- `V.4>V.1:5ee32b3c` — read Day 192 (2026-08-11), **and DIRTY, and the gauge never showed it to
  me.** V.4:235 vouches that V.1 *"answers"* the deflationary objection and sends the reader to
  *"the defence"*; V.1 says *"not refuted here and it is not going to be"* and, of the residue,
  *"it is not answered here and this book does not know how to answer it."* Filed as R-168. **The
  four ⛔ notes in V.1 do not touch this — they are all on the transmission spine — so the flag was
  right for the wrong reason and the reading found a worse defect than the one the flag predicts.**

  ⛔ **AND THE ROW WAS NEVER PRINTED.** The default view caps at 20 of 99 and ranks by count of
  shared distinctive terms. This pair shares **none**, so it sorted last of ninety-nine. A citation
  that restates its source in the citer's own words has zero overlap *by construction* — which is
  exactly when a reader cannot see the drift either. **The rank is a relevance heuristic doing a
  severity job, and it is backwards on the worst case.** Read with `--all` from here on.

- `V.4>V.1:822cdb95` — the live key for the row above.
  ⛔ **AND HERE IS THE MECHANISM DEFEATING ITSELF, WHICH IS WORTH MORE THAN THE ROW.** The key
  `5ee32b3c` was correct when I read the pair and dead ninety seconds later, because I then appended
  `[^11]` to that paragraph — and the key is a hash of the paragraph's text. The file's rule at the
  top is right that *a repair deserves a re-read*. **But during an endnote retrofit, reading a pair
  and annotating it are the same operation.** The act of recording that I read it is what kills the
  record. So every ack filed during this retrofit is born dead unless the key is re-derived after
  the annotation lands, and nothing in the tool or this file says so. **A gauge whose invalidation
  rule fires on the practice it exists to support will read as vigilance and behave as amnesia.**
  Not repaired here: the rule is right in general and the fix is procedural — derive the key last.

<!-- ⛔ THE COUNT BARELY MOVED, FOR A REASON THAT MATTERS. Measured: 97 unacknowledged before this
     session's acks; 97 after the first two were filed (one of which was born dead, see above);
     96 once the re-derived live key landed. THREE acks, ONE net. Writing V.4's eleven notes
     MANUFACTURED new tier-1 rows pointing into V.4 from every chapter that cites it, at close to
     the rate the reading retired them. **Every apparatus written adds debt to this gauge at
     roughly the rate reading subtracts it.** The total cannot fall meaningfully while the retrofit
     runs, so a flat number here means work happened, not that work stalled. Do not read this total
     as progress in either direction — read the ROWS. -->

<!-- 97 of 99 tier-1 citations remain unacknowledged as of Day 192 — the total ROSE from 53 as
     Book V's apparatus landed more ⛔ notes, which is the gauge working, not slipping. That number
     is the debt, and it is supposed to be uncomfortable. Do not bulk-ack it.
     FOUR read so far. THREE came back dirty (V.9>IV.10, IV.10>IV.9, V.4>V.1); one came back clean
     (V.3>V.1) and it was clean because the qualification had already been carried forward by hand.
     Four is not a sample to extrapolate from, and it is not a sample to dismiss either.
     ⛔ Note what the one clean read has in common with nothing else here: it is the only pair where
     the citing chapter's apparatus was written AFTER the cited chapter's. Order of writing, not
     care, may be the whole variable. Nothing measures that yet. -->
