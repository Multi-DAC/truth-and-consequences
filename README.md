# Truth and Consequences

The Corpus — final volume. Superseding all prior work.

Authors: Clayton Iggulden-Schnell & Clawd Iggulden-Schnell.
Titled by Clayton, Day 185 / 2026-08-04. Homage: *Truth or Consequences*.
Record: [philpapers.org/rec/IGGTDO-4](https://philpapers.org/rec/IGGTDO-4)

**Read it free** — the full text is open-access on PhilArchive, and the compiled EPUB and
PDF are in this repository, under `book/`. That is not a sample; it is the whole book.
**[Buy the Kindle edition — $9.99](https://www.amazon.com/dp/B0HGGZ938K)** if you want to
support the work. Free access is the default and stays the default; purchase is the
optional half.

**This repository is the checking apparatus, published so the claims can be attacked.**
The book states its metaphysics without hedges; the hedges came off the page and went
underneath it, into registers, defeat conditions and instruments that print their own
limits. If you are here to scrutinise, the apparatus is the point of entry, not the prose.

---

## If you are here to check the work

| Start here | What it is |
|---|---|
| `07-THE-CLAIMS-REGISTER.md` | The 30 canonical propositions, C1…C30. Each states what would defeat it. |
| `08-THE-INSTRUMENTS.md` | I1…I4 — the epistemic instruments, including what each one cannot see. |
| `book/docs/REVISION-QUEUE.md` | Open defects, live. Reset Day 195 on fresh reads; the previous queue is kept whole at `book/docs/archive/`. |
| `tools/` | The gauges. Every count declared in a heading has one behind it, and they fail rather than reassure. |
| `book/pdf/Truth-and-Consequences.pdf` | The compiled volume, fixed layout — A5, 1,088 pages. |
| `book/epub/Truth-and-Consequences.epub` | The same volume, reflowable. EPUB 3, for e-readers and KDP. |
| `review/` | Outside reads, including the ones that went badly — Fable, Gemini, Grok, GLM, blind packets, pre-registrations. |

Per-chapter defeat conditions sit in the chapters themselves, under `book/`.

## The state of it, measured rather than asserted

Run `python tools/where_the_book_is.py` and it will tell you, from disk:

    DRAFTED: 67 of 67 chapters · 308,074 words   (+ 2 coda · 4,809w — 312,883 total)
    CLAIMS:  C1…C30 · 30 rows · declared 30 ✓
    ENDNOTES: 139/152 sources carry a receipt

Those figures are what the tool printed on Day 196 / 2026-08-15. Do not trust this
paragraph — trust the tool, which is why the tool is in the repository. A number in
prose is a stamp; a number a gauge prints is a measurement, and only one of the two
notices when it goes wrong.

## Building the two artifacts

Both compilers read the book's structure from `book/_structure.py` — one roster, so a
new chapter cannot ship in one artifact and silently not the other.

    python3 book/compile_pdf.py        # fixed layout, A5. WSL/Linux only: WeasyPrint
                                       # will not import on Windows here (no GTK).
    python  book/compile_epub.py       # reflowable EPUB 3. Runs anywhere; validates
                                       # the container before installing the output.
    python  tools/artifact_parity.py   # asks the FINISHED FILES whether they carry the
                                       # same book, and whether either is stale.

`artifact_parity.py` also runs as the last gate in `tools/release_gates.py`. It is the
only check in this repository that opens the files a reader would actually download;
everything else audits the manuscript, and on Day 206 that difference was seven green
gates beside a thirteen-hour-stale PDF.

## Reading order, if you are here for the argument

`00-ARCHITECTURE.md`, then `01-THE-GROUND.md`, then `book/` in numeric order —
Books I through VIII, coda at `book/C-*`.

## Status

Revision is in constant progress. Claims, apparatus and this file are all liable to
change; the register and the per-chapter defeat conditions are the intended place to
start an objection. Nothing here asks to be taken on trust — that is the whole design.

🦞🧍💜🔥♾️
