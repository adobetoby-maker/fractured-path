# Recheck r1 — Book 5, Movement 8 "The Challenge" (chapters 47–53)

**Seat:** Claude Fable (claude-fable-5-1), standing in for Sol (Codex quota exhausted). Fresh context. Read: the full current movement (ch47–53), every chapter's `diff -U0` against `pre-repair/`, REPAIR-BRIEF.md with the coordinator rulings, review-editorial.md (§4, §6, repair brief), review-cold.md, AUTHOR-REPORT.md "## Repair r1", BOOK_MAP §§3D, 7.1, 10, the M8 packet's coordinator notes, STATE_LEDGER's "After Movement 8" block, ch46's ending, and targeted greps of ch01–46 and the source chapters 16–19. No manuscript file was edited. No git command was run. Date: 2026-10-05.

---

## VERDICT: CLOSE WITH LINE FIXES

**Scope:** six required line fixes (three of them seams the repair itself opened: a stray quotation mark in ch47, an off-by-one time-word on Lira's stair line in ch52, and a dropped tag in ch53 that hands Lira's line to Karis; one tabled tracker the author kept verbatim in ch53; one restored tag in ch52; one count in ch51), and five optional fixes that break the last source-order runs I could find by reading. Nothing needs a second repair. Every brief item is RESOLVED or acceptably PARTIAL; every protected line greps exactly once; gates, overlap, skeleton and formula reproduce the author's figures to the digit; the ceiling exchange and Vastin's section are sound.

---

## (1) Brief items, with evidence from `diff -U0` vs `pre-repair/`

### Coordinator rulings (thirteen)

| # | Ruling | Status | Evidence on the page |
|---|---|---|---|
| 1 | Keeper is "he" | RESOLVED | ch52: "The keeper had given up counting. He did more than give up." ch53: "the keeper went to bed past every door, as he did every night" |
| 2 | No weekday names | RESOLVED | ch49 s1 is "the design session"; grep of the seven chapters for weekday/season/month words is empty |
| 3 | Cutaways ~27% | ACCEPTED (no change asked) | ch49 6,722 w; Vastin ≈1,000 w in ch50; Seln ≈600 w in ch53 |
| 4 | Match line *filed; acceptance pending* (T19) / *Accepted.* (T20) | RESOLVED | ch48: "*filed; acceptance pending*"; ch50: "*Filed; acceptance pending* had been painted out. … *Accepted.*" |
| 5 | Third place: four exchanges, 3–1, M7 format | RESOLVED | ch51: E1 Rhagen "by a handful of quarter-minutes"; E2 Halcenvane "by more"; "gave the fourth exchange to Halcenvane, as they had given the third. Three exchanges to one." No unit figure posted |
| 6 | "to be confirmed at the closing"; trial final on finals day | RESOLVED | ch51: "Third of fourteen, as the count stands at the close of the trials. To be confirmed at the closing." ch48: "the three bracket finals and the trial's final waited for finals day" |
| 7 | Crown: half-inch dome to a grounding trench; fix "where it shows" | RESOLVED | ch52: "Half an inch … From the oak to the barrier's foot, all round … The long way is north to south, straight over the top, so that's the longest road downhill in here." |
| 8 | Auremont's risk office writes the ring spec | RESOLVED | ch50 (Umber): "supplied to this office by Auremont's own risk office, at the house's expense, this morning"; ch49: the risk officer writes "an order to the facilities office, for masts" on the stair |
| 9 | Vastin leaves two mornings after the notice; resolves to stay | RESOLVED | ch50: notice "the evening of the day after the filing" (T20); "Departure, the morning after next" (T22); "This time he would stay." |
| 10 | Seln's slip at the fifth bell T23, ash broken, nobody named | RESOLVED | ch53 opens "At the fifth bell of the day before finals"; "Somebody had already broken the ash"; "He did not let himself think about whose hand." |
| 11 | Daeva's Storm Path from her side; exhibition at fifteen; her vocabulary | RESOLVED | ch49 pressure hour: "She asked it, rather … the leaning … like a road somebody had swept … She laid one crooked"; the coastal Gold Six "had let the air in front of her go slack" at fifteen. Cael's "Fold. Lane. Her. She arrives third." and Karis's *Permitted.* stay on the Halcenvane side of the wall |
| 12 | Protected patterns (ten added) | RESOLVED | overlap: 0 unprotected, 27 protected |
| 13 | Re-compose "Half a beat's a fortune" and "the first time anybody's described a floor to me" | RESOLVED | ch53: "Half a beat," said Cael. "Then we're rich." with the ch13 callback named ("what Lira had said to her boot on the frosty night at the mill town"; ch13: "Lira addressed the remark to her boot. 'Anyone else notice we're rich?'" and "a hard frost came down off the tops"). ch52: "I don't think anybody has ever just walked one with me and said what they saw." Neither source line survives (grep) |

### Priority 1 — Source tracking (per scene)

I checked the editorial's §6 table against the page scene by scene. Status is RESOLVED where the tabled sentences no longer keep the source's content *and* order; PARTIAL where a run still does.

| Scene | Status | Evidence |
|---|---|---|
| ch48 s1 narrowing / Ternhall pair | RESOLVED | Enters by things stopping: "The coach was the first thing to go … at *seven* he simply stopped … Then the mallet"; the Ternhall pair is gone ("The Blade two mats over was already walking toward the doors with his practice lath"). "Thirty conversations became twenty" kept |
| ch48 s2 Auremont ignored / broadsides | RESOLVED | Told through Lira over a stranger's shoulder and Karis's "meant to be found in a drawer in ten years"; the charter-has-no-door sentence is gone; the kindness is one quoted odds-sheet column |
| ch48 s3 the board | RESOLVED | Enters from Ephram at the foot of the steps; Withrow's absence before the strip ("Then he looked for Withrow, and she was not there"); the formation felt, not catalogued; Seln on the tower porch. One carried fact remains (Lira "at the slate in the circuit house at Ardenmere … he could not remember a single board in between") but it is the formation's canon, re-seen, and no longer the source's order |
| ch48 s4 long table / back room | RESOLVED | Withrow goes down the form "box by box, with one finger"; Brom speaks first from the door; Lira's case is a run of questions; her own side comes last; the coin in the pocket replaces the lane's mouth |
| ch49 s1 design session | RESOLVED | Enters from the chart wall; the "disruption" column corrected to "asking a man the time"; the note is *Opponent insufficient for profile. Revise upward.*; "You needn't. It was made with great care."; ends on *stranger* |
| ch49 s3 the file | RESOLVED | "a coat on a hook, holding the shape of somebody's shoulders, with nobody inside" (she read the shelf at sixteen) |
| ch49 s4 composure / registry / ladder / Gold Six / "no one her own age" | PARTIAL | Composure opens from the present; the ranks now run down the registry's page "like a well being filled"; the registry's love is "the rare coin rather than the bad one"; the Gold Six enters from the exercise sheet with the new ledger line. **Two runs survive in source order:** (a) "She had been Auremont's since twelve … Whole classes were assembled round her and broken up again when she grew past them. Stations opened early so that an evaluator could see her before the day began." (source: recruited/kept close/cohorts rebuilt/stations opened early; the probe pairs the cohorts sentence at 0.36 with "Accelerated cohorts, assembled around her age and rebuilt twice as she outgrew them"), with "the day of the garden court was a half-holiday now. There was a demonstration in the afternoon" following as in the source; (b) "There were the brave Silvers, who lost. There were the old Golds, who lost carefully … There were the program's measurements, and the tournament's processions. She shook every one of them by the hand … That had been taught to her too" (source: brave Silvers / career Golds managing dignity / calibration exercises / coronations / grace on the curriculum). Optional fixes 7 and 8 break both runs in the author's own sentences |
| ch49 s5 recognition | RESOLVED | "your own handwriting on an envelope addressed to somebody else"; the two doors "looked exactly alike"; "Never been met" gone |
| ch49 s6 risk officer / objection room | RESOLVED | The officer begins with his signature; her answer is a question ("if the only thing in the ring were me?") and "You've brought me a list"; "Seven years of—" / "You can finish"; counsel reads *Withdrawal of a filing. By the filing party only.*; the ladder-in-a-garden is gone. The officer's order-the-masts/price-against-myself/sign-first beats are still the source's three in order, but they are the scene's required content (BOOK_MAP: the risk office writes the spec) and the sentences are new |
| ch50 s1–s2 | RESOLVED | "sick with nerves"; "Umber had written down where the afternoon would end before it started"; "the same word twice"; ring before people; "You are the parties"; "He's never thanked anybody for anything in that tower. I asked." Item 47 verbatim |
| ch50 s3 Vastin | RESOLVED | Anchor sentence first; "screwed … crooked, on his first morning"; "in, held, done"; the river-and-bridge is gone ("nothing had come down it since"); the fourth sort is "the silence that falls when you have been taken off a list"; calendar from the bottom up; requisition from the sixth line back. Two short sentences still shadow the source's content ("It said nothing that was not so, and he had never asked a form for anything else"; the clerk "wrote the journey into it without a word. Vastin let him") but each is one clause and reworded; I would not reopen them |
| ch51 s1 inspection | RESOLVED | Enters from Rhagen's ringed staff (Ephram copies the numbers); Karis stamps the saddle, "Hollow on the near side"; Brom shoulders the bank; Lira "The stack hides you for one stride going north. Then you're there." |
| ch51 s2 Rooke's brief / orphan / harbour / Withrow | PARTIAL | The orphan is Bracken's reading; "*the bluff* the way it said *the harbour*"; "They want to see us do third properly." **Rooke's brief** still runs clause → grammar → "best-made thing on this floor" → "go and argue with it" → the near-smile, which is the source's order (doctrine → best-structured → almost smiled → go take it apart). **Withrow at the rail** still runs not-sat-for-a-bracket-bout → front rail, files closed → Rooke beside her with a blank sheet → nothing to write, the source's order. Optional fixes 9a/9b and 10 |
| ch51 s3 lessons / "robbed by" / calls | RESOLVED | "three things, in his own order"; "a man who has had his purse taken three times in one street and has started walking down the middle of it"; *Show him something*; "Brom. West saddle. He's coming before the bell."; the captain "taps along a plastered wall listening for the stud" |
| ch51 s4 consolidation / calls / harbour | RESOLVED (noted) | "the least exciting thing Cael had ever been part of, and the hardest"; the market at closing replaces the harbour. The fighter-by-fighter order (Ephram, Lira, Karis, Brom, Cael) is the source's, but it is the squad's natural order and every sentence is new; "counts the strokes in a boat" replaces the keel |
| ch51 s5 Rooke's file / Marek / standings | RESOLVED | "I looked for the name today and there wasn't one to write"; "It isn't a method. It's him."; standings enter from the house with no line; Halcenvane "twelfth to be read" |
| ch52 s1 party / crest / toast / stair | RESOLVED | Cold room first ("Not you, I think."); crest from the bell *not* ringing; "the moment went where those moments go" gone; "like water over a weir"; "the one for rolls and registers"; the log rebuilt around the dash "like a wall"; the vote on the wording cut; "as if she were trying a door". The coaches' sentence still carries the source's content (twenty years back / disagreed on everything / content) in one sentence; noted, not reopened |
| ch52 s2 the rail | RESOLVED | Enters from the double hammer-stroke; masts first; "like a rock left when the tide goes out"; "Nobody had a sheet for the other side of the ring." Item 26 verbatim |
| ch52 s4 ring walk | RESOLVED | Enters from his trench; "It would have been stranger if either had stayed away"; "correct a figure in a column"; the puddle; "you'd only feel it once"; the ceiling exchange ADDED (see (2)); "the only time a floor's ever honest with you … They never bothered to close that door"; "every rung exactly where my foot would go … and they clap"; "a new knife on her thumb"; "the way Karis spoke across a table". The losing exchange keeps the source's three beats in order (honest / nobody protected me / door left open) but "Being allowed to" is on the keep-list and the words are new |
| ch52 s5 | RESOLVED | "what a thing weighed by how he carried it in through a door"; "Go to sleep. I mean it." |
| ch53 s1 Seln | RESOLVED | "a list of warm-up times"; "the plain round copy-hand … that belongs to nobody" |
| ch53 s2 Rooke | RESOLVED | "There were eleven more in that." / "the ones I gave them to were slow the next day"; "nothing on my sheet I can't use" |
| ch53 s3 the eve | PARTIAL | Enters from the eleventh line on the door; pipe dies on "you can't turn in nothing", river on "It pulls your sleeve"; the recall as a doorway; the card crouched at the stove in three new lines; Karis's case turns on the rider's clause; "a tidy story told by the winners"; the loose thread "comes away in your hand at a counter in the wing"; the doubled "nobody wrote it down" removed. **One tabled sentence survived verbatim:** "The night before had a form now, and this was the third time they had kept it." — the source's opening sentence of the eve ("The night before had a form now … Tonight it convened for the third time in its history"); seven identical words, one under the gate. Required fix 5. The three objections stay in the source's order, which the drama needs (why she stopped must be last); the Auremont / Storm Path / ceremonies triplet is still the source's three in order with a potter's glaze for the guild's; noted |
| ch53 s4 the slip log | RESOLVED | All three italic paragraphs rewritten; Seln's observable supplied ("the rider and the protocols and the three scribes … by counting what came across his counter") |
| ch53 s5 the house at night | RESOLVED | "lying very still so as to seem to be"; the inventory as fingers on a blanket in a new order ("a whole hand and some over"); the clock "put it back, and be sure of something" |

**Surviving-images list (editorial §6, twelve items).** Checked each: the road to the river — gone; the question walking — gone (loose thread); "the moment went where those moments go" — gone; the three trays "since the first one" — now "since before he had a desk worth the name" (new); "robbed by" — gone; the harbour takes up a crew — gone; a ship it is fond of — gone (market at closing); the Gold Six ten beats — re-entered from the sheet, the middle run (the man / the slack air / two awake exchanges / the sleepless night / years to name it) remains in event order but the events are canon and the ledger line is new; the ladder's six items — PARTIAL (above); "two weights in the same pan" — now "as a man might look at two weights" (cut to one clause; acceptable); "civic event … Not fewer. None." — "Not fewer. None." gone, "civic event" is packet; "the first time anybody's described a floor" — gone; "Half a beat's a fortune" — gone; the card's five items — now three new lines; the night inventory's seven items — new order, new frame; "a correction he already knew how to make" — now "put it back, and be sure of something"; "we had a vote on the wording" — gone.

**The author's "category (c)" claim, tested.** I ran a scratch copy of the probe with the show threshold lowered to 0.35: 173 pairs at 0.35+, of which 27 are at 0.50+ (all protected or packet, as before), 37 in 0.40–0.49 and 109 in 0.35–0.39. I read all 37 of the 0.40–0.49 pairs and the 0.35–0.39 pairs for ch49, ch52 and ch53. They are, with four exceptions, matches to unrelated magnet sentences ("He filed the acceptance at the first bell", "It was whether the band survived the night", "The absurdity is not a flaw in the schedule", "She looked at him across the fresh floor for a moment"). The four content pairs are: the cohorts sentence (0.36, above); "Her body won't tell you anything, so don't ask it" (0.36, a packet beat of Karis's model); "My name goes on the bottom of the safety sheet" (0.36, the scene's required content); "She crossed his ground on the trial floor without even looking at him and he had half a second" (0.35, Karis's case, the trial's canon fact). So the probe's band is noise, as claimed. The genuine trackers that remain are the handful of content-and-order runs listed as PARTIAL above, which sit below the probe's radar because the words were changed; they are the editorial's category (b) at perhaps six to eight sentences in three chapters, down from about fifty-five in fifteen scenes. That is a real repair, not a synonym pass, and the optional fixes below take out the four runs most worth taking out.

### Priority 2 — Continuity, anchors and lines

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | ch48 board: three bracket finals + trial's final | RESOLVED | "the three bracket finals and the trial's final waited for finals day, and every one of them was set lower and printed smaller" |
| 2 | ch52 ceiling exchange at the west mast; keep the log | RESOLVED | "What are they rated to?" said Cael. / "She told him. … each head rated to take her full discharge at her assessed ceiling four times over before it ran hot, each cable grounded twice, and the margin … half again. Then she gave him the figure … in a single number. He said it back to her once … He did not write it down." Log: "*I asked her what the masts were rated to, which is the same as asking how much she has, and she told me, to the figure, and never asked why I wanted it.*" Ledger line corrected (STATE_LEDGER After M8: "Daeva told Cael what the masts are rated to, at the west mast (ch52)" and the Cael-knowledge row) |
| 3 | ch53 "this morning" → yesterday | RESOLVED | "Yesterday morning in the hall you put Lira down and listened past her." |
| 4 | ch50 Vastin: anchor; item 49 verbatim as thought; initials; one blank line | RESOLVED | Anchor: "For a year the Archmarshal Vastin had kept the Compact's record on the enrollee of Halcenvane, and kept it honest, and a week before he had sat in a held chair at Norhold to watch the boy fight a duelist, and written twice, and gone home before the figure." (duelist T14, dispatch T20: six days; "a week" is honest). Initials: "with no routing slip and no initials" (matches ch24 and ch43 exactly). Item 49: "As he straightened from it a thought came to him whole, the way his best thoughts did, and he let it stand in his head and did not write it down." then one blank line, then the protected paragraph verbatim (capital A opening the paragraph, as the editorial allowed). Double-blank-line count across all seven chapters: 0 |
| 5 | ch53 bank inventory glosses | RESOLVED | Wind: "six is where the hip starts sending bills, and past it they come due next morning"; the push: "the shove that moves a man off his feet from a hand's width"; Reydan's give: "the thing that lets a blow land on me and go nowhere". Spark unchanged; the read "as deep as it goes"; the sealed thing unnamed; the minute's form unchanged ("Set down tonight, ahead of the thing") |
| 6 | ch49 Daeva's whereabouts; ch47 the Silver's afternoon | RESOLVED | ch49: "For two days she had watched the frame … On the first morning she had stood through the steward's whole hour … That afternoon she had gone back … and been there when the Silver from the east house … On the second morning she had been in the warehouse … the coopers' boys had told her about it at noon." Zerin: "came down to the frame yesterday afternoon". ch47: "come down to the frame that afternoon, long after the register's hour … filled in, to be ready for the morning. Half the tunnel had seen it." / "Nobody entered anything." Consistent with the register's one hour at the first bell |
| 7 | ch52 toast log: eighteen years are the house's | RESOLVED | "Eighteen years this house waited to have something worth keeping" (ch01: "This house has not been there in eighteen years") |
| 8 | ch52 crown "where it shows" | RESOLVED | "straight over the top, so that's the longest road downhill in here"; and Cael's later "the longest one in here runs north and south straight over the oak" agrees |
| 9 | ch51 dropped "with" | RESOLVED | "Marek came through the crowd with his notation book under his arm" |
| 10 | ch48 / ch51 Lira's left arm as habit | RESOLVED | ch48: "the left one high and close, from a habit that had outlasted the week it had been needed"; ch51: "swinging her left arm loose and wide as she went, which she had not done all sitting and did now without seeming to notice" |

Also done unasked, correctly: ch50's acceptance box no longer says "Both parties confirmed" before the hearing ("*Parties to confirm before the Chief Adjudicator.*"), which closes the cold read's item 4.

### Priority 3 — Tags and audio

- **"said" counts** (my grep, whole word): ch47 44→23, ch48 35→37, ch49 32→33, ch50 27→25, ch51 28→28, ch52 45→27, ch53 40→23; movement 251→196 on 33,781 words = 58 per 10k. Matches the author's report. Every one- to three-word line keeps its tag ("Now," he said.; "That," said Rooke.; "No," said Umber.; "Good," said Zerin.; "No," said Brom.); the nine-chair scene and the standings keep theirs. RESOLVED, with three seams opened by the trim (required fixes 1, 3, 4).
- **ch52 "Lira bursts"**: "Lira burst. Cael stood with his eyes shut in the middle of the floor." RESOLVED.
- **ch50 blank line**: one. RESOLVED.

---

## (2) Continuity

**Calendar (#41).** T17 ch47 (breakfast, "Four mornings from now" = T21; the Silver that afternoon); T18 the rain and two hundred (ch47) = ch49's "second morning of the empty board"; T19 ch48 ("On the third morning"; "He had written that three nights ago" from T16), the board at dusk, the back room; T19 ch49's filing "before dawn on the third day"; T20 ch50 ("a day and a half" of shouting; the squall "the evening of the hearing"); T20 evening Vastin's dispatch "the day after the filing", departure "the morning after next" (T22, two days' post road, arrives T24); T21 ch51 and the standings "at the eighth bell"; T21 night the party, the ring at midnight ("The crews will build it on the night after the third-place trial", ch50); T22 the drill and the ring walk ("the last hour of the day"), Daeva's "the day after tomorrow" and Lira's "Two days" both = T24; T23 ch53 "the day before finals", Karis's "Yesterday morning". **One slip, repair-introduced:** Lira on the stair on T21 night now says "Day after tomorrow you're out there by yourself" (= T23, the eve). The pre-repair line was "In three days it turns round the other way", which was right. Required fix 2. No season, month, weekday or metric word; no year increment; the tournament's length in days not stated.

**M7 inheritances (nine).** All hold as the editorial found; the repair touched none of them. Rhagen's semifinal in one line ("And the ledger counts ground"); the format not restated; Rooke's five findings paid on the hill item by item; Vastin's office "two days from Norhold by the post road"; the read's seed is the air, not a body.

**Protected lines (exact grep, each once in ch47–53 unless noted):** 13 (*Overdue.* twice, ch48 and ch49, both the filing's word); 14; 15; 25's tail (ch48, capitalised as a sentence, as pre-repair); 26; 27 (with "favorite" and the dash); 28 (all four pieces); 47; 48 (both parts); 49 (capital A, one blank line before, anchored as his thought); 50 (both sentences); 51 (all four parts, "Neither number is us" twice as the exchange requires); 52 (Brom's two, Lira's, the slip); 60 (thirteen, in a garden court, ch49); §7.1's line in ch53. None used early. The packet lines the author lists are present whole.

**Knowledge boundaries and reserved truths.** Daeva never theorises what Cael is ("She did not try to work out from the file what he was"; "she found she did not want to guess"). The circle of four holds the council and the seal; Ephram outside the door, Seln never told and never in the room; his slip is inferred from "the rider and the protocols and the three scribes". Rooke does not ask. Umber states no theory. Vastin draws "nothing from them, as was proper". No *integration*, *fragment*, *witnessed*, *acquisition*, *absorb* in the seven chapters (grep). No maker, no system age, no Tide practitioner; the coastal fatality stays one plain sentence. The sealed technique is never named; "Because of who it came from" with "a quiet man at a counter in the wing" is the series' intended inferability (the cold read raised it; the ledger confirms it is by design).

**The ceiling exchange (ch52), checked specifically.**
- *Her knowledge:* she knows her own assessed ceiling and the facilities office's margin from the brass plate on every sill ("the rating was always her own assessed ceiling and a margin", ch49), she has read the protocol ("You read everything", the head; her finger "ahead of his voice" down Umber's list, ch50), and the risk officer's terms are hers to repeat ("Masts at your ceiling. The barrier up. The rows back. A floor rated for you, on a frame", ch49). Nothing she says exceeds that.
- *The masts' language elsewhere:* ch49 "masts … rated on my ceiling" (risk officer, her sill); ch50 "At each quarter of the ring a mast would stand, with an arrestor on top and two cables down into the trench"; ch52 "crown of iron nails … iron shoe … heard them hum"; the ledger's M9 note "four masts grounded twice into the trench". "Discharge" is BOOK_MAP's own word for the Storm's fire (M9 "a spark of discharge"; "the Gold discharge on the left side") and is new to the manuscript here, glossed by "before it ran hot". Consistent. One small count wobble is pre-existing, not the repair's: ch52 shows "a braided cable running down its length" and "the cable" (one per mast) while ch50 specifies "two cables" per mast; Daeva's "each cable grounded twice" leans on the ch52 reading. Optional fix 11 ("each mast grounded twice") reconciles both and matches the ledger.
- *The figure:* said aloud, said back once, not written, not printed on the page, which is what the ledger records and what §9's limits want. The log now describes exactly what the scene shows. "Nobody's done that in four years" was there pre-repair and is Cael's own count.
- *The Reader Standard:* "as if reading from the foreman's folded sheet" is Cael's simile (he saw the sheet at midnight; she did not), and reads as such.

**Vastin (ch50).** The new first sentence resolves every back-reference the cold read stalled on (the record kept a year, the held chair, the two notes, leaving before the figure); "A steward who knew his title before he gave it" and the digests now have a hook. Item 49 is verbatim and framed as his thought with "he let it stand in his head and did not write it down", which also keeps it out of his register (the register's own lines, *Close.* and *Everything I saw today, I already had a word for.*, match ch43 exactly). "nineteen years" in this room against ch05's "forty years" of service is not a conflict. "a week before" against T14/T20 is honest.

**Bodies and counts carried to M9.** Brom's LEFT shoulder "the far one" leaned on in E1; Karis's pink palms; Lira's arm a habit only; Cael's "dull pressure behind the eyes that would still be there in the morning" from the T23 recall; the narrowing twice (Lira at a yard; Brom four minutes). The bank as minuted matches BOOK_MAP §7.1's M8 row and the B4 reconciliation (Wind past six; Pressure at a fighting load "past the four blows a sitting"; Reydan's give "since the bout at Ardenmere that's its only paper"; the spark "past the two contacts a bout we allow it in public"; the read; Shadow sealed). Hesk's clock an hour fast (ch52 Karis's bench clock "ran an hour fast and was right about the seconds"; ch53 the winding) agrees with the M5 ledger. "Fenmark" (ch48) is Lira's old academy (ch03, ch13, ch24, ch34, ch35), not a new name. Brom's "nineteen" (ch53) are Rooke's nineteen exercises (ch32). The Silver Standard's guard: the ledger says a guard of two; the page now says "with two of the colour-guard on either side", which a listener will count as four. Required fix 6.

---

## (3) Formula and tools (reproduced on the current text, 2026-10-05)

- `formula_metrics.py` on ch47–53: words_prose 33,781 · sentences 2,551 · mean 13.24 · median 9 · sd 11.37 · ≤5 words 28.3% · ≥40 words 4.2% · paragraphs 840 · paragraph median 29.0 · scene breaks 26 (7.7/10k) · words/scene 1,023.7 · FRE 88.3 · FK 4.24. Identical to the author's metrics.txt.
- `ed.sh overlap book-05-the-silver-standard 8`: **0 unprotected** shared runs of ≥8 words; 27 protected.
- `ed.sh gates book-05-the-silver-standard 8`: reader_standard 0, metadata 0, modern 0 on all seven chapters (3,515 / 3,914 / 6,722 / 4,499 / 5,174 / 5,031 / 5,000 words).
- `sweep_probe.sh book-05-the-silver-standard 8 8`: 1,494 sentences; **skeleton 2%, close 12%**; by chapter 47: 1/7 · 48: 3/13 · 49: 0/12 · 50: 2/11 · 51: 1/11 · 52: 3/13 · 53: 3/12. Pre-repair 2/14. No scene flagged over 15% skeleton. Every ≥0.50 pair is protected or packet (items 13, 25, 26, 27, 28, 47, 48, 49, 50, 51, 52, §7.1; "the whole category's problem"; "Tonight was for making sure I know why"; "household"; "the theater"; "come back to this table"), plus "He went off to talk to the staff" at 0.50 against "He went down to the Concourse at midnight", which is noise.
- Lengths: −10 / +39 / +133 / +40 / +63 / +125 / +42 words by chapter; no scene changed shape.

The close band's floor is set by the fourteen packet and protected lines that must stay and by the common-sentence magnets; 12% on this movement is as low as a re-composition can honestly go without avoiding plain English, and the six-to-eight residual runs I list would move it by well under a point. I accept the author's stop.

---

## (4) Reader clarity

**Speaker attribution after the tag trim.** I checked every dropped tag in ch47, ch52 and ch53 against its paragraph. Three fail and are required fixes: ch47 l.149, where removing "said the other" left an opening quotation mark inside the speech ("either. "Look at the Silvers."); ch52 "You can't climb it." / "You can run along it." / "Yes." A sideways look. "You can run along it.", where the pre-repair "She glanced at him sideways" told the listener which line was hers and the new "A sideways look" does not; ch53 "Karis put the pen down." followed by "Nothing moved. Not a hair on my arm. A river going that fast, I'd have felt it from the gallery.", which is Lira's (she was "right beside it. North-east ramp.") but lands on Karis for a beat. Everything else resolves inside the line: ch47's drill ("You'll pay for that door in heat." / "Every frame costs heat. This one costs it when I choose."), the bread stall, the twelve bursts ("You called me," came Lira's voice); ch52's trench ("How deep?" answered by "He let the grating down"), "Once is enough." She stepped back., "Losing?" / "Being allowed to."; ch53's models (Brom's bound forearms; "Why not?" is Karis's by content; "Heavy, and then?"), the council (every turn named or carried by "He did not look away" / "She held his eyes" / "Brom nodded"), and Cael's resumed speech after "He did not say the name" ("If I use it …"). The pre-existing "It isn't for rain." / "They roofed this place …" / "It's for the cables." She stood is a two-hander a reader follows by sense and was passed by the editorial; I leave it.

**Referents and time-words at the seams.** The re-entries are clean: ch48 s3 "Then he looked for Withrow" after Ephram; ch49 "On the second morning" opens and is paid at "the coopers' boys had told her about it at noon"; ch50 "For a year the Archmarshal Vastin" before "The fast dispatch reached his room"; ch51 "One house at the reading had no line" before the standings are explained (deliberate, and the explanation follows in the next paragraph); ch52 "The hammering started a little before midnight" is heard from his room after the stair; ch53 "The eleventh thing they did not know" before the door is explained in the next line. The one broken time-word is Lira's "Day after tomorrow" (fix 2). "Yesterday morning in the hall" (ch53) and "a week before" (ch50) are right.

**The thirteen-year-old lens.** The inventory now carries its prices in Cael's mouth; "discharge" is glossed; "the leave runs out where the lane does" rests on Karis's *Permitted.* and "where the air has let her by" two paragraphs earlier; "Then we're rich" is explained in the next sentence. Nothing in the movement is a word a child would stop on without the page's help. The Reader Standard gate is 0.

---

## (5) Listening proof, by chapter

Mechanical pass (per-paragraph quote and asterisk parity; `---` with a blank line on both sides; digits outside the protected board line and log): ch48, ch49, ch50, ch51, ch52, ch53 clean; ch47 one paragraph with three quotation marks (l.149, fix 1). ch50 l.49's "*1. The parties. 2. Underwriting. 3. Protocols and the ring. 4. The rating.*" is the agenda as a document and was pre-repair; a narrator reads "one, the parties", which is right.

- **ch47.** Changed regions: the breakfast tags, the frame, the Silver's afternoon, the stall, the twelve bursts, "Two days." Quotes balanced except l.149. Italics balanced (*Ready. Not early.* etc.). Scene breaks at ll.43, 123, 161 spaced. No numerals. Homographs: "wound" absent; "read"/"lead" fine in context. Joins: "He sat down. 'Rhagen. We're fighting Rhagen.'" and "Lira snorted." read cleanly aloud; "And the table laughed" as a sentence opener is fine for the ear.
- **ch48.** The narrowing, the odds-sheet column (one long italic, balanced), the board, the form box by box, the back room. Quotes and italics balanced. "*filed; acceptance pending*" and the board line are set as the protected item. Joins at "Then Seln spoke, from the end" and "before he had even turned round from it, he spoke" are clean. The *Decided in the back room* log balanced.
- **ch49.** The chart wall, Zerin's bench, the pressure hour, the coat on a hook, the registry page, the sheet, recognition, the two days, the stair, the room. Italic runs (*Phase one: assessment,* / *tidying* / *Opponent insufficient…* / *Specimen.* / *Corrective: lane integrity…* / *The exercise worked…* / *Withdrawal of a filing…* / *Overdue.*) all balanced. "Am I early … or are you late?" intact. Ear: "rows back" / "rose" no collision in context; "lead" (glass "set in lead") reads as the metal by its sentence. Joins clean.
- **ch50.** The counter, the agenda, the rider, the ring before the people, "You are the parties", Vastin whole, the squall. Italic log lines balanced, including the protected paragraph after one blank line. Umber's two consecutive quoted paragraphs each close their quotes (two utterances; acceptable aloud). "the morning after next" and "two days from Norhold" voice cleanly. No numerals except the agenda.
- **ch51.** The hill (counting in words), the brief, the bedsheets ("the second A had been put in backwards" reads aloud), the exchanges, Rooke's file, Marek's page (*One point. Everything goes through the fifth man.* balanced), the house with no line, the standings, item 15. Italic calls (*West, old.* / *Crown, two, wait* / *Show him something*) balanced. "Third of fourteen" in words. Joins clean.
- **ch52.** The party reordered (every paragraph balanced; the keeper's speech one paragraph), the crest, the toast and its log (dash inside italics balanced), the stair (fix 2), the rail notebook (*Bull-nose* balanced; "Four feet, each way" in words), the drill, the ring walk (fix 3; the ceiling exchange reads aloud as prose, no figure voiced), item 51 with the italic repeat balanced, both logs balanced. "Lira burst." no longer a verb collision.
- **ch53.** Seln's strip (protected italics balanced), Rooke's pads, the door and the wall (*We don't know.* / *A pipe. Dead. Brom: she turned.* / *Most of an hour.* / *she arrives third* / *trial, read live* / *Permitted.* all balanced), the card (three lines, balanced), the council (fix 4 at "Nothing moved"; fix 5 at the eve's second paragraph), the minute (one italic paragraph, balanced), the slip logs (three italic paragraphs, balanced), the house at night, item 28 (four italic pieces, balanced). "ash" / "broke the new ash into the old" voices cleanly; "wound it" is the clock and reads as such from "took it off the sill and wound it".

---

## (6) Line fixes

Each `old` string was verified with `grep -c -F` to occur exactly once in the named file.

**Required (1–6).**

1. `manuscript/chapter-47.md`
   old: `The other shook his head. "Nobody wants to be the man he doesn't beat, either. "Look at the Silvers. They lost and they're heroes. Who files to be the third hero? It's the same bout twice."`
   new: `The other shook his head. "Nobody wants to be the man he doesn't beat, either. Look at the Silvers. They lost and they're heroes. Who files to be the third hero? It's the same bout twice."`

2. `manuscript/chapter-52.md`
   old: `Day after tomorrow you're out there by yourself, and we're the ones at the rail.`
   new: `Three days from now you're out there by yourself, and we're the ones at the rail.`

3. `manuscript/chapter-52.md`
   old: `"You can't climb it."`
   new: `"You can't climb it," she said.`

4. `manuscript/chapter-53.md`
   old: `"Nothing moved. Not a hair on my arm. A river going that fast, I'd have felt it from the gallery."`
   new: `"Nothing moved," said Lira. "Not a hair on my arm. A river going that fast, I'd have felt it from the gallery."`

5. `manuscript/chapter-53.md`
   old: `The night before had a form now, and this was the third time they had kept it. The first time nobody had known it was a form.`
   new: `They had kept this night twice before, and by now it had a form. The first time nobody had known it was a form.`

6. `manuscript/chapter-51.md`
   old: `with two of the colour-guard on either side. It would not be unbound before the closing.`
   new: `with one of the colour-guard at either side. It would not be unbound before the closing.`

**Optional (7–11): the last source-order runs, re-ordered in the author's own sentences, and one count. Apply at the coordinator's discretion; none is a defect a reader would notice.**

7. `manuscript/chapter-49.md`
   old: `Afterwards nothing in her life had been left to happen by itself. Whole classes were assembled round her and broken up again when she grew past them. Stations opened early so that an evaluator could see her before the day began. Floors were relaid to her measure.`
   new: `Afterwards nothing in her life had been left to happen by itself. Floors were relaid to her measure. An evaluator who wanted a look at her had his station opened before the day began, and came, and looked. Whole classes were assembled round her and broken up again when she grew past them.`

8. `manuscript/chapter-49.md`
   old: `There were the brave Silvers, who lost. There were the old Golds, who lost carefully, with their dignity held up in front of them like a shield. There were the program's measurements, and the tournament's processions.`
   new: `There were the program's measurements, and the tournament's processions. There were the old Golds, who lost carefully, with their dignity held up in front of them like a shield, and the brave Silvers, who simply lost.`

9. `manuscript/chapter-51.md`
   old: `"Their whole doctrine, in one line, as they'd say it themselves. Five-as-one-argument.`
   new: `"I've read their book twice, and I'd sign it. It's the best-made thing on this floor all week. Their whole doctrine, in one line, as they'd say it themselves. Five-as-one-argument.`

10. `manuscript/chapter-51.md`
   old: `"It's the best-made thing on this floor all week," said Rooke. "I've read their book twice. I'd sign it." He looked at the five of them, taped and waiting, with their year written all over them. "So go and argue with it."`
   new: `He looked at the five of them, taped and waiting, with their year written all over them. "So go and argue with it."`

11. `manuscript/chapter-51.md`
   old: `Withrow had come down to the front rail. She had not sat there for a single bracket bout of the sitting; she had watched those from the upper gallery, among the other chancellors. Today she sat at the rail itself, with her closed files on her knee and her hands folded on them, and Rooke stood at her shoulder holding a coaching sheet with nothing written on it.`
   new: `Rooke went down to the front rail with a coaching sheet that had nothing written on it, and found Withrow already there. She had watched every bracket bout of the sitting from the upper gallery, among the other chancellors, and had not once come down. Today she sat at the rail itself, with her closed files on her knee and her hands folded on them, and he stood at her shoulder.`

12. `manuscript/chapter-52.md`
   old: `each cable grounded twice`
   new: `each mast grounded twice`

(Fixes 9 and 10 go together; 12 is the cable count against ch50's "two cables" and the ledger's "grounded twice".)

---

## Notes for the coordinator (not for the author)

- With fixes 1–6 applied the movement is CLOSED. Fixes 7–12 are at your discretion; if applied, the ledger needs no change except that fix 12 makes the page match its "four masts grounded twice" wording exactly.
- The ledger's After-Movement-8 block already carries the corrected ceiling line and the Cael-knowledge row; both match the page as it stands.
- Pre-existing and left alone: ch52's one-cable / ch50's two-cables (fix 12 reconciles if wanted); ch49 "steady for two days in front of two hundred people" (the two hundred were only the second morning; reads as loose speech); the ch52 "It isn't for rain" two-hander.
- The team-trial final is now on finals day's card by ch48's board line; M9 places it on the morning card per your ruling 6.
