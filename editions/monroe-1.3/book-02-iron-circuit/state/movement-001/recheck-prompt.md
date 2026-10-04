You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: /Users/drive/fractured-path-monroe13.

Book 2, Movement 1 (chapters 1–8) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1.

Files (under editions/monroe-1.3/book-02-iron-circuit/):
- The brief: state/movement-001/REPAIR-BRIEF.md.
- The reviews it consolidated: review-editorial.md and review-cold.md, in the same folder.
- The author's report: state/movement-001/AUTHOR-REPORT.md, section "## Repair r1".
- The pre-repair text: state/movement-001/pre-repair/.
- The current text: manuscript/chapter-01.md … chapter-08.md.
- Context: BOOK_MAP.md (§8 protected wording, §6.1), STATE_LEDGER.md ("After Movement 1" and the entry state), and editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-04.md and chapter-06.md (the registry "four … three died" fact).

This is not a fresh review. Diff each chapter against pre-repair (`diff -U0`), then check:

(a) Every brief item: RESOLVED, PARTIAL or NOT, with quoted evidence.
- The twelve Copper formals.
- Trial nine visibly not firing, and the nine-burst record true everywhere it is counted (ch5, ch6 Log, ch7, ch8).
- The ch8 REVISIONS block exact against ch7 / BOOK_MAP §8.
- The ch6 Log compression: everything on the brief's keep list still present.
- The ch3 present-tense stake, and the ch4 registry restatement: is it consistent with Book 1 ch4/ch6, and does it disclose nothing reserved?
- The ch1 watcher plant, and its ch8 payoff.
- The ~108 splits and ~20 re-joins: no speech split, and the joins read as joins.

(b) Run these and report the totals:
- `bash editions/monroe-1.3/tools/ed.sh overlap book-02-iron-circuit 1`
- `bash editions/monroe-1.3/tools/ed.sh gates book-02-iron-circuit 1`
- `bash editions/monroe-1.3/tools/sweep_probe.sh book-02-iron-circuit 1 1`
- `python3 editions/monroe-1.3/tools/formula_metrics.py` on the eight chapters. Confirm the author's numbers: mean 13.34, ≥40w 3.0%, 897 w/scene.

(c) Check every changed region for: joins; fragments; dangling referents; orphaned callbacks; the calendar (months unnamed); knowledge boundaries (Brom absent, no Compact contact, nothing reserved); every protected line exact; and the Reader Standard.

Write state/movement-001/recheck-r1.md. Put the verdict first: CLOSE, CLOSE WITH LINE FIXES, or SECOND REPAIR, with scope. Then sections (a)–(c). Then the exact line fixes, in this exact format, one per fix, with each old string verified with grep to match exactly once:
N. `manuscript/chapter-NN.md`
   old: `...`
   new: `...`
