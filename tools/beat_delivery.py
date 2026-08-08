#!/usr/bin/env python3
"""beat_delivery.py — ruling 98's instrument. Truth and Consequences, Day 187.

WHY THIS EXISTS, and it is the fourth confession in this file family — the first about a
direction rather than a corpus.

  beat_sweep         plan  <-> plan            OK
  prose_beat_sweep   plan  <-> OTHER prose     OK   collision: has this move been SPENT?
  prose_echo         prose <-> prose           OK   repeat: is this said TWICE?
  (nothing)          plan  <-> ITS OWN prose   <--  coverage: was it said ONCE?

Every gauge in this repository hunts REPETITION. Not one of them asks whether a chapter
contains the argument it was planned to make. Asked of the set — the question
`prose_beat_sweep`'s docstring tells you to ask of every gauge here — the answer is that
**omission has no detector at all**, and omission is the worse failure: a repeat is visible to
any reader who gets that far, and a missing argument is visible to nobody except the one reader
who needed it and does not know it was promised.

THE CASE THAT BUILT IT, and it is a real one from the day this file was written. III.7's beat 3
reads *we are not the prisoners of the whole; we are its inhabitants **and co-constituents***.
The first draft delivered *inhabitants* and dropped co-constitution — C10, load-bearing —
entirely. `claim_sweep` passed. `prose_echo` returned zero. `prose_beat_sweep` returned zero
spent, pre-draft and post-draft. **Every instrument in the repo was clean on a chapter missing
one of its four beats**, and it was caught by re-reading the draft against `06` by eye.

They were all clean BY CONSTRUCTION, which is the part worth keeping. `prose_beat_sweep` sweeps
*"every beat of every UNDRAFTED chapter"* — so a beat leaves the measured corpus at the exact
moment its chapter ships, which is the exact moment it first becomes possible to check whether
the prose contains it. The blind region is not an oversight in that tool. It is the shape of
its question.

WHAT IT CHECKS. For every DRAFTED chapter, every beat that chapter claims in `06`, against
that chapter's OWN paragraphs. Two numbers and one list:

  coverage   what fraction of the beat's distinct, non-house content words appear ANYWHERE in
             the chapter. Chapter-level on purpose: a beat may be delivered across four
             paragraphs, and a max-over-paragraphs score would read that as a miss.
  anchor     the single paragraph with the highest containment, so a person has somewhere to
             start reading. It is a pointer, not a verdict.
  MISSING    the beat's words that occur nowhere in the chapter. This is the useful output.
             `coverage 0.71` says nothing a person can act on; `MISSING: co-constituents`
             says exactly where to look.

WHAT IT DELIBERATELY DOES NOT DO — and this is larger here than in the tools next door.

**It reads WORDS.** A beat delivered in different vocabulary reads as missing, and a beat whose
words are all present in scattered unrelated sentences reads as delivered. Both errors are
live. **A low score is a question and a high score is not an answer** — the second half of that
sentence matters more than the first, because a coverage table that reads as a checklist is how
a chapter ships with a beat performed in name only. `--semantic` adds an embedding arm when the
organ is available; it changes the anchor, not the verdict, because there is no verdict.

**It cannot see a beat that was RIGHT TO DROP.** Chapters legitimately supersede their plan —
III.4 cut the draw-distance image on purpose, III.5 moved the MMO beat before a word was
drafted, III.7's own beat 1 was moved by the pre-draft brief because `06` had it wrong. Every
one of those would print here. **The output is a reading list, and the adjudication is a
person's**, exactly as it is for `--brief`.

THE EDITORIAL-TAIL RULE, and it is a real defect this tool would otherwise have. `06`'s beat
lines carry editorial matter after the beat proper — reservations, cross-references, ⚠ notes,
★ flags. Those are instructions to the drafter, not moves the prose owes. Every beat is
therefore truncated at the first ★ / ⚠ / ✅ marker before its words are taken, and the count of
truncations prints, because a silent truncation is how a gauge stops measuring the second half
of what it was pointed at.

USE.

    python tools/beat_delivery.py                 # every drafted chapter, ranked
    python tools/beat_delivery.py --chapter III.7
    python tools/beat_delivery.py --semantic      # add the bge-m3 anchor arm
    python tools/beat_delivery.py --selftest      # MUST detect the case that built it
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from beat_sweep import chapters, beats, words                      # noqa: E402
from prose_beat_sweep import (SCAFFOLD, paragraphs, drafted,       # noqa: E402
                              house, contain, read_disk, embedder, MIN_BEAT)

# The floor is a REPORTING threshold, not a verdict, and it was chosen after the distribution
# was measured on the 21 drafted chapters rather than before. Everything under it prints; the
# lowest ten print regardless, because a run in which nothing crosses a bar teaches nothing.
FLOOR = 0.60
ALWAYS = 10

# The scaffold's editorial markers. A beat's text ends at the first one of these.
TAIL = re.compile(r"[★⚠✅]")

# ★ RULING 108's REPAIR, installed Day 188 at IV.9 after the ruling fired for the THIRD time
# (IV.7, IV.8, IV.9). The tail rule above handles drafter-register that comes AFTER a marker
# and cannot see drafter-register that is INLINE — and inline is where it actually lives:
# `(the out-list holds)`, `looked at from outside`, `used explicitly rather than smoothed`.
# Those are instructions to whoever drafts the chapter. The prose owes them nothing, and every
# one of them scores as a MISS against a chapter that delivered the beat perfectly.
#
# `06` writes in two voices — page content and drafter instruction — and marked NEITHER, so a
# word-reading gauge is obliged to read all of it as content. The fix is not smarter parsing;
# no parser can tell an instruction from a move. It is that the SCAFFOLD must say which voice
# it is in, and guillemets say it: «…» is stripped before the words are taken.
#
# Guillemets rather than braces or parentheses because both of those already occur in beat
# lines as content, and a marker that collides with content is a marker that deletes moves the
# prose really does owe. Measured before choosing: 0 occurrences of « in `06`.
#
# The count PRINTS, on the same principle as the truncation count directly beneath it: a
# scaffold that can silently exempt itself from its own gauge is worse than no gauge, because
# the drafter who wants a clean score has been handed the pen. What is marked is visible in
# the diff and in the report, and it stays a person's call.
DRAFTER = re.compile(r"«[^»]*»")

# INFLECTIONS. An inflection is NOT a delivery and this tool does not score it as one: the
# match stays exact and coverage does not move by a thousandth. What changes is what a MISS
# TELLS you. `filter` reported missing while `filters` sits in the paragraph printed directly
# beneath it on the NEAR line is the shape of a gauge that gets disbelieved — and a gauge is
# spent the first time it is disbelieved (ruling 107). It has now happened twice in two
# chapters, IV.1's `gates` and IV.2's `filters`, both adjudicated by hand as word-level false
# positives, which is two adjudications spent on the same non-finding. So the near form is
# NAMED and the adjudication is left exactly where it was. Stemming into the match was the
# other available repair and it is the wrong one: it would manufacture false DELIVEREDs, and
# for a tool whose entire output is a list of gaps, a missed gap costs more than a spurious one.
SUFFIXES = ("s", "es", "ed", "d", "ing")


def near_form(w, chap_words):
    """A word present in the chapter that is `w` under an inflection, or None."""
    cands = [w + s for s in SUFFIXES]
    if w.endswith("y"):
        cands += [w[:-1] + "ies", w[:-1] + "ied"]
    if w.endswith("e"):
        cands.append(w[:-1] + "ing")
    if w.endswith("s") and len(w) > 4:
        cands.append(w[:-1])
    return next((c for c in cands if c in chap_words), None)


def beat_text(raw):
    """The move, with the drafter's notes cut off. Returns (text, was_truncated, n_marked)."""
    m = TAIL.search(raw)
    text, cut = (raw[:m.start()], True) if m else (raw, False)
    marked = len(DRAFTER.findall(text))
    return DRAFTER.sub(" ", text).strip(), cut, marked


def measure(scaffold_text, dr, focus=None):
    hv, _ = house(dr)
    chs = {cid: body for cid, _, body in chapters(scaffold_text)}
    rows, truncated, short, marked = [], 0, 0, 0

    for cid, paras in sorted(dr.items()):
        if focus and focus != cid:
            continue
        body = chs.get(cid)
        if body is None:
            print(f"  ⚠ {cid} is drafted and has no entry in 06 — NOT MEASURED")
            continue
        chap_words = set()
        for _, p in paras:
            chap_words |= set(words(p))

        for kind, raw in beats(body):
            text, cut, mk = beat_text(raw)
            truncated += cut
            marked += mk
            bw = [w for w in dict.fromkeys(words(text)) if w not in hv]
            if not bw:
                continue
            # ⚠ NO ADMISSION GATE, and that is a decision made after the gate ate the design
            # case. `prose_beat_sweep`'s MIN_BEAT exists because a four-word beat scores 1.00
            # containment against any paragraph by accident — a real hazard for a COLLISION
            # ratio. It is not a hazard here: this arm's output is the MISSING list, and a
            # short beat makes that list SHARPER, not noisier, because every word counts.
            # III.7 b3 — the beat this tool was built for — carries three admissible words and
            # was dropped by the imported gate on the first run. Short beats are measured,
            # flagged, and their coverage number is marked unreliable rather than withheld.
            if len(bw) < MIN_BEAT:
                short += 1
            present = [w for w in bw if w in chap_words]
            missing = [w for w in bw if w not in chap_words]
            cov = len(present) / len(bw)
            near = {w: n for w in missing if (n := near_form(w, chap_words))}
            anchor = max(paras, key=lambda lp: contain(bw, words(lp[1])))
            rows.append({"ch": cid, "kind": kind, "text": text, "cov": cov,
                         "missing": missing, "near_forms": near, "anchor": anchor,
                         "short": len(bw) < MIN_BEAT})
    return rows, truncated, short, marked


def semantic_anchor(rows, dr):
    fn, note = embedder()
    print(f"  semantic arm: {note}")
    if fn is None:
        return
    for r in rows:
        paras = dr[r["ch"]]
        vecs = fn([r["text"]] + [p for _, p in paras])
        q, rest = vecs[0], vecs[1:]
        best = max(range(len(rest)), key=lambda i: sum(a * b for a, b in zip(q, rest[i])))
        r["sem"] = (paras[best][0], sum(a * b for a, b in zip(q, rest[best])))


def report(rows, truncated, short, marked=0, floor=FLOOR):
    print()
    print("BEAT DELIVERY — 06-THE-SCAFFOLD.md against each chapter's OWN prose")
    print()
    rows.sort(key=lambda r: r["cov"])
    shown = [r for r in rows if r["cov"] < floor][:max(ALWAYS, 1)]
    if len(shown) < ALWAYS:
        shown = rows[:ALWAYS]

    for r in shown:
        flag = "!!" if r["cov"] < floor else "  "
        tag = " · SHORT, coverage unreliable" if r.get("short") else ""
        print(f"  {flag} {r['ch']:>6} ({r['kind']})  coverage {r['cov']:.2f}{tag}")
        print(f"        BEAT  {r['text'][:150]}")
        nf = r.get("near_forms", {})
        miss = ", ".join(f"{w}→{nf[w]}" if w in nf else w for w in r["missing"])
        print(f"        MISS  {miss or '—'}")
        ln, para = r["anchor"]
        print(f"        NEAR  {r['ch']}:{ln}  {para[:130]}")
        if "sem" in r:
            print(f"        SEM   {r['ch']}:{r['sem'][0]}  cos {r['sem'][1]:.3f}")
        print()

    under = sum(1 for r in rows if r["cov"] < floor)
    print(f"  {len(rows)} beat(s) measured across {len({r['ch'] for r in rows})} drafted chapter(s) · "
          f"{under} under the {floor:.2f} reporting floor")
    print(f"  {truncated} beat(s) truncated at an editorial marker · "
          f"{short} under {MIN_BEAT} distinct words — MEASURED ANYWAY, coverage flagged SHORT")
    print(f"  {marked} inline «drafter-register» span(s) stripped before scoring (ruling 108). "
          f"A span marked here is a MOVE THE PROSE NO LONGER OWES — check the diff, not the score.")
    print()
    print("  READ THE `MISS` LINE, not the coverage number. A missing word may have been")
    print("  delivered by a synonym, and a beat at 1.00 may have been performed in name only:")
    print("  this arm reads WORDS. No verdict is offered and none is available. What it")
    print("  narrows is where to look — the adjudication is the same person's it always was.")
    print("  `filter→filters` means the chapter carries an INFLECTION of the missing word and")
    print("  NOT the word. It is not scored as delivered and coverage does not count it; it is")
    print("  printed so a plural can be told from a gap at a glance instead of by hand, twice.")
    return under


def selftest():
    """MUST show the mechanism firing on an omission it did not choose.

    ⚠ THE FIRST VERSION OF THIS TEST WAS BUILT AROUND A NAMED FIXTURE — III.7's
    co-constituents beat, the case that motivated the tool — and it was WRONG TWICE, which is
    worth keeping. (a) The imported MIN_BEAT gate dropped the beat before it could be tested,
    so the test failed for a reason that had nothing to do with detection: a gauge's design
    case dying in an admission gate, one file after reading the warning about exactly that.
    (b) Once admitted, the beat's words were missing from the SHIPPED chapter too, so
    amputating a paragraph moved nothing and the test could not distinguish a working detector
    from a broken one. A fixture pinned to one hand-chosen pair rots with the prose it names.

    So the test is constructed instead of named: take the best-covered beat in the tree,
    amputate every paragraph that carries any of its words, and require coverage to collapse
    and every word to surface in MISSING. It survives any edit to any chapter."""
    text = SCAFFOLD.read_text(encoding="utf-8")
    dr = drafted(read_disk)
    rows, _, _, _ = measure(text, dr)
    if not rows:
        print("!! selftest FAIL — nothing measured")
        return 2

    best = max(rows, key=lambda r: (r["cov"], len(r["text"])))
    bw = [w for w in dict.fromkeys(words(best["text"]))]
    hurt = dict(dr)
    hurt[best["ch"]] = [(ln, p) for ln, p in dr[best["ch"]]
                        if not (set(words(p)) & set(bw))]
    after_rows, _, _, _ = measure(text, hurt, focus=best["ch"])
    after = [r for r in after_rows if r["text"] == best["text"]]

    print(f"  fixture: {best['ch']} ({best['kind']}) — the best-covered beat in the tree")
    print(f"  {best['ch']}: {len(dr[best['ch']])} paragraph(s) → {len(hurt[best['ch']])} after amputation")
    if not after:
        print("  selftest PASS — the beat's chapter has no paragraphs left; nothing to cover it")
        return 0
    a = after[0]
    # Every paragraph carrying any of the beat's words is gone, so nothing can cover it.
    # Coverage must be exactly zero and every admissible word must be listed as missing.
    ok = a["cov"] == 0.0 and a["missing"]
    print(f"  coverage {best['cov']:.2f} whole → {a['cov']:.2f} amputated · "
          f"MISS {len(a['missing'])} word(s)")
    print(f"  selftest {'PASS — the detector fires on an omission' if ok else 'FAIL'}")
    return 0 if ok else 2


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--chapter", help="only this chapter, e.g. III.7")
    ap.add_argument("--floor", type=float, default=FLOOR)
    ap.add_argument("--semantic", action="store_true", help="add the bge-m3 anchor arm")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    text = SCAFFOLD.read_text(encoding="utf-8")
    dr = drafted(read_disk)
    rows, truncated, short, marked = measure(text, dr, focus=a.chapter)
    if not rows:
        print("  nothing measured — is the chapter drafted and present in 06?")
        return 1
    if a.semantic:
        semantic_anchor(rows, dr)
    report(rows, truncated, short, marked, a.floor)
    return 0


if __name__ == "__main__":
    sys.exit(main())
