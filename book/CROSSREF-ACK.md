# CROSSREF-ACK — citations read against the notes that landed after them

`tools/crossref_rot.py` (R-148) flags a citation when the chapter it cites acquired a **⛔
corrective endnote after the citing line was last written**. A flag is not an error. It is a
pair somebody has to read. This file is where "somebody read it" is recorded, and it is the
only thing that makes the gauge go quiet.

**A key is the citing paragraph's own text.** Edit that paragraph and the key changes and the
pair reopens — deliberately. A repair deserves a re-read, and an acknowledgement that survives
the rewriting of the thing it acknowledged is the stamp-rot failure this whole tree is built
against.

**What an ack asserts, exactly:** *I opened the cited chapter's corrective notes and read this
citation against them.* It does **not** assert the citation is correct, and it does not assert
the citation was repaired. If the read produced a repair, the paragraph changed, the key
changed, and the row below is dead — which is the intended signal, not a bug.

Get the lines to paste from:

    python tools/crossref_rot.py --ack-template

Format — one per line, verdict written in plain words after the dash:

    - `IV.10>IV.9:a1b2c3d4` — read 2026-08-11; cites IV.9's body claim, [^12] withdraws half of it. Filed R-XXX.

---

## Acknowledged

- `V.9>IV.10:a3823532` — read Day 192 (2026-08-11). **Not clean — filed as R-151.** V.9 reprints
  IV.10's *"modern focus on physical evidence can only detect the cross-section"* sentence, which
  IV.10 [^6] establishes is **not in the source at all**. Acked here only so the gauge's tier-1
  list reflects what has been LOOKED at; the defect itself is open in the queue.

<!-- 54 tier-1 citations remain unread as of Day 192. That number is the debt, and it is
     supposed to be uncomfortable. Do not bulk-ack it. -->
