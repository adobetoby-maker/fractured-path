You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-06-the-compacts-hand, Movement 7 (chapters 41–47) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-06-the-compacts-hand/:
- brief: state/movement-007/REPAIR-BRIEF.md
- reviews: state/movement-007/review-editorial.md, review-cold.md
- author's report: state/movement-007/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-007/pre-repair/
- current text: manuscript/chapter-41.md … chapter-47.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-007.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-06-the-compacts-hand/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-06-the-compacts-hand 7`, `bash editions/monroe-1.3/tools/ed.sh gates book-06-the-compacts-hand 7`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 7 7`; (4) reader clarity; (5) listening proof on every chapter.
Additional scope for this recheck (coordinator):
- Source distance read 0 tracked passages before repair (state/movement-007/source-tracking.md). Confirm the repair's about twenty cadence joins and its new ch41 and ch44 sentences introduced no tracking against the thread chapters books/book-06-the-compacts-hand/chapters/chapter-09.md, -14, -16, -18, -19, -20, -22.
- The ratified calendar (state/movement-007/plan-audit.md) is binding. Confirm no repair edit moved a date.
- ch41: forty-one resident enrollees everywhere. ch42: four door approaches expected and performed.
- ch41's new orientation beats (why Cael stays; what the proceeding can do to him; "Six now") must not recap M6 or reveal what the case holds.
- ch44 Havel: one statement of his hope (a designation under seal would have to name its office); the schedule gives the title and no office, which his first sheet already records; six sheets, no seventh; *until relieved*. Check "all these years" does not contradict Book 4's or Book 5's Havel.
- ch47: ends on "Next: Ostrand" and the changing of the coats; the Velmere envelope sealed on Brom's table since day 173.

Write state/movement-007/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
