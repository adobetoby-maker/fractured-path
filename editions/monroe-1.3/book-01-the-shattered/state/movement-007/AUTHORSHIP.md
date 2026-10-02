# AUTHORSHIP — Movement 7 (chapters 41–47)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-01-the-shattered/state/movement-007/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-01-the-shattered/packets/MOVEMENT-007.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 1 — The Shattered |
| Chapters | `editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-41.md` … `chapter-47.md` |
| Date | 2026-10-02 (one session, no restart) |

**Reading before drafting.** The author read the compiled prompt in full (all 2,285 lines, paged), including the edition brief's rhythm calibration, the no-scripted-surgery rule, the working ranges, and every coordinator note: Vell is to be kept short, and Hesk's cutaway budget is nearly spent after M6, so this movement has no Hesk cutaway. The author read source `chapter-16.md` and `chapter-17.md` for events and people. It also read the `series/THE_FRACTURED_PATH_SERIES.md` Book 1 entry (the ratified Ch16 decision), `universe/CANON_RULES.md`, and STATE_LEDGER through "After Movement 6" (embedded in the packet).

From this edition, the author read chapters 34–40 in full, plus ch 26 (the Borrowed and promise scene) and ch 22 (Amrit's eating house). A read-only helper agent (Explore) read chapters 1–33 in full and compiled a continuity digest. The digest covered:
- the yard's layout;
- Vell's call formulae and history (never stated to be Bronze);
- Lira's habits and lodging;
- Torvin's house;
- the district;
- the Log's form and instance count;
- recurring images.

The author used the digest for running details only. The helper wrote no prose.

**Drafting.** All seven chapters were written forward by the same author, in order. No formula or scoring tool was run between chapters. During and just after the run the author fixed blocking slips as they were noticed:
- **Weekdays.** In ch 41 the opening night moved to Tuesday (the fourth night of the step), and the keys became an extra Thursday at the mender's, whose days are Monday and Wednesday. Cael's "yes" to Vell moved to Wednesday, before the Corvane lesson. In ch 45, Hesk's reply now arrives on the second Tuesday and the bout reference reads "On Monday". Lira's "same time Tuesday" was also fixed.
- **Who has heard the word.** Vell must not know [SHATTERED] before Cael says it at her table, so Corvane now asks "What are you?" and Lira tells her that is his to tell.
- **Reader Standard / no romance.** A joke about the wall girls thinking Lira and Cael were "courting" was cut while drafting.
- **Hesk's history.** Hesk's reply was reworded so he claims nothing about what he saw of the old file.
- **Instance numbering.** The unasked step in the box drill is logged as the fifth instance, and Feryn's third exchange as the sixth.

The author checked raw word counts once after the seventh chapter (29.2k). It then wrote six further full scenes by the same author, each a brief item or supporting-cast beat that had been underwritten:
- Lira doing the step on purpose, and seeing his;
- the letter posted;
- Torvin's supper and Doss;
- the cooper's roof;
- Vell's terms said back, with Lira's ruling;
- Dessa at the board, the mender's key, and the Corvane return.

It also expanded the Fenrow interim bout and dramatized the Sunday Kestrel watch. Nothing was summarized or compressed to save length.

**After all seven existed:**
1. **Source-reuse pass.** `ed.sh overlap book-01-the-shattered 7` found **34 unprotected runs**, almost all in the Feryn bout (ch 46) and the dinner and notice night (ch 47), with one in Corvane's demonstration (ch 44). Each was rewritten by reading, with events unchanged. *When you figure it out, I want to know.* was set as a single untagged line, so it stands as protected wording. A re-run reports **0 unprotected runs and 1 protected run** (the notice).
2. **Formula metrics.** One run of `tools/formula_metrics.py` on the seven chapters. No formula-driven rewriting was done.
3. **Structural fix after the metrics run.** Two `---` breaks inside the Feryn bout were removed, so the bout is one scene as the task requires, along with one break inside Vell's cutaway. Three small wording fixes followed, about 40 words: the instance numbering, and an unexplained "chew on the left side". Overlap was re-run (still 0) and so were the gates (still 0). The metrics were not re-run. See AUTHOR-REPORT for the arithmetic effect on words per scene.
4. **Gates.** `ed.sh gates book-01-the-shattered 7` reports reader_standard=0, metadata=0 and modern=0 on all seven chapters.
