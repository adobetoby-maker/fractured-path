CLOSE WITH LINE FIXES — scope: Book 2, Movement 8 repair r1, chapters 52–60, plus the two authorised side-words in closed Movement 7 (ch47, ch51). Every repair-brief item and every OWNER-DECISIONS #36 ruling is resolved on the page; continuity, protected wording, reserved truths, Reader Standard, source distance, formula ranges, the Book 3 hand-off and all required automated checks pass. Apply the six line fixes at the end (one continuity residual the shoulder re-siding left behind in the ch55 anomaly entry; one say-it-once trim in ch60; two scene-separator spacings; two cosmetic italics), record the two coordinator notes in (2), then close the movement and the book. No second author repair is warranted.

# Targeted recheck — repair r1 (Book 2's final movement)

Review seat: Claude Fable, review seat (standing in for the Sol/Codex seat, which is out of quota; where the prepared prompt says "Sol, via codex", read Claude Fable, review seat). Author: Claude Opus 5.5. Fresh context; not the author. This is an informed targeted recheck of a same-author repair, not a cold read or an audience test. I read the full current movement in chapter order; diffed all nine chapters against `state/movement-008/pre-repair/` and all eight M7 chapters against `state/movement-007/pre-repair/` with `diff -U0`; and checked the text against REPAIR-BRIEF.md, both reviews, AUTHOR-REPORT.md "## Repair r1", OWNER-DECISIONS #36 (and its update), BOOK_MAP.md (§1, §7, §8, §11), STATE_LEDGER.md (entry state and the After Movement 7 block), packets/MOVEMENT-008.md, the M7 close records (AUTHOR-REPORT "Repair r1", recheck-r1.md), and the closed edition Book 3 chapter 1 in full. No manuscript or repository file other than this report was written; no git commands were run.

---

## (1) Brief items

### Coordinator rulings (OWNER-DECISIONS #36) — all RESOLVED

**Ruling 1 — the redirect shoulder is the RIGHT. RESOLVED.**

*Closed M7, only the authorised side-words.* The M7 `pre-repair/` snapshot is the pre-M7-r1 text, so the `diff -U0` across ch44–51 also shows M7's own r1 edits. I classified every hunk against the M7 AUTHOR-REPORT "Repair r1" changelist and the M7 recheck's quoted examples (ordinals tagged with weekdays; the ch45 notebook/supper compressions; the ch47 tally-gloss cuts and two paragraph splits; the ch48 report compression; the ~sixty narration joins; the ch51 closing quote, `*ands*`, inventory compression; the ch45 blank-line insertion at 201/196, which is the spacing fix applied at M7 close). Every hunk maps to one of those, except exactly two:

- ch47:117 — pre-repair `turned his left shoulder to it and let it in` → current `turned his right shoulder to it and let it in`.
- ch51:159 — pre-repair `he sat favouring his left shoulder by a hair` → current `he sat favouring his right shoulder by a hair`.

File mtimes corroborate: ch47 and ch51 both carry 08:57:28 (the M8 repair's single pass); ch44/46/48/49/50 carry 07:56–07:57 (M7 r1); ch45 carries 08:18 (the close spacing fix). `grep -i "left shoulder|left arm|groove"` across ch44–51 now returns no "left shoulder" at all; the groove lines (ch48:105, :117; ch50:77, :79, :105; ch51:21, :201) name no side; ch48:131 and ch50:61 mention the right shoulder only as where Lira's staff and Brom's forearm land, which now reads even better against Reydan's "somebody had been hitting him there all fortnight". `ed.sh overlap book-02-iron-circuit 7`: **0 unprotected, 5 protected** (reproduced). The M7 side-word change was surgical.

*M8, every body-state line re-sided.* Evidence from `diff -U0`:
- ch52:195 (Lira's cutaway, redirect one): `turned his left shoulder` → `turned his right shoulder`; the crookedness is now motivated by "his legs not yet all the way back from the stone" and "the hip catch on it, the way it caught in the alcove when he was tired". The forearm hit stays left (ch52:123–131 unchanged).
- ch53:5: `the left shoulder ringing… the count had been made for a whole arm. He had half an arm now` → `the right shoulder ringing… made for a body that had not just been put on the floor`.
- ch53:142 (redirect two): `To turn his left shoulder to it he had to turn half his back` → `For once the bursts were coming at the side he had drilled. He had only to plant and turn the right shoulder a little further into the beat`. The cost line now runs "from the top of the right arm to the breastbone, on top of the bill from the rope".
- ch53:146–150 (redirect three): `There was the right. / He had never drilled it…` → `There was the last one. / One left, by the count, in a shoulder already burning…`.
- ch53:160 (the completion): `the way the left had passed… It was the wrong side and a line he had never learned` → `the way the shoulder had passed… The joint was spent and the line was going ragged`.
- ch53:206, :210, :212 (the aftermath count): the groove "three redirects deep" and "the joint under the groove" replace "the groove in the left" / "two redirects deep" / "the right shoulder".
- ch54:119: `the left shoulder full, and the right shoulder turning` → `the shoulder full, and the last one turning`.
- ch55:63 (the Log): `Redirects: three, all the right shoulder, the drilled side…`; :71 cost line now "the groove, three deep… and under the groove, in the joint, a hollow"; :79 "for a body that hadn't been on the stone yet"; :135 Brom's dawn read "Under the groove… The groove's loud, all three of them… But under it, in the joint, it's quiet."
- ch58:11: the groove from the three redirects eases "the way it always did"; the joint under it is "simply quiet".
- ch60:213 Log: `Cost: right shoulder and breastbone`.
- **Counts kept exact:** ch55 Log 14 knocked / 12 answered / 2 smeared; Wind 6 all left; giving face 3; redirects 3; the ch53 per-exchange arithmetic still reconciles (5/4, 4/3, 3/3, 2/2).

**One residual the re-siding missed** (not in the author's changelist, unchanged from pre-repair): ch55:105, the half-second anomaly entry, still reads `A redirect on the right shoulder (never drilled) that stopped passing the burst` — which now contradicts ch55:63 ("all the right shoulder, the drilled side") forty lines above it and ch53:142. Line fix 1.

**Ruling 2 — track name. RESOLVED.** ch57:153, once, one clause: "The demonstration-provision track, or the observer track, as they'll have it on the gate list, because that is what the clerks have always called it." B3 ch1:296 ("And Cael, on the observer track") now lands as a name the reader has heard.

**Ruling 3 — season. RESOLVED.** ch57:161: `before the first snow on the hill road… after the first snow` → `before the weather turns on the hill road… once it has`. ch58:240 `a frost so hard the cobbles rang` → `a cold so raw the cobbles sweated with it`. ch59:29 `the frost going off the cobbles` → `the wet drying off the cobbles`; ch59:199 `the street was white with frost` → `the cobbles were wet and black under the lamp`. ch60:5 `in the frost` → `in the raw cold before light`; :7 `sweeping the frost off her step` → `sweeping last night's wet`; :47 `breath going up in the frost` → `going up white in the cold`; :177 `in a frozen yard` → `in a cold yard`; :197 `bite down on something cold` → `drink too fast from a spring`. A word-grep of ch57–60 for frost / snow / frozen / ice finds nothing on the departure days or the road. The remaining season words are all memories or earlier canon ("a winter and a half ago", "since the autumn", "since the spring", "in a frozen yard" at ch58:67 — Book 1's winter yard, a recollection on the Ulric night; see note (ii) in (2)).

**Ruling 4 — exchange and notice. RESOLVED.** Compression completes in the fourth exchange (ch53:118–196); he decides only to go in ("He did not reach for the thing in his shoulder… He only went in", ch53:174); the notice arrives at the desk after the Wind-only Ulric bout (ch58:133–144). Nothing touched on the Book 3 side (B3 ch1 read in full; identical in substance to what the reviews quote).

**Ruling 5 — Log format. RESOLVED / ACCEPTED.** ch58:178–190 rules the Compression entry under Function / Benefit / Cost / Integration and has Cael mean "to bring the other three over to match it on the road, where there would be time"; B3 ch1's "every section used the same four headings" is reachable in two road days.

### Priority 1 — ch60 roadside tests re-imaged against B3 ch1 — RESOLVED

Every beat and result is kept, in order: inert, with the cat "that has heard its name and decided not to know it" (ch60:175–177); the piece sent into the left knee (:181); early reaches that get nothing (:189, now three, "like calling a dog that is still on the far side of the field"); the waited-for try — now the sixth — "let Brom's lean come right in… told it where. *Back. Out the way you came.*" (:189); "Some of it went" (:191); the cost in the right shoulder, breastbone and teeth (:197); twice more, one quarter, one nothing (:209); the Log line and "*Exactly like Wind at the start.*" (:213–215). The shared figures are all gone: the hot iron bar and the two-breaths run (now "a young horse had kicked him in the middle of the chest… stood there with its hoof on him" and "little sips of air"); "like a door shutting in another room" (now "a short dull thump like a fist on a table in the next house"); "a weight a man could count" (now "the way a man leans on a gate to see if the post will hold"); "like a flat stone" (now "something more like the end of a beam"); "Quarter." / "Quarter." (now "Did that come back at me?" / "Some." / "How much?" / "…A quarter, maybe. Of a tenth." / "Then I'll call it a quarter… and you can argue with me when you can breathe."); "a road of its own… he chose one for it" (now "before it could go looking for his knee again, he told it where"). The day-one language is rawer than B3's settled vocabulary ("go after it" / "bunched up" / "swung round" / "paid for it"), so B3's "That was the first thing the road had taught him" now reads as three days' maturing. Moving the success from the seventh try to the sixth is within the brief (the seventh was on the shared-figure list; the beat, not the ordinal, was protected).

**The brief's 8-gram script, reproduced:** `0` shared 8-word runs between ch60 and B3 ch1. I also ran it at 7 words (0) and 6 words (1: "on the far side of the", stock). Scene length is held (ch60 5,021 words; the test scene is the same length within a few lines).

### Priority 2 — consistency and protected lines — RESOLVED

- **ch59 Ansel:** `nineteen that year and so had I` → `nineteen that year, and I'd been twenty-four` (ch59:139), matching closed ch46 ("Nineteen. I was twenty-four.").
- **ch56 Quenna:** `Eight bouts on the main floor, seven won… His win over you` → `Nine bouts in your keeper's book, eight won. The one he lost, his first. The ninth, his win over you. A season of floors before any of that, up the river` (ch56:125). Checked against closed ch17:97 ("Eight bouts and seven wins") and :139 ("One loss, first bout, the Shield… Then seven wins") and the M3/M4 ledger blocks ("eight bouts, seven wins; his only loss was his first, to the Shield"); the Cael bout (M4, Brom's win) is the ninth; the ledger shows no later Brom bout. "Main floor" is gone.
- **ch60 protected lines restored whole** (ch60:221–233): `They had gone a long way without talking when Cael said it, to the road ahead as much as to either of them.` / `"I have four things that aren't a Path and two people who know about it. This might be enough."` / `Brom answered first, from the outside.` / `"It's a start."` / `Then Lira, from the inside, without looking round.` / `"It's more than we had when we got here."` / `"Yes," said Cael.` — every sentence of §8 item 17 whole and terminal-period exact; attribution before each line, so the three-speaker close still names its speakers for audio.
- **Hesk's timing:** ch57:21 the letter goes by "the up-country night coach, which changed horses at every stage and did not stop to sleep"; ch57:31 `Two each way, three if the roads are bad` → `A day and a half each way, by the night coach. Longer if the roads are bad.` Posted Thursday morning → Denvash Friday night → Hesk writes → second post Sunday (ch57:85). Tight, and it now works.
- **Dace's "a month" vs Quenna's six nights:** ch57:49 `honoured it on faith for a month` → `let her in on it blind the night before and taken her coppers at the door four times before that` = 1 + 1 + 4 = six nights, matching ch54:170 and the M7 ledger (first credentialed pass honoured on the Monday card).
- **"He never would":** ch60:107 now `He did not know which, and Dace would never tell him; Dace kept a promise the way Vell kept a line. He was as sure of it as he was of anything. He didn't know the man's name. He never would.` — Cael's certainty, with the two protected sentences exact and untagged after it.
- **ch58 day order:** scene 1 now runs hill's news → the mending week Wednesday/Saturday/Sunday/Monday → Brom's Monday read → Ulric watched "That day" → Tuesday's read and the arm's limit → "Quenna took the coach that morning… By the evening the hill had already begun to behave as if she had never been there." Chronological; the Monday no longer precedes a Tuesday that has already happened.

### Priority 3 — say it once; clarity at the notice — RESOLVED (one trim offered)

- **ch60 duplicate nod:** Cael-side nod-and-carter paragraph (pre-repair :85–87) cut; replaced by one registering sentence in the pluperfect (:79) that keeps "*Find me later…*" and the ledger of things owed (:81–83). Reydan's side (:39–43) stands in full, including his reason for not asking twice (:31).
- **Session nine after ch55:** ch58:174 is now one short paragraph ("It said *force absorption*, and in session nine nothing had been absorbed… Whatever session nine had been, it was not this.") followed by "One anomaly. Still one." — the one restatement the brief allows. ch59:183–191 is leaf housekeeping without re-proving (and keeps the good image, "alone on its leaf… with all that clean space behind it"). ch60 states the count in the closing entry (:145). **Minor:** ch60:141 narration also says "behind session nine alone on its leaf" four lines before the Log's "session nine, alone on its leaf, and staying there" (:145); the cold read asked for one of these, not both. Line fix 2 trims the narration and leaves the Log line.
- **Farewell walk thinned:** ch60:53 the paper-stall man no longer says "Feeling well?" / "Bring it back full"; he "turned the empty slate round on the counter… the way a man turns a clean plate to show there is nothing left on it, and said nothing at all" (new, and his best beat). ch60:61 the mending-stall woman loses "You're in my light"; "Feed him" / "Feed yourself as well" stay. Kept as required: Vell's copied record and offer (ch59), Brom's goodbyes (ch59), Dace's sealed note, Lira's line, Reydan's nod.
- **ch58 notice:** `the particular quiet that had come three times before` → `the particular quiet that came with every notice` (:137). Brom: `It's mine. It's the thing I found in the boat shed.` → `That's my trick. The thing I found in the boat shed.` (:242); "I didn't do it. It did." kept (:244).
- **To taste:** `"You walked me," said Ulric.` → `"You walked me."` (ch58:109; the laugh two lines up names him); ch59:143 Ansel's tag replaced by `Ansel laid both hands flat on the table.` Spoken lines otherwise untouched.
- **Other, author-reported:** ch60:79 "Whatever was still owed between them would keep, and it was not owed this morning." replaces an 11-word source run that the move created; ch60:25 "It turned out that Reydan did want to know it." Both fine.

### Length — RESOLVED
`wc -w` 40,115 (tool 40,013), inside 38,500–41,000. The bout (ch52–53) and both cutaways are intact; the ch60 test scene is the same length.

---

## (2) Continuity

**Movement 7 join.** ch51 closes on the Monday night (day 13) with the inventory, the protected plan line and "Tomorrow is a bout"; ch52 opens on the bout night with Dace's count (504 inside + the street ≈ six hundred, honouring M7's "room for four hundred" plus the street and §11 d), Brom at the north rope and Lira at the south (as ch51 promised), the grey-coat woman with her book, and Reydan handing his coat to nobody. Clean.

**Calendar (no month named; rulings #35/#36 observed).** Day 0 Tuesday: bout, Quenna, Reydan's night (ch52–54). Day 1 Wednesday: Brom's dawn read, the district walk, the lamp relit, Lira's table, the letter dictated (ch55–57). Day 2 Thursday: letter posted; Quenna's inn (ch56–57). Day 3 Friday: "the third day", Quenna agrees to wait; Dace's wall and the Ulric slot (ch57:23–81). Day 5 Sunday: Hesk's reply in the second post; the reply; signing; the binder (ch57:85–191). Day 6 Monday: Ulric watched (ch58:17). Day 7 Tuesday: Quenna's coach; the Ulric bout; the notice; Lira through the wall after midnight (ch58). Day 8 Wednesday: Brom told at first light; Brom's rounds, Keth, Vell's back room, Ansel's stew, Maud at the ropewalk (ch58:240–ch59:155). Day 9 Thursday: departure before light; Reydan's wool wagon ("three weeks ago" = 23 days since M7 day 0 ✓); road day one, the midday tests (ch59:159–ch60). Relative checks land: "written four days ago" for session nine (day 10 → day 14) ✓; "a week ago Tuesday, and then yesterday" in Vell's sheaf on the Wednesday ✓; Reydan at the cooper's "Yesterday. In the morning" = the Ulric Tuesday ✓; "*You've no wall,* Brom had said… eleven days ago" (day 3 → day 14) ✓; "I'd thought to take the coach on Monday. I'll take a later one." → Tuesday ✓; Quenna "Come within the fortnight" and B3 ch1 "the third morning out of Ardenmere" ✓.

**Bodies.** Left forearm plum → slate → pond → yellow (ch55, ch58:7, ch60:163); both hands close "on the Sunday, though not hard" (the left-handed signature, ch57:155); knees locked on purpose, itemised bill, back by the Monday; right shoulder: the groove three deep easing as always, the joint "quiet" under it, lifting to shoulder height by the Tuesday (ch58:25), "something in it to give" on road day one (ch60:161); the left knee takes the second test (ch60:181). Reydan: cracked rib, right shoulder front, right thigh, carried through ch59:135 and ch60:5. Lira's hands yellow (ch56:63). All consistent with M7's closed mechanics and with the #36 right-shoulder ruling — except the ch55:105 "(never drilled)" residual (fix 1).

**Counts and limits.** Knock: when-not-where paid for exactly as M7 set it (ch52:117–123; ch53:11–15); the ch55 Log reconciles with the narrated bout (14/12/2; nine on bursts, two on the count, one on the gathering). Wind: six asked, all left; chain-of-two unused; the lock two *ands*. Pressure: giving face three on the beat; redirects capped at three, all right-shouldered; the cost all at once afterward. Four hundred drop repetitions (ch52:77, ch56:149) ✓. The Ulric bout spends two Wind bursts, eyes and feet, nothing else (ch58:135 Log) ✓ §11 q. Consent boundary: Cael reads only what Reydan gives off at the surface; "he went into no one" stands as in the reviews.

**Knowledge boundaries.** Lira's cutaway stays outside the mechanism (she sees the lock as a shape and Reydan's eyes on the stone; ch52:137–205). Reydan's cutaways never name a Path, the file or the mechanism ("nothing he had a name for"); he learns "I don't have one" and believes it (ch54, ch60:31). Quenna knows the file exists (told by Cael, ch54:184) and nothing of fragments. Brom and Lira know everything including the Compression notice (ch58:206–252). Nobody but Cael knows the [UNBOUND] copy ("told nobody", ch59:105). Hesk knows of the offer and wrote *Go.* Ansel knows only of a close-in "thing" with leave. Reydan's grey-coat warning (ch54:47) gives away nothing.

**Protected wording (§8), exact-string checked.** Item 5 session-nine *Note* line: ch55:89, ch58:174 (by reference), ch59:189 ✓. 6 "Find me later…" ch54:51, ch60:81 ✓. 7 the four-line "What Path is that?" exchange ch54:33–39 ✓. 8 the Compression notice ch58:139–144, all four lines verbatim ✓. 9 "The records know you existed here." ch59:85 ✓. 15 Vell's method line ch53:194; "What did it feel like?" / "Like I had enough." ch54:117–121 ✓. 16 Hesk's three sentences ch57:97 ✓; Brom's three lines ch56:155–159 ✓. 17 the note ch60:103 ✓; "He didn't know the man's name. He never would." ch60:107 ✓; the four road lines ch60:223–233 ✓ (now whole). 30 the two Fenmark lines ch54:204–208 ✓; the provision wording ch54:180, ch57:151 ✓. 31 the Book 1 log line ch60:151 ✓. §1's closing phrase "Compression-adjacent, incomplete expression preceding integration." ch58:168 ✓. Item 10's "three integrated fragments, one anomaly" lives in ch51 as required. The 14 protected overlap runs are these.

**Reserved truths (§7).** Integration: ch58:162 goes closest and stays inside the line ("It had come, as all of them had come, unasked… found in him afterward… That was all he knew about how they came. It was all he let himself know."); "He did not think, *I took it.*"; no rule, no theory; B3 ch9's "never random" remains a first. Falsification, [UNBOUND], Architect, primordial: untouched (the cupboard is a cupboard; the word is not quoted). Tide-adjacent: one occurrence, unreproduced, "Still one"; Compression explicitly does not explain it (ch55, ch58:174). Watcher, Book 1 stranger, Hesk's history, Coss's grade: not raised. Compact: no contact; file mentioned once (ch54:184).

**Names.** Only canon names; Bede (ch52:147, ch53:29) and Maud (ch56:59, ch59:151) never in a spoken list run with Brom; the note's writer never named; Ulric is an established name (M1).

**Two coordinator notes for the close (not manuscript fixes):**
- (i) The STATE_LEDGER "After Movement 7" author end-state still says *left* in four places ("the **left** shoulder carries a 'groove'"; "Reydan saw him favour the left shoulder"; "take it on the turned (left) shoulder"; new canon 9 "the left shoulder"). The manuscript now governs (right, per #36); the After Movement 8 block should say so once, and the M7 block's closing line already states that the manuscript governs where the author end-state predates r1.
- (ii) The series calendar remains the owner's question (#36 item 4): Book 2 still refers to "the autumn" as its own recent past and keeps frost through M5–M7, while B3 ch1 opens in "early autumn". M8 does what the ruling asks (no season, no frost, no snow on the departure days or the road) and nothing in ch57–60 names a season going forward. Not counted against Book 2.

---

## (3) Formula

Reproduced on the current ch52–60 with `python3 editions/monroe-1.3/tools/formula_metrics.py`:

| Measure | Working range | Author (after r1) | Reproduced |
|---|---|---|---|
| Words (tool / `wc`) | 38,500–41,000 | 40,013 / 40,115 | **40,013 / 40,115** |
| Sentence mean | 13–15.5 | 13.72 | **13.72** |
| Sentence median | — | — | 9.5 |
| ≥40-word share | 2.5–4.5% | 3.4% | **3.4%** |
| ≤5-word share | ≤ ~34% | 30.4% | **30.4%** |
| Paragraph median | ≤ ~30 | 27 | **27** |
| Words per scene | 850–1,050 | 909.4 | **909.4** (35 breaks, 8.75 / 10k) |
| FK grade | 3.5–6 | 3.90 | **3.9** |
| Flesch RE | — | — | 91.5 |
| SD (pop.) | — | — | 11.56 |

Every primary measure is inside its working range and matches the author's table. `ed.sh overlap book-02-iron-circuit 8`: **0 unprotected, 14 protected.** `ed.sh overlap book-02-iron-circuit 7`: **0 unprotected, 5 protected.** `ed.sh gates book-02-iron-circuit 8`: **0 / 0 / 0** on all nine chapters. `sweep_probe.sh book-02-iron-circuit 8 8`: **1% skeleton, 10% close** (per chapter 0/11, 0/11, 2/11, 0/8, 1/10, 1/10, 0/9, 0/12, 2/13) — the skeleton hits are the protected lines. B3 ch1 8-gram check on ch60: **0**.

---

## (4) Reader clarity

- **Speaker attribution.** The three-speaker scenes (ch56 the landing table; ch59 the cookshop; ch60 the close) carry names where the ear needs them; the two tags dropped (Ulric ch58:109, Ansel ch59:143) are each preceded within two lines by the speaker's name or action. ch60:199–207 (Brom / Cael / Brom / Cael / Brom) alternates cleanly with one tag at each end.
- **Referents.** "The last one" (ch53:148) is anchored by "By the count… there was one left in it" six lines up; "the joint under the groove" (ch53:212) by the full sentence at :206. "The side he had drilled" (ch53:142) is now the right, and the ch53:136 geometry (every burst "at Cael's right shoulder", walking him leftward) agrees with it. The editorial's two stumbles (the "half his back" body map; Brom's "It's mine") are gone.
- **The thirteen-year-old lens.** The night coach that "did not stop to sleep", the track-name clause, the re-imaged tests ("Nearest thing that bends"; "A quarter, maybe. Of a tenth.") are all concrete and one-pass. The ch58 session-nine paragraph is now short enough not to be skipped.
- **Reader Standard.** The repair added nothing to the word sweep: no oath, no crude slang, no gore; the new road-test cost ("a young horse had kicked him… stood there with its hoof on him") is vivid without injury detail. Pass.
- Brom's "The groove's loud, all three of them" (ch55:135) is grammatically loose by ear but in character (he counts); left as spoken.

---

## (5) Listening proof — every changed region and every chapter

Per-line scan of all nine chapters (odd `"` or `*` counts per paragraph; `---` spacing; digits; abbreviations; curly quotes; ellipses; dash-quote joins):

- **Quotes and italics:** balanced in every paragraph of every chapter. The only italic inconsistency is cosmetic: ch53:130 italicises "on the *three*" but ch53:132 twice writes "On the three" plain beside "*two*" (fixes 5–6; no audio effect).
- **`---` spacing:** every separator has a blank line before and after. Two places carry an extra blank line (two consecutive blank lines): ch53 after "Reydan let him go." before the `---`, and ch54 between "Brom watched the doors." and "You looked at me," (both pre-existing, both harmless to a narrator, both the kind of thing the M7 close fixed; fixes 3–4).
- **Numerals and abbreviations:** no digits in prose (only chapter headers); "Five hundred and four", "six hundred", "fourteen lamps", "about thirty leaves" are words. Initials in letters and chalk (*H.*, *— C.*, *— L.*, *Q.*, *C. — gone east*) voice as letters. "My classification—" (ch54:188) is a spoken interruption on an em dash, which a narrator renders as a cut-off.
- **Homographs and ear collisions:** "read"/"lead" (ch59:117 "the lead seam under his left boot" — metal, unambiguous in context); "wound" absent; "bow window" (ch56:113, ch57:23) could be heard as a bow of the head but "window" disambiguates at once. "Bede"/"Brom" never in one spoken run.
- **Broken joins:** the ch58 scene-1 reorder reads continuously (news → week → Monday → Ulric → Tuesday → coach → evening); the ch60 nod cut leaves "When he looked up again, the far pump was empty" with its "again" earned by the pluperfect that follows; the ch60 four-line close reads as four spoken beats with the attributions carried before them. No dangling sentence anywhere in the diff.

---

## (6) Book-end hand-off (BOOK_MAP §1 and edition B3 ch1)

Checked item by item against §1's ending state and B3 ch1 read in full:
- **Redirect shoulder (right):** B3 ch1:45 "his own right shoulder, the one the Reydan bout had already used hard" and :111 "three clean uses mapped, each paid for in the right shoulder" are both literally true now; "the old complaint, the one that announced itself on certain angles" matches ch58:25's arm that lifts to shoulder height and no higher.
- **Track name:** B3 ch1:296 "And Cael, on the observer track" ← ch57:153 introduces it.
- **Season:** B3 "Early autumn… without yet taking the green out of anything" and "Cold air came down off the hills… smelled of wet stone" are not contradicted by anything in ch59–60 (wet cobbles, raw cold, breath white, sun up, no frost, no season named).
- **Binder:** B3 "a binder now, its rings stiff with cold… the original cover was mostly a memory" ← ch57:173–191 (three iron rings; the old cover set under the rings, ch60:151); "every section used the same four headings" ← ch58:178–190 with the re-ruling intended on the road.
- **Four fragments + session nine:** B3 lists Wind (Lira's), Pressure (Feryn's, three uses, right shoulder, contact only), Iron (Brom's), Compression ("Days old. Bad at everything."), the notice "exactly as it had arrived, the night after his last circuit bout", and "a fifth page, set apart… a date, a short account of an afternoon in Brom's sparring circle, and a single line underneath" ← ch60:145 Log; ch58:139–144 notice after the Ulric bout; ch59:187–189 the one leaf with its date, the thirteenth burst of the ninth session, and the *Note* line exact.
- **Bodies:** B3 "the faint ache that had been there since the first day" / "Knee on day one" ← ch60:181; "the fragment did nothing with force that was still on its way… Reaching early gets nothing… Choose first" ← ch60:189 and ch58:184; Brom kneeling, "right hand open", Iron Skin hardened so the contact "arrived like a flat stone", the braced left forearm ← ch60:163–171 (the stone image now belongs to B3 alone); "Three in twelve… a quarter of a slow push each time… Same price on every success" ← ch60:209 ("one time in four… a quarter of what Brom put in… cost exactly what the first had").
- **Papers, people, pace:** Vell's sheaf and the stranger's note "among the papers he meant to keep" (ch60:109) → B3 ch5/ch12; "six hundred" (B3) ← ch52:11; "Their three paces had become one pace" (ch60:219) ← B3 "they had been doing it for so long that none of them noticed the switching"; "a place… that had written their names down before they came" (ch60:235) ← B3's clerk with her list; Lira provisional and past Fenmark (ch56:63, ch60:121–127); Brom standard enrollment with Vell's stamped extract (ch56:135, ch59:95); Reydan's question, Keth's supper, Vell's cupboard open; no Compact contact.
- **8-gram ch60 ↔ B3 ch1: 0.**
- **Known Book 3-side errata, noted and not counted against Book 2** (queued under #36 for the v1.1 re-lock): B3 ch22 and ch35:227 "third exchange" → "fourth exchange"; ch35 "the notice had come" → the arrival of the thing itself; B3 ch1's loose "weeks" stands by ruling; B3 ch1:111 "Nobody outside the three of them had ever been told it existed" sits oddly beside six hundred witnesses and Hesk's letter (reviews already noted; Book 3's to settle, if ever).

---

## Line fixes (apply all six, then close)

Each old string verified with grep/count to match exactly once in its file; `\n` marks a line break.

1. `manuscript/chapter-55.md`
   old: `A redirect on the right shoulder (never drilled) that stopped passing the burst`
   new: `A redirect on the right shoulder, the third and last, that stopped passing the burst`

2. `manuscript/chapter-60.md`
   old: `behind the four entries and behind session nine alone on its leaf, to the clean pages`
   new: `behind the four entries and session nine's leaf, to the clean pages`

3. `manuscript/chapter-53.md`
   old: `Reydan let him go.\n\n\n---`
   new: `Reydan let him go.\n\n---`

4. `manuscript/chapter-54.md`
   old: `Brom watched the doors.\n\n\n"You looked at me,"`
   new: `Brom watched the doors.\n\n"You looked at me,"`

5. `manuscript/chapter-53.md` (cosmetic; italic consistency with line 130)
   old: `*Inward.* On the three. He went.`
   new: `*Inward.* On the *three*. He went.`

6. `manuscript/chapter-53.md` (cosmetic; same)
   old: `knocked again. *Inward.* On the three.`
   new: `knocked again. *Inward.* On the *three*.`
