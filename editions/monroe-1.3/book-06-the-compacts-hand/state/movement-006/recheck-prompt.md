You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-06-the-compacts-hand, Movement 6 (chapters 35–40) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-06-the-compacts-hand/:
- brief: state/movement-006/REPAIR-BRIEF.md
- reviews: state/movement-006/review-editorial.md, review-cold.md
- author's report: state/movement-006/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-006/pre-repair/
- current text: manuscript/chapter-35.md … chapter-40.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-006.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-06-the-compacts-hand/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-06-the-compacts-hand 6`, `bash editions/monroe-1.3/tools/ed.sh gates book-06-the-compacts-hand 6`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 6 6`; (4) reader clarity; (5) listening proof on every chapter.
Additional scope for this recheck (coordinator):
- Source distance: the pre-repair read found 5 tracked passages (state/movement-006/source-tracking.md: 36:89, 37:178 lead-in only, 39:95, 40:119, 40:163). Confirm each is RESOLVED side by side with books/book-06-the-compacts-hand/chapters/chapter-15.md … chapter-17.md. Check that the echo compression introduced no new tracking.
- ch38: the clean door's forty-day trigger now counts from the close of the fourth sitting (the one that put the record). Check the arithmetic (day 75 → day 115) and its consistency with the *fled* entry, the four files and the good-standing door.
- ch40: "Four young people and a man at a window."
- RESERVED TRUTHS: the coordinator applied two ch37 fixes from state/movement-006/reserved-truths-audit.md (Seln's seal terms, matched to Book 7's witness/exposure logic). Confirm they are present and unchanged, and that the Kindling mechanics and the older word remain as the audit passed them.
- The echo compression (about 240 words in ch36, ch39, ch40) must not have removed an evidence class, any item the brief named, or a beat a later chapter relies on.

Write state/movement-006/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
