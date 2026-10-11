You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-07-void-roads, Movement 2 (chapters 8–14) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-07-void-roads/:
- brief: state/movement-002/REPAIR-BRIEF.md
- reviews: state/movement-002/review-editorial.md, review-cold.md
- author's report: state/movement-002/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-002/pre-repair/
- current text: manuscript/chapter-08.md … chapter-14.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-002.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-07-void-roads/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads 2`, `bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads 2`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 2 2`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-002/REPAIR-REPORT-r1.md. The baseline for diff -U0 is state/movement-002/pre-repair-r1/ (the frozen draft plus the coordinator's twelve plan-audit line fixes); state/movement-002/pre-repair/ is the draft the reads saw.
- Also read state/movement-002/plan-audit.md and source-tracking.md, the STATE_LEDGER "AFTER MOVEMENT 2 — Coordinator rulings", and OWNER-DECISIONS.md #18, #23, #42, #46, #48, #49, #50.
- Settled, not findings: every author flag ruled KEEP by the plan audit (fight length; ford placement; Seln's own Shadow Path under water; the flint fire; the map bend and "a quiet place"; Teague by report only; the well; the closing tack).
- Protected text: confirm the three-speech healer unit at the steading's gate (ch13) is verbatim and that the repaired joins make it audible who says "There isn't one." and that "they" reads as healers; confirm Lira's later protected question has a lead-in that follows; confirm the quiet-ground speech is one uninterrupted three-sentence unit and nobody asks more; confirm no protected document is printed twice.
- Source distance: for the six passages sent back (now about ch8:115, ch11:205, ch11:361, ch12:3, ch13:175, ch14:27), open the source chapters named in source-tracking.md and rule each RESOLVED or STILL TRACKING by the same standard (same content in the same order = tracking, even reworded). Say whether the repair introduced new tracking anywhere.
- The water clause must stay a hypothesis until the fight supplies evidence, and the finding must be entered only after it. Deployment since the Line: none on days 51–52, ONE from day 53, never more. No healer appears; Lira's ankle is not mended; her day-65 run reads as a chosen risk.
- The cold read asked for stable hound identifiers and count anchors at the ch10–ch11 handoff: read that stretch as a first-time listener and rule whether the count can be followed in one pass.
- Never propose a line fix inside a protected unit. Run no git commands.

Write state/movement-002/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
