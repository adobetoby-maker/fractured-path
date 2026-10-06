# Repair brief — Book 5, Movement 5 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context, on the review seat.
The cold read saw the manuscript only.

**Verdict.** This is the book's strongest movement so far for texture and warmth. Both readers name:
- the corner game;
- Seln's joke;
- Umber's eve (the finest prose in the movement);
- Brom's five-exchange bout;
- Lira's screener bout.

The scale is felt, not counted. The scoring format is clear by ear on its one statement, and the two-number call
teaches itself. Daeva at a hundred yards builds from wariness to cold fear at the head-turn.

The editorial verified every ruling:
- **#39 continental format:** your added detail holds against every bout on the page and against BOOK_MAP §8's
  Lira–Zerin arithmetic.
- **#40:** no bouts for third, and the public capabilities at their documented rates.
- **#38:** ratings in band.
- **World rules:** no seasons, months, metres or English weekdays, and no year increments.
- **Cutaways:** all limits honoured.
- **Karis's door:** means the drafters.
- **Protected lines:** all verbatim.
- **Overlap:** 0 unprotected.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags
1. **The Daeva first-read log:** the editorial confirmed it is nowhere in BOOK_MAP, and no later book calls back to
   it. Your own-words log STANDS and is not protected.
2. **The continental format detail:** ACCEPTED as canon. An exchange closes at the bell or at three points. The bout
   stops when the trailer can no longer draw level. If the points are level after five, the figures decide. Note for
   M6: a four-exchange finish needs a margin over three.
3. **Staging:**
   - the banner enters last with the colour-guard alone, and its holder stays unnamed;
   - Auremont's file is reversed so Daeva leads;
   - the draw falls at dusk on orientation day;
   - the trial rules post on T4.

   All ACCEPTED, with the one-banner clarification in P3.
4. **Havel "knows the grade" of seat twelve:** ACCEPTED. He names no one and infers nothing beyond the grade. See P2.
5. **New canon:** Umber about forty years at the seals, with his late master in one line; "the Halcenvane wall" as a
   broadside nickname; Karis not saying Ivenne's name aloud. All ACCEPTED.

## Priority 1 — Brom's fifth exchange (both readers)
ch32, ll.93–97. The prose scores THREE Brom touches against one, then calls "Two to one. Nine to seven." Remove one
Brom touch. The cleanest way is to cut "Then Brom took another, plainly, through the middle, a breath before the
bell." That leaves the door point, the sweep and the final fist, which gives 2–1. The totals and figures stay as they
are.

## Priority 2 — Seat twelve, three passes (cold)
Vastin's cutaway and Havel's are the same seat-twelve scene twice, and Cael's view of the Compact row is a third pass.
- **Havel:** halve his cutaway to about 250 words. Give him ONE thing Vastin's lacked, something only a second-seat
  records officer would notice, and keep "Blank pages are the ones that get written last."
- **Vastin:** keep his aching-hand plant.
- **Cael:** let his pass at the Compact row carry only what he can see.

## Priority 3 — Counts, clocks and clarity (both)
- **ch30, the clock (cold).** "That night" is placed before the afternoon and dusk of the same day. Reorder the line,
  or re-time it.
- **ch32, l.345, the Compact row.** Cael lists eight people for eleven plated chairs, which doesn't match Vastin's plan
  at ch29 l.229 (six observation seats, two district officers, one liaison, two host). Make Cael's list match the plan
  (two district officers, no clerks), with one clause that the other observation seats "changed on the rotation".
- **ch28, the guesting house.** Make the floors agree: put the hill house above and the southern house below. Change
  Cael's room from "the top of the house" to "the top of Halcenvane's floor", or move him to an attic room.
- **ch32, l.287.** "The wool town's rule" becomes "the quarry town's".
- **ch27, l.39.** "thirteen more of her" becomes "twelve more of her".
- **ch32, l.289.** "There were and colour-sellers" has a dropped word. Fix it, and break the paragraph before "And all
  through it".
- **ch31, l.183, the banner.** Is it one cloth or two? Add half a sentence: "the colour-guard had brought it down from
  the gate at dawn", or similar.
- **ch30, l.141.** Rooke cites an off-page "map table" briefing about Umber. Make it "I'll tell you about him once,
  here", or similar.
- **"Eight thousand"** is stated about seven times. Let two go.
- **Optional (cold).** One reaction line from the Halcenvane block at Daeva's head-turn, so the house feels the count
  and not only Cael's notebook.

**Length.** Finish within 30,500–33,000 words.

## After the repair
Run:
- `ed.sh overlap book-05-the-silver-standard 5` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-05-the-silver-standard 5 5` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the six chapters.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- before/after metrics;
- the changelist, by chapter.

Edit only ch27–32 and AUTHOR-REPORT.md. Run NO git commands of any kind.
