#!/usr/bin/env python3
"""CITATION-FORWARD GATE — the census a note makes ABOUT THE BOOK, re-counted.

    python tools/citation_forward.py             # gate, with the control first
    python tools/citation_forward.py --selftest  # control only
    python tools/citation_forward.py --all       # print agreeing claims too

WHY THIS EXISTS. `note_binding.py` audits marker->note in both directions and
reports 0 orphans and 0 dangles across 528 endnotes. It is right, and it is
STRUCTURALLY BLIND to the defect this file watches, because the notes in question
exist, are reachable, and are wrong about something else: they point at a SOURCE,
or at a COUNT, rather than at a note.

Three chapters running in Book VIII carried a provenance note that got the
provenance wrong, and each failed a different way:

  R2-047  "`blind spot` occurs eleven times in this manuscript and every one of
          them is in VI.8."      A count measured over ONE CHAPTER, asserted over
          THE VOLUME. VI.8 does carry 11; the manuscript carries 20.
  R2-048  "Robert Anton Wilson, who occurs thirteen times in this book (II.5,
          VI.7)."                NO counting rule yields thirteen, and the address
          list omits two of the chapters.
  R2-058  "Evan Stark ... and the Hassan and Lifton material ... are used in this
          manuscript at VII.3 and VII.4."   The names occur NOWHERE but in that
          sentence. An address list pointing at empty rooms.

  ==> A CENSUS IS THE ONE CLAIM A BOOK CAN CHECK ABOUT ITSELF. <==

Every other claim in this volume needs a reader, an outside source, or a judgement.
`occurs eleven times` needs a grep. It is the cheapest verifiable claim on the page
and it was the only class with nothing watching it. [[feedback_self_generated_denominator]]

  ==> WHAT THIS TOOL DOES NOT DO. <==

It does not decide. It RE-COUNTS and prints the claim beside the measurement, and
it exits 1 when they disagree -- because a disagreement is mechanical and needs no
taste. It cannot tell you whether the right counting rule is the full name or the
surname; it prints BOTH the count including the claiming sentence and the count
excluding it, so the rule is chosen by a human in the open rather than by this file
in silence. Where it cannot extract a subject it says UNREAD and counts that as an
open row, because a claim it could not parse and a claim that checks out must never
print the same. [[feedback_denial_leaves_no_row]]

  ==> AND IT READS UNWRAPPED. <==

The manuscript is hard-wrapped. `relative_ref_sweep.py` was line-scoped for its whole
life and 19 sites were invisible (R2-075); this file reuses that module's paragraph
join rather than repeating the defect three weeks later. [[feedback_line_scoped_grep_over_wrapped_prose]]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from relative_ref_sweep import blocks, _lineno_at, BOOK_DIR   # noqa: E402

NUMBER = {
    "zero": 0, "no": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
}
_NUMWORDS = "|".join(NUMBER)

# The SCOPE word decides what the count is a claim ABOUT, and getting it wrong is
# exactly R2-047: a number true of one chapter, said of the volume.
VOLUME_SCOPE = r"(?:this\s+manuscript|this\s+book|this\s+volume|the\s+manuscript|the\s+volume)"
CHAPTER_REF = r"(?:[IVX]{1,5}\.\d{1,2}|[CZ]\.\d)"

# --- A. COUNT CLAIMS -------------------------------------------------------
# "`blind spot` occurs eleven times in this manuscript"
# "`Sartre` occurred zero times across the fifty-seven chapters before this one"
# ⚠ THE SUBJECT IS BOUNDED, and the bound is the difference between a gate and a
# noise generator. The first version accepted any italic span up to 60 characters,
# and on the live book it adopted a 240-character quotation as a "subject" four
# times in one chapter, then confidently reported the book wrong about it. A gate
# that cries wolf trains its reader to skip it, which is worse than no gate at all
# and is the failure this whole tool family exists to refuse.
_SUBJ = (r"(?P<subj>`[^`\n]{2,40}`"                        # backticked: the good case
         r"|\*[^*\n.;:⛔⚠\"“”]{2,40}\*"                     # short italic, no sentence guts
         r"|(?:[A-Z][\w’'-]+(?:\s+[A-Z][\w’'-]+){0,3}))")  # a proper-name run

# `occurs` is a claim about STRINGS and a grep settles it.
# `is used` is a claim about USE and a grep does not -- Aquinas is NAMED 23 times
# and USED as a source four, and both sentences are true. Those go to a human.
# Pooling the two verbs is how a gate starts reporting sense errors it cannot see,
# which is the same move as counting one chapter and asserting the volume.
_STRING_VERB = r"(?:occurs?|occurred|appears?|appeared|shows?\s+up)"
_SENSE_VERB = r"(?:is\s+used|are\s+used|is\s+spent|are\s+spent|is\s+cited|are\s+cited)"

PAT_COUNT = re.compile(
    _SUBJ + r"[^.;\n]{0,60}?"
    r"\b(?P<verb>" + _STRING_VERB + r"|" + _SENSE_VERB + r")\b"
    r"[^.;\n]{0,40}?"
    r"\b(?P<n>" + _NUMWORDS + r"|\d{1,3})\s+times?\b"
    # ⚠ THE TAIL MUST ADMIT A FULL STOP. It read `[^.;\n]`, and every chapter
    # reference in this book has a period in it — so "occurs eleven times in VI.8"
    # handed back a tail of "in VI", and the scope resolver correctly found no scope
    # in it and printed UNREAD. Ten of fifteen claims went unread over one character,
    # against REPAIRED text. A delimiter that excludes the thing being looked for
    # reports a clean absence. [[feedback_case_sensitivity_scoped_wider_than_its_discriminator]]
    r"(?P<tail>[^;\n]{0,90})")

# --- THE SCOPE, and it is the whole reason R2-047 was a defect ---------------
# "occurs eleven times" is not a claim until you know eleven times WHERE. The first
# version of this gate counted the volume for every claim and so reported `blind
# spot` wrong at VIII.2 -- against the REPAIRED sentence, which correctly says
# "in VI.8". It committed R2-047's error while checking for it. An unresolvable
# scope is UNREAD; it is never silently taken as the volume.
PAT_SCOPE_VOL = re.compile(r"\b(?:in|across|throughout)\s+" + VOLUME_SCOPE, re.I)
PAT_SCOPE_CH = re.compile(r"\b(?:in|of)\s+(?P<ch>" + CHAPTER_REF + r")\b")
PAT_SCOPE_BEFORE = re.compile(
    r"\b(?:before\s+this\s+(?:one|line|chapter)"
    r"|across\s+(?:the\s+)?[\w-]+\s+chapters?"
    r"|" + VOLUME_SCOPE + r"\s+before\s+this)", re.I)
PAT_SCOPE_SELF = re.compile(r"\bin\s+this\s+chapter\b", re.I)
PAT_SCOPE_DEIXIS = re.compile(r"\b(?:there|here|elsewhere|above|below)\b", re.I)

# --- B. ADDRESS CLAIMS -----------------------------------------------------
# "are used in this manuscript at VII.3 and VII.4"   -> the rooms must not be empty
PAT_ADDR = re.compile(
    r"\b(?:used|spent|cited|sourced|named|introduced|argued|established)\b"
    r"[^.;]{0,50}?\b(?:in|across)\s+" + VOLUME_SCOPE + r"\s+at\s+"
    r"(?P<addr>" + CHAPTER_REF + r"(?:\s*(?:,|and|,\s*and)\s*" + CHAPTER_REF + r")*)")

# --- C. EXCLUSIVITY CLAIMS -------------------------------------------------
# "and every one of them is in VI.8"  /  "and nowhere else"
PAT_ONLY = re.compile(
    r"\b(?:every\s+one\s+of\s+them\s+(?:is|are)\s+in|all\s+of\s+them\s+(?:are|sit)\s+in"
    r"|and\s+nowhere\s+else\s+in\s+" + VOLUME_SCOPE + r")"
    r"\s*(?P<addr>" + CHAPTER_REF + r")?")

STOP_SUBJECTS = {
    # Sentence furniture that the proper-name branch would otherwise adopt as a
    # subject. Kept SHORT on purpose: a long stop-list is a precision filter, and
    # a precision filter here eats recall on real one-word subjects like `Aion`.
    "The", "That", "This", "It", "And", "But", "So", "A", "An", "There", "What",
    "Not", "No", "Both", "Each", "Every", "Its", "His", "Her", "Their",
}


# ⚠ THE ACKNOWLEDGEMENT PATH, and it is the difference between a gate and a siren.
# Four claims in this volume cannot be settled by any grep: a deictic scope ("occurs
# zero times THERE"), a sense verb ("Aquinas is USED four times"), a count over a
# corpus that is not this book ("three times in 884 KB"), and a scopeless count. If
# those keep the exit code at 1 forever, the gate becomes unclearable BY CONSTRUCTION
# and the next reader learns to skip it — which is the failure mode this project
# measured today in a different tool: an alarm branch that is the only branch.
# So an UNREAD claim is OPEN until a human writes its key down, and then it is
# acknowledged rather than fixed, on the record, with a reason.
ACK = BOOK_DIR / "CENSUS-ACK.md"


def acknowledged():
    if not ACK.exists():
        return {}
    out = {}
    for line in ACK.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*-\s*`([^`]+)`\s*—\s*(.+)$", line)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def ack_key(r):
    """Stable across re-wraps: chapter + subject, never the line number. A key that
    carries a line number is invalidated by the next paragraph inserted above it,
    and an ack that silently stops matching reopens as a mystery."""
    return f"{label_of(r['file'])}:{r.get('subject') or '?'}"


CHAPTER_FILE = re.compile(r"^(?:[IVX]+|C|Z)-\d+-")


def chapter_files():
    """⛔ THE CORPUS IS CHAPTERS, NOT `book/*.md`. Writing CENSUS-ACK.md put the
    gate's own adjudications into the book it was auditing: the total went 14 -> 16
    the instant the file was saved, and the gate began re-reading its own quoted
    claims as if the volume made them. A gauge whose output lands inside its own
    subject measures itself. [[feedback_gauge_reachable_from_its_own_subject]]"""
    return sorted(p for p in BOOK_DIR.glob("*.md") if CHAPTER_FILE.match(p.name))


def corpus():
    """{path: unwrapped text}. Unwrapped, because the manuscript is hard-wrapped and
    a subject can straddle a soft break exactly as a reference can."""
    out = {}
    for p in chapter_files():
        joined = " ".join(j for j, _ in blocks(p.read_text(encoding="utf-8",
                                                           errors="replace")))
        out[p] = joined
    return out


def label_of(path):
    m = re.match(r"^([IVX]+|C|Z)-(\d+)-", path.name)
    return f"{m.group(1)}.{int(m.group(2))}" if m else path.stem


def count_term(corp, term, exclude=None, keep=None):
    """Occurrences of `term` per chapter label. `exclude` is a (path, span) whose
    characters are masked out, so the claiming sentence can be counted BOTH ways."""
    pat = re.compile(re.escape(term), 0 if any(c.isupper() for c in term) else re.I)
    per = {}
    for path, text in corp.items():
        if keep is not None and label_of(path) not in keep:
            continue
        if exclude and exclude[0] == path:
            a, b = exclude[1]
            text = text[:a] + (" " * (b - a)) + text[b:]
        n = len(pat.findall(text))
        if n:
            per[label_of(path)] = n
    return per


def reading_order(corp):
    """Linear labels I.1 ... VIII.n, so a 'before this one' scope has an index."""
    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    rows = []
    for path in corp:
        m = re.match(r"^([IVX]+)-(\d+)-", path.name)
        if m and m.group(1) in roman:
            rows.append((roman.index(m.group(1)), int(m.group(2)), label_of(path)))
    return [lbl for _, _, lbl in sorted(rows)]


def resolve_scope(tail, claim_label, order):
    """(kind, arg) or (None, why). The scope is READ, never assumed to be the volume."""
    # ⛔ THE EARLIEST SCOPE WINS, NOT THE FIRST PATTERN TRIED. This function used to
    # test chapter-scope before volume-scope, so R2-047's own defect — *"occurs eleven
    # times IN THIS MANUSCRIPT and every one of them is IN VI.8"* — resolved to VI.8,
    # counted 11, and PASSED. The gate written to catch that sentence exonerated it,
    # because a later clause in the tail outranked the scope the claim actually states.
    # Caught by the end-to-end control, not by the regex asserts. [[feedback_repair_scoped_to_named_cause]]
    # ...but a NARROWING MODIFIER beats position, because it modifies whatever it
    # follows. *"in the manuscript BEFORE THIS LINE"* is one scope, not two: earliest-
    # wins alone read it as the whole volume and reported `philia` wrong at VII.6,
    # where the claim is true. Position decides between two RIVAL scopes (R2-047's
    # manuscript-vs-VI.8); it must not decide between a scope and its own qualifier.
    if PAT_SCOPE_BEFORE.search(tail):
        return "before", claim_label
    cands = []
    for m, kind, arg in (
        (PAT_SCOPE_VOL.search(tail), "volume", None),
        (PAT_SCOPE_SELF.search(tail), "chapter", claim_label),
    ):
        if m:
            cands.append((m.start(), kind, arg))
    mc = PAT_SCOPE_CH.search(tail)
    if mc:
        cands.append((mc.start(), "chapter", mc.group("ch")))
    if cands:
        cands.sort()
        return cands[0][1], cands[0][2]
    if PAT_SCOPE_DEIXIS.search(tail):
        return None, "scope is deictic — 'there'/'here' names a place this file cannot resolve"
    return None, "no scope stated in the sentence"


def scope_labels(kind, arg, order):
    if kind == "volume":
        return None                      # everything
    if kind == "chapter":
        return {arg}
    if kind == "before":
        return set(order[:order.index(arg)]) if arg in order else set()
    return set()


def clean_subject(raw):
    s = raw.strip().strip("`*").strip()
    s = re.sub(r"^(?:the|a|an)\s+", "", s, flags=re.I).strip()
    return s


def scan():
    corp = corpus()
    order = reading_order(corp)
    rows = []
    for path, _ in corp.items():
        text = path.read_text(encoding="utf-8", errors="replace")
        for joined, offs in blocks(text):
            for m in PAT_COUNT.finditer(joined):
                # ⚠ THE NEAREST CANDIDATE WINS, not the leftmost. `re` scans left to
                # right, so *"the Ethics has never been used: `philia` occurs zero
                # times"* handed back `Ethics` — a real subject, the wrong one, and
                # the resulting count was measured against a term the sentence was
                # not talking about. Re-pick the LAST candidate before the verb.
                pre = joined[m.start():m.start("verb")]
                cands = list(re.finditer(_SUBJ, pre))
                subj = clean_subject(cands[-1].group("subj") if cands else m.group("subj"))
                if not subj or subj in STOP_SUBJECTS:
                    rows.append({"kind": "count", "file": path, "verdict": "UNREAD",
                                 "line": _lineno_at(offs, m.start()),
                                 "claim": m.group(0)[:120], "subject": None})
                    continue
                claimed = NUMBER.get(m.group("n").lower())
                if claimed is None:
                    claimed = int(m.group("n"))
                base = {"kind": "count", "file": path,
                        "line": _lineno_at(offs, m.start()),
                        "subject": subj, "claimed": claimed,
                        "claim": m.group(0)[:160]}
                if re.fullmatch(_SENSE_VERB, m.group("verb").strip(), re.I):
                    rows.append({**base, "verdict": "UNREAD", "scope": "—",
                                 "why": "verb is 'used'/'cited' — a claim about USE, "
                                        "not about strings; a grep cannot settle it"})
                    continue
                kind, arg = resolve_scope(m.group("tail"), label_of(path), order)
                if kind is None:
                    rows.append({**base, "verdict": "UNREAD", "scope": "—", "why": arg})
                    continue
                keep = scope_labels(kind, arg, order)
                span = (joined.find(m.group(0)), joined.find(m.group(0)) + len(m.group(0)))
                per_all = count_term(corp, subj, keep=keep)
                per_ex = count_term(corp, subj, exclude=(path, span), keep=keep)
                rows.append({
                    **base,
                    "total": sum(per_all.values()), "total_ex": sum(per_ex.values()),
                    "per": per_all, "verdict": None,
                    "scope": f"{kind}" + (f" {arg}" if arg else ""),
                })
            for m in PAT_ADDR.finditer(joined):
                addrs = re.findall(CHAPTER_REF, m.group("addr"))
                rows.append({"kind": "address", "file": path,
                             "line": _lineno_at(offs, m.start()),
                             "addrs": addrs, "claim": m.group(0)[:160],
                             "sentence": joined[max(0, m.start() - 220):m.end()],
                             "verdict": None})
            for m in PAT_ONLY.finditer(joined):
                rows.append({"kind": "only", "file": path,
                             "line": _lineno_at(offs, m.start()),
                             "addr": m.group("addr"),
                             "claim": m.group(0)[:120],
                             "sentence": joined[max(0, m.start() - 220):m.end()],
                             "verdict": None})
    return corp, rows


def adjudicate(corp, rows):
    """Mechanical verdicts only. AGREES / DISAGREES / UNREAD."""
    for r in rows:
        if r["verdict"] == "UNREAD":
            continue
        if r["kind"] == "count":
            if r["claimed"] in (r["total"], r["total_ex"]):
                r["verdict"] = "AGREES"
            else:
                r["verdict"] = "DISAGREES"
        elif r["kind"] == "address":
            # An address claim is checkable without knowing the subject: the named
            # chapters must carry SOMETHING the claiming sentence names. The subject
            # is taken as every capitalised run in the sentence before the claim.
            names = [n for n in re.findall(r"\b[A-Z][a-z]{3,}\b", r["sentence"])
                     if n not in STOP_SUBJECTS]
            if not names:
                r["verdict"] = "UNREAD"
                continue
            r["names"] = sorted(set(names))
            empty = []
            for a in r["addrs"]:
                found = False
                for path, text in corp.items():
                    if label_of(path) != a:
                        continue
                    if any(re.search(r"\b" + re.escape(n) + r"\b", text) for n in r["names"]):
                        found = True
                if not found:
                    empty.append(a)
            r["empty"] = empty
            r["verdict"] = "DISAGREES" if empty else "AGREES"
        elif r["kind"] == "only":
            names = [n for n in re.findall(r"`([^`]+)`", r["sentence"])]
            if not names or not r["addr"]:
                r["verdict"] = "UNREAD"
                continue
            subj = clean_subject(names[-1])
            per = count_term(corp, subj)
            r["subject"] = subj
            r["per"] = per
            outside = {k: v for k, v in per.items() if k != r["addr"]}
            r["outside"] = outside
            r["verdict"] = "DISAGREES" if outside else "AGREES"
    return rows


def selftest():
    """POSITIVE CONTROL — the three defects that caused this file, as SYNTHETIC text.

    ⚠ Synthetic on purpose. All three are repaired or on their way to being, and a
    control anchored to a live defect set reads green the moment the book becomes
    correct -- which is not the same as the detector working. This project has
    already been bitten by that once, in `endnote_order.py`, the same week.
    """
    # R2-047's original sentence: count + exclusivity, and the count is volume-scoped.
    s047 = ("[^1]: `blind spot` occurs eleven times in this manuscript and every one "
            "of them is in VI.8.")
    m = PAT_COUNT.search(s047)
    assert m, "count claim not matched at all"
    assert clean_subject(m.group("subj")) == "blind spot", \
        f"subject mis-extracted: {m.group('subj')!r}"
    assert NUMBER[m.group("n")] == 11, "number word not read"
    assert PAT_ONLY.search(s047), "exclusivity claim invisible"
    assert PAT_ONLY.search(s047).group("addr") == "VI.8", "exclusivity address lost"

    # R2-048: a bare proper name as subject, and a digit-free number.
    s048 = ("[^2]: Not Robert Anton Wilson, who occurs thirteen times in this book "
            "(II.5, VI.7).")
    m = PAT_COUNT.search(s048)
    assert m, "proper-name subject not matched"
    assert "Wilson" in m.group("subj"), f"proper name lost: {m.group('subj')!r}"
    assert NUMBER[m.group("n")] == 13, "thirteen not read"

    # R2-058: an ADDRESS claim with no number in it at all. The form that carries no
    # count is the one a count-only gate would print a green over.
    s058 = ("Evan Stark on coercive control, and the Hassan and Lifton material on "
            "group capture, are used in this manuscript at VII.3 and VII.4; they are "
            "not re-sourced here.")
    m = PAT_ADDR.search(s058)
    assert m, "address claim with no count is invisible — R2-058's exact shape"
    assert re.findall(CHAPTER_REF, m.group("addr")) == ["VII.3", "VII.4"], \
        "address list mis-parsed"

    # NEGATIVE HALF, and it must be a sentence where right and wrong DISAGREE.
    # Prose that merely contains a number and a chapter must not become a claim.
    quiet = "He spent three years in VII.3 reading the same page."
    assert not PAT_COUNT.search(quiet), "count pattern fires on ordinary prose"
    assert not PAT_ADDR.search(quiet), "address pattern fires on ordinary prose"

    # ...and the counter must actually count, or every verdict above is a green over
    # an instrument that returns nothing. Fixture where the two rules DIFFER.
    class _P:
        name = "VI-08-x.md"
    fake = {_P: "blind spot here, and blind spot again, and blind spot once more"}
    per = count_term(fake, "blind spot")
    assert per == {"VI.8": 3}, f"counter is dead or mislabels chapters: {per}"
    per_ex = count_term(fake, "blind spot", exclude=(_P, (0, 12)))
    assert sum(per_ex.values()) == 2, \
        "exclude-the-claiming-sentence path does not change the count — it tests nothing"

    # --- END TO END, on R2-047's ORIGINAL sentence. -------------------------------
    # The regex asserts above prove the claim is SEEN. This proves the chain reaches
    # DISAGREES, which is a different thing: scope resolution and counting sit between
    # them, and both were wrong in the first draft of this file.
    class _A:
        name = "VI-08-a.md"

    class _B:
        name = "II-05-b.md"
    fake = {_A: "blind spot " * 11, _B: "blind spot once"}
    order_f = reading_order(fake)
    # scope as WRITTEN in the defect: "in this manuscript" -> the volume -> 12, not 11
    kind, arg = resolve_scope("in this manuscript and every one of them is in VI.8",
                              "VIII.2", order_f)
    assert kind == "volume", f"volume scope not read: {kind}"
    got = sum(count_term(fake, "blind spot", keep=scope_labels(kind, arg, order_f)).values())
    assert got == 12 and got != 11, \
        "the chain does not reach DISAGREES on R2-047's original — it is not a gate"
    # ...and the REPAIRED sentence must go the other way, or the control only proves
    # the detector says no to everything.
    kind2, arg2 = resolve_scope("in VI.8. The retinal analogy behind the phrase",
                                "VIII.2", order_f)
    assert kind2 == "chapter" and arg2 == "VI.8", f"chapter scope not read: {kind2} {arg2}"
    got2 = sum(count_term(fake, "blind spot",
                          keep=scope_labels(kind2, arg2, order_f)).values())
    assert got2 == 11, "the repaired sentence does not check out — the gate says no to all"
    # THE QUALIFIER, whose fixture must disagree with the earliest-wins rule or it
    # tests nothing: "in the manuscript" starts EARLIER than "before this line".
    k3, a3 = resolve_scope("in the manuscript before this line. That is the fourth",
                           "VII.6", order_f)
    assert k3 == "before", \
        f"a narrowing qualifier lost to the scope it qualifies: {k3}"
    assert PAT_SCOPE_VOL.search("in the manuscript before this line").start() \
        < PAT_SCOPE_BEFORE.search("in the manuscript before this line").start(), \
        "the qualifier fixture does not actually contest earliest-wins"

    # THE SELF-REFERENCE TRAP. The acknowledgement file lives in book/ and quotes the
    # very claims it adjudicates; if the corpus is `book/*.md` the gate audits itself.
    assert not CHAPTER_FILE.match("CENSUS-ACK.md"), \
        "the gate's own ack file is inside the corpus it audits"
    assert CHAPTER_FILE.match("VIII-02-a-chapter.md"), \
        "the corpus filter is over-broad — it just excluded a real chapter"
    assert all(CHAPTER_FILE.match(p.name) for p in chapter_files()), \
        "a non-chapter file reached the corpus"

    import inspect
    n = sum(1 for ln in inspect.getsource(selftest).splitlines()
            if ln.strip().startswith("assert "))
    print("POSITIVE CONTROL — the three defects that caused this file, synthetic:")
    print("    R2-047  count + exclusivity, volume-scoped   : both caught")
    print("    R2-048  bare proper name, number as a word   : caught")
    print("    R2-058  ADDRESS claim carrying NO number     : caught")
    print("    ordinary prose with a number and a chapter   : silent")
    print("    the counter itself, on a fixture             : counts, and excludes")
    print(f"  [ok] all {n} assertions live (counted from source, not typed).\n")


def main():
    args = sys.argv[1:]
    selftest()
    if "--selftest" in args:
        return 0
    show_all = "--all" in args

    corp, rows = scan()
    rows = adjudicate(corp, rows)

    acks = acknowledged()
    for r in rows:
        if r["verdict"] == "UNREAD" and ack_key(r) in acks:
            r["verdict"] = "ACKED"
            r["ack"] = acks[ack_key(r)]
    bad = [r for r in rows if r["verdict"] in ("DISAGREES", "UNREAD")]
    print(f"CITATION-FORWARD GATE — {len(rows)} self-census claim(s) over "
          f"{len(corp)} file(s)")
    print("  A claim the book makes about its own text. The only class of claim here")
    print("  that a grep can settle, and the only one nothing was watching.\n")

    for r in sorted(rows, key=lambda r: (r["verdict"] != "DISAGREES", str(r["file"]))):
        if r["verdict"] in ("AGREES", "ACKED") and not show_all:
            continue
        mark = {"DISAGREES": "⛔", "UNREAD": "❓", "AGREES": "✅",
                "ACKED": "◻"}[r["verdict"]]
        print(f"  {mark} {label_of(r['file'])}:{r['line']}  [{r['kind']}]")
        print(f"      claim: {r['claim'].strip()}")
        if r["kind"] == "count" and r.get("subject") and "total" in r:
            print(f"      subject `{r['subject']}` · claimed {r['claimed']} · "
                  f"measured {r['total']} in scope [{r['scope']}] "
                  f"({r['total_ex']} excluding this sentence)")
            top = sorted(r["per"].items(), key=lambda kv: -kv[1])[:6]
            print("      where: " + (", ".join(f"{k}×{v}" for k, v in top) or "nowhere"))
        elif r["kind"] == "count":
            print(f"      subject `{r.get('subject')}` · claimed {r.get('claimed')} · "
                  f"NOT COUNTED — {r.get('why', 'subject not extractable')}")
        elif r["kind"] == "address":
            print(f"      names read: {', '.join(r.get('names', []))[:90]}")
            if r.get("empty"):
                print(f"      ⛔ EMPTY ROOM(S): {', '.join(r['empty'])} — the address "
                      f"points where the names do not appear")
        elif r["kind"] == "only" and r.get("subject"):
            print(f"      subject `{r['subject']}` · claimed to sit only in {r['addr']}")
            if r.get("outside"):
                print("      ⛔ ALSO IN: " + ", ".join(
                    f"{k}×{v}" for k, v in sorted(r["outside"].items())))
        print()

    agree = sum(1 for r in rows if r["verdict"] == "AGREES")
    dis = sum(1 for r in rows if r["verdict"] == "DISAGREES")
    unread = sum(1 for r in rows if r["verdict"] == "UNREAD")
    acked = sum(1 for r in rows if r["verdict"] == "ACKED")
    print(f"  {agree} agree · {dis} DISAGREE · {unread} unread "
          f"· {acked} acknowledged by a human in {ACK.name}")
    assert agree + dis + unread + acked == len(rows), "verdict tally does not reconcile"
    if unread:
        print(f"\n  → to clear an ❓ row, add its key to book/{ACK.name}:")
        for r in rows:
            if r["verdict"] == "UNREAD":
                print(f"       - `{ack_key(r)}` — <why a grep cannot settle it>")
    print("\n  ⚠ LIMIT, printed on every run including a clean one: this gate checks")
    print("  ARITHMETIC and ADDRESSES, never sense. It cannot tell you whether the")
    print("  right counting rule is the full name or the surname — R2-048 turned on")
    print("  exactly that, and a human picked it. Both totals are printed so the rule")
    print("  is chosen in the open. A green here means no claim contradicts a grep.")
    print("\n  ⚠ SECOND LIMIT: a claim whose subject this file could not extract is")
    print("  printed ❓ UNREAD and counted OPEN, never folded into the green. An")
    print("  unparsed claim and a checked one must not print the same.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
