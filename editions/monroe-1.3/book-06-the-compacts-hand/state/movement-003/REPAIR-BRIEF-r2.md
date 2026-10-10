# Repair brief r2 — Book 6, Movement 3 (bounded second repair: source distance only)

**Source:** `recheck-r1.md` (Sol, independent).

**Verdict:** SECOND REPAIR, limited to the **91 of 136** tabled passages still tracking the source.

| Chapter | Passages still tracking |
|---|---|
| ch14 | 24 |
| ch15 | 12 |
| ch16 | 11 |
| ch17 | 4 |
| ch18 | 5 |
| ch19 | 14 |
| ch20 | 21 |

Everything else is RESOLVED, and none of it may regress:
- continuity;
- the sealed Velmere letter;
- Seln not told;
- the two hearing orientation beats;
- the cadence of ch15–16;
- the town count;
- the full stop;
- rhythm;
- reader clarity;
- the listening proof;
- protected wording;
- gates.

The current text is frozen in `pre-repair-r2/`.

## What "still tracking" means here

Your r1 changed entrances and scene devices. That was real redrafting, and Sol says so. But below the scene level, the same source content still runs in the same local order. Sol's examples:
- ch14 still moves query → advisory → request → "not asked, told", and re-dramatizes the source's station-request example.
- ch20's hearing still runs Jent's concessions → the remaining frame question → the four-part answer → the two-paragraph ruling → gallery movement → aftermath, in the source's order.

Where the PLAN fixes the order of events, for example the hearing's architecture, keep the events. Inside each passage, change what Cael notices first, what is shown and what is told, which detail carries the beat, and what is said aloud versus left in silence or the Log. A passage that follows the source's local sequence of observations is still tracking even when every word is new.

## The job

1. Open `recheck-r1.md`, section "### Source-distance passage audit". Each STILL TRACKING passage is keyed to `source-tracking.md`.
2. For each one, read the source sentence it follows once. Then close the source and rebuild the passage from your EVENT-LIST.md, with:
   - a different first detail;
   - a different internal order;
   - and, where it helps, a different carrier for the beat: dialogue for narration, narration for dialogue, an object, or the Log.
3. Keep:
   - all protected and packet wording;
   - the accepted new canon;
   - ch17's original bout;
   - ch20's opening honest-floor scene;
   - the two orientation beats;
   - the sealed letter in Brom's left pocket.
4. No padding. The movement is complete at 31,667 words; hold it near that.

## After

1. From editions/monroe-1.3, run `bash tools/ed.sh gates book-06-the-compacts-hand 3` (target 0) and `bash tools/ed.sh overlap book-06-the-compacts-hand 3` (target 0 unprotected).
2. From the worktree root, run `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 3 3`.
3. Append "## Repair r2" to AUTHOR-REPORT.md: a table of the 91 keys, each with its old local order and its new one.
4. Run no git commands.
