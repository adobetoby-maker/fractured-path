# Repair brief — Book 5, Movement 3 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context, on the review seat.
The cold read saw the manuscript only.

**Verdict.** Both reviewers call this a strong movement, the best material in the book so far:
- Lira's Fenmark arc;
- the page-three funnel;
- the slate hall as an opponent.

The cold reader wants the next part. The scouting economy is clear by ear. Lira's bout is the dramatic peak and the
quay is the emotional one, and they do not undercut each other.

Canon is clean:
- every figure re-sums under #38, with the bands holding;
- bursts are 3 of 4 on slate;
- the left seam, Pressure flat, Compression banked and Shadow zero are all as they should be;
- no seasons, the weekdays are right, and the year counts are not incremented;
- protected lines are exact;
- overlap is 0 unprotected.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags (all ACCEPTED)
- **The market moved to the quarry town:** accepted, because M2 left the mill town without it.
- **Lira's third title:** accepted.
- **Brom's funnel and honest final:** accepted.
- **An exhibition throw counts as a touch:** accepted. Add it to the #39 note.
- **Slate gives four free bursts a day:** accepted.
- **The grappler is a Stone Path:** accepted.
- **Fenmark's third-form gap on the left foot:** accepted.
- **Auremont is correctly NOT the banner-holder:** accepted.
- **The null report closes the movement:** accepted.
- **Seln's "fifteen years":** accepted as new canon. It will be recorded in the ledger.

## Priority 1 — Lira's Iron final: the touch count (editorial)
ch18, ll.107–113. The summary says "in four exchanges, two touches to one". The narration, though, gives Lira touches
in the second, third AND fourth exchanges, and under #39 the bout ends at her second touch. Fix it in one or two
sentences:
- **Either keep "in four":** the third exchange runs out with nobody touched, and the decisive touch comes in the
  fourth.
- **Or change the summary** to "in three exchanges, two touches to one", and delete "and the fourth exchange's after
  it".

Keep "She did not follow. She stopped in the middle of the floor on dry flags… and let him go." and "That was your
bout. I only fought it." Update your report's table to match.

## Priority 2 — The clocks (cold)
- **ch19 quay.** "And this morning there they were" is two days late at the payoff line. Make it "And on the Fifth-day
  morning there they were", or similar per your day table. Also fix "So all day I've been asking" (→ "for two days")
  and "I've been saving the coat-rack" (→ "…two days").
- **ch15, "the whole of the five days on the road".** The silence ran five days, and only two were on the road. Make it
  "the five days of the silence", or similar.

## Priority 3 — The Seln cutaway, and the file-trade vocabulary (both)
- **ch17, ll.95–107, the reasons block.** The two reviewers pull opposite ways: the editorial wants more picture, the
  cold reader wants it shorter. Do both in fewer words:
  - Compress the block to three or four sentences.
  - Give each of the four items one concrete picture-word: the post locking in the east hall; Jask, a third-year
    "quick off a read" in the queue; "the guest floor", where the delegation worked; the one slip of wing paper.
  - Keep "He had had the word since last year, and he had not got it from figures."
  - State NO reason and NO mechanism.
  - Trim the paper paragraphs (ll.73–79) by one sentence.
  - In the in-head deduction (ll.117–151), keep "door, record, man, company" and the stair, and hold the
    payment-method evidence back for the table, so Seln has something new to say to Karis.
  - Net: about 250–400 words out. Keep "*Managed?*", "The first time through… the second time, he read it for how it
    had been made.", "Offices insist. Shops make do." and the quarterly.
- **ch17, ll.171–173.** Seln must not KNOW what is on Karis's private page before he sees it. Make it his inference
  ("he had no doubt it was open in Karis Dellenmoor's grey notebook too, under a heading of its own").
- **The file trade by ear.**
  - Use "shop" (or "firm") for the commercial compiler throughout ch17, not "house".
  - Anchor "the office" with one early clause ("the office that had put him behind the counter").
  - ch19 "mispriced *too*" becomes a referent ("mispriced the other way from Cael", or "mispriced. The dangerous
    direction.").
- **Audio referents (editorial):**
  - ch15, ll.137–143: Cael's "Four free on this, in a day" against Lira's "Three a bout for me". Add one clause marking
    a day's price against a coach's per-bout rate.
  - ch16:311 and ch18:95: two different valley Blades. Tag one ("the other valley Blade").
  - ch19:447: "He read them as he ate" reads as Brom. Fix the referent or cut the clause.
- **ch19, the four stacked codas (cold).** If one is a restatement, cut it. Keep the null report as the close.

**Length.** Finish within 31,500–34,000 words.

## After the repair
Run:
- `ed.sh overlap book-05-the-silver-standard 3` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-05-the-silver-standard 3 3` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the six chapters (keep the paragraph median ≤ 30; ch17 is at 31).

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the final's touch count as now written;
- before/after metrics;
- the changelist, by chapter.

Edit only ch14–19 and AUTHOR-REPORT.md. Run NO git commands of any kind.
