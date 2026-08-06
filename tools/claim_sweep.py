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
    # ⚠ Day 187 — CASE HOLE, and it is a CLASS defect, patched here for the second time
    # per-term rather than fixed. These patterns are case-SENSITIVE, so `THE NARROWING` in a
    # heading walked straight past this rule; TERM/map already carries a hand-added `\bTHE MAP\b`
    # for exactly the same reason and nobody generalised it. Headings and chapter titles are
    # upper-case, and *the map*'s whole precedent is that it survived a day IN TWO CHAPTER TITLES.
    # The real fix is re.IGNORECASE on the TERM/* family with the licence patterns re-checked
    # under it. Not done tonight because it is a behaviour change to every TERM rule at once.
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
    ("TERM/fullness", "book-after-one", r"\bthe Fullness\b|\bthe still\b", None,
     "05 §3a — RULING 14 (Day 187). *The Fullness* and *the still* are Book I's mythic names for "
     "the Ground, and they are RETIRED at the I/II boundary. I.6's closing move — 'they will not "
     "hold' — makes the supersession deliberate, and a deliberate supersession leaks the moment a "
     "later book reaches back for the old name for variety. Axis 3, POLYSEMY: not a collision "
     "(nobody else owns it) and not a gradient (the word is not ominous) — our own two names for "
     "one referent, which is the defect the lexicon's collision-only column could never see. "
     "SCOPE: drafted chapters after Book I. The registers may discuss the terms freely; the "
     "prose may not use them. The term is **the Ground**."),
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
     "usual detectors miss it. NOTE: legitimate where the cut is being MADE (I.6 b4, VIII.6)."),

    # --- prose-only ------------------------------------------------------------
    ("PROSE/self-reference", "prose",
     r"\bDoPI\b|Corpus[- ]Perspectival|\bthe Anchor\b|Coherent Structure|The Inside View|"
     r"\bin (?:our|the) (?:previous|earlier|prior) (?:work|volume|book)|as we (?:argued|showed|"
     r"have argued|have shown) (?:elsewhere|previously|earlier)|\bour earlier work\b", None,
     "Clayton, Day 186: no past work of ours is referred to by name. AND the anonymous form is "
     "worse — it points at something the reader cannot even look up. See 00, ruling 8."),
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
    ("book/DRAFT-LOG.md", "TERM/bottleneck", "bottleneck geometry",
     "★ Day 187, II.3. The log quoting the Null-Space Theorem's RETRIEVED FORMAL STATEMENT, which "
     "uses the retired term — in the sentence whose entire point is that it does, and that this is "
     "why II.3's beat says 'in plain words'. Tidying the quotation into current vocabulary would "
     "destroy the evidence for the ruling it is evidence for. Own line, per the standing "
     "instruction on the DRAFT-LOG entry above; not a widening of it."),
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
    for rule_id, scope, pattern, licensed, why in RULES:
        if not in_scope(scope, path, is_prose):
            continue
        rx = re.compile(pattern, re.IGNORECASE)
        lic = re.compile(licensed, re.IGNORECASE) if licensed else None
        for n, line in enumerate(lines, 1):
            m = rx.search(line)
            if not m:
                continue
            if lic and lic.search(line):
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
            is_mention = bool(MENTION_MARKERS.search(line)) or (
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
        # measuring while still printing output.
        for joined, spans in paras:
            for m in rx.finditer(joined):
                ln_start, raw = line_of(spans, m.start())
                ln_end, _ = line_of(spans, max(m.start(), m.end() - 1))
                if ln_start == ln_end:
                    continue                      # the line pass already saw this one
                window = joined[max(0, m.start() - 90):m.end() + 90].strip()
                if lic and lic.search(window):
                    continue
                reason = exemption_for(path, rule_id, window)
                if reason:
                    exempt.append((rule_id, path, ln_start,
                                   "(cross-wrap) " + window[:150], reason))
                    continue
                hit = (rule_id, path, ln_start, "(cross-wrap) " + window[:150], why)
                is_mention = bool(MENTION_MARKERS.search(raw)) or (
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--prose", default="book", help="directory of book prose (default: book/)")
    ap.add_argument("--show-mentions", action="store_true",
                    help="print suppressed mentions, to audit the mention/use classifier")
    args = ap.parse_args()

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
    for rule_id, path, n, line, why in all_exempt:
        print(f"    [{rule_id}] {path.relative_to(REPO)}:{n} — {why[:96]}")
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


if __name__ == "__main__":
    sys.exit(main())
