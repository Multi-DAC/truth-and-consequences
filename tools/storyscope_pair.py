#!/usr/bin/env python3
"""
storyscope_pair.py — score named prose files against each other, WITH coverage.

Two things storyscope_lite.py does not do, both of which bit on Day 186:

  1. COVERAGE. paragraphs() silently drops anything under 25 words. In Specimen 1-B that was
     42% of the paragraphs — the short beats, which are the whole point of speaking voice —
     and the tool printed a clean dyn_range number computed on 58% of the text with no hint
     that it had looked away. Here every metric carries its coverage, and anything computed on
     less than COVERAGE_FLOOR of the words prints as VOID instead of as a figure.

  2. PARAGRAPH-LOCAL comparison. A whole-chapter statistic cannot see a twelve-word edit; a
     null there is guaranteed by construction, not evidence. Local pairs are the only test
     with any power, and even they are weak at this length — reported with n, not as a verdict.

Usage:  python tools/storyscope_pair.py
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from storyscope_lite import (  # noqa: E402
    ANNOUNCE, TERMINAL, SECOND, META,
    sentences, words, style_vector, cosine, stdev, per1k,
    proper_nouns_per1k, terminal_commentary_rate,
)

PROSE = Path(r"C:\Users\Wasch\truth-and-consequences\prose")
COVERAGE_FLOOR = 0.70
FLOOR_WORDS = 25


def all_paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def measured_paragraphs(text):
    return [p for p in all_paragraphs(text) if len(p.split()) >= FLOOR_WORDS]


def coverage(text):
    allp = all_paragraphs(text)
    meas = measured_paragraphs(text)
    wa = sum(len(p.split()) for p in allp)
    wm = sum(len(p.split()) for p in meas)
    return {
        "paras_all": len(allp),
        "paras_measured": len(meas),
        "para_cov": len(meas) / len(allp) if allp else 0.0,
        "word_cov": wm / wa if wa else 0.0,
    }


def body_between_rules(text):
    """Body = the block between the first standalone --- and the next one."""
    blocks = re.split(r"^---\s*$", text, flags=re.M)
    cand = [b.strip() for b in blocks if b.strip()]
    # first block is title/front-matter; body is the longest remaining block that is not
    # dominated by italic commentary
    cand = [b for b in cand if not b.lstrip().startswith("#")]
    return max(cand, key=lambda b: len(b.split()))


def load_specimen1():
    txt = (PROSE / "SPECIMENS.md").read_text(encoding="utf-8")
    seg = txt.split("## SPECIMEN 1 —")[1].split("## SPECIMEN 2 —")[0]
    return body_between_rules(seg)


def load_file_body(name):
    txt = (PROSE / name).read_text(encoding="utf-8")
    # cut trailing analysis sections so they cannot contaminate the prose metrics
    for marker in ("## THE NOTE", "## THE DIFF"):
        txt = txt.split(marker)[0]
    return body_between_rules(txt)


def profile(name, text):
    n = len(words(text))
    cov = coverage(text)
    meas = measured_paragraphs(text)
    vecs = [v for v in (style_vector(p) for p in meas) if v]
    vu = None
    if len(vecs) >= 3:
        sims = [cosine(vecs[i], vecs[j])
                for i in range(len(vecs)) for j in range(i + 1, len(vecs))]
        vu = sum(sims) / len(sims)
    means = []
    for p in meas:
        ss = sentences(p)
        if ss:
            lens = [len(s.split()) for s in ss]
            means.append(sum(lens) / len(lens))
    dyn = stdev(means) / (sum(means) / len(means)) if len(means) >= 3 else None
    voided = cov["word_cov"] < COVERAGE_FLOOR
    return {
        "corpus": name,
        "words": n,
        "para_cov": f"{cov['paras_measured']}/{cov['paras_all']}",
        "word_cov": round(cov["word_cov"], 3),
        "voice_uniformity": ("VOID" if voided else round(vu, 4)) if vu is not None else None,
        "dyn_range_CV": ("VOID" if voided else round(dyn, 3)) if dyn is not None else None,
        "announce_/1k": round(per1k(ANNOUNCE, text, n), 2),
        "2nd_person_/1k": round(per1k(SECOND, text, n), 2),
        "meta_textual_/1k": round(per1k(META, text, n), 2),
        "named_ref_/1k": round(proper_nouns_per1k(text, n), 2),
        # terminal commentary over ALL paragraphs, not just measured ones: a short closing
        # beat is exactly where the gloss would hide, so the floor must not apply here.
        "terminal_comm": round(terminal_commentary_rate(all_paragraphs(text)), 3),
        "first_person_I": len(re.findall(r"\b(I|I'd|I'm|my|me)\b", text)),
    }


def find_para(text, needle):
    for p in all_paragraphs(text):
        if needle.lower() in p.lower():
            return p
    return None


PAIRS = [
    ("flinch paragraph",
     "not held down, not frozen",          # Specimen 1 counterpart
     "none of which is sad"),              # 1-B / 1-C
    ("confession paragraph",
     "wrong tense, and this is the one admission",
     "now the confession"),
]


def main():
    s1 = load_specimen1()
    b = load_file_body("SPECIMEN-1B-speaking-voice.md")
    c = load_file_body("SPECIMEN-1C-tolkien-register.md")

    profs = [profile("Specimen 1 (mythic)", s1),
             profile("1-B (speaking, narrator)", b),
             profile("1-C (speaking, no narrator)", c)]

    keys = [k for k in profs[0] if k != "corpus"]
    w = max(len(k) for k in keys) + 2
    print("\n=== WHOLE-CHAPTER (paired: same chapter, register varied) ===\n")
    print("".ljust(w) + "".join(p["corpus"][:26].rjust(28) for p in profs))
    for k in keys:
        print(k.ljust(w) + "".join(str(p[k]).rjust(28) for p in profs))

    print("\n=== WHAT ACTUALLY TRIPPED THE ANNOUNCEMENT COUNTER ===\n")
    for nm, t in (("S1", s1), ("1-B", b), ("1-C", c)):
        hits = [h if isinstance(h, str) else h[0] for h in ANNOUNCE.findall(t)]
        print(f"  {nm:>4}: {len(hits)} -> {hits}")

    print("\n=== PARAGRAPH-LOCAL: did cutting the 'I' revert the paragraph toward S1? ===")
    print("    (falsification threshold set in PREDICTION-1C.md: mean gain >= 0.010)\n")
    powered, unpowered = [], []
    for label, s1_needle, bc_needle in PAIRS:
        p1 = find_para(s1, s1_needle)
        pb = find_para(b, bc_needle)
        pc = find_para(c, bc_needle)
        if not all((p1, pb, pc)):
            print(f"  {label}: NOT FOUND ({bool(p1)},{bool(pb)},{bool(pc)}) — alignment failed")
            continue
        v1, vb, vc = style_vector(p1), style_vector(pb), style_vector(pc)
        cb, cc = cosine(vb, v1), cosine(vc, v1)
        n = len(pb.split())
        ok = n >= FLOOR_WORDS
        (powered if ok else unpowered).append((label, cc - cb))
        flag = "" if ok else "  [UNDER FLOOR — n too small; a function-word vector here is noise]"
        print(f"  {label}  (n={n}w){flag}")
        print(f"      cos(1-B, S1) = {cb:.4f}")
        print(f"      cos(1-C, S1) = {cc:.4f}")
        print(f"      gain         = {cc - cb:+.4f}\n")

    # A mean across arms of wildly different n lets the noisiest arm write the verdict.
    # That is the exact defect this project keeps finding elsewhere; it does not get a pass here.
    print(f"  arms with power (n>={FLOOR_WORDS}w): {len(powered)}    "
          f"arms excluded as noise: {len(unpowered)}")
    for label, g in unpowered:
        print(f"      excluded: {label} ({g:+.4f}) — NOT averaged in, at any weight")
    if not powered:
        print("  VERDICT: INDETERMINATE — no arm has the power to rule. No number is emitted.")
    else:
        mg = sum(g for _, g in powered) / len(powered)
        signs = {g > 0 for _, g in powered}
        if len(signs) > 1:
            print(f"  VERDICT: INDETERMINATE — powered arms disagree in sign (mean {mg:+.4f}).")
        elif mg >= 0.010:
            print(f"  MEAN GAIN (powered only) = {mg:+.4f}  ->  'structurally forced' SURVIVES")
        else:
            print(f"  MEAN GAIN (powered only) = {mg:+.4f}  ->  'structurally forced' "
                  f"WITHDRAWN as unsupported"
                  + ("  [and the sign is REVERSED: 1-C moved AWAY from S1, i.e. cutting the "
                     "'I' did not revert it]" if mg < 0 else ""))

    print("\n=== SHORT BEATS THE 25-WORD FLOOR DROPS (the ones 1-B's numbers never saw) ===\n")
    for nm, t in (("S1", s1), ("1-B", b), ("1-C", c)):
        drops = [p for p in all_paragraphs(t) if len(p.split()) < FLOOR_WORDS]
        dw = sum(len(p.split()) for p in drops)
        print(f"  {nm:>4}: {len(drops)} paragraphs, {dw} words unmeasured")
        for p in drops[:3]:
            print(f"          - {p[:70]}")


if __name__ == "__main__":
    main()
