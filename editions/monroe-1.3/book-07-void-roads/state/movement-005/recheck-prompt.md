You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-07-void-roads, Movement 5 (chapters 31–37) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-07-void-roads/:
- brief: state/movement-005/REPAIR-BRIEF.md
- reviews: state/movement-005/review-editorial.md, review-cold.md
- author's report: state/movement-005/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-005/pre-repair/
- current text: manuscript/chapter-31.md … chapter-37.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-005.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-07-void-roads/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads 5`, `bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads 5`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 5 5`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-005/REPAIR-REPORT-r1.md. The baseline for diff -U0 is state/movement-005/pre-repair-r1/ (the frozen draft plus the coordinator's 21 plan-audit line fixes); state/movement-005/pre-repair/ is the draft the reads saw.
- Also read state/movement-005/plan-audit.md and source-tracking.md, the STATE_LEDGER "AFTER MOVEMENT 5 — Coordinator rulings", packets/MOVEMENT-006.md (with its coordinator note "the telling and its cost"), MOVEMENT-007.md and MOVEMENT-008.md, and OWNER-DECISIONS.md #18, #23, #24, #42, #46, #48, #49, #50.
- Settled, not findings: the flags ruled KEEP by the plan audit (the crossbow fetched by Seln; the Ring's length; the stated thirteen).
- **Reader Standard, the weighing of the tenth fragment (ch36–37).** The choice stays: Cael lets the long reading run without telling Oryn first and tells her the minute it is over. Judge whether the repaired page now makes it unmistakable to a 13-year-old that (a) all four companions named it wrong, (b) Cael knows refusing would be right and chooses against it, (c) writing it down beforehand makes it knowing, not permitted, and (d) nothing forgives him or supplies consent, with Oryn's own naming and terms left for Movement 6. If any sentence still reads as endorsement, give an exact fix.
- **The count and the rules after repair.** The throw (ch32) and the second lock were re-staged: confirm no fragment use was added or removed (twelve in the Ring, thirteen in all), each use still obeys STATE_LEDGER §2's capability rules, the night log's sum still adds, and Shadow's one use still satisfies the seal on the page (Oryn screened; cannot attribute).
- **Brom's hand:** ONE hand, the pads of FOUR fingers, everywhere; no string until the 100th. **Oryn's failed reads of Cael:** count them across ch20–22 and this movement and check the repaired ch34 read (Lira forces it; "wrist and neck, stops at six") against the protected "I don't say a finding four times to a patient and change it on the fifth" and against Movement 3's reading that stopped at five. Give an exact fix if the numbers disagree.
- Source distance: for the nine passages sent back (ch31 the binding; ch32 the throw and the second lock; ch33 the hour; ch34 scene 3, re-entered; ch35 the arrival; ch36 the loft opening; ch37 "along, not down"), open the source chapters named in source-tracking.md and rule each RESOLVED or STILL TRACKING by the same standard (same content in the same order = tracking, even reworded). Say whether the repair introduced new tracking.
- The restored protected units verbatim, each once, nothing nearby repeating their content. The #49 default; "Quieting" absent; "Compact" aloud once (Seln); nothing about where the file is, what it says or why; "nineteen" absent; Oryn does not know the mechanism at movement end; integration cost not paid.
- Rule on the follow-on facts the author lists (Cael's calf never bound by Oryn, Karis's blanket strip on until the 99th; Brom's folded cuff spent on Lira's arm; the bowman at the east gate; lantern oil four fingers, three, one) against the closed text and Movement 6's packet.
- Never propose a line fix inside a protected unit. Run no git commands.

Write state/movement-005/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
