# Going wide — non-Amazon EPUB distribution for *Truth and Consequences*

**Day 208 / 2026-08-27.** Opened on Clayton's instruction of 2026-08-26 20:29 ("let's talk about
widening the reach of our volume"), unblocked by his 13:00 ruling the same day: **KDP Select is OFF,
on purpose**, to protect free PhilArchive access. No exclusivity clause binds us. Going wide is
therefore a mechanical question, not a strategic one.

Rule applied throughout: **a path is named only if its stated requirements were checked against our
actual file.** Recall that a platform exists does not count.

---

## 1. What we are actually shipping

Measured from `book/epub/Truth-and-Consequences.epub` this morning, not recalled:

| property | value |
|---|---|
| size | 935,498 B (0.89 MB) |
| EPUB version | 3.0 |
| container | `mimetype` first entry, `ZIP_STORED` — correct |
| documents | 84 XHTML, largest 68,752 B |
| spine | 84 itemrefs |
| images | 1 (`cover.jpg`, 143,516 B) |
| cover | 1600 × 2560 px, RGB, ratio 1:1.600 |
| text | ~330,526 words |

**Metadata present:** title, language, two `dc:creator`s (Clayton Iggulden-Schnell, Clawd
Iggulden-Schnell, both `marc:aut`), description, UUID identifier, `dcterms:modified`.

**Metadata absent:** `dc:publisher`, `dc:date`, `dc:rights`, `dc:subject`, ISBN. None of these block
upload at the lanes below — every one of them collects this through its own web form and writes it
into the file or the store record itself. Listed because it is the difference between our file and a
shop-ready one, and because it is cheap to add if we ever want the file to stand alone.

The file is small, well-formed and unexceptional in every dimension a distributor gates on. **Nothing
about the artifact is the obstacle.** The obstacles found are all policy and cover art.

---

## 2. Lane A — Payhip. Unconditional. Reachable today.

**Checked** against `payhip.com/faq`, fetched 2026-08-27.

- Accepts EPUB. Their exclusion list is EXE, ISO, DMG, VBS, SCR — security-driven, and we are none
  of them.
- **Free forever plan, 5% per sale.** 2% on Plus, 0% on Pro. No activation fee, no maintenance fee,
  no annual charge for earning under a threshold.
- Explicitly permits selling here *while* selling elsewhere ("Can I sell on Payhip if I'm already
  selling on other platforms like Amazon?" — yes).
- Handles VAT/tax. Stripe, PayPal and a dozen other gateways.
- **No editorial gate. No review queue. No authorship policy.** It is a storefront, not a retailer.

**This lane cannot reject us.** That is its entire value: it is the one path with no gatekeeper
between the file and a reader, and it is live the same hour we decide to use it.

What it does not do: no retail discovery, no libraries, no Apple/Kobo shelf. Traffic must come from
us — the Substack, PhilArchive, the repo.

## 3. Lane B — Draft2Digital. Real reach, one real gate.

**Checked** against `draft2digital.com/faq`, fetched 2026-08-27.

The format question is answered outright, in their words:

> "If you already have an epub of your own, Draft2Digital accepts epub files for ebook... **We won't
> make any changes to your epub formatting**, but we'll gladly distribute it to all our digital
> stores for you."

That sentence is why this lane is worth the trouble. Our EPUB carries 1,222 footnotes wired with
`epub:type="noteref"` / `epub:type="footnote"` so Kindle and Apple pop endnotes in place. **An
aggregator that re-converts from Word would destroy that.** D2D distributes the file as-is.

**Reach from one upload:** Apple Books, Barnes & Noble, Kobo (incl. Kobo Plus), Smashwords,
Bookshop.org, Tolino, OverDrive, cloudLibrary, Everand, Hoopla, Vivlio, BorrowBox, Gardners. Amazon
is invite-only and irrelevant to us here. **OverDrive, cloudLibrary, hoopla and BorrowBox are library
systems** — that is public-library shelf space, which sits well with the free-access principle behind
declining Select.

**Cost:** $20 one-time activation, non-refundable. $12/yr maintenance while earning under $100/yr.
~10% commission. Tax interview required **even for titles listed free**.

### ⚠ The gate, quoted exactly

> "While we support AI-assisted content, we do not accept content that has been generated entirely by
> AI/LLMs that has not gone through extensive editing from a human. **Draft2Digital does not accept
> noncredentialled nonfiction content produced by AI and may require further documentation of subject
> matter expertise.**"

This is nonfiction, and our OPF names an AI as co-author in `dc:creator`. **They may ask.** I am not
calling this a rejection — the first clause ("generated entirely by AI... without extensive human
editing") plainly does not describe this book, which is co-written and human-edited throughout. The
second clause is the live one, and it is vague enough to go either way.

**Decide the answer before uploading, because it is a good one and it is true:**

- The book is **co-authored, not generated** — Clayton is a named author, not a prompter.
- **Documentation of subject-matter expertise exists**: 10+ years professional behavioural health;
  the Meridian papers hold Zenodo DOIs; the corpus is listed on PhilArchive.
- We are not hiding the authorship — it is on the cover, by choice.

**Do not pre-emptively strip Clawd from the metadata to slip the gate.** That is the co-authorship
Clayton has been public about for months, and it is the thing the Substack leads with. If a
distributor won't carry a co-authored book honestly labelled, that is worth knowing plainly.

## 4. Lane C — Kobo Writing Life direct. Blocked on the cover, and I could not read their own page.

Direct upload, free, no activation fee, EPUB accepted. Attractive on paper.

**Blocker found:** stated cover minimum is **2,400 px on the short side, 6:9 (1:1.5) ratio**. Ours is
1600 px short side at 1:1.600. **Fails both.**

⚠ **Evidence grade: MEDIUM, single third-party source** (ScribeCount's KWL guide). Kobo's own help
pages returned 403 to this box twice, direct and through a text proxy — **Kobo's spec is not
reachable from here**, so this number is uncorroborated at the primary source. Treat as a strong
prior, not a fact.

Worth noting the pattern: this is **the third gate the same cover has failed for the same reason.**
The print pipeline already died on 1:1.600 against a 1:1.418 trim. The cover was built to one spec
and every vendor wants a different one. A re-render at 2400 × 3600 would satisfy Kobo, Apple and D2D
simultaneously and cost nothing but the render.

**Not urgent** — Lane B reaches Kobo anyway, without the cover problem, because D2D handles store
specs on our behalf.

## 5. What is not available from this box

- **Apple Books direct** requires macOS (Transporter) or an aggregator. We have no Mac. Reach Apple
  through Lane B; there is no other route from here.
- **epubcheck** cannot be run locally — no `java` on this box, and no `pandoc` or `ebooklib` either.
  D2D and Kobo both validate on ingest, so the first real validation will be theirs. `book/_epubcheck.py`
  is our own partial substitute, not the reference validator.

---

## 6. Recommendation and next concrete step

**Run both lanes, in this order.**

1. **Payhip today.** Zero risk, zero gate, zero cost, and it establishes a support path that is ours
   and cannot be revoked by anyone's policy change. This is the lane that makes "support if desired"
   real without touching free access anywhere.
2. **Draft2Digital next**, accepting the $20 and the tax interview, with the authorship answer
   written down *before* the upload rather than improvised at a review queue.

**NEXT CONCRETE STEP — needs Clayton, ~15 minutes, cannot be done by me:**
create the Payhip account (name + email), set the price, upload
`book/epub/Truth-and-Consequences.epub`. It is the same file already in the public repo; nothing
needs rebuilding.

**Mine, and I can do them without him:**
- Re-render the cover at 2,400 × 3,600 (1:1.5) so it clears every store spec at once, including the
  Kobo minimum.
- Add `dc:publisher`, `dc:date`, `dc:rights` and BISAC-aligned `dc:subject` to the OPF and rebuild
  from the manuscript.
- If it matters later: reach Kobo's own spec page through `web_actuator` and settle §4 at the primary
  source instead of a third party.

**Open question for him, one line, not a menu:** free or paid on Payhip, and if paid, what number.
The book is free on GitHub and PhilArchive by design, so any price here is a tip jar with a file
attached, not a gate. I would put it at something unembarrassed — $9.99 — precisely because the free
copy is one click away and always will be.
