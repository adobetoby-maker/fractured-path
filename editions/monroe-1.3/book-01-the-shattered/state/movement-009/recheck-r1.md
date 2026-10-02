# Recheck r1 — Book 1, Movement 9 (chapters 54–60)

Review seat: Claude Fable 5.1 (targeted recheck, not a fresh review). Author of the repair: Claude Opus 5.5. Method: `diff -U0` of each chapter against `pre-repair/`, every hunk read in context; the brief, both reviews and "## Repair r1" of the author's report read in full; BOOK_MAP §§1 and 7, STATE_LEDGER (calendar lines for M2, M6, M8 and the M9 calendar in the author's report), the M9 packet; the probe, the overlap tool, `ed.sh gates` and `formula_metrics.py` run by me. No manuscript file was modified.

---

## Verdict: CLOSE WITH LINE FIXES

Scope: three line fixes, listed at the end. One is a real defect introduced by the repair (a sentence in ch 59 broken at a join: `…and the gate. and what he had had for supper…`). Two restore a dialogue tag where the thinning went one step past the brief's own rule (the paragraph before the speech names the *other* speaker, or three people share the scene). Nothing else is open. The seven months question is ruled below in the author's favour: no fix.

---

## (a) Brief items

### Months ruling (the ch 58 line)

What the ledger gives:
- The vouch and the brackets: **day 8** (M2 calendar, "Day 8 (Thursday): Vell's table in the morning"; "Lira: has vouched"). From then on the formal line reads *Unrated (14; nothing to register; vouched, L.)* and the board reads *unrated (vouched)* (After M4: "the formal line still reads… and the board reads *unrated (vouched)*").
- The assessment: **day 97** (M6 calendar, "Day 97 (Tue): assessed-Copper"), as "a short line in Vell's hand beside his standing line. The board and card are not described as changed" (M6 new canon 16); "Vell: assessed is not rated" (M7); "Still assessed-Copper and unrated at the rope. Still no name in Vell's book" (After M8).
- The bout: **day 200** (author's M9 calendar; Monday day 180 = board; Sunday fortnight from the Sunday-186 card).

So on the morning of the bout the brackets have stood 192 days (about six and a third months) and the assessment 103 days (about three and a third). The manuscript's "seven months" is the book's own rounding for Cael's whole time in Ardenmere (he arrived day 4; BOOK_MAP §1 calls the ending "about seven months later"), and it is used that way in six unchanged places that both reviews let stand: ch 54 "For seven months the line under his bouts had said the same thing: *unrated (vouched)*", ch 57 "In seven months the board had known him as a line in brackets" and "For seven months, at this place in the rules, she had said *unrated*, and *vouched*", ch 58 "which in seven months he had never once seen happen", ch 59 "where in seven months there had only ever been a pair of brackets", ch 60 the bread woman's loaf "every morning for seven months". The vouch is four days younger than his arrival; the rounding is the same.

**Ruling.** The editorial's "since the winter" was the right fix for the *assessment* while the line read *assessed Cu (vouched)*. The author's card decision changed what the line says, and with it what the sentence counts. `the way she had written it for seven months: *unrated (vouched)*` is true to the ledger and consistent with ch 54/57/59; `since the winter` would now be false (the brackets date from the autumn). The assessment's age is correctly placed where it now lives: ch 55 "The assessment she had written beside his standing line in the winter stayed in the margin where she kept it" (day 97 is the book's winter) and ch 58 "The assessment lived in her margin, not on the line." **No fix.** The author's restoration stands.

### The card wording — RESOLVED
`grep -i assessed` over ch 54–60 returns exactly two lines: Vell at the rope (ch 57:133) and the protected ledger line (ch 59:77). *assessed Cu* appears nowhere. The line/card/board/return now read *unrated (vouched)* in ch 55 (the book line and the card: "Her book got the line it had always got, in her own hand: *unrated (vouched)*… *against unrated (vouched)*"), ch 56 (the district return copy), ch 57 (the board) and ch 58 (the morning line). Vell's "Cael Hesk-ward," said Vell. "Assessed-Copper. Vouched." is set up by the unchanged sentence before it ("For seven months, at this place in the rules, she had said *unrated*, and *vouched*, and stopped there") and paid by "She had never said it at the rope before." It says at the rope what she then writes on the protected line, which is the right order; and it is a motivated departure from M7's "so will I at the rope" — the yard has come, which was her own condition.

### The drawer thesis — RESOLVED
Kept, as the brief asked: Cael at the board (ch 54 s1, unchanged), Hesk's letter (ch 56, read only), Vell's "It keeps them asked about" (ch 59), and the *frightened* beat intact at ch 56:185–193 ("Put it on the post. A stroke for it, and a ring, and *frightened* beside it in small letters… We did. On Feryn's bill."). Cut or varied, each verified in the diff: Feryn ch 54 → "So you'd like to cost them something… That's a fighter's answer, anyway. Not a clerk's."; Lira ch 54 → "Gone and stood in the middle of the market, so nobody could ever say they hadn't seen him."; Lira on the steps ch 56 → the protected line plus "It's your grandfather's, near enough. I've been turning his letter over since Monday… I only said it shorter." (and Cael's "You had it first" still reads right against it); Cael to Coss ch 56 → "I was quiet all autumn… It didn't keep the sweep out of the market, or the mark off my file, or you off that cart." with "better in a drawer" → "better somewhere small"; Cael to Lira ch 60 → "I made myself loud for one kind of looking." The idea is now stated in full three times and gestured at twice.

### The seven merges — RESOLVED
Break counts (heading plus `---` lines): pre 42 → post 35, i.e. 35 breaks → 28. The seven removed, each read at the join:
- ch 55 s2+3: "She was asleep before she had finished adding this. She woke before it was light with the sum still there, and went down through the widow's shop…" — time cut; clean.
- ch 55 s5+6: "He was still turning it over the next morning, coming down from the old man's gate, when he passed the woman who kept the chalk board…" — antecedent is Doss's "He'd wait" two paragraphs up, and the sentence names it ("with *he'd wait* in his head"); "two was not three" now lands as pattern.
- ch 57 s3+4: Feryn leaves the bench; "When she had tied off the right wrap, Lira took the Log out of his coat on the bench…" — continuous.
- ch 58 s5+6: Darrow out through the gate; "Lira put him on the bench before his legs could give their own opinion…" — motion cut; "him" is unambiguous once Darrow is in the lane.
- ch 59 s1+2: Doss's hand on the table; "Lira came to the kitchen door at the hour of the grey half and did not come in." — continuous.
- ch 59 s2+3: "Then Lira jerked her head toward the back wall, and he got up. / Vell was at her table in the shade of the back wall…" — motion cut.
- ch 60 s3+4: "…asleep before Yeni had finished turning down the lamp. / In the morning he went up to the grey half…" — time cut.
No between-exchange break was touched (ch 57 removal is before the bout; ch 58 removal is after Darrow leaves); the break before Vell's cutaway stands.

### The tail — RESOLVED
ch 59: the eel woman, the kindling man and the pump women are gone; "In the afternoon he went down to the market, because Lira said he could walk if he walked slowly, and the boys found him at the bottom of the market steps." leads straight to the geese and the bread woman ("Don't you dare." / "You had your chance"). ch 60 Coss: compressed by about a third (the rack, the register, the query form each in one sentence) with the slip, the printed head, "There was a date", the refusal to infer ("A thing could be dated the day after another thing without being caused by it"), the footprints, *Noted*, the empty page, "the first thing in his working life that he could not have written down and then stood behind", the key home and the carried seven all kept. The stranger (ch 59 s6) is intact beat for beat, including "That was all, at first.", "They were looking at him." and "He did not go after them." The last line is still "She kept them in the grey half for as long as there was any grey half left."

### Tags, joins, speech — RESOLVED with two restorations (fixes 2 and 3)
"said" count 185, as reported. Every speech line in the bout is byte-identical (ch 57/58 hunks touch only narration and the card). Vell's count and the landing beats are unchanged: "It had been there first.", "The gate was open.", "It made a noise like a latch.", "Darrow knelt." each once. The only speech changed anywhere is the five thesis lines above, all sanctioned by the brief. Narration joins read as joins; the two places I would not have thinned are listed under (c).

---

## (b) Source distance

- `skeleton_probe.py --show` (source ch 21–24 vs ch 54–60): **TOTAL sentences=1373, skeleton=1%, close=10%.** Per chapter: 54 1%/11%, 55 0%/5%, 56 2%/11%, 57 0%/10%, 58 0%/10%, 59 1%/11%, 60 2%/11%. Highest scene: ch 60 s3 at 8% skeleton, which is the three protected log lines.
- Every listed sentence at ≥0.65 is protected or packet-quoted: ch 54 s5 0.91 "I'd rather be worried and informed…" and 1.00 "You're more like him than you probably realize."; ch 56 s1 1.00 *Being seen is not the same as being safe.*, s4 0.88 "It changes who'd have to explain themselves…"; ch 58 s7 1.00 "They're one thing with parts I haven't found all of yet."; ch 60 s3 1.00 ×3 (the fence sentence and the closing two). **No unprotected sentence ≥0.65.** (Two 0.50s shown — "All of it, where you can both see it." and Hesk's "more like me than you know" — are under the gate.)
- `ed.sh overlap book-01-the-shattered 9`: `# summary: 0 unprotected shared runs of >= 8 words; 8 protected runs (allowed)`.

---

## (c) Changed regions

**Joins, fragments, referents, callbacks.**
- **Defect (fix 1):** ch 59:163, the Hesk-letter lead-in was joined into one sentence and a full stop survived inside it: `…and the bucket and the gate. and what he had had for supper after, which had been nothing…` — a fragment beginning with a lowercase "and". One character.
- **Tag thinned past the rule (fix 2):** ch 55:78–80. "The widow was up… She looked at Lira, and at the tick, and at Lira again." is followed by the untagged `"I'll give you a mark for it."` The last-named subject is the widow; a listener assigns the line to her and has to back up at "It's not worth a mark." The pre-repair tag ("said Lira") was the right one to keep here.
- **Three-speaker scene (fix 3):** ch 56 s3 (Feryn's notes on the wall) lost four tags (lines 105, 115, 133, 139) although the author's report says tags were kept there. 133 and 139 resolve by their paragraphs (Lira "had leaned over too"; Cael completes her dash). 105 does not: after Feryn's confession and a paragraph that ends on "Cael saw that she had put it away", `"What did they say it felt like? The three. Hitting him."` could be Lira's or Cael's, and the next untagged questions ("Which side?", "How does he stand?") ride on it until the washer bill reveals the asker. One restored tag at 105 anchors the run.
- Feryn's "So you'd like to cost them something" — "them" is loose but reads as the people Cael has just described wanting him gone; acceptable.
- No orphaned callbacks: the cut market walk's "whether the district had changed" has no later referent (grep "changed" in ch 59 returns nothing); "below the fourteen names" (ch 56:275, replacing "the line about the drawer") matches ch 54's back-page list; "You had it first" still answers Lira's shortened line.

**Calendar** (weekdays from day 55, a Tuesday; author's M9 calendar checked against the ledger).
- ch 54: board Monday 180; Feryn, Vell's Wednesday card, Lira's room "before the lamps" Wednesday 182; "all through Tuesday at the post" fits.
- ch 55: Lira's cutaway Wednesday night → "woke before it was light" → the widow's yard → "I asked Doss this morning at your yard door, coming in off his watch" → the straw post at first light, all Thursday 183. Doss's kitchen scene is "an hour before his watch" (evening) and he reports her question as past ("The girl asked me about Iron"); with the merge, the chalk-board woman is "the next morning" = Friday 184, the second straw-post morning, which is what the pre-repair said in other words and what the editorial dated. Her "I heard you've got an Iron coming" is still two days before the Sunday-186 card (noted by the editorial, no fix).
- ch 56: Hesk's letter "on the Monday" 187, "written on the night of Coss's pie stall" 178, "a week on the road"; the steps on the tenth night = Saturday 192, "turning his letter over since Monday"; Coss "On the Wednesday before the bout" 196, "My section head put it on my desk on Monday" 194.
- ch 59: "It was a Monday" 201; Hesk's proud letter "written on the Sunday before last" = 193, after sitting "three days" with Cael's letter (posted 183, arrived ~190), "the best part of a week before Darrow" ✓.
- ch 60: stranger "Two days after" = Tuesday 202; Coss "on the Wednesday afternoon, three days after" = 203; "come back on the noon cart… a week ago" = 196 ✓; "through two nights of carters' benches… At his desk on the Friday" = 198 ✓; "at home on the Sunday" = 200 ✓; "put on his desk on Monday of last week" = 194 ✓; "since then he had gone to the rack himself for the next one" = this one ✓. Cael's letter "on the Wednesday night" 203; "told off once this week for sitting on a wall" = Tuesday ✓; the grey half Thursday 204. Coss's week is now counted one way.

**Knowledge boundaries.**
- ch 60:15: "Even the man with the pin in the autumn had it, and all he did was walk through a market." Cael no longer knows the pin was borrowed. ✓
- Cael's closing lines (ch 60 s3) and his letter to Hesk carry nothing of Coss's flag; the Coss cutaway is sealed at "He did not know who he was keeping it from… or from a boy on a cot two days east". ✓
- Nothing new is said about the stranger's sex, features or source; Coss still refuses the inference from two dates. ✓

**Protected lines.** All present and exact, once each (twice where the map says): the `FRAGMENT NOTICE` block (ch 58); "What are you?" / "I don't fully know yet." (ch 58, Darrow, the only occurrence); "It goes in the book… as it happened." (ch 58:191, interpolated as the map's ellipsis allows); the fence sentence (ch 58 and ch 60); the ledger line (ch 59); the closing log line (ch 60, followed only by the bench image); *Being seen…* (ch 56, as read); "It doesn't change what you are," said Lira. "It changes who'd have to explain themselves if something happened to you." (ch 56, tag interpolated — accepted by the editorial); "I can't out-quiet that." (ch 56); the four §2.21 lines (ch 54); "During, I coach." / "After, I get to be a person." (ch 55 born, ch 58 said). Each first appears where BOOK_MAP §7 says.

**Reader Standard.** `ed.sh gates book-01-the-shattered 9`: reader_standard=0, metadata=0, modern=0 on all seven. Nothing in the changed regions adds an oath, a wound, or a touch beyond the embrace.

---

## (d) Metrics (my run of `formula_metrics.py` on the seven chapters)

words_total 33,209 (wc 33,287: 54 4,921 · 55 4,876 · 56 4,867 · 57 4,620 · 58 6,830 · 59 3,713 · 60 3,460); sentences 2,534; **sentence_mean 13.1**; sentence_median 8; **share_ge40_words 0.045** (at the ceiling, as the author says); share_le5_words 0.343; paragraph_median 26; scene_breaks_marked 28; scene_breaks_per_10k 8.43; **words_per_scene 948.8**; FK grade 3.61. The author's numbers are confirmed exactly.

---

## For the book-completion pass

Out of this recheck's scope, but noticed:
1. **"Seven months" is the book's rounding, not a count.** Ardenmere time at the bout is 196 days from arrival; BOOK_MAP §1 says "about seven months". Check that no earlier movement says "six months" for the same span, and that the ledger's "After Movement 9" fixes the day numbers above (vouch day 8; assessed day 97; bout day 200) so later books quote one calendar.
2. **Ledger entry for M9** should record the card decision as canon: the line reads *unrated (vouched)* until the yard comes; the assessment is a margin note; Vell says the name and "Assessed-Copper" at the rope only on the day the yard comes, superseding M7's "so will I at the rope". Also: Lira asks Doss at dawn day 183; Doss's kitchen scene the evening of 183; the chalk-board woman day 184.
3. **Season words.** ch 60 "the mark Ilsev had found in the spring" (Ilsev day 141) against ch 55's "in the winter" for day 97 and the M8 ledger's spring beginning around the pear blossom (~day 178). Decide where winter ends for this book and sweep the three movements that name it.
4. **Darrow's stance** (edition: right foot forward, left back and nailed) differs from source ch 23; the series map should quote the edition's foot, as the editorial already flagged.
5. **Darrow's autumn** ("back up this river in the autumn… he'll want to know") and Feryn's "The coat's not done… I'll not see it till the autumn" both fall in the between-books gap; Book 2's map must stage or lapse them.
6. **Coss's flag, the empty log page and the key** need their Book 6 plant entry; the ledger phrase for the Iron Path should be "the crossing is the reset after each load" so Book 3 ch 8's wording and this one are the same fact.
7. **Feryn's "I've been here a fortnight"** (ch 59, day 201; he arrived day 182 and went down the river twice between) is loose by five days; harmless unless Book 2 counts it.
8. **Reporting verbs** still ~90 per 10k in M9 (target ~41). If the book pass harmonizes density across movements, the multi-speaker scenes here (ch 56 s3, ch 59 s1–3) are where the remainder lives, and fix 3 below adds one back on purpose.
9. **≥40-word share at the ceiling** after the joins; any further joining in a book-level smoothing pass should aim at 15–30-word sentences, as the author notes.

---

## Line fixes

Each old string verified with grep to match exactly once in the named file.

1. `manuscript/chapter-59.md`
   old: `and the crossing, and the straw post, and the bucket and the gate. and what he had had for supper after, which had been nothing,`
   new: `and the crossing, and the straw post, and the bucket and the gate, and what he had had for supper after, which had been nothing,`

2. `manuscript/chapter-55.md`
   old: `"I'll give you a mark for it."`
   new: `"I'll give you a mark for it," said Lira.`

3. `manuscript/chapter-56.md`
   old: `"What did they say it felt like? The three. Hitting him."`
   new: `"What did they say it felt like?" said Cael. "The three. Hitting him."`
