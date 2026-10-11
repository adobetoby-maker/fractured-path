You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-06-the-compacts-hand, Movement 5 (chapters 28–34) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-06-the-compacts-hand/:
- brief: state/movement-005/REPAIR-BRIEF.md
- reviews: state/movement-005/review-editorial.md, review-cold.md
- author's report: state/movement-005/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-005/pre-repair/
- current text: manuscript/chapter-28.md … chapter-34.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-005.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-06-the-compacts-hand/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-06-the-compacts-hand 5`, `bash editions/monroe-1.3/tools/ed.sh gates book-06-the-compacts-hand 5`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 5 5`; (4) reader clarity; (5) listening proof on every chapter.
Additional scope for this recheck (coordinator):
- Source distance: the pre-repair read found only 6 tracked passages (state/movement-005/source-tracking.md: 28:7, 29:23, 29:49, 29:133, 33:67, 34:177). Confirm each is RESOLVED, reading side by side with books/book-06-the-compacts-hand/chapters/chapter-12.md … chapter-14.md, and that the cadence pass introduced no new tracking.
- ch30: the seal-number logic. The two registered dies sit on consecutive ledger lines, and the rubbing's number has no line between them. Check that Havel's slip and his sixth sheet agree.
- ch30–31: the attacker count. The lead stays at the cart and sends four men in. The fifth man stands at the off horse's head watching Karis, then withdraws. Check every attacker is accounted for in the reveal, the ring and the withdrawal.
- ch33 and ch34: the two Storm resettlings, a quarter hour before noon and then forty minutes in the afternoon, must agree with ch34's inventory.
- "The annex" clause in ch29 is consistent with M2 (the reading room plus the lumber room). The protected closing line is unchanged.

Write state/movement-005/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
