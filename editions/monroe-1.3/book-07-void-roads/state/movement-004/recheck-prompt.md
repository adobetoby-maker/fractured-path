You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-07-void-roads, Movement 4 (chapters 23–30) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-07-void-roads/:
- brief: state/movement-004/REPAIR-BRIEF.md
- reviews: state/movement-004/review-editorial.md, review-cold.md
- author's report: state/movement-004/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-004/pre-repair/
- current text: manuscript/chapter-23.md … chapter-30.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-004.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-07-void-roads/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads 4`, `bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads 4`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 4 4`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-004/REPAIR-REPORT-r1.md. The baseline for diff -U0 is state/movement-004/pre-repair-r1/ (the frozen draft plus the coordinator's seven plan-audit line fixes); state/movement-004/pre-repair/ is the draft the reads saw.
- Also read state/movement-004/plan-audit.md and source-tracking.md, the STATE_LEDGER "AFTER MOVEMENT 4 — Coordinator rulings", packets/MOVEMENT-005.md through MOVEMENT-008.md, and OWNER-DECISIONS.md #18, #23, #24, #42, #46, #48, #49, #50.
- Settled, not findings: the flags ruled KEEP by the plan audit; the manuscript's Ring geometry (western line stone 220 yards from the floor's middle; floor 26 yard-strides across; den under the EASTERN lip); no cord or stride length stated.
- **Rule specifically on "took the fence".** The restored protected Pike line says Teague "Put it back under the stone and took the fence." In repair the author staged a fence job in Teague's day-89 window: the upper inn's paddock, three days, five marks. BOOK_MAP's plan for later movements has a fence job in its own right (search BOOK_MAP and packets 5–8 for "fence", e.g. Pike's "Fence. Forty. Teague says it's yours if you want it; he's got the cold road" and the cold-term fence). Is the author's paddock fence consistent with what the plan means by "the fence" Teague took, with its price and duration, and with every later reference? If not, give exact fixes that make the day-89 window agree with the plan WITHOUT altering the protected line.
- Rule on the two facts the author changed in repair: (a) the cut bands now run round the FOOT of each of the eleven uprights and the band on the lip is gone — check against BOOK_MAP, the Ring-sheet references and Movement 5–8 packets (the rubbings; "Ring 11"); (b) Cael's overrun of his own limit for the sheets is now three quarters of an hour. KEEP or AMEND with exact fixes.
- Source distance: for the four passages sent back (ch29 Lira's burst becoming a step; ch30 the floor's edge; ch30 the masonry samples; ch30 the den approach), open the source chapters named in source-tracking.md and rule each RESOLVED or STILL TRACKING by the same standard (same content in the same order = tracking, even reworded), and say whether the re-entered ch30 floor scene or anything else in the repair introduced new tracking.
- The #49 default: confirm again, after the repair, that nothing outside the protected log entries says "his Path", says Cael's Arbiter is awake or unaffected, or says why the fragments answer; "Quieting" does not occur; "Compact" is not said aloud; "made" once, by Karis; no stillhound is seen; Oryn reads nobody inside; the new anchor in ch29 (the cost of telling, now Seln) spends nothing reserved for Movement 5 or 6.
- Seln's locked case: shut, on his strap, through the movement and over the line. The three restored protected units (Pike; Brom; Lira's clock line) verbatim, each once, nothing nearby repeating their content.
- Never propose a line fix inside a protected unit. Run no git commands.

Write state/movement-004/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
