You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-02-iron-circuit, Movement 3 (chapters 16–22) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-02-iron-circuit/:
- brief: state/movement-003/REPAIR-BRIEF.md
- reviews: state/movement-003/review-editorial.md, review-cold.md
- author's report: state/movement-003/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-003/pre-repair/
- current text: manuscript/chapter-16.md … chapter-22.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-003.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-02-iron-circuit/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-02-iron-circuit 3`, `bash editions/monroe-1.3/tools/ed.sh gates book-02-iron-circuit 3`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-02-iron-circuit 3 3`; (4) reader clarity; (5) listening proof on every chapter.
SPECIFIC CHECKS: (a) Coss's grey slip — verify against the edition's Book 1 ending (editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-60.md and STATE_LEDGER "After Movement 9 — BOOK 1 ENDING": the senior flag dated the day after the bout, no file entry, the empty working-log page, the slip) and Book 2 M2's unsigned middle line (ch15): is "the slip is gone from the file; Coss believes its code now sits as the unsigned second line but cannot be sure because he never wrote it down; a second empty log page" consistent? (b) The author fixed a POV slip in ch22 (Cael's trust paragraph had drawn on Brom's private ch20 decision); confirm no other Cael-POV passage uses a cutaway-only fact (Brom ch16/ch20, Coss ch17). (c) The hardening intervals (activation / "the hold" / recovery) are consistent across ch18, ch20, ch21, ch22 — one beat for the hold everywhere.

Write state/movement-003/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
