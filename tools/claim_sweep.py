#!/usr/bin/env python3
"""claim_sweep.py — the mechanical half of the claims register (07-THE-CLAIMS-REGISTER.md).

WHY THIS EXISTS. `05-THE-LEXICON.md` retired five words on stated arguments. The
retirements were recorded in three files and enforced in none, and on Day 186 two of them
were still in live use inside `00-ARCHITECTURE.md`'s own macro-structure — the file that
records the retirement. Two more survived as chapter titles in `06`. Nothing was watching,
because the ruling was a stamp and not a gauge. This is the gauge.

WHAT IT IS, EXACTLY. A pattern list with a mention/use classifier. It catches the careless
instance — the retired word that slid back in during a revision, the "ultimately" that
smuggles Trap 5, the participle that hands the Ground a motive. It does NOT understand the
sentences. A determined author defeats it trivially and a subtle breach walks straight
past it. It is a seatbelt against our own carelessness at 3am, not a proof of doctrinal
coherence. The register's numbered claims are the doctrine; this only reports lines.

THE MENTION/USE PROBLEM. The planning documents discuss the banned vocabulary constantly —
that is their job. A sweep that flagged every occurrence would be pure noise and would be
switched off within a week, which is the real failure mode of a checker. So each hit is
classified: a line carrying a meta-marker (RETIRE, banned, not-list, quoted correction) is
a MENTION and is suppressed with a count; everything else is a USE and is reported. The
classifier is a heuristic and it WILL have false negatives. Read the hits.

PROSE VS PLANNING. Some rules only make sense against book prose (the self-reference ban,
the manifestation vocabulary). Planning files are swept with the structural rules only.
Book prose is anything under --prose (default: book/). There is no prose yet; the rules are
written now so the first draft is swept by a tool that predates it.

USAGE
    python tools/claim_sweep.py                 # sweep the repo
    python tools/claim_sweep.py --prose book/   # add the prose-only rules over book/
    python tools/claim_sweep.py --show-mentions # show what was suppressed, to audit the filter

EXIT CODE: 1 if any USE-class violation is found, else 0.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent

# A line matching any of these is talking ABOUT the word, not using it.
MENTION_MARKERS = re.compile(
    r"RETIRE|retir\w+|\bBAN\b|banned|not-list|not the map|"
    r"⚠|Corrected|correction|DEMOTE|violation|CANONICAL|Trap \d|tells:|smuggle\w*|"
    r"says:|brief says|\bquoted\b|retitl\w+|→|superseded|"
    r"^\s*\|",  # a table row in these files is nearly always a register of terms
    re.IGNORECASE,
)

# ⚠ HEADINGS ARE NOT MENTIONS. An earlier version of this file suppressed any line
# starting with '#', on the theory that headings are structural. Two of the five
# violations found on Day 186 were CHAPTER TITLES (06's III.3 and VII.7) and the filter
# hid both. A title is the most expensive place a retired term can survive, because it
# propagates into every cross-reference written after it. Never suppress a heading.

# In a planning document a blockquote is nearly always a citation of somebody else's
# words — including our own retired ones. In book prose it is content. Scoped, not global.
PLANNING_MENTION = re.compile(r"^\s*>")

# ---------------------------------------------------------------------------
# RULES. (id, scope, pattern, licensed_pattern_or_None, what it smuggles)
#
#   scope "all"      — every file, including the planning documents. ONLY the retired
#                      terms belong here: a planning doc that describes the book should
#                      use the book's ruled vocabulary. This is the scope that produced
#                      the Day-186 finding.
#   scope "scaffold" — book prose AND 06-THE-SCAFFOLD.md. For doctrinal tells that a
#                      chapter beat can leak (00's queue item 8 is exactly this sweep).
#   scope "prose"    — book prose only.
#
#   Doctrinal tells are NOT scope "all", and the reason is the checker's own failure mode:
#   the planning documents' whole job is to discuss merge/union/hide-and-seek/softeners,
#   so sweeping them there produced 58 hits of pure noise on the first run — and a checker
#   that cries wolf is switched off within a week, which is worse than not having one.
#
#   `licensed` is a per-rule exemption for uses that are correct. Kept narrow and explicit,
#   because a broad exemption is how a gauge quietly stops measuring.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# CASE-SENSITIVE RULES — Day 187.
#
# Every rule is compiled with re.IGNORECASE by default, and that is right for a rule whose
# needle is a WORD (`narrowing`, `bottleneck`, `merge`): the reader meets those in any case,
# and a heading is the most expensive place one can survive.
#
# It is wrong for a rule whose needle is a TITLE — a proper name that happens to be spelled
# out of common words. `the Fullness` is a term; `the fullness of God` is English. Matching
# the second to catch the first does not make the gauge stricter, it makes it noisier, and a
# gauge that cries wolf is switched off within a week — this file's own docstring says so.
#
# ⚠ MIXED RULES CANNOT USE THIS SET, AND PROSE/self-reference IS ONE. Its pattern carries
# title needles (`DoPI`, `the Anchor`, `The Inside View`) *and* phrase needles (`as we argued
# elsewhere`), and the phrase needles must stay case-insensitive. The owed fix is to SPLIT it
# into `-title` and `-phrase` rules. Filed, not done today: it is a second behaviour change on
# a day that already has one, and the Day-187 lesson is that the run which changes three
# matchers at once is the run nobody reviews.
# ---------------------------------------------------------------------------
CASE_SENSITIVE_RULES = {"TERM/fullness"}

# Rules whose `licensed` field is a REQUIRED COMPANION, not an exception. For these the
# guard is evaluated against the whole paragraph, because the manuscript hard-wraps at
# ~100 chars and "the gloss is not on this line" is not the finding — "the gloss is not
# anywhere near it" is. Ruling 44. Keep this set small: a paragraph-wide guard suppresses
# more than a line-wide one, and quiet over-suppression is how a gauge stops measuring.
PARA_LICENSED_RULES = {"TERM/awareness-unglossed"}

RULES = [
    # --- retired terms (05 §3) -------------------------------------------------
    ("TERM/substrate", "all", r"\bsubstrates?\b",
     r"substrate[- ]independen|no substrate|beneath\W{0,3}the render|"
     r"simulation hypothesis|\bIIT\b|Bostrom|the field finds|in the wrong (?:one|place)",
     "05 §3a — Bostrom's word for the hardware, and a bare synonym for the Ground. "
     "Permitted exactly once, in the sentence that denies it. Breaches C5. "
     "LICENSED: 'substrate-independence', the standard name of a position in philosophy of "
     "mind that IV.6 must engage — refusing to name an opponent's term is worse than using it "
     "(00, ruling 9 corollary; recorded Day 186 when this sweep surfaced it)."),
    ("TERM/map", "all", r"\bthe map\b|\ba complete map\b|\bcomplete map\b|\bTHE MAP\b",
     r"map is not the territory|chapter[- ]map|map it out|map out|the map is done|"
     r"state-space map|settledness-map|knowing the map",
     "05 §3b — imports representation-OF, and collides with Korzybski in Book VI. "
     "Breaches C5. LICENSED: Korzybski's model-sense, and our own planning-process sense."),
    # ★★ TERM/map-self — ADDED DAY 189, AND IT EXISTS BECAUSE RULING 126'S OWN CASE WOULD NOT
    # HAVE BEEN CAUGHT BY THE RULE RULING 126 CITED.
    # Ruling 126 struck IV.1's beat 1 — *"mapped as far as an atlas can map its own blindness"* —
    # on the grounds that `map` is banned by `05` §3b "for our own instrument, the one word Book IV
    # may not use for the thing it is." TERM/map above matches THE NOUN: `the map`, `complete map`.
    # The beat used THE VERB. So the defect was found by hand, recorded as a gauge finding, and the
    # gauge could not have found it — which nobody noticed for a day, because a rule that fires on
    # a DIFFERENT case still reads as a working rule.
    # ⚠ THE BLANKET VERB BAN IS REFUSED BY MEASUREMENT, NOT BY TASTE: `\b(maps?|mapped|mapping)\b`
    # hits 127 lines repo-wide, nearly all of them legitimate — Korzybski in II.5, the card that
    # maps frameworks in IV.1, the territory you cannot map in IV.1:231. A rule with that yield is
    # a rule nobody reads. So the pattern is scoped to the verb WITH OUR OWN INSTRUMENT AS ITS
    # APPARENT SUBJECT, which takes it to 3 hits repo-wide.
    # ⚠⚠ AND ONE OF THOSE THREE IS A FALSE POSITIVE, DECLARED HERE RATHER THAN ENGINEERED AWAY:
    # IV.8:181 reads "the inherited material this atlas draws on calls it a structure that maps",
    # where the grammatical subject of *maps* is `a structure` and `this atlas` is two clauses
    # upstream. Proximity cannot see grammar. It is exempted BY NAME below, with that reason, so
    # the limit of the instrument is on the record instead of hidden inside a cleverer regex —
    # ruling 38's principle, applied to a rule rather than to a threshold.
    ("TERM/map-self", "scaffold",
     r"\b(?:this\s+)?(?:atlas|census)\b[^.;:!?]{0,40}?\b(?:maps?|mapped|mapping)\b"
     r"|\b(?:maps?|mapped|mapping)\b[^.;:!?]{0,25}?\b(?:this\s+atlas|this\s+census)\b",
     r"map is not the territory|map it out|map out",
     "05 §3b, as read by RULING 126 — the VERB, applied to our own instrument. Book IV is an "
     "ATLAS and may not describe itself as mapping. TERM/map catches the noun only; this is the "
     "half that struck IV.1's beat 1 and had no detector behind it until Day 189."),
    # ⚠⚠ Day 187 — THE COMMENT THAT USED TO SIT HERE WAS FALSE OF THE CODE BELOW IT, and it
    # prescribed a fix that was already in force. It read: *"These patterns are case-SENSITIVE,
    # so `THE NARROWING` in a heading walked straight past this rule… The real fix is
    # re.IGNORECASE on the TERM/* family. Not done tonight."* Every rule in this file has been
    # compiled with `re.IGNORECASE` at the point of use (see `sweep_file`) the whole time.
    # Measured, not read: `## THE NARROWING` matches today, and so does `the narrowing`.
    #   The two fossils it left behind are still visible above and below — the hand-added
    # `\bNARROWING\b` here and `\bTHE MAP\b` in TERM/map are DEAD alternations, unreachable
    # under IGNORECASE. They are kept rather than deleted: they are the evidence, and deleting
    # them would matter the day one of these rules is made case-sensitive.
    #   ★ The live cost is the OPPOSITE hole from the one the comment feared. A rule whose
    # needle is a TITLE (`the Fullness`, `the Anchor`) fires on the ordinary common noun.
    # `claim_sweep` filed exactly this on Day 187 (`the anchor` → `\bthe Anchor\b`) and declined
    # to fix it; it recurred the next chapter, in TERM/fullness, on Paul's *plērōma*.
    # ★★ THE PROPERTY BELONGS TO THE NEEDLE, NOT TO THE RULE — which is why it keeps recurring:
    # the rule tuple has nowhere to say which kind a needle is, so the knowledge went into a
    # comment and a hand-patched alternation instead, and the comment then rotted. See
    # CASE_SENSITIVE_RULES below, and the MIXED-rule note on PROSE/self-reference.
    ("TERM/narrowing", "all", r"\bnarrowings?\b|\bnarrowed\b|\bthe Narrowing\b|\bNARROWING\b",
     r"\bnarrower\b|\bnarrowly\b|kept narrow|no narrower",
     "05 §3a — RETIRED by ruling 13 (Day 186). The term is **the Focusing**: focusing is "
     "specification of something diffuse, and a lens destroys no light. *Narrowing* is the one "
     "term that failed the CONNOTATION screen rather than the collision screen — it prosecutes for "
     "Trap 1 (*it was a fall*) and Trap 5 (*it is to be undone*) before the argument starts, which "
     "is the reading the book exists to refuse. LICENSED: the comparative *narrower* and adverbial "
     "*narrowly* in their plain-English senses — C19's `no wider, and no narrower` is doctrine and "
     "must survive. NOT licensed by this rule, and correctly so: quoted contest material in "
     "`prose/SPECIMENS.md`, which is suppressed as a MENTION by the blockquote and ⚠ markers and "
     "must NEVER be exempted by widening the pattern above."),
    ("TERM/egregore", "all", r"\begregor(?:e|es|ic|ial)\b|\bEGREGORE\b", None,
     "05 §3a — RULING 109 (Day 188), at IV.5. BANNED as a term; the tradition is CREDITED once, in "
     "IV.5, with its lineage (nineteenth-century French occultism ← the ἐγρήγοροι of *1 Enoch* ← the "
     "ceremonial orders). Axis 1 finds a real owner and axis 3 a real polysemy, but **the killing "
     "axis is 2, and it is ruling 30's criterion re-run without amendment: an analogy has to be "
     "made of something the reader already has.** *Collapse* has a civilian life and kept its word; "
     "*superposition* had none and was banned; *egregore* has none either — nobody has ever used it "
     "about the traffic, or a marriage, or a firm — so borrowing it transfers AUTHORITY rather than "
     "MEANING, which is the exact transaction §3c exists to refuse. The book's words are the plain "
     "ones: **a movement, a company, a country.** LICENSED: the single credit-and-refusal passage "
     "in IV.5, exempted by pair below. ⚠ Wired the same day it was ruled, because a lexicon ruling "
     "with no gauge behind it survives its own retirement — `the map` proved it in two live chapter "
     "titles and `magic circle` proved it as an un-carried-out INSTRUCTION (ruling 101)."),
    ("TERM/fullness", "book-after-one", r"\bthe Fullness\b|\bthe still\b", None,
     "05 §3a — RULING 14 (Day 187). *The Fullness* and *the still* are Book I's mythic names for "
     "the Ground, and they are RETIRED at the I/II boundary. I.6's closing move — 'they will not "
     "hold' — makes the supersession deliberate, and a deliberate supersession leaks the moment a "
     "later book reaches back for the old name for variety. Axis 3, POLYSEMY: not a collision "
     "(nobody else owns it) and not a gradient (the word is not ominous) — our own two names for "
     "one referent, which is the defect the lexicon's collision-only column could never see. "
     "SCOPE: drafted chapters after Book I. The registers may discuss the terms freely; the "
     "prose may not use them. The term is **the Ground**."),
    # ⚠ THIS RULE HAS A NEGATIVE GUARD (4th field) — it fires on the term only when the
    # neutrality is ABSENT from the same paragraph. Ruling 44, and it is the first rule
    # here whose finding is an OMISSION rather than a presence. A pattern list cannot see
    # a missing sentence; a pattern plus a required-companion can.
    ("TERM/awareness-unglossed", "chapters-not-II-01",
     r"made of awareness", r"neither mind nor matter|pre-split|prior to the split|"
     r"before the split|neither solely mind|not idealism|Nishida",
     "05 §7, SECOND AMENDMENT (Day 187). The four-clause definition of the Ground ends "
     "on *made of awareness*, and that is the excerptable sentence — quoted alone it "
     "hands the reader idealism, which is C24's expensive trap and the entire reason "
     "`substrate` was retired. INSIDE II.1 the gloss is deliberately 2,000 words "
     "downstream: the misreading cannot be answered until the first three clauses stand, "
     "and a disclaimer in sentence one is words rather than an argument. OUTSIDE II.1 "
     "there is no chapter to carry it and the neutrality must be in the same paragraph. "
     "Any Book V restatement, any chapter opening reaching back for the definition, any "
     "jacket copy."),
    ("TERM/pre-rendered", "all", r"pre-render\w*|prerender\w*", None,
     "RULING 65 (Day 187). RETIRED as a doctrinal phrase. Two independent faults, and the "
     "second is the one nobody saw for two days. (1) TENSE: *pre-* is priority, and priority is "
     "a position in time — III.1's entire cut. C1's stated trap is the past tense, 'in a word "
     "nobody notices'; this is that word, in a prefix, in a chapter title. (2) THE METAPHOR'S OWN "
     "VOCABULARY: in games *pre-rendered* is the ANTONYM of generated-at-contact — baked by a "
     "studio, stored as assets, played back. Authorship, medium and playback, which is the server "
     "picture II.1 retired, and a flat contradiction of III.4's thesis four chapters later. "
     "The doctrine sentence is `01` §262's, which was already right: **every possible state, "
     "complete, at once. Nothing is authored.** NO LICENSED USE — mentions of the retired form "
     "are suppressed by the ⚠/retitled markers or exempted by name below."),
    ("TERM/stream", "book-after-one", r"\bstreams?\b|\bstreaming\b|\bstreamed\b",
     r"\bnot streamed\b|\bno stream\b|\bnothing is streamed\b",
     "RULING 70 (Day 187), AXIS 3 — our own abolished noun, run on a word the SCAFFOLD handed "
     "III.4. `stream` is the source volume's defined term and is NOT one here: it occurs once in "
     "the drafted book, in I.3, inside its own negation — *There is no stream.* Ruling 28 caught "
     "the same import in `Coherence`'s definition. The scaffold's III.4 beat says *not stored, not "
     "fetched, not streamed*, and the VERB is the delivery sense — a different word in the "
     "reader's ear, which is exactly why it walks past a collision screen. The hazard is FORWARD, "
     "not local: a later drafter who meets `streamed` on a Book III page reads the noun as "
     "available again, and that is precisely how *the map* survived its own retirement into two "
     "live chapter titles. LICENSED: the denial itself, which is the only construction it may "
     "ever appear in. SCOPE excludes Book I, where the abolition is made. NOT licensed and "
     "correctly so: `upstream`/`downstream`, which carry no word boundary before `stream` and "
     "never match — checked, not assumed."),
    ("TERM/aperture", "all", r"\bapertures?\b", None,
     "05 §3 — demoted; the term is the Perspective."),
    ("TERM/bottleneck", "all", r"\bbottlenecks?\b", None,
     "05 §3 — demoted; the term is the Perspective."),

    # --- Trap 5 / C15: union as the destination --------------------------------
    ("C15/trap5", "scaffold",
     r"\bmerges?\b|\bmerging\b|\bultimately\b|\bunion\b|\bunify\b|\bunification\b",
     r"not union|no union|nothing to merge|part from|refuse|neither dissolution|"
     r"union-telos|error|failure",
     "Trap 5 tells (01, §10). There is nothing to merge into. The one trap that cannot be "
     "fixed late — it springs in Book V, ten chapters after its only guard. (00 queue item 8.)"),
    ("C15/temporary", "scaffold",
     r"narrowing is (?:only |merely |just )?temporar|temporary narrowing", None,
     "Trap 5 in its subtlest form: the narrowing described as a phase to be exited."),

    # --- C3: the scope rule. The breach is in participles, never in main verbs.
    ("C3/motive", "scaffold",
     r"the Ground[,\s][^.]{0,40}\b(?:seek|seeks|seeking|want|wants|wanting|need|needs|needing|"
     r"lack|lacks|lacking|gain|gains|gaining|chose|chooses|choosing|desire|desires|yearn|yearns)\b",
     r"does not|cannot|never|no motive|not because",
     "C3 — the Ground does not want, lack, fall or intend. Breaches arrive in participles and "
     "possessives, not in main verbs."),
    ("C3/purpose", "scaffold",
     r"the Ground[^.]{0,60}\bin order to\b|\bin order to\b[^.]{0,60}the Ground",
     r"which hands|reads as|would hand|error",
     "C2/C3 — 'in order to' hands the Ground a purpose in the same sentence that denies it one."),

    # --- C7: reactivity IS awareness. Any softener demotes all of Part Two. ----
    ("C7/softener", "scaffold",
     r"(?:reactivity|reactive|awareness|aware)[^.]{0,50}\b(?:may be|might be|in some sense|"
     r"a kind of|something like|arguably|perhaps|seems to|appears to|correlates? with|gives rise to)\b",
     r"not \"|not '|never |Not \*",
     "C7 — 'is', not 'correlates with' or 'gives rise to'. One hedge retroactively converts "
     "every consequence in Part Two into a speculation."),

    # --- C6/C9: the God-player, which deletes C9 while sounding affirming -----
    ("C6/godplayer", "prose",
     r"God (?:is )?play|playing at being|God in a mask|wearing every (?:face|mask)|"
     r"hide[- ]and[- ]seek|divine play", None,
     "C6 — the Ground cannot play. Watts's picture arrives wearing warmth, which is why Trap 3's "
     "usual detectors miss it. NOTE: legitimate where the cut is being MADE — I.6 b4 (the early "
     "guard), III.2 (the full argument, Day 187: the site of record), III.5, VIII.6. "
     "⚠ III.5 WAS MISSING FROM THIS LIST UNTIL DAY 187 AND THE OMISSION WAS THE GAUGE'S, NOT THE "
     "PROSE'S. C9's register entry has always required the mask to be named at III.5 — *it must be "
     "named at III.5 too, because that is where the reader first has the thought* — so the gauge's "
     "licensed-site list contradicted the claims register for as long as both existed, and the "
     "contradiction was invisible because III.5 was undrafted. A licence list that is only checked "
     "against the chapters already written is a list that ages into a false positive on schedule."),

    # --- prose-only ------------------------------------------------------------
    ("PROSE/self-reference", "prose",
     r"\bDoPI\b|Corpus[- ]Perspectival|\bthe Anchor\b|Coherent Structure|The Inside View|"
     r"\bin (?:our|the) (?:previous|earlier|prior) (?:work|volume|book)|as we (?:argued|showed|"
     r"have argued|have shown) (?:elsewhere|previously|earlier)|\bour earlier work\b", None,
     "Clayton, Day 186: no past work of ours is referred to by name. AND the anonymous form is "
     "worse — it points at something the reader cannot even look up. See 00, ruling 8."),
    ("PROSE/self-metric", "prose",
     r"\bour (?:own )?(?:corpus|archive|shelf|research notes)\b|"
     r"\b(?:this book's|the) corpus\b|\bcorpus (?:does|doesn't|does not|knows) \b|"
     r"\bfiles\b|\b(?:million|thousand) words\b", None,
     "RULING 113 (Day 188, Fable + one more found by this rule). ★ THE SECOND SPECIES OF "
     "RULING-8 BREACH, and the reason PROSE/self-reference read clean over all three instances "
     "for two months: that rule hunts RHETORICAL self-reference — *as we argued elsewhere* — and "
     "enumerates IDIOMS. This species is METRICAL. II.3 shipped three: *absent from three million "
     "words of our own corpus*, *a name our corpus does know, in ninety-five files*, and *he is "
     "not in this book's corpus once*. None of them gestures at an argument. Each is a READOUT "
     "FROM OUR OWN INSTRUMENT — `tools/ancestor_gap.py` prints a per-name corpus file-count, and "
     "its output walked onto the page as a rhetorical move. **The units are the tell.** A word "
     "count and a FILE count are quantities no reader has, can obtain, or can check, which is "
     "ruling 8(c)'s own criterion for why the anonymous form is worse than the named one — met "
     "exactly, by the rule written to enforce it, and missed. ⚠ *this book's corpus* is the "
     "worst-disguised: it wears the book's name, and a book has no corpus. The SHELF has one."),
    ("PROSE/manifestation", "prose",
     r"\bmanifest(?:ing|ation|s)?\b|\battract(?:ing|ion)? (?:abundance|wealth|what you)|"
     r"\bcreate your (?:own )?reality\b|\bthe universe (?:wants|gives|provides|responds)\b", None,
     "C12 — editable ≠ the world obeys your wanting. The edit is to the filter; by C10 the render "
     "is not solely yours. The claim most likely to be quoted back at us out of context."),
    ("PROSE/hedge", "prose",
     r"\bit could be argued\b|\bone might say\b|\bwe would suggest\b|\bit seems plausible\b|"
     r"\bto some extent\b|\barguably\b|\bin a sense\b|〔(?:established|suggestive|framework-permitted|cut)〕",
     None,
     "The register rule. The four epistemic tags are off the page and the hedging register with "
     "them. Ground in evidence, ground in reasoning, or cut it."),
    # RULING 39 (Day 187, Fable). THE THIRD HOME OF THE HEDGES. Ruling 9 took the four
    # epistemic tags off the page and predicted displacement; it named two destinations,
    # footnote and coda, and closed both. It missed the one the hedges actually took:
    # **the sentence that asserts its own non-hedging.** Six instances shipped, across
    # five of Book II's eight chapters, while PROSE/hedge above read clean — because
    # PROSE/hedge hunts hedge VOCABULARY and this form contains none. It is the style
    # contract's already-banned move (*the clause that exists to pre-empt an objection*)
    # aimed at the book itself.
    #
    # THE DISCRIMINATOR IS THE SUBJECT, and it has to be, or the rule eats good prose.
    # "Completeness is not a mood the Fullness is in" (I.1), "He was not hedging" (II.3,
    # of Nishida), "the wrongness you have felt ... is not a mood" (II.8, of the reader)
    # are all the same grammar and none of them are the defect. The defect is when the
    # subject is OUR OWN ACT — the refusal, saying so, the retirement, this book.
    #
    # THE REMEDY IS ALWAYS DELETION, and that is the tell for the whole class: the clause
    # sits next to the reason it is trying to substitute for. Cut it and the reason is
    # still standing. All six cut this way; not one needed a replacement argument.
    ("PROSE/antihedge", "prose",
     r"(?:the refusal|refusing it|refusing them|the declining|declining it|saying so|"
     r"admitting it|admitting so|the retirement|the ban|the whole list|the roster|"
     r"the restraint|the deferral|the omission|the reservation|the exception|the caveat|"
     r"the qualification|the silence|this chapter|this book)"
     r"[^.;:!?]{0,50}?(?:is|are|reads|sounds|looks)\s+not\s+(?:a |an |the )?"
     r"(?:soften\w*|caveats?|hedg\w*|throat.clearing|housekeeping|retreat|apolog\w*|"
     r"disclaimers?|equivocation|evasion|nerves?|timidity|cowardice|posture|excuses?|"
     r"cop.out|climb.down|padding|pedantry|fussiness|bookkeeping)"
     r"|(?:declines?|refuses?|withholds?|defers?)[^.;:!?]{0,40}?"
     r"rather than (?:out of |from )?(?:nerves?|fear|timidity|cowardice|caution|"
     r"politeness|modesty|hedging|throat.clearing)"
     r"|(?:or|lest)[^.;:!?]{0,60}?(?:reads?|sounds?|looks?) (?:as|like) (?:a )?"
     r"(?:retreat|climb.down|hedge|apology|cop.out|evasion)", None,
     "Ruling 39 — the hedges' third home: the sentence that asserts its own non-hedging. "
     "The style contract already bans the clause that exists to pre-empt an objection; this "
     "is that clause pointed at the book. Delete it — the reason it stands next to is the "
     "argument, and it survives the cut alone."),
    ("PROSE/outlist", "prose",
     r"Timewave|Novelty Theory|eight[- ]circuit|Terror Management|Stoned Ape", None,
     "00's out-list — out because we do not hold them, not because a skeptic would object."),
]

# ---------------------------------------------------------------------------
# DELIBERATE EXEMPTIONS — named lines, not a widened pattern.
#
# A retired term sometimes has to stay on a page: a quotation is evidence, and a
# quotation tidied into the current vocabulary stops being a record of what was said.
# The tempting fix is to widen a rule's `licensed` regex until the hits go away. That
# is invisible, it grows, and it is how a gauge quietly stops measuring — the failure
# this file's docstring already names once.
#
# So: exemptions are ENUMERATED, each with a reason, and **printed at every run whether
# or not anything else fires.** A suppression nobody can see is a suppression nobody
# audits. If this list is long, that is a finding about the manuscript, not about the tool.
#
#   (path suffix, rule_id, substring that must be on the line — None means whole file, why)
# ---------------------------------------------------------------------------
EXEMPTIONS = [
    ("book/IV-08-the-divine-and-the-hierarchies.md", "TERM/map-self",
     "a structure that maps",
     "THE DECLARED FALSE POSITIVE OF TERM/map-self, and it is exempted rather than regexed "
     "away. The subject of *maps* is `a structure` — an inherited depiction — and `this atlas` "
     "sits two clauses upstream as the possessor of `the inherited material`. A proximity "
     "pattern cannot see a grammatical subject, and the alternative was a cleverer regex fitted "
     "to this one line, which is how a rule stops measuring. The instrument reports its own "
     "resolution here instead. Ruling 38's principle; Day 189."),
    ("book/DRAFT-LOG.md", "TERM/map-self", "an atlas can map its own blindness",
     "A DATED RECORD RECORDS WHAT WAS TRUE WHEN IT WAS WRITTEN — ruling 126's own convention, "
     "verbatim, applied to ruling 126's own entry. The log QUOTES the struck beat in order to "
     "strike it; a register that cannot quote the breach it ruled on cannot record the ruling. "
     "Named-line, not whole-file: any other TERM/map-self hit in the log is a fresh decision."),
    ("book/DRAFT-LOG.md", "PROSE/self-metric", None,
     "SCOPE, not licence — and the SECOND time this exact mistake has been made. Ruling 14's "
     "first-draft scope swept DRAFT-LOG for TERM/fullness and had to be narrowed; this rule was "
     "written four hours later and repeated it, firing 14 times on a register whose entire job is "
     "to record corpus file-counts. The log is where the readouts BELONG — DRAFT-LOG:1007 is the "
     "very line (*'95 files in the'*) that the II.3 sentence was written from, and deleting it "
     "would destroy the evidence for ruling 113. Whole-file for this rule ONLY."),
    ("book/III-01-the-wrong-game.md", "PROSE/self-metric", "Irenaeus files separately",
     "THE VERB, not the noun. `\\bfiles\\b` is deliberately unqualified because a book of "
     "metaphysics has no business naming a filesystem — the cost of that breadth is exactly one "
     "hit, and it is a heresiologist sorting schools. Enumerated rather than narrowed to "
     "`(?<!Irenaeus )files`, per the note above: widening the pattern is how the rule would stop "
     "measuring the thing it was written for."),
    ("prose/RULING-13-the-narrowing.md", "TERM/narrowing", None,
     "The ruling document FOR the retirement — the file whose entire subject is the word. "
     "Whole-file. One of two whole-file entries; see DRAFT-LOG below."),
    ("book/DRAFT-LOG.md", "PROSE/manifestation", None,
     "SCOPE, not licence. DRAFT-LOG.md is the log ABOUT the manuscript, not manuscript prose, and "
     "its whole function is to record which trap was guarded where — a log that cannot name a trap "
     "cannot record that the trap was guarded. Whole-file for this rule ONLY: any other rule firing "
     "in DRAFT-LOG.md is a fresh decision and gets its own line here, not a widening of this one. "
     "Added Day 187 when the I.5 entry named the manifestation slide in the act of pre-empting it."),
    ("00-ARCHITECTURE.md", "TERM/narrowing", "TERM/narrowing",
     "The ruling index naming the GAUGE's rule-id, not the term. A ruling list that cannot "
     "name what it retired is a ruling list that cannot be audited."),
    ("00-ARCHITECTURE.md", "TERM/narrowing", "13. THE NARROWING",
     "Same: the heading of ruling 13's index entry. Added when the case hole above was closed "
     "and this line started firing for the first time — which is the fix working."),
    ("04-THE-UNSATISFYING-ANSWERS.md", "TERM/substrate", "crediting substrates the field",
     "★ Day 187, ruling 25. The opponent-V entry QUOTING ITS OWN WITHDRAWN SENTENCE — the "
     "'epicyclic boundary work / stopped short to stay respectable' charge against Tononi, which "
     "the record refuted and which is kept inline with its fault named rather than deleted. The "
     "retired word is inside quoted superseded text of our own, which is the RULING-13 pattern: "
     "tidying it into current vocabulary would destroy the evidence for the correction. Own line, "
     "one needle, not a widening of the licensed 'substrate-independence' exception."),
    ("book/DRAFT-LOG.md", "TERM/bottleneck", "bottleneck geometry",
     "★ Day 187, II.3. The log quoting the Null-Space Theorem's RETRIEVED FORMAL STATEMENT, which "
     "uses the retired term — in the sentence whose entire point is that it does, and that this is "
     "why II.3's beat says 'in plain words'. Tidying the quotation into current vocabulary would "
     "destroy the evidence for the ruling it is evidence for. Own line, per the standing "
     "instruction on the DRAFT-LOG entry above; not a widening of it."),
    ("06-THE-SCAFFOLD.md", "TERM/bottleneck", "bottleneck point",
     "★ Day 189, ruling 155, V.6. THE SAME GROUND AS THE DRAFT-LOG ENTRY ABOVE, in `06` rather "
     "than the log: the scaffold quoting a RETRIEVED MEMORY verbatim — Clayton, 2026-06-27, "
     "'a precise prior of our bottleneck point' — because the retired word IS the finding. The "
     "beat had drifted that phrase to 'a precise prior statement of the Focusing', and the whole "
     "evidence for the drift is which noun the source actually used. Paraphrasing into current "
     "vocabulary would delete the ruling's only exhibit. Named line, not a whole-file scope on "
     "`06`: any other TERM/bottleneck hit in the scaffold is a fresh decision."),
    # --- Day 187: three fresh lines, per the standing instruction on the entry above.
    # Not a widening of it. All three are the log QUOTING the prose whose guard it records.
    ("book/DRAFT-LOG.md", "C15/trap5", "Dissolving, merging, the drop going back to the sea",
     "The I.6 entry quoting the Trap 5 vocabulary in the sentence that records its refusal. "
     "The quoted words are the trap; the surrounding line is the guard."),
    ("book/DRAFT-LOG.md", "C6/godplayer", "one player wearing every face",
     "The I.6 entry naming the Watts reading in the act of recording that I.6 refuses it."),
    ("book/DRAFT-LOG.md", "C3/motive", "will want it to be the thing doing all of that",
     "Day 187. The II.1 entry QUOTING the false-positive line in the act of recording that it is a "
     "false positive — the same shape as the three entries around it. Fresh line per the standing "
     "instruction on the whole-file DRAFT-LOG entry above, not a widening of it. ⚠ Note that the "
     "log's copy is UNWRAPPED where the manuscript's is wrapped, so this needle is longer than the "
     "II-01 one for the identical sentence; that asymmetry is the hard-wrap defect leaving a mark."),
    ("book/DRAFT-LOG.md", "C6/godplayer", "the theology that removes the divine player",
     "Quoting 01 §9 — the sentence that states our position AGAINST the god-player. "
     "The rule is firing on our own refutation."),
    ("prose/SPECIMENS.md", "TERM/narrowing", "all narrowings exist in all states",
     "Clayton's own C17 objection, in his wording. Ruling 13, Day 186."),
    ("prose/SPECIMENS.md", "TERM/narrowing", "If nesting made the narrowing illusory",
     "Quoted contest material — the resisted half of the C17 exchange, kept as evidence."),
    ("prose/SPECIMENS.md", "TERM/narrowing", "narrowing is, and that is the open question",
     "Same exchange, the sentence that named the VII.1 × VIII.6 question."),
    ("book/I-03-the-focusing.md", "TERM/narrowing", "and it will be *narrowing*",
     "★ THE ONE LICENSED USE IN THE MANUSCRIPT. Scaffold I.3 beat 4 requires the retired word to "
     "be NAMED once, on the page where the act is defined, so it can be refused — a retirement the "
     "reader never sees made is a retirement that leaves the reader holding the wrong word. Scoped "
     "to the single line that names it; the refusal below it never repeats the noun, by design, so "
     "this exemption cannot silently widen to cover a second use. If a second line in book/ ever "
     "needs this rule, that is a breach, not a missing entry."),

    # --- I.6, the chapter where two cuts are MADE. A cut has to name what it cuts. ---
    ("book/I-06-the-recognition.md", "C6/godplayer", "not one player wearing every face",
     "★ THE CUT ITSELF. C6's own rule text already says the God-player is legitimate where the cut "
     "is being made (I.6 b4, VIII.6); this is the line that makes it. Scoped to the refusal."),
    ("book/I-06-the-recognition.md", "C6/godplayer", "hide-and-seek with a single participant",
     "The warm picture stated in the reader's own terms so it can be refused in the next breath — "
     "the I.3 procedure for a retired word, applied to a retired cosmology. The cost paragraph "
     "beneath it (a mask is not anybody; the grief would be a misunderstanding about costume) is "
     "what this line exists to set up, and it is the only statement of the picture in the book "
     "outside Book V, where it is named and credited."),
    # --- Day 187, II.1: the first hit of a class the C3/motive rule text does not name. ---
    # ⚠ The needle below is SHORT ON PURPOSE. It was first written as the full clause
    # "will want it to be the thing doing all of that" and matched nothing, because the
    # manuscript is HARD-WRAPPED and the clause breaks across two physical lines. The
    # exemption matcher works line-by-line, exactly like the litany gauge that under-read
    # by 10% for the same reason on Day 187. Keep every needle inside one wrapped line.
    ("book/II-01-the-ground.md", "C3/motive", "will want it to be the thing",
     "★ FALSE POSITIVE, and the class is worth more than the line. **The wanter is the READER.** "
     "C3/motive is a proximity pattern — `the Ground` within 40 characters of a wanting verb — and "
     "it cannot see which noun is the grammatical subject. So it fires on a sentence that ASSERTS "
     "C3 by describing the reader's error, and by the same blindness it would miss a real breach "
     "phrased with the Ground more than 40 characters from its participle. **The exemption is the "
     "cheap half; the finding is that this rule over-reads on subject and under-reads on distance, "
     "and neither direction is visible from the hit list.** Recorded rather than reworded on "
     "purpose: rewording the prose would have made the tool look correct."),
    ("book/I-06-the-recognition.md", "C15/trap5", "in the drop going back to the sea",
     "★ TRAP 5's ONLY EARLY GUARD, and it cannot be made without naming the destination it refuses. "
     "01 §10 requires the refusal to be structural and stated in Book I's own last movement, ten "
     "chapters before the trap springs in Book V. The sentence after this one is the refusal: a "
     "destination with no perspective is the one condition in which nothing whatever is the case."),
    # NB: needles for CROSS-WRAP hits are matched against the joined window, so this one may
    # span a line break in the file. Needles for line-pass hits still must fit inside one.
    ("book/II-02-the-focusing-and-the-render.md", "PROSE/manifestation", "create your own reality",
     "★ THE OPPONENT'S OWN PHRASE, and ruling 16 requires it on the page — a chapter that cuts a "
     "position without quoting it is arguing with a strawman. The seed beat cuts BOTH ways and this "
     "is the first half; the sentence naming it is followed immediately by the credit and then by "
     "the break (`create` is the word that fails: authorship is the player wearing your face). "
     "**Two findings, and the exemption is the smaller one.** (a) This is the hit that exposed the "
     "cross-wrap hole — `create your own` / `reality` straddles a wrap, so the rule reported the "
     "chapter CLEAN. (b) Once seen, it turned out to be suppressed a SECOND time and for a reason "
     "unrelated to the phrase: MENTION_MARKERS carries `\\bquoted\\b` and the sentence happens to "
     "say 'quoted out of context'. Any manuscript sentence containing the word `quoted` is "
     "currently invisible to every prose rule. Recorded, not widened, and not reworded."),
    # --- Day 187, II.5. Two lines, one reason, and the reason is the rule's own licence.
    ("book/II-05-the-tunnel.md", "TERM/map", "the map has one, the territory",
     "★ KORZYBSKI'S MODEL-SENSE — the use this rule's own message already calls LICENSED, in the "
     "chapter whose assignment is to put the dictum beyond negotiation. The licensed regex covers "
     "the quotation itself (`map is not the territory`) and NOT the unpacking of its second clause, "
     "which is where II.5's entire argument lives. **The licence was declared in the rule text and "
     "implemented for one phrasing** — a smaller cousin of the week's standing lesson that a "
     "declared blind spot is not a checked one. Enumerated rather than widened: `\\bthe map\\b` is "
     "the whole rule, and any widening that admits this line admits the Ground-sense too."),
    ("book/II-05-the-tunnel.md", "TERM/map", "the map is good insofar as",
     "Same sentence, second line — the wrap falls mid-clause. Own entry, per the standing rule that "
     "an exemption is a named line and never a paragraph."),
    # --- Day 187, II.6. An exemption that PAYS DOWN an open queue item instead of buying silence.
    ("book/II-06-coherence.md", "C15/trap5", "Union is not the erasure of the parts",
     "★ A SECOND TRAP-5 GUARD, AND A BETTER ONE — arriving as a CONSEQUENCE rather than a caution. "
     "This rule's own message says Trap 5 'springs in Book V, ten chapters after its only guard' "
     "(`00` queue item 8): I.6's guard is a REFUSAL, and a refusal ten chapters back is exactly what "
     "a reader in Book V will not remember. II.6's separation condition supplies a REASON — union is "
     "not the erasure of the parts, because where the parts are erased there is one level left and "
     "one level cannot cohere with anything. Trap 5 is now foreclosed by the definition of the "
     "book's own core term rather than by a warning the reader has to carry. The rule fired on the "
     "vocabulary because the guard cannot be built without it, which is the same shape as I.6:70's "
     "exemption. → `00` queue item 8 is PART-PAID; it stays open for the Book V approach."),
    # --- Day 187, II.6. THE LOG RECORDING A RULE FIRING, FIRES THE RULE. Third occurrence of a
    # standing shape (already at DRAFT-LOG:588 and :830): an entry cannot record which line tripped
    # which rule without reproducing the line. Enumerated per hit, never scoped to the file — the
    # log is prose about the manuscript, but it is not exempt wholesale, or a real breach written
    # INTO the log would be the one place nothing looks.
    ("book/DRAFT-LOG.md", "C15/trap5", "fired **C15/trap5** on",
     "The II.6 entry naming the rule and quoting the line, in the sentence that records the "
     "adjudication. Recording a firing reproduces the firing."),
    ("book/DRAFT-LOG.md", "C15/trap5", "condition supplies a **reason**",
     "Same entry, the second half of the argument — the sentence that states WHY the guard needs "
     "the trap's vocabulary. Own entry, per the rule that an exemption is a named line."),
    # --- Day 187, II.8. THE ONE LINE IN THE MANUSCRIPT THAT USES A RETIRED TERM AFTER ITS
    # RETIREMENT, and it is the line that names who owned it first.
    ("book/II-08-the-return.md", "TERM/fullness", "the standard English for it is the Fullness",
     "★ THE COLLISION NAMED, ONCE, IN THE ONLY CHAPTER WITH STANDING TO NAME IT. `the Fullness` "
     "is the standard English for the Gnostic *pleroma* — Book I's name for the plenum is the "
     "opponent's own technical term for the thing you escape TO, in the book whose Trap 1 is "
     "Gnosticism. Ruling 14 screened this row on axis 3 (our own second name) and never on axis 1 "
     "(who else owns it), which is the inverse of the defect ruling 14 was written to correct. "
     "The Tillich precedent in `05` §3a governs and is quoted verbatim there: an unnamed borrowing "
     "from a famous source is what a hostile reader uses; a named one is a credential — and it is "
     "to be named AT THE DEFINITION. The definition is in Book I, where rule 5 forbids naming an "
     "opponent on the page, so the borrowing has no legal home at its own definition and II.8 is "
     "the first door: the only chapter that names Gnosticism at all. "
     "⚠ THE DEBT IS PART-PAID, NOT PAID. The reader meets the correction six chapters after the "
     "word, and a correction that late does not undo a first impression — it only stops the book "
     "looking ignorant to the reader who had *pleroma* before page one. Recorded rather than "
     "dressed up. → ruling 34; `05` §3a Fullness row, axis-1 column."),
    ("book/DRAFT-LOG.md", "PROSE/hedge", "The second hit was **PROSE/hedge**",
     "The II.6 entry quoting the hedge it REWORDED rather than exempted. The manuscript line is "
     "gone; this is the receipt for its removal, and a receipt has to name what it removed."),
    ("book/DRAFT-LOG.md", "PROSE/hedge", "inside the physicalism card",
     "Day 188, the IV.2 entry. Same shape as the II.6 receipt above and it gets its OWN line rather "
     "than widening that one: the IV.1 hedge — *arguably at a range within one grade* — is gone "
     "from the manuscript, rewritten to ground the variation in which physicalist you ask. The log "
     "quotes it because this is the receipt, and because IV.1 SHIPPED with it: the sweep was never "
     "run on that chapter, and a finding whose whole point is that a gauge went unread cannot be "
     "recorded in a form the gauge then objects to."),
    # --- Day 187, III.2. THREE lines, and they are the rule's own NOTE being cashed for the first
    #     time in Book III. C6/godplayer says the god-player is legitimate WHERE THE CUT IS MADE.
    #     I.6 makes the early guard; III.2 makes the argument, so III.2 is where the pattern MUST
    #     fire and must be exempted line by line. Three entries, not a whole-file scope: a chapter
    #     that cuts a claim is exactly the chapter where a real breach would be invisible.
    ("book/III-02-the-game-that-is-playing-you.md", "C6/godplayer",
     "God also likes to play hide-and-seek",
     "★ THE QUOTATION BEING CUT. Watts, *The Book* ch. 1, block-quoted at full strength so that the "
     "reader meets the warm picture in its author's own words before it is refused. C6's rule text "
     "already licenses this shape at I.6 b4; III.2 is the chapter that spends it."),
    ("book/III-02-the-game-that-is-playing-you.md", "C6/godplayer",
     "The demiurge and the divine Player have almost nothing in common",
     "★ THE CUT ITSELF, and the chapter's hinge: the two figures share a TENSE and nothing else. "
     "The pattern fires on 'divine Player' — which is the thing being killed in the sentence that "
     "kills it."),
    ("book/III-02-the-game-that-is-playing-you.md", "C6/godplayer",
     "If there is one player wearing every face",
     "THE COST, stated in the conditional. C6's own ⚠ says one God-player means every other person "
     "is a costume and C9 is deleted while appearing to be affirmed — this line is that consequence "
     "written out, antecedent-first, in order to refuse it. Same shape as the I.6:53 exemption: the "
     "warm picture stated in the reader's terms so it can be refused in the next breath."),
    # --- Day 187, III.5. THREE lines, the second cashing of the rule's NOTE, and the first one the
    #     NOTE did not already name — see the ⚠ appended to C6/godplayer above. C9's trap is the
    #     generous-sounding inversion, and the register requires it named HERE because III.5 is
    #     where the reader first has the thought. Line by line, not whole-file, for the III.2 reason:
    #     the chapter that refuses a claim is exactly where a real breach would read as the refusal.
    ("book/III-05-there-are-no-npcs.md", "C6/godplayer",
     "*Everyone is God in a mask.*",
     "★ THE TRAP STATED, in the reader's own words and at full warmth, so that it can be refused in "
     "the paragraphs under it. Same shape as I.6:53 and III.2's third entry. This is the line C9's "
     "register entry mandates and the one the rule's NOTE had not anticipated."),
    ("book/III-05-there-are-no-npcs.md", "C6/godplayer",
     "divine player was taken apart on his own merits",
     "THE CITATION OF THE CUT, not the cut again. III.2 is the site of record and this line says so "
     "— the pattern fires on 'divine player' inside a sentence whose whole content is that the "
     "argument was made two chapters ago and is not being made twice."),
    ("book/III-05-there-are-no-npcs.md", "C6/godplayer",
     "If there is one player wearing every face",
     "THE COST, in the conditional, second placement. The identical antecedent is exempted at "
     "III.2:109 — and the two are doing different work: III.2 draws the cost for C6 (the Ground "
     "cannot play), III.5 draws it for C9 (the person in front of you is not a position the one "
     "somebody is occupying). Two chapters, one sentence-shape, two claims. ⚠ A THIRD USE OF THIS "
     "ANTECEDENT IS A TIC, not a discipline — VIII.6 is the last licensed site and it should reach "
     "for a different form."),
    # --- Day 187, III.7. THE CITATION OF THE CUT, third occurrence — and the third is what makes
    #     it a pattern worth naming rather than a third one-off. III.5 already carries this exact
    #     shape ("divine player was taken apart on his own merits"). The rule's ⚠ predicted the
    #     recurrence and predicted the cause: the licensed-site list is hand-kept and only ever
    #     checked against chapters already drafted, so it ages into a false positive on schedule.
    #     ⚠ AND THE OBVIOUS CURE IS WRONG, which is why it is written down here instead of built.
    #     `07`'s C6 entry lists III.5 · III.7 · V.9 · V.10 · VII.2 · VII.6 · VIII.1 · VIII.6 under
    #     **Depends**, and deriving the licence list from that field would license nine chapters in
    #     one commit — the "broad exemption is how a gauge quietly stops measuring" failure, arrived
    #     at by automation. ESTABLISHES ≠ DEPENDS. A chapter that USES a settled claim is not
    #     thereby licensed to restate the figure the claim was cut out of; it is licensed to cite
    #     that the cut was made. That distinction is the exemption, and it has to be adjudicated
    #     per line, by a person, exactly as it was here.
    ("book/III-07-the-walking-is-real.md", "C6/godplayer",
     "game away from a divine player",
     "THE CITATION OF THE CUT, not the cut again — the III.5:'taken apart on his own merits' shape, "
     "in a subordinate clause whose entire function is to name where C6 was established (III.2) "
     "before cashing its three-part content in the main clause: not-knowing, stakes, duration. The "
     "figure appears in the past tense, as the thing removed, and nothing in the chapter reinstates "
     "it. ⚠ Third use of this shape. A FOURTH IS A TIC — the next chapter that needs to point at "
     "III.2 should point at the argument (what playing requires) rather than at the figure."),
    ("book/DRAFT-LOG.md", "C15/trap5", "the union telos is four sentences later",
     "Day 187, ruling 59. The III.2 entry recording that Trap 5 is stated VERBATIM in Watts's "
     "primary text — the log cannot record where the trap was found without naming it. Fresh line "
     "per the standing instruction on the whole-file DRAFT-LOG entry, which covers "
     "PROSE/manifestation ONLY."),
    # --- Day 187, ruling 65. FOUR LINES, NOT A WHOLE-FILE ENTRY, and deliberately so: this
    # rule was written an hour ago and its first four hits are the ruling that created it.
    # A whole-file exemption on 00 or 06 would blind the rule inside the two documents most
    # likely to reach for the retired phrase again while restating doctrine.
    ("00-ARCHITECTURE.md", "TERM/pre-rendered", "the title became",
     "Ruling 65 quoting the retired title in the sentence that retires it. The retitle cannot be "
     "recorded without naming what it replaced."),
    ("00-ARCHITECTURE.md", "TERM/pre-rendered", "two adjacent bullets",
     "Ruling 65's evidence: the two macro-structure bullets quoted side by side, which is the "
     "whole finding. Quoting only the surviving half would delete the contradiction from the "
     "record of the contradiction."),
    ("06-THE-SCAFFOLD.md", "TERM/pre-rendered", "the gauge flagged",
     "The III.3 entry's retitle history — the Day-186 title quoted so the two-round failure is "
     "legible to a reader who arrives after both fixes."),
    ("06-THE-SCAFFOLD.md", "TERM/pre-rendered", "immediately above",
     "Same entry, the `00` adjacency quoted as evidence. Own line, per the standing rule that an "
     "exemption is a named line and never a paragraph."),
    ("06-THE-SCAFFOLD.md", "TERM/egregore", "**Beats:** egregores",
     "★ THE BEAT LINE THAT PRODUCED THE RULING, and the one place in the apparatus the word was "
     "ever going to be. `06` is the PLAN, not prose — SCOPE, not licence, the DRAFT-LOG pattern. "
     "The plan is what routed the term to a chapter and therefore what forced it to be screened; "
     "editing the beat to remove the word would delete the reason ruling 109 exists from the file "
     "that caused it. ⚠ Deliberately NOT widened to the whole file: the ✅ entry below it and the "
     "two IV.5 prose lines are already suppressed as MENTIONS by the mention/use window, and if a "
     "later edit turns any of them into a USE this rule must fire."),
    ("book/DRAFT-LOG.md", "TERM/pre-rendered", "asserted, in a prefix",
     "The III.3 entry naming the retired title in the sentence recording its retirement. Fresh "
     "line, per the standing instruction on the whole-file DRAFT-LOG entry, which covers "
     "PROSE/manifestation ONLY."),
    # --- Day 189, V.5. Three USE-class hits that had been standing since Aug 7 in APPARATUS
    # files, surfaced by the V.5 run and dispositioned in the same pass rather than filed.
    # A USE-class hit nobody rules on is how a sweep goes quiet: the next reader sees three
    # standing hits, learns the output is noisy, and stops reading the section.
    ("06-THE-SCAFFOLD.md", "TERM/substrate", "THE SUBSTRATE ANSWER IS THE ONLY THING",
     "RULING 9's COROLLARY, VERBATIM — the licence already existed and the row was missing. "
     "IV.6's scaffold entry naming `substrate-independence`'s territory, which is the standard "
     "name of a position in philosophy of mind that IV.6 must engage; refusing to name an "
     "opponent's term is worse than using it. Named line, not the entry: a second use in IV.6's "
     "block is a fresh decision. Found Day 189 by the V.5 run; standing since 0270ec3, Aug 7."),
    ("book/DRAFT-LOG.md", "TERM/substrate", "cross-substrate work",
     "THE LOG TALKING ABOUT MY OWN RUNTIME, NOT THE BOOK'S REFERENT — and the distinction is the "
     "whole of the exemption. §3a retires `substrate` for the BOOK's vocabulary because it is "
     "Bostrom's word for the hardware and a bare synonym for the Ground. Neither applies to a "
     "note about which model drafted what. Named line; any use of the word FOR THE GROUND in "
     "this file must still fire. Standing since e0b8f13, Aug 7."),
    ("book/DRAFT-LOG.md", "TERM/aperture", "what the aperture admits",
     "Same ground as the line above: the log describing a REVIEW PROCESS's selectivity, not the "
     "book's demoted term for the Perspective. §3's demotion governs the manuscript's vocabulary. "
     "Named line. Standing since e0b8f13, Aug 7."),
    ("book/DRAFT-LOG.md", "TERM/substrate", "the IV.6 entry naming the opponent's term",
     "★ THE EXEMPTION'S OWN RECEIPT FIRING — V.5's log entry recording the three disposals above "
     "quotes the term in the sentence that rules on it, and the sweep found the record one run "
     "after it found the thing recorded. Same principle already on the books for TERM/map-self: "
     "a register that cannot quote the breach it ruled on cannot record the ruling. Named line, "
     "and the line is a citation of `06`:1262, not a use. Day 189."),
]


def exemption_for(path: pathlib.Path, rule_id: str, line: str):
    rel = path.as_posix()
    for suffix, rid, needle, why in EXEMPTIONS:
        if rid == rule_id and rel.endswith(suffix) and (needle is None or needle in line):
            return why
    return None


SCAFFOLD_NAME = "06-THE-SCAFFOLD.md"

CHAPTER_RE = re.compile(r"^### ((?:[IVX]+|C)\.\d+) — (.+?)\s*$", re.MULTILINE)

# Ruling 14 — filenames of drafted chapters in Books II-VIII. Book I is absent on
# purpose; so is every register that happens to live under book/.
CHAPTER_AFTER_I = re.compile(r"^(II|III|IV|V|VI|VII|VIII)-\d")
CHAPTER_ANY = re.compile(r"^[IVX]+-\d")
TOUCHES_RE = re.compile(r"^\*\*Touches:\*\*", re.MULTILINE)


def in_code_span(line: str, pos: int) -> bool:
    """True if `pos` falls inside a backtick code span. Odd number of backticks before it."""
    return line.count("`", 0, pos) % 2 == 1


def emphasis_wrapped(line: str, start: int, end: int) -> bool:
    """True if the match is wrapped *tightly* in markdown emphasis: *x*, **x**, _x_.

    Deliberately tight. A whole italicised sentence containing the term is still a USE —
    the claim being made is 'this word is being pointed at', and pointing at one word does
    not license a paragraph of it.
    """
    before, after = line[:start], line[end:]
    for mark in ("**", "*", "_"):
        if before.endswith(mark) and after.startswith(mark):
            return True
    return False


def in_scope(scope: str, path: pathlib.Path, is_prose: bool) -> bool:
    if scope == "all":
        return True
    if scope == "prose":
        return is_prose
    if scope == "scaffold":
        return is_prose or path.name == SCAFFOLD_NAME
    if scope == "chapters-not-II-01":
        # 05 §7's Day-187 second amendment. The four-clause definition ends on *made of
        # awareness* and is the excerptable sentence; quoted alone it is idealism. INSIDE
        # II.1 the neutrality gloss is 2,000 words downstream and that placement is ruled
        # correct — the misreading cannot be answered before the first three clauses
        # stand. EVERYWHERE ELSE there is no chapter to carry it. Whitelist by chapter
        # filename, per ruling 14's scope lesson: a scope phrased as "book/ but not X"
        # swept a register the first time it was written.
        return bool(CHAPTER_ANY.match(path.name)) and not path.name.startswith("II-01")
    if scope == "book-after-one":
        # Ruling 14: Book I's mythic names are retired at the I/II boundary.
        # DRAFTED CHAPTERS OF BOOKS II-VIII ONLY. Enumerated rather than expressed as
        # "in book/ and not Book I", because that phrasing also swept book/DRAFT-LOG.md,
        # a register that must stay free to quote Book I's prose. Whitelist, not blacklist.
        return bool(CHAPTER_AFTER_I.match(path.name))
    raise ValueError(f"unknown scope {scope!r}")


def paragraphs(lines):
    """Group the file into blocks of consecutive non-blank lines.

    Returns [(joined_text, [(char_offset, line_no, raw_line), ...]), ...] so a match found
    in `joined_text` can be resolved back to the line it starts on.
    """
    out, block = [], []
    for n, line in enumerate(lines, 1):
        if line.strip():
            block.append((n, line))
        elif block:
            out.append(block)
            block = []
    if block:
        out.append(block)
    built = []
    for block in out:
        parts, spans, off = [], [], 0
        for n, line in block:
            s = line.strip()
            spans.append((off, n, line))
            off += len(s) + 1          # +1 for the joining space
            parts.append(s)
        built.append((" ".join(parts), spans))
    return built


# Ruling 103. The unit a mention actually lives in is the SENTENCE. `MENTION_MARKERS` was
# always applied to a LINE, and a line in this manuscript is a hard wrap — an artifact of
# the file, not of the prose. So a cue word and the term it is talking ABOUT get separated
# by a wrap and the suppressor stops seeing them together: a mention is promoted to a
# USE-class hit and the tool reports a breach that is not there. Tripped Day 187 in the
# DRAFT-LOG, and repaired that night by REWRAPPING the line rather than exempting it,
# because an exemption would have hidden the class instead of naming it. This is the class.
#
# WHY NOT THE PARAGRAPH, which is what `beat_sweep.chapters()` reads and what the Day-187
# note proposed. Because a paragraph-wide guard suppresses far more than a line-wide one —
# a single ⚠ anywhere in a long block would excuse every hit in it — and quiet
# over-suppression is how a gauge stops measuring while still printing output. That warning
# is already written twice in this file (the PARA_LICENSED_RULES note, and the cross-wrap
# pass's own comment). The sentence is the narrowest window that fixes the defect: WIDER
# than the wrap, so the cue is found; NARROWER than the block, so it cannot be borrowed
# from three sentences away.
#
# Over-splitting is the safe direction here — a window cut too short suppresses less, and
# the gauge measures more. Abbreviations ("e.g. ") split; decimals and section numbers
# ("0.60", "II.6") do not, because the period is not followed by whitespace.
SENT_END = re.compile(r"""(?<=[.!?])["'”’\)\]\*]*\s""")


def sentence_window(joined: str, start: int, end: int) -> str:
    """The sentence of `joined` containing [start, end) — the cue's search window."""
    lo = 0
    for m in SENT_END.finditer(joined, 0, max(0, start)):
        lo = m.end()
    m = SENT_END.search(joined, end)
    return joined[lo:m.end() if m else len(joined)]


def sentence_at(para_at, n: int, line: str, m) -> str:
    """Sentence window for a LINE-pass match: map the raw-line offset into the block first.

    Falls back to the line itself if the line is not in a block (it always is; the guard is
    there so a mapping bug degrades to today's behaviour rather than throwing at 3am).
    """
    if n not in para_at:
        return line
    joined, base, indent = para_at[n]
    return sentence_window(joined,
                           base + max(0, m.start() - indent),
                           base + max(0, m.end() - indent))


def line_of(spans, pos):
    """(line_no, raw_line) for the joined-text offset `pos`."""
    found = spans[0]
    for span in spans:
        if span[0] <= pos:
            found = span
        else:
            break
    return found[1], found[2]


def sweep_file(path: pathlib.Path, is_prose: bool):
    uses, mentions, exempt = [], [], []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        print(f"  !! {path.name}: not utf-8, skipped")
        return [], [], []
    paras = paragraphs(lines)
    # line_no -> the joined text of its paragraph. Needed by PARA_LICENSED_RULES, whose
    # `licensed` field is a REQUIRED COMPANION rather than an exception: the finding is
    # that a companion sentence is MISSING, and "missing from this one wrapped line" is
    # not the claim. Every other rule's guard stays line-scoped, unchanged.
    para_of = {}
    # line_no -> (joined paragraph, that line's offset into it, its indent) so a match found
    # at a RAW-line offset can be located inside the joined block. Ruling 103's plumbing:
    # the sentence window needs the joined text, and the line pass only has the line.
    para_at = {}
    for joined, spans in paras:
        for off, ln, raw in spans:
            para_of[ln] = joined
            para_at[ln] = (joined, off, len(raw) - len(raw.lstrip()))
    for rule_id, scope, pattern, licensed, why in RULES:
        if not in_scope(scope, path, is_prose):
            continue
        flags = 0 if rule_id in CASE_SENSITIVE_RULES else re.IGNORECASE
        rx = re.compile(pattern, flags)
        lic = re.compile(licensed, flags) if licensed else None
        for n, line in enumerate(lines, 1):
            m = rx.search(line)
            if not m:
                continue
            guard_text = para_of.get(n, line) if rule_id in PARA_LICENSED_RULES else line
            if lic and lic.search(guard_text):
                continue
            reason = exemption_for(path, rule_id, line)
            if reason:
                exempt.append((rule_id, path, n, line.strip()[:150], reason))
                continue
            # A term wrapped in a code span or in emphasis is being NAMED, not used.
            # Checked against the MATCH, never against the line, so one code span does not
            # excuse a whole paragraph — a broad exemption is how a gauge quietly stops
            # measuring. Widened Day 186 from "backticks immediately adjacent" to (a) any
            # enclosing code span, because `prose/RULING-13-the-narrowing.md` is a filename
            # and the old test only saw the characters touching the word, and (b) direct
            # `*x*` / `**x**` emphasis, because naming a retired word to refuse it is what
            # ruling 13's own §3 paragraph is FOR. Emphasis must wrap the term itself and
            # nothing else — an italicised sentence that merely contains it still counts.
            if in_code_span(line, m.start()) or emphasis_wrapped(line, m.start(), m.end()):
                mentions.append((rule_id, path, n, line.strip()[:150], why))
                continue
            hit = (rule_id, path, n, line.strip()[:150], why)
            # ADDITIVE, and deliberately so: the LINE test is kept and the sentence window
            # is an extra OR. Two reasons. (a) `^\s*\|` — the table-row cue — is anchored to
            # the start of a physical line, and consecutive table rows join into ONE block,
            # so a window-only test would see the pipe on the first row and nowhere else.
            # (b) Additive means this change can only move hits USE→mention, never the
            # reverse, so the delta is readable in one direction. The tightening it declines
            # to make (a cue in a DIFFERENT sentence of the same line should stop
            # suppressing) is a real finding and a separate one; folding it in here would
            # have made both invisible.
            is_mention = bool(MENTION_MARKERS.search(line)) or bool(
                MENTION_MARKERS.search(sentence_at(para_at, n, line, m))) or (
                not is_prose and bool(PLANNING_MENTION.match(line)))
            (mentions if is_mention else uses).append(hit)

        # --- CROSS-WRAP PASS (Day 187) -------------------------------------------------
        # Every rule above is applied LINE BY LINE and the manuscript is hard-wrapped, so a
        # needle spanning a wrap matches nothing and the file is reported clean. Found four
        # times in three days. The first three were exemptions that failed to fire — noisy,
        # harmless. The fourth was a real breach: `create your own\nreality`, the single most
        # quotable phrase in the banned list, sitting in II.2 while this tool printed "no
        # USE-class hits". A false negative on the manuscript is the failure direction that
        # matters, and it does not announce itself, because a clean sweep looks identical to
        # a clean chapter.
        #
        # ADDITIVE ON PURPOSE. It reports ONLY matches that cross a join point; anything the
        # line pass can see is skipped here, so this cannot change any existing verdict.
        # Mention-classification deliberately reads the START LINE and not the joined window
        # — a wider context suppresses more, and quiet over-suppression is how a gauge stops
        # measuring while still printing output. AMENDED by ruling 103: it now also reads the
        # SENTENCE the match sits in. The refusal above stands as written — the ±90-character
        # window is still refused, because it has no grammatical edge and would suppress by
        # accident of arithmetic. A sentence has one. See SENT_END.
        for joined, spans in paras:
            for m in rx.finditer(joined):
                ln_start, raw = line_of(spans, m.start())
                ln_end, _ = line_of(spans, max(m.start(), m.end() - 1))
                if ln_start == ln_end:
                    continue                      # the line pass already saw this one
                window = joined[max(0, m.start() - 90):m.end() + 90].strip()
                if lic and lic.search(joined if rule_id in PARA_LICENSED_RULES else window):
                    continue
                reason = exemption_for(path, rule_id, window)
                if reason:
                    exempt.append((rule_id, path, ln_start,
                                   "(cross-wrap) " + window[:150], reason))
                    continue
                hit = (rule_id, path, ln_start, "(cross-wrap) " + window[:150], why)
                # Ruling 103 applies here TOO, and here it is not a corner case: a match
                # that crosses a wrap is one whose cue is, by construction, likely to be on
                # the other side of that wrap. The comment above ("reads the START LINE and
                # not the joined window") was right to refuse the WINDOW — ±90 characters is
                # an arbitrary span with no grammatical edge. It is the sentence that has one.
                is_mention = bool(MENTION_MARKERS.search(raw)) or bool(
                    MENTION_MARKERS.search(sentence_window(joined, m.start(), m.end()))) or (
                    not is_prose and bool(PLANNING_MENTION.match(raw)))
                (mentions if is_mention else uses).append(hit)
    return uses, mentions, exempt


def check_touches(scaffold: pathlib.Path):
    """Every chapter in 06 must name the C-numbers it touches. Enforcement item 1."""
    if not scaffold.exists():
        return None
    text = scaffold.read_text(encoding="utf-8")
    chapters = CHAPTER_RE.findall(text)
    blocks = re.split(r"^### ", text, flags=re.MULTILINE)[1:]
    missing = [CHAPTER_RE.match("### " + b.splitlines()[0]).group(1)
               for b in blocks if CHAPTER_RE.match("### " + b.splitlines()[0])
               and not TOUCHES_RE.search(b)]
    return len(chapters), missing


def selftest() -> int:
    """Ruling 103's classifier, enforced. FOUR cases, and the two NEGATIVES matter most.

    A gauge that suppresses correctly is worth nothing on its own; the question is always
    what it suppresses by accident. C proves a real breach with no cue is still reported.
    D proves the window stops at the sentence edge and does not borrow a cue from the
    sentence before it — which is precisely what a paragraph-wide guard would have done,
    and is the reason this fix is scoped to a sentence rather than to a block.
    """
    doc = (
        "### Fixture\n\n"
        "A. The phrase the opposition itself quoted\n"
        "is create your own reality, and the chapter cuts it.\n\n"
        "B. The one phrase they quoted at us, and the only one, is\n"
        "create your own\n"
        "reality, credited on the spot.\n\n"
        "C. An honest breach with no cue anywhere near it: create your own reality.\n\n"
        "D. A cue that belongs to a different sentence entirely, quoted there.\n"
        "Here we simply say create your own reality and mean it.\n"
    )
    tmp = pathlib.Path(tempfile.gettempdir()) / "claim_sweep_selftest.md"
    tmp.write_text(doc, encoding="utf-8")
    try:
        uses, mentions, _ = sweep_file(tmp, True)
    finally:
        tmp.unlink(missing_ok=True)
    u = " || ".join(h[3] for h in uses if h[0] == "PROSE/manifestation")
    m = " || ".join(h[3] for h in mentions if h[0] == "PROSE/manifestation")
    checks = [
        ("A line-pass mention whose cue is across a wrap", "and the chapter cuts it" in m),
        ("B cross-wrap mention whose cue is across a wrap", "credited on the spot" in m),
        ("C real breach with no cue is still a USE hit", "An honest breach" in u),
        ("D cue in a DIFFERENT sentence does not suppress", "and mean it" in u),
    ]
    bad = [name for name, ok in checks if not ok]
    print("  mention/use self-test:",
          "PASS — the window is wider than a wrap and narrower than a block"
          if not bad else "** FAIL ** " + "; ".join(bad))
    return 0 if not bad else 2


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--prose", default="book", help="directory of book prose (default: book/)")
    ap.add_argument("--show-mentions", action="store_true",
                    help="print suppressed mentions, to audit the mention/use classifier")
    ap.add_argument("--selftest", action="store_true",
                    help="the mention/use classifier test only")
    args = ap.parse_args()

    # ALWAYS FIRST, never optional. A clean sweep produced by a broken classifier is
    # indistinguishable from a clean manuscript — that is the whole failure this tool keeps
    # having, and the only defence is a gauge on the gauge that runs before the verdict.
    rc = selftest()
    if rc:
        print("  refusing to report a verdict from a classifier that fails its own test.")
        return rc
    if args.selftest:
        return 0
    print()

    prose_root = (REPO / args.prose).resolve()
    files = sorted(p for p in REPO.rglob("*.md") if ".git" not in p.parts)

    all_uses, all_mentions, all_exempt = [], [], []
    for f in files:
        is_prose = prose_root in f.parents
        u, m, e = sweep_file(f, is_prose)
        all_uses += u
        all_mentions += m
        all_exempt += e

    print(f"CLAIM SWEEP — {len(files)} files · prose root: "
          f"{prose_root.relative_to(REPO) if prose_root.exists() else '(none yet)'}\n")

    if all_uses:
        print(f"!! {len(all_uses)} USE-class hit(s) — read every one, then fix or allowlist:\n")
        for rule_id, path, n, line, why in all_uses:
            print(f"  [{rule_id}] {path.relative_to(REPO)}:{n}")
            print(f"      {line}")
            print(f"      → {why}\n")
    else:
        print("  no USE-class hits.\n")

    print(f"  {len(all_mentions)} mention(s) suppressed "
          f"(lines talking ABOUT the term — rerun with --show-mentions to audit).")

    # Always printed, never folded into the mention count: a suppression nobody can see
    # is a suppression nobody audits, and these are the ones we chose on purpose.
    print(f"\n  {len(all_exempt)} DELIBERATE exemption(s) in force "
          f"({len(EXEMPTIONS)} rule(s) in the list):")
    # ⚠ Day 188, with ruling 113: runs of the SAME (rule, file, reason) are COLLAPSED.
    # The whole-file exemption added an hour ago printed 35 identical lines and buried the
    # thirty named-line exemptions underneath — which is this block's own docstring failing
    # one level up: a suppression list nobody can READ is a suppression list nobody audits.
    # Every line number still prints. This wraps the list; it does not shorten it.
    grouped = {}
    for rule_id, path, n, line, why in all_exempt:
        grouped.setdefault((rule_id, path, why), []).append(n)
    for (rule_id, path, why), lns in grouped.items():
        rel = path.relative_to(REPO)
        if len(lns) > 3:
            print(f"    [{rule_id}] {rel} — {len(lns)} lines: "
                  f"{','.join(str(x) for x in lns)}")
            print(f"        → {why[:150]}")
        else:
            for n in lns:
                print(f"    [{rule_id}] {rel}:{n} — {why[:96]}")
    if args.show_mentions:
        for rule_id, path, n, line, _ in all_mentions:
            print(f"    [{rule_id}] {path.relative_to(REPO)}:{n}  {line[:100]}")

    t = check_touches(REPO / "06-THE-SCAFFOLD.md")
    if t:
        total, missing = t
        print(f"\n  TOUCHES coverage: {total - len(missing)}/{total} chapters carry a "
              f"**Touches:** line.")
        if missing:
            print(f"    missing: {', '.join(missing)}")

    report_formula_density(prose_root)
    report_cut_shapes(prose_root)

    print("\n  Reminder: this tool reports LINES, not doctrine. A subtle breach walks past it.")
    return 1 if all_uses else 0


# --- RULING 15: the apophatic formula, REPORTED and never tripped ----------------
#
# The move is "X wants Y, and there is no Y" — the via negativa applied to desire, and
# it is Book I's doctrine rather than its ornament, so a gauge that FAILS on it would be
# a gauge that fails on the argument. It reports.
#
# ⚠ It reports RAW, and the overcount is stated rather than hidden — in the SAME UNIT it
# prints, which took two corrections to get right on the day it was written:
#   * The hand count that produced ruling 15 was 26 — but that was 26 matching LINES,
#     and this prints OCCURRENCES. Same evidence, different unit; a baseline in the wrong
#     unit is worse than none, because it looks comparable.
#   * Wrap-corrected occurrences on the same text: 52. Of these ~17-18 are the true
#     formula (the ~16 hand-marked lines, two of which carry it twice), so the raw number
#     over-reads by roughly 3x, not the ~38% the line count suggested.
# A regex that could tell a doctrinal denial from a plain one would have to parse the
# want preceding it. We did not build that. **A tripping gauge that cries wolf two times
# in three gets ignored, which is worse than no gauge** — so this one has no threshold,
# no exit code and no opinion. It hands over a number and a baseline; a person does the
# rest. What it IS good for is MOVEMENT: the rate is stable across Book I's six chapters,
# so a later book that departs from it departs visibly.
FORMULA_RE = re.compile(r"\bthere (?:is|was) (?:no|nothing|nobody|nowhere|none)\b", re.I)

# Book I as drafted and ruled acceptable on Day 187. The point of a baseline is that a
# later book can be compared to something instead of to a feeling.
BASELINE = ("Book I as ruled acceptable, Day 187 (pre-ruling-15 text): 52 occurrences / "
            "6,354 words = 8.18/1k raw, of which ~17-18 are the formula proper (~2.8/1k)")


def report_formula_density(prose_root):
    if not prose_root.exists():
        return
    # ⚠ Match the CHAPTER pattern, not "starts with a capital" — DRAFT-LOG.md starts
    # with a capital too, and ruling 14's first scope draft swept exactly that file, a
    # register, and counted its quotations as prose. Same trap, eight hours later.
    chapters = sorted(p for p in prose_root.glob("*.md")
                      if re.match(r"^[IVX]+-\d+-", p.name))
    if not chapters:
        return
    print("\n  APOPHATIC FORMULA density (ruling 15 — REPORTED, never tripped):")
    tot_hits = tot_words = 0
    for p in chapters:
        text = p.read_text(encoding="utf-8", errors="replace")
        words = len(text.split())
        # ⚠ COLLAPSE WHITESPACE FIRST. The manuscript is hard-wrapped at ~100 chars, so
        # roughly one formula in six straddles a line break — "there\nis nobody" does not
        # match "there (?:is|was)". Caught on the day this was written, and only because
        # a new instance was added to I.2 and THE NUMBER DID NOT MOVE. A gauge that does
        # not respond when you feed it the thing it measures is the whole trip-test, and
        # it is the same lesson ruling 14 paid for: a rule with nothing in scope passes
        # forever and proves nothing.
        hits = len(FORMULA_RE.findall(re.sub(r"\s+", " ", text)))
        tot_hits += hits
        tot_words += words
        rate = (hits / words * 1000) if words else 0.0
        print(f"    {p.name:<28} {hits:>3} raw · {words:>5}w · {rate:5.2f}/1k")
    rate = (tot_hits / tot_words * 1000) if tot_words else 0.0
    print(f"    {'ALL DRAFTED':<28} {tot_hits:>3} raw · {tot_words:>5}w · {rate:5.2f}/1k")
    print(f"    baseline — {BASELINE}")
    print("    raw over-reads ~3x (ordinary negation); no threshold is set and none "
          "should be inferred. Watch MOVEMENT, not level.")


# ---------------------------------------------------------------------------
# RULING 43 — THE CUT-SHAPE INVENTORY.
#
# Rule 5 requires every ancestor be credited at full strength and then cut. It does
# NOT require the cut be made in the same sentence every time, and `03` §3.5's actual
# prescription was ONE CLAUSE AT THE POINT OF USE — every fifth-silence name had been
# escalated to a full set piece.
#
# ⚠ THE DEFECT IS NOT DENSITY, IT IS UNIFORMITY, so this reporter prints SHAPES and not
# a number. When the credit is always the setup for the same sentence, the reader stops
# reading the credit — which defeats the thing rule 5 was for. A count cannot see that;
# a list of the actual constructions, side by side, can.
#
# Reported, never tripped — same contract as ruling 15's density gauge, and for the same
# reason: there is no correct level, only a movement worth looking at. The licence this
# measures against is on the page already. **Mariotte is never cut** (used as a
# measurement) and **Nishida does the cutting for us** (against a reading, not a person).
# Those two are the proof that rule 5 does not require the liturgy, and if a later book
# has none of that kind, that is the finding.
STOCK_CUT = re.compile(
    r"Where (?:he|she|they) (?:goes?|stops?|lands?)"
    r"(?:\s+and\s+this\s+does\s+not)?\s*:", re.I)
ANY_CUT = re.compile(
    r"(?:Where (?:he|she|they) (?:goes?|stops?|lands?)[^.:]{0,40}:"
    r"|\bThe cut is\b[^.]{0,70}"
    r"|\b(?:He|She|They) (?:stops?|keeps?|takes?) (?:one|it one)[^.]{0,60})", re.I)


def report_cut_shapes(prose_root):
    if not prose_root.exists():
        return
    chapters = sorted(p for p in prose_root.glob("*.md")
                      if re.match(r"^[IVX]+-\d+-", p.name))
    if not chapters:
        return
    print("\n  ANCESTOR CUT-SHAPES (ruling 43 — REPORTED, never tripped):")
    stock = shapes = 0
    for p in chapters:
        # Collapse whitespace first — the manuscript hard-wraps at ~100 chars and a cut
        # marker straddles the break roughly one time in six. Ruling 15's gauge paid for
        # this lesson already; not paying for it twice.
        text = re.sub(r"\s+", " ", p.read_text(encoding="utf-8", errors="replace"))
        found = ANY_CUT.findall(text)
        if not found:
            continue
        print(f"    {p.name}")
        for f in found:
            f = f.strip()
            is_stock = bool(STOCK_CUT.match(f))
            stock += is_stock
            shapes += 1
            print(f"      {'STOCK ' if is_stock else '      '}{f[:78]}")
    if shapes:
        print(f"    {shapes} cut marker(s), of which {stock} use the stock "
              f"'Where he goes/stops' opener.")
    print("    READ THE COLUMN, not the count. Two markers that name different objects "
          "(a word, a scope,\n    a sum, a room he kept) are a discipline; two that open "
          "identically are a rite. Book II\n    shipped with five stock openers, four of "
          "them in II.1-II.3 where the reader learns the\n    shape — front-loading, not "
          "book-wide. Baseline after ruling 43's repair: 1.")


if __name__ == "__main__":
    sys.exit(main())
