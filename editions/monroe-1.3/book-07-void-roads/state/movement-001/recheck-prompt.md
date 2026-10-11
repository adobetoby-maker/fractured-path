You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-07-void-roads, Movement 1 (chapters 1–7) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-07-void-roads/:
- brief: state/movement-001/REPAIR-BRIEF.md
- reviews: state/movement-001/review-editorial.md, review-cold.md
- author's report: state/movement-001/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-001/pre-repair/
- current text: manuscript/chapter-01.md … chapter-07.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-001.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-07-void-roads/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads 1`, `bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads 1`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 1 1`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-001/REPAIR-REPORT-r1.md. The baseline for diff -U0 is state/movement-001/pre-repair-r1/ (the frozen draft plus the coordinator's two plan-audit line fixes); state/movement-001/pre-repair/ is the draft the reads saw.
- Also read state/movement-001/plan-audit.md and source-tracking.md, and OWNER-DECISIONS.md #18, #23, #42, #46, #48, #49, #50. Book 6 is text-locked; its manuscript ch54–60 and STATE_LEDGER "AFTER MOVEMENT 9" (corrected Objects ruling) are the seam authority.
- Settled, not findings: the length (about 37,100 against a 34,000 budget); Teague's healer absent; the Thornwater ford unplaced; the carter's round trip; the road rule as custom; companions' native Paths and Shadow's "rent" not counted as Cael's deployments; all new canon ruled KEEP by the plan audit.
- The stillhound's SENSE must remain unknown in this movement. The coordinator changed ch5's "*It hears. As a dog does.*" to "*It tracked the buckle.*". Check the whole movement for any line that still states or implies HOW it perceives. Rule specifically on the road-rule sound metaphors the author left in ch1 and ch4 ("a burst is a shout", "whatever it is a road hears") and on the changed ch5 line ("might, for all she knew, be a declaration too"): KEEP or AMEND, with an exact fix if AMEND.
- Source distance: for ch7's woman-captain passage (now about ch7:27–43), open the source chapters named in source-tracking.md and rule RESOLVED or STILL TRACKING by the same standard (same content in the same order = tracking, even reworded). Say whether the repair, including the roughly forty sentence joins of item G, introduced any new tracking anywhere.
- Item E moved one history detail (Anchor's uncommanded twelve-second doorway hold) to ch6 (Thornwater's ladder). Check it against Book 6 (the event happened once, in Book 6; it must read as recalled history, not a new event, and Anchor must remain undeployed).
- Item A: confirm the gate-to-stone distance is now one distance (a hundred and ten yards; Seln's hundred and four longer paces stated as the same distance; the forty-five-yard following distance intact) and that "eight roads" is clear. Rule on the author's choice to give Karis no stride count.
- Never propose a line fix inside a protected unit (BOOK_MAP §10; packet-quoted lines; protected-patterns.txt). Run no git commands.

Write state/movement-001/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
