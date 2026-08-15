#!/usr/bin/env python3
"""
FRESH READ — coverage gauge for the Day-195 queue reset.

WHY THIS EXISTS. On Day 195 night Clayton retired `REVISION-QUEUE.md` rather than splitting it:
226 rows, 205 of them live, accumulated across weeks of drafting against a book that kept moving
underneath them. His reasoning is the same one this project has now filed three times in other
words — **a queue row is a MEASUREMENT and it rots.** Eleven closures earlier the same day were
rows whose machine was fine and whose description had gone stale. So the queue starts again from
fresh reads of the compiled PDF, and *"then we will know what is actually left to do."*

⛔ **THE FAILURE THIS FILE EXISTS TO PREVENT IS THE OBVIOUS ONE AND IT IS NOT PARANOIA.** A reset
queue is EMPTY, and an empty queue reads exactly like a finished book. There is no visual
difference between *nothing is wrong* and *nobody has looked*, which is the same defect the retired
queue's last row was about. So coverage gets a gauge before the first finding gets filed, and the
gauge's loud half is the UNREAD list, not the read one.

WHAT IT MEASURES, AND THE UNIT IS THE PDF, NOT THE MARKDOWN. The reader gets the compiled volume,
so the read is against `book/pdf/Truth-and-Consequences.pdf` and the chapter map is parsed out of
that PDF's own table of contents — page numbers included, so a session can be handed a range rather
than a filename. Reading the markdown is a different act with different findings and does not count
here.

THE MAP GETS A CONTROL, because a chapter map derived from one artefact and applied to another is
exactly where a silent gap lives. Every chapter file on disk must appear in the PDF's TOC and every
TOC entry must exist on disk; either direction failing is printed as an ERROR and suppresses the
coverage verdict. A book with a chapter that never reached the PDF would otherwise read as 100%
covered the moment the ledger was filled in.

WHAT IT CANNOT DO — stated because a green here is weaker than it looks:
  · It cannot tell whether a read was ATTENTIVE. It records that a chapter was marked read, by
    whom, on what date, against which PDF build. A careless pass and a careful one look identical.
  · It cannot re-find a defect that is invisible in the PDF. Tool bugs, gauge holes, cross-file
    inconsistencies and anything living in `tools/` CANNOT be found by reading prose, so retiring
    the old queue really does drop them. `--carry` lists the archived rows that name a tool path,
    because those are the ones a fresh read is structurally incapable of recovering.

  usage:  python tools/fresh_read.py [--carry] [--read <CH> [--by NAME]] [--selftest]
  exit:   0 = map verified, 1 = map ERROR (disk/TOC disagree), 2 = self-test failed
"""

import os
import re
import sys
import json
import glob
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")
PDF = os.path.join(BOOK, "pdf", "Truth-and-Consequences.pdf")
LEDGER = os.path.join(BOOK, "docs", "fresh-read-ledger.json")
ARCHIVE = os.path.join(BOOK, "docs", "archive", "REVISION-QUEUE-RETIRED-D195.md")

# A TOC line: "IV .10 — WHAT THE CENSUS CANNOT SEE ......  381". The roman numeral and the
# chapter number are separated by an optional space in the rendered PDF (the font's kerning
# puts one there), which is why this normalises rather than matching a fixed form.
TOC_LINE = re.compile(r"^\s*([IVXC]{1,4}|C|Z)\s*\.\s*(\d+)\s*[—–-]\s*(.*?)[\s.]*?(\d+)\s*$")

# ⚠ THE BACK MATTER HAS NO `Z.n` IN THE RENDERED CONTENTS — it is set by title alone,
# so the chapter-number regex above cannot see it and `Z-01`/`Z-02` on disk read as two
# chapters that never compiled. They are in the book, a reader reads them, and they get
# read-tracked like everything else; only their TOC form differs.
BACK_MATTER = re.compile(r"^\s*(THE CLOSED VOCABULARY|WORKS CITED)\b.*?[\s.]*?(\d+)\s*$", re.I)
BACK_MATTER_IDS = {"THE CLOSED VOCABULARY": "Z.1", "WORKS CITED": "Z.2"}


def norm(part, num):
    return f"{part}.{int(num)}"


def chapters_on_disk():
    """(id, filename, words) for every chapter file, in book order."""
    out = []
    for f in sorted(glob.glob(os.path.join(BOOK, "*.md"))):
        b = os.path.basename(f)
        m = re.match(r"^([IVXCZ]+)-(\d+)-", b)
        if not m:
            continue
        words = len(open(f, encoding="utf-8").read().split())
        out.append((norm(m.group(1), m.group(2)), b, words))
    return out


def toc_from_pdf(path=PDF):
    """(id, title, start_page) parsed out of the compiled PDF's own contents pages."""
    try:
        import pypdf
    except ImportError:
        return None, "pypdf not installed — the map cannot be built from the PDF"
    if not os.path.exists(path):
        return None, f"no compiled PDF at {path} — recompile before reading"
    reader = pypdf.PdfReader(path)
    entries, seen = [], set()
    # The contents run in the front matter; stop once the body starts. Bounded rather
    # than whole-document because a chapter TITLE also appears at its own opening page,
    # and a running header would otherwise be parsed as a second TOC entry.
    #
    # ⚠ LINES WRAP, AND THE FIRST DRAFT OF THIS PARSER DID NOT KNOW THAT. Seven of the
    # sixty-nine entries have titles long enough that the rendered TOC breaks them
    # across two lines and the page number lands on the second — so a per-line match
    # dropped exactly the chapters with the longest names. It was the map control, not
    # a reader, that caught it: coverage was refused rather than reported at 62/69,
    # which is the whole reason the control checks both directions before printing a
    # number. Lines are now joined until a page number closes the entry.
    for page in reader.pages[:12]:
        buf = ""
        for line in (page.extract_text() or "").split("\n"):
            line = line.replace("\xa0", " ").rstrip()
            buf = (buf + " " + line).strip() if buf else line
            m = TOC_LINE.match(buf)
            if m:
                cid = norm(m.group(1), m.group(2))
                buf = ""
                if cid in seen:
                    continue
                seen.add(cid)
                entries.append((cid, m.group(3).strip(), int(m.group(4))))
                continue
            b = BACK_MATTER.match(buf)
            if b:
                cid = BACK_MATTER_IDS[b.group(1).upper()]
                buf = ""
                if cid in seen:
                    continue
                seen.add(cid)
                entries.append((cid, b.group(1).strip(), int(b.group(2))))
                continue
            # Only a line that OPENS an entry is worth carrying forward; anything else
            # would glue unrelated front-matter prose into a false match.
            if not re.match(r"^\s*(?:[IVXCZ]{1,4}\s*\.\s*\d+|THE CLOSED VOCABULARY|WORKS CITED)",
                            buf):
                buf = ""
    return entries, None


def verify_map(disk, toc):
    """Both directions. A map checked in one direction cannot see the gap in the other."""
    d, t = {c for c, _, _ in disk}, {c for c, _, _ in toc}
    return sorted(d - t), sorted(t - d)


def load_ledger():
    if not os.path.exists(LEDGER):
        return {"pdf_build": None, "chapters": {}}
    return json.load(open(LEDGER, encoding="utf-8"))


def save_ledger(led):
    json.dump(led, open(LEDGER, "w", encoding="utf-8"), indent=2, sort_keys=True)


def carry_forward():
    """Archived rows a fresh read CANNOT recover, because their subject is not in the book.

    ⚠ HEURISTIC, AND SAID SO RATHER THAN PRINTED AS A COUNT. A row is flagged when its body
    names a `tools/` path or a `.py` file — the rows about instruments rather than prose. It
    will over-select (a prose row that happens to cite the gauge that found it) and it will
    under-select (a cross-file inconsistency described in words). It is a READING LIST for the
    carry-forward decision, not the decision.
    """
    if not os.path.exists(ARCHIVE):
        return []
    rows, cur = [], None
    for line in open(ARCHIVE, encoding="utf-8").read().split("\n"):
        m = re.match(r"^## (R-\d+[\w() ]*)\s*—\s*(.*)$", line)
        if m:
            cur = [m.group(1).strip(), m.group(2).strip()[:96], False]
            rows.append(cur)
        elif cur and re.search(r"tools/[\w_]+\.py|`[\w_]+\.py`", line):
            cur[2] = True
    return [(r[0], r[1]) for r in rows if r[2]]


SELFTEST_TOC = [("I.1", "THE FULLNESS", 5), ("I.2", "THE NECESSITY", 20)]
SELFTEST_DISK = [("I.1", "I-01-x.md", 100), ("I.3", "I-03-x.md", 100)]
# Expected: I.3 is on disk and absent from the PDF (a chapter that never compiled);
# I.2 is in the PDF and absent from disk (a chapter deleted after the last build).
# ⚠ THE FIXTURE PLANTS ONE OF EACH ON PURPOSE. A control with a gap in only one
# direction passes identically whether the checker looks both ways or one way.
SELFTEST_EXPECT = (["I.3"], ["I.2"])


def selftest():
    got = verify_map(SELFTEST_DISK, SELFTEST_TOC)
    ok = got == SELFTEST_EXPECT
    return ok, got


def main():
    argv = sys.argv[1:]
    ok, got = selftest()
    print("POSITIVE CONTROL — synthetic map with one gap planted in EACH direction:")
    print(f"    on disk, missing from the PDF : {got[0]}   (expected {SELFTEST_EXPECT[0]})")
    print(f"    in the PDF, missing from disk : {got[1]}   (expected {SELFTEST_EXPECT[1]})")
    if not ok:
        print("  [X] CONTROL FAILED — the map checker is not checking. Verdict withheld.")
        return 2
    print("  [ok] both directions live.\n")
    if "--selftest" in argv:
        return 0

    disk = chapters_on_disk()
    toc, err = toc_from_pdf()
    if err:
        print(f"⛔ {err}")
        return 1

    missing_from_pdf, missing_from_disk = verify_map(disk, toc)
    if missing_from_pdf or missing_from_disk:
        print("⛔ MAP ERROR — the PDF and the chapter files disagree. Coverage is NOT reported,")
        print("   because a chapter that never reached the PDF reads as covered the moment the")
        print("   ledger is filled in.")
        for c in missing_from_pdf:
            print(f"     on disk, absent from the compiled PDF : {c}")
        for c in missing_from_disk:
            print(f"     in the compiled PDF, absent from disk : {c}")
        print("   Recompile, then re-run.")
        return 1

    led = load_ledger()
    if "--read" in argv:
        cid = argv[argv.index("--read") + 1]
        if cid not in {c for c, _, _ in disk}:
            print(f"⛔ {cid} is not a chapter in this book. Nothing recorded.")
            return 1
        by = argv[argv.index("--by") + 1] if "--by" in argv else "clawd"
        led.setdefault("chapters", {})[cid] = {
            "read_on": datetime.date.today().isoformat(),
            "by": by,
            "pdf_mtime": datetime.datetime.fromtimestamp(
                os.path.getmtime(PDF)).isoformat(timespec="seconds"),
        }
        save_ledger(led)
        print(f"  recorded: {cid} read by {by}\n")

    pages = {c: p for c, _, p in toc}
    read = led.get("chapters", {})
    total_w = sum(w for _, _, w in disk)
    read_w = sum(w for c, _, w in disk if c in read)

    print(f"FRESH READ — against {os.path.basename(PDF)}, built "
          f"{datetime.datetime.fromtimestamp(os.path.getmtime(PDF)).strftime('%Y-%m-%d %H:%M')}")
    print(f"  chapters mapped   : {len(disk)}  (disk and PDF agree, both directions checked)")
    print(f"  READ              : {len(read)}/{len(disk)}   "
          f"{read_w:,}/{total_w:,} words")
    unread = [(c, pages.get(c, 0), w) for c, _, w in disk if c not in read]
    print(f"  ⛔ UNREAD         : {len(unread)}/{len(disk)}   "
          f"{total_w - read_w:,} words — an empty queue over these is not a clean book")
    if unread:
        print()
        for cid, pg, w in unread:
            print(f"      {cid:<8s} p.{pg:<5d} {w:6,}w")

    stale = [c for c, v in read.items()
             if v.get("pdf_mtime") and v["pdf_mtime"] < datetime.datetime.fromtimestamp(
                 os.path.getmtime(PDF)).isoformat(timespec="seconds")]
    if stale:
        print(f"\n  ⚠ READ AGAINST AN OLDER BUILD: {len(stale)} — {', '.join(sorted(stale))}")
        print("    The PDF has been recompiled since. These reads are not void, but they are")
        print("    not reads of the current artefact either.")

    if "--carry" in argv:
        rows = carry_forward()
        print(f"\nCARRY-FORWARD CANDIDATES — {len(rows)} archived row(s) naming a tool path.")
        print("  ⚠ A FRESH READ CANNOT RECOVER THESE. Their subject is not in the book, so")
        print("  retiring the queue really does drop them unless they are moved by hand.")
        print("  Heuristic, and it both over- and under-selects — a reading list, not a ruling.")
        for rid, title in rows:
            print(f"      {rid:<10s} {title}")
    else:
        print("\n  (run with --carry for the archived rows a fresh read cannot re-find)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
