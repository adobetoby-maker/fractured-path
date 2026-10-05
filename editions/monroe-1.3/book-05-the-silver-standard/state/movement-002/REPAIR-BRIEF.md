# Repair brief — Book 5, Movement 2 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context, on the review seat.
The cold read saw the manuscript only.

**Verdict.** A strong movement. Both readers would continue.

The editorial confirms that the ruled canon holds:
- every rating is re-summed under #38 and sits in its band;
- year counts are not incremented;
- the second semester evaluation is routine, with the plate flat;
- there are no slips in season words, weekdays or names;
- Seln infers management only;
- all 16 protected and packet lines are exact;
- overlap is 0 unprotected.

The cold reader can follow who is fighting, the scores, and why the tidy figures matter. The freshest bouts are the
people-read ones: Brom's hinge, Karis and Lira's hand, Ephram's late half-turn.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags (OWNER-DECISIONS #38 aligned; #39 new)
1. **The Iron split at the fifth rank** is a HOST OPTION the charter allows, not custom. The mill town exercised it;
   the confluence (M4) will not. In ch11 (about l.89), "third season at the head of the lower Iron" cannot predate a
   split announced as news in ch10. Make it "at the head of the Iron here", or similar.
2. **Seeding by foot-against-head:** ACCEPTED (Lira's debut against the top seed; the guild champion at R4).
3. **Formats (#39):**
   - Exhibition bouts: at most five exchanges; two touches ends it.
   - Regional bracket bouts: two touches inside four exchanges; level after four, the figures decide.
   - Continental (Norhold) bouts run a points-per-exchange regime, stated in M5. Do not state a continental format
     here.
4. **The #38 strike is per axis,** as your ch11 prose has it. OWNER-DECISIONS #38 is now aligned. No change needed.
5. **Lira's tell and early warning; page thirty-one via Bracken; the titles:** ACCEPTED.
6. **Karis vs Lira at about 1,470 words:** ACCEPTED. Its brevity is part of its wit. If room is added anywhere, it
   belongs to the guild-champion bout's second and third exchanges.

## Priority 1 — Ember mechanics in the Karis–Lira semifinal (editorial: real canon defect)
At ch11 ll.171–209 the chapter states Ember fires "at a single point and only on contact". Then Karis ignites a
point on the floor where Lira will land, and later on "an empty stretch of floor", with no contact. Canon is contact
only (B4 ch54: "No heat away from the hand. Contact only.").

Restage both ignitions as contact, keeping every beat and line:
- **First exchange.** Karis reads the flick, turns early, and is already at the landing spot. The ignition is on her
  palm as it meets Lira's shoulder in the landing beat ("a contact's worth" survives).
- **Third exchange.** Lira's fake flick draws Karis's step and committed hand to a landing spot that stays empty. No
  heat blooms. Karis "finishing the turn" with her hand out is what Lira steps inside.

Keep the exchange count, the figures, "Since Greyvane", "two lines", the tell, "You've been watching my *hand*",
Karis's forecast and "Your hip."

## Priority 2 — The numbers (editorial)
1. **The mill-town day's bursts.** Six are spent (four against the yard-master, one across the academy Irons, one over
   the Bronze's sweep) on a floor priced at five free, but the Log bills four. Make the Bronze's second-exchange move
   a STEP over a low sweep, so the day totals five. That is one line at ch12:233 and its answer. Check that ch12:215,
   ch13:155 (the inventory) and the road agree. Keep the four-count inside the yard-master bout (*One… Three… Four,
   of five*) untouched.
2. **ch11:7.** "rated four times now, twice in a mock ring" becomes "three times now, once in a mock ring". **ch11:9.**
   "a day away" becomes "two days away".
3. **Clarify the burst budget once:** per day on a floor, not per bout. One clause, wherever it reads most naturally.

## Priority 3 — The ending lands once; say it once; read-aloud (both)
- **ch13: the thesis is delivered five times** (Seln, Rooke, Cael, Lira, and the final paragraph). Deliver it twice.
  Let the movement close on the travelling-coat reader's finger stopping on the exhibition leaf, or on "Not this
  season's problem". Keep protected item 21 (the first pole) exactly where the map puts it.
- **ch12 (cold).** The yard-master bout explicitly cites ch11's pillar, which turns "the floor feature he stopped
  seeing" into a formula. Cut or invert the comparison, so the crane-beam's light reads as discovered, not assigned.
- **Line fixes (editorial P3, one pass):**
  - ch13:97, the broken quotation in Seln's speech;
  - ch13:3, the "first" frost after two earlier frosts;
  - ch13:71, the Blade's "eighteen at one meet and twenty-seven at the other", which implies too much (make it
    illustrative and true);
  - ch11:177, "that morning at the wool town";
  - ch7:17, "where Cael would be… at the fourth bell" (a card cannot list a bout not yet filed);
  - ch8:47, "low in the band" for a fifteen (fix the band word);
  - ch12:197, the exhibition figure chalked on the day: use "went into the record at the proper interval".
- **Referents (cold):**
  - the garbled "four blows a sitting the cap" clause in the inventory;
  - "His place" after an Ephram paragraph in ch13;
  - two different Blades at the wool town (anchor "the same one");
  - introduce "Hesk" in a clause on first mention in this movement.
- **Lira's "five-point range":** make it checkable from the page, or soften it.

**Length.** Finish within 33,500–36,000 words.

## After the repair
Run:
- `ed.sh overlap book-05-the-silver-standard 2` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-05-the-silver-standard 2 2` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the seven chapters (hold the mean ≥ 13.3, and keep the paragraph median ≤ 30).

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the burst ledger by day;
- before/after metrics;
- the changelist, by chapter.

Edit only ch7–13 and AUTHOR-REPORT.md. Run NO git commands of any kind.
