#!/usr/bin/env python3
"""
EDIT MANIFEST — the list of intended edits, held as anchor→replacement pairs that ROT LOUDLY.

WHY THIS EXISTS, in Clayton's words (Day 196): *"keep a list of intended edits for a full revision
pass. If we use the queue as a method of checking, we can determine the actual edits necessary and
keep a list for ease of use when it comes time to actually implement edits."*

That splits a job the queue has been doing badly by doing it twice. A queue row DIAGNOSES — it
argues that something is wrong and why. An edit PRESCRIBES — it says which bytes in which file
become which other bytes. The retired 229-row register mixed the two in prose, and the inbound
146-row synthesis is 81% rows that prescribe nothing testable at all (*"disclose the edition
marker"*, *"maintain strict demarcation"*). A row that names no string cannot be checked, cannot be
closed by evidence, and cannot rot visibly — so it reads OPEN forever. This file is the other half.

⛔ THE PROPERTY THAT MAKES IT WORTH BUILDING: AN ENTRY HERE CANNOT ROT SILENTLY. Every READY entry
carries the exact text it expects to find. Between filing and applying, the prose moves — someone
rewrites the sentence, a sweep absorbs the citation, a recompile reflows the page. In a prose queue
that shows up as nothing at all; you arrive to implement, the sentence is different, and you patch
from memory. Here `--check` re-resolves every anchor against the file on disk and a miss is an
ERROR with an exit code. The manifest measures its own staleness on every run.
[[feedback_filed_defect_misprices_its_own_subject]]

⚠ TWO STATES, COUNTED SEPARATELY, AND THIS IS THE WHOLE DISCIPLINE. An edit whose exact anchor has
been chosen is READY. An edit that is agreed in principle with the file named and the text not yet
chosen is SCOPED. They are never summed. "17 edits pending" would otherwise read as seventeen
things you could apply tonight, when it means seventeen decisions someone still has to make — and
that arithmetic is exactly how a backlog becomes a number nobody trusts.
[[feedback_bucket_derived_by_subtraction]]

WHAT IT DOES NOT DO. It does not decide whether an edit is a good idea; the queue row does that,
and every entry names its row. It does not recompile the PDF — applying edits to markdown while
the shipped artefact stands is the split this project is explicitly avoiding while the volume is
public, so `--apply` prints the recompile reminder and does not act on it.

  usage:  python tools/edit_manifest.py                    # check every anchor, print the manifest
          python tools/edit_manifest.py --render           # rewrite EDIT-MANIFEST.md from the JSON
          python tools/edit_manifest.py --apply EM-001     # apply one, verified both directions
          python tools/edit_manifest.py --apply-all        # apply every READY entry
          python tools/edit_manifest.py --selftest         # positive control on the alarm branch
  exit:   0 = every READY anchor resolves uniquely
          1 = at least one anchor is STALE (missing) or AMBIGUOUS (>1 hit)
          2 = self-test failed
"""

import os
import re
import sys
import json
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")
MANIFEST = os.path.join(BOOK, "docs", "edit-manifest.json")
RENDERED = os.path.join(BOOK, "docs", "EDIT-MANIFEST.md")


def load():
    with open(MANIFEST, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save(data):
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def read_chapter(fname):
    """Return (text, used_crlf). Matching happens on LF-normalised text.

    ⚠ CRLF is a known silent-miss route in this environment: an anchor written with LF will not
    match a file stored with CRLF, and the failure looks exactly like a deleted sentence. So the
    normalisation is explicit and the write-back restores whatever the file had.
    """
    path = os.path.join(BOOK, fname)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        raw = fh.read()
    return raw.replace("\r\n", "\n"), ("\r\n" in raw)


def write_chapter(fname, text, used_crlf):
    path = os.path.join(BOOK, fname)
    if used_crlf:
        text = text.replace("\n", "\r\n")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def resolve(entry):
    """Resolve one READY entry against disk. Returns (verdict, hits).

    OK        anchor occurs exactly once — applying it is unambiguous
    STALE     anchor occurs zero times — the prose moved under the filed edit
    AMBIGUOUS anchor occurs more than once — applying it would hit a site nobody read
    NOFILE    the chapter is gone
    """
    path = os.path.join(BOOK, entry["file"])
    if not os.path.exists(path):
        return "NOFILE", 0
    text, _ = read_chapter(entry["file"])
    hits = text.count(entry["anchor"])
    if hits == 1:
        return "OK", 1
    return ("STALE" if hits == 0 else "AMBIGUOUS"), hits


def check(data, quiet=False):
    ready = [e for e in data["edits"] if e["status"] == "READY"]
    scoped = [e for e in data["edits"] if e["status"] == "SCOPED"]
    applied = [e for e in data["edits"] if e["status"] == "APPLIED"]
    void = [e for e in data["edits"] if e["status"] == "VOID"]

    bad = []
    rows = []
    for e in ready:
        verdict, hits = resolve(e)
        rows.append((e, verdict, hits))
        if verdict != "OK":
            bad.append((e, verdict, hits))

    if not quiet:
        print("EDIT MANIFEST — Truth and Consequences")
        print("=" * 78)
        print()
        print("  READY   %3d   anchor chosen, resolves on disk, applying it is mechanical" % len(ready))
        print("  SCOPED  %3d   agreed in principle, exact text NOT yet chosen  <- not addable to READY" % len(scoped))
        print("  APPLIED %3d" % len(applied))
        print("  VOID    %3d   filed then withdrawn; kept so the withdrawal is visible" % len(void))
        print()
        if ready:
            print("READY — anchor resolution against the markdown on disk")
            print("-" * 78)
            for e, verdict, hits in rows:
                mark = "OK " if verdict == "OK" else "!! "
                print("  %s%-8s %-6s %-44s %s" % (
                    mark, e["id"], e["source"], e["file"][:44],
                    verdict if verdict == "OK" else "%s (%d hits)" % (verdict, hits)))
            print()
        if scoped:
            print("SCOPED — each of these needs a person to choose the exact text")
            print("-" * 78)
            for e in scoped:
                print("  .. %-8s %-6s %-44s %s" % (
                    e["id"], e["source"], e["file"][:44], e.get("note", "")[:60]))
            print()
        if applied:
            print("APPLIED")
            print("-" * 78)
            for e in applied:
                print("  ++ %-8s %-6s %-40s %s" % (
                    e["id"], e["source"], e["file"][:40], e.get("applied_on", "?")))
            print()

    if bad:
        print("ERROR: %d READY entr%s no longer resolve%s on disk." % (
            len(bad), "y" if len(bad) == 1 else "ies", "s" if len(bad) == 1 else ""))
        print("       This is the manifest catching its own rot. Re-read the passage before")
        print("       re-writing the anchor — the prose moving usually means the row moved too.")
        for e, verdict, hits in bad:
            print("       %s  %s  %s" % (e["id"], verdict, e["file"]))
            print("         anchor: %r" % e["anchor"][:90])
        return 1
    if not quiet:
        print("All %d READY anchor(s) resolve uniquely. %d SCOPED entr%s still need%s text." % (
            len(ready), len(scoped), "y" if len(scoped) == 1 else "ies",
            "s" if len(scoped) == 1 else ""))
    return 0


def apply_one(data, eid):
    matches = [e for e in data["edits"] if e["id"] == eid]
    if not matches:
        print("ERROR: no entry %s" % eid)
        return 1
    e = matches[0]
    if e["status"] != "READY":
        print("ERROR: %s is %s, not READY. Only READY entries can be applied." % (eid, e["status"]))
        return 1

    verdict, hits = resolve(e)
    if verdict != "OK":
        print("ERROR: %s did not resolve (%s, %d hits). Nothing written." % (eid, verdict, hits))
        return 1

    text, crlf = read_chapter(e["file"])
    new = text.replace(e["anchor"], e["replacement"])

    # ⚠ VERIFY BOTH DIRECTIONS. Old must be gone AND new must be present exactly once. Checking
    # only that the new text appeared would pass an edit that also left the old text standing
    # somewhere, which is the shape of a half-applied repair.
    if new.count(e["anchor"]) != 0:
        print("ERROR: %s — anchor still present after replacement. Nothing written." % eid)
        return 1
    if new.count(e["replacement"]) != 1:
        print("ERROR: %s — replacement resolves %d times, expected 1. Nothing written." % (
            eid, new.count(e["replacement"])))
        return 1

    write_chapter(e["file"], new, crlf)
    e["status"] = "APPLIED"
    e["applied_on"] = datetime.date.today().isoformat()
    save(data)
    print("APPLIED %s in %s" % (eid, e["file"]))
    print("  - %s" % e["anchor"][:100])
    print("  + %s" % e["replacement"][:100])
    print()
    print("⚠ THE MARKDOWN NOW DIFFERS FROM THE SHIPPED PDF. The volume is public; a source edit")
    print("  without a recompile splits the artefact from its source. Recompile and version-bump")
    print("  before this is done, and run tools/self_citation_gate.py before AND after.")
    return 0


def render(data):
    """Rewrite the human-readable view FROM the JSON, so the two cannot disagree.

    The .md is a rendering, never a source. Editing it by hand loses the edit on the next run,
    which is the correct failure — one file is authoritative and it is the one the tool reads.
    """
    ready = [e for e in data["edits"] if e["status"] == "READY"]
    scoped = [e for e in data["edits"] if e["status"] == "SCOPED"]
    applied = [e for e in data["edits"] if e["status"] == "APPLIED"]

    L = []
    L.append("# EDIT MANIFEST — Truth and Consequences")
    L.append("")
    L.append("⚠ **GENERATED FILE.** Source of truth is `book/docs/edit-manifest.json`; regenerate with")
    L.append("`python tools/edit_manifest.py --render`. Hand edits here are lost on the next run.")
    L.append("")
    L.append("**Clayton's ruling, Day 196:** *\"keep a list of intended edits for a full revision pass.")
    L.append("If we use the queue as a method of checking, we can determine the actual edits necessary")
    L.append("and keep a list for ease of use when it comes time to actually implement edits.\"*")
    L.append("")
    L.append("The queue **diagnoses**. This manifest **prescribes** — file, exact anchor text, exact")
    L.append("replacement. Every READY anchor is re-resolved against the markdown on every run, so an")
    L.append("edit filed against a sentence that has since moved fails **loudly** instead of being")
    L.append("silently patched from memory at implementation time.")
    L.append("")
    L.append("| state | count | meaning |")
    L.append("|---|---|---|")
    L.append("| **READY** | %d | anchor chosen and resolving; applying is mechanical |" % len(ready))
    L.append("| **SCOPED** | %d | agreed, exact text **not yet chosen** — never summed with READY |" % len(scoped))
    L.append("| APPLIED | %d | done, verified both directions |" % len(applied))
    L.append("")

    for title, group, ready_group in (
            ("READY", ready, True), ("SCOPED", scoped, False), ("APPLIED", applied, True)):
        if not group:
            continue
        L.append("---")
        L.append("")
        L.append("## %s" % title)
        L.append("")
        for e in group:
            L.append("### %s — %s · `%s`" % (e["id"], e["source"], e["file"]))
            L.append("")
            if e.get("locus"):
                L.append("**Locus:** %s" % e["locus"])
                L.append("")
            L.append("%s" % e.get("rationale", ""))
            L.append("")
            if ready_group and e.get("anchor"):
                L.append("```diff")
                L.append("- %s" % e["anchor"])
                L.append("+ %s" % e["replacement"])
                L.append("```")
            else:
                L.append("⚠ **Text not chosen.** %s" % e.get("note", ""))
            L.append("")

    with open(RENDERED, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("Rendered %s (%d READY, %d SCOPED, %d APPLIED)" % (
        os.path.basename(RENDERED), len(ready), len(scoped), len(applied)))
    return 0


def selftest():
    """POSITIVE CONTROL on the ALARM branch, which is the branch nobody exercises.

    A checker that has only ever printed OK has not been shown to be able to print anything else.
    So this fabricates the two failures that matter — an anchor that is gone, and an anchor that
    matches twice — against a real chapter file, and fails if either is reported clean.
    [[feedback_gauge_can_only_render_its_good_news]] [[feedback_zero_needs_a_positive_control]]
    """
    victim = "VI-02-the-voices.md"
    if not os.path.exists(os.path.join(BOOK, victim)):
        print("SELFTEST FAIL: fixture chapter %s missing" % victim)
        return 2

    text, _ = read_chapter(victim)
    ok = True

    # 1. an anchor that IS there, exactly once — the control on the control
    good = "It is countable, it has been counted, and anyone may recount it."
    v, h = resolve({"file": victim, "anchor": good})
    if v != "OK":
        print("SELFTEST FAIL: known-present anchor scored %s (%d hits), expected OK" % (v, h))
        ok = False

    # 2. an anchor that is NOT there — must be STALE, not silently clean
    v, h = resolve({"file": victim, "anchor": "zzz-this-string-is-not-in-the-book-zzz"})
    if v != "STALE":
        print("SELFTEST FAIL: absent anchor scored %s, expected STALE" % v)
        ok = False

    # 3. an anchor that matches MANY times — must be AMBIGUOUS. `the ` is guaranteed plural here.
    v, h = resolve({"file": victim, "anchor": "the "})
    if v != "AMBIGUOUS" or h < 2:
        print("SELFTEST FAIL: plural anchor scored %s (%d hits), expected AMBIGUOUS" % (v, h))
        ok = False

    # 4. the file really does contain what test 1 assumed — guards against a green from an
    #    empty read, where every count is 0 and test 2 passes for the wrong reason.
    if good not in text:
        print("SELFTEST FAIL: fixture text absent; test 2's pass would be vacuous")
        ok = False

    print("SELFTEST %s — alarm branch reachable (STALE and AMBIGUOUS both produced)"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 2


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    data = load()
    if "--render" in args:
        rc = check(data, quiet=True)
        render(data)
        return rc
    if "--apply-all" in args:
        rc = 0
        for e in [e for e in data["edits"] if e["status"] == "READY"]:
            rc |= apply_one(data, e["id"])
        return rc
    if "--apply" in args:
        i = args.index("--apply")
        if i + 1 >= len(args):
            print("ERROR: --apply needs an entry id")
            return 1
        return apply_one(data, args[i + 1])
    return check(data)


if __name__ == "__main__":
    sys.exit(main())
