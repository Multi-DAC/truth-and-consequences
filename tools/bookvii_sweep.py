#!/usr/bin/env python3
"""bookvii_sweep.py — the Day-204 in-order read's Book VII instrument.

Every claim below is measured with ONE instrument across ALL page ranges, so the books
are comparable.  That rule is Book V's finding: three ranges swept three ways produced a
number that could not be set beside itself.

Six probes, and each one exists because the read produced a candidate that could have
been wrong in either direction:

  1  APPARATUS LEAK   process-register strings, in NOTES and in BODY separately.
                      The body/notes split is the whole finding for Book IV (0 in body,
                      91 in notes) and for Book II (leaked into the argument).
  2  BARE SLUG        [[wiki]] tags — the ones compile_pdf.py:69-73 strips, so the
                      reader meets a bare underscored slug as if it were a term of art.
  3  DANGLING SOURCE  "taken in full / entire / as stated" with nothing named as the
                      source.  Candidate: the framework-source citations were redacted
                      and left the verb standing.
  4  NOTE WELD        an endnote definition on the line IMMEDIATELY after another one's
                      last line, with no blank between.  Markdown footnote extensions
                      fold the second into the first.  CHECKED AGAINST THE PDF, because
                      the reader gets the PDF and Book VI cost me a claim for reading
                      the markdown instead.
  5  APPARATUS RATIO  notes-words / body-words per chapter.  Book V peaked at 1.02.
  6  ORDER            printed endnote sequence vs body citation order.

python tools/bookvii_sweep.py
"""
import re, sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"

BOOKS = {
    "I": "I-", "II": "II-", "III": "III-", "IV": "IV-",
    "V": "V-", "VI": "VI-", "VII": "VII-", "VIII": "VIII-",
}

def chapters(prefix):
    # 'V-' must not swallow 'VI-' / 'VII-' / 'VIII-'
    out = []
    for p in sorted(BOOK.glob("*.md")):
        stem = p.name
        m = re.match(r"^([IVXC]+)-(\d+)-", stem)
        if not m:
            continue
        if m.group(1) + "-" == prefix:
            out.append(p)
    return out

def split_body_notes(text):
    """Notes begin at the first line matching '[^n]: '.  Everything before is body."""
    lines = text.split("\n")
    first = None
    for i, ln in enumerate(lines):
        if re.match(r"^\[\^[^\]]+\]:", ln):
            first = i
            break
    if first is None:
        return text, ""
    return "\n".join(lines[:first]), "\n".join(lines[first:])

# ---- probe 1: apparatus leak -------------------------------------------------
LEAK = [
    r"\bR-\d+\b", r"\bruling \d+\b", r"\bRuling \d+\b",
    r"\bthe register\b", r"\bthe retrofit\b", r"\bendnote retrofit\b",
    r"\bDay \d+\b", r"\bthe brief\b", r"\bthis manuscript\b",
    r"\bdrafted chapters\b", r"\bthe ghost audit\b", r"\bpre-draft screen\b",
    r"\bfiled rather than\b", r"\bRecorded rather than hidden\b",
    r"\bReceipt status\b", r"\bfirst housing\b", r"\bFirst housing\b",
    r"\bthe batch sweep\b", r"\boutside read\b", r"\bthe queue\b",
    r"\bsatisfaction test\b", r"\bshipped without\b", r"\bnearly shipped\b",
    r"\bfeedback_[a-z_]+\b", r"\btools/[a-z_]+\.py\b",
]
LEAK_RE = [re.compile(p) for p in LEAK]

def leak_hits(text):
    hits = []
    for rx in LEAK_RE:
        for m in rx.finditer(text):
            hits.append((m.start(), m.group(0)))
    # dedupe overlapping starts
    seen, out = set(), []
    for s, g in sorted(hits):
        if s in seen:
            continue
        seen.add(s); out.append(g)
    return out

WIKI = re.compile(r"\[\[([a-z0-9_\-]+)\]\]")
DANGLE_SRC = re.compile(
    r"\*\*[^*]{3,120}\*\*[,:]?\s*(?:—\s*)?taken (?:in\s+full|entire|as stated)"
    r"|,\s*taken\s+(?:in\s+full|entire|as stated)"
    r"|—\s*taken\s+(?:in\s+full|entire|as stated)")

def main():
    print("BOOK VII SWEEP — one instrument, every book, both halves\n")

    # ---------------- probes 1-3, 5 ----------------
    print(f"{'book':>5} {'chs':>4} | {'leak:BODY':>10} {'leak:NOTES':>11} | "
          f"{'[[slug]]':>9} | {'dangle-src':>10} | {'notes/body':>10}")
    print("-" * 78)
    totals = {}
    per_chapter = {}
    for bk, pre in BOOKS.items():
        chs = chapters(pre)
        b_leak = n_leak = wiki = dang = 0
        bw = nw = 0
        for p in chs:
            t = p.read_text(encoding="utf-8")
            body, notes = split_body_notes(t)
            bl, nl = leak_hits(body), leak_hits(notes)
            b_leak += len(bl); n_leak += len(nl)
            wiki += len(WIKI.findall(t))
            dang += len(DANGLE_SRC.findall(t))
            bwc, nwc = len(body.split()), len(notes.split())
            bw += bwc; nw += nwc
            per_chapter[p.name] = dict(body_leak=bl, note_leak=nl,
                                       wiki=WIKI.findall(t),
                                       dangle=len(DANGLE_SRC.findall(t)),
                                       ratio=(nwc / bwc if bwc else 0))
        ratio = nw / bw if bw else 0
        totals[bk] = dict(chs=len(chs), body_leak=b_leak, note_leak=n_leak,
                          wiki=wiki, dangle=dang, ratio=ratio)
        print(f"{bk:>5} {len(chs):>4} | {b_leak:>10} {n_leak:>11} | "
              f"{wiki:>9} | {dang:>10} | {ratio:>10.3f}")

    print("\n⚠ BODY leak is the column that matters — a reader meets it as argument, "
          "not as apparatus.\n")

    # body-leak detail for the worst book
    print("BODY-PROSE LEAK, every hit, every chapter (the column above, itemised):")
    any_body = False
    for name, d in sorted(per_chapter.items()):
        if d["body_leak"]:
            any_body = True
            print(f"  {name:<48} {d['body_leak']}")
    if not any_body:
        print("  (none anywhere in the volume)")

    print("\nBARE SLUGS, by chapter (compile_pdf.py strips the brackets):")
    for name, d in sorted(per_chapter.items()):
        if d["wiki"]:
            print(f"  {name:<48} {d['wiki']}")

    print("\nDANGLING SOURCE VERBS ('taken in full/entire/as stated', no source named):")
    for name, d in sorted(per_chapter.items()):
        if d["dangle"]:
            print(f"  {name:<48} {d['dangle']}")

    print("\nAPPARATUS RATIO, Book VII chapter by chapter (Book V peaked 1.02):")
    for name, d in sorted(per_chapter.items()):
        if name.startswith("VII-"):
            print(f"  {name:<48} {d['ratio']:.3f}")

    # ---------------- probe 4: note weld ----------------
    print("\nNOTE WELD — an endnote definition with no blank line above it:")
    weld = []
    for p in sorted(BOOK.glob("*.md")):
        if not re.match(r"^[IVXC]+-\d+-", p.name):
            continue
        lines = p.read_text(encoding="utf-8").split("\n")
        for i, ln in enumerate(lines):
            if i == 0:
                continue
            if re.match(r"^\[\^[^\]]+\]:", ln) and lines[i - 1].strip() != "":
                # only a weld if the PREVIOUS line belongs to another note
                weld.append((p.name, ln[:14], i + 1, lines[i - 1][-60:]))
    if weld:
        for w in weld:
            print(f"  ⛔ {w[0]:<46} {w[1]:<14} line {w[2]}")
            print(f"      preceded directly by: …{w[3]}")
    else:
        print("  none.")

    # ---------------- probe 6: endnote order ----------------
    print("\nENDNOTE ORDER — printed definition sequence vs body citation order:")
    for p in sorted(BOOK.glob("VII-*.md")):
        t = p.read_text(encoding="utf-8")
        body, notes = split_body_notes(t)
        cited, seen = [], set()
        for m in re.finditer(r"\[\^(\d+)\](?!:)", body):
            n = m.group(1)
            if n not in seen:
                seen.add(n); cited.append(n)
        defined = re.findall(r"^\[\^(\d+)\]:", notes, re.M)
        flag = "  ⛔ OUT OF ORDER" if cited != defined else "  ok"
        print(f"  {p.name:<48}{flag}")
        if cited != defined:
            print(f"      body cites : {'·'.join(cited)}")
            print(f"      notes print: {'·'.join(defined)}")

    (ROOT / "work" / "bookvii-sweep.json").write_text(
        json.dumps({"totals": totals, "per_chapter":
                    {k: {kk: vv for kk, vv in v.items()} for k, v in per_chapter.items()}},
                   indent=2), encoding="utf-8")
    print("\nwrote work/bookvii-sweep.json")

if __name__ == "__main__":
    main()
