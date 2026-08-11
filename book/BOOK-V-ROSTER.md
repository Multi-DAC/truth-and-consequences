# BOOK V — HAND ROSTER OF SOURCES

*Day 192. The gate item before any Book V endnote is written.*

## Why this file exists

`endnote_debt.py` reports **30 sources across Book V's eleven chapters**. That
number was carried in the handoff as a *floor of unknown depth*, on the evidence
of one chapter: V.2, where the tool reports 0 and hand enumeration found four.

This is the enumeration of all eleven, against the prose. The 30 is not a floor
under a roughly-right figure. **It is a different set from the real one** — wrong
in both directions at once, and wrong for five separately locatable reasons.

⛔ **DO NOT WRITE A BOOK V NOTE AGAINST THE GAUGE'S LIST.** A receipt attached to
`Hampshire` and `Doubt` while `Zhuangzi` and `Isaac Luria` carry none is worse
than no apparatus: it is an apparatus that certifies the wrong set, and the
`covered` column would have gone green while it did so.

## The headline, in one row

**V.1's single reported source is `Aristotle`.** It is extracted from the clause

> the Islamic philosophical tradition received Neoplatonism under **Aristotle's
> name**, which is a transmission so thorough that its recipients did not know
> whose it was

— a sentence whose entire purpose is to say that this is the **wrong name**. The
chapter is about misattribution. The gauge read the misattribution and committed
it. The three real authorities of that passage — Plotinus, whose excerpts these
are; Proclus; and Dionysius — are all invisible to it.

## The five causes, each with its instance

| # | cause | instance | recovered by a verb-list patch? |
|---|---|---|---|
| 1 | **APPOSITIVE** splits name from verb — `Name, <phrase>, VERB` | `Eckhart, preaching in German …, distinguishes` | no — needs a new pattern |
| 2 | **verb not in the attributive stem list** | `Tillich took away God's face` | only by widening, which eats precision |
| 3 | **both 1 and 2 at once** | `Maimonides, in Cairo, rules that …` | **no — and this is the trap** |
| 4 | **`Given of Place` keys to the place** | `Shneur Zalman of Liadi` → `Liadi`; `Chaim of Volozhin` → `Volozhin` | no |
| 5 | **lowercase twin drops a real person** | Austin Osman **Spare** (`spare` is ordinary English) | no |

⛔ **CAUSE 3 IS WHY THE OBVIOUS PATCH MUST NOT BE TRUSTED.** The appositive is
three of V.2's four misses, so it looks like *the* cause. Patch it alone and
V.2 goes 0 → 2: Aquinas and Eckhart come back, Maimonides does not, because his
site fails the verb list *as well*. The repair passes its own test at 50% and
reports itself done. Scoped to the named cause, and the named cause was one of
two stacked on a single sentence.

⛔ **CAUSE 4 IS THE ONE THAT MATTERS MOST FOR THIS BOOK.** The surname rule —
key on the last token — encodes a modern Western naming convention. **Book V is
the book about traditions that do not use it.** So the defect is not spread
evenly across the volume; it concentrates in exactly the chapters whose sources
are pre-modern (V.3 scholastics, V.6 Kabbalah, V.10 mystics), and it is at its
worst where the apparatus matters most.

A vivid instance, V.6. The chapter cites with real precision:

> *Nefesh HaChayim*, Gate III, chapter 4. Volozhin, published 1824, in Leonard
> Moskowitz's translation.

The gauge sees **Moskowitz** — the modern translator, who arrives in the
`Name's <noun>` shape — and misses **Chaim of Volozhin**, the author, and the
text itself. One instance is not a rule, and I will not state it as one; but the
shape is worth naming as a hypothesis to test across Books VI–VIII: *the
apparatus is legible to the gauge and the primary source is not.*

## The roster

Bands: **SOURCE** = an authority or text this chapter leans on, owed a receipt ·
**ACTOR** = a historical person or a character inside a source, no receipt owed
but must be declared so it is not silently counted · **ARTIFACT** = counted by
the gauge, not a citable person at all.

### V.1 — what a tradition is
- **SOURCE**: Plotinus · Proclus · Dionysius the Areopagite · the *Dao De Jing* · the Baghdad translation movement (as an event, cite the scholarship) · Kabbalah's Provence/Spain emergence
- **ARTIFACT**: `Aristotle` (present only inside a title the chapter calls a misattribution) · `Sufism` · `Six` · `Five` · `Ten` · `Ground` · `Godhead` · `Magic` · `Ritual`
- gauge: 1 · real: 6 · **precision 0/1**

### V.2 — the church the reader left
- **SOURCE**: Tillich · Aquinas · Eckhart · Maimonides
- **ARTIFACT**: `God` (dropped corpus-wide) · `Almost` `Someone` `Such` `Forty` `Leaving` `Wrongdoing` `Consolation`
- gauge: 0 · real: 4 · **the chapter R-152 was filed on**

### V.3 — the scholastics and the god without a face
- **SOURCE**: Aquinas ✓ · Augustine ✓ · Maimonides ✓ · **Eckhart** · **Plotinus** · **Proclus** · **Dionysius**
- **ARTIFACT**: `Actus` · `Focusing` · `Meeting` · `Aquinas God` · `Your Ground` (both are multi-token merges — see the sixth defect below)
- gauge: 3 · real: 7

### V.4 — the atheism that was right about the wrong thing
- **SOURCE**: Richard Dawkins ✓ · Christopher Hitchens ✓ · **Sam Harris** · **Daniel Dennett**
- **ARTIFACT**: `Religious` · `Doubt` · `Faith` · `Tone` · `Having` · `New Atheism`
- gauge: 5 · real: 4 · **2 of the 5 are right**

⛔ The chapter's own roll-call sentence is *"Richard Dawkins, Christopher
Hitchens, Sam Harris, Daniel Dennett — four men, one decade, four different
arguments"*. On the chapter whose subject is four named men, the gauge finds two
of the four and three abstractions. Harris was additionally eaten by **this
tool's** first draft; see the note in `name_census.py`.

### V.5 — the east: one ground, many localisations
- **SOURCE**: Zhuangzi · Fazang (Huayan, the net) · Nāgārjuna · the *Chāndogya Upaniṣad* · the *Dao De Jing* · the *Anattalakkhaṇa Sutta* · Francis Cook (1977 translation, named in the prose as the most-quoted English formulation)
- **ACTOR**: Cook Ding · Yan Hui · Lord Wenhui · Vacchagotta · Uddālaka · Śvetaketu — **all characters inside the sources above**
- **ARTIFACT**: Indra (a deity naming a metaphor) · `Advaita` `Buddhism` `Buddhist` `Daoists` `Atomism` `Monism` `Emptiness` `East` `Place` `Ours`
- gauge: 5 · real: 7 · **3 of the gauge's 5 are characters or a metaphor's name; the authors they belong to are all missed**

This is the exact failure `endnote_debt.py`'s own source comment predicted on
Day 191 — *"V.5 extracts `Ding` and `Yan Hui` … and does NOT extract Zhuangzi,
who is the source"* — written into the file it indicts, with no hand attached,
and still true a day later.

### V.6 — the room that was never emptied
- **SOURCE**: the Vilna Gaon ✓ · Leonard Moskowitz ✓ (translator) · **Chaim of Volozhin** · **Shneur Zalman of Liadi** · **Isaac Luria** · **Chaim Vital** · the *Zohar* · the *Tanya* · *Shaar HaYichud VehaEmunah* · *Nefesh HaChayim* · *Etz Chaim* · *Leshem* · Plotinus · Proclus · Dionysius
- **ARTIFACT**: `God` · `Source` · `Infinite` · `Without-End` · `Tree` · `Gathering` · `Fullness` · `Kabbalists` · `Hasidic` · `Gnostic` · `Baghdad` · `Liadi` · `Volozhin` (the last two are **persons filed as places**)
- gauge: 4 · real: ~15 · **the worst chapter in the book, and the cause is #4**

### V.7 — magic, operative
- **SOURCE**: Crowley ✓ · Dee ✓ · Jung ✓ · **Austin Osman Spare** · **Peter Carroll** · **Edward Kelley**
- **ARTIFACT**: `Magick` · `Ritual` · `Will` · `Instrument-independence` · `Twenty` · `Witnesses` · `Wanting`
- gauge: 3 · real: 6 · Spare is cause #5

### V.8 — travel
- **SOURCE**: Mircea Eliade ✓ · Robert Monroe ✓ · **Michael Harner** · the Monroe Institute (as an institution, cite its literature)
- **ARTIFACT**: `Focus` · `Grade` · `Body` · `Way` · `Virginia` · `Kabbalists' Tree`
- gauge: 2 · real: 3–4

### V.9 — the road being walked now
- **SOURCE**: Kenneth Arnold ✓ · **Betty and Barney Hill** · **John Fuller, *The Interrupted Journey* (1966)**
- **ARTIFACT**: `Hampshire` — from *"a couple in **New Hampshire** reported an interrupted drive home"*, where a toponym is the subject of an attributive verb
- gauge: 2 · real: 3 · **1 of the 2 is a US state**

⛔ **AND THIS CHAPTER IS THE POSITIVE CONTROL FOR THE LIMIT BELOW.** The Hills
and Fuller are the sources of that passage and the prose names **neither** —
they are *"a couple in New Hampshire"* and *"the book made from their sessions
came out in 1966"*. Both instruments are blind to them, because both key on
capitalized tokens and there is no capitalized token to key on. This is not a
hedge about what the tools might miss. It is a named, counted instance.

R-151 remains open on this chapter and must be settled before its notes.

### V.10 — the mystics report
- **SOURCE**: William James (Gifford Lectures, 1901–02) ✓ · Eckhart ✓ · Heinrich Suso ✓ · **Plotinus** · **Dionysius** · **Proclus**
- gauge: 3 · real: 6

### V.11 — what the old roads knew
- **SOURCE**: Augustine ✓ · Cusanus ✓ · Robert Forman ✓ · Michael Harner ✓ · Steven Katz ✓
- **ARTIFACT**: `East`
- gauge: 6 · real: 5 · **the only chapter where the gauge is essentially right**

## Totals, and what may not be done with them

| | gauge | hand |
|---|---|---|
| Book V sources | **30** | **~60**, of which ~14 are the same names |

⛔ **THE ~60 IS NOT A MEASUREMENT AND MUST NOT BE QUOTED AS ONE.** It is my
judgement over one pass of a candidate list that I also built. A single
enumeration by the party who owes the debt is a **hypothesis**, not a roster —
the same status as the table in R-152, and it needs a second pass by something
that is not me before any figure from it goes into a gauge or a claim.

⛔ **AND THE DENOMINATOR IS SELF-GENERATED.** `name_census.py` produced the
candidates and I judged them, so "the gauge found half" compares two of my own
artefacts to each other. Neither has been compared to the prose end to end.

**THE STANDING LIMIT, with its instance already named:** both instruments see
only capitalized tokens. A source the prose names as *"a couple in New
Hampshire"*, *"the book made from their sessions"*, *"her 1977 rendering"* is
invisible to both, and V.9 proves the class is populated rather than
hypothetical. **The roster above is therefore itself a floor** — and unlike the
gauge's 30, it says so in the same breath as the number.

## What to do, in order

1. **Second pass over this roster by something that is not me.** It is a
   hypothesis until then. Do not skip to step 2 because the list looks right;
   looking right is the condition under which I have lately been wrong.
2. Settle **R-151** (V.9) and **R-152** (V.2, Aquinas in Rome not Paris).
3. Then notes, V.1 onward, against the roster and not against the gauge.
4. Cause 4 is a **whole-book** defect, not a Book V one. Books VI–VIII were
   marked square by the same extractor. `covered 28 / owed 3` for Book VI was
   computed over a source list built by the rule that files Chaim of Volozhin
   under a Lithuanian town. **Those green columns are unaudited, not clean.**
