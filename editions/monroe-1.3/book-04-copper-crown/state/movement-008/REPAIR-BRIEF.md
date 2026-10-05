# Repair brief — Book 4, Movement 8 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context, on the review seat.
The cold read saw the manuscript only.

**Verdict.** Both reviewers would continue. The editorial calls the Copper final and the fault second "the
best-built action in the book". The cold reader found all four measured rooms clear to a listener, with the
interview cleanest.

The editorial confirms:
- the calendar: the 19th, 20th and 21st, with Lira's hip ten days old;
- Lira's record: 9 + semifinal + final = **11 unbeaten, none lost**, which checks against the ledger;
- the final's 0–1 / 1–1 / 2–1 fits the four-exchange, more-touches rule;
- six trials with Ember second (C10), and the plate withheld and flat (C9);
- two public capabilities, and Shadow at zero deployment;
- "decision point" used exactly once;
- Vastin unaged and unwarning, Seln unnamed, Lira clean of the slip, and Ilsev reaching no conclusion;
- no new names, and no weekday or month leaks;
- every §10 protected line is exact;
- all the formula measures are inside range.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags (all ACCEPTED)
1. **The five tag-split packet lines.** They are now pattern-protected in `book-04-copper-crown/protected-patterns.txt`:
   - the vessel reading;
   - "is what a real semester looks like";
   - the most-competent-half-hour line;
   - "a cage built for people… who did not exist";
   - "Magister. I need an interval."

   **Rejoin each one whole.** Put the tag before or after the line, never inside it. The double-tagged Gault line is
   the audible seam the editorial heard.
2. The six reworded packet lines stand.
3. The final's first exchange is even, on her guard (0–1, 1–1, 2–1).
4. Trial 5 is new, and the frame weights run 1–5. Both are accepted, provided P2 below makes the six count to six on
   the page.
5. The small new canon is accepted.
6. **"Third one someday" said twice.** Keep the floor line at the eighth bell. Make calibration night's repetition
   unmistakably Brom echoing it, or cut it. The floor line must land as the original.

## Priority 1 — The doubled homecoming (ch55; both readers)
The party arrives in the common room twice.
- In the first arrival, Karis names Cael "a renewed enrollee" and makes the tray joke.
- In the second, she is found alone with a book "since the second bell", asks "Well?", and closes her eyes at
  *renewed*, as if hearing it for the first time.

Merge them into ONE scene:
- Keep the stair, Brom's ice, the coach-accident tableau and the tune exchange.
- Cut the second opening.
- Let Karis turn to Cael and ask about the glass ("And the glass? You said you'd tell me"), so "the column" is glossed
  as the thread in the straw.
- Keep the third word under the two (*a spark*, *a letting-go*, then "decision point"), the line drawn under all
  three, and "That's the last one. I can feel that it is."
- Fix the legs-and-arms joke so it counts, or make Karis miscount on purpose and get corrected.

## Priority 2 — Make the numbers true (both readers)
1. **The six trials count to six (ch53–55).** Karis's slate leaves a second slot that nothing occupies until Cael asks
   for Ember there. Make the posted second slot explicit on the slate in two or three sentences. For example, the
   wing keeps slot two "at the enrollee's placing", so Gault's "The six stand as posted otherwise" refers to something
   the page has shown.
2. **ch55, Gault's "Five of six have moved"** comes with two trials still unrun. Move it to the note at the end of the
   sitting, or make it "four so far, and one of them hasn't".
3. **11/12 called "the floor".** Karis's floor was five in six. Make it "a call above the floor".
4. **The protected M9 line.** In the ch55 four pieces, the audible release comes BEFORE Cael's correction. That would
   falsify the protected M9 notebook line "Correction preceded the audible release". Move one clause so the
   correction comes first.
5. **ch55, the glance tally.** It names six people and claims seven. Add the clerk, or say six.
6. **ch55 ledger.** "Drifts: two" and "it never flickered" sit in one entry. Change the second to something two logged
   drifts allow ("it never went").
7. **Brom's clock (ch51–52).** Decide whether it is cumulative from the walk-out or per exchange. Make ch51's "both had
   started" and ch52's "four minutes of iron and eleven seconds more" agree.
8. **Brom's strapped hand.** Give it its cause in one clause in ch53, after the book-and-fist rehearsal.
9. **ch53, "Weeks ago"** for an eight-day-old slip becomes "Eight days ago", or "a week ago".
10. **The incidental elevens.** "Eleven" carries about nineteen unrelated counts. Vary ONLY the purely incidental ones
    where another figure is free: porters' minutes, carrels, years of print, Karis's weeks, the seam-hunters. NEVER
    change a canon or protected eleven:
    - Lira's eleven bouts;
    - "eleven of twelve";
    - "eleven drifts" on calibration night (if it is the counted figure);
    - "eleven questions";
    - "subsection eleven";
    - Gault's protected "in eleven years";
    - Ilsev's "eleven months";
    - the delegation's eleven names;
    - "Lira has done it eleven times", if that is the packet line.

    List each eleven you changed in your report.
11. **Speakers (cold).** The unattributed "Two gone." echo in ch51 needs a speaker. In ch53, "The nearest chair-back
    took his grip" reads as Brom after Brom's line; name whose grip it is.

## Priority 3 — Rhythm: none required
All measures are in range. Do not add rhythm work. Rejoining the split lines will lift the mean slightly.

**Length.** Finish within 29,500–31,500 words.

## After the repair
Run:
- `ed.sh overlap book-04-copper-crown 8` (0 unprotected; the rejoined lines show as protected);
- `ed.sh gates`;
- `sweep_probe.sh book-04-copper-crown 8 8` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the six chapters.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the elevens changed;
- the clock decision;
- before/after metrics;
- the changelist, by chapter.

Edit only ch51–56 and AUTHOR-REPORT.md. Run no git commands.
