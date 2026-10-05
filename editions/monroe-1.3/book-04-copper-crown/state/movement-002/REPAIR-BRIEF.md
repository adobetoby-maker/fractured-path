# Repair brief — Book 4, Movement 2 (one consolidated same-author repair)

**Sources.** Two reviews, both by Sol, the review seat: `review-editorial.md` and
`review-cold.md` (the cold read saw the manuscript only). Coordinator measurements are added.

**Verdict.** Both reviewers would continue. The baseline pays off the wait: the trials stay
dramatic without becoming a conventional fight. Cael volunteers his ceiling, catches the
dragging release and withholds Pressure. Seln testing the very blind spot the movement teaches
(Cael is wary of people who stare; Seln's trade is not looking) is the hook. Pre-repair text is
frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags

- **Accepted:**
  - Rooke's twelve-day bench (reconciles Brom's silence at day 21);
  - Lira signing "by the fourteenth" on the twelfth;
  - the sprung-oak demonstration floor with brass grid (matches §7 "four free");
  - the five packet lines you recomposed;
  - all other new canon.
- **Lira's Fenmark Arbiter reading,** "about a minute and a half": no earlier edition book
  states her timing, so it is accepted as new canon. Keep it consistent across ch9 and ch12.

## Priority 1 — Counts and calendar (both reviews)

This book is built on counts, records and measured intervals; every number must close.
1. **ch8 (l.3, l.153–185).** A three-session discovery, the fortnight after it and a narrated
   tenth day cannot fit between the twenty-second morning and the thirtieth evening. Change the
   concluding day, the opening day or the duration. Then check the joins against the
   thirty-third-day Lattice visit and the forty-eighth-day baseline. Keep the whole false-feed
   learning sequence.
2. **ch9 (l.47–77).** The Crown-yard rule says three exchanges, but the bout runs four and scores
   3–1. Correct the rule line to the actual victory condition (e.g. "first to three clean
   touches"). Do not rescore or shorten the bout; keep all four adaptations.
3. **ch10 (l.103–115).** "Four bursts for what three used to cost" is not "a third off" on the
   same denominator. Fix the comparison phrase so the denominator and the fraction agree. Keep
   "four free" and the unshortened landing beat.
4. **ch9 → ch10.** "Inside ten days she had fought nine and won nine" against day thirty-two's
   "I'm eight and nil": ch10 rewinds without a cue. Add one temporal signpost at ch10's opening
   or before the day-twenty-eight scene, and make the two counts agree on the page.

## Priority 2 — Source distance and say-it-once

1. **Close paraphrase is 20% overall** (event-list baseline about 11%), with ch14 at 29%.
   - Scenes at 30% or above: ch12 s4 and s5, ch14 s7.
   - ch14 s4 is 51%, but that is mostly Seln's protected brief and the officer's line; leave the
     protected text and recompose only the unprotected sentences around it.
   - For each listed scene, run `SHOW=1 bash editions/monroe-1.3/tools/sweep_probe.sh book-04-copper-crown 2 2`.
     Recompose the sentences at ≥0.35 in your own construction, source closed. Change the shape;
     do not swap synonyms.
   - Target: close share 15% or lower overall, and no unprotected scene above about 25%.
2. **ch12, from Karis's "laid against" through the fourth-evening common-room decision.** The
   low-line/high-line dilemma is restated across several nights before the group scene restates
   it again. Compress the repetition so the common-room debate comes sooner. Keep the ethical
   distinction and Lira's third option.

## Priority 3 — Rhythm and density (light)

- **Sentence mean** is 13.08, at the floor. Join a few one-thought narration runs while you are in
  the scenes above.
- **"That"** runs about 112 per 10k; thin it where easy.
- **Progression vocabulary** is about 80 per 10k against the packet's 90. Raise it only where it
  comes naturally.
- **Scene lengths:** four scenes are under 850 words. Merge only where it is the same place and
  time.

**Length.** Finish within 32,000–34,500 words.

## After the repair

- Run `ed.sh overlap book-04-copper-crown 2` (must stay at 0 unprotected), `ed.sh gates`,
  `sweep_probe.sh book-04-copper-crown 2 2`, and `formula_metrics.py` on ch8–14.
- Append "## Repair r1" to `AUTHOR-REPORT.md`: before/after metrics, the probe's skeleton and
  close shares per chapter, the calendar fix chosen, and a changelist.
- Edit only ch8–14 and the report. No git commands.
