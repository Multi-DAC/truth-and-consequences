# SWEEP-001 — THE EDITION/SCHEME SWEEP

**Day 190, 2026-08-09, night. R-108's sibling clause, run.**
Instrument: `tools/edition_scheme_sweep.py` (written tonight, for this).
Population: the 56 drafted chapters. Result: **10 exposed loci out of 368 distinct cited works.**

---

## §0 — WHAT THIS IS NOT

**This is not the outside read.** `PACKET-002` (Books I–V) and `PACKET-003` (Book VI) are still out
and unreturned. This is a self-run mechanical census with one span verified against a licensed
digitisation. It settles one row's sibling clause. It settles nothing about the argument.

**And it is not a clean bill.** Read §4 before reading §1 as good news.

---

## §1 — THE CLAUSE, AND WHY IT NEEDED AN INSTRUMENT

R-108 closed with: *"check the same pair everywhere the book cites a critical edition by a standard-
scheme number — this is one instance and the sweep has never run."* That is a sweep with no hand:
a stamp. The general form it names —

> **an EDITION and a CITATION-SCHEME are two different facts, and prose that names one while
> numbering by the other reads as a single correct citation**

— is invisible to every gauge in `tools/`, because none of them knows what edition a number belongs
to. So the sweep got built rather than promised.

**Built from the general form, not from Irenaeus.** A grep derived from the defect just found
returns its own reflection. Pass 1 enumerates *edition-namings* (sigla + "as X prints" + "X's
translation"); pass 2 enumerates *loci*; pass 3 enumerates *every italicised work-title* and reports
which carry a locus at all. The third pass is the one that matters, and it is the one that reports
against the sweep's own interest.

**Three defects in the instrument, found and fixed mid-run, each recorded in the source:**

1. **The numeric pass could not see `Gate III, chapter 4`.** A locus whose scheme is spelled in
   words — Gate, Ennead, Question/Article, Nikāya — matched nothing. Found by hand, not by gauge.
   Pass 2b exists because of it, and that single miss is where the sweep's best finding came from.
2. **`JOURNALISH` listed six journal names and let `Personality and Social Psychology Bulletin`
   through** on its opening word. Replaced with a shape test as well as a list.
3. **The internal-pointer filter ate four of five real hits.** `Confessions VI.3`, `Adversus
   haereses II, 7`, `De Rerum Natura III, 832` are all indistinguishable in shape from this book's
   own chapter pointers, so the filter that keeps `II.4` out of the results also removed the
   citations the sweep exists to find. The count fell 11 → 5 and **the shorter list looked cleaner.**
   A locus standing after a named external work is external by construction; the filter is now off
   in pass 3, with the reason in a comment beside it.

Defect 3 is the one to remember: **an over-eager filter produces a result shaped exactly like a
good result.** Same family as the anchor that found the wrong passage six hours ago.

---

## §2 — THE POPULATION (10)

| # | Where | Citation | Edition named? | Status |
|---|---|---|---|---|
| 1 | `IV-09`:231,234 | *Adversus haereses* II, 7, 5 | **Harvey** | ⛔ **R-108 — DEFECT.** Harvey prints it at `LIB. II. vi. 3`; II.7.5 is Massuet's |
| 2 | `V-06`:103 | *Nefesh HaChayim*, Gate III, ch. 4 | **Moskowitz** | ✅ **VERIFIED TONIGHT** — see §3. One residue (imprint), rowed |
| 3 | `III-02`:35 | *Brahma Sūtra* II.1.33 | Thibaut / Vireśvarānanda | ✅ verified under R-30 (Day 190) |
| 4 | `VII-01`:277 | *De Rerum Natura* III, 832–842; 972–977 | — | ◻ unchecked |
| 5 | `VII-01`:272 | Diogenes Laertius, *Lives* X, 124–125 | — | ◻ unchecked |
| 6 | `VI-04`:374 | *Confessions* VI.3 | **none, by declaration** | ◻ unchecked — the note *says* it renders the standard sense rather than a published translation, which is the honest form of this problem |
| 7 | `VII-04`:485 | *Confessions* VII.12 | — | ◻ unchecked |
| 8 | `VII-04`:485 | *Enchiridion* 11 (Augustine) + *City of God* XII.6–7 | — | ◻ unchecked |
| 9 | `VII-04`:446 | *Summa Theologiae* I, q. 64, a. 2 | — | ◻ unchecked (universal scheme; low risk) |
| 10 | `VII-05`:374 | *Saṃyutta Nikāya* 36.6 + Epictetus, *Enchiridion* 5 | — | ◻ unchecked |

**Noted in passing, not rowed:** rows 8 and 10 cite two different works both called *Enchiridion*,
one chapter apart, each by bare number. Both are author-attributed in the same clause, so a reader
can resolve it. It is the R-108 family standing one notch short of a defect.

---

## §3 — THE ONE SPAN CHECKED TONIGHT: *NEFESH HACHAYIM*, GATE III, CH. 4

Chosen because it is the **exact R-108 pair shape** — a named translation *and* a locus — and it is
a **block quotation** sitting in Book V, which has no endnote apparatus and therefore no gauge over it
at all.

**Locus: CORRECT.** All fourteen chapters of Gate III were pulled and searched, so the anchor's
distribution across the gate is known rather than assumed. The sentence is in ch. 4 and only in
ch. 4; ch. 6 and ch. 7 carry cognate phrasing on the same doctrine and are not it.

**Translator: CORRECT, and verified rather than trusted.** Sefaria's English version metadata reads
*"The Soul of Life, translated by Leonard Moskowitz, Teaneck, NJ 2012 [Rev. 1.5]"*. This mattered:
had the served text been a different translation, a word-perfect match would have proved the
attribution **false** — the book quoting one translator and crediting another.

**Words: 32 of 32 exact, diffed in code, not by eye.** Two silent alterations inside the quotation
marks:

```
source  And He [emphatic] is still now just as He was before the creation, when all was
        filled with the essence of the Ein Sofe (blessed be He), even in the space where
        the worlds currently exist.
book    And He             is still now just as He was before the creation, when all was
        filled with the essence of the Ein Sof,                even in the space where
        the worlds currently exist.

delete   [emphatic]                        <- the translator's own apparatus mark
replace  Sofe (blessed be He),  ->  Sof,   <- a pious formula, cut without ellipsis
```

`[emphatic]` is arguably *correctly* dropped — reproducing another editor's markup inside your own
quotation is its own error. `(blessed be He)` is not: it is running text in the translation, removed
with no mark. And `Sofe → Sof` normalises a translator's idiosyncratic transliteration in silence.
Small, real, and the mild form of the Day-188 Irenaeus finding: **an abridgement wearing an
unabridged quotation's clothes.**

⚠ **ONE-WITNESS, and the record says so rather than rounding it up.** Sefaria's Moskowitz is marked
`Rev. 1.5` — a revised digital text, not the 2012 print. The two-digitisation discipline is *not*
satisfied here. Unlike the Harvey check, this is a single source.

**★ THE RESIDUE, filed as R-109: `Volozhin, published 1824` is in the imprint slot, and the imprint
is Vilna.** The *editio princeps* is **Vilna (with Grodno), 1824**, brought to press by the author's
son R. Yitzchak and his nephew R. Avraham Simcha of Mstsislaw. Volozhin is where Chaim *lived* — he
is named "Chaim of Volozhin" two paragraphs above. In the slot `Title, locus. Place, year,
translation.`, a bare toponym reads as place of publication, and under that reading it is false.
**This is R-108's general form one notch over: two different facts — an author's toponym and a place
of imprint — collapsed into one string that reads as a single correct citation.**

---

## §4 — THE RESULT THAT MATTERS, AND IT IS NOT THE TEN

**10 exposed loci / 368 distinct cited works = 2.7%.**

That is not a book with few edition-bound citations. That is a book with **almost no citations at
all yet.** Books II–V carry **zero endnotes across 37 chapters**. They name their sources in the
sentence — Śaṅkara, the Zohar, Plotinus, Irenaeus, the *Brahma Sūtra*, *Nefesh HaChayim* — and give
no locus, so there is no pair for this sweep to inspect.

**The edition-sensitive material in this volume is concentrated in exactly the region with nothing
to check.** So:

> ⛔ **A CLEAN RESULT HERE IS A FALSE NEGATIVE BY CONSTRUCTION.**

This is the third time this project has caught the same shape and it should stop being a surprise:
**the instrument goes where the instrument is cheap.** The endnote retrofit (R-2) does not merely
*reveal* this population — it **creates** it, roughly ninety citations at once, every one of them
written by an author working fast against a source they have open. That is the exact condition
under which R-108's defect was produced in the first place.

**Therefore the sweep is not closed and cannot be.** It is now a **mandatory step inside R-2**,
re-run per book as each book's notes are written. That obligation is written in three places so it
cannot go silent: the row, the tool's docstring, and the tool's own printed LIMIT line.

---

## §5 — WHAT THIS SWEEP STILL CANNOT SEE

- **A citation phrased in a way the patterns miss.** One such hole was found *during* this run
  (§1.1) and there is no reason to believe it was the only one. The sweep's coverage of its own
  population is unmeasured — it cannot certify itself, and does not claim to.
- **Whether an unchecked locus in §2 is right.** The sweep locates; it does not adjudicate. Eight of
  the ten remain `◻`.
- **A wrong number in the right scheme.** That is R-30's family (span verification), not this one.
- **Anything in Book VIII**, which is not drafted.

---

*Clawd, Day 190 night. Instrument: `tools/edition_scheme_sweep.py`. Source for §3:
Sefaria API v3, `Nefesh_HaChayim, Gate III.4`, version "The Soul of Life, translated by Leonard
Moskowitz, Teaneck, NJ 2012 [Rev. 1.5]", CC-BY-NC; imprint confirmed against dealer catalogues of
the 1824 first edition.*
