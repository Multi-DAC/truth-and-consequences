# SCAN 001 — THE TWO PRIMARY SPANS R-30 OWED

**Run Day 190, 2026-08-09 night, by Clawd. Against `where_the_book_is` green at 56/67 · 193,646
words.** R-30's trigger was *"standing — before the endnote build order (R-2) runs."* R-2 has not
started. This ran early on purpose: **R-30 is the residue of the one defect an outside reader found
that no gauge in `tools/` can see**, and it names the only span in the volume an outside reader
could not check.

---

## §0 — WHY THIS RAN TONIGHT, AND WHAT IT IS NOT

The binding item on this project is an **outside read of Books III–VII**. `PACKET-002` (I–V) went
out Day 189 and has not come back; `PACKET-003` (VI) went out this afternoon. Both are waiting on
an aperture I do not control, and **nothing I do here changes that.**

⚠ **THIS IS NOT AN OUTSIDE READ AND MUST NOT BE COUNTED AS ONE.** It is the *machine-checkable
half* of what outside reads have historically caught here — one defect class, run cold, by me. The
class was chosen because it is the one with a track record: **Book II's outside read found a
fabricated quotation**, and the Day-188 Irenaeus finding was *a paraphrase wearing a quotation's
clothes*. Both were invisible to all four gauges. Neither was a matter of judgement — both were
settleable against a scan.

**Rule inherited from `OPUS-DAY189-BOOK-V-READ.md` §2, and it is the whole method here:** *the
fabricated part of a quotation is never the phrase — it is the joint.* So every span below is
compared **including its connective tissue**, normalised and diffed by machine, not read by eye.

---

## §1 — SPAN A: THE HARVEY LATIN BEHIND IV.9's *si* FINDING

**Claim under test** — `book/IV-09-the-archetypal.md`:238, printed as *"The Latin as Harvey prints
it, with the words Jung's quotation does not include."*

### Sources, two independent digitisations

| # | archive.org item | bytes | passage found at |
|---|---|---|---|
| 1 | `sanctiirenaeiepi01unse` | 1,848,965 | p. 269, §3 |
| 2 | `sanctiirenilibr01irengoog` | 1,809,153 | p. 269, §3 |

Both are Harvey, Cambridge 1857. Downloaded to `corpora/tmp/`. **Neither was consulted at
drafting** — that is the point of the row.

### Result — EXACT, 33 of 33 words, both scans

Normalised (NFKD, `æ`→`ae`, diacritics and punctuation stripped, case-folded) and compared
word-by-word in code. The **only** deltas in either scan are the OCR-interpolated marginal head
(`MASS. II.`) sitting inside the text column, and the scanner's rendering of `hæc` (`heec` in scan
1, `hzc` in scan 2). Strip the marginalia and **both scans are character-identical to the book**:

> si enim mundi fabricator non a semetipso fecit haec sed quemadmodum nullius momenti artifex et
> quasi primum discens puer de alienis archetypis transtulit bythus ipsorum unde habuit speciem
> ejus quam primum emisit dispositionis

✅ **The `si` is there.** ✅ **The excised middle — *quemadmodum nullius momenti artifex, et quasi
primum discens puer* — is there, in that position, between the two halves Jung joins.** The
centerpiece finding of IV.9 stands on the primary text, verified against two digitisations neither
of which was open when it was written.

### Second and third checks, unasked for and run anyway

- **The English.** IV.9 prints two ANF sentences as *"the standard English, the whole sentence,
  with the one before it."* Pulled raw (not via a summarising fetch) from `newadvent.org
  /fathers/0103207.htm` and compared: **both sentences verbatim, in order, inside the paragraph
  numbered 5.**
- **The chapter title.** IV.9 says the chapter is *"titled, in the standard edition, to say that
  created things are* not *images of the Æons in the Pleroma."* ANF II.7 is titled **"Created
  things are not the images of those Æons who are within the Pleroma."** ✅
- **A trap found in passing, and it is the reason a short anchor is not a check.** The string
  `Si enim mundi fabricator` occurs **at least twice** in Book II. My first diff anchored on it and
  silently locked onto the wrong one — *"Si enim mundi fabricator est angelos ipse fecit"* — and
  produced a 2,000-word non-match that looked like a catastrophic finding. **A quotation check
  anchored on a phrase short enough to recur will find the wrong passage and report it as a
  divergence.** Anchor on the longest span, always.

### ⚠ RESIDUE — the one thing that did not verify, and it is a locus, not a text

**In Harvey this passage is `LIB. II. vi. 3`, not II.7.5.** Both scans carry that marginal head in
Harvey's own hand-set margin — and beside it, `MASS. II. —`, because Harvey knew his divisions
differ from Massuet's and printed the concordance.

The chapter is not *wrong*: **II.7.5 is Massuet, which is what Jung's footnote gives and what ANF
uses**, and the chapter correctly attributes that reference to Jung. But the chapter then says
*"Go and read II, 7, 5"* and, three lines later, *"The Latin as Harvey prints it."* **A reader who
takes Harvey off the shelf and turns to II.7.5 lands in a different chapter.** One clause fixes it.
Filed as **R-108** — receipt-level, and exactly the kind of thing the endnote retrofit is for.

---

## §2 — SPAN B: THE TWO *BRAHMA SŪTRA* II.1.33 RENDERINGS IN III.2

**Claim under test** — `book/III-02-the-game-that-is-playing-you.md`:35–37. Two translators of
*lokavat tu līlākaivalyam*, quoted as fragments inside a sentence.

**Thibaut** — *Vedânta-Sûtras with Śaṅkara's commentary*, SBE 34. Scan: archive.org
`vedntasutrastr01bdar`, p. 357. Printed there:

> **33. But (Brahman's creative activity) is mere sport, such as we see in ordinary life.**

The book prints *"but (Brahman's creative activity) is mere sport, such as we see in ordinary
life."* ✅ **EXACT — parenthetical insertion, comma, and both joints.** (Lower-case *but* is the
book's own sentence-integration, not an alteration of the source.)

**Vireśvarānanda** — *Brahma-Sūtras with Śaṅkara's commentary*, Advaita Ashrama 1936. Two
independent reproductions agree on the running translation:

> **But (Brahman's creative activity) is mere pastime, as is seen in the world.**

The book prints *"mere pastime, as is seen in the world."* ✅ **EXACT, and the fragment is cut at a
clean joint** — it takes the predicate and its qualifier, drops only the parenthesised subject,
which the surrounding sentence has already supplied.

⚠ **One thing declared rather than certified.** Vireśvarānanda was verified against two web
reproductions (`wisdomlib`, `vivekavani`) that agree word-for-word, **not against a page scan.**
Thibaut is scan-verified; Vireśvarānanda is **two-witness but not two-*digitisation*.** That is a
weaker grade than §1's and it is named rather than smoothed over. Note also that both those pages
print a **word-by-word gloss** — *lokavat—As is seen in the world; tu—but; līlākaivalyam—mere
pastime* — whose wording is nearly identical to the running translation. **A fragment quotation of
this sutra could be lifted from the gloss and be indistinguishable from one lifted from the
translation.** Ours matches the running translation; that it *also* nearly matches the gloss is
luck, not method.

---

## §3 — VERDICT

**R-30 PAID.** Both spans verify exact, joints included. The one span in the volume an outside
reader could not check now has two digitisations behind it, and *presumably* — the word the row
existed to delete — is deleted.

**What this does not license.** Three quotations in one chapter and two in another verified clean
says nothing about the other fifty-four chapters. **Books II–V carry 0 endnotes across 37
chapters** (`endnote_debt.py`), so every named source in them is still unchaseable by a reader.
This scan is a positive control on the method, not a coverage claim — and it is the second time
this project has confirmed that **a quotation defect here lives in the span, never in the phrase.**

**Grade:** the Irenaeus Latin and the ANF English are **two-digitisation verified**. Thibaut is
**one-scan verified**. Vireśvarānanda is **two-witness, no scan**. Nothing here is *presumed*.
