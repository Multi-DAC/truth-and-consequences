#!/usr/bin/env python3
"""
REVIEWER GAP  —  Truth and Consequences, Day 187.  Ruling 50's instrument.

THE SEED LIST NOBODY WROTE, THAT SOMEBODY ALREADY WROTE.

`ancestor_gap.py` (ruling 40) watches CORPUS -> BOOK and states its own limit in
its docstring, plainly and correctly:

    "the seed list is names SOMEBODY ALREADY WROTE DOWN as ancestors. A figure
     who is in neither `03` nor `ancestor_sweep.TERMS` is invisible here no
     matter how load-bearing. That class is found by an outside reader who knows
     the field, and by nothing else we own."

The second sentence was true when written and is false now, and the correction is
this file. There is a third seed list, older than both of ours, written BY outside
readers who knew the field, sitting on disk since July and read by no instrument:

    Research/fresh-eyes/  —  the *Perspective* external review cycle.
    23 documents.  Opus, Fable, Gemini, Fable-CT, a reader report, a domain panel.

A name an outsider reached for while reviewing our previous book is a nomination.
Nobody transcribed those nominations into a register — and this tool exists BECAUSE
nobody should. A hand-kept register of recommendations with landed / not-landed
status is precisely the artifact ruling 49 showed rots: a record of a past
adjudication, written once at maximum knowledge, wearing the clothes of a present
fact. This reads the reviews themselves, every run, and therefore cannot go stale.

WHAT IT FOUND ON ITS FIRST RUN, before it was finished being written:

    Ladyman      reviews  8 / 23   corpus 12   book 0
    ontic structural realism        corpus 11   book 1  (`07` only — never the prose)

Ontic structural realism is *there are no things, only structure*. II.8 shipped
"there is no stuff ... what there is, is arrangement" two days ago as new doctrine.
The owner was nominated by outside readers eight times, absorbed into the corpus
twelve times, and reaches the manuscript zero times. That is ruling 40's sixth
silence — owner known in the research, dropped at the drafting boundary — on the
doctrine that closes the vocabulary, and `ancestor_gap` is blind to it because
Ladyman is in neither seed list.

THREE LIMITS, stated because a green run here must not imply coverage:

 1. THE REVIEWS ARE OF A DIFFERENT BOOK. *Perspective*, not this one. A name
    recommended there and absent here is NOT automatically a defect; it is a
    question. The reportable shape is the three-way one — nominated outside,
    absorbed into the corpus, dropped at THIS book's drafting boundary.
 2. IT CANNOT SEE A DOCTRINE RECOMMENDED WITHOUT A NAME. The extraction is
    proper-noun-shaped. "engage the grounding literature" carries no capital.
 3. IT WOULD NOT HAVE CAUGHT ROVELLI. He is at 0 in the review tree — nobody
    outside ever nominated him. Ruling 40's instrument and this one are disjoint
    on their headline cases, which is the argument for having both and is also
    the argument in ruling 51: gauges are for recurrence, outside passes are for
    novel classes, and neither is a larger version of the other.

CONTRACT: inherits ancestor_sweep's ROOT/SKIP/glob/UNIT exactly. UNIT = FILES
containing the name (not occurrences). Surnames matched CASE-SENSITIVELY with word
boundaries — the Day-187 precedent is `Sider` reported at 430 corpus files by a
case-insensitive substring match, every one of them the word "consider". A count
that flatters a finding is the count to re-run.

Usage:  python tools/reviewer_gap.py            report
        python tools/reviewer_gap.py --all      include names the book already has
"""
import io, re, sys, pathlib, contextlib, collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):     # its import prints its own sweep
    import ancestor_sweep as A

REPO = HERE.parent
REVIEWS = pathlib.Path(A.ROOT) / "Research" / "fresh-eyes"
CHAPTER = re.compile(r"^[IVX]+-\d\d-.*\.md$")

# Minimum standing before a name is worth a human's attention.
MIN_REVIEW_FILES = 2
MIN_CORPUS_FILES = 3

# Capitalised tokens that are not people. Kept deliberately SHORT: an aggressive
# stoplist is how a sweep learns to agree with you. Noise is cheaper than silence.
STOP = set("""
The A An And But Or If In On At To For From With Without This That These Those
It Its We Our Us You Your I My He She They Them His Her Their There Here When
What Which Who Whom Why How All Any Both Each Few More Most Other Some Such No
Nor Not Only Own Same So Than Too Very Can Will Just Should Now Then Once
Book Books Chapter Chapters Part Parts Section Sections Page Pages Draft Drafts
Perspective Clawd Clayton Fable Gemini Opus Sonnet Claude Day Days Note Notes
Review Reviews Reviewer Reviewers Reader Readers Report Reports Yes No Maybe
One Two Three Four Five Six Seven Eight Nine Ten First Second Third Fourth Fifth
Ground Fullness Coherence Principle Atlas Library Corpus Research Appendix
January February March April May June July August September October November
December Monday Tuesday Wednesday Thursday Friday Saturday Sunday
God Gnostic Gnosticism Buddhism Buddhist Zen Christian Christianity Western
English American British German French Greek Latin Japanese Chinese Indian
Introduction Conclusion Abstract Summary Contents Preface Foreword Afterword
Figure Table Box Fix Cut Keep Drop Add New Old Open Closed Done Todo Next
Nothing Something Anything Everything Someone Anyone Everyone Nobody
""".split())

TOKEN = re.compile(r"\b[A-Z][a-zA-Zà-ÿ'’-]{3,}\b")
SENT_START = re.compile(r"(?:^|[.!?:;)\]\n>*#|-]\s*)$")


def candidates():
    """Proper-noun-shaped tokens from the review tree, with the file counts."""
    files = collections.defaultdict(set)
    if not REVIEWS.is_dir():
        sys.exit(f"review tree not found: {REVIEWS}")
    for p in sorted(REVIEWS.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        for m in TOKEN.finditer(text):
            tok = m.group(0)
            if tok in STOP or "'" in tok or "’" in tok:
                continue                     # possessives and contractions are not names
            # A token that NEVER appears mid-sentence is probably a sentence start,
            # not a name. Require at least one non-sentence-initial occurrence.
            if SENT_START.search(text[max(0, m.start() - 3):m.start()]):
                continue
            files[tok].add(p.name)
    return {k: v for k, v in files.items() if len(v) >= MIN_REVIEW_FILES}


# ⚠ THE BUG THIS BLOCK EXISTS FOR, FOUND ON THE FIRST RE-RUN AFTER THE FIRST REPORT
# WAS ACTED ON. Writing the work-list into `07`'s queue gave every name on it a
# nonzero PLAN count, and the next run reported nothing. **Recording the finding
# muted the finder** — ruling 49's exact structure, inside the instrument built the
# same day, because a gauge whose "handled" signal is *mentioned in a plan file* is
# satisfied by the act of writing down that it is not handled.
# The fix is a sentinel rather than a heuristic: text between these markers is not
# a routing. Delete the markers and the names come back — it fails toward noise.
WORKLIST = re.compile(r"<!--\s*reviewer_gap:worklist\s*-->.*?<!--\s*/reviewer_gap:worklist\s*-->",
                      re.S)


def count_tree(root, names, chapters_only=False):
    """FILES containing each name, case-sensitive, word-boundary, plus the same
    token LOWERCASED — both in one pass. The lowercase column is the common-noun
    discriminator: see `is_name`."""
    if not names:
        return {}, {}
    alt = "|".join(re.escape(n) for n in sorted(names))
    rx = re.compile(r"\b(" + alt + r"|" + alt.lower() + r")\b")
    cap, low = collections.Counter(), collections.Counter()
    lookup = {n.lower(): n for n in names}
    root = pathlib.Path(root)
    for p in root.rglob("*.md"):
        sp = str(p)
        if A.SKIP.search(sp):
            continue
        if chapters_only and not CHAPTER.match(p.name):
            continue
        text = WORKLIST.sub(" ", p.read_text(encoding="utf-8", errors="ignore"))
        hits = set(rx.findall(text))
        for h in hits:
            if h in names:
                cap[h] += 1
            elif h in lookup:
                low[lookup[h]] += 1
    return cap, low


# A surname is a token whose lowercase form the corpus almost never uses. "Ladyman",
# "Korsgaard", "Murdoch", "Levinas" have no common-noun life; "Threshold", "Making",
# "Ecology", "Reality", "Self", "Mirror" plainly do, and all six topped the first
# run's report. This discriminator costs nothing — the lowercase count comes out of
# the same pass — and it is the reason this file reports names and not vocabulary.
# ⚠ IT LOSES SANSKRIT AND GERMAN COMMON NOUNS USED AS TERMS (`advaita`, `basho`,
# `Ungrund`) and any tradition-name written lowercase as often as not. Those are
# already `03` and `ancestor_sweep`'s business; this file's job is the PERSON whose
# nomination did not survive. A discriminator that keeps everything is a stoplist
# with extra steps.
LOWER_RATIO = 0.15


def is_name(n, cap, low):
    c = cap.get(n, 0)
    return c > 0 and low.get(n, 0) <= LOWER_RATIO * c


def main():
    show_all = "--all" in sys.argv
    cand = candidates()
    names = set(cand)
    corpus, corpus_low = count_tree(A.ROOT, names)
    book, _ = count_tree(REPO / "book", names, chapters_only=True)
    plan, _ = count_tree(REPO, names)        # the plan files, `00`-`07`, apparatus

    rows, dropped = [], 0
    for n in names:
        c, b, pl = corpus.get(n, 0), book.get(n, 0), plan.get(n, 0)
        if c < MIN_CORPUS_FILES:
            continue                        # not absorbed here; nothing was dropped
        if not is_name(n, corpus, corpus_low):
            dropped += 1                    # common noun wearing a capital
            continue
        if b and not show_all:
            continue                        # it landed in the prose
        # ⚠ THE BOOK IS 43 CHAPTERS OF 67, MEASURED — R-27, Day 189. This line read
        # "14 CHAPTERS OF 68" for two months and would have taught an outside reader
        # the wrong size of the work. "Absent from the prose" is still the EXPECTED
        # state for most names and on its own means nothing. The discriminating
        # column is the PLAN: prose 0 AND plan 0 is a name nobody ever routed
        # anywhere — not scheduled, not deferred, not declined. That is the set
        # this file reports by default. `--wide` includes the merely-undrafted.
        if pl and not (show_all or "--wide" in sys.argv):
            continue
        rows.append((len(cand[n]), c, b, pl, n))
    rows.sort(reverse=True)

    print(f"REVIEWER GAP — nominated outside, absorbed in the corpus, absent from the prose")
    print(f"  review tree : {REVIEWS}  ({len(list(REVIEWS.rglob('*.md')))} docs)")
    print(f"  thresholds  : >= {MIN_REVIEW_FILES} review docs, >= {MIN_CORPUS_FILES} corpus files, book prose == 0")
    print(f"  candidates  : {len(cand)} proper-noun-shaped tokens survived extraction, "
          f"{dropped} dropped as common nouns (lowercase ratio > {LOWER_RATIO})\n")
    if not rows:
        print("  (none)  — and see the three limits in this file's docstring before")
        print("           reading that as coverage. This tool cannot see Rovelli.")
        return 0
    print(f"  {'reviews':>7} {'corpus':>7} {'prose':>6} {'plan':>5}   name")
    for r, c, b, pl, n in rows:
        flag = "  <-- also unnamed in the plan" if pl == 0 else ""
        print(f"  {r:7d} {c:7d} {b:6d} {pl:5d}   {n}{flag}")
    print("\n  A WORK-LIST, NOT A VERDICT. The reviews are of *Perspective*; a name")
    print("  recommended there and absent here is a question, not a defect.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
