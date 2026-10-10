You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-06-the-compacts-hand, Movement 4 (chapters 21–27) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-06-the-compacts-hand/:
- brief: state/movement-004/REPAIR-BRIEF.md
- reviews: state/movement-004/review-editorial.md, review-cold.md
- author's report: state/movement-004/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-004/pre-repair/
- current text: manuscript/chapter-21.md … chapter-27.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-004.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-06-the-compacts-hand/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-06-the-compacts-hand 4`, `bash editions/monroe-1.3/tools/ed.sh gates book-06-the-compacts-hand 4`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 4 4`; (4) reader clarity; (5) listening proof on every chapter.
Additional scope for this recheck (coordinator):
- SOURCE DISTANCE IS THE PRIMARY CHECK. The pre-repair text failed a side-by-side source-distance read with 85 tracked passages, tabled in state/movement-004/source-tracking.md. Ch22 and ch27 were redrafted whole without reopening the source; the passages in ch21, ch23 and ch25 were re-composed.
  - For each tabled passage, judge RESOLVED or STILL TRACKING by reading side by side with the source chapters books/book-06-the-compacts-hand/chapters/chapter-09.md, chapter-10.md and chapter-11.md.
  - Also look for NEW tracking in the redrafted ch22 and ch27.
  - Give counts per chapter. If more than a handful remain, the verdict is SECOND REPAIR, scoped to those passages.
- Check the ch24 burst ledger: exactly five bursts before E4 (the crossways launch is now a push). Check that Brom's count, Rooke's bill and the "borrowed" sixth all agree.
- Check that every interval agrees with the day-71 meet (the coordinator ruling): the day-68 council, the 23-day sealed-letter interval, the day-75 sitting and the day-76 gate.
- Check Seln's ch22 cutaway is at the same altitude: he is not told about Shadow, nothing sealed is named, and the records' content is never stated. The day-45 Velmere letter stays sealed in Brom's left pocket.
- Check the escort order is verbatim under its six-word heading *In the matter of Caelen Hesk-ward.* (#44).
- Length is 30,437 words. Judge only whether anything a reader needs is missing.

Write state/movement-004/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
