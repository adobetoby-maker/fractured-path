# Repair brief — Book 2, Movement 5 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Sol (review seat). The cold read
saw the manuscript only.

**Verdict.** Both reviewers would continue. They name these local payoffs:
- the Shield win;
- Lira's confirming win;
- the dinner friendship, including Brom's *"Being noticed"*;
- Cael's pulse.

All protected wording is exact, including *"systemic protocol, origin: registry sub-layer."*
Reserved truths hold. The editorial confirms nothing states deliberate integration, falsified
classification, UNBOUND naming Cael, or the watcher's identity. Source distance is the cleanest
yet: 0% skeleton, 6% close. Pre-repair text is frozen in `pre-repair/`. Repair in reading order,
in place, by reading — never by script.

## Coordinator rulings on your flags

Accepted:
- **The sub-layer line** in a registry marker index, dated before the file (consistent with
  Book 3's origin query).
- **Coss signs his upward note** and makes his first log entry (BOOK_MAP §3 D governs over the
  source).
- **Havel's quarterly review sheet.**
- **[UNBOUND]**: copied small, untold, one unlabelled stroke in Carrying. Vell knows "perhaps
  half" the margin words. The full reading is still owed.
- **The pulse as Cael's own "knock"** at about one in three. M6 must earn about half.
- **The Keth seed** without "declaration".
- **Havel and Coss slightly short.** Do not pad.
- **Lira** provisional, "One of two".
- **The dull-coat watcher**, unlinked.
- **The four reworded packet lines**, as written.

Vell's ages are fixed below (Priority 3).

## Priority 1 — The consent boundary (editorial; Reader Standard)

**Where:**
- ch32, the final Log rule;
- ch33, the market tests on the old man, the girl and the smith;
- ch34, the nightly sweeps.

**Problem.** Cael writes an absolute ask-first rule, then reads strangers without asking and
without recognising a breach.

**Fix.** Define on the page what the rule covers. Most plausibly, a *targeted* read of one person
beyond what their public presence gives off needs consent; sensing ambient presence in a public
place does not. Revise:
- the Log line, so it states that boundary;
- the first public test, so Cael stays on the right side of it or catches himself crossing it and
  names it, as he named his earlier wrong;
- every later sweep, so it follows the stated rule.

Keep the training sequence, the watcher detection, the supper's warmth and Cael's willingness to
name his own wrong.

## Priority 2 — Logic and say-it-once

1. **ch31, notebook security** (from Dace's *"Good thing we don't share"* to the evening recoding).
   Cael anonymises only fighters absent from Vell's ledger, which leaves ledgered fighters attached
   to exploitable weaknesses. Fix the logic in one move: anonymise every fighter identity in the
   private book, or state a real protection for the ledgered names. Keep Dace's story, the
   principle that records partly belong to the people in them, and Cael's choice not to destroy
   factual observations.
2. **ch35, Coss's chapter.** From Coss opening Havel's query through the file/index coda, Section
   Twelve, the missing authorization and the query chain are re-explained after ch33 already
   established them, and the coda repeats the rule again. Compress, so these arrive sooner:
   - Coss's self-protective courage;
   - the institutional silence;
   - the impossible pre-file date.
3. **ch34–35, the watcher sightings and the vigil.** The same diagnostic wording recurs at every
   sighting: level pressure, held on purpose, hardness underneath, gone when noticed. Keep the
   accumulation, but vary the wording and cut the middle repetitions after the market
   confirmation. Make the vigil cost or change something, however small.
4. **ch30, the opening.** It stacks scheduling, purse structure, ratings, betting, district
   commerce and names before the Lira scene gives a personal stake. Tighten lines and bring Cael's
   stake forward. This is not a structural rewrite.

## Priority 3 — Vell's chronology (editorial)

**ch36:** "Bronze at twenty-one … I had a few years of that … I was twenty-two" leaves about one
year at Bronze. Change only the duration phrase. Keep her ages, the bout and the break from the
guild.

**Length.** Finish within 35,000–37,500 words.

## After the repair

- Run `ed.sh overlap book-02-iron-circuit 5` (must stay at 0 unprotected), `ed.sh gates`,
  `sweep_probe.sh book-02-iron-circuit 5 5` and `formula_metrics.py` on ch30–36.
- Append "## Repair r1" to `AUTHOR-REPORT.md`: the consent boundary as now stated, the notebook
  fix, before/after metrics, and a changelist.
- Edit only ch30–36 and the report. Run no git commands.
