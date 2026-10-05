# Book 4 completion pass — Lane A report (ch1–31)

**Seat:** Monroe Jackson 1.3 author (O'Connor 1.3.0), Opus. **Date:** 2026-10-05.
**Scope:** `manuscript/chapter-01.md` … `chapter-31.md` only. No chapter from 32 to 62 was touched, and no git command was run.

**Method.**
- Every chapter was read in full, in order, and revised in place, sentence by sentence.
- Each change was a single hand-written replacement, checked to occur exactly once before it was applied. There was no global find-and-replace and no pattern edit.
- The grep counts below were only used to measure the targets.
- Snapshots of the pre-pass ch1–31 are kept outside the repo, in the session scratchpad, for comparison.

## 1. Priority 1 — counts, before and after (ch1–31, `grep -oiE`)

| Target | Pattern | Before | After |
|---|---|---|---|
| Explanatory simile | `the way (a\|an) ` | 47 | 24 |
| Explanatory simile, other subjects | `the way (some\|people\|men\|you\|anybody\|everybody\|cattle\|water\|rain…) ` | 16 | 11 |
| "the way" (any use, proxy) | `\bthe way\b` | 199 | 163 |
| as if | `\bas if\b` | 97 | 52 |
| as though | `\bas though\b` | 25 | 13 |
| exactly | `\bexactly\b` | 89 | 41 |
| Measured pause | `for a( [a-z]+)? (moment\|while\|time)` | 83 | 44 |
| "a long moment" (any) | | 9 | 0 |
| without a word | | 18 | 3 |
| did not / didn't look up, without looking up | | 21 | 4 |
| nodded once | | 5 | 3 |
| He wrote it that night (frame) | `wrote (it\|this\|that) (that\|the same) night` | 1 | 0 |
| wrote it / that down | | 23 | 19 |
| That was all. / That was the whole of it. | | 6 | 5 |
| eleven / eleventh | `\beleven(th)?\b` | 123 | 57 |
| the corner of his/her mouth | | 5 | 2 |
| like water round a post | | 1 | 1 (first instance, kept) |
| as if it owed (him/you) money | | 1 | 1 (ch15, Brom, first instance, kept) |
| checking/testing whether it was attached | | 1 | 1 (ch3, first instance, kept) |

**Notes on the counts.**

- **The simile cap.** Every chapter was read against the cap of three explanatory "the way a X does Y" and "as if / as though" together, with never two on one gesture.
  - The raw grep still shows more than three in ch14, ch19 and ch22, because grep cannot tell functional uses from similes. Examples of functional uses: "I sound as though I'm hiding something", "carried … forward as if it were the rule", "as if weighing whether the word was strong enough".
  - The explanatory figures in those chapters are three or fewer.
  - Character-specific firsts were kept, such as:
    - Fiske "the way a carpenter comes into a room";
    - the porter "as a man tells a thing he has told so often";
    - Karis "the way Vell had once taught him to read a ledger" (ch12; the ch1 echo was removed);
    - the clerk "the way a careful man is upset by a form with no box";
    - Seln's mill;
    - the loose board in the hall;
    - the coat taken off.
- **Repeated images taken out:**
  - the floor that "breathes" (kept ch6; cut ch8, ch16);
  - the bowl or cup "filled to the brim" (kept ch10; cut ch13, ch15, ch25);
  - "like a hammer into a bell" (kept ch23; cut ch27);
  - "polite as shopkeepers" (kept ch16; cut ch30);
  - "plainly as gateposts" (kept ch16; cut ch19);
  - "mallet on a post" (kept ch20; cut ch26);
  - Lira's "feed she let go by" nod (kept ch15 and ch21; cut ch17 and ch22);
  - the carpenter / door-frame figure for Fiske (kept ch9, ch25 and ch28; cut ch29);
  - the "first winter … so her hand would know the floor" explanation (kept ch19; cut ch29);
  - Lira "telling him the time / the hour" (kept ch12; cut ch29).
- **Did not look up.** It now belongs to Prynn (ch1, ch2) and Bracken (ch5, ch20). The ch18 Seln-window line "The boy had not looked up that morning" is a statement of fact and stays.
  - The leaks to Karis, Wray, Quenna, the lodge clerk, the watchers, the yard instructor, the Shield man, Brom and the Ash instructor were rewritten in each character's own terms: "kept her eyes on the page", "still in her pencil", "over his letter", "to her bread".
- **Log frame.** The one "wrote it that night" frame is gone. "He wrote it down that night" and "he wrote that night" variants were varied in ch1, ch8, ch9, ch11, ch13, ch14 and ch25:
  - "It went into the Log that night…";
  - "That night the binder got it plainly.";
  - "At the desk by the window that night he put…";
  - "Under the plate that night he added the rest.";
  - "That night it went under her name…".
  
  Every entry is kept word for word.
- **"That was the whole of it."** Four remain, one in each movement: ch7 (M1), ch9 (M2), ch19 (M3) and ch28 (M4). The ch13 one was cut, because "Four short sentences" follows it directly.
- **The stake and the corner.** Lane A has no re-explanations of them; that work is lane B's.

### Elevens

**Removed (66):**
- **ch1:** "in their run of eleven" (founding compilations), cut; "named eleven titles", now "a dozen" (fetched eight, four accounted for).
- **ch2:** Prynn's "the run of eleven", now "the founding run".
- **ch5:** "worth more than eleven clauses", now "a schedule".
- **ch6:** **eleven instruments** ("There were eleven" pieces of apparatus), now "a dozen"; "At eleven he was right about seven", now "At ten … about seven, and wrong about the other three" (three examples follow).
- **ch7:** "Eleven wrong rooms.", cut.
- **ch9:** Fiske's eleven minutes ×2, now "a dozen minutes" / "twelve minutes".
- **ch10:**
  - "All eleven", "every one of the eleven", "not one of the eleven", "eleven people have each seen", "Eleven polite people", now "them" / "That many polite people";
  - the Current lecturer's "first eleven minutes", now "ten";
  - "eleven bays", now "bay after bay";
  - "the third in the eleventh", now "twelfth".
- **ch11:** the Lattice page's "eleven lines … the eleven … a twelfth guess", now a column of guesses / "another guess"; **"eleven Paths I've never been close to"**, now "half the Paths this hill teaches"; "their eleven careful silences", now "their careful silences"; "eleven Paths still out of reach", now "half the bluff's Paths".
- **ch12:**
  - the Shield crossover at the "eleventh minute", now "twelfth";
  - **"Eleven instruments"**, now "A dozen instruments";
  - "nine pieces out of the eleven", now "twelve";
  - "the margin of the eleven", now "the supervisors' list".
- **ch13:** "eleven ways at once", cut.
- **ch16:** "eleven times in his first month", now "a dozen"; "Eleven minutes" (boot-lacing), now "Twelve".
- **ch18:** Seln's "Eleven seconds … the eleven seconds", now "for the length of the yard".
- **ch19:** the Current lecturer's "first eleven minutes" and "eleventh minute", now ten / tenth (matches ch10).
- **ch20:**
  - **Nyle's "eleven wins across two seasons"**, now "a dozen wins";
  - "beat the Copper column eleven times", now "a dozen";
  - a third "it had been eleven seconds", cut;
  - Fiske "the whole eleven seconds", now "the whole of it".
- **ch21:** **"Eleven Paths fought … all eleven"**, now "A dozen Paths … all of them".
- **ch22:** "eleven occasions" inside two paces, now ten (the residence-board count goes from two to one, matching the single queue anecdote); Brom's "Eleven times", now "Ten times".
- **ch23:** **eleven swings** ×4, now no count.
  - It reads "the full run" / "*nine clean before the hum gave. In the third week, rested, it held to the end of the run*".
  - No number is given, because lane B's ch34 and ch35 measure the middle bag at eleven. Stating "ten" here would have made a contradiction.
- **ch26:** "paid for eleven feeds", now "thirteen" (the page's own tally is 4 + 6 + 3); "ran it eleven times. On the twelfth", now nine / tenth.
- **ch27:** "eleven or twelve paces" and the Log's "Eleven paces", now "a dozen".
- **ch28:**
  - "eleven paces of open boards", now "a dozen";
  - Seln "filed under it eleven times … Eleven times … Eleven people", now seven ×3;
  - the Silver-sheet head-count "Eleven.", now "Twelve.";
  - "past the eleventh bell", now "tenth".
- **ch29:** "eleven movements" in Lira's sequence, now "nine" (the movements listed number nine); "in eleven seconds there was nowhere", now "in a dozen heartbeats".
- **ch31:**
  - "Eleven rows of ticks", now "Row after row";
  - "eleven days later", now "today";
  - "the eleven rows", now "the rows";
  - Brom's "Eleven days", now "All these days";
  - "Against: eleven days of the same two coats", now "day after day";
  - "eleven days at a ferry landing", now "a column of ticks";
  - "eleven more times … eleven more numbers", now "a dozen in all".

**Kept (57):**
- carrel eleven (×16 across ch5–28, plus Brom's "Is eleven a good number?");
- eleven weeks (ch1, ch2 ×2, ch5);
- "week eleven" (ch2, the Greyvane calendar);
- eleven hundred seats (ch6, ch10, ch14);
- the eleventh day and "*Eleven days*" Log (ch6, the d11 day-count);
- the eleven rumours (ch7 ×3, ch13 "Eleven so far", ch14 "eleven stories");
- the eleven supervisors (ch10 ×4, ch11, ch19);
- eleven of twelve / eleven in twelve (ch13 ×2);
- the fame tally "five of eleven" (ch17);
- eleven seconds (ch20 title, ch20 ×2, ch21, ch25);
- "the eleventh session" (ch25 ×2, a session ordinal);
- the eleven words of the incident report (ch28, canon);
- eleven days since the pin (ch30 ×2, ch31 ×3, including the protected-run Log "Eleven days of the same two coats");
- the middle bag "eleven" (ch31, matches lane B's ch34 and ch35);
- the committee charter's "eleven clauses" (ch5, ch10).

The committee charter's "eleven clauses" are on the read's canon list (§3 item 2) but not on the brief's KEEP list. **For the coordinator:** this pair now stands beside Ilsev's protected "eleven clauses" of article forty-one; change it to another number if you want that eleven to ring alone.

**Not reachable from lane A:** "**eleven feet**" is assigned to lane A but occurs only in ch34 (lines 119 and 131), which is lane B's range. It was left untouched.

## 2. Words

| | Before | After | Δ |
|---|---|---|---|
| `wc -w` ch1–31 | 143,678 | 141,912 | −1,766 |
| formula_metrics words_total | 143,347 | 141,581 | −1,766 |

## 3. formula_metrics.py, ch1–31

| Metric | Before | After | Hold |
|---|---|---|---|
| sentence_mean | 13.45 | 13.36 | ≥ 13.3 ✓ |
| sentence_median | 9.0 | 9.0 | |
| share ≤5 words | 0.29 | 0.291 | |
| share ≥40 words | 0.04 | 0.039 | ≤ 4.5% ✓ |
| paragraphs | 3,552 | 3,549 | |
| paragraph_median | 29 | 28 | |
| scene breaks | 128 | 128 | unchanged ✓ |
| words_per_scene | 901.6 | 890.4 | 850–1,050 ✓ |
| Flesch RE / FK grade | 87.4 / 4.41 | 87.5 / 4.37 | |

## 4. Overlap, gates, sweep

- **`ed.sh overlap book-04-copper-crown N`:** M1 0 unprotected (8 protected); M2 0 (8); M3 0 (8); M4 0 (12); M5 0 (18). This is the same as before.
  - M5 (ch30–37) was also run with lane B's concurrent edits in place.
  - ch30 and ch31 were also checked by eye. Every change there is a cut, or a rewording into the chapter's own register; no source phrasing was brought in.
- **`ed.sh gates`, M1–M5:** reader_standard 0, metadata 0, modern 0 in every chapter, before and after.
- **`sweep_probe.sh book-04-copper-crown 1 4`:** M1 1% / 13%, M2 1% / 6%, M3 1% / 13%, M4 1% / 13%. This is unchanged from before.
  - Single chapters moved by ±1–2 points of "close" in both directions (ch1, 5, 8, 12–16, 18, 21, 22). That comes from the smaller sentence count, not from new matches; no movement total rose.

## 5. Priority 2 — the M3 counting study

| Chapter | Before | After | Δ | What went |
|---|---|---|---|---|
| ch15 | 4,751 | 4,634 | −117 | The first, second and third failed maps are told in a sentence each; the fourth and fifth are kept whole. |
| ch16 | 4,637 | 4,532 | −105 | Priority 1 only. |
| ch17 | 4,360 | 4,108 | −252 | The retelling to the three now stops at the overlay. |
| ch18 | 4,625 | 4,374 | −251 | The fatigue page's restatement of the ch17 plan is cut. |
| **ch15–18** | | | **−725** | |

The study-specific cut, excluding the Priority 1 trims inside those chapters, comes to about 620 words. No scene breaks were added or removed.

- **ch17 detail.**
  - The "four failed maps" re-walk is gone, along with the counter story, Karis's handling of the dead map and the narrated restatement of "evidence first".
  - The fame tally, the control column, the overlay, "Nineteen of nineteen", and the gallery and lamp in one sentence are kept.
- **ch18 detail.**
  - Cut: the tally re-explanation, the "*If it's a rate…*" chain, "a thing with no edges…", the "third column since Ardenmere" preamble and the "Touch and speech" item.
  - Kept: the four-hour curve, the toll figure, "How far", a shortened "Floors", and Vell's "guess wearing a ledger's coat".

## 6. Seams reread

- **ch9–10, the ladder book.**
  - ch9 had Lira's climb "on a ladder of better than two hundred". That contradicted its own sixty-five-line Copper column, so it now reads "up a column that already ran to sixty-five lines and would run longer before the brackets posted". The sixteen-climb sum still holds.
  - ch10 (fixes 14–16) is confirmed: no figures, every name, and "a book of names".
  - ch20's "she stood on the sixty-fifth line, the last" and "the ladder book was not the bracket" now agree with both chapters.
- **ch14, ch28, ch30, Seln's hands.** Confirmed: four hands and the cipher.
  - ch14: "Four were at his command … settled on the first, a round clerk's script", and the residence card "in the round hand".
  - ch18: product "in the fourth hand".
  - ch28: round clerk's script at the copying table, quick cramped one for notes, merchant's sloping hand for wrappers, fourth upright plain hand for product.
  - ch30: "Not one of his four hands … a fifth thing, a private shorthand grown out of the cramped hand".
  - ch31: the residence-board sheet in "the wing's round copying hand".
  - No change was needed.
- **ch30–31, Lira's hip calendar.**
  - Fix 32 was in place, but it left "By the week's end she meant to be back in hall one". The scene is d144, a Seventh-day, so the week's end is that same day, and ch31 has her promising hall one "at the sixth bell" on Third-day. It now reads "**By Third-day** she meant to be back in hall one at a third of her pace".
  - "Three days on the top line" (fix 33) is confirmed against the Fiske bout three days before.
  - ch31's wash-house "First-day evening" (d145) agrees.
- **ch23, rule two.**
  - The minute reads *a directed acquisition permitted only within earnest engagement the subject begins himself, close, in the ordinary course of his assignment; any reach to be awake and directed*. That matches lane B's ch34 after fixes 35–36.
  - ch31's narrated gloss "an engagement Seln himself began" echoed the ch34 misquote, so it now reads "an engagement **the man began himself**".
- **#35 / seasons.**
  - "by spring" ×3 (the Lattice girl and the Lattice instructor, ch11) is now "by the year's end" / "until then".
  - The porter's "the first winter" and "the winter before the lock" (ch11, Halcenvane) are now "her first year" and "the year before the lock".
  - No English weekday names appear in ch5–31. The remaining season words (Ironyard, Ardenmere, Greyvane's winter) belong to the closed books.

## 7. Protected wording

- A 56-line check of every §10 line and protected pattern that falls in ch1–31 found all of them present and exact. The check covered:
  - the enrollment record;
  - Gault's note;
  - Seln's brief;
  - the first product;
  - the plate;
  - the incident report;
  - the exception report's close;
  - every M1–M5 spoken line and Log entry in range, including Withrow's "I know exactly how rare that is" and the Log's "knowing exactly, and deciding anyway".
- No notice, bout exchange, landing beat, tally, day or date was changed.
- The only counts changed are reached-for elevens and the corrections noted above. Each was checked against later chapters with grep, and no later reference exists for any of them:
  - ch26 "thirteen feeds" (the page's own sum);
  - ch22 "ten occasions";
  - ch28 Seln's "seven times";
  - ch29 "nine movements";
  - Fiske's "a dozen minutes".
- Gwen and Abbot were left as they are.

## 8. Changelist by chapter

| Ch | Changes |
|---|---|
| 1 | Cut the rain simile in ¶1 and the Vell-ledger echo (kept in ch12); Karis "kept her eyes on the page"; Wray's "without a word" and Hobb's long pause cut; Log frame varied; founding run and titles de-elevened (dozen / eight); one "exactly". |
| 2 | Five similes cut or recast in register ("It cost Karis something to say it", "the look she kept for very stupid remarks", "into the quiet"); "for a magistrate"; pause cut; Prynn's "founding run". |
| 3 | Five "exactly" cut; Wray's and Quenna's look-ups recast; Edran's pause and "without another word" cut. |
| 4 | Knots-on-wraps echo of ch3 cut; Brom's bags simile and the Vell column cut; "agreed, without ever saying so"; two pauses cut. |
| 5 | Two similes cut; the lodge clerk and watchers no longer "look up"; two pauses cut; "a schedule and a chancellor". |
| 6 | A dozen instruments; Brom's swollen-joint simile cut; pause and Karis's look trimmed. |
| 7 | "Eleven wrong rooms." cut; Rooke "exactly" and the Log's "exactly" cut; Karis's look-up and the long-while pause cut. |
| 8 | Floor-breath repeat cut; three similes cut; "without a word" cut; Log frame "That night the binder got it plainly." |
| 9 | **Ladder-book seam**; one "exactly"; the instructor's look-up; Log frame varied; Fiske "a dozen minutes". |
| 10 | Four similes cut ("all at once" for the boiling water); supervisor elevens thinned; Current lecturer ten minutes; "bay after bay"; pause cut. |
| 11 | Stone-in-boot simile and two others cut; Lattice elevens and **eleven Paths** removed; **season words fixed**; corner-of-mouth recast; pause cuts; Log frame varied. |
| 12 | Four similes cut; Karis's look-ups recast; **a dozen instruments** / twelve pieces; Shield twelfth minute; "unremarked"; two "exactly"; pause. |
| 13 | Three similes cut (load, spill, arm); the clerk "kept his eyes on the pendulum"; three "exactly"; redundant "That was the whole of it" cut; Log frame "Under the plate that night he added the rest." |
| 14 | Three "without a word" cut; Seln's arm simile cut (the ch13 echo); one "exactly"; Brom's "as if it might go off" cut; Log frame varied. |
| 15 | **Maps one to three told in a sentence each**; four similes cut; one "exactly"; pause; "to the page" / "still bent over them". |
| 16 | Eight explanatory similes cut down to three (lit window, keeping it waiting at a door, rain); "kept his eyes on the floor"; "over his letter"; a dozen times; twelve minutes. |
| 17 | **Retelling stops at the overlay**; four similes cut; two "exactly"; Lira's door "without a word"; long-moment pauses cut; Lira's nod recast. |
| 18 | **Fatigue-page restatement cut**; hum, draught and "as a man might stand" similes cut; Gault's nod and "without a word" cut; Seln's eleven seconds removed. |
| 19 | Limp, gateposts and lecturer similes cut; two "exactly"; "to her bread"; "without a word" cut; Current lecturer ten minutes / tenth. |
| 20 | Dog, page, quartermaster tail, knee, hip, doorpost, arm and lesson similes cut; **Nyle's wins de-elevened**; two "without a word" cut; Merrick "just as". |
| 21 | **Eleven Paths** gone; three "exactly"; Karis's look-up recast; two pauses cut. |
| 22 | Feed-nod, numbers and yard similes cut; ten occasions; corner-of-mouth recast; two "exactly"; "still making her mark". |
| 23 | **Eleven swings** de-numbered (consistent with lane B's middle bag); Karis's nod and one "exactly" cut. |
| 24 | Five similes cut (fault, never-left, inventory, cattle, change); "without a word" cut; one "exactly". |
| 25 | Post, spill and smith similes cut; four "exactly"; two "without a word"; Log frame varied; Brom's speech seam smoothed ("Brom added"). |
| 26 | Mallet and wall, leaf, lock, dropped, writing and funnier similes cut; thirteen feeds; nine runs; three "exactly"; Brom "kept his eyes on his bread"; two pauses. |
| 27 | Tap, bell, counting and distance similes cut; a dozen paces; one "exactly"; two pauses; Rooke's "without another word" cut. |
| 28 | Heft, sound and coin similes cut; a dozen paces; Seln's seven filings; twelve Silver; tenth bell; three "exactly"; two pauses; Jask's doubled open mouth merged. |
| 29 | Floor-ritual repeat and carpenter echo cut; nine movements; a dozen heartbeats; two "exactly"; Lira's "telling the time" echo cut. |
| 30 | **Hip calendar ("By Third-day")**; cards, shopkeepers, boots and embarrassed similes cut; Ash's look-up recast; one "exactly"; pause. |
| 31 | **Rule-two gloss aligned to the minute**; elevens thinned (the Log entry untouched); ceiling, pencil, weather and "owes you money" similes cut (the last a repeat of ch15); corner-of-mouth recast; Karis's look-up; one "exactly"; pause. |

## 9. For lane B and the coordinator

1. "Eleven feet" lives only in ch34, so lane B must make that cut if it is to be made.
2. The middle bag's "eleven" (ch34 and ch35) is safe, because ch23 no longer states a ceiling.
3. First instances kept in lane A, so that lane B can cut its later repeats freely:
   - "as if it owed you money" (ch15, Brom);
   - "whether it was attached" (ch3, Lira);
   - "like water round a post" (ch15);
   - "a hammer into a bell" (ch23);
   - "polite as shopkeepers" (ch16);
   - "the only lit window in a dark street" (ch16; Seln echoes it deliberately in ch18).
4. The committee charter's "eleven clauses" (ch5, ch10) was kept, per the read's canon list. Rule on it if Ilsev's protected "eleven clauses" should stand alone.
5. The metric margin is thin: the sentence mean is 13.36 against a floor of 13.3. The Step 4 listening proof should prefer joins over splits in ch1–31.
