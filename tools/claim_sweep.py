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
    ("TERM/narrowing", "all", r"\bnarrowings?\b|\bnarrowed\b|\bthe Narrowing\b",
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
     "Whole-file, and it is the only whole-file exemption in this list."),
    ("prose/SPECIMENS.md", "TERM/narrowing", "all narrowings exist in all states",
     "Clayton's own C17 objection, in his wording. Ruling 13, Day 186."),
    ("prose/SPECIMENS.md", "TERM/narrowing", "If nesting made the narrowing illusory",
     "Quoted contest material — the resisted half of the C17 exchange, kept as evidence."),
    ("prose/SPECIMENS.md", "TERM/narrowing", "narrowing is, and that is the open question",
     "Same exchange, the sentence that named the VII.1 × VIII.6 question."),
]


def exemption_for(path: pathlib.Path, rule_id: str, line: str):
    rel = path.as_posix()
    for suffix, rid, needle, why in EXEMPTIONS:
        if rid == rule_id and rel.endswith(suffix) and (needle is None or needle in line):
            return why
    return None


SCAFFOLD_NAME = "06-THE-SCAFFOLD.md"

CHAPTER_RE = re.compile(r"^### ((?:[IVX]+|C)\.\d+) — (.+?)\s*$", re.MULTILINE)
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
    raise ValueError(f"unknown scope {scope!r}")


def sweep_file(path: pathlib.Path, is_prose: bool):
    uses, mentions, exempt = [], [], []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        print(f"  !! {path.name}: not utf-8, skipped")
        return [], [], []
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

    print("\n  Reminder: this tool reports LINES, not doctrine. A subtle breach walks past it.")
    return 1 if all_uses else 0


if __name__ == "__main__":
    sys.exit(main())
