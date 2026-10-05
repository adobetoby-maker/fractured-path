# AUTHORSHIP — Book 2, Movement 2 "Holding Back" (chapters 9–15)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-02-iron-circuit/state/movement-002/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-02-iron-circuit/packets/MOVEMENT-002.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 2 — Iron Circuit |
| Chapters | `editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-09.md` … `chapter-15.md` |
| Date | 2026-10-04 |

One session, not interrupted. No chapter was drafted by anyone else. No coordinator correction arrived during drafting (Movement 1 was in recheck throughout).

**Reading before drafting.**
- The compiled prompt in full (1,613 lines, paged): profile, formula sections 2–6 and 8–9, the packet (no coordinator notes beyond the brief itself; checked against `packets/MOVEMENT-002.md`, identical), the edition brief (event-list method, 8-word gate, working ranges), BOOK_MAP §§1–12, STATE_LEDGER entry state and "After Movement 1" with its coordinator rulings, CANON_RULES, owner voice.
- This edition's `manuscript/chapter-06.md`, `chapter-07.md` and `chapter-08.md` in full; `chapter-01.md` (Ulric bout, watcher plant, Lira cutaway) and `chapter-03.md` (sweep, officials page, *findable only where they look*) for continuity; greps of ch 2–5 for recurring texture (fruit woman, Red Cap, Dessa, Stedd, Orvet).
- `universe/UNIVERSE_BIBLE.md`: tiers and ranks, advancement (rank accumulation plus formal evaluation at a registered Arbiter station), city access by tier.
- Book 1 of this edition, by grep: Lira's examination (ch 9, 38, 55: the skipped middle, three examiners and a slate, the coal stairs); Dessa's frame and count (ch 24–25, ledger); where the Wind notice arrived (ch 40, Torvin's, night 39); the Book 1 calendar (autumn arrival, frosts by day ~70).
- `state/movement-001/AUTHORSHIP.md`, `AUTHOR-REPORT.md`, `REPAIR-BRIEF.md` and `recheck-prompt.md`, for the shape of these files and the r1 rulings.
- Source `books/book-02-iron-circuit/chapters/chapter-05.md`, `chapter-06.md`, `chapter-07.md`, once each, then closed.

**Method.** After the single source read, the author wrote a private event list in its own words in the scratchpad (outside the repo), scene by scene, with its own order and entry points: the landing-beat bout first, built on the watcher-Blade's six ledger lines; the ceiling told at night with the *what* withheld; Lira refusing Cael's page on Dravin; the Dravin bout seen first from the rope and then from inside Lira; the dip and the betting man; Vell holding the line for a month; the gaze grown out of the view inside the lock, measured with chalk; Keth chosen as the one fighter who varies his count; the stranger sitting inside a ration the author broke; Dessa's count as the architecture example; the clock bout as the pace-matching win; Havel's approach as a careful man weighing a file and walking a district he cannot read; the market square chosen to keep the Compact out of Dace's room; the pear; the empty initials column. It drafted from that list with the source closed.

**Honest note on source distance.** The method held for the invented scenes. Three retold scenes leaned toward the source's beat order from memory and were rewritten after the overlap and probe runs: the steps conversation in ch 12 (first draft followed the source's question, answer, "I think you're going to get there", shoulder bump; recomposed around the backwards hook drawn in frost and Lira's *wrong sum*); Lira's talk about the stranger in ch 13 (first draft followed the source's "odd thing for a stranger" / "what did he want" / "built a personality" / "will he come back" run; recomposed around "Do me" and the bench facing the other way); and Havel's private sentence about the district's order in ch 14 (a source device; replaced by the card-game image in narration). Cael's summary of the three layers in ch 13 also followed the source's log entry and was recomposed. Smaller tracked sentences were recomposed after the probe (the findability bill, the off-form pencil line, "A year at one address", Lira's "the wrong people").

**Drafting.** Seven chapters, written forward in order by the same author. No formula tool was run between chapters. Blocking slips fixed as noticed: "from the bell" (there is no bell; Vell says *Begin*) in ch 9–10; Vell's loss tally in ch 14; a second Darrow memory removed from ch 9 (owner decision #30); the Wind acquisition placed correctly at Torvin's (ch 12, after a Book 1 check); an invented anecdote about Dessa's teacher removed (ch 13); Havel's thought that the marker might be "nobody at all" softened to an unsigned entry (BOOK_MAP §5, §9).

**After all seven existed.**
1. `ed.sh overlap book-02-iron-circuit 2`: nine hits on the first run, all recomposed in context. Final: **0 unprotected, 4 protected**.
2. `ed.sh gates book-02-iron-circuit 2`: reader_standard=0, metadata=0, modern=0 on all seven.
3. `sweep_probe.sh book-02-iron-circuit 2 2` (SHOW=1): the script parses the packet's "Read before drafting" line and picks up only `chapter-08.md` (from the manuscript path), so it probed **source ch 8**: 0% skeleton. Run by hand against the packet's actual sources, ch 5–7 (`skeleton_probe.py --show --source ch05 ch06 ch07`): **1% skeleton** total; no chapter above 1%; no scene above 6% (ch 10 scene 2, the protected lines).
4. `formula_metrics.py` once on the seven chapters. No formula-driven rewriting.
5. After the metrics run, by reading: a dialogue-tag pass (79 reporting tags dropped where the speaker was already clear; no sentence split or joined), the Torvin's correction in ch 12 and the Darrow line in ch 9. Overlap, gates and both probes were re-run after these and stayed as above. The metrics were not re-run.

Only the seven chapter files and these two state files were written (plus a scratchpad event list outside the repo). No git commands were run.
