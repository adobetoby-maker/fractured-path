# AUTHOR REPORT — Book 8, Movement 3 "The Border Road" (chapters 13–19)

> **Repair r1 applied (2026-10-11).** The six markers are filled (by the coordinator), the loads at the fork and the closing file are changed, and chapters 17–19 are recomposed in part; see `REPAIR-REPORT-r1.md`, which governs wherever the sections above "New canon minted" differ (their tables, line references, marker list and the owner flags describe the first draft). "New canon minted" and "State at movement end" below are refreshed.

Author: `claude-opus-5-5` (Claude Opus 5.5), O'Connor 1.3.0 seat, 2026-10-11. NO-SOURCE method: no file under `books/` or `v3-runs/` was opened, read or searched (see `AUTHORSHIP.md`). Drafted from `EVENT-LIST.md`, which was written first; changes made while drafting are listed at its foot.

**Status: all seven chapters exist in full. Six `[[TIER-B]]` markers stand. Deployment moved from thirty to thirty-two. Purse 138. Several stagings and minted facts are listed for a ruling.**

## Words and metrics per chapter

`formula_metrics.py`, after the last edit.

| | Title | words | mean | ≤5 | ≥40 | para median | breaks | words/scene | FK |
|---|---|---|---|---|---|---|---|---|---|
| ch13 | Ours | 5,233 | 13.88 | 22.5% | 2.4% | 27 | 4 | 1,047 | 3.61 |
| ch14 | Carters Declare | 4,599 | 13.57 | 25.1% | 3.2% | 26 | 4 | 920 | 3.20 |
| ch15 | The Loudest Thing | 4,672 | 14.11 | 17.8% | 2.1% | 29.5 | 4 | 934 | 3.29 |
| ch16 | A Month | 4,610 | 13.48 | 25.4% | 3.8% | 21 | 4 | 922 | 3.46 |
| ch17 | Three Readers | 4,677 | 14.00 | 24.0% | 3.3% | 30.5 | 4 | 935 | 3.80 |
| ch18 | A Year and a Day | 5,056 | 13.97 | 19.1% | 1.9% | 29 | 4 | 1,011 | 3.87 |
| ch19 | Different Verbs | 5,095 | 13.70 | 23.4% | 3.0% | 25 | 4 | 1,019 | 3.33 |
| **movement** | | **33,942** | **13.82** | **22.5%** | **2.8%** | **26** | **28** | **970** | **3.51** |

Sentences 2,457; sentence median 11; paragraph mean 39.0; Flesch Reading Ease 94.5. Every chapter is inside the three per-chapter working ranges (mean 13.3–14.2; ≥40 at most 4.5%; 850–1,050 words a scene). Drift to report: the ≥40 share is under the 2.5% floor of the edition's working range in chapters 13, 15 and 18; FK grade is under 3.5 in chapters 14, 15, 16 and 19. The marker lines are counted by the tool as prose (about 150 words in all).

**POV:** Cael ≈31,810 (93.7%); Seln 2,131 (6.3%), two scenes at the head of chapter 18, against a plan of about 1,800.

**Days:** ch13 the 278th · ch14 and ch15 the 279th · ch16 the 279th evening and the 280th morning · ch17 and ch18 the 280th at the spring · ch19 the 280th evening and the 281st to noon.

**Growth beats (my count, a heuristic): 15.** Rules on a job and says why he will not vow a town (13) · has to tell the man who questioned him for three days how to walk on a road (13) · takes a man's stated breaking-point as a thing worth more than a promise, and stations him by it (13) · takes the loud part as his to pay (14) · reads three wrecks as far as the wheels and no further (14; owned in 16) · sees that a wall is useless when the only reason to cross it stands at its end (15) · bursts away from his friends for the first time and trusts his skin to another man's knee (15) · waits for an eleventh thing and has ten (15) · enters his own bad plan and will not enter Vastin's wall as a fault (16) · sees a man look almost free (16) · thinks that paper will be different, and is one short (17) · does the sum and refuses the verb (18) · does not write it, for the first time in his life (18) · writes *inside* in the log and hears it (19) · turns from the light, and lays his hand on the page (19).

**Supporting beats:** Vastin 5 (says where he will break before the job; is passed over by a hound and "let off something"; stands the wall; "I know fields"; looks, and notices a wind) · Seln 3 (the choice to place and not to say; minds not watching; teaches for the first time) · Oryn 3 (takes Pike's line; asks, and binds for a month; the column for the patient's tier and the station term) · Karis 3 ("Ours"; stops the lamps sentence; afraid of being right) · Brom 2 (refuses the wrong rope; "It's a boot") · Lira 2 (votes with the left; the slow hand holds and the quick one strikes) · Pike 1 (a column for a healer) · Teague 1 (says what he would do with a man at his back).

## Checks

- **Gates** (`ed.sh gates book-08-before-the-paths 3`): all seven chapters `reader_standard=0 metadata=0 modern=0`.
- **Overlap** (`ed.sh overlap book-08-before-the-paths 3`): **3 unprotected runs**, 11 protected. All three are the plan's own text and were left: `clearance the cut below the shoulder hold on the border road two days west` (13:27; the packet's slip, 14 words); `clear because it's empty not because it's safe` (16:93; inside a marker); `the one thing i'm walking up that road owing` (19:177; inside a marker). Eight other runs on the first pass were ordinary phrases and were re-composed.
- **Sweep probe** (run once, no `SHOW`; the script takes movement numbers, so `sweep_probe.sh book-08-before-the-paths 3 3`): skeleton 0 / 1 / 2 / 3 / 1 / 4 / 5% and close 12 / 14 / 16 / 14 / 11 / 19 / 18% by chapter; **total skeleton 2%, close 15%** over 1,576 sentences. Movement 2 was 2% / 12%. I have not seen what it matched; chapters 18 and 19 carry most of the protected dialogue.

## Deployment

**Thirty-two at the movement's end** (thirty at entry).

| # | Day | Fragment | Where | Price or limit shown |
|---|---|---|---|---|
| — | 278 | the read asks at the first bend; Shadow at dusk | 13:169; 13:259 | refused; held |
| — | 279 | all ten wake at a hound in the mist | 14:25 | refused, one by one |
| — | 279 | the read and Anchor ask in the cut | 14:221 | refused |
| **31** | 279 | **Ember**, one grain, on tow, at the mark | 14:233–235 | the heat comes home to the left palm though he held nothing |
| — | 279 | Wind leans as he walks back | 14:239 | refused; his own legs |
| — | 279 | Blade, Pressure, Anchor, Storm, each with its reason | 15:101 | refused: the sound was already there |
| **32** | 279 | **Wind**, one burst, away, ten strides, to the north bank inside the plane | 15:143–163 | the lock, one count, spent behind another man's wall |
| — | 279 | no eleventh | 15:223–227 | "He had ten" |
| — | 279–280 | Shadow at dusk; Tide lies still while Oryn works | 16:127; 16:47 | held; not used |

**Log lines:** 13:269 *Deployment since the Line: thirty.* · 16:205 *The point: Ember, one grain, at the mark. In earnest. The left palm, though I held nothing.* · 16:207 *Wind: one burst, away, ten strides, to the north bank inside the wall. The lock was spent behind another man's wall. It cost me nothing but the count, and I was more afraid in that count than I have been since a hall.* · 16:209 *Nothing came of standing by it. Ten.* · 16:211 *Deployment since the Line: thirty-two.*

Shadow not opened. Anchor's counted uses still two. Tide used on nobody; no self-reading; the still place not read, touched or named (Oryn refers to "a thing that I made you write down and leave alone", 19:87). The Iron read was not opened in earnest. Cael has not touched the cord or either edge.

## Protected units placed and markers left

**Placed whole, once** (checked by exact string): the slip (13:27) · "Ours," Karis (13:41) and Brom (13:45) · "Carters declare, on the ice." the factor (14:91) · "A month." Oryn (16:55) · the lesson, Vastin's four sentences (16:159, 16:163, 16:169) · the S4 log (16:197) · "Behaves as device. Cannot be." (17:85) · "This has to go up." Vastin (18:161) · "You keep drafting orders." / "Habit." / "Out here the habit's the tell." / "Draft nothing. Just look." Seln, Vastin, Seln, Seln (18:171–179) · the close, Karis's four sentences (18:213, 217, 221, 225) · "I'm not an archive person," Oryn (19:19) · "Leaving and routing are different verbs. I'm doing the second." Oryn (19:63) · "Three weeks," Seln (19:71) · the station term, Oryn (19:91) · the fork's log entry (19:105) · "Bring me whatever walks out of that archive with you. All of it." Oryn (19:185).

**Markers left (chapter:line):**

1. **16:93** — "clear because it's empty, not because it's safe". Partial, no speaker. It stands after Brom's "So it's clear," on the north bank above the sink; the next line is neutral ("Nobody added to it, and the factor came down off the bank"), and the factor then says "Empty's what I posted. I never asked anybody for safe."
2. **16:165** — "You do now," No speaker. It stands alone between Vastin's "forty years" sentence and "Vastin received it… He bowed his head by a little, toward the voice". Cael, Brom, Lira, Karis, Seln and Oryn are all in the long house.
3. **17:185** — "Two copies of one ignorance." No speaker. It stands after Karis lays the dead man's ledger above the four sheets, a pencilled stroke and bar over four in ink. Karis, Seln, Vastin, Lira, Brom and Cael are at the slab.
4. **18:219** — "Treswick," / "The archive under it. Cleon." / "Who's Cleon?" No speakers. One marker for the three lines, between Karis's "Everything I can't read points at the same place." and her "The only historical-Path practitioner…". All seven are within hearing (Oryn at the basin).
5. **19:177** — Oryn's "… the one thing I'm walking up that road owing". Partial. It stands after her "You, I've not read… And I'll not do it tired, at a fork, with a round in front of me." and before Cael's "Then it'll keep."
6. **19:215** — "Not the steps," … "Not the square." No speaker or speakers. Oryn stands before Cael at her own distance with the mule's strap in her hand; the next line is "She turned the mule's head to the north."

**Not reprinted:** the technician's two lines (ch12 has them once; 18:115 has only "*Deep layer*… and then two words; and then that day"). Karis's ruler rule is invoked at 17:99 and not quoted.

## New canon minted

*(Refreshed after repair r1. Line numbers are those of the repaired chapters.)*

- **The slip and Pike's rule.** The clearance slip came over in the bag on the 277th; Pike drew a road between two heaps beside it. Twenty, "at the hold's own gate, on the factor's thumb, when the factor's walked it". **Pike will not write a clearance taken until a healer is said** (his own rule since his second year, when one of a crew of four bled for two days on a hurdle). His sixth line: *And a healer; of her own road; at her own price.*, the first column he has had for Oryn.
- **Oryn's round this thaw.** West with the six as the slip's healer; from the fork-stone north to "five gates up along the hill-foot", one with a child that she was to have heard a cold term ago; then "down the far water to the ford, and over, and on to the mill from above". Three weeks puts her at Millrace.
- **Teague.** The forty sacks went aboard on backs on the morning of the 278th; he is still on the east landing when the six cross, bound for the block on the cold road. He had first call on the slip by the cloth and left it. "A man that holds a thing so doesn't leave off because nobody's asked him. I'd know what I had at my back." The word left with Pike: the cut, two days west by the border road, and whatever is beyond it; no day.
- **The ferry and the rope.** On the 278th she crossed in the forenoon with people, led beasts and carried sacks; no wheels. A copper a head, the mule a head. **The broker's cordage on the western landing is three-strand, hawser-laid. Brom refused it.** The sixty yards of four-strand are still owed.
- **The border road.** One of two roads out of the western landing. Alders, then moor; a halting-ground in a fold by a beck, eleven miles out, with a dozen dead rings; a long shoulder of hill; the cut; four miles of high moor to a spring; six more to the fork-stone; a long rise of a mile and more.
- **The four hands.** Flat, palm down: *stand*. A shut fist: *seen*. Two fingers: *come on*. A hand turned over empty: *nothing*. The doctrine in one line: "Nobody declares unless they're meant to be loud. One of us, once, in a place that we've chosen beforehand."
- **Stillhounds, added to Book 7's account.** One paced the column for half a mile in the hour before sunrise and stopped at a beck. **Karis's sixth line (16:119):** *It goes to where a declaration ends, if it has learned that the declaring moves.* Eight laired round the sink, three of them under the north bank where the lip hides four yards.
- **The shoulder hold and its factor.** A foot-track from a cairn below the spur; a plain bar in a wall as thick as a cart; a small clean yard, a long low house, a salting-shed with empty hooks. The factor: spare, grey, a leather apron, a slate on a cord, a sheep-crook, pale eyes; a thumb-mark like a crook; **no name and no pronoun on the page**. Three carts, a carter and two mules lost since the frost.
- **The cut.** A hundred strides, a cart and a man wide, rising east to west by the height of two men. South bank: thirty feet of scree, with the hold's sheep-walk on its lip. North bank: low; beyond it fifty-five yards of scree down to the sink, a round bowl in shadow where water goes into the hill, iced grey and rotten. A seep at the cut's head runs down the middle of the road under ice that never thaws in that shade. Three runs worn over the north bank in the upper half. Three wrecked carts at the foot.
- **Iron Wall as shown.** Named by Vastin (16:109); **no tier is stated**. He steps into the road and brings the stick's foot down once; a line runs from his boots across the cut and cracks the ice white; "the air stood up from it": a face from bank to bank as tall as the scree, seen only by the frost that lies on it. It holds eight hounds at a run. It does not go anywhere; **he may not lift a foot**; each blow on it comes down through him into the stiff leg; it goes out of him steadily; it shuts the road and not the banks. "A Path of the tribunal floor… taught for fields; and a field is ground where a thing has been declared, a hearing, or a square, or a gate with a crowd at it." "I have stood on eleven such."
- **The fight's count.** Brom's rock at the plane's south end; Lira, two-handed, on the hound at Vastin's knee; one broken on the plane in the second run; Seln's knife on one standing in the runnel; Brom's rock on the other. Three over the north bank and through the sink's ice. Seln was on the north bank above the sink when he said that the cut was clear because it was empty.
- **Bodies.** Vastin: four holes and a tear below the right knee, shut by Oryn; the joint bound with linen and two laths; **the bad knee is the right**. Brom: the right boot torn; two toes bruised, bound together, ten days.
- **Oryn's past (kept by the coordinator as written; the order of telling changed in r1).** "I'd my rank off a board at the foot of a bed." A house for the sick "inside a wall", forty beds, six healers; her Iron fourth rank is provisional because she "never stayed to have it confirmed". **A sheet on a board at each bed's foot: name, complaint, what had been spent, and a column for the patient's tier.** In a week of fever the spending went down the column from the top; a woman from the river sheds with no tier went to the bottom of the heap; Oryn went to her at night, off the sheet, and it was enough (**nobody died**); the woman who kept the house said that a healer who spends off the sheet has stolen from whoever stood next on it. Asked where, she will not say: "They keep the same sheet at the foot of every bed inside the Line." She walked out of a gate in the coat she stood in and has not been through one since.
- **The spring.** A furlong south of the road, four miles past the cut: an outcrop as big as a barn, a stone-built basin, and a fallen slab twelve feet by six, waist-high, out of the wind.
- **The abstracts, read in daylight.** Karis counted every row twice and had each counted again; **no figure for any row is printed**. **She gives no number of places.** She sorted the sheets by their sign-groups, matched **four** to the hide by their measures (three alike to the stride, one double), and will not call the unmatched groups places until a sign can be read (17:27–39). **Five columns:** the day, in the registry's reckoning; the station (eight points); the measure; *Instruments*; and the anomaly. No radius of the four has changed by a stride in six years; four surveyors by their figures; three clerks' hands. The fourth column reads *Cord true. Edge true. Level true.* on every sheet. The three oldest rows have a ruled space at the foot headed *Remarks*, empty but once: **the Stair's sheet in the fourth row carries the protected four words, in a hand that is none of the three clerks'; Karis laid the dead man's ledger beside it and will not swear to the hand either way.** From the next year's printing the space is gone. Brom counts the three findings on his fingers (17:61, 17:77, 17:139).
- **Seln's five omissions:** no routing head; no surveyor's name, a number in its place; nothing to say who ordered the survey; no column for a cause; the remarks space struck from the block after the year of the remark.
- **Vastin on the form.** "A survey abstract of the second schedule… the sheet that stands in place of the field book when the book has been called in. The book itself does not survive it." Drawn at the year's end in the office that has the charge of the stations. "A clerk enters what the form has a column for. What it has no column for goes with the book." His two false starts: an order to re-tape each row under two hands, and "restricted matter… under the first article of the closed schedule". **No second calendar: the stations' year and the difference are gone.**
- **The box.** To the right of the four signs and the number, on every abstract, a small printed square with a heading in the unread signs. **On all four of the hide's places it holds the short stroke and the bar, drawn alike**, the double-sized place included. "It is a class." Nobody says who filled it or by what rule. Nothing is said of any other sheet's square.
- **The date.** The registry writes, on the first line of a person's file, after the name and before the bracketed word, the day on which the person was classed; every paper served on Cael began with it. Seln copied that line twice when he was employed at the house above Ostrand. The technician's sheet carries a registry year and a day in it, and it is that day. Seln knew it by the lamp, doubted a date read once over a shoulder in another person's pencil, and read the original a figure at a time in daylight. Cael laid the one date against the other, twice. **No figure, no span, no arithmetic owed to anybody; nothing spoken; nothing written.**
- **The fork-stone and the fold.** A slab as tall as Brom, a worn hand cut on each face. A round drovers' pen of dry stone a little down the northern branch, a quarter of it roofed, with a hearth and flue in the wall and a stack of peat: "You burn what you want, and you cut as much again before you go."
- **The loads from the fork (r1).** Boxes on Brom (left shoulder), Lira (both arms through the beckets) and Cael. Seln carries none: he goes ahead with his hands empty. **The tarred case was left leaning on the fork-stone; Karis stopped forty strides up; Vastin went back for it unasked, after Oryn was out of sight, hooked its strap with his stick without kneeling, and slung it above his sound leg.** He told Cael so at once: "I waited until she could not be put to the trouble of forbidding it a third time." "It is a cord, a mallet and one stake."
- **Seln on the provision:** "A provision of that kind is granted by the week."
- **Treswick from the rise.** A green plain with hedged fields; a river out of the north in loops; a bluff in the nearest loop; three walls in steps; a small pale steady light above the highest roofs. A day's walk off.
- **Roles (all unnamed):** the shoulder hold's factor and "the hold's woman"; the broker and his clerk on the western landing; the keeper of the house for the sick, the Gold with the wrist and the woman from the river sheds in Oryn's account.

## State at movement end (for the ledger)

*(Refreshed after repair r1.)*

**Calendar.** A little before noon on the **two hundred and eighty-first day past the Line**, going down the western side of the long rise, a day's walk from Treswick. Days on the page: 278, 279, 280, 281. No season, month or weekday name; no figures for the technician's date; no count of years since the Kindling.

**Where everyone is.** Six going down off the rise: Seln in front, Lira, Brom, Karis, and then **Cael with Vastin walking beside him on the ditch side** (from the top of the rise; nobody asked him to and nobody told him no). Oryn and the brown mule went north from the fork at first light and did not look back. Teague's five are east of the river.

**Cael.** Nineteen. **Ten fragments; no eleventh.** **Deployment thirty-two.** Left palm stung by Ember. He ruled on a job and has made no vow. **He has read the technician's date, laid it against the first line of his own file, and knows it for the day of his own Kindling. He has not written it, has told nobody, and has put no verb to it.** He said "You do now" to Vastin at the hold. He has written in the log, at Oryn's asking, that inside Treswick he does not go near the station. **He has laid his hand on the page once, on the rise, and Karis has it again.** He has seen the light on the crown and turned from it. He carries a box. He asked "Who's Cleon?" and has the name.

**Lira.** Wind; Iron, Rank One. No burst. **Arm: the sixteenth day out of the wool on the 281st.** It held a hound by the scruff while the right hand struck; it votes; **she carries a box on her back with both arms through its beckets.** Oryn: slow for as long again; don't fall on it. **She no longer has the crossbow.** She knows that Cael has put something away and has not asked.

**Brom.** Iron Skin; Copper. No grey at any point. Right shoulder still in the older healer's knot (if it tells him anything he is to put the load down and leave it down). **Right foot: two toes bruised, bound; ten days from the 279th, eight left on the 281st.** One box on the left shoulder. He has the purse and Pike's thumbed slip. He lays seven bowls and will carry Oryn's empty.

**Karis.** Ember; Iron, Rank Three; one point set in the peats. She holds the flat (six rows, counted twice by two people and re-taped, the technician's sheet at the foot of the second), the completion report, the page in its oilcloth inside her coat, her copy, the hide, the kit's ledger and her notebook. She knows: four sign-groups matched to the hide and others matched to nothing, **no number given and none of the others called a place**; five columns; no measure changed in six years; the instruments true; the remark, and that she will not swear to its hand; the box, the same on all four; what an abstract is. She cannot read the index or the box. She began a sentence about lamps and stopped it with her rule, verbatim. She heard "I've read it" from Cael as she had from Seln and asked neither. She named the archive and Cleon. Six findings on her stillhound leaf.

**Seln.** Shadow; Bronze. One hound with a short knife; "It's clear because it's empty, not because it's safe". **He has read the original date in daylight, has told nobody, and has set the sheet before Cael without a word; he does not know for certain that it was read.** He has taught for the first time ("Draft nothing. Just look.", to Vastin). **He carries no box.** **The case is on him, shut; no ruling upon it.**

**Oryn.** Tide; Iron, Rank Four, provisional. On Pike's slip as its healer. She asked Vastin and had an explicit yes; shut four holes; bound the joint; two fingers on his wrist. She has priced all six and given Vastin as long as any. **She has not read Cael**: "It's the one thing I'm walking up that road owing, and I'll pay it." She has told the house, the column and why she left, and will not say where. She has her term in his log and has read it there. Gone north with the mule, her linen, and her crossbow with its one bolt; five gates, the ford, then Millrace in three weeks. She does not know that Vastin is carrying the kit's case.

**Vastin.** No office; **no age stated**. **Iron Wall declared once, on the 279th, in the cut**; spent to the floor. **Right knee: bitten, shut, bound stiff; the 281st is the second day of thirty**; on the stick; no kneeling, running or walls. He qualified every instruction. **He has not sat in front of the crew since the cut.** **He carries the tarred kit case (cord, mallet, stake thirty-two) on the shoulder above his sound leg, taken up unasked at the fork-stone after Oryn had gone, and has told Cael so.** **He walks beside Cael from the top of the rise.** He said the town's name at the spring, the first to say it since the page. He knows the four hands, the doctrine and where a post stands. He has heard the daylight reading whole. **He does not know that the date means anything to anybody**, the mechanism, what Cael carries, the instruments' behaviour in Cael's hand, or what is under the bar; nothing has been said of a directive or an objection. He has not asked to join and nobody has spoken of it.

**Teague and his crew.** On the east bank; salt going over; then the cold road. He knows the six went west to the cut "and what's beyond it", and that Vastin walks behind them. His term is "where I left it".

**Pike's book.** Eleven completed lines. The clearance is taken (five strokes and a healer's line) and not yet said closed; **the thumbed slip is in Brom's shirt**. The season line's number still blank. Eleventh on the cloth.

**Objects and money.** **A hundred and thirty-eight marks.** The reserve sealed. **Owed: sixty yards of four-strand rope to the ferryman.** Three boxes on Brom, Lira and Cael. The kit's case with Vastin. Stake thirty-two never driven. The cord and both edges untouched by Cael since the 168th. Hesk's book has the term on the 280th's leaf and no line for the date.

**The Quieting, as known.** On paper: the four places of the hide, measured for six years with no change; instruments true inside; one word in the fifth column; one surveyor's remark, and the space for remarks removed afterward; a class mark that is the same on all four. Other sign-groups in the rows, unmatched and uncounted on the page. In the field: unchanged.

**Who knows what.** The mechanism: six, as before. The daylight reading: the six at the slab, and Oryn by hearing. **The date: Cael and Seln, each alone.** Nobody has interpreted the sequence, said who classed the places or why, or joined the remark to anything or anybody.

**Words said aloud for the first time.** *Iron Wall* (Vastin, 16:109). The town's name, for the first time since the page (Vastin, 18:215). *Cleon* (Karis, 18:219).

**Open threads.** A date that two people know and neither has said. "All of it." Sign-groups that are not yet places. A box that nobody can read. A lamps sentence stopped. A knee on its second day, and a case on the shoulder above the other. A reading that a healer owes. Two sentences in a log about a flight of steps and a paved place. A rope of the wrong lay. A question that Cael kept from Vastin at Lowmarch, still kept.

## Owner flags

1. **Six markers** (above). The largest is the close (18:219), where three of the plan's lines have no speakers; the smallest are single tags.
2. **"The wall held the line," … given to Vastin** (16:159) on the strength of the "forty years" sentence that the map joins to it; and "I know fields…" given to Vastin on the strength of the log's "He knows fields". If either is somebody else's, the join will want a line fix.
3. **Staging of the cut.** BOOK_MAP §8 puts Cael "twenty strides west, past the sink" and the protected log has the wall go up "two feet from me". I made the first his mark (he sets the point there and walks back) and the second the moment of the wall. The den's lesson (it runs to where a declaration ends) is mine; so is the reason for the wall (eight hounds running at the foot, where Karis, Oryn and the mule stand). The wall is therefore neither needless nor right, and the log does not enter it as a fault.
4. **"The fourth's twice the size."** I read it as the place (twice the others' size, with the same mark, "drawn no larger and no differently"), not as a mark drawn twice as large. If the plan meant the mark, 17:173 wants one sentence changed.
5. **"Five."** Repaired ch11 has Karis lay down four fingers and a thumb and promise a number in daylight; she gives it at 17:27. With it come two things the packet does not list: a fifth place "larger again than the fourth" with no known position, and a box on its sheets that is "not filled as ours are" (not described). Both support the protected "They graded it — the sites are ranked by something". If either is too early for the 298th, the cut is local (17:27–41 and 17:177).
6. **The sum as a turn between two counts.** To make "the sum" a sum without a figure or a span, the stations' office keeps a year that opens later than the seat's, and Vastin gives the difference as procedure. Repaired ch12 already has Karis write the figures down "and did not turn them into anything". This mints a small piece of registry practice.
7. **The remark is in the dead surveyor's hand** (as far as Karis will say), on the Stair's sheet in the fourth row.
8. **Oryn's past** (the house, the column, the woman who lived) is minted from the packet's three phrases. No patient dies.
9. **The crossbow is back with Oryn** and went north on the mule.
10. **The rope was refused** as three-strand; the cash spine (118 → 138) left no room to buy it.
11. **The factor has no pronoun.** Movement 7 gives the factor a line; nothing here fixes man or woman.
12. **Vastin's knee is the right.** His tier is not stated. He says that he has stood on "eleven" fields.
13. **Cael lays his hand on the page** on the rise (19:281); custody stays with Karis.
14. **The cutaway is long** (2,131 against about 1,800).
15. **Chapter 10's frame shop.** When I first re-read the repaired chapter 10 it still had "down a stair and through a frame shop" in Cael's thought about the two roads to the town; after the coordinator's closing note I searched chapter 10 again and the phrase is gone. Nothing of mine refers to a frame shop or a mender.
16. **The probe's arguments.** The launch prompt's `13 19` are chapter numbers; the script takes movement numbers. Run as `3 3`.
