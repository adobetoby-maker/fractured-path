# Repair brief — Book 3, Movement 6 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the
cold read is manuscript-only). Both would keep reading. The "spark, not fire" discovery and the
gauntlet are genuine highlights; Coss as a decent antagonist is the freshest thing in the
movement; it ends a week and a half short of the hearing with exactly the right amount withheld.
Reader Standard passes; all five coordinator notes met. Pre-repair text is frozen in
`pre-repair/`. Repair in reading order, in place, by reading — never by script.

**Rulings on your flags:** the calendar is consistent (the only calendar defect is inside the Coss
cutaway — Priority 2); all new canon is accepted (Oona Kindles Anchor, Copper; the voiceless
observer rule; Coss over the draper's shop; "a spark" as rewording one; the taxonomy master as
Prynn's former reader); the Coss cutaway's length stands; progression vocabulary is honest drift.

**Leave untouched — clean, invented, and strong:** chapters 40–41 (except the Priority 2 and 3
items), and every new episode: the bench, the tests, the gauntlet, D6, the witness interviews,
the clap, the draper's window. Every protected and brief-quoted line stays exact.

## Priority 1 — Re-compose the retold scenes of ch42–46 (the main work)

The editorial review found these scenes are close paraphrase of source chapters 15–17: 23–32% of
sentences in ch42–44 follow a source sentence in order, word for word, with words varied inside.
Rebuild them as new prose:

- **Rebuild (about 9,600 words):** ch42 scenes 3, 4 and 6; ch43 scenes 1 and 4; ch44 scenes 3 and
  6; ch45 scene 4; ch46 scene 5 and the opening of scene 2.
- **Re-touch (about 2,400 words):** ch44 scenes 1 and 4; ch45 scenes 2 and 3.

**Method (the edition brief's new "Draft from your own event list" section):** for each scene, list
its events in your own words — what happens, in what order, who wants what, what changes, which
protected or brief-quoted lines it must carry. Then close the source and write the scene fresh from
that list: your own entry point, your own order of beats, your own sentences. Do not reopen the
source chapters while writing. Copy protected wording only from BOOK_MAP and the packet. Keep every
event and every protected line; change the construction. As you go, fold in paragraph breaks at
thought-turns (ch42–45 run long), remove the doubled "That was why the schedule had/carried no
scars" sentence in ch45, and merge the two stub scenes the editorial review names.

## Priority 2 — Coss's clock, his lever, and line slips

- **Coss's clock (ch41 → ch42):** he reads Oona's notation "eight days" after the Tuesday of week
  18 and sets out the following Tuesday, yet is at the gate on the Monday of week 19 — impossible by
  at least three days. Compress his approval-and-journey chain so the arrival stands, or move the
  arrival to week 20 and shift the later week labels by one — whichever keeps the hearing's week
  fixed (filing early week 19, delegation week 21, hearing week 22).
- **His lever (cold read):** in ch42 Coss's lever is Greyvane's charter, not Cael, yet Cael's "no
  authority over me" stands unchallenged across ch43–46. Add one short exchange — Naveth or Prynn —
  that names the charter, and let Cael box it as *not yet*, turning the hole into suspense for the
  hearing.
- **Slips:** Oona is called "a thirteen-year-old" at her own Kindling (Kindling is at fourteen —
  she has turned fourteen, or the line goes); the duplicated "no scars" line (also Priority 1);
  mark the sitting's post in ch46 as a different post from the burnt one; recast "walked him to the
  stable for breakfast he did not want and ate"; soften "oldest instrument in the world" and "a few
  hundred years" (no dating that leans on later reveals).

## Priority 3 — Rhythm, small

The ≥40-word share (5.1%) sits in ch40 (6.0%) and ch41 (8.1%), not the archive chapters: split
about twelve long sentences there by reading. Rebalance scene spacing in ch42–44 as part of the
rebuild. Keep sentence mean and words per scene in range.

**Length.** Finish within 35,500–38,500 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-03-no-path-given 6` (8-word runs; must reach 0
unprotected) and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the seven chapters,
then append "## Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, the overlap summary,
which Coss-clock option you chose and the weeks as they now stand, the charter exchange,
changelist by chapter and scene). Edit only the seven chapter files and AUTHOR-REPORT.md.
