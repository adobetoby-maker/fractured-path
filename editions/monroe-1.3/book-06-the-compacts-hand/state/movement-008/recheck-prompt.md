You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-06-the-compacts-hand, Movement 8 (chapters 48–54) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-06-the-compacts-hand/:
- brief: state/movement-008/REPAIR-BRIEF.md
- reviews: state/movement-008/review-editorial.md, review-cold.md
- author's report: state/movement-008/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-008/pre-repair/
- current text: manuscript/chapter-48.md … chapter-54.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-008.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-06-the-compacts-hand/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-06-the-compacts-hand 8`, `bash editions/monroe-1.3/tools/ed.sh gates book-06-the-compacts-hand 8`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 8 8`; (4) reader clarity; (5) listening proof on every chapter.
Additional scope for this recheck (coordinator):
- **Baselines.** pre-repair/ holds the author's FIRST draft. pre-repair-author/ holds the text after the coordinator applied the plan audit's nine exact fixes (state/movement-008/plan-audit.md, "Exact line fixes") and before the author's r1. Diff against pre-repair-author/ to see the author's r1 changes.
- **PROTECTED TEXT.** Check that these are now verbatim against BOOK_MAP §8 Tier B and the protected source wording, and that the author's r1 did not alter them:
  - the ruling paragraph (ch51);
  - Ephram's "Still glad." speech (ch54);
  - the ninth's Log entry, *Nine. Taken in earnest from a friend…* (ch54);
  - the boards-ritual line (ch54).
- **Leftovers.** Check that nothing in ch51–54 still assumes the removed versions: five numbered heads, "the second head", the loser chalking, a blank rule above Ephram's name, two books, five drill days for Lira.
- **Naming.** "The certifying office" is the Archmarshal's office in ch49–50. Unqualified "evaluator of record" means Gault. The protected certification line is verbatim.
- **Source distance.** The two tracked passages, 49:83 and 54:154, should be RESOLVED against books/book-06-the-compacts-hand/chapters/chapter-18.md and chapter-20.md. Check for new tracking in the r1 changes.
- **ch52.** The three small edits ("station"; Ephram's line pointing at his Book 5 trial line, "glad it was on my side of the floor") must agree with Book 5's text (editions/monroe-1.3/book-05-the-silver-standard/manuscript).
- **M9 inheritance.** Confirm the M9 inheritance list in plan-audit.md still matches the page after r1: dates, bodies, fragment inventory, who knows what, the envelope, the boxes.

Write state/movement-008/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
