# Recheck r1 — Book 5, Movement 3 "The Scouting Economy" (chapters 14–19)

Review seat: **Claude Fable, review seat** (standing in for the Sol/Codex seat, which is out of quota), fresh context, 2026-10-05. Author under recheck: Claude Opus 5.5 (same-author repair r1). I read the full current movement (`manuscript/chapter-14.md` … `chapter-19.md`, wc 32,482), the brief, both reviews, the author's "## Repair r1", the `diff -U0` of every chapter against `pre-repair/`, BOOK_MAP §6/§10/§11/§13, STATE_LEDGER (entry anchor; After Movement 2; After Movement 3 with the coordinator's rulings), the M3 packet and `protected-patterns.txt`. No manuscript or repository file was modified except this report. No git commands were run.

---

## VERDICT: CLOSE WITH LINE FIXES

**Scope:** three line fixes, none touching a bout, a protected line or a packet line.
1. **One residual clock error the repair missed** (ch19 line 401): the quay scene still has Lira say the equipment mistress "nodded this morning". The repair fixed the three lines the brief listed (353, 385, 389) and left this fourth one, which carries the same two-day error into the line that pays the coat-rack off ("One each. That's the whole estate."). Required.
2. **Two minor count wobbles in ch17**, both pre-repair text, both flagged or implied by the editorial review and outside the brief's named scope: the inn tally of "five nights" against a six-night stay (line 7), and "the next three evenings" after "the first evening", which makes four evenings against a file read on "the third night" and returned the morning after (line 57). Minor; cheap; fix now rather than carry.

Everything in the brief is otherwise RESOLVED with the text as it stands. No second repair.

---

## (1) Brief items — RESOLVED / PARTIAL / NOT, with evidence (diff -U0 vs `pre-repair/`)

### Priority 1 — Lira's Iron final: the touch count — **RESOLVED**

The author took the brief's first option (keep "in four"). ch18 lines 107–115 now run: summary unchanged, "She won the final in four exchanges, two touches to one"; E1 the Stone's touch ("The Stone took the first touch anyway"); E2 Lira's ("Lira took the second exchange's touch from below"); E3 the refusal, then the new close:

> `-The Stone stood by the north rope for some time, waiting for her. The gallery began to murmur. At last he came back out to the middle, because the glass was running and a fighter who will not come to his opponent cannot touch her. As he came off the damp slate onto the dry, his feet changed speed, and she was waiting for exactly that change. She took the touch there, and the fourth exchange's after it.`
> `+The Stone stood by the north rope for some time, waiting for her. The gallery began to murmur, and the glass ran out with nobody touched.`
> `+In the fourth he came back out to the middle at the call, because a fighter who will not come to his opponent cannot touch her. As he came off the damp slate onto the dry, his feet changed speed, and she was waiting for exactly that change. She took the touch there, and the bout with it.`

Count by exchange: 0–1, 1–1, 1–1 (glass out, nobody touched), 2–1. Two touches inside four, the bout ending at her second touch: #39 regional format holds. "She did not follow. She stopped in the middle of the floor on dry flags, and stood there, and let him go." is kept verbatim (line 109). "That was your bout," she told him at the rope. "I only fought it." is kept (line 119). "The figure was twenty-five. It was her third title of the season" unchanged (line 115). The author's ratings table ("2–1 in four … 25") matches the page.

### Priority 2 — The clocks — **PARTIAL** (ch19 one residual line); **RESOLVED** (ch15)

ch19, the three lines the brief named, all changed as asked:
> line 353: `"…I've been saving the coat-rack."` → `"…I've been saving the coat-rack for two days."`
> line 385: `"And this morning there they were, two lanes over…"` → `"And on the Fifth-day morning there they were, two lanes over…"`
> line 389: `"So all day I've been asking where it went."` → `"So for two days I've been asking where it went."`

Checked against the author's day table and the house formula (day N → weekday (N mod 7)+1): the coat-rack is d81 → 81 mod 7 = 4 → Fifth-day ✓ (ch15 line 225 "first light on the Fifth-day"); the quay scene is d83 → Seventh-day ✓ (ch18 line 249 "The exhibitions were on the Seventh-day"; ch19 line 343 "a little before midnight"). Two days ✓.

**Residual, not in the brief's list, same error:** ch19 line 401, unchanged from pre-repair:
> `She drank the last of her mug. "So she nodded this morning, and I nodded back. One each. That's the whole estate. Institution's bankrupt; the person gets paid."`

The nod was at the coat-rack on the Fifth-day morning, two days before this speech. The line is the cash-out of the whole coat-rack account, so the slip sits exactly where the cold reader said trust leaks. Fix 1 below. "that morning" would be ambiguous here (it could attach to the gate day she has just described), so the fix anchors it to the coat-rack instead.

ch15 line 291, as asked:
> `-He heard in it the whole of the five days on the road, and the milestone…`
> `+He heard in it the whole of the five days of the silence, and the milestone…`

The silence's count checks: begins at the milestone d77 (ch14 line 285–287); Log "on the second day of it … gone two days without one name" (ch14 lines 291–293, d78); supper at the inn "two days of nobody saying anything" (ch15 line 25, d78); "It was the fourth day of the silence" (ch15 line 201, d80); "The silence had lasted five days. It was over before her bout was called." (ch15 line 299, d81). Five ✓, two of them on the road ✓.

### Priority 3 — The Seln cutaway and the file-trade vocabulary — **RESOLVED** in every sub-item

**The reasons block (ch17 lines 93–95, was 95–111).** Seven paragraphs compressed to two; the four items each carry one concrete picture; no reason for the switch, no mechanism:
> `+He had it from four things, and he had filed none of them. There was the post locking in the east hall, with the dial sheets against his chest, and two things the boy's record said he did not own arriving inside one breath. There was Jask, a third-year, telling the refectory queue for a week that the boy was *quick off a read*; the file that came home from the guest floor with nothing written on it, and his own line under it, *unmarked file. one of three. probably the third.*; and one slip of wing paper, cut small, in a hand that was nobody's.`
> `+He laid the four beside the compiler's question mark and looked at the two roads to one word. He did not know what the boy was managing, and he had never tried to know; fifteen years of not wondering past what was in front of him had kept him employed in rooms where wondering was not safe. Something was being held, and held well. He did not reach for more.`

The removed text included the one near-mechanism description ("a move forward on the Wind, into the face of a live danger … a blow taken on a forearm that went into the forearm and did not come out") — now only "two things the boy's record said he did not own", which is observation of the record, not of the thing. "He had had the word since last year, and he had not got it from figures." kept verbatim (line 91). "*Managed?*" (line 81) and "The first time through, he read it for what it said. The second time, he read it for how it had been made." (line 67) untouched. The "fifteen years of not wondering" clause is Seln's rule, not his reason for the switch; §11's "no sentence stating his reason" holds.

**Paper paragraphs trimmed by one sentence** (the clerk's-hand sentence, old line 75, cut) ✓.

**Payment evidence held back for the table.** In-head (lines 121–123): the alehouse-fire payment paragraphs are replaced by
> `+There was also the matter of how this shop paid its readers, which a runner had let fall by the alehouse fire on the first evening, among a great deal about coal. Seln set that aside for the table. Karis Dellenmoor would ask for a reason, and it would be better to have one she had not heard.`
"Door, record, man, company" (line 107) and the stair (lines 111–119) kept. At the table (line 195) Seln now gives Karis the shop's habit as new evidence — "In advance. On paper, unsigned. Through a box near water, let by the month and given up… The man on the stair was paid through a box by the river, let for one month." — set against what she already knew from ch14 line 231 (the stair job's box by the river), and before the confirming absence. "Offices insist. Shops make do. This one made do." kept (line 199). The table scene now lands as a reveal, not a repeat.

**Net words:** ch17 prose 4,971 → 4,674 (−297), inside the brief's 250–400.

**Karis's page as inference** (lines 149–151):
> `+It was half a year old. He had kept it open in his own head the whole time, and he had no doubt it was open in Karis Dellenmoor's grey notebook too, under a heading of its own.`
> `+He found he was looking forward to watching her close it. He suspected she drew a very straight line.`
Paid at line 205, "She drew a line through the heading. It was a very straight line." ✓.

**"Shop" throughout ch17.** grep `house` in ch17 now returns only alehouse(s), "betting houses", and two academies ("a house in the valley", "other houses"). The compiler is "a commercial shop" (lines 53, 183), "where a shop showed what it thought of itself" (73), "the order of a shop" (109), "this shop" (121), "the shop's buyer" (127), "The shop builds its files… This shop has written its orders" (195), "the shop went round to the public hearing" (199). "A file is made the way a house is built" → "the way a wall is built" (99). ✓

**"The office" anchored** at its first appearance in ch17 (line 43): "in the voice of the office that had put him behind the wing's counter" ✓.

**"mispriced too" given a referent** without touching the protected line (ch19 line 445, new; 451 exact):
> `+"…They're holding him at One for reasons of their own. Same as the girl at the wool town they kept at Four. Same as my own card, come to that." He tapped the word *Copper* at the head of the tier. "Every one of us priced below what we fight like."`
> line 451 (unchanged, protected item 38): `"This one's been mispriced too. The dangerous direction."`
The author was right to keep item 38 verbatim rather than take the brief's "mispriced. The dangerous direction." variant. "The girl at the wool town they kept at Four" is M2's buried Copper R4 (ledger: her coach "keeping"; Brom wanted "somebody" to file for her) ✓.

**Audio referents.** ch15 line 143, one narrative clause between the two numbers: `+She nodded. His four were a day's price on a floor; hers were a coach's ration for a single bout, and Rooke had never changed it. "Three a bout for me, same as always…"` ✓ (per-day vs per-bout now stated). ch18 line 95: `+It was the other valley Blade, not the one Ephram had beaten, and he fought just as Rooke's sheet said he would` ✓ (ch16 line 311's Blade left distinct). ch19 line 447: "He read them as he ate" cut → `+He read the notations again from the top, slowly and completely, all the way through, and his face went still…` ✓.

**The stacked codas.** Two restating passages cut from the board scene (old lines 467 "It had cost a shoulder to make it look like that…" and 477–481, the grey-wool woman's round, "a little less tidy", "Good. That was the product working."). The board keeps the two figures, the band breathing, the standings, "Wagons." and the companions at their leaves; the quarterly follows the scene break and the movement closes on `True. Complete in form. Empty.` (line 487) ✓.

**Length:** wc 32,482, inside 31,500–34,000 ✓. **Author report:** "## Repair r1" appended with the final's touch count, before/after metrics and a changelist by chapter ✓. Only ch14–19 and the report were edited (ch14 and ch16 diffs are empty) ✓.

---

## (2) Continuity

**Calendar.** House weekdays only (ch14: Fourth-day, Fifth-day, Second-day/Sixth-day for the hill coach, Seventh-day; ch15: Third-day, Fourth-day, Fifth-day; ch18: Seventh-day; ch19: Fourth-day, Fifth-day). Every one checks against day N → (N mod 7)+1 on the author's table (d66 Fourth, d67 Fifth, d69 Seventh, d79 Third, d80 Fourth, d81 Fifth, d83 Seventh). No English weekday, season or month name anywhere in ch14–19 (grep: the only "spring"/"fall" hits are the oak's spring and "did not fall"/"let fall"); Daeva's window is not in this movement. Relative clocks all check: the audit's "Yesterday morning at first light… that afternoon… This morning the Stone declined it too" (ch18 line 225, d82 night) ✓; "more than a fortnight ago" from the costing d66 to d83 ✓; "Karis's rules had held for a whole day" (ch19 line 261) ✓; "eleven weeks" from d4 to d81 ✓. **Two count wobbles in ch17**, pre-repair text: the inn tally "five nights" (line 7) against the stay d78 dusk → d84 morning = six nights; and "It took him the first evening… What he did over the next three evenings… On the third night he read it… In the morning… the copy went back" (lines 47–135), which is four evenings against a read on night three (d80) and a return on d81 morning (the ledger's table). Fixes 2–3.

**Ratings re-summed under #38 (per-axis strike: each axis is a middle-three average, so every composite is a multiple of one third).** Cael vs the Blade 26.00 = 78/3 → 26, strong Iron/Silver-touched, "three points up" from a 23 centre ✓. Cael vs the foreman 20.33 = 61/3 → 20, Iron, "two shares were mine by plan and one was the floor's" ✓. Season 23, 22, 24, 22, 21, 23, 26, 20 matches M2's posted six ✓. Lira 26 / the boy 21 ✓; Lira 25 (final) ✓; Ephram 23 / the Stone 24 ✓; Karis 22 / the Stone 23, "Level after four, the figures decided it" ✓; Brom 23 / the southern boy 21 (above Copper's band, on M2's precedent of Copper opponents at 19–22) ✓. Formats: brackets two touches inside four (Lira's final now conforms; Karis's QF level after four; Ephram's SF 1–2 in four; Brom's final 2–1 in four); exhibitions at most five with two touches ending it (the foreman: "The fifth exchange was the last one the rules allowed. If it ended level, the figure would decide it.") ✓; the clean throw as a touch stated on the page (ch19 line 25) and the unfinished throw not flagged (line 131) ✓.

**Bursts.** Per-day budget on a floor: slate four ("Four free on this, in a day. Maybe three, if the cold gets into the hip"), with the new clause marking Lira's three as a coach's per-bout ration ✓. d83 count on the page: the Blade E3 "*One*… *Of four, on this floor*"; the foreman E2 "*Two*… *Of four*", E5 "*Three*… *Of four*"; Log "three of four on slate today, one in the morning and two for him" ✓. Documented rate kept (twenty feet; the knee burst twelve, a downward deviation).

**Bodies.** The LEFT shoulder-seam, front of the joint, by a lever (ch19 lines 109–111); Rooke "It's wrenched. The seam at the front… Four days"; Log "the lever went where levers go, into the left shoulder, at the seam"; "Pressure: untouched; the right shoulder has had a quiet week"; Lira sits "on Cael's right, the good side" and cuffs "the right shoulder, the sound one". Left and right kept distinct throughout ✓. Compression banked at contact ("He kept his thumb off the latch"), Ember none for Cael (Karis's spark at contact only), Shadow deployment none ✓.

**Year counts not incremented.** "three years" twice (Lira's protected line, line 391; Cael's Log, line 287, dated from the circuit); "half a year ago, last term" for the reader; Brom's seam "closed since last term"; Seln's "fifteen years" (accepted canon, three instances); the foreman's "twelve years"; no "four years", no "decades", no "four centuries" ✓.

**Knowledge boundaries and reserved truths.** Seln infers management from the four items only, no mechanism, no stated reason ✓; the acquisition stays off the page ✓; Karis's page is now his inference ✓. Lira never speaks the equipment mistress's name ("She—" … "She did not say it.") ✓. Hesk's history: the door line and "Ask me when the road runs home" only ✓. No one outside the circle approaches the mechanism; the Log says "the other thing" and "Reydan's gift" ✓. Tide anomaly untouched ✓. Auremont not called the banner-holder ✓. Two ledger-only notes carried from the editorial, unchanged by r1: Ephram has now heard Cael say his record is curated (ch17 line 223, "followed perhaps half of it"); "Bronze trials" (ch19 line 9) should be glossed in the ledger as a station evaluation. **One ledger line is now stale:** STATE_LEDGER line 576 (and the author's end-state, Knowledge → Auremont) says "The grey-wool woman's next edition will think him 'a little less tidy'" — that passage was cut in r1; drop the clause at close.

**Protected lines (exact; each once).** Item 34 ch15 line 69 ✓; item 37 both lines ch17 lines 183 and 223 ✓; item 38 both Lira lines ch19 lines 405/409 (with the italic *right now*) and Brom's line 451 ✓; item 61 "Thank you for the form." / "Mm." ch14 lines 189–191 ✓. The six M3 packet lines in `protected-patterns.txt` all stand whole; none is split by a tag. **No new names**: the capitalised-word inventory across ch14–19 is Cael, Brom, Rooke, Lira, Ephram, Karis, Seln, Gault, Bracken, Hesk, Vell, Jask, Reydan, Zerin, Marek, Dellenmoor, Halcenvane, Greyvane, Velmere, Ostrand, Ardenmere, Norhold, Fenmark, Auremont, Rhagen, the Compact — all canon; every new role unnamed ✓.

---

## (3) Formula (reproduced)

`python3 editions/monroe-1.3/tools/formula_metrics.py` on ch14–19:
```
words_total 32410 · prose 32410 · sentences 2325
sentence_mean 13.94 (target 14.6) · median 10 · sd 11.06
share_le5_words 0.259 · share_ge40_words 0.03
paragraph_median 28 · paragraph_mean 31.25
scene_breaks_marked 26 · per_10k 8.02 · words_per_scene 1012.8 (target 950)
flesch_reading_ease 88.8 (target 72.3) · flesch_kincaid_grade 4.34 (target 6.8)
```
(The author reported prose 32,407; I reproduce 32,410, a three-word difference, immaterial.) Per chapter (prose / mean / paragraph median / words per scene): ch14 4,966 / 13.72 / 29 / 993 · ch15 5,220 / 14.58 / 27 / 1,044 · ch16 5,036 / 14.90 / 28 / 1,007 · ch17 4,674 / 13.87 / **30** / 935 · ch18 5,383 / 13.98 / 26 / 1,077 · ch19 7,131 / 13.08 / 28 / 1,019. ch17's paragraph median is down from 31 to 30 as the brief asked; the movement median holds at 28. All primary measures inside the working ranges; FRE high as in M1–M2, reported not chased.

`bash editions/monroe-1.3/tools/ed.sh overlap book-05-the-silver-standard 3`: **0 unprotected shared runs of ≥8 words; 11 protected runs (allowed)** ✓.
`bash editions/monroe-1.3/tools/ed.sh gates book-05-the-silver-standard 3`: reader_standard=0, metadata=0, modern=0 on all six chapters ✓.
`bash editions/monroe-1.3/tools/sweep_probe.sh book-05-the-silver-standard 3 3`: ch14 0%/4% · ch15 1%/3% · ch16 0%/6% · ch17 2%/6% · ch18 1%/6% · ch19 2%/9%; **TOTAL 1,451 sentences, skeleton 1%, close 6%** (≤5% / ≤13%) ✓.

---

## (4) Reader clarity

Speaker attribution is clean in every three-plus-speaker scene (the ch14 breakfast; the ch16 file and supper; the ch17 table, every line tagged; the ch18 supper and audit; the ch19 Marek page: Ephram, Brom, Karis). The three referent wobbles the editorial located are closed by ear: a day's price against a coach's ration (ch15), "the other valley Blade" (ch18), and "slowly and completely" with no eating at midnight (ch19). The three Stones remain distinguishable in their own scenes (the reserve at home; "the home house's Stone" in the bracket; "a Stone Path, of the rooting kind" for the foreman). For the thirteen-year-old: the Seln cutaway's one dark stretch is now two paragraphs with a picture on each item, and the proof at the table is in a vocabulary ("shop") the chapter had already earned; the thing the young reader keeps ("Offices insist. Shops make do.") is sharper for it. Brom's new three sentences give "mispriced too" a referent a listener can hold ("Same as the girl at the wool town they kept at Four. Same as my own card"); the "at One / at Four" parallel keeps "Four" a rank by ear. The null report is the close. Reader Standard: no change to the clean finding; the gates confirm 0.

---

## (5) Listening proof (every chapter, every changed region)

- **Quotes:** no line in ch14–19 carries an odd count of straight double quotes; no curly quotes present. Every changed line in ch15/17/18/19 re-read: balanced.
- **Italics:** no line carries an odd asterisk count (scene-break lines excluded). The new ch17 line 93 carries three italic runs (*quick off a read*; *unmarked file. one of three. probably the third.*) each closed; the lower-case Log quotation reads by ear as a quoted line. ch19 line 445's *Copper* and line 409's *right now* closed.
- **Scene breaks:** every `---` in all six chapters has a blank line before and after (26 breaks checked by script).
- **Numerals and abbreviations:** the only digits in the movement are inside the two printed extracts (`Rank 9`, `Rank 1`), which a narrator voices as "Rank nine" / "Rank one" without ambiguity; no Mr/etc./No./initialisms. "Fourth-day", "Fifth-day" are spoken forms. "kept at Four" reads as a rank on the "holding him at One" parallel.
- **Homographs and ear collisions:** "read" past/present is unambiguous in every instance checked in the changed regions ("He read the notations again"; "quick off a read" is the noun, italicised). "Iron" tier vs Iron Skin and the Path-nouns ("the Stone", "a Blade") are the book's established usage. The one collision worth a word is in the quay speech itself and is fixed below: "this morning" against "the Fifth-day morning" four lines earlier.
- **Broken joins:** none. ch15 line 143's inserted clause sits between "She nodded." and her speech and reads as narration before dialogue, not as a split line. ch18's new paragraph boundary ("…nobody touched." / "In the fourth he came back out…") is a clean exchange boundary. ch17 lines 121–131 read continuously after the cuts ("He held the stair and the file's order in his head together… They agreed."). ch19 lines 445–451 read Brom → read-through → protected line without a gap.

---

## Line fixes (each old string verified with grep to match exactly once)

1. `manuscript/chapter-19.md`
   old: `"So she nodded this morning, and I nodded back. One each.`
   new: `"So she nodded at the coat-rack, and I nodded back. One each.`

2. `manuscript/chapter-17.md`
   old: `What he did over the next three evenings, and with whom, and at what price, nobody would ever be able to write down.`
   new: `What he did over the two evenings after that, and with whom, and at what price, nobody would ever be able to write down.`

3. `manuscript/chapter-17.md`
   old: `beds for the whole delegation, five nights, supper and breakfast,`
   new: `beds for the whole delegation, six nights, supper and breakfast,`

**Ledger notes for the coordinator at close (no prose change):** drop "The grey-wool woman's next edition will think him 'a little less tidy'" from Knowledge → Auremont (cut in r1); record that Ephram has heard Cael call his record curated (ch17 line 223); gloss "Bronze trials" as a station evaluation; the exhibition throw-as-touch rule into the #39 note as already ruled.

**Deferred, not required:** the editorial's optional Log line acknowledging Cael's own open rehearsal of the escape on the shared practice floor (ch15 lines 165–171) against the audit's finding on Ephram; and ch19 line 7's "Rooke's sheet said" for a challenger who filed the evening before. Both were left outside the brief and neither breaks anything.
