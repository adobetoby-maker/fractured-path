# Repair brief — Book 6, Movement 5 (one bounded same-author repair)

**Sources.** All on Sol (codex), fresh context:
- `review-editorial.md`;
- `review-cold.md`;
- `source-tracking.md`.

**Verdicts.**

| Read | Verdict |
|---|---|
| Editorial | Close with targeted line and cadence fixes. It delivers its story turn, keeps canon, honors the Reader Standard, and lands the midpoint acquisition with "unusually strong cause-and-effect". |
| Cold | Strong. Three local fixes. |
| Source distance | PASS — 6 genuine tracked passages, against M3's 136 and M4's 85. No densely tracked scene. |

The no-source method worked. Keep using it.

Text is frozen in `pre-repair/`. Repair by reading, never by script.

## Coordinator rulings on your flags

1. **The "Eight…" Tier B line.** Your middle words stand. The packet and map elide the middle, so the elided part is the author's.
2. **Flood geography:** ACCEPTED.
   - The town ferry and Ostrand bridge are closed (at the third ring on the middle pier).
   - The coach uses the upper chain ferry at the narrows.
   - It returns through the cut on the river road west of Ostrand.
3. **Anchor mechanics:** ACCEPTED as minted.
   - Fixed points, and lines between them.
   - A cage built from a first point set on his coat.
   - Release from inside.
   - Consistent with Book 7's ledger.
4. **Seln's ch29 press, "a little above where it should have sat… put there by somebody who could reach":** ACCEPTED. It carries no content and never says falsification; it is a fair plant for M6.
5. **The four-minute decision** in the exchange's yard, and **Withrow's private-book line:** ACCEPTED.
6. **Details:** ACCEPTED.
   - Lira's RIGHT ankle.
   - Brom's shoulder out and back in by itself.
   - Lira's three struck bouts.
   - Karis's boxed *for now* guess.
7. **"The eleventh of Sowing"** once, with no day count: ACCEPTED (#35/#42).
8. **The annex (cold-read item 2): NO CONTRADICTION.**
   - In this edition "the annex" is the house's name for the reading room plus the lumber room across the landing (M2, ch8).
   - "Tomorrow, Seln's annex" is a protected packet line.
   - Optional: add one clause in ch29, where the researcher's room is chosen, reminding the reader that the house calls the two rooms together the annex. Do not change the closing line.

## Must fix

1. **The six tracked passages** (`source-tracking.md`): 28:7, 29:23, 29:49, 29:133, 33:67, 34:177.
   - Break each chain: start from a different link, drop or invert a link, or let a link arrive off-page as its consequence.
   - At 33:67, the source's forty-minute and quarter-hour order of the two Storm resettlings survives. Change the order or the measure.
   - Do not reopen the source.
2. **ch30:41–43, the seal-number deduction** (editorial). "The two numbers were one apart" contradicts "the number between them": consecutive numbers have nothing between them.
   - Make the registered entries clearly sit on either side of the absent number, with no ledger line for it.
   - Recheck the three later references to the number and the gap.
3. **ch30–31, the attacker count** (cold). Ch30 reveals five masked men plus the woman: one at the cart, two from the north bank, two from the gully. Ch31's ring and withdrawal account for only four men plus the woman.
   - State whether the cart leader stays at the cart while four others close.
   - Give the fifth man one visible assignment and a withdrawal beat.
   - Do not shorten or reconceive the fight.
4. **ch30, the opening of Havel's audit** (cold). Add one short orienting echo that ties his seal rubbing directly to the gate order. Optionally trim one repeated statement of the seal's absence.
   - Keep all three independent register checks.
   - Keep the fact that the official form has no line for what he found.

## Cadence, and length (OWNER-DECISIONS #45)

The editorial asks for a restrained cadence pass in the procedural and introspective runs of ch28–30 and the explanatory parts of ch33. Join adjacent short statements only where they form one thought, and let a few clear compound-complex sentences carry deduction or reflection.

Do not touch:
- dialogue;
- protected text;
- the notice;
- the ch31 fight.

Do not chase decimals.

The owner has ruled (#45) that Movements 5–9 develop their planned scenes more fully, so the book lands nearer its budget. Your M5 is already at 99% of budget, so hold its length; the fixes above should not shrink it. No padding.

## After

1. Rerun from editions/monroe-1.3:
   - `bash tools/ed.sh gates book-06-the-compacts-hand 5` — target 0;
   - `bash tools/ed.sh overlap book-06-the-compacts-hand 5` — target 0 unprotected.
2. Rerun from the root: `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 5 5`.
3. Append "## Repair r1" to AUTHOR-REPORT.md.
4. No git.
