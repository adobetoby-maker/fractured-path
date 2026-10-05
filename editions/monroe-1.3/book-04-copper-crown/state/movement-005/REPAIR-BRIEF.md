# Repair brief — Book 4, Movement 5 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Sol (review seat). The cold read saw the
manuscript only.

**Verdict.** Both reviewers would continue without hesitation. Here is what they singled out:
- **Strongest pull:** ch32–34. The fire-watch slate becomes an alarm, the three nights make attention physical,
  and "The door stood open. A man was standing in it" is the cleanest turn.
- **Seln:** he is magnetic because his care lives only in conduct.
- **Clean on the editorial's checks:**
  - the notice is verbatim, including line order and punctuation;
  - every other protected anchor is exact;
  - Seln never learns anything;
  - Jessup's client stays unidentified;
  - the anomaly appears only in the inventory;
  - reserved truths stay at altitude;
  - the Reader Standard passes;
  - source distance is clean.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings
- **The closing countdown: "seventeen days" STANDS.** The plan's protected Log said "nine weeks", but that
  collides with M4's closed and protected "Six weeks. I'll see you in the final." It also collides with the plan's
  own dates: the final on the nineteenth of Reaping, the evaluation on the twentieth. BOOK_MAP §9 is now amended
  to "seventeen days". Keep the ch37 board ("Sixteen days to the final, and the semester evaluation the day after
  it") and the Log exactly as they are. OWNER-DECISIONS #35 records the one residue, the Sowing month name.
  - Do not state which month follows which, or any day count between a Sowing date and a Reaping date.
  - Check ch30–37 for any such statement and remove it if found.
- **Seln's "thirteen weeks" (from d51): ACCEPTED.** The packet's "nine weeks" was a planning approximation.
- **Gwen: closed by policy.** OWNER-DECISIONS #11 lists her as a placeholder until approved. Draft under the
  screened proposal (as with Abbot, Bede and Maud, and Book 3 #12) so one find-and-replace applies the owner's
  choice. No change.
- **Your flags: ACCEPTED.**
  - Private Wind sessions on the quadrangle flagstones.
  - The senior clerk in the registrar's office.
  - Lira's letter to Hesk "a year ago" set at Greyvane.
  - Brom's pear-fork story.
  - Shadow settles further out than the Iron read.
  - No count of unit sessions.
- **Cael's grandmother: ACCEPTED, with care.** "I never knew her" must mean *he has no memory of her*. Hesk's
  protected note says she held him the day he was born, and Book 8 has Cael's guardian passing on her sayings. Do
  not state when or how she died, and do not add anything Hesk told him beyond the note. "Ask." is a good close.

## Priority 1 — Make the numbers true (both reviewers)
1. **Brom's count (ch30, ch35).** Ch30 says "Twelve boxes. Three weeks, four a week" on d144. But the nineteen
   began at Brom–Tarn (s12, ≈d128), only about two weeks earlier, so at four a week the count can be eight or nine
   at most.
   - Use your day table to restate ch30's count and its weeks correctly.
   - Re-time "number nineteen" in ch35 at four a week from the corrected figure.
   - Check that every other mention of the count agrees. Karis keeps it exactly, and readers trust her.
2. **Cael's sleep across the operation (ch32–35).** As written:
   - ch32: "three hours after the last bell";
   - ch33: "two hours" after the first watch;
   - Lira: "four hours in two nights";
   - ch34: "four hours of sleep in three nights";
   - ch35: "seven hours' sleep in four nights".

   These don't reconcile. Fix the three or four affected sentences so the hours add up night by night. Do not
   alter the watches, their timing, or the recovery arc.
3. **Keep, don't lose:** Cael's admission that taking the fire-watch quarter-sheet was probably theft must
   survive any trimming (editorial, Reader Standard note).

## Priority 2 — Say it once (both reviewers)
- **ch30–31, the offer and the council.** Cael's three-sheet reading of Seln's offer and the common-room
  trap/no-trap debate revisit distinctions ch30 already worked through, before the unchanged coats and the signed
  contingency move things forward.
  - Tighten only the duplicated reasoning.
  - Keep every voice's distinct contribution: Brom's public-recruitment logic, Karis's four readings and her
    unprofessional sentence, Lira refusing and then arguing the other side.
  - Keep the Log's "So: both".
  - Add at most one unobtrusive orienting phrase that reminds a reader what the signed minute and rule two are.
- **ch35–36, mechanics restated.** The new fragment's integration comparison, the idle-state explanation and the
  working-ledger setup each re-explain what the reader already holds. State each mechanic once, at its clearest
  point.
- **ch36, the ladder (cold).** In the transition into the wash-house trials, add or sharpen one sentence making
  clear that the ladder gave an *ordinary* model of attention going elsewhere, not a successful use of the
  fragment. Leave the experiments and failures intact.

## Priority 3 — Sentence architecture, by hand, where you are already working (editorial)
The working ranges pass: sentence mean 13.57, ≥40-word share 3.6%, 922 words per scene. But FK is 4.41, the
spread is narrow, and the paragraph median of 29 is already at the ceiling.
- In ch30's file and audit rationale, the ch31 council and Log, and the abstract explanations in ch35–36: join
  adjacent clipped explanations that are one thought into clearly subordinated sentences, and cut true restatement.
- Do not alter dialogue, protected wording, the notice, scene breaks, the three-night operation, or ch37's warm
  simplicity.
- Do not raise the paragraph median.

**Length.** Finish within 37,000–39,000 words. P2 trims are expected.

## After the repair
Run:
- `ed.sh overlap book-04-copper-crown 5` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-04-copper-crown 5 5` (stay ≤ 5% skeleton and ≤ 13% close);
- `formula_metrics.py` on the eight chapters.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- before/after metrics;
- the corrected Brom count and sleep ledger (night by night);
- an updated day table if anything moved;
- the changelist, by chapter.

Edit only ch30–37 and AUTHOR-REPORT.md. Run no git commands.
