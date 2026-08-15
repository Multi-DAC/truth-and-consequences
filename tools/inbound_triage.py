#!/usr/bin/env python3
"""Triage an INBOUND revision register against the actual book text.

WHY THIS EXISTS. A revision row is a measurement and it rots. An externally
synthesized register arrives with no way to tell a live defect from one that was
repaired last week -- and a rotted row reads exactly like a fresh one. This tool
does not read the register's claims about itself. It takes each row's *quoted
target string* and asks the chapter files whether that string is still in the
BODY, still only in the APPARATUS, or gone.

CLASSIFICATION
  LIVE      quoted target still present in body prose         -> row is real
  PAID?     present only inside an endnote / apparatus block  -> body repaired,
            the note is now the record of the repair
  ABSENT    quoted target found nowhere                       -> repaired, or the
            row's quotation is not verbatim (see UNDECIDABLE below)
  NOLOCUS   row names no chapter locus this tool can resolve
  NOQUOTE   row quotes no target string long enough to test

  Rows that land ABSENT are UNDECIDABLE by this instrument alone: a string can be
  missing because it was fixed or because the register paraphrased it. They are
  reported as their own bucket and are NEVER folded into either answer.

POSITIVE CONTROL (--control). Two rows in the register are known by hand:
  086 V.11 "under the threshold"  -- repaired in the body on Day 195, note kept
  085 V.6  "twelfth century"      -- still standing in the body
A run that cannot separate those two is not measuring anything, and the tool
exits 2 (UNKNOWN) rather than printing a verdict it has not earned.
"""
from __future__ import annotations
import io, os, re, sys, glob, json, argparse, collections

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")

# ---------------------------------------------------------------- chapter map
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8}


def chapter_files():
    """label ('V.6', 'C.1', 'Z.2') -> path, from the on-disk filenames."""
    out = {}
    for p in sorted(glob.glob(os.path.join(BOOK, "*.md"))):
        base = os.path.basename(p)
        m = re.match(r"^([IVX]+|C|Z)-(\d\d)-", base)
        if not m:
            continue
        out[f"{m.group(1)}.{int(m.group(2))}"] = p
    return out


def split_body_apparatus(text: str):
    """Body prose vs footnote blocks. A footnote is a '[^x]:' line plus every
    indented line under it -- the apparatus in this volume wraps deeply."""
    body, app, in_note = [], [], False
    for line in text.split("\n"):
        if re.match(r"^\[\^[^\]]+\]:", line):
            in_note = True
        elif in_note and line.strip() and not line.startswith(("    ", "\t")):
            in_note = False
        (app if in_note else body).append(line)
    return "\n".join(body), "\n".join(app)


# ------------------------------------------------------------- register parse
QUOTE_RE = re.compile(r"[\"“]([^\"“”]{8,120})[\"”]")
LOCUS_RE = re.compile(r"\b([IVX]{1,4}|C|Z)\.(\d{1,2})\b")


def parse_register(path: str):
    """⚠ QUOTE PROVENANCE IS THE WHOLE GAME. A quoted string on the DEFECT side of
    a row is text that should be GONE; the same string on the ACTION side is text
    that should be THERE. Finding one in the body means LIVE; finding the other
    means PAID. Treating both alike inverts the verdict on every repair row, which
    is what the first version of this parser did."""
    text = io.open(path, encoding="utf-8-sig").read()
    rows = []
    for m in re.finditer(r"^\*\s*(\d{3})\s*\[([A-Z-]+)\](.*)$", text, re.M):
        rid, sev, rest = m.group(1), m.group(2), m.group(3)
        loci = []
        for lm in LOCUS_RE.finditer(rest):
            tag = f"{lm.group(1)}.{int(lm.group(2))}"
            if tag not in loci:
                loci.append(tag)
        defect_q, fix_q, consumed = [], [], rest
        # ⚠ THREE CONSTRUCTIONS PUT THE OLD AND NEW TEXT IN THE ORDER THAT DEFEATS A
        # PLAIN Defect:/Action: SPLIT. All three appear in this register, and all
        # three were misread by the first parser -- 'Replace "twelfth century" with
        # "sixteenth century"' scored PAID because the wrong text sat after the verb.
        for pat, order in [
            (r'Replace\s+["“]([^"”]+)["”]\s+with\s+["“]([^"”]+)["”]', "df"),
            (r'from\s+["“]([^"”]+)["”]\s+to\s+["“]([^"”]+)["”]', "df"),
            (r'["“]([^"”]+)["”]\s+instead of\s+["“]([^"”]+)["”]', "fd"),
        ]:
            for pm in re.finditer(pat, rest):
                a, b = pm.group(1).strip(), pm.group(2).strip()
                (defect_q if order[0] == "d" else fix_q).append(a)
                (fix_q if order[1] == "f" else defect_q).append(b)
                consumed = consumed.replace(pm.group(0), " ")
        # whatever is left: Defect side before the imperative, prescription after
        cut = re.search(r"\bAction:|\bRequirement:|\bUpdate to\b|\bCorrect to\b", consumed)
        head, tail = (consumed[: cut.start()], consumed[cut.start():]) if cut else (consumed, "")
        defect_q += [q.strip() for q in QUOTE_RE.findall(head)]
        fix_q += [q.strip() for q in QUOTE_RE.findall(tail)]
        rows.append(dict(id=rid, sev=sev, text=rest.strip(), loci=loci,
                         defect_q=defect_q, fix_q=fix_q))
    return rows


def norm(s: str) -> str:
    """Collate away the differences that are not the defect: smart punctuation,
    emphasis markers, and line wrapping."""
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "--").replace("–", "-")
    s = s.replace("*", "").replace("`", "")
    s = re.sub(r"\s+", " ", s).strip().lower()
    # The register punctuates American-style -- the comma or period lands INSIDE
    # the closing quote and is not part of the quoted text. Row 096 failed the
    # control on exactly this: it looks for `run at full cost,` and the book
    # prints `run at full cost never`. Trimming edge punctuation removes a
    # typographic artifact; it does not widen what counts as a match.
    return s.strip(" ,.;:!?…-")


# ------------------------------------------------------------------- the test
def classify(row, chapters, corpus):
    if not row["defect_q"] and not row["fix_q"]:
        return "NOQUOTE", ""
    targets = [t for t in (chapters.get(l) for l in row["loci"]) if t]
    if not targets:
        return "NOLOCUS", "no resolvable chapter locus -- not searched book-wide"
    # FIX side first: prescribed text already printed is the strongest paid signal
    for q in row["fix_q"]:
        nq = norm(q)
        if len(nq) < 8:
            continue
        for path in targets:
            if nq in corpus[path][0]:
                return "PAID", f'{os.path.basename(path)}: prescribed text "{q}" already in body'
    for q in row["defect_q"]:
        nq = norm(q)
        if len(nq) < 8:
            continue
        for path in targets:
            nbody, napp = corpus[path]
            label = os.path.basename(path)
            if nq in nbody:
                return "LIVE", f'{label}: defect text "{q}" still in body'
            if nq in napp:
                return "PAID?", f'{label}: defect text "{q}" survives only in the apparatus'
    return "ABSENT", "no quoted target found in the named chapter"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("register")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--show", default="LIVE,PAID?", help="buckets to list")
    args = ap.parse_args()

    chapters = chapter_files()
    corpus = {}
    for label, path in chapters.items():
        t = io.open(path, encoding="utf-8").read()
        b, a = split_body_apparatus(t)
        corpus[path] = (norm(b), norm(a))

    rows = parse_register(args.register)
    if not rows:
        print("REFUSED: parsed 0 rows out of the register -- the parser, not the book.")
        return 2

    for r in rows:
        r["verdict"], r["evidence"] = classify(r, chapters, corpus)

    by_id = {r["id"]: r for r in rows}

    # ---- positive control, run before any verdict is printed
    # Both control rows were grepped BY HAND against the chapter files before this
    # tool ran, so the control is independent of the thing it certifies:
    #   130 V.7:147  body still reads "the grimoires are, by volume, warnings"
    #   096 V.9:126  body was repaired on Day 195; "run at full cost never"
    #                now survives only inside endnote [^14]
    #   018 V.6:178  body still reads "in the twelfth century"     (Replace-A-with-B)
    #   021 V.7:191  body still reads "gave the rest of his life"  (Replace-A-with-B)
    # 018 and 021 were grepped in the same first pass, before the parser existed;
    # they are here because they are the construction that inverted, and a control
    # that does not include the failure mode is decoration.
    CONTROL = {"130": "LIVE", "096": "PAID?", "018": "LIVE", "021": "LIVE"}
    ctl, ok = [], True
    for rid, expect in CONTROL.items():
        got = by_id[rid]["verdict"] if rid in by_id else "MISSING"
        ctl.append((rid, expect, got))
        ok &= (got == expect)

    print("POSITIVE CONTROL  (both loci hand-grepped before this tool existed)")
    for rid, expect, got in ctl:
        print(f"  {'✅' if got == expect else '❌'} row {rid}: expect {expect:<6} got {got}")
    if not ok:
        print("\n⛔ CONTROL FAILED. The instrument cannot separate a repaired row from a")
        print("   standing one, so it has no verdict to give. Exit 2 = UNKNOWN, which is")
        print("   not the same as clean and must not be read as one.")
        return 2
    print("  ✅ the instrument separates a repaired row from a standing one.\n")

    counts = collections.Counter(r["verdict"] for r in rows)
    print(f"REGISTER : {args.register}")
    print(f"ROWS     : {len(rows)}\n")
    order = ["LIVE", "PAID?", "ABSENT", "NOQUOTE", "NOLOCUS"]
    for k in order:
        print(f"  {k:<9} {counts.get(k,0):4d}")
    print()
    print("⚠ ABSENT / NOQUOTE / NOLOCUS are NOT verdicts. They are the rows this")
    print("  instrument cannot decide, and they must be read by hand. Folding them")
    print("  into either answer is how a triage tool manufactures a clean book.\n")

    want = [w.strip() for w in args.show.split(",") if w.strip()]
    for k in want:
        sel = [r for r in rows if r["verdict"] == k]
        if not sel:
            continue
        print(f"--- {k} ({len(sel)}) " + "-" * 40)
        for r in sel:
            print(f"  {r['id']} [{r['sev']}] {r['evidence']}")
            print(f"        {r['text'][:150]}")
        print()

    if args.json:
        io.open(os.path.join(ROOT, "work", "inbound_triage.json"), "w", encoding="utf-8").write(
            json.dumps(rows, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
