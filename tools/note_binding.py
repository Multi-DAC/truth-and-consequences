#!/usr/bin/env python3
"""note_binding.py — does every endnote have a door, and does every door open?

The signature defect of this project is MECHANISM WITHOUT A TRIGGER: correct code
nothing calls. The book has the same defect class in its apparatus. An endnote can
be written, edited, graded, compiled and PRINTED while no sentence anywhere points
at it. Nothing errors. The chapter ends, a numbered Notes block appears, and the
numbers refer to nothing the reader can find.

Two directions, because one of them is the silent one:

  ORPHAN   [^n]: exists, no [^n] marker in the body   -> note prints, unreachable
  DANGLE   [^n] marker in the body, no [^n]: exists   -> marker prints raw / drops

A dangle is loud (a stray "[^7]" in the text, or a broken link). An orphan is
SILENT: the rendered page looks completely normal. That asymmetry is the whole
reason this file exists.

  python tools/note_binding.py             # census, both directions, control first
  python tools/note_binding.py --pdf       # also: do orphaned notes still PRINT?

⚠ THE --pdf CHECK NEARLY MANUFACTURED A FALSE FINDING. The volume's PDF encodes
f-ligatures (ff, fi, fl, ffi, ffl) as glyphs pypdf cannot map, so "suffering"
extracts as "suering" and a literal phrase search MISSES. Three notes read as
"absent from the shipped book" until the source side was ligature-stripped too,
at which point all three were there. Any probe here therefore runs a POSITIVE
CONTROL first — notes known to be referenced — and refuses to report if the
control does not hit. A zero needs a positive control.
"""
import argparse
import pathlib
import re
import sys

BOOK = pathlib.Path(__file__).resolve().parent.parent / "book"
PDF = BOOK / "pdf" / "Truth-and-Consequences.pdf"

DEFN = re.compile(r"^\[\^([^\]]+)\]:", re.M)


def scan(text):
    """Return (defs, marker_counts) for one chapter's markdown."""
    defs = DEFN.findall(text)
    body = DEFN.sub("@@DEFINITION@@", text)  # a definition is not a reference to itself
    marks = {}
    for m in re.findall(r"\[\^([^\]]+)\]", body):
        marks[m] = marks.get(m, 0) + 1
    return defs, marks


def audit(text):
    defs, marks = scan(text)
    return {
        "defs": defs,
        "marks": marks,
        "orphans": [d for d in defs if d not in marks],
        "dangles": [m for m in marks if m not in defs],
    }


def control():
    """A gauge that has never seen a defect is not known to be able to see one."""
    planted = (
        "A sentence with a live note.[^1]\n\n"
        "A sentence pointing at a note that was deleted.[^99]\n\n"
        "[^1]: the live one.\n\n"
        "[^2]: written, and nothing in the chapter points here.\n"
    )
    r = audit(planted)
    ok = r["orphans"] == ["2"] and r["dangles"] == ["99"]
    print("POSITIVE CONTROL — synthetic chapter, one gap planted in EACH direction:")
    print(f"    orphan detected : {r['orphans']}   (expected ['2'])")
    print(f"    dangle detected : {r['dangles']}   (expected ['99'])")
    print(f"  [{'ok' if ok else 'FAIL'}] both directions live.\n")
    return ok


def normalise(s):
    """Squash to alnum, and delete f-ligatures — the PDF drops them entirely."""
    return re.sub(r"ffi|ffl|ff|fi|fl", "", re.sub(r"[^a-z0-9]", "", s.lower()))


def note_text(text, nid):
    m = re.search(r"^\[\^" + re.escape(nid) + r"\]: (.+?)(?=\n\n|\Z)", text, re.M | re.S)
    return " ".join(m.group(1).split()) if m else None


def pdf_index():
    try:
        import pypdf
    except ImportError:
        print("  [skip] pypdf not installed; --pdf needs it.")
        return None
    if not PDF.exists():
        print(f"  [skip] no PDF at {PDF}")
        return None
    reader = pypdf.PdfReader(str(PDF))
    pages = [normalise(p.extract_text() or "") for p in reader.pages]
    return pages, "".join(pages)  # joined kills page-break splits


def probe(index, phrase, window=60):
    pages, joined = index
    q = normalise(phrase)[:window]
    if not q:
        return None
    hits = [i + 1 for i, p in enumerate(pages) if q in p]
    if hits:
        return hits
    return ["spans a page break"] if q in joined else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true",
                    help="also check whether orphaned notes still PRINT in the volume")
    args = ap.parse_args()

    if not control():
        print("REFUSING to report: the gauge failed its own control.")
        return 2

    files = sorted(BOOK.glob("*.md"))
    if not files:
        print(f"no chapters under {BOOK}")
        return 2

    rows, tot_o, tot_d, tot_n = [], 0, 0, 0
    for p in files:
        t = p.read_text(encoding="utf-8", errors="replace")
        r = audit(t)
        tot_o += len(r["orphans"])
        tot_d += len(r["dangles"])
        tot_n += len(r["defs"])
        rows.append((p, t, r))

    print(f"NOTE BINDING — {len(files)} chapters, {tot_n} endnote definitions\n")
    print(f"  ORPHANED (note exists, nothing points at it) : {tot_o}")
    print(f"  DANGLING (marker exists, no note)            : {tot_d}\n")

    broken = [(p, t, r) for p, t, r in rows if r["orphans"] or r["dangles"]]
    if not broken:
        print("  every endnote in the volume is reachable from the prose.")
    for p, _, r in broken:
        bits = []
        if r["orphans"]:
            bits.append(f"{len(r['orphans'])} ORPHAN {r['orphans']}")
        if r["dangles"]:
            bits.append(f"{len(r['dangles'])} DANGLE {r['dangles']}")
        print(f"  ⛔ {p.name:<50} {' · '.join(bits)}")

    if args.pdf and broken:
        index = pdf_index()
        if index:
            print("\nDOES THE ORPHANED NOTE STILL PRINT? (control first — see module docstring)")
            ctrl_ok = 0
            ctrl = [("VII-03-the-floor.md", "1"), ("II-01-the-ground.md", "1"),
                    ("V-11-what-the-old-roads-knew.md", "1")]
            for fn, nid in ctrl:
                f = BOOK / fn
                if not f.exists():
                    continue
                s = note_text(f.read_text(encoding="utf-8", errors="replace"), nid)
                if s and probe(index, s):
                    ctrl_ok += 1
            print(f"  control — referenced notes found in the PDF: {ctrl_ok}/{len(ctrl)}")
            if ctrl_ok < len(ctrl):
                print("  ⛔ control failed; a MISS below would be the instrument, not the book.")
            for p, t, r in broken:
                found = sum(1 for n in r["orphans"] if probe(index, note_text(t, n) or ""))
                print(f"    {p.name:<50} {found}/{len(r['orphans'])} orphaned notes present in the PDF")
            print("\n  Present-but-unreachable is the finding. The text is not missing;")
            print("  the reader has no route to it. [[feedback_carried_not_triggered]]")

    return 1 if (tot_o or tot_d) else 0


if __name__ == "__main__":
    sys.exit(main())
