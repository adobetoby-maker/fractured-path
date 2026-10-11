You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-06-the-compacts-hand, Movement 9 (chapters 55–60) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-06-the-compacts-hand/:
- brief: state/movement-009/REPAIR-BRIEF.md
- reviews: state/movement-009/review-editorial.md, review-cold.md
- author's report: state/movement-009/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-009/pre-repair/
- current text: manuscript/chapter-55.md … chapter-60.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-009.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-06-the-compacts-hand/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-06-the-compacts-hand 9`, `bash editions/monroe-1.3/tools/ed.sh gates book-06-the-compacts-hand 9`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 9 9`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-009/REPAIR-REPORT-r1.md (not a "## Repair r1" section). The baseline for diff -U0 is state/movement-009/pre-repair-r1/ (the text the three reads saw, plus the coordinator's first-pole restoration). state/movement-009/pre-repair/ is the frozen copy the reads saw.
- Also read state/movement-009/source-tracking.md and protected-text.md, and OWNER-DECISIONS.md #43, #45 and #46.
- Settled rulings, not findings: ch60:253 carries the protected first pole "a stamp renewed four times" (identical to ch7); the ch60 closing inventory and "The log banked the thread beside its lineage" (ch59) are protected and stay verbatim; `"This is the first archive I have ever kept that nobody can close," said Karis.` is a BOOK_MAP §4 planned line and stays; the shelf is the second camp past the Line and the first fire.
- Source distance: for the three passages sent back (ch55:175 Bracken off procedure; ch57:13 the cleared table; ch60:3 onward the descent and the shelf), open the source chapters named in source-tracking.md and rule each RESOLVED or STILL TRACKING by the same standard (same content in the same order = tracking, even when reworded). Say whether the repairs introduced any new tracking.
- The author made four changes outside the brief in ch60 (listed in the report: "whose the quiet thing was"; "he wrote it at the stream"; "one line that had no name"; Lira's route line "Scree: by hand again"). Check each against the restored protected text, ch59 and the packet, and rule it KEEP or REVERT.
- This is the book's last movement. Check the end state against book-07-void-roads/BOOK_MAP.md's opening and book-07-void-roads/state/B6-RECONCILIATION-AUDIT.md §F, and list anything Book 7's plan must inherit that the audit does not already carry.
- Never propose a line fix inside a protected run (protected-patterns.txt). Run no git commands.

Write state/movement-009/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
