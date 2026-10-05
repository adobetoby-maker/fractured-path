# Repair brief — Book 4, Movement 7 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context. Fable has the
review seat while Sol is out of quota. The cold read saw the manuscript only.

**Verdict.** Both readers would continue. What they name:
- the pen-count device ("He is calibrating the instrument. I am the reading."), which is wrong in exactly one of
  the five marks, and only the reader can see which;
- the drill run on the frame;
- the folder-and-foot beat;
- the three windows, where head-of-view is always identifiable, usually from the first sentence.

The editorial confirms every Book 4 ruling:
- the calendar holds: 13th–15th, then the 19th and 20th;
- only Wind, the Iron read and the thin Ember exhibit are visible;
- Vastin has no age;
- Seln's nulls go undetected;
- "unbound" appears once, unlinked;
- there are no new names and no "decision point";
- every protected line is verbatim;
- the Reader Standard passes;
- overlap is 0 unprotected.

All twelve of your flags were judged acceptable. Pre-repair text is frozen in `pre-repair/`. Repair in reading
order, in place, by reading — never by script.

## Coordinator rulings on your flags (all ACCEPTED)
- Ilsev's interval is "eleven months", following the edition calendar.
- This is her second return. Book 3 ch52 had the first. Her new filing is her second referral.
- Events moved to the 14th are fine. Havel's fourth entry is written at the second recess.
- Karis's single-directive link is accepted.
- The small new canon is accepted.
- The capitalised maxim and the ladder bout "for the fifth line" are accepted.
- **Rejoin the two split lines.** They are now protected patterns in
  `editions/monroe-1.3/book-04-copper-crown/protected-patterns.txt`:
  - Havel's "Two years. Two of us now. Nothing has ever come back with a name on it.";
  - the close, "Four days to the final. Five to the twentieth."

  Set each as you meant it, as one paragraph or one line. Overlap will report them as protected.
- **"Half-metre" stays.** It has been the edition's term for the air round the body since ch34 (closed M5–M6).
  The cold reader's "arm's length" is not taken.

## Priority 1 — Continuity line fixes (editorial; cold)
1. **ch45, the red bundle.** "Two years of demonstration sittings… fourteen and then fifteen" is wrong. Book 3
   fixes ONE semester of fourteen sittings, with Cael at fifteen throughout. Correct the clause to match.
2. **The inky-knuckled clerk.** She is "on the next chair" in ch48, but "two places along", with empty seats either
   side of Cael, in ch49. Make it one seat.
3. **Brom's boxes.** The unexplained shift to nightly boxes contradicts the ledger: four a week, all nineteen done
   around d160, then round two. Either say in a clause that round two runs nightly, or keep it to four a week.
4. **Havel's "a much younger man"** for two years ago: soften it, or make it his own wry exaggeration.
5. **Day names (cold).** ch49's "Saturday" and "Monday" must use the book's scheme (Fifth-day, Sixth-day,
   Seventh-day, First-day…). Grep ch45–50 for any other English weekday name and fix it.
6. **Arithmetic (cold).**
   - ch47 "Day sixteen" against "a month": make the stair-night origin explicit, or correct the number.
   - ch47, the 31st repetition and "the last one": make them agree.
7. **Referents (cold).**
   - ch48: "Seln" at first naming should be anchored ("Seln, at the copying table").
   - ch50: the "he sat down at the window" just after Brom "went up" becomes "Cael sat down…".

## Priority 2 — Ch49: the return read once, and the lead re-anchored (both)
The return's three sentences are set out on the sheet, quoted again in Ilsev's Greyvane memory, paraphrased, then
copied whole into Havel's notebook. About 2,900–3,800 words pass without Cael.
- In Ilsev's Greyvane memory, drop the second verbatim quotation ("She had met the first two sentences before"
  carries it).
- In Havel's working-room section, cut the verbatim fourth-entry text to a one-line summary. Keep:
  - "Two carriers now…";
  - the broken rule and the protected three-line Havel quotation, rejoined;
  - "written by a man";
  - the cross-referenced three sheets;
  - the courier section whole, including his filing the return in its place.
- Then place ONE short Cael beat between the two windows, a few hundred words at most. Move the live fourth pen
  mark into it if you can do so without changing what the reader knows and Cael does not. Mark four, which Havel
  does not see, must survive where it is.
- Net: ch49 should lose 300–500 words.

## Priority 3 — Anchor the word, once (cold)
In ch50, Karis's directive scene and Cael's numbered entry are the movement's climax. The six chapters never say
that *Shattered* is the category on Cael's own sheet.

Add ONE factual clause, in Cael's head or in Karis's mouth, that *Shattered* is the word on his own registry sheet.
Nothing more:
- no theory;
- no claim about what he is;
- no link from "unbound" to his nature.

The scene's restraint is the point. Keep "a coincidence with good posture", Karis's refusal, the one line on the
empty page, and Cael's part 3.

**Length.** Finish within 29,000–31,000 words.

## After the repair
Run:
- `ed.sh overlap book-04-copper-crown 7` (0 unprotected; the two rejoined lines show as protected);
- `ed.sh gates`;
- `sweep_probe.sh book-04-copper-crown 7 7` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the six chapters.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- before/after metrics;
- the changelist, by chapter;
- an updated day table if anything moved.

Edit only ch45–50 and AUTHOR-REPORT.md. Run no git commands.
