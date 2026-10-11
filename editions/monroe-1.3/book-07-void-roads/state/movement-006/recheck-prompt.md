You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-07-void-roads, Movement 6 (chapters 38–44) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-07-void-roads/:
- brief: state/movement-006/REPAIR-BRIEF.md
- reviews: state/movement-006/review-editorial.md, review-cold.md
- author's report: state/movement-006/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-006/pre-repair/
- current text: manuscript/chapter-38.md … chapter-44.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-006.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-07-void-roads/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads 6`, `bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads 6`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 6 6`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-006/REPAIR-REPORT-r1.md. The baseline for diff -U0 is state/movement-006/pre-repair-r1/ (the frozen draft plus the coordinator's fourteen plan-audit line fixes); state/movement-006/pre-repair/ is the draft the reads saw.
- Also read state/movement-006/plan-audit.md and source-tracking.md, the STATE_LEDGER "AFTER MOVEMENT 6 — Coordinator rulings", packets/MOVEMENT-007.md and MOVEMENT-008.md (with their coordinator notes), and OWNER-DECISIONS.md #18, #23, #24, #42, #46, #48, #49, #50, #51.
- Settled, not findings: the flags ruled in REPAIR-BRIEF.md; "Tomorrow makes three" verbatim and unglossed (OWNER #51); Oryn's "north" and Millrace (EXC-B7-003, owner-resolved); `[UNBOUND]` in ch42 is the protected in-world form, not a placeholder; "the still place" avoided here by ruling.
- **The telling (ch38) after repair — Reader Standard.** The author added a line of Cael's ("Then it's owed, and I've heard you say so.") before Oryn's restored unit. Confirm the scene still gives Oryn full agency (she names it; the condition and the cost are hers; he does not argue his reasons; nothing forgives him for confessing; no consent after the fact), that sources are told by Path and not person, and that Seln is not identified to her.
- **ch44 joins:** Karis now asks Oryn for a healer's count at the next edge, and Lira asks "And if it's sooner than Thornwater?". Check both against Movement 7's packet (Oryn joins as a stop on her route, never "sixth", never "join"; her Millrace table; the ask refused) so nothing is promised that Movement 7 contradicts. Check Oryn's sum (sixteen out of the gate; seventeen at Oxhollow; the odd day) adds up in loft, yard and road.
- **ch41 reordered** (night of day 103 before noon of 104; Karis's window in two parts): confirm every dependency still runs forward and each window is headed with its day.
- Source distance: for the seven passages sent back (ch38:13; ch39:31; ch40 scene 4 re-entered — Pike's copy and Hesk's absent parcel; ch40 the first self-reading; ch41 the stopped pen; ch43 Cael's parallel), open the source chapters named in source-tracking.md and rule each RESOLVED or STILL TRACKING by the same standard (same content in the same order = tracking, even reworded). Say whether the repair introduced new tracking.
- Unchanged and to be confirmed: deployment thirteen (yard leans outside it); the debt owed, not paid; the tenth used on nobody but himself; "Quieting" first at Karis's naming; Karis's hypothesis never stated; [UNBOUND] once; the birthday never beside a season, month order or count back; Gault's line as memory only; the restored protected units verbatim, each once.
- Never propose a line fix inside a protected unit. Run no git commands.

Write state/movement-006/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
