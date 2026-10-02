# AUTHORSHIP — Movement 8 (chapters 48–53)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-01-the-shattered/state/movement-008/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-01-the-shattered/packets/MOVEMENT-008.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 1 — The Shattered |
| Chapters | `editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-48.md` … `chapter-53.md` |
| Date | 2026-10-02 (one session, no restart) |

**Reading before drafting.** The author read the compiled prompt in full (all 2,344 lines, paged). That included:
- the edition brief's rhythm calibration, the no-scripted-surgery rule, the working ranges and the 8-word source gate;
- BOOK_MAP §§1–11 (§§3a, 3e, 5 and 8 were the ones the brief named);
- STATE_LEDGER through "After Movement 7";
- `universe/CANON_RULES.md`;
- every coordinator note: post the Pressure letter; Vell has heard the word; six instances; "What are you?" is reserved for Darrow; Hesk's budget is nearly spent; the Halvern/Halden guard; the yard-owner's lesson belongs here.

The author also read:
- source `chapter-18.md`, `chapter-19.md` and `chapter-20.md`, once each, for events and people;
- the Clue/Plant Ledger and the Ch18 plant in `books/book-01-the-shattered/CHAPTER_ARCHITECTURE.md`;
- movement-007's AUTHORSHIP and AUTHOR-REPORT, for the shape of these files.

From this edition, the author read chapters 41–47 in full. It also read ch 32 (Coss's evaluation and the rocking desk) and the end of ch 33 (Coss's second report and the shim) directly. A read-only helper agent (Explore) read chapters 1–40 in full and compiled a continuity digest. The digest covered:
- the old yard-owner's every line and his number calls;
- Torvin's house and boarders, including the boots woman, who is named nowhere before this movement;
- the bread woman and the fruit woman;
- the errand boys;
- Coss and the post's layout;
- Dessa's habits and tell;
- Vell's call formulae;
- Lira's drills and lodging;
- every Hesk letter;
- the Log's conventions;
- the mender;
- district geography.

The author used the digest for running details only. The helper wrote no prose.

**Coordinator method note (received after chapter 48 was written).** The note says to draft from a private event list, not from the source page. The source chapters were never open while any chapter was drafted. Chapter 48's scenes were not drawn from the source's scene shape: the uncut Part Six, Halden's bone knife, and the realization that Cael's own autumn objection is the first half of section four are all new. After the note, the author wrote a private event list in its own words and drafted chapters 49–53 from that list and BOOK_MAP. When all six chapters existed, the author re-read its own retold scenes (Ilsev, the thin wall, the flag, Lira on trust, Coss at the table, Lira on the roof, the Hesk letters, Torvin and the rent, the market and the apricots) for sentences that followed a source sentence's order with words varied. About twenty-five such places were recomposed before any overlap check, with the beats kept and the construction new. AUTHOR-REPORT, "Source reuse", lists them.

**Drafting.** All six chapters were written forward by the same author, in order. No formula or scoring tool was run between chapters. Blocking slips were fixed as they were noticed:
- Hesk's home letter no longer mentions Cael's mother, whom canon has not established.
- Coss no longer names "the flag on the evaluation" before saying he knows nothing about a flag.
- The section head's line no longer reveals that Vell is a woman, which Ilsev's report could not have told him.
- Lira's savings tin is kept in her pocket, not under a board.
- "Six weeks" became "a season" in Cael's thought behind the partition, to match Coss's words.
- Hesk's thought about the fourth case no longer implies how it ended.

**After all six existed:**
1. **Source-reuse pass.** After the paraphrase rework above, `ed.sh overlap book-01-the-shattered 8` found **7 unprotected runs**. Each was recomposed by reading. One of them was replaced with Hesk's saying exactly as BOOK_MAP §3b gives it. Re-run: **0 unprotected, 3 protected**.
2. **Formula metrics.** One run of `tools/formula_metrics.py` on the six chapters. No formula-driven rewriting was done.
3. **Gates.** `ed.sh gates book-01-the-shattered 8` reports reader_standard=0, metadata=0 and modern=0 on all six chapters.

Only the six chapter files and these two state files were written. No git commands were run.
