# Recheck r1 — Book 4, Movement 8 "Measured Rooms" (chapters 51–56)

Review seat: **Claude Fable, review seat** (standing in for the Sol/codex seat, which is out of quota; the recheck prompt's "Sol, via codex" should be read as me). Author of the movement and of repair r1: Claude Opus 5.5. Fresh context; I did not draft any of this. Date: 2026-10-05.

Read in full: the six current chapters (`manuscript/chapter-51.md` … `chapter-56.md`), the six frozen pre-repair files, `REPAIR-BRIEF.md`, both reviews, `AUTHOR-REPORT.md` ("## Repair r1"), `protected-patterns.txt`, `packets/MOVEMENT-008.md`, BOOK_MAP §10, the STATE_LEDGER "After Movement 7" and "After Movement 8" blocks, and the earlier chapters where a count or a date had to be sourced (ch01, ch05, ch13, ch29, ch43–44, ch46–49). Tools run myself: `formula_metrics.py`, `ed.sh overlap`, `ed.sh gates`, `sweep_probe.sh`, and `diff -U0` against `pre-repair/` for all six chapters. No manuscript or repository file was modified except this report; no git commands were run.

---

## VERDICT: CLOSE WITH LINE FIXES

Scope: **two one-string fixes**, both in the Log or the slate, neither touching a fight, a protected line or a scene.

1. ch55 Log, "it never went" — the brief's own suggested wording, applied exactly, but in this movement "it goes" is the fixed idiom for the corner drifting ("Say it if it goes" / "I said it." fifty lines above), so the entry now denies in its ninth line what it logs in its third. One phrase.
2. ch53, the chalked `*11/11*` — the one bare numeral in the movement that a narrator will misvoice. One phrase.

Everything the brief asked for is on the page, and the repair introduced no regression I could find. Every rejoined packet line is whole and pattern-protected; the six trials count to six; the correction precedes the audible release; the homecoming happens once; the counts are true; the canon and protected elevens stand; "decision point" is used once; Shadow has zero deployment; the formula is inside range and matches the author's after-table to the decimal.

Two cross-movement flags for the coordinator (section 2, not M8 fixes): ch13's "the second of the four weights" against the now-accepted weights numbered one to five; and the baseline called "the first month" in M8 while closed ch48 has Cael call it "the second month" (closed ch49 has Gault say "first month", so M8 follows Gault; inherited, no M8 action).

---

## (1) Brief items

Evidence is quoted from `diff -U0 pre-repair/chapter-NN.md manuscript/chapter-NN.md` (`-` pre-repair, `+` current) or from the current text with line numbers.

### Coordinator rulings

**Ruling 1 — the five tag-split packet lines, rejoined whole.** RESOLVED.
- ch54:217 `-"That is a better instrument reading," he said, "than the Greyvane exhibit supports.` → `+"That is a better instrument reading than the Greyvane exhibit supports," he said.`
- ch54:247 `-"Magister," he said. "I need an interval."` → `+He said, "Magister. I need an interval."`
- ch55:67 `-That," said Gault, "is what a real semester looks like."` → `+That is what a real semester looks like," said Gault.`
- ch56:249 `-in a cage built for people," he said, "who did not exist.` → `+in a cage built for people who did not exist.`
- ch56:307 `-"That is the most competent half-hour," said Gault, "that I have sat through in eleven years. I did not," he said, "say one word in it."` → `+Gault said, "That is the most competent half-hour I have sat through in eleven years, and I did not say one word in it."` — the double-tagged line the editorial heard is gone; one tag, in front.
- All five match `protected-patterns.txt` (I grepped each pattern against the current text; four match as 8+-word runs, and "Magister. I need an interval." is five words, below the overlap gate, so it cannot form a run — which is why the protected count rose 9 → 13, not 14). The tag is before or after each line, never inside.

**Rulings 2–5 (reworded packet lines, the even first exchange, trial 5 / weights 1–5, small canon).** Stand; nothing in r1 touched them. The six-count condition on ruling 4 is met (P2.1 below).

**Ruling 6 — "Third one someday" twice; the floor line must land as the original.** RESOLVED.
- ch52:383 (the eighth bell, the floor) is byte-identical to pre-repair: `"Third one someday," he said.`
- ch53:41 `-"Third one someday."` → `+"What I said on the floor still stands," he said. "Third one someday."`; ch53:43 `-"You said that on the floor."` → `+"You said it once. Once was plenty."`; ch53:45 unchanged, "I'm saying it again so it's written down somewhere." The repetition is now unmistakably Brom echoing the floor, and Lira's "Once was plenty" gives the floor line its weight back.

### Priority 1 — the doubled homecoming (ch55). RESOLVED.

One arrival now. The sequence on the page (ch55:235–257): the quadrangle → the stair → Brom on the landing with the ice → Karis in the common room, book shut, "Well?" → `+He told her, and at *renewed* her eyes closed for a moment` (ch55:241; *renewed* is heard by Karis exactly once) → the coach-accident tableau → the counted joke → "I can carry a tray" / "You can't carry a tune" → `+Karis turned to Cael on the settle. "And the glass? The thread in the straw. You said you'd tell me what it did."` (ch55:251; "the column" is gone and the glass is glossed) → the third word written under *a spark* and *a letting-go*, the short line under all three, "That's the last one. I can feel that it is." (ch55:255–257, unchanged) → Bracken's half-sheet.
- The second opening is cut: `-In the common room Karis sat with a book on her knee, open at the page it had shown since the second bell. She shut it.` / `-"Well?"` / `-"And the column?" she said, opening them.` all removed.
- The joke now counts: `-"Between you, you have four working legs and three working arms."` → `+"A champion, a finalist and a renewed enrollee," she said, and counted on her fingers. "Between the three of you, three working legs and four working arms."` Check against the page: Lira one leg, two arms; Brom one leg (iced knee), one arm (strapped hand); Cael one leg (hip), one arm (shoulder) → 3 legs, 4 arms. Correct.
- The walk home: `-two people with one good leg between them` → `+two people with two good legs between them, one each` — true of Lira and Cael.
- Kept: the stair, Brom's ice, the tableau, the tune exchange, the grey notebook paragraph intact.

### Priority 2 — make the numbers true

**P2.1 The six trials count to six (ch53–55).** RESOLVED. ch53:79 `+…which leaves the second slot empty, and the posted sheet says so in so many words: *Two, at the enrollee's placing.* Anything already on your record that you choose to show goes there, or nowhere." She chalked a short dash beside the figure two.` The posted order is now, on the page: 1 board; 2 at the enrollee's placing; 3 read and move together (read carried); 4 plate; 5 new; 6 the cold run (board and read). ch54:113 "Second, then. The six stand as posted otherwise, with the read carried in the third and the last" now refers to something shown; ch55 runs "Third trial" (l.5), "Fourth trial" (l.63), "The fifth trial" (l.81), "Last came the cold run: the board, then the read" (l.171). Six. The slate's `*5.`/`*Hold going past thin*` lines and ch53:269 "the placing was his" already agreed with it.

**P2.2 Gault's "Five of six have moved" (ch55).** RESOLVED. ch55:67 `-This wing measures six things. Five of them have moved and one hasn't.` → `+So far this morning I've measured four things, and one of them hasn't moved.` At that point four trials have run (board up; vessel better than the Greyvane exhibit; combined 11/12 at weight four over 7/8 at three; plate flat). True when said. The end-of-sitting arithmetic stays where it is already true: the note (ch55:177–185), Lira's recap "Growth confirmed in five" (ch55:227), the Log "five up, one level" (ch55:273).

**P2.3 11/12 called "the floor".** RESOLVED. ch55:29 `-sitting on the floor of them as near as made no difference, which was exactly where it was supposed to sit.` → `+a call above the floor of them, which was exactly where a term should put it.` Karis's floor is "weight four with you clear at least five times in six" (ch53:91) = 10/12; Cael's plan was "Right on the floor of it" (ch53:161); 11/12 is one call above. Consistent.

**P2.4 The protected M9 line (ch55 four pieces).** RESOLVED. The order is now: `+The first was his forearms. The weight was already moving before anything in the room had made a sound.` (l.93) → `+The second was the answer, which was already in his legs.` (l.95) → `+The third was a pair of shoes.` (l.97) → "He did not finish the burst… He shut it." (l.99–101) → `+Only then came the fourth piece, which was a sound. It reached him after he had already shut the door: a small dry catch and drag… and then the late clack of a release… it had let the weight go before it made its proper noise.` (l.103). Cael's correction (the burst shut) precedes the audible release, so BOOK_MAP §10's *Frame fault, trial five. Correction preceded the audible release.* is true on the page it describes. The Mire instructor's "It's failed outright. Early, and off the upper rack" (l.111) and Gault's "Frame fault at the second notch, releasing early and high" (l.141) agree with a notch that let go before it sounded. The added `+and the order of them turned out to matter` (l.91) is a fair signpost. "He did not finish the burst.", "Enrollee. Are you hurt?" through "Because the clerk was standing where I'd have landed." are unchanged.

**P2.5 The glance tally (ch55).** RESOLVED. `-seven people in that room had needed the second look` → `+six people` (l.159); Log `-*Seven people needed a second look at me.` → `+*Six people` (l.287). The list at l.151 names Gault, the Mire instructor, the Ash instructor, the counsel, Havel, Ilsev: six. The clerk is accounted for separately at l.137 (dust, shoes, page). The tally reads six and claims six.

**P2.6 ch55 Log, "it never flickered".** PARTIAL — applied exactly as the brief suggested, but the suggested word is the wrong one for this movement, and I propose a one-phrase fix (fix 1).
- Diff: `-and it never flickered.` → `+and it never went.` (l.279).
- The problem: in ch53–55 "it goes" is the established idiom for the corner slipping, i.e. for a drift — ch53:201 "It never goes while I'm working… Leave me standing with nothing asked of me, and it goes."; ch54:59 "And if the corner goes?"; ch54:63 and ch55:229 "Say it if it goes."; ch55:231 "I said it." (meaning: it went, at the hour and a half, and he said so). The same Log entry opens "Drifts: two" and describes both (l.269). So "it never went" is now a flat contradiction in the book's own words — the same fault as "it never flickered", moved one word along. The brief wanted "something two logged drifts allow"; what two drifts allow is a statement about deployment, not about the corner. The entry itself supplies the word two lines above: "Q.'s question… could I keep it in" (l.275). Fix 1 makes l.279 "and it stayed in." — zero deployment, two drifts allowed, and it answers Quenna's question in her own verb.

**P2.7 Brom's clock (ch51–52).** RESOLVED, as per exchange. ch51:259 `-both had started the moment the two of them walked out.` → `+they did not run the same way.`; ch51:261 `+four minutes, near enough, of hard contact inside a single exchange. The turn of the glass between exchanges gave some of it back, and never all.`; ch51:265 `+and nothing gave any of it back: three bursts`; ch51:325 `-His four minutes had begun.` → `+His clock had started. It would start again with every exchange, a little shorter each time.`; ch52:145 `-four minutes of iron and eleven seconds more had put his turn on the fifth count` → `+The third exchange had held him on the iron for four minutes and eleven seconds, and the turn of the glass had not given that back; eleven seconds into the fourth, his turn came on the fifth count instead of the fourth, a hair late.` Lira's POV line (ch51:65, "Somewhere past four minutes of hard contact") is agnostic and still true. The exchange-3 slowing "with the glass more than half gone" (ch52:95) fits a clock that restarts "a little shorter each time". The STATE_LEDGER ruling (PER EXCHANGE) matches. One small note for the author's report only: it says he "slows at four minutes into that exchange"; the page says past the half-glass, which is the better reading and needs no change.

**P2.8 Brom's strapped hand.** RESOLVED. ch53:231 `+with the ice in his hand and his right knuckles strapped to the second joint in Karis's clean linen; they had taken Lira's forearms all afternoon and the hall-rules book all evening, and at last they had split.` Precedes ch54:3 ("strapped to the second knuckle in clean linen"). "Second joint" / "second knuckle" are the same place; fine by ear.

**P2.9 "Weeks ago".** RESOLVED. ch53:201 `-"Weeks ago, in hall three, Brom found it,"` → `+"Eight days ago, in hall three, Brom found it,"`. Sourced: the M6 ledger puts the hall-three slip Brom's read caught at d175 (the eleventh); calibration night is d183 (the nineteenth); eight days. The lesson "busy is the safest thing" (gaps, not work) was learned at the d179 sitting (ch48:263), and ch53 is him joining the two; consistent.

**P2.10 The incidental elevens.** RESOLVED. The author's list matches the diff exactly:
- ch51:277 seam-hunters `-eleven of them` → `+nine of them`;
- ch52:69 `-eleven pages of it` → `+nine pages of it`;
- ch55:95 `-He had given it eleven times that morning` → `+a score of times` (8 board runs + 12 combined = 20: true);
- ch56:57 `-Three mentions in eleven years of print` → `+ten years and more of print`.
Kept, and I checked each against its source: Lira's eleven bouts (ch52:193; 9 + semifinal + final); "eleven of twelve" and the baseline's "Eleven calls in twelve" (ch55:27, ch53:85; ch13:95 "Eleven of twelve"); the eleven drifts / Lira's eleven marks (ch53; the packet's count); "eleven questions" and "subsection eleven" (ch56; packet and §10); Gault's "in eleven years" (protected); Ilsev's form "in eleven minutes" (ch52:33; the M7 ruling's eleven-minute referral); carrel eleven (ch56:57; canon since ch05:243 and used in ch06, ch07, ch12); Karis's "eleven weeks" (ch56:139; canon since ch01:195, ch02); "Lira has done it eleven times" (packet); 4:11 and the eleven-second fourth (packet); the porters' eleven minutes (ch55:145, 155; the packet's "eleven minutes on the rail"). The brief listed carrels and Karis's weeks among candidates to vary, but they are earlier-book canon, and the author was right to leave them.

**P2.11 Speakers.** RESOLVED. ch51:365 `-"Two gone."` → `+"Two gone," Cael said.`; ch53:147 `-The nearest chair-back took his grip.` → `+Cael took hold of the nearest chair-back.`

### Priority 3 — rhythm: none required. RESOLVED (no rhythm work done; mean 13.21 → 13.26 from the rejoins alone).

### Length. RESOLVED. `formula_metrics.py`: 30,607 prose words (brief: 29,500–31,500).

### After the repair. RESOLVED. All four runs reproduced by me (section 3). AUTHOR-REPORT.md has "## Repair r1" with the elevens, the clock decision, before/after metrics and a changelist by chapter; every entry in the changelist corresponds to a hunk in the diff, and there are no hunks the changelist omits. Only ch51–56 and the report were edited (the diff touches nothing else; the pre-repair files are unchanged).

---

## (2) Continuity

- **Calendar.** Final the nineteenth (ch52:193), evaluation the twentieth (ch55:265), interview the twenty-first ("Fourth bell today", ch56:19, the day after). Ledger day 21 / day 22 and "thirty-five days since the stair" (ch54:13) follow M7's "day sixteen; twenty-nine since the stair" on the 14th. "Ten days" for the hip (ch51:9; semifinal the ninth). "Nine days" of no sparring (ch51:57). "Eight days ago" (above). "Fourth-days" (ch55:67) is the book's scheme; the 19th is a Fourth-day by the d176 anchor and "they were looked at yesterday" is right for the 20th. No English weekday names, no "weekend", no month order (grep clean).
- **Lira's record.** "Ten bouts unbeaten. None lost." certified at the first bell, then the final written at the foot in public and "Eleven bouts unbeaten. None lost." (ch52:189, 193). 9 (ch29:249 "Nine and nothing") + semifinal + final = 11. Unchanged by r1; verified.
- **The final.** Even on the guard / Iron Skin / Wind / Wind → "Two touches to one. The bout." Unchanged.
- **Protected lines (BOOK_MAP §10).** The diff touches none of them: the slip (ch53:239), the note's four lines (ch55:179–185), subsection eleven and "twelve feet by fourteen" (ch56:7, 19), "Two years I've been trying to solve you." / "And?" / "Third one someday." (ch52:377–383), "She held it like an exhibit." (ch52:357), "Like somebody with something in his pocket." (ch53:73), "Be the fighter. In a measured room. Both." (ch53:227), "He doesn't wish me harm. He wishes me *measured*." … "Sleep. Fight in the morning." (ch53:301–305), "Because the clerk was standing where I'd have landed." (ch55:133), "That is what the provision is for." (ch54:157), the interview exchange and the keynote with its em dash (ch56:173–287), "I'm going to stop calling it a habit." (ch55:281). The M9 dependency ("Correction preceded the audible release") now holds (P2.4). The five M8 packet lines are whole and pattern-protected (Ruling 1).
- **"Decision point."** Exactly one hit across the six chapters: ch54:209, as Ember's third word. Karis writes "the third" without the phrase (ch55:253–255).
- **Shadow-adjacent.** Zero deployment. The only "shadow" in the movement is the literal one on the Archmarshal's face (ch56:111, lower case). Two drifts on the 20th, both lapses of the hold inside the plan; the quarter-burst is "one point isn't a line" (ch55:283). The Log's "it never went" is the one phrase that mis-states this (fix 1).
- **Knowledge boundaries.** Lira's POV (ch51) predates the slip and she is asleep when it burns (ch53:231). Havel does not wonder about the notebook (ch51:191). Ilsev reaches no conclusion ("She marked the thought and went no further with it", ch52:47; "a proper errand", ch52:333). Vastin unnamed, unaged, unwarning; notebook lines unseen; Cael's tally "Two" (ch55:201). Seln, Gwen, Abbot: no hits in ch51–56. Bracken is "he".
- **Bodies.** Lira's hip (four days, stick), Brom's knee and knuckles (now sourced), Cael's hip (three days), shoulder ("to the week's end"), forearm numb, the headache: unchanged and consistent with the ledger.
- **Reserved truths.** Tide anomaly, [UNBOUND], the Architect, the Quieting, Seln's switch: untouched (grep clean).
- **The slate and Gault's "Where would you like it?" (ch53:79 / ch54:109).** Now that the sheet says *Two, at the enrollee's placing*, Gault's question has one answer on the sheet; but "at the enrollee's placing" also reads as "placed where the enrollee says", ch53:269 already had "the placing was his", and Cael gives a reason ("It's done by touch, and I'd like the arm unspent"). It coheres; no change.
- **Cross-movement flag A (coordinator's call; outside M8).** ch13:53 (M2, recheck pending): "racked the second of the four weights". M8 now states, with the coordinator's acceptance, that "the wing numbers its weights one to five" (ch53:91) and runs "The heaviest weight, the fifth" (ch55:35, 87). ch13's "four" contradicts the accepted five. The clean fix is in ch13, not here: `the second of the four weights` → `the second of the five weights` (one word; ch13's read-only trial at weight two is unaffected). I have not listed it among the M8 fixes.
- **Cross-movement flag B (inherited; no M8 action).** M8 calls the baseline "the first month" seventeen times (ch54, ch55). The M2 ledger puts the baseline at day 48. Closed ch48:55 has Cael think "his baseline in the second month"; closed ch49:195 has Gault say "at this enrollee's baseline, in his first month". M8 follows Gault's own phrase; the wobble is already inside closed canon, and I would not reopen it from M8. Reported for the owner's C3-style ruling.

---

## (3) Formula

Reproduced by me on the current chapters (`python3 editions/monroe-1.3/tools/formula_metrics.py manuscript/chapter-5{1..6}.md`):

```
words_total 30607 · prose 30607 · sentences 2308
sentence_mean 13.26 (target 14.6) · median 10.0 · sd 10.75
share_le5_words 0.273 · share_ge40_words 0.034
paragraph_median 25 · paragraph_mean 32.53
scene_breaks_marked 28 · per_10k 9.15 · words_per_scene 900.2 (target 950)
flesch_reading_ease 88.1 · flesch_kincaid_grade 4.27
```

| Measure | Pre-r1 | After r1 (mine) | Author's after | Range |
|---|---|---|---|---|
| Words (prose) | 30,404 | 30,607 | 30,607 | 29,500–31,500 ✓ |
| Sentence mean | 13.21 | 13.26 | 13.26 | 13–15.5 ✓ |
| ≥40-word share | 3.2% | 3.4% | 3.4% | 2.5–4.5% (≤4.0) ✓ |
| ≤5-word share | 27.3% | 27.3% | 27.3% | ≤ ~34% ✓ |
| Paragraph median | 25 | 25 | 25 | ≤ ~30 ✓ |
| Words per scene | 894 | 900 | 900 | 850–1,050 ✓ |
| FK grade | 4.25 | 4.27 | 4.27 | 3.5–6 ✓ |

The author's after-table is reproduced exactly.

- `ed.sh overlap book-04-copper-crown 8`: **0 unprotected shared runs of ≥8 words; 13 protected runs (allowed).** Pre-repair was 9 protected. 9 + 4 = 13: the four rejoined lines long enough to form an 8-word run (vessel, semester, half-hour, cage) now match `protected-patterns.txt`; "Magister. I need an interval." is five words and sits under the gate. The tool does not list protected runs, so the arithmetic is my check on the count. The `source-overlap.tsv` in `state/` is the pre-repair file (0 lines = 0 unprotected then, too).
- `ed.sh gates book-04-copper-crown 8`: reader_standard=0, metadata=0, modern=0 on all six chapters.
- `sweep_probe.sh book-04-copper-crown 8 8`: TOTAL 1,356 sentences, **skeleton 2%, close 7%** (brief: ≤5% / ≤13%). By chapter: ch51 0/4 · ch52 2/9 · ch53 1/3 · ch54 1/8 · ch55 3/11 · ch56 3/7. Matches the author's report.

---

## (4) Reader clarity

- **Speaker attribution.** Every turn in the evaluation and the interview is named. The two cold-read stumbles are fixed ("Two gone," Cael said; "Cael took hold of the nearest chair-back"). The merged homecoming keeps every speaker clear: Karis "Well?", Brom "I can carry a tray", Lira "You can't carry a tune", Karis to Cael on the settle. The Archmarshal's unattributed lines in ch56 remain unambiguous in a five-chair room.
- **Referents.** "The glass? The thread in the straw" glosses the vessel for a listener. "It" in the ch55 Log is the one weak referent (fix 1 also removes the second "went" in that entry, so the notch's "went" at (b) no longer collides with the corner's).
- **The thirteen-year-old lens.** The six slots are now countable on the fingers (the slate names slot two and chalks a dash beside it); Gault's "four things" matches the trials she has watched; the joke counts; the Ember payoff arrives in one scene. The brackets in ch53 remain the chapter's densest stretch, as both reviews said, and were not in the brief.
- **Reader Standard.** Gates 0/0/0. No oath, no gore, nobody cruel, no romance. Unchanged.

---

## (5) Listening proof

Checked on every chapter, with the changed regions read twice: quote balance per paragraph (straight and curly), italic asterisks per paragraph, `---` with a blank line before and after, bare digits and abbreviations, homographs, joins at every hunk.

- **ch51.** Quotes and italics balanced. 5 scene breaks, all spaced. No digits. The clock paragraphs (l.259–267) read cleanly aloud; "they did not run the same way" sets up both clocks. "Two gone," Cael said / "How much does she have?" now lands with the speakers audible. Joins clean.
- **ch52.** Balanced. 6 breaks, spaced. No digits ("four minutes and eleven seconds" is in words). l.145 carries "eleven seconds" twice in one sentence, which is the packet's two figures (4:11 and the eleven-second exchange) and reads as intended; no change.
- **ch53.** Balanced (the slate's italics close). 5 breaks, spaced. Two bare numerals: `*5. No rehearsal…*` (l.167; a narrator says "five", fine) and `*11/11*` (l.197), which a narrator will voice as "eleven eleven" or a date. **Fix 2.** The new slate sentence (l.79) is long but has its commas in the right places for breath; "*Two, at the enrollee's placing.*" is set off. The knuckles clause (l.231): "they" attaches to the knuckles, the nearest plural; clean on a second hearing. "Eight days ago" is plain.
- **ch54.** Balanced. 4 breaks, spaced. No digits. The two rejoined lines read as one breath each: "…than the Greyvane exhibit supports," he said. / He said, "Magister. I need an interval."
- **ch55.** The note (l.177–185) is a multi-paragraph speech with open quotes on each paragraph and one close on the last; correct convention, verified. 4 breaks, spaced. No digits. The four pieces (l.93–103) read in order and the "Only then came the fourth piece" join is audible as a hinge. The merged homecoming (l.235–257) has no restart; "Well?" occurs once in the room (and once at the gate, to Lira, which is a different "Well?" and a different voice). "Fourth-days" voices cleanly. The Log: "went" at (b) for the notch and "went" at l.279 for the hold is the one ear collision in the movement — fix 1 removes it.
- **ch56.** The three odd-quote paragraphs (l.69, 85, 285) are continuing speech into the next paragraph (l.71, 87, 287); correct and verified. 4 breaks, spaced. No digits. l.307 is now a single tag before a single sentence. "a face set in shadow" (l.111) is the literal word; no collision with the Path name for a listener.

---

## Line fixes

1. `manuscript/chapter-55.md`
   old: `and it never went.`
   new: `and it stayed in.`

2. `manuscript/chapter-53.md`
   old: `*11/11*`
   new: `*eleven of eleven*`

Each old string was verified with `grep -c -F` to match exactly once in its file.

Cross-movement suggestion, **not** an M8 fix, for the coordinator to apply at M2's recheck if the weights-one-to-five ruling stands: `manuscript/chapter-13.md` old `the second of the four weights` → new `the second of the five weights` (verified once in ch13).
