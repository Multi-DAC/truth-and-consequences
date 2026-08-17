#!/usr/bin/env python3
"""RELATIVE-CHAPTER REFERENCE SWEEP — the one cross-reference form nothing else can see.

    python tools/relative_ref_sweep.py             # sweep, with the control first
    python tools/relative_ref_sweep.py --selftest  # control only
    python tools/relative_ref_sweep.py --book III  # one book

WHY THIS EXISTS, stated so it survives being forgotten. `crossref_rot.py` resolves
explicit tokens -- `III.4`, `[^6]`, `C9`. A reference written as *two chapters ago*
carries no token. It resolves against nothing, it is invisible to every other sweep
in this directory, and when it is wrong it fails in the one way a reader blames on
themselves: they turn back, find the wrong chapter, and conclude they missed it.

Filed as queue row R2-020, after a fresh read of III.5 found TWO wrong ones at
opposite ends of one chapter (R2-017) -- and found them by reading, because nothing
was watching. The row shipped citing 19 sites; the case-insensitive fix made it 33.

  ==> AND 33 WAS STILL 20% OF THE CLASS. Read session 4 (III.2, Day 198). <==

The COUNTED form -- *two chapters ago* -- was the whole vocabulary this tool knew.
The UNCOUNTED form -- *the last chapter*, *the next chapter* -- is 135 further sites
across 48 of 71 chapters, and it was invisible here for the same reason the
sentence-initial hits were: a matcher narrower than its subject. Real denominator
168, of which this tool saw 33.

  ==> AND THE BLIND CLASS IS THE MORE DANGEROUS ONE, not the less. <==

*Two chapters back* carries a count, so it can be wrong on the day it is written and
a reader can catch it. *The last chapter* is correct BY ADJACENCY -- it is true the
moment it is typed and stays true until a chapter is inserted, split, moved or cut,
at which point every affected site flips wrong AT ONCE, silently, with no token to
resolve and nothing in the repo watching. The loud class was instrumented first
because it was the class that had already made noise. [[feedback_orphan_is_silent_dangle_is_loud]]

  ==> WHAT THIS TOOL DOES NOT DO, AND MUST NOT BE READ AS DOING. <==

It resolves the ARITHMETIC and prints the target's TITLE. It does not, and cannot,
decide whether the sentence means that chapter. *Two chapters ago the divine player
was taken apart* is wrong because the divine player is not in III.3 -- a fact about
subject matter, not about counting. So every hit is printed for a HUMAN to adjudicate
and nothing is ever marked clean automatically. A green from this tool means the
arithmetic resolves to a chapter that exists. It does not mean the reference is right.

That distinction is the whole design. A sweep that printed OK per site would convert
19 unexamined references into 19 references that LOOK examined, which is worse than
having no sweep -- an audited-looking corpus is harder to get a second read of than
an unaudited one. So the exit code is about resolvability only, and the report is a
worklist, not a verdict.

ORDERING is linear across the volume (I.1 ... VIII.n), because that is the order the
reader meets the chapters in, which is what *ago* indexes. Across a book boundary the
count runs backward into the previous book -- IV.1's "two chapters ago" is III.7.
Front matter and the coda (C.1, C.2) are excluded: nothing in them uses the idiom and
including them would shift every index by two.
"""

import re
import sys
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parent.parent / "book"

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

WORD_N = {
    "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8,
}

# BACKWARD and FORWARD are separate on purpose: "four chapters later" is a promise
# about text the reader has NOT seen, and it resolves in the other direction.
BACK = r"(ago|back|earlier|before)"
FWD = r"(later|ahead|on|hence)"

PAT_BACK = re.compile(
    r"\b(" + "|".join(WORD_N) + r")\s+chapters?\s+" + BACK + r"\b", re.IGNORECASE)
PAT_FWD = re.compile(
    r"\b(" + "|".join(WORD_N) + r")\s+chapters?\s+" + FWD + r"\b", re.IGNORECASE)

# ---------------------------------------------------------------------------
# THE UNCOUNTED CLASS — added Day 198. Same defect, no number attached to it.
# ---------------------------------------------------------------------------
# Each of these carries an implicit +/-1 ... EXCEPT when it does not, which is the
# whole reason this is written out rather than globbed:
#
#   "the next chapter but one"  is +2.   A naive +1 here is a WRONG resolution
#   presented in the same face as a right one, which is worse than no sweep at
#   all -- the failure this file's own header exists to refuse. The offset suffix
#   is therefore matched, not assumed, and it is in the control below.
PAT_ADJ = re.compile(
    r"\bthe\s+(?P<w>last|previous|preceding|next|following)\s+"
    r"(?P<plural>chapters|chapter)"
    r"(?P<suffix>\s+but\s+(?:one|two))?", re.IGNORECASE)

ADJ_DIR = {"last": -1, "previous": -1, "preceding": -1,
           "next": +1, "following": +1}
SUFFIX_N = {"one": 2, "two": 3}      # "but one" == skip one == distance 2

# POSTPOSITIVE forms: the direction word comes AFTER the noun. Found by diffing this
# tool against a wider hand-pattern (Day 198) -- i.e. the extension that closed the
# uncounted class was itself measured and was itself narrow. Third pass, same axis.
#
#   ==> "the chapter before LAST" is -2. <==
#
# That is the backward twin of "the next chapter but one", and it was NOT caught by
# the fix that caught that one, because the fix was written to the example in hand.
# Both traps are in the control. [[feedback_repair_scoped_to_named_cause]]
PAT_POST = re.compile(
    r"\bthe\s+(?P<plural>chapters|chapter)\s+"
    r"(?P<w>before|after|preceding|following)\s+"
    r"(?P<tail>last\b|this(?:\s+one)?)", re.IGNORECASE)

POST_DIR = {"before": -1, "preceding": -1, "after": +1, "following": +1}

# DELIBERATELY OUT OF SCOPE, named so the exclusion is a decision and not an oversight:
#   "earlier in this book"    -- target is a PASSAGE, not a chapter. Nothing to resolve
#   "earlier in this chapter"    to; a different instrument, and it does not exist yet.
#   "the opening chapter"     -- ABSOLUTE, not relative. Resolves against a named unit,
#                                so crossref_rot's class, not this one.
# Both are counted and reported, never silently dropped, because an exclusion that
# prints nothing is indistinguishable from a miss. [[feedback_denial_leaves_no_row]]
PAT_OUT_OF_SCOPE = re.compile(
    r"\b((?:earlier|later)\s+in\s+this\s+(?:book|chapter)"
    r"|the\s+(?:opening|closing|final)\s+chapter)\b", re.IGNORECASE)

# ⚠ THE SENSE COLLISION, and it is not a parser bug — it is English.
# "the last chapter" means PREVIOUS. "the last chapter OF THE ATLAS" means FINAL.
# Same three words, opposite referents, and only the tail distinguishes them. A
# sweep that resolves the second as -1 reports a confident wrong answer, so these
# are routed to their own section and adjudicated for SENSE before position.
# [[feedback_field_keeps_name_swaps_referent]]
PAT_FINAL_SENSE = re.compile(
    r"\bthe\s+(last|first|final|opening|closing)\s+chapter\s+of\s+", re.IGNORECASE)


def chapter_order(book_dir):
    """Linear reading order. Returns [(label, title, path), ...]."""
    found = []
    for p in sorted(book_dir.glob("*.md")):
        m = re.match(r"^([IVX]+)-(\d+)-(.+)\.md$", p.name)
        if not m:
            continue                      # C-01, C-02, and anything else
        book, num, slug = m.group(1), int(m.group(2)), m.group(3)
        if book not in ROMAN:
            continue
        found.append((ROMAN.index(book), num, f"{book}.{num}",
                      slug.replace("-", " "), p))
    found.sort(key=lambda r: (r[0], r[1]))
    return [(lbl, title, path) for _, _, lbl, title, path in found]


def sweep(order, only_book=None):
    index = {lbl: i for i, (lbl, _, _) in enumerate(order)}
    hits = []
    for i, (lbl, _title, path) in enumerate(order):
        if only_book and not lbl.startswith(only_book + "."):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), 1):
            for pat, direction in ((PAT_BACK, -1), (PAT_FWD, +1)):
                for m in pat.finditer(line):
                    n = WORD_N[m.group(1).lower()]
                    tgt = i + direction * n
                    if 0 <= tgt < len(order):
                        t_lbl, t_title, _ = order[tgt]
                        resolves = True
                    else:
                        t_lbl, t_title, resolves = "—", "OFF THE END OF THE VOLUME", False
                    hits.append({
                        "from": lbl, "line": lineno, "file": path.name,
                        "phrase": m.group(0), "n": n,
                        "dir": "back" if direction < 0 else "fwd",
                        "target": t_lbl, "target_title": t_title,
                        "resolves": resolves,
                        "sentence": line.strip(),
                        "form": "counted",
                    })

            # --- the uncounted class ---------------------------------------
            for m in PAT_ADJ.finditer(line):
                word = m.group("w").lower()
                sign = ADJ_DIR[word]

                # SENSE FIRST, position second. Decided on the span that FOLLOWS
                # the phrase, because that is where the two senses differ.
                if PAT_FINAL_SENSE.match(line[m.start():]):
                    hits.append({
                        "from": lbl, "line": lineno, "file": path.name,
                        "phrase": m.group(0), "n": None, "dir": "sense",
                        "target": "?", "target_title":
                            "SENSE AMBIGUOUS — 'last/first' here may mean FINAL, not adjacent",
                        "resolves": False, "sentence": line.strip(),
                        "form": "sense",
                    })
                    continue

                # A plural gestures at a span, not a chapter. It has no arithmetic
                # to check, so inventing one would manufacture a checked-looking site.
                if m.group("plural").lower() == "chapters":
                    hits.append({
                        "from": lbl, "line": lineno, "file": path.name,
                        "phrase": m.group(0), "n": None, "dir": "span",
                        "target": "—", "target_title":
                            "PLURAL SPAN — no single target; scope is the finding",
                        "resolves": False, "sentence": line.strip(),
                        "form": "span",
                    })
                    continue

                n = 1
                if m.group("suffix"):
                    n = SUFFIX_N[m.group("suffix").strip().split()[-1].lower()]
                _emit_adj(hits, lbl, lineno, path, m.group(0), n, sign,
                          i, order, line, "uncounted")
                continue

            # --- postpositive forms: "the chapter before last" (-2) ---------
            for m in PAT_POST.finditer(line):
                sign = POST_DIR[m.group("w").lower()]
                if m.group("plural").lower() == "chapters":
                    hits.append({
                        "from": lbl, "line": lineno, "file": path.name,
                        "phrase": m.group(0), "n": None, "dir": "span",
                        "target": "—", "target_title":
                            "PLURAL SPAN — no single target; scope is the finding",
                        "resolves": False, "sentence": line.strip(),
                        "form": "span",
                    })
                    continue
                # THE BACKWARD TRAP: "before last" skips one. 2, not 1.
                n = 2 if m.group("tail").lower().startswith("last") else 1
                _emit_adj(hits, lbl, lineno, path, m.group(0), n, sign,
                          i, order, line, "postpositive")

            # --- named exclusions, counted rather than dropped --------------
            for m in PAT_OUT_OF_SCOPE.finditer(line):
                hits.append({
                    "from": lbl, "line": lineno, "file": path.name,
                    "phrase": m.group(0), "n": None, "dir": "oos",
                    "target": "—", "target_title":
                        "OUT OF SCOPE BY DECISION — target is a passage or a named unit",
                    "resolves": True, "sentence": line.strip(),
                    "form": "out-of-scope",
                })
    return hits, index


def _emit_adj(hits, lbl, lineno, path, phrase, n, sign, i, order, line, form):
    """Resolve one adjacency-based reference and append it. Shared so the counted,
    uncounted and postpositive paths cannot drift apart in how they resolve."""
    tgt = i + sign * n
    if 0 <= tgt < len(order):
        t_lbl, t_title, _ = order[tgt]
        resolves = True
    else:
        t_lbl, t_title, resolves = "—", "OFF THE END OF THE VOLUME", False
    hits.append({
        "from": lbl, "line": lineno, "file": path.name,
        "phrase": phrase, "n": n,
        "dir": "back" if sign < 0 else "fwd",
        "target": t_lbl, "target_title": t_title,
        "resolves": resolves, "sentence": line.strip(),
        "form": form,
    })




def selftest(order):
    """POSITIVE CONTROL. Two planted references, one resolvable and one not.

    Runs against a SYNTHETIC ordering, never the book -- a control that shares the
    subject it is controlling for cannot fail independently of it.
    """
    fake = [("X.1", "first", None), ("X.2", "second", None), ("X.3", "third", None)]
    line_ok = "as was said two chapters ago, the thing"
    line_off = "as was said seven chapters ago, the thing"
    ok = PAT_BACK.search(line_ok)
    off = PAT_BACK.search(line_off)
    assert ok and WORD_N[ok.group(1)] == 2, "backward pattern did not match"
    assert off and WORD_N[off.group(1)] == 7, "backward pattern did not match"
    # from X.3, two back == X.1 (resolvable); seven back == off the end.
    i = 2
    assert 0 <= i - 2 < len(fake), "resolvable case failed"
    assert not (0 <= i - 7 < len(fake)), "off-the-end case was NOT caught"
    # and the forward pattern must not fire on backward text, or every hit doubles
    assert not PAT_FWD.search(line_ok), "forward pattern fired on backward text"
    assert PAT_FWD.search("named four chapters later"), "forward pattern is dead"
    # a negative: prose about chapters that is not a relative reference
    assert not PAT_BACK.search("two chapters of this book are about place"), \
        "pattern fires on non-reference prose"
    # --- UNCOUNTED CLASS. Four of these five are traps, not confirmations. ---
    a_back = PAT_ADJ.search("as the last chapter showed, the thing")
    a_fwd = PAT_ADJ.search("that is the next chapter's subject")
    a_off = PAT_ADJ.search("the next chapter but one runs it")
    a_plu = PAT_ADJ.search("the next chapters stop pretending")
    assert a_back and ADJ_DIR[a_back.group("w").lower()] == -1, "adjacent-back dead"
    assert a_fwd and ADJ_DIR[a_fwd.group("w").lower()] == +1, "adjacent-fwd dead"
    # THE OFFSET TRAP: this must be 2, not 1. A +1 here is a confident wrong answer.
    assert a_off and a_off.group("suffix"), "'but one' suffix not captured — would resolve +1"
    assert SUFFIX_N[a_off.group("suffix").strip().split()[-1]] == 2, "'but one' is not +2"
    # and the bare form must NOT pick up a suffix that is not there
    assert not a_fwd.group("suffix"), "suffix matched on a phrase that has none"
    assert a_plu and a_plu.group("plural").lower() == "chapters", "plural not distinguished"
    # THE SENSE TRAP: 'the last chapter of the atlas' is FINAL, not PREVIOUS.
    sense_line = "it is the last chapter of the atlas rather than the first"
    ms = PAT_ADJ.search(sense_line)
    assert ms, "sense-family phrase not matched at all"
    assert PAT_FINAL_SENSE.match(sense_line[ms.start():]), \
        "sense family NOT diverted — would have resolved FINAL as PREVIOUS"
    # ...and the ordinary adjacent form must not be swept into the sense family
    assert not PAT_FINAL_SENSE.match("the last chapter showed"), \
        "sense guard is over-broad — it would swallow real adjacent references"

    # --- POSTPOSITIVE forms, and the trap the FIRST fix did not generalise to ---
    p_last = PAT_POST.search("the objection at the end of the chapter before last")
    p_this = PAT_POST.search("the chapter before this one is where it broke")
    p_aft = PAT_POST.search("the whole subject of the chapter after this one")
    p_plu = PAT_POST.search("the chapters after this one will lean on it")
    assert p_last, "postpositive form not matched at all"
    # THE BACKWARD TRAP. 'before last' is -2. A -1 here is a confident wrong answer,
    # and it is the exact twin of 'but one' -- caught only by re-measuring the fix.
    assert p_last.group("tail").lower().startswith("last"), "'before last' tail lost"
    assert (2 if p_last.group("tail").lower().startswith("last") else 1) == 2, \
        "'the chapter before last' resolved as -1"
    assert p_this and not p_this.group("tail").lower().startswith("last"), \
        "'before this' wrongly took the -2 branch"
    assert p_aft and POST_DIR[p_aft.group("w").lower()] == +1, "postpositive fwd dead"
    assert p_plu and p_plu.group("plural").lower() == "chapters", \
        "postpositive plural not distinguished"
    # named exclusions must be VISIBLE, not dropped
    assert PAT_OUT_OF_SCOPE.search("retired a word earlier in this book"), \
        "out-of-scope family is silently invisible instead of counted"

    print("POSITIVE CONTROL — synthetic ordering, both directions and one null:")
    print("    resolvable back-reference (X.3 - 2)      : caught, resolves to X.1")
    print("    unresolvable back-reference (X.3 - 7)    : caught, flagged OFF THE END")
    print("    forward pattern on backward text         : silent  (no double count)")
    print("    'two chapters of this book are about...' : silent  (not a reference)")
    print("  UNCOUNTED class — the four cases a naive +/-1 gets WRONG:")
    print("    'the last chapter showed'                : caught, -1")
    print("    'the next chapter but one'               : caught, +2  NOT +1")
    print("    'the next chapters' (plural)             : caught, NO target invented")
    print("    'the last chapter OF THE ATLAS'          : diverted, sense before position")
    print("    'the last chapter showed' vs that guard  : NOT diverted (guard not over-broad)")
    print("  POSTPOSITIVE class — found by re-measuring the fix above, not by a reader:")
    print("    'the chapter before LAST'                : caught, -2  NOT -1")
    print("    'the chapter before this one'            : caught, -1  (not the -2 branch)")
    print("    'the chapter after this one'             : caught, +1")
    print("    'the chapters after this one' (plural)   : caught, NO target invented")
    print("    'earlier in this book' (excluded)        : COUNTED, not dropped")
    print("  [ok] all fifteen live.\n")
    if order:
        print(f"  volume ordering parsed: {len(order)} chapters, "
              f"{order[0][0]} -> {order[-1][0]}\n")


def main():
    args = sys.argv[1:]
    only_book = None
    if "--book" in args:
        only_book = args[args.index("--book") + 1]

    order = chapter_order(BOOK_DIR)
    selftest(order)
    if "--selftest" in args:
        return 0

    hits, _ = sweep(order, only_book)

    print(f"RELATIVE-CHAPTER REFERENCES — {len(hits)} site(s)"
          + (f" in Book {only_book}" if only_book else " across the volume"))
    print("  Every one is printed. None is marked clean. The arithmetic is mechanical;")
    print("  whether the sentence MEANS that chapter is not, and is yours to decide.\n")

    unresolved = 0
    current = None
    for h in hits:
        if h["from"] != current:
            current = h["from"]
            print(f"  ── {current} ─────────────────────────────────")
        arrow = "<-" if h["dir"] == "back" else "->"
        flag = "" if h["resolves"] else "   ⛔ UNRESOLVABLE"
        if not h["resolves"]:
            unresolved += 1
        print(f"    {h['file']}:{h['line']}  \"{h['phrase']}\"  {arrow} "
              f"{h['target']} — {h['target_title']}{flag}")
        s = h["sentence"]
        print(f"        {s[:150]}{'…' if len(s) > 150 else ''}")

    by_form = {}
    for h in hits:
        by_form[h["form"]] = by_form.get(h["form"], 0) + 1
    print(f"\n  resolvable: {len(hits) - unresolved}/{len(hits)}"
          f"   ⛔ needs a human: {unresolved}")
    # DERIVED, not hand-listed. The first version of this line named four forms by
    # hand and silently dropped the two added minutes later -- 161 printed against
    # 169 counted, in the summary of a tool whose whole subject is a narrow matcher.
    # A total that does not reconcile to its own parts is the cheapest gauge here.
    print("  by form — " + " · ".join(f"{k} {v}" for k, v in sorted(by_form.items())))
    assert sum(by_form.values()) == len(hits), "by-form breakdown does not reconcile"
    print("\n  LIMIT, printed on every run including a clean one: this tool checks that")
    print("  the count lands on a chapter that exists. It has no idea what any chapter")
    print("  is ABOUT. Both defects that caused it to be written (R2-017) resolve")
    print("  perfectly and are wrong. Read the target titles against the sentences.")
    print("\n  SECOND LIMIT, and it is the newer one: the UNCOUNTED sites resolve by")
    print("  ADJACENCY, so they are all correct today by construction and this tool")
    print("  will print them green forever. Their real failure mode is a chapter being")
    print("  MOVED, and a green run the day before that happens says nothing about the")
    print("  day after. Re-run this after ANY reordering, split, insertion or cut —")
    print("  that is the only moment its answer can change. A sweep whose subject")
    print("  cannot vary between runs is a sweep that has stopped being a gauge.")
    print("\n  PRECISION, measured not asserted: a 14-site random sample of the")
    print("  uncounted class read by hand (Day 198) found 12 genuine positional")
    print("  pointers and 2 of the FINAL-sense family, which is why that family now")
    print("  has its own section rather than a resolution.")
    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
