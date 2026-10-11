You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-07-void-roads, Movement 3 (chapters 15–22) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-07-void-roads/:
- brief: state/movement-003/REPAIR-BRIEF.md
- reviews: state/movement-003/review-editorial.md, review-cold.md
- author's report: state/movement-003/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-003/pre-repair/
- current text: manuscript/chapter-15.md … chapter-22.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-003.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-07-void-roads/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads 3`, `bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads 3`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 3 3`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-003/REPAIR-REPORT-r1.md. The baseline for diff -U0 is state/movement-003/pre-repair-r1/ (the frozen draft plus the coordinator's ten plan-audit line fixes); state/movement-003/pre-repair/ is the draft the reads saw.
- Also read state/movement-003/plan-audit.md and source-tracking.md, the STATE_LEDGER "AFTER MOVEMENT 3 — Coordinator rulings", packets/MOVEMENT-004.md and packets/MOVEMENT-005.md, and OWNER-DECISIONS.md #18, #23, #24, #42, #46, #48, #49, #50.
- Settled, not findings: the sixteen flags ruled KEEP by the plan audit; the length (now about 41,350 against 40,000; the repair removed about 1,480 words of repeated procedure and the author stopped where the next cut would remove the only showing of a method).
- Source distance: for the six passages sent back (ch16 Seln ahead; ch20 Oryn's arrival, the limb image, the stop at five; ch21 the taping opening and Lira's ankle question), open the source chapters named in source-tracking.md and rule each RESOLVED or STILL TRACKING by the same standard (same content in the same order = tracking, even reworded). Say whether the repair introduced new tracking anywhere, including the new footmark at the seep in ch16.
- Rule on two author questions:
  (1) Oryn's route sum in ch22: he is whole on the 99th by her rule, her Thornwater stop ends on the 95th, she plans four days of work at Thornwater's table and adds one day for the reading. Movement 4's packet has her walk the Fallow road in those days. Is the ch22 plan consistent with Movement 4 and Movement 5's packets and the BOOK_MAP day table if she changes it at the gate on the 93rd? If not, give the exact fix (the author offers: cut the second half of the paragraph beginning "She took it out of the round", keeping "She put a day on the route.").
  (2) The clawless footmark at the seep (ch16): new canon — KEEP or CUT against the bible's Edge Fauna and later packets.
- Teague must learn nothing he could not read off a yard: read his whole window and his meeting with Oryn and confirm nothing lets him tie the healer's lateness to the five.
- Oryn knows nothing of fragments, runs no deep reading, and "More than one" is not said. Deployment since the Line stays ONE. The ankle is not mended. Nobody mentions quiet ground. The "Cold" unit and the Tide axiom are verbatim.
- Never propose a line fix inside a protected unit. Run no git commands.

Write state/movement-003/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
