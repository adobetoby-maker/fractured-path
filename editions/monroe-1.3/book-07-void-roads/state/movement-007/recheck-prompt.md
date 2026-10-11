You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-07-void-roads, Movement 7 (chapters 45–52) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-07-void-roads/:
- brief: state/movement-007/REPAIR-BRIEF.md
- reviews: state/movement-007/review-editorial.md, review-cold.md
- author's report: state/movement-007/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-007/pre-repair/
- current text: manuscript/chapter-45.md … chapter-52.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-007.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-07-void-roads/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-07-void-roads 7`, `bash editions/monroe-1.3/tools/ed.sh gates book-07-void-roads 7`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-07-void-roads 7 7`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-007/REPAIR-REPORT-r1.md. The baseline for diff -U0 is state/movement-007/pre-repair-r1/ (the frozen draft plus the coordinator's ten plan-audit line fixes); state/movement-007/pre-repair/ is the draft the reads saw.
- Also read state/movement-007/plan-audit.md and source-tracking.md, the STATE_LEDGER "AFTER MOVEMENT 7 — Coordinator rulings", packets/MOVEMENT-008.md (with its coordinator notes) and BOOK_MAP §1 "Ending", and OWNER-DECISIONS.md #18, #23, #24, #42, #46, #48, #49, #50, #51.
- Settled, not findings: the flags ruled KEEP in REPAIR-BRIEF.md; **the length** (the reads split; the coordinator ruled the Stair's action is not cut for the map's 40,000 line; repetition was removed; the movement stands at about 42,350 — do not re-raise the ceiling as a finding); Pike's Fallow line narrated, not reprinted.
- **Rule on three author questions, with an exact fix where needed:**
  (1) ch52 (about line 295): the restored protected unit gives the recurring line's spacing as "every ten cords and a piece. Two hundred and twenty yards and a stride" — yet the chamber is about ten strides across. What does the full source unit mean by a spacing of that size "on every wall… between the courses" (a figure cut INTO the line? the line's interval as read off the sheets? a scale?), and does the surrounding manuscript let a reader understand it without contradiction? If one clause is needed (the author suggests at about 52:251), give it.
  (2) ch48 (about line 19) and ch47 (lines about 105, 123): Oryn's protected "it's the same day as the lean-to and a different question". The author reads the difference as WHERE and WHO he asked (the healer at her own bench, against "a woman on a rock"). Check the source's full context: what was asked at the lean-to and what on the road? Is the author's reading right, or is the difference the reading itself (for a diagnostic reason at the table; to be taught on the road; short against long)? Fix if wrong.
  (3) The chamber's roof height is now corrected on the page (ch49: "a foot"; ch52: "a hand above Brom's head"): confirm the correction reads as Cael correcting a rushed estimate, and that it agrees with the Stair's forty steps and the Hall in Movement 8's packet.
- **ch52 after repair:** no trace of a continuous groove; the line stands BETWEEN the courses on its own; the forty-one kinds are "in the courses"; the design confirmed once; the closing log's protected "five years ago" now stands beside the kit (the ledger's eight stations are the old irons, dated by Seln at five cold terms; the stroke-and-bar is "two visits", the later undated; nothing decoded). Judge whether item D is resolved without spending anything reserved (no decoding, no theory, no who or why) and agrees with the Ring's stake ("five years… maybe six") and Movement 8.
- Source distance: for the three ch52 passages sent back (the stair's air; the "proper catalogue"; the open kit), open the source chapters named in source-tracking.md and rule each RESOLVED or STILL TRACKING by the same standard. Say whether the re-entered scene or anything else in the repair introduced new tracking.
- Confirm after repair: deployment ends at twenty-three and the night log of the 114th sums; Shadow once in the movement, the seal satisfied on the page, Oryn not told its source; the rim faceless and seeing only a declaration outside; Teague asks nothing; the debt still owed (one self-reading done); "the still place" not said; "Tomorrow makes three" not explained; #50's council line unglossed; the five restored protected units verbatim, each once, nothing nearby repeating them; no stride length for Karis.
- Never propose a line fix inside a protected unit. Run no git commands.

Write state/movement-007/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
