# Repair brief r2 — Book 6, Movement 4 (bounded second repair: source distance only)

**Source:** `recheck-r1.md` (Sol, independent).

**Verdict:** SECOND REPAIR, scoped to the **41 of 85** tabled passages still tracking:

| Chapter | Passages |
|---|---|
| ch21 | 7 |
| ch22 | 13 |
| ch23 | 2 |
| ch25 | 6 |
| ch27 | 13 |

These all pass and must not regress:
- continuity;
- the day-71 calendar;
- the burst ledger;
- the Seln/Shadow/cache boundary;
- the sealed Velmere letter;
- the escort order;
- the hearing-provision plant;
- the Crown-yard reconstruction;
- reader clarity;
- completeness;
- gates.

The coordinator has already applied Sol's one ch24 listening fix. Leave ch24 and ch26 alone.

Text frozen in `pre-repair-r2/`.

## What worked last time, and what to do

The M3 r3 method closed its last ten units. Use it here:
- Each remaining passage has a new surface, but it keeps the source sentence's internal chain (A → B → C).
- **Break the chain itself.** Use one or more of these:
  - begin from a different link;
  - drop or invert a link;
  - let one link happen off-page and arrive only as its consequence;
  - give the beat to a different carrier: object, Log, dialogue, or silence.
- Re-wording the same chain is not enough.

Each key is listed in `recheck-r1.md`, keyed to `source-tracking.md`, with its source chain described. Do not reopen the source chapters. The chain is described in the recheck; that is all you need.

Keep:
- all protected and packet wording;
- every planned event;
- the length near 30,400 (no padding).

## After

1. From editions/monroe-1.3:
   - `bash tools/ed.sh gates book-06-the-compacts-hand 4` (target 0);
   - `bash tools/ed.sh overlap book-06-the-compacts-hand 4` (target 0 unprotected).
2. From the worktree root: `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 4 4`.
3. Append "## Repair r2" to AUTHOR-REPORT.md: the 41 keys, each with its old chain and its new one.
4. No git.
