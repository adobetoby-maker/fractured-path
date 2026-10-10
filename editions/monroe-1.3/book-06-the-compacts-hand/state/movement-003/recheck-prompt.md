You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-06-the-compacts-hand, Movement 3 (chapters 14–20) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-06-the-compacts-hand/:
- brief: state/movement-003/REPAIR-BRIEF.md
- reviews: state/movement-003/review-editorial.md, review-cold.md
- author's report: state/movement-003/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-003/pre-repair/
- current text: manuscript/chapter-14.md … chapter-20.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-003.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-06-the-compacts-hand/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-06-the-compacts-hand 3`, `bash editions/monroe-1.3/tools/ed.sh gates book-06-the-compacts-hand 3`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 3 3`; (4) reader clarity; (5) listening proof on every chapter.
Additional scope for this recheck (coordinator):
- SOURCE DISTANCE IS THE PRIMARY CHECK. The pre-repair text failed a side-by-side source-distance read: 136 tracked passages, tabled in state/movement-003/source-tracking.md. Ch14, ch19 and ch20 scenes 2–6 were redrafted whole; ch15–18 were mostly redrafted scene by scene.
  - For each tabled passage, decide whether its source content and order now survive in the current text (RESOLVED / STILL TRACKING), working side by side with the source chapters books/book-06-the-compacts-hand/chapters/chapter-05.md … chapter-08.md.
  - Also look for NEW tracking introduced by the redraft.
  - Give counts per chapter. If more than a handful remain, the verdict is SECOND REPAIR, scoped to those passages.
- Check the Velmere day-45 letter: it stays SEALED, in Brom's left pocket, carried visibly through ch18–20, and is consistent with BOOK_MAP §4e #10 for M7.
- Check that Seln is NOT told why Shadow was sealed. That reveal is the edition's M6.
- Check the new canon from the repair for contradictions with Books 4–5 and the B6 ledger:
  - Cael writes back to Hesk by Bracken's pouch;
  - Gault's minute line on the four observers;
  - Brom and Ephram at the frames without speaking;
  - the ferry watcher looking at the document cases;
  - Vastin striking a refusal in the old form.
- Length is 31,667 words against about 34,000. Judge only whether anything a reader needs is missing.

Write state/movement-003/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
