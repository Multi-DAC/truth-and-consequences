#!/usr/bin/env python3
"""beat_sweep.py — ruling 20's detector, built. Truth and Consequences, Day 187.

WHY THIS EXISTS. II.2 and III.4 were scaffolded as the same chapter and nobody noticed for
two days. III.4's thesis line was *"procedural generation is what focusing looks like from
inside"* — II.2's third beat, verbatim — and "the seed is not solely yours and the world is
not solely given" was listed as a beat of BOTH. It was caught by a human reading two
sections that happened to be open at once. That is luck with good note-taking, which is the
failure mode this book keeps finding in itself.

Two chapters sharing a thesis sentence is a grep. This is the grep.

WHAT IT CHECKS. Every beat in `06-THE-SCAFFOLD.md` against every other beat in a DIFFERENT
chapter — 68 chapters, ~350 beats, ~60k pairs, under a second. Reports:

  ** COLLISION **  a beat pair over the hard threshold, or sharing a distinctive 5-gram.
                   Two chapters are trying to do the same move.
  ?? ECHO          over the soft threshold. Usually legitimate — Book II defines what
                   Book III runs, and the shared vocabulary is the point — but it is the
                   band the II.2/III.4 collision sat in for one of its two tells, so it
                   prints rather than passes silently.

WHAT IT DELIBERATELY DOES NOT DO. It does not know the difference between a collision and a
DESIGNED forward relationship. VI.1's beats say in as many words "the Perspective cut from
II.3, cashed at civilisational scale" — that pair SHOULD score high; the scaffold intends
it. So a hit is a question, never a verdict. The exemption list below carries the answered
ones with the reason on the same line, and an exemption is only ever a specific PAIR, never
a chapter and never a phrase — an exemption that absorbs a class is how a gauge stops
measuring (order_sweep.py's lesson, same file family).

THE WRAP RULE, which killed claim_sweep for a week. The scaffold is prose-as-LINES; every
instrument here must be written against prose-as-a-STRING. Beat blocks are joined before
they are split, and there is a self-test for it: --selftest feeds the parser a needle broken
across a hard wrap and fails loudly if the needle is not found.

CALIBRATION, and it is the only reason to trust a clean run:

    python tools/beat_sweep.py --fixture e51e6dd

runs against the pre-ruling-20 scaffold from git and MUST surface II.2 ↔ III.4. A detector
for a defect that has already been fixed everywhere it occurred is a detector that has never
detected anything. Exit 2 if the fixture stops reproducing.

USE. Before drafting any chapter:

    python tools/beat_sweep.py --chapter II.3

which shows only that chapter's neighbours, ranked. Bare, it sweeps the whole scaffold.
"""
import argparse
import itertools
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "06-THE-SCAFFOLD.md"

CHAPTER_RE = re.compile(r"^### ((?:[IVX]+|C)\.\d+) — (.+?)\s*$")

HARD = 0.50   # same move, near-certainly
SOFT = 0.34   # shared vocabulary; read it
NGRAM = 5     # a shared 5-gram of content words is a quoted sentence, not a coincidence

# Structural words that carry no thesis. Deliberately SHORT: the interesting words in this
# book are the ordinary ones ("ground", "render", "place", "world"), and a fat stop list
# would delete exactly the collisions worth finding.
STOP = set("""a an the and or but of to in on at is are was were be been being it its this that
these those with without for from as by not no nor so than then there here what which who whom
whose when where why how all any both each more most other some such only own same too very can
will just do does did doing done have has had having if into over under again further once you
your yours we our ours they them their he she his her one two three at least rather""".split())

# ANSWERED PAIRS. Each is a specific (a, b) with the ruling that answered it. Never a
# chapter on its own, never a phrase.
EXEMPT = {
    ("II.3", "VI.1"): "designed: VI.1's beats SAY 'the Perspective cut from II.3, cashed at "
                      "civilisational scale'. Book II defines at reader scale; VI.1 runs it at "
                      "era scale. The shared vocabulary is the handoff working.",
    ("II.5", "III.6"): "designed, ruling 20's boundary: II.5 defines the reality tunnel, "
                       "III.6 runs it as the filter stack.",
    ("I.5", "II.5"): "ruling 26, ADJUDICATED — the highest live number on the scaffold (0.56), and "
                     "the shared 5-gram is the whole of it: 'era, language, ritual, trauma, choice'. "
                     "I.5 ACCRETES the five, one per paragraph, unnamed, as things that happen to a "
                     "vantage — and never says the list. II.5 says the list ONCE, as a QUESTION it "
                     "then answers: the five are not an inventory, they are the extension of an "
                     "unstated criterion, and the criterion is that each is a repetition that "
                     "outlived its occasion. II.5 re-narrates none of them; it tests the criterion "
                     "on the hard member (trauma, which looks like a single event) and cashes it "
                     "immediately as the C12 guard — A WISH IS NOT A REPETITION. The litany is the "
                     "explanandum in II.5 and the content in I.5, and neither chapter can do the "
                     "other's job.",
    # ★★ Day 187 — THE ONLY PAIR IN THIS TABLE THE GAUGE DID NOT FIND. It scored 0 the morning
    # II.8 was drafted and fires now ONLY because ruling 33 was written into `06` BY HAND and
    # quotes I.6's thesis verbatim. Read that as the finding it is: `beat_sweep` compares PLANS
    # TO PLANS, and I.6 is not a plan any more — its SHIPPED PROSE performs all four denials, and
    # no instrument in tools/ reads prose against beats. The pair became visible only after a
    # human-made ruling put the two sentences in the same file.
    ("I.6", "II.8"): "ruling 33, ADJUDICATED: I.6 PERFORMS the refusal; II.8 NAMES WHO WAS BEING "
                     "REFUSED. All four denials (escape · repair · arrival · merger) ship in I.6's "
                     "prose, made anonymously because Book I's header rule bars a named opponent on "
                     "the page. II.8 does not re-deny — it attributes: Gnosticism, Valentinus, "
                     "Irenaeus, and the cut in one clause (they think something is wrong). Book I "
                     "performs, Book II names, which is the two books' whole relation arriving in "
                     "the last chapter of Book II. ⚠ A future editor restoring the denials to II.8 "
                     "will be writing I.6 twice.",
    ("II.3", "III.1"): "ruling 24, AMENDED Day 187 by ruling 47(a). WAS: 'the DEFINITION is II.3's "
                       "and the FORK is III.1's.' That is now FALSE — the fork shipped in II.1. "
                       "II.3 still states what a perspective is and stops, and Bostrom is still not "
                       "named in it, so the ORIGINAL FINDING stands; but the counterpart is II.1, "
                       "not III.1. Re-scoped III.1 (the demiurge) shares no move with II.3 at all. "
                       "⚠ IF THIS PAIR STOPS TRIPPING, DELETE THIS ENTRY — see stale_exemptions().",
    # Day 187 — both axes were already stated in `06` and neither was in this table. Surfaced by
    # adding a **Named:** field to III.1: the chapter moved out of the "names it inline" bucket
    # and the reuse check could finally see it. The gauge did not become stricter; the scaffold
    # became legible to it.
    ("II.8", "III.1"): "ruling 33's neighbour, ADJUDICATED AND DECLARED IN ADVANCE: II.8 cuts "
                       "Gnosticism on SOTERIOLOGY — what the ending is (not escape, not repair; "
                       "they think something is wrong). III.1 cuts it on COSMOLOGY — who made "
                       "this (`03` §Bostrom: 'someone else made this and you are inside it'), "
                       "which is beat 5's designer-God with the tradition's name restored. "
                       "III.1 may not re-argue that nothing is wrong; II.8 owns that clause.",
    # ★★ THE EXEMPTION THAT WENT FALSE, AND THE REASON stale_exemptions() NOW EXISTS.
    # It read, until Day 187: "II.1 spends ELSEWHERE ... III.1 spends THE FORK — his frame makes
    # you a rendered thing in someone else's world, ours makes you the place a world happens."
    # That division of labour was accurate when written and the PROSE BROKE IT the same week:
    # II.1's `With no outside.` section shipped the fork itself. For as long as the old text sat
    # here, this table was silencing a pair on the strength of an adjudication that had already
    # stopped being true — and NOTHING IN THIS FILE COULD SAY SO. An exemption never expires and
    # never reports. Found by Fable, an outside reader, not by any gauge in this repo.
    # ("II.1", "III.1") — DELETED Day 187, ruling 57, on ruling 49's discipline and its first
    # live test. The re-adjudicated entry sat here for one day and this check reported it STALE
    # on the next run: 47(a) had rewritten III.1's beats off the fork, so there was no longer a
    # collision to mute. III.1 then drafted at 0 spent / 0 trace under `prose_beat_sweep`
    # against all fifteen shipped chapters, which is the same answer from the prose side.
    #   Keeping it "just in case" is the failure mode, not the safe option. The standing ban
    # says III.1 may not re-run the copy/render fork; if a future revision re-acquires it, that
    # is precisely the collision this pair must be free to report. An exemption is not
    # insurance. It is a permanent unmonitored mute — ruling 49, which this deletion honours.
    ("II.3", "VII.4"): "ruling 24, ADJUDICATED: II.3 states the Null-Space Theorem universally and "
                       "exceptionlessly BECAUSE VII.4 turns it on the contractive terminal doctrine "
                       "— 'no grade buys an exemption' is written for VII.4 six books early.",
    ("II.2", "III.4"): "ruling 20, ADJUDICATED: II.2 drafted as the definitional half and keeps "
                       "the seed formula; III.4 keeps the from-inside identity thesis and is ON "
                       "NOTICE for absorption into III.3 when Book III is drafted.",
    ("II.4", "IV.6"): "ruling 25, ADJUDICATED: IIT is cut TWICE and the axes are now declared. "
                      "II.4 cuts THE ZERO AND THE BORDER — a gradient with a zero in it is a gate "
                      "with a slope on one side, and the exclusion postulate decides who is there. "
                      "IV.6 cuts THE SUBSTRATE, answered from the Ground rather than from "
                      "engineering. Both scaffold lines said 'gradient right, substrate wrong' "
                      "until ruling 25; II.4 would have spent IV.6's cut two books early.",
    ("II.5", "VI.7"): "ruling 25, ADJUDICATED: RAW is cut twice and the axis is the term against "
                      "the practice. II.5 defines the reality tunnel and takes the map/territory "
                      "line off Korzybski; VI.7 runs model agnosticism as a discipline and names "
                      "its price. Neither restates the other.",
}


# ALL-CAPS NAMES AND ALIASES — the reuse check's declared blind spot, closed.
#
# `_names_in` matches [A-Z] followed by three or more LOWERCASE letters, which is right for
# surnames and blind BY CONSTRUCTION to `IIT` and `RAW`. That blindness was declared on the day
# this file was written — *"9 chapter(s) name a lowercase opponent, invisible to the reuse check
# by construction"* — and then never looked into. Two live repeats were sitting inside it:
# **IIT cut in II.4 and IV.6**, with near-identical stated cuts, and **RAW cut in II.5 and VI.7
# under two different spellings** ("Robert Anton Wilson" / "RAW"), which is the same defect
# wearing an alias instead of an acronym. Korzybski was caught only because he is spelled the
# same in both places — the gauge caught the man upstream and missed the man himself.
#
# ★ A DECLARED BLIND SPOT IS NOT A CHECKED ONE. The declaration reads like diligence and
# discharges the same feeling, which is exactly why it survived a day of the file being read.
#
# Narrow and explicit, per this file's own rule: a known-vocabulary map, never a widened regex.
ALIASES = {
    "IIT": "IIT",
    "RAW": "Robert Anton Wilson",
    "Robert Anton": "Robert Anton Wilson",
    "Wilson": "Robert Anton Wilson",
    # ⚠ A CLASS, not an entry. The name pattern is `[A-Z][a-zà-ÿ]{3,}` — FOUR characters
    # minimum — so EVERY SURNAME OF THREE LETTERS OR FEWER IS INVISIBLE TO THE REUSE CHECK,
    # silently, with no bucket and no count. Found Day 187 at II.7, when `Zeh` did not appear
    # in a **Named:** field that plainly contains him. Relaxing the pattern to {2,} would drag
    # in every sentence-initial Not/And/One, so the short names are carried here by hand — and
    # the honest cost of that is that the list is only as complete as the last person to
    # notice. Any future ancestor with a short surname must be added here or it does not exist
    # to this gauge.
    "Zeh": "Zeh",
}


# The scaffold's HOUSE VOCABULARY FOR PROCEDURE — how a beat operates, never what it claims.
# "stated at full strength, credited, and then cut" is the book's standard move against an
# ancestor and appears wherever an ancestor is cut, which is everywhere. A pair whose entire
# shared vocabulary is drawn from this set shares a METHOD, not a thesis. This is a narrow
# filter on a known vocabulary, not a threshold widened until the noise stopped.
METHOD = set("""stated state case front full strength openly flatly plainly credited cut cuts
first once beat beats chapter chapters book books said say says made make makes work worked
named names naming arrives arrive given give stating claim claims""".split())


def chapters(text):
    """[(id, title, joined_body)] — body joined so a hard wrap cannot hide a needle."""
    out, cur, buf = [], None, []
    for line in text.splitlines():
        m = CHAPTER_RE.match(line)
        if m:
            if cur:
                out.append((cur[0], cur[1], " ".join(buf)))
            cur, buf = (m.group(1), m.group(2)), []
        elif cur is not None:
            if line.startswith("## ") or line.startswith("# "):
                out.append((cur[0], cur[1], " ".join(buf)))
                cur, buf = None, []
            else:
                buf.append(line.strip())
    if cur:
        out.append((cur[0], cur[1], " ".join(buf)))
    return out


def beats(body):
    """The moves a chapter claims, as strings. Thesis counts as a beat — it is the one the
    II.2/III.4 collision was hiding in."""
    out = []
    # **Thesis:** … up to the next bold field label
    for m in re.finditer(r"\*\*Thesis:?\*\*(.*?)(?=\*\*(?:Beats|Named|Source|Why|Register)|$)",
                         body, re.IGNORECASE):
        out.append(("thesis", m.group(1)))
    for m in re.finditer(r"\*\*Beats:?\*\*(.*?)(?=\*\*(?:Named|Source|Why|Thesis|Register)|$)",
                         body, re.IGNORECASE):
        chunk = m.group(1)
        # Two scaffold dialects: numbered lists (Book I, III.1, III.2) and ·-separated runs.
        if re.search(r"(?:^|\s)\d\.\s", chunk):
            parts = re.split(r"(?:^|\s)\d{1,2}\.\s", chunk)
        else:
            parts = chunk.split("·")
        out.extend(("beat", p) for p in parts)
    return [(k, t.strip()) for k, t in out if len(t.strip()) > 25]


def named(body):
    """The chapter's **Named:** roster, as bare surnames/terms. The second gauge, and it
    catches a class the Jaccard cannot: two chapters CUTTING AGAINST THE SAME OPPONENT.
    Bostrom is cut three times by design and the scaffold demands a new axis each time; a
    name that turns up twice with no such note is an unplanned repeat, and the reader meets
    the same argument twice with no idea which one was the real one."""
    # ⚠ THE TERMINATOR LIST IS THE WHOLE GAUGE. Day 187, at II.7: a **Named:** field followed
    # by ruling prose ran on until the next Beats/Source/Thesis/Why/Register — and since a
    # chapter's rulings come AFTER its fields, it slurped every ⚠ note in the chapter and
    # reported the tool's own name as an ancestor. A field ends where the next MARKER begins,
    # and ⚠ / ★ / **RULING are markers. An unterminated field is not a big field; it is a
    # field that has stopped being one.
    # ⚠⚠ AND THE FIRST VERSION OF THIS FIX WAS ANCHORED ON `\n\s*[⚠★]` — A NEWLINE THAT CANNOT
    # EXIST HERE, because `chapters()` hands this function the body ALREADY JOINED. It matched
    # nothing, the field ran on exactly as before, and the run still looked fixed. That is the
    # standing gauge note — *every instrument here is written against prose-as-a-string and the
    # manuscript is prose-as-lines* — walked into inside the hour it was quoted. The markers are
    # real; they are just not at line starts by the time anything reads them. Anchor on the
    # MARKER, never on the line.
    chunks = [m.group(1) for m in re.finditer(
        # ⚠ AND THE SECOND VERSION OVER-CORRECTED: terminating on a bare `★` cut 8 OTHER
        # chapters' Named fields off at their first emphasis marker and dumped them into the
        # lowercase bucket (6 → 14) — a gauge "fix" that made the reading worse in a direction
        # that reads as MORE alarm, so it would have looked like diligence. `⚠` only ever
        # opens a note; `★` is used inside Named fields for emphasis and cannot terminate.
        r"\*\*Named[^:]*:?\*\*(.*?)(?=\*\*(?:Beats|Source|Thesis|Why|Register|RULING|Boundary"
        r"|Gauge|Touches|Axis|Note)|⚠|$)",
        body, re.IGNORECASE)]
    return _names_in(chunks)


def _names_in(chunks):
    out = set()
    for raw in chunks:
        chunk = re.sub(r"\*\(.*?\)\*", " ", raw)
        chunk = re.sub(r"\([^)]*\)", " ", chunk)
        # NEGATED NAMINGS. Found Day 187 by the gauge printing "Bostrom cut in 2: II.1, II.3"
        # off II.3's own boundary note, which says *"II.3 does not name Bostrom."* A negation
        # read as an assertion — and a false line that prints every run is the boot-banner
        # failure again. Narrow: a name inside a does-not-name clause is not a naming.
        chunk = re.sub(r"(?:does not name|is not named|never named|not named in|unnamed)"
                       r"[^.·]{0,60}", " ", chunk, flags=re.IGNORECASE)
        # ★ WIDENED Day 187, at II.7, by the gauge acquitting II.8 on the word `Gnosticism`
        # taken out of the sentence *"AND THIS CHAPTER STILL HAS NO NAMED ANCESTOR OR
        # OPPONENT ... wants Gnosticism named."* THE SENTENCE DECLARING THE GAP IS WHAT CLOSED
        # IT. That is yesterday's exculpatory-bucket lesson arriving inside the fix for
        # yesterday's exculpatory-bucket lesson, and it was caught only because that fix made
        # the bucket SHOW ITS WORK — an acquittal you can read is an acquittal you can
        # disagree with. Widened to the whole family of gap-declarations: a chapter's own
        # complaint that it lacks a name is not evidence that it has one.
        chunk = re.sub(r"(?:has no named|have no named|no named ancestor|no named opponent|"
                       r"still has no|wants\b|owes\b|would want|rule 5 says)"
                       r"[^.·]{0,80}", " ", chunk, flags=re.IGNORECASE)
        for tok in re.findall(r"[A-Z][a-zà-ÿ]{3,}(?:\s+[A-Z][a-zà-ÿ]{3,})?|`[^`]+`", chunk):
            t = tok.strip("` ")
            # ★ Day 187, at II.7: `beat_sweep` was reported as an ANCESTOR CUT IN TWO
            # CHAPTERS (II.5, II.7) — the gauge finding itself in the ruling prose that
            # discusses it. An identifier is never a person. `_outside_names` had this filter
            # and the reuse path did not, which is the same defect as ruling 31 one floor
            # down: a rule stated in one place and implemented in one of the two that need it.
            if "_" in t or "/" in t or t.endswith(".py"):
                continue
            # drop sentence-initial prose capitals that are not names
            if t.split()[0] in {"The", "Named", "Every", "Read", "Where", "This", "Book",
                                "Beats", "Quarry", "Rule", "Full", "Day", "Present", "Same",
                                "That", "What", "Their", "Both", "Added", "Because"}:
                continue
            if t.isdigit():          # `03`, `05` — file references, not people
                continue
            out.add(ALIASES.get(t, t))
        # the acronyms the pattern above cannot see at all
        for token, canon in ALIASES.items():
            if re.search(rf"(?<![A-Za-z]){re.escape(token)}(?![A-Za-z])", chunk):
                out.add(canon)
    return out


# TOKENS THAT ARE OURS. A capitalised word in a chapter body is not evidence of an ancestor
# when it is one of the scaffold's own field labels, one of the lexicon's house terms, or the
# book pointing at its own source material. Rule 5 asks whether an OUTSIDE party is on the
# page; self-citation is the opposite of that, and `00` ruling 8 bans it from the prose
# outright. Deliberately over-inclusive: a term wrongly listed here can only push a chapter
# INTO the loud bucket, where it gets read. The failure this list exists to prevent is silent.
OURS = set("""Source Sources Tier Thesis Beats Named Register Why Quarry Touches Note Boundary
Axis Beat Chapter Book Part Front Coda Ruling Rulings Status Named Measurement Hole Cut
Ground Fullness Focusing Narrowing Perspective Perspectives Grade Grades Tunnel Tunnels
Collapse Return Coherence Principle Render Renders Seed Player Still Game Null Space Theorem
Promethean Configuration Library Research Unreleased Work Corpus Atlas Meridian Drift
Nearly Said Consider Promoted Retitled Otherwise Outside Ours Grant Name Base Cartographers
State New Old Same Next Last One Two Three Four Five Six Seven Eight Nine Ten
respawn save level quest sandbox""".split())


def _outside_names(body):
    """The names in a body that belong to somebody ELSE. Feeds the rule-5 exoneration only —
    the reuse check keeps using `named()`, whose **Named:** field already supplies the context
    this filter has to supply by hand. Multi-word tokens are split, because the two-word arm of
    the name pattern produces things like 'State Bostrom' where the ancestor is one of the two."""
    out = set()
    for tok in _names_in([body]):
        if "/" in tok or "." in tok or "_" in tok:   # a path is the book citing itself
            continue
        keep = [w for w in tok.split() if w not in OURS]
        if keep:
            out.add(" ".join(keep))
    return out


def named_report(chs):
    roster = {}
    for cid, _, body in chs:
        for n in named(body):
            roster.setdefault(n, []).append(cid)
    # RULE 5 is non-optional: every chapter carries a named ancestor or opponent. A chapter
    # with no **Named:** field is also INVISIBLE to the reuse check above — which is how the
    # under-report becomes the finding rather than a quiet zero.
    # PRESENCE of the field, not extractability of a name from it. The first version of this
    # check reported 56 of 68 chapters bare, because II.3's opponent is the lowercase phrase
    # *"it's all just perspective"* and II.4's is `IIT` — both real Named lines with nothing
    # capitalised to grab. A gauge that cries 56 is a gauge nobody reads twice.
    has_field = re.compile(r"\*\*Named", re.IGNORECASE)
    bare = [cid for cid, _, body in chs
            if not has_field.search(body) and not cid.startswith("C.")]
    # Book I's header rule FORBIDS a named opponent on the page; its ancestor is carried in
    # the book header and acknowledged in the coda. Counting those as violations would make
    # the number a lie in the direction of alarm.
    bare = [c for c in bare if not c.startswith("I.")]
    body_of = {cid: body for cid, _, body in chs}
    # ★★ THE EXCULPATORY BUCKET NEEDS A STRICTER GATE THAN THE ALARMING ONE.
    # Found Day 187, drafting II.6, by asking the `--` line WHO it had found. It had found
    # `Perspective` — our own prior volume, in the chapter's **Source:** line — and on that
    # basis excused II.6 from rule 5 with the words "hygiene, not a rule-5 gap". Sixteen of
    # the twenty-eight were excused the same way: by a field label (Source, Tier, Thesis), by
    # a path (`atlas_entries_*.md`), or by one of OUR OWN house terms (the Ground, the Return,
    # the Coherence Principle, the Null-Space Theorem). The book citing itself was being read
    # as the book naming an ancestor, which is the precise inverse of what rule 5 is for.
    # The general shape, and it is why this is filed as a lesson rather than a typo: the `!!`
    # bucket errs toward ALARM and is therefore safe to build loosely — a false cry gets
    # checked and dismissed. The `--` bucket errs toward SILENCE. A false exoneration is never
    # checked by anyone, because nothing asks to be. So an exculpatory bucket must (a) gate
    # harder than the accusing one and (b) SHOW ITS WORK — print the name it acquitted on, so
    # the acquittal can be disagreed with. It could not, before this.
    inline_names = {c: _outside_names(body_of[c]) for c in bare}
    inline = [c for c in bare if inline_names[c]]
    unnamed = [c for c in bare if c not in inline]
    if inline:
        print(f"  -- {len(inline)} chapter(s) name their ancestor INLINE in the beats, not in the")
        print(f"     field — hygiene, not a rule-5 gap. The name each was acquitted on:")
        for c in inline:
            print(f"        {c:8} {', '.join(sorted(inline_names[c]))}")
        print()
    if unnamed:
        print(f"  !! {len(unnamed)} chapter(s) have NO named ancestor or opponent anywhere —")
        print(f"     rule 5 says that is non-optional: {', '.join(unnamed)}")
        print()
    # Named-but-unextractable: has the field, nothing capitalised in it. NOT a defect — it is
    # the reuse check declaring its own blind spot instead of scoring a silent zero.
    opaque = [cid for cid, _, body in chs
              if has_field.search(body) and not named(body) and not cid.startswith("C.")]
    if opaque:
        print(f"  -- {len(opaque)} chapter(s) name a lowercase opponent, invisible to the reuse")
        print(f"     check by construction: {', '.join(opaque)}")
        print()

    repeats = {n: c for n, c in roster.items() if len(c) > 1}
    if not repeats:
        print("  no opponent is cut in more than one chapter.")
        return len(bare)
    # An adjudicated repeat must print as ANSWERED, not as a question. Otherwise every run
    # re-asks a settled question, and a gauge that re-asks settled questions is one nobody
    # reads — the 56-of-68 lesson, arriving in the other half of the same file.
    open_ = 0
    for n, cids in sorted(repeats.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        note = None
        for a, b in itertools.combinations(sorted(set(cids)), 2):
            hit = EXEMPT.get((a, b)) or EXEMPT.get((b, a))
            if hit:
                # ⚠ Day 187 — EXEMPT HAS TWO CONSUMERS AND stale_exemptions() SHIPPED KNOWING
                # ABOUT ONE. Its first run called II.8~III.1, II.4~IV.6 and II.5~VI.7 stale while
                # THIS check was printing them ANSWERED nine lines further down the same output.
                # A staleness check that reads one of two call sites reports the other's live
                # entries as dead — an over-accusing gauge, which is the 56-of-68 failure again
                # and in the very function written to stop a silencer going unexamined.
                # Caught by reading the new tool's output against the rest of its own run.
                FIRED_BY_REUSE.add(tuple(sorted((a, b))))
            note = note or hit
        if note:
            print(f"  {n:<28} cut in {len(cids)}: {', '.join(cids)}  — ANSWERED")
            print(f"  {'':<28} {note[:96]}…")
        else:
            open_ += 1
            # ⚠ Day 187 — THE LABEL USED TO READ "NO AXIS STATED", WHICH IS A CLAIM ABOUT THE
            # SCAFFOLD THIS TOOL NEVER CHECKS. The only thing consulted is EXEMPT, three lines
            # up. `Gnosticism II.8/III.1` and `Bostrom II.1/III.1` both had their axes stated in
            # full, in prose, in `06`, and were accused anyway. An accusing bucket that overstates
            # what it looked at is the exoneration lesson wearing the other coat — and the fix for
            # the accusing side is the same: SAY WHAT YOU CHECKED.
            # ★ OWED: read the axis out of the scaffold prose instead of a hand-kept table. Filed.
            print(f"  {n:<28} cut in {len(cids)}: {', '.join(cids)}  "
                  f"?? NOT IN THIS TOOL'S EXEMPT TABLE — `06` may already state the axis")
    print()
    print("  Each repeat needs a NEW AXIS stated in the scaffold, per II.2's Bostrom note.")
    print("  A repeat with no axis note is the reader meeting one argument twice.")
    return open_


def words(s):
    s = re.sub(r"\*\(.*?\)\*", " ", s)                 # editorial asides in italic parens
    s = re.sub(r"[*_`★⚠→←↔]", " ", s)
    s = re.sub(r"\([^)]*\)", " ", s)                   # remaining parentheticals
    s = s.lower()
    toks = re.findall(r"[a-zà-ÿ]+", s)
    return [t for t in toks if t not in STOP and len(t) > 2]


def score(a, b):
    """Jaccard on content words. Symmetric, size-aware, and it does NOT reward a long beat
    for containing a short one — the containment metric fires on every 'the definition'."""
    sa, sb = set(a), set(b)
    if len(sa) < 4 or len(sb) < 4:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def grams(toks, n=NGRAM):
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def sweep(text, focus=None, quiet=False):
    chs = chapters(text)
    if not chs:
        print("!! no chapters parsed — the scaffold's heading format changed")
        return None
    index = []
    for cid, title, body in chs:
        for kind, t in beats(body):
            w = words(t)
            # ⚠ THE ADMISSION FLOOR WAS 4 AND THAT IS WHERE THE NEEDLE ACTUALLY DIED.
            # A beat whose entire content is one trigram — II.4's *"a grade is a position, not
            # a permission"*, three content words after normalisation — never entered the index,
            # so NO discriminator could reach it, including the trigram discriminator built
            # for three-content-word cases. The docstring below says in as many words that the
            # case that matters has "only THREE content words"; the gate two lines up threw
            # those away before it ran. **The instrument excluded its own design case.**
            # Admit at 3; `score()` keeps its own floor at 4, so a short beat still cannot
            # produce a noisy Jaccard — it is reachable only by the exact-phrase discriminators,
            # which is the correct treatment for a beat that IS a phrase.
            if len(w) >= 3:
                index.append((cid, title, kind, t, w, grams(w)))

    hits = []
    for (ca, _, ka, ta, wa, ga), (cb, _, kb, tb, wb, gb) in itertools.combinations(index, 2):
        if ca == cb:
            continue
        if focus and focus not in (ca, cb):
            continue
        s = score(wa, wb)
        shared = ga & gb
        if s < SOFT and not shared:
            continue
        hits.append((max(s, HARD if shared else s), s, shared, ca, ka, ta, cb, kb, tb))

    # RARE TRIGRAM. The Jaccard is a bag of words and the 5-gram wants a quoted sentence;
    # between them sits the case that actually matters — II.3's "a place where the world
    # happens" against III.1's "the place a world happens". Same move, nine words apart,
    # 0.14 on the Jaccard, and only THREE content words survive normalisation, so the
    # 5-gram cannot reach it. A content-word trigram appearing in exactly two chapters is
    # not a coincidence in a book whose beats are this compressed.
    tri = {}
    for cid, _, kind, t, w, _ in index:
        for g in grams(w, 3):
            tri.setdefault(g, set()).add(cid)
    # ⚠⚠ `== 2` WAS THE BUG, AND IT IS THE THIRD TIME THIS FILE'S OWN NORMALISATION HID THE
    # NEEDLE. A trigram in THREE chapters fell out of `rare` entirely, so the discriminator
    # built for the subtle case went blind precisely when the defect got WORSE. Measured on
    # Day 187: *"grade position permission"* sits in I.4, II.4 and VII.2 — and the sweep had
    # been printing it as the PAIR I.4 ~ VII.2, because II.4's beat is three content words and
    # dies on the Jaccard's `len(sa) < 4` floor. **The pair it reported was never a pair. It
    # was a triple with its middle term missing**, and the middle term is the one that decides
    # what the other two are allowed to say.
    #
    # The widening is not a threshold retreat and the cost is measured rather than asserted:
    # across 238 beats there is EXACTLY ONE trigram in three or more chapters, and it is that
    # one. `>= 2` costs one line on the current scaffold. `== 2` cost the finding.
    rare = {g: cs for g, cs in tri.items() if len(cs) == 2}
    spread = {g: cs for g, cs in tri.items() if len(cs) >= 3}
    seen = {(h[3], h[6]) for h in hits} | {(h[6], h[3]) for h in hits}
    for g, cs in rare.items():
        ca, cb = sorted(cs)
        if (ca, cb) in seen:
            continue
        if focus and focus not in (ca, cb):
            continue
        ta = next(t for c, _, _, t, w, _ in index if c == ca and g in grams(w, 3))
        tb = next(t for c, _, _, t, w, _ in index if c == cb and g in grams(w, 3))
        hits.append((HARD, score(words(ta), words(tb)), {g}, ca, "beat", ta, cb, "beat", tb))
        seen.add((ca, cb))

    hits.sort(key=lambda h: -h[0])
    return chs, index, hits, spread


def spread_report(spread, focus=None):
    """A move made in THREE OR MORE chapters. Never a pair — a spread is a different object,
    and reporting it as pairs is what let the grade sentence read as a two-way split for a day."""
    rows = []
    for g, cs in spread.items():
        if focus and focus not in cs:
            continue
        rows.append((sorted(cs), " ".join(g)))
    if not rows:
        return 0
    print()
    print("TRIGRAM SPREAD — the same move in three or more chapters")
    print("  Not a pair. A three-way split needs THREE stated jobs, and the middle one is")
    print("  where the other two get their licence.")
    for cids, g in sorted(rows, key=lambda r: -len(r[0])):
        print(f"  {g:<32} in {len(cids)}: {', '.join(cids)}")
    return len(rows)


# Every consumer of EXEMPT must record what it silenced here, or stale_exemptions() accuses the
# live entries of the consumers it does not know about. There are two today; a third added without
# a line into this set makes the staleness check wrong rather than merely incomplete.
FIRED_BY_REUSE = set()
FIRED_BY_REPORT = set()


def stale_exemptions(fired):
    """EXEMPT entries that silenced nothing this run.

    Built Day 187, ruling 49, and it is a gauge over this file's own silencers rather than over
    the manuscript. Every other check here asks whether the BOOK still holds. This one asks
    whether the RULINGS do.

    An exemption is a permanent, unmonitored mute. It is written on the day a pair collides, it
    records the division of labour that answered the collision, and then it sits here forever —
    still muting, whether or not the division of labour survived. ("II.1","III.1") went false
    inside a week: it said III.1 spends the fork, II.1's prose spent the fork, and this table
    went on exempting the pair on the strength of a sentence that had stopped being true. No
    check in this repo could see it. FABLE saw it, and Fable is an outside reader, not a gauge.

    Two things a stale entry means, and the tool does not guess which:
      · the pair no longer collides, so the adjudication is spent and the entry is dead weight —
        delete it, because a table of dead rules is a table nobody reads (the boot-banner
        lesson, third occurrence in this project);
      · or the pair never collided and the entry was written pre-emptively — in which case it
        is a mute installed against a sound that has not been made, which is worse.

    ⚠ WHAT THIS CANNOT DO, stated so it is not mistaken for cover. This catches an exemption
    whose PAIR went quiet. It CANNOT catch one whose pair still collides while its stated REASON
    has gone false — which is precisely the ("II.1","III.1") case. That one needs a person, or an
    outside reader, and ruling 49 says so rather than letting this function imply otherwise.
    """
    stale = sorted(set(EXEMPT) - fired - FIRED_BY_REUSE)
    if not stale:
        return 0
    print()
    print("STALE EXEMPTIONS — muted a collision that did not happen this run")
    print("  An exemption never expires on its own. Each of these is EITHER a spent ruling to")
    print("  delete OR a mute installed against a sound never made. Decide; do not leave it.")
    for pair in stale:
        print(f"  ?? {pair[0]} ~ {pair[1]}   {EXEMPT[pair][:96]}…")
    print("  ⚠ This check sees SILENCE, not WRONGNESS. An exemption that still fires while its")
    print("    reason has gone false is invisible here — ruling 49, and it is why Fable exists.")
    return len(stale)


def report(chs, index, hits, quiet=False):
    collisions = echoes = exempted = method = 0
    fired = set()
    for rank, s, shared, ca, ka, ta, cb, kb, tb in hits:
        pair = tuple(sorted((ca, cb)))
        note = EXEMPT.get(pair)
        overlap = set(words(ta)) & set(words(tb))
        if overlap and overlap <= METHOD:
            method += 1
            if not quiet:
                print(f"  --    {ca} ~ {cb}  {s:.2f}  METHOD — shares only procedural "
                      f"vocabulary ({', '.join(sorted(overlap))}), no thesis")
            continue
        hard = rank >= HARD
        if note:
            exempted += 1
            fired.add(pair)
            FIRED_BY_REPORT.add(pair)
            if not quiet:
                print(f"  --    {ca} ~ {cb}  {s:.2f}  EXEMPT — {note}")
            continue
        if hard:
            collisions += 1
            print(f"  ** COLLISION **  {ca} ({ka}) ~ {cb} ({kb})   jaccard {s:.2f}"
                  + (f" · shared {NGRAM}-gram: \"{' '.join(next(iter(shared)))}\"" if shared else ""))
        else:
            echoes += 1
            print(f"  ?? ECHO          {ca} ({ka}) ~ {cb} ({kb})   jaccard {s:.2f}")
        print(f"        {ca}: {ta[:150].strip()}")
        print(f"        {cb}: {tb[:150].strip()}")
    print()
    print(f"  {len(chs)} chapters · {len(index)} beats · "
          f"{collisions} collision(s) · {echoes} echo(es) · {exempted} exempt · {method} method")
    if collisions:
        print("  A COLLISION is a QUESTION, not a verdict: two chapters want the same move.")
        print("  Answer it in the scaffold — split the work or absorb the chapter — and add the")
        print("  PAIR to EXEMPT with the ruling that answered it. Do not widen the threshold.")
    return collisions


def selftest():
    """The wrap rule, enforced. A beat broken across a hard wrap must survive parsing."""
    # NB the id must be a REAL id shape — the first draft of this test used "Z.1" and the
    # parser rightly refused it, which is the self-test doing its job on itself.
    doc = ("### IX.1 — A TEST\n**Thesis:** procedural generation is what focusing\n"
           "looks like from inside.\n**Beats:** the seed is not solely yours\nand the world "
           "is not solely given · second beat here for the count\n")
    chs = chapters(doc)
    assert chs, "self-test: no chapter parsed"
    bs = beats(chs[0][2])
    joined = " ".join(t for _, t in bs)
    ok = ("procedural generation is what focusing looks like from inside" in joined
          and "not solely yours and the world is not solely given" in joined)
    print("  wrap self-test:", "PASS — needles survive a hard wrap" if ok else "** FAIL **")
    return 0 if ok else 2


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--chapter", help="show only this chapter's neighbours, e.g. II.3")
    ap.add_argument("--fixture", metavar="REV",
                    help="run against 06-THE-SCAFFOLD.md at a git rev; with the default rev "
                         "this is the calibration and MUST reproduce II.2 ~ III.4")
    ap.add_argument("--selftest", action="store_true", help="the hard-wrap parser test only")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    if args.fixture:
        # The calibration runs the wrap test FIRST. A calibration that passes while the
        # parser is broken is the exact green-run-you-cannot-trust this file exists to refuse.
        rc = selftest()
        print()
        if rc:
            return rc
        raw = subprocess.run(["git", "show", f"{args.fixture}:06-THE-SCAFFOLD.md"],
                             cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if raw.returncode != 0:
            print(f"!! could not read the scaffold at {args.fixture}: {raw.stderr.strip()}")
            return 2
        text = raw.stdout
        print(f"CALIBRATION — scaffold at {args.fixture}, exemptions OFF\n")
        EXEMPT.clear()
        out = sweep(text, focus=args.chapter)
        if out is None:
            return 2
        chs, index, hits, spread = out
        report(chs, index, hits)
        spread_report(spread, focus=args.chapter)
        found = any(tuple(sorted((h[3], h[6]))) == ("II.2", "III.4") for h in hits)
        print()
        if found:
            top = [tuple(sorted((h[3], h[6]))) for h in hits].index(("II.2", "III.4")) + 1
            print(f"  CALIBRATION PASS — II.2 ~ III.4 reproduced, rank {top} of {len(hits)}.")
            return 0
        print("  ** CALIBRATION FAIL ** — the known collision is no longer detected.")
        print("  Fix the detector before trusting any clean run of it.")
        return 2

    print(f"BEAT SWEEP — {SCAFFOLD.name}"
          + (f" · chapter {args.chapter}" if args.chapter else "") + "\n")
    rc = selftest()
    print()
    if rc:
        return rc
    out = sweep(SCAFFOLD.read_text(encoding="utf-8"), focus=args.chapter)
    if out is None:
        return 2
    chs, index, hits, spread = out
    rc = report(chs, index, hits)
    spread_report(spread, focus=args.chapter)
    print()
    print("NAMED-OPPONENT REUSE — who is cut in more than one chapter")
    named_report(chs)
    # ⚠ MUST RUN LAST, AND THIS IS LOAD-BEARING RATHER THAN COSMETIC. It reports what NOTHING
    # silenced, so it cannot run until every consumer of EXEMPT has had its turn. Called from
    # inside report() — where it was first written — named_report() had not run yet, so
    # FIRED_BY_REUSE was empty and three live exemptions were printed as stale. A check on
    # what did not happen is order-dependent in a way a check on what did happen is not.
    stale_exemptions(FIRED_BY_REPORT)
    return 1 if rc else 0


if __name__ == "__main__":
    sys.exit(main())
