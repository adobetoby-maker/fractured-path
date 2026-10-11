# Repair brief — Book 6, Movement 6 (one bounded same-author repair)

**Sources.** All four on Sol (gpt-5.6-sol), fresh context:
- `review-editorial.md`
- `review-cold.md`
- `source-tracking.md`
- `reserved-truths-audit.md`

**Verdicts.**
- **Editorial:** close after two line fixes. It calls the movement "the book's central revelation with unusual patience and moral force". These all hold:
  - calendar;
  - injuries;
  - knowledge boundaries;
  - fragment limits;
  - the secret reach;
  - reserved disclosures;
  - protected wording.
- **Cold:** two priorities.
- **Source distance:** **PASS, 5 tracked passages**, and no dense scene. Ch40 scene 5 has 0.
- **Reserved truths:** PASS WITH LINE FIXES.
  - The Kindling mechanics PASS against the B7 and B8 reservations.
  - The older word spoken once by Karis PASSES.
  - Two ch37 line fixes keep Seln's seal terms consistent with Book 7's witness- and exposure-based logic. **The coordinator has already applied both.** Re-read ch37 in context and do not undo them.

Text is frozen in `pre-repair/`. The two reserved-truths fixes were applied after the freeze. Repair by reading, never by script.

## Coordinator rulings on your flags

1. **The room:** follow the page. Karis's reading room, with the shelf empty on the morning of day 88. ACCEPTED.
2. **Kindling (the corrections function failing safe; the bracketed word written over the old name):** ACCEPTED. The reserved-truths audit passed it.
3. **Seln's seal terms:** ACCEPTED as amended by the audit's two ch37 fixes. In substance: while its use can be seen by anyone who could carry the seeing west, it stays sealed.
4. **The clean door:** ACCEPTED as PROVISIONAL. Fix its trigger sentence (below).
5. **Anchor perception figures** (about 10 / 12 / 14 ft, *for now*): ACCEPTED.
6. **Vastin tells the junior aloud to continue observation, files nothing, writes nothing:** ACCEPTED.
7. **The rule said by five,** with Cael's "Nothing about me" and Seln's "Nothing about the boy": ACCEPTED.

## Must fix

1. **ch38:173, the clean door's forty-day trigger** (editorial).
   - The problem: the prose says the clock follows "the last sitting he failed to attend", but it calculates from day 75, a sitting Cael attended.
   - The fix: repair only the trigger sentence so it states the mechanism unambiguously.
   - Keep: day 75, day 115, the *fled* entry, the four marked files, the post-ruling good-standing door, Karis's three-part proof, and Lira's "we don't run, we walk".
2. **ch40:279, "Five young people and a man at a window"** (both reviewers). The room holds Cael, Lira, Brom, Karis and Seln: four young people and the man at the window. Make it "Four young people and a man at a window". Change nothing around it.
3. **The five tracked passages** (`source-tracking.md`): 36:89, 37:178, 39:95, 40:119, 40:163.
   - Break each chain: begin from a different link, drop or invert a link, or let one arrive off-page.
   - At 37:178, rework only the unprotected lead-in (the long look, the unreadable face, the delayed speech). Keep the protected sentence that follows.
   - Do not reopen the source.
4. **Explanatory echoes** (cold read). The places to look are ch36:51–79 and 199–203, ch39:65–165 and 189–217, and ch40:154–197.
   - Compress only the sentences that paraphrase a conclusion the immediately preceding document or dialogue has already established.
   - Do NOT remove an evidence class, and do NOT shorten Vastin's silent read or the east-hall learning scene.
   - Keep all of these:
     - the father's letter;
     - the coal-order analogy;
     - Seln's mother's ledger;
     - Karis's entered limit;
     - "It's not evidence. It's a map.";
     - Vastin's three refusals.

## Length (OWNER-DECISIONS #45)

M6 is about 105% of budget, which is right under the owner's ruling. The echo compression may trim a little. Do not pad back what it trims, but do not cut scenes either.

## After

1. From editions/monroe-1.3, run:
   - `bash tools/ed.sh gates book-06-the-compacts-hand 6` (target 0)
   - `bash tools/ed.sh overlap book-06-the-compacts-hand 6` (target 0 unprotected)
2. From the worktree root, run `bash editions/monroe-1.3/tools/sweep_probe.sh book-06-the-compacts-hand 6 6`.
3. Append "## Repair r1" to AUTHOR-REPORT.md.
4. No git.
