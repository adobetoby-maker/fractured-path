# AUTHORSHIP — Book 7, Movement 1 "Unmeasured" (chapters 1–7)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-07-void-roads/state/movement-001/compiled-prompt.md` (movement brief: `packets/MOVEMENT-001.md`, with its coordinator note of 2026-10-11 and its `[B6-reconciled]` marks). The on-disk `BOOK_MAP.md`, `STATE_LEDGER.md` and packet were checked against the compiled prompt and are identical to it. |
| Coordinator rulings applied | The NO-SOURCE method (O3); the Book 6 STATE_LEDGER blocks AFTER MOVEMENT 8 and AFTER MOVEMENT 9, with the corrected Objects ruling (the Velmere letter left sealed at the academy; Seln's case under the cart's canvas from the shelf); the seam as Book 6's closed text has it (the shelf is the second camp past the Line and the first fire; the second day past the Line; five travellers; nine fragments and the uncounted anomaly; Anchor idle; Shadow sealed; no deployment since the Line; the orchard watch rota in Karis's table). OWNER-DECISIONS #18 (no year count since the Kindling), #23 (cart and gelding sold in Lowmarch's first week; the sale and the Book 6 purse sealed as a reserve), #24, #33, #42 and #48 (season-blind; feet, yards, paces, strides; day counts "past the Line"), #46, #49, #50. Cael has no Path: his own Arbiter woke at his Kindling and went dark, and the fragments answer. Reader Standard. No new names. |
| Edition | `monroe-1.3` |
| Drafted | 2026-10-11 |
| Manuscript files | `manuscript/chapter-01.md` … `manuscript/chapter-07.md` |
| State files written | `state/movement-001/EVENT-LIST.md`, `state/movement-001/AUTHORSHIP.md`, `state/movement-001/AUTHOR-REPORT.md` |

## Method statement

- **No source chapter was opened.** No file under `books/` was read, searched, listed or grepped by me at any point in this session: not Book 7's source chapters, not Book 6's, not Book 8's. Events came from the packet, BOOK_MAP (the plan sections, §10 protected wording, §11 release limits, §12 conflicts), STATE_LEDGER, and the closed edition text of Book 6.
- **What was read:** the compiled prompt in full; the edition's Book 6 `chapter-54.md` through `chapter-60.md` in full, from disk; the Book 6 STATE_LEDGER blocks AFTER MOVEMENT 8 and AFTER MOVEMENT 9; `OWNER-DECISIONS.md` (the table and #33, #41–#50); `B6-RECONCILIATION-COORDINATOR-OVERRIDES.md`; Book 7's packets for Movements 2–8, as plans, for forward consistency (the plank, the stone, the wall, the wash, the loft, the carter's map); `universe/UNIVERSE_BIBLE.md` by search, for the Edge Territories and Edge Fauna paragraphs; the edition's Book 1 by search, for the Cinder House board; Book 6 Movement 9's `AUTHORSHIP.md`, the head of its `EVENT-LIST.md` and the head of its `AUTHOR-REPORT.md`, for format; `protected-patterns.txt` (read only); the tools' own scripts.
- **Order of work:** `EVENT-LIST.md` first, then the seven chapters from it. Every scene's mechanics are mine. Changes made while drafting are recorded at the foot of the event list.
- **Source-derived text seen:** only the output of `ed.sh overlap`, which prints shared runs out of my own chapters. Eleven runs of 8–13 words were listed on the first run; seven were re-composed (five ordinary phrases and two that ran one word past a protected line), and the four that remain are packet lines.
- **Probe use:** `sweep_probe.sh book-07-void-roads 1 1` was run once, after drafting, without `SHOW`. No matched pair and no source sentence was displayed.
- **Protected text:** every unit that BOOK_MAP §10 gives for chapters 1–7 is in the manuscript word for word, as the map now writes it, without its inline marks. I found no unit that the map gives only in part, so there are no `[[TIER-B]]` markers.
- **Rhythm repair:** the first drafts measured short (chapter means between 11.9 and 12.4, with too many or too few forty-word sentences by chapter). Each chapter was re-composed by reading, by the same author in the same session. The changes were applied as individually written replacements of exact passages; no rule or script split or joined sentences at punctuation. Two small read-only listings (sentences of forty words or more; sentences of five words or fewer, by the metrics tool's own splitter) were used to find where to read, and live in the session's scratch directory, not in the repository.
- **No git command was run.** `BOOK_MAP.md`, `STATE_LEDGER.md`, the packets, `protected-patterns.txt` and every Book 6 file are untouched. Nothing was written outside `manuscript/chapter-01.md`–`chapter-07.md` and `state/movement-001/`.
