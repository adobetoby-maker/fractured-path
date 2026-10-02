# AUTHORSHIP — Movement 6 (chapters 34–40)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-01-the-shattered/state/movement-006/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-01-the-shattered/packets/MOVEMENT-006.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 1 — The Shattered |
| Chapters | `editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-34.md` … `chapter-40.md` |
| Date | 2026-10-02 (one session, no restart) |

**Reading before drafting.** The author read the compiled prompt in full and source `chapter-15.md`. The author read chapters 28–33 of this edition in full. From chapters 1–27 the author read the Renn I bout (ch 12), ch 18 (the step, the drop and Lira's view), the Borrowed and promise scene (ch 26) and the Dessa letter (ch 27). A read-only helper agent (Explore) also read chapters 7–27 in full and skimmed 1–6 to compile a continuity digest: the yard's layout, Vell's call formulae, Renn's tells, Lira's curriculum, Torvin's house and the district. The author used that digest for running details only. It wrote no prose. The author also checked the Bible's fragment-notice format and the later books' recall of Sarel, Talis and Corbin ("Talis's ground vibration, Sarel's closing speed").

**Drafting.** All seven chapters were written forward by the same author in one run, with no scoring between chapters. During the run the author corrected blocking slips as they were noticed:
- **New names.** A stray name in ch 35 ("Hollis") and one in ch 36 (a guild member's name, struck as written) were removed. The guild hall's street name was also removed. No new names remain.
- **Time references.** Weeks and months were recounted against the day count: "two months" since Renn I, not seven weeks.
- **What Hesk can know.** Hesk's letter line in ch 35 and his ch 36 thoughts were reworded so he knows only what Cael's letters said.
- **Hesk's form of address.** Alis calls him "Master Hesk", since "Hesk-ward" is Cael's name.
- **Lira's academy.** Year counts were removed (M2 ruling) and nothing was added about her life before it.
- **Tuesday card.** Sarel's first watched bout was moved to the afternoon card.

Writing forward, the author checked word counts twice between chapters (after ch 34 and after ch 35) but ran no formula or scoring tools.

**After all seven existed:**
1. **Source-reuse pass.** `ed.sh overlap book-01-the-shattered 6` found **3 unprotected runs**: Dellin's line in ch 39, and two in ch 40 (the gathering sentence and the *Not yet* entry). All three were rewritten by reading, events unchanged. The tool now reports **0 unprotected runs and 0 protected runs**. One later one-word edit (ch 35, "forty miles" → "a week") was re-checked: still 0.
2. **Formula metrics.** One run of `tools/formula_metrics.py` on the seven chapters. No formula-driven rewriting was done.
3. **Gates.** `ed.sh gates` reports reader_standard=0, metadata=0 and modern=0 on all seven chapters.
4. **Day-count fixes after the metrics run.** Writing the state section of the report exposed some week and day references that did not match the day count, and these were corrected by hand, wording only. In ch 37: "eighteenth morning since the board", and Brenna "three weeks ago". In ch 38, also "three weeks ago". In ch 39: Dellin given "on the Monday after Talis"; his earlier bouts "a Thursday and a Sunday in the third week"; the fortieth *gone* "near the end of the fifth week"; and Cael's fallback "Then I'll say gone, and do something else". About 40 words changed in all. Overlap was re-run (still 0) and so were the gates (still 0). The metrics were not re-run.
