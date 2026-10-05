You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-02-iron-circuit, Movement 5 (chapters 30–36) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-02-iron-circuit/:
- brief: state/movement-005/REPAIR-BRIEF.md
- reviews: state/movement-005/review-editorial.md, review-cold.md
- author's report: state/movement-005/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-005/pre-repair/
- current text: manuscript/chapter-30.md … chapter-36.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-005.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-02-iron-circuit/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-02-iron-circuit 5`, `bash editions/monroe-1.3/tools/ed.sh gates book-02-iron-circuit 5`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-02-iron-circuit 5 5`; (4) reader clarity; (5) listening proof on every chapter.


Write state/movement-005/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
