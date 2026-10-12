You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

book-08-before-the-paths, Movement 5 (chapters 27–33) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under editions/monroe-1.3/book-08-before-the-paths/:
- brief: state/movement-005/REPAIR-BRIEF.md
- reviews: state/movement-005/review-editorial.md, review-cold.md
- author's report: state/movement-005/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-005/pre-repair/
- current text: manuscript/chapter-27.md … chapter-33.md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-005.md (incl. coordinator notes), the previous chapters, and the source chapters in books/book-08-before-the-paths/chapters/.

Read the FULL current movement, then follow editions/monroe-1.3/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the chapters, `bash editions/monroe-1.3/tools/ed.sh overlap book-08-before-the-paths 5`, `bash editions/monroe-1.3/tools/ed.sh gates book-08-before-the-paths 5`, `bash editions/monroe-1.3/tools/sweep_probe.sh book-08-before-the-paths 5 5`; (4) reader clarity; (5) listening proof on every chapter.

COORDINATOR NOTES FOR THIS RECHECK (they override the generic file list above where they differ):
- The author's repair report is state/movement-005/REPAIR-REPORT-r1.md; the brief is REPAIR-BRIEF.md. The baseline for diff -U0 is state/movement-005/pre-repair-r1/ (the draft plus the eight fixes the coordinator applied from plan-audit.md, listed in plan-audit-apply.md, and the eleventh's lines taken out of their code fence and set in italics); state/movement-005/pre-repair/ is the draft the reads saw.
- **Settled, not findings:** all nineteen author flags and every minted item as plan-audit.md ruled them (KEEP). **Audit fixes 9–10 were DECLINED by the coordinator:** the protected "Fragment eleven" unit is Cael's own cataloguing (the source prints it in italics as his reading; it names Vastin and says "Eleventh"; "Fragment twelve", in the same form, says "it will tell me"), so it is NOT printed as a system block under FRAGMENT ACQUIRED; the author's frame stands and the unit is in italics. Do not propose reverting this. In audit fix 8 the source's stage directions between Cleon's four spoken pieces were replaced by neutral joins which the author may have rewritten; only the spoken words are protected.
- Read LEDGER-RULINGS.md (now in STATE_LEDGER "AFTER MOVEMENT 5") and check EVERY bullet against the surviving prose; report any the text does not bear out, with chapter:line. Also read packets/MOVEMENT-006.md with its coordinator notes: confirm the exit state meets Movement 6's opening (the 291st; the handcart by the carts' street; Karis's bound left hand; eleven fragments; "the clerk has not asked three things").
- **What the author was told to do — judge the result:**
  1. **ch27, the Hall's table:** "Being believed — … It's the end of being able to be wrong." and "Give me a week." are CLEON's (source speaker). Is the re-joined scene true to that — who has been believed, who asks for the week — with Karis then asking the five for the same week in her own words (the protected S10 log says "Karis says give her a week")? Any leftover line that still treats either as Karis's (ch27; ch30's "A week… Mine. From today."; ch31's opening)? Does Cleon's week (from the 287th to the 293rd) still reconcile with "three days" on the 290th?
  2. **ch28:** Seln's whole line at the hatch and the narration's claim that every word was true and that he did not lie: test each clause of the line against the facts on the page ("same as yesterday"; "entered by the practitioner"; "answered for by her"; "we're through").
  3. **ch29–30:** the two "Cleon said" lines; Cleon's close whole, once, with the author's joins; he uses Karis's name there (how does he have it?).
  4. **The tracked passage (ch27:101–107):** open the source sentence named in source-tracking.md and rule RESOLVED or STILL TRACKING; say whether the repair introduced new tracking.
  5. The cipher proof's two physical anchors (ch31); method restatements compressed without losing a discovery or a test; first-use anchors for "*There?*", "the read" and a bracketed status word.
  6. **ch33, the eleventh's lines:** in italics, once, word for word against BOOK_MAP §10 Tier A 12; the frame before and after them reads true; no code fence; not deployed; not told.
- **Check against the edition's own earlier text:** ch28 "For fifteen years no desk had been able to say what Seln looked like"; ch30 the case "had gone through three postings… stood for some months between a researcher's grey boxes… twelve years"; ch30 "six days since" the spring (the 280th → the 286th); ch31 "eleven days ago" for the back room at Lowmarch (the 277th → the 288th); ch33 "the eleventh day of thirty"; Lira having fed Cael "after a stair"; Brom "a Copper from Velmere"; the purse (136 → 134 on the 289th).
- Confirm: every chapter within the three working ranges; gates 0; overlap 0 unprotected; season-blind; no year count since the Kindling in narration; no possessive before "Path" in narration; no new proper noun; Cael never on the square or steps and never looking at the crown; Shadow sealed; Seln's case shut and its contents unnamed; Cleon's Path from outside only; the leaf unread; no restricted name written; consent explicit.
- If you propose a line fix, do not introduce a run of eight or more words that also stands in the source; never inside a protected unit. Run no git commands.

Write state/movement-005/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
