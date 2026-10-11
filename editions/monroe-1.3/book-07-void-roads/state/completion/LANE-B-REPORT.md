# Book 7 — completion pass, Step 3: Lane B report (chapters 31–60)

Author seat: Claude Opus 5.5 (O'Connor 1.3 seat). Date: 2026-10-11.
Scope: `manuscript/chapter-31.md` to `chapter-60.md` only. Baseline: `state/completion/pre-lanes/`.
Method: every chapter read in order, in full; every change made in place with the Edit tool, one sentence at a time. No script touched a manuscript file. No git command was run. Nothing under `books/` or `v3-runs/` was opened, and no source-tracking or plan-audit file. Helper files live only in `state/completion/laneB/`.

## 1. Result in one view

| Target | Brief (Lane B) | Applied | In the named focus chapters |
|---|---|---|---|
| Priority 1 — retrospective interpretation | 50–60 | **57** | 20 in ch38–43, 23 in ch54–60 |
| Priority 2 — "at once", measured pauses, repeated looks | 30–35 | **31** | 10 in ch41–43, 7 in ch57–60 |
| Priority 3 — generic spill of hand / count / entered / price / bill | 45–55 | **46** | 20 in ch41–46, 7 in ch53–57 |
| Smaller habits ("let it stand", "put / set it by") | thin while there | 6 | — |

140 edits in all. Words, chapters 31–60: **153,382 → 151,801** by `formula_metrics.py` (153,748 → 152,167 by `wc`): **−1,581 words, 1.03%**.
Chapters 32, 36, 37, 38 and 49 are byte-identical to the baseline.

Nothing was added. No scene was cut, moved or re-staged; the scene-break count is unchanged in every chapter (133 in the lane). No sentence was lengthened to chase a reading grade.

## 2. Counts before and after, by grep (chapters 31–60, case-insensitive)

Regexes are in `laneB/counts.sh`. The pools are whole-text pools (dialogue, logs and protected lines included), so they fall by less than the number of edits made in narration.

| Pool | Before | After |
|---|---|---|
| "that was" | 179 | 177 |
| "which was" | 69 | 65 |
| "as [someone] had / has" (my regex is wider than the brief's 158) | 213 | 184 |
| "at once" | 46 | 37 |
| measured pauses (for a moment / while / breath / some time, after a while, count- and breath-length) | 92 | 77 |
| evaluative looks with a ruler or a repeat (approximate regex; the read counted about 25 by hand) | 77 | 66 |
| hand(s) | 821 | 797 |
| count-family | 329 | 311 |
| enter-family | 80 | 77 |
| price-family | 54 | 51 |
| cost / bill-family | 65 | 63 |
| "let it / that stand" | 6 | 3 |
| "put / set it by" | 7 | 4 |
| "as if / as though" | 38 | 38 |

What the 57 Priority 1 edits were: 27 "as [someone] had" callbacks cut; 13 restatements of a scene or finding the reader already has; 6 retrospective glosses; 4 "which was"; 2 "That was" codas; 5 interpretive codas or glosses of a line just spoken.
What the 31 Priority 2 edits were: 9 "at once"; 14 measured pauses; 8 looks with a ruler or a repeat on them.
What the 46 Priority 3 edits were: 28 resting or merely moving hands (among them five of Seln's hands-behind-him or folded hands, two of Oryn's palm-rubbing, Brom's fourth thumb on his finger-lines, three slip-of-bark and pencil-in-hand beats); 10 counts that changed nothing; 2 thoughts "entered"; 6 costs priced a second time or called a bill.

## 3. Checks (the brief's "After" section)

- **Overlap, 8 words, movements 5–8:** 0 unprotected in every movement. Protected runs unchanged: 38 / 42 / 34 / 45, the same as the baseline.
- **Gates, movements 5–8:** reader_standard 0, metadata 0, modern 0 in all thirty chapters.
- **Probe (`sweep_probe.sh book-07-void-roads 5 8`):** movement totals unchanged — M5 6% / 21%, M6 3% / 18%, M7 3% / 18%, M8 4% / 17%. I also compared the tool's per-scene numbers before and after (numbers only; no matched text was printed or read): **no chapter's skeleton count or close count rose, and no scene's did** (`laneB/probe-compare.txt`). Six chapters show a rounded percentage one point higher because the pass removed sentences from the denominator while the matched count stayed the same: ch39 close 12→13, ch40 skeleton 4→5, ch45 close 20→21, ch50 close 16→17, ch55 skeleton 5→6, ch56 close 15→16. Five chapters fell (ch42, ch43, ch46, ch57, ch60). This is the case LANE-RULINGS.md ruling 1 accepted for Lane A; see ruling 3 below.
- **The probe caught six of my own recasts** that the 8-word gate could not see: each moved one sentence nearer a source sentence. All six are restored to the baseline wording and listed in the reserve (ch33:235, ch51:353, ch53:361, ch54:65, ch54:213, ch58:111). After the restorations the counts are as stated above.
- **Metrics, per chapter:** every chapter that was inside 13.3–14.2 is still inside it (lowest ch42 13.31 and ch43 13.34; highest ch54 14.15). The two outliers in the lane did not move outward: ch32 14.74 → 14.74 (untouched); ch33 12.58 → 12.60. The ≥40-word share is at or below 4.5% everywhere except ch52, which was 4.7% before the pass and is 4.7% after it. Movement level: sentence mean 13.69 / 13.46 / 13.78 / 13.88; ≥40 share 3.9% / 3.8% / 3.9% / 3.7%; words per scene 984 / 899 / 913 / 936.
- **Protected text, how I checked:**
  1. `laneB/protected.py check` diffs each chapter against `pre-lanes/` and tests every changed line: any run of six or more words shared with BOOK_MAP §10, any `protected-patterns.txt` match and any italic span on a changed line must stand unchanged in the replacement. Result: 140 changed baseline lines, **0 violations**. Four changed lines carry an italic emphasis word (ch41:169, ch53:79, ch54:123, ch56:7); in each the italic text is intact and the edit lies elsewhere in the line.
  2. Every protected run found in the baseline chapters is still present in the edited chapters, and every pattern in `protected-patterns.txt` matches the same number of times as before.
  3. All lines that begin with an italic mark (every log entry, letter, slip, ledger line and document) and the FRAGMENT ACQUIRED block are identical to the baseline, line for line.
  4. The thirteen "Deployment since the Line" lines in the lane are identical in text and order: thirteen (ch33, 35, 39, 40, 45, 46), fourteen (ch48), twenty-three (ch51, 52, 53), twenty-six and twenty-seven (ch55), twenty-seven (ch60).
  5. The overlap tool's protected-run counts are unchanged in all four movements.
  6. I read the whole word-level diff once more after the last change (`laneB/worddiff.py`).
- **House rules on the changed lines:** no season, month or weekday name, no metric unit, no "his Path", no new name. Owner defaults #49, #50 and #51 are untouched and unglossed (ch44:219, ch46:111 and the lines around them were left exactly as they were).

## 4. Declined, and why

- **The consent thread.** Chapters 36, 37 and 38 are untouched. In ch39, 44, 47, 48, 55, 56 and 60 I changed nothing inside the passages the whole-arc read cites (ch39:281–291; ch44:145–213; ch47:97–129; ch48:7–105; ch55:169–287; ch56:153–205; ch60:113–125). This costs the pass its Priority 1 concentration in ch38, which the brief names; the 20 edits in ch38–43 are all in ch39–43. See ruling 1 for the edits that sit in those chapters outside the cited passages.
- **The Ring, the Stair, the Hall.** Chapter 32 has no edit and chapter 31 one habit word. Chapter 49 has no edit; chapters 50 and 51 carry 7 between them, none in the Stair's action; chapter 54 carries 4, each a single clause or a duplicated count.
- **Pike.** Every double look and counted pause of his stands (ch45:107, ch46:213, ch51:267, ch59:157, ch59:193, ch60:57).
- **Medical counts and reserve pauses** stand (for example ch47:79, ch55:27 "as long as it takes to count a hundred", ch60:167).
- **The closing (ch60:247–265)**, including "Cael counted four seconds by the tick of the wood", is left exactly as ratified.
- **"as if / as though":** none changed. The instances I weighed explain an action, not a face or a silence, or sit in frozen chapters.
- **Priority 3 landed at the low end of its range.** Most uses of hand, count, entered and price in this lane are doing work: healing contact, Karis's measuring, Seln's reports, Pike's book, fragment costs and the consent thread. Enter, price and bill had about ten generic uses in the whole lane. I did not recast working uses to raise the number.

## 5. Rulings wanted

1. **Scope of the consent freeze.** I read "the consent thread's wording in ch36–38, ch47–48, ch55–56" as the thread's passages, and froze ch36–38 whole. If the freeze is meant to cover ch47, 48, 55 and 56 whole, these thirteen narration edits should be restored (all outside dialogue; two of them remove a hand beat between two halves of one speech, the spoken words unchanged): ch47:139, ch47:181; ch48:129, ch48:241; ch55:9, ch55:27, ch55:101, ch55:129, ch55:153; ch56:7, ch56:47, ch56:79, ch56:135. The one with real weight is ch55:27, a 57-word sentence in which Cael prices Oryn's reserve again after her mending of Brom's shoulder.
2. **Chapter 41 lost 249 words (4.9%)**, the most of any chapter, under the pacing note for ch41–43. Its words per scene went from 853 to 812; movement 6 stands at 899. The two largest cuts are ch41:145 (Cael re-totals Oryn's days straight after she has said them) and ch41:289 (the clerk-and-capitals gloss, told at ch33:269 and again at ch44:73). If a chapter-level floor of 850 a scene is wanted, restore those two.
3. **"Does not rise" for the probe.** Counts did not rise anywhere; six rounded chapter percentages did, by one point each, from the smaller denominator. Lane A's ruling 1 accepted the same case; I ask that it be confirmed for Lane B.
4. **Chapters 42 and 43 sit at 13.31 and 13.34**, just inside the 13.3 floor. Seven further candidates in those two chapters are held in the reserve for that reason alone.

## 6. Joins for a second ear in the listening proof

Speech joined where a stage beat was removed (the spoken words are unchanged; the breath between them is gone): ch40:317 (Seln, "many happy returns"), ch41:127 (Oryn at the barn door), ch43:151 (Oryn to Cael), ch44:47 (Oryn in the loft), ch46:59 (Lira, "walk away"), ch46:119 (Seln), ch48:241 (Seln's order), ch51:173 (Seln's reading of what the six saw), ch53:351 (Karis), ch55:129 (Lira on the bow), ch60:25 (Karis), ch60:73 (Karis at the plank).

Paragraphs that now open or close on a different sentence: ch33:177; ch41:39, ch41:145, ch41:195–201, ch41:289; ch42:43, ch42:193; ch43:29, ch43:107, ch43:121, ch43:135, ch43:241, ch43:291; ch44:73, ch44:279; ch45:83, ch45:165, ch45:191; ch46:92, ch46:131; ch52:15, ch52:301; ch54:289; ch55:27; ch56:79; ch57:71, ch57:195; ch58:35, ch58:41; ch60:103, ch60:227.

## 7. Helper files (all in `state/completion/laneB/`)

`edits.tsv` (every applied edit), `reserve.tsv` (held back), `counts.sh`, `metrics.sh`, `protected.py`, `worddiff.py`, `probe_scenes.sh`, `probe_compare.py`, and the before / after outputs: `base-*.txt`, `after-*.txt`, `metrics-compare.txt`, `movement-metrics.txt`, `protected-check.txt`, `probe-compare.txt`, `protected-lines.txt`.

## 8. Words and edits per chapter

| ch | words before | words after | change | mean before → after | ≥40 share before → after | words/scene before → after | P1 | P2 | P3 | habit |
|---|---|---|---|---|---|---|---|---|---|---|
| 31 | 5362 | 5361 | -1 | 14.07 → 14.07 | 0.042 → 0.042 | 1072.4 → 1072.2 | 0 | 0 | 0 | 1 |
| 32 | 5850 | 5850 | 0 | 14.74 → 14.74 | 0.033 → 0.033 | 1170.0 → 1170.0 | 0 | 0 | 0 | 0 |
| 33 | 4502 | 4498 | -4 | 12.58 → 12.6 | 0.034 → 0.034 | 900.4 → 899.6 | 1 | 0 | 0 | 0 |
| 34 | 5120 | 5109 | -11 | 13.33 → 13.34 | 0.044 → 0.044 | 1024.0 → 1021.8 | 0 | 1 | 3 | 0 |
| 35 | 6457 | 6408 | -49 | 13.57 → 13.49 | 0.044 → 0.042 | 922.4 → 915.4 | 1 | 2 | 2 | 0 |
| 36 | 4764 | 4764 | 0 | 13.46 → 13.46 | 0.04 → 0.04 | 952.8 → 952.8 | 0 | 0 | 0 | 0 |
| 37 | 4438 | 4438 | 0 | 14.14 → 14.14 | 0.042 → 0.042 | 887.6 → 887.6 | 0 | 0 | 0 | 0 |
| 38 | 5425 | 5425 | 0 | 13.7 → 13.7 | 0.038 → 0.038 | 904.2 → 904.2 | 0 | 0 | 0 | 0 |
| 39 | 5133 | 5092 | -41 | 13.4 → 13.36 | 0.039 → 0.039 | 855.5 → 848.7 | 1 | 0 | 2 | 0 |
| 40 | 6140 | 6092 | -48 | 13.55 → 13.48 | 0.04 → 0.035 | 1023.3 → 1015.3 | 3 | 1 | 1 | 1 |
| 41 | 5118 | 4869 | -249 | 13.8 → 13.6 | 0.038 → 0.034 | 853.0 → 811.5 | 8 | 4 | 5 | 0 |
| 42 | 5221 | 5152 | -69 | 13.42 → 13.31 | 0.044 → 0.041 | 1044.2 → 1030.4 | 3 | 3 | 1 | 0 |
| 43 | 5135 | 4990 | -145 | 13.44 → 13.34 | 0.042 → 0.043 | 855.8 → 831.7 | 5 | 3 | 3 | 0 |
| 44 | 5340 | 5257 | -83 | 13.59 → 13.45 | 0.041 → 0.038 | 890.0 → 876.2 | 2 | 1 | 2 | 0 |
| 45 | 4394 | 4298 | -96 | 14.08 → 13.91 | 0.035 → 0.029 | 878.8 → 859.6 | 3 | 2 | 2 | 1 |
| 46 | 6223 | 6131 | -92 | 13.98 → 13.9 | 0.04 → 0.039 | 889.0 → 875.9 | 2 | 1 | 7 | 1 |
| 47 | 4445 | 4425 | -20 | 13.63 → 13.57 | 0.04 → 0.04 | 889.0 → 885.0 | 0 | 2 | 0 | 0 |
| 48 | 4644 | 4642 | -2 | 13.54 → 13.57 | 0.044 → 0.044 | 928.8 → 928.4 | 0 | 0 | 2 | 0 |
| 49 | 4875 | 4875 | 0 | 13.66 → 13.66 | 0.034 → 0.034 | 975.0 → 975.0 | 0 | 0 | 0 | 0 |
| 50 | 5311 | 5290 | -21 | 14.12 → 14.07 | 0.037 → 0.037 | 885.2 → 881.7 | 0 | 1 | 2 | 0 |
| 51 | 6533 | 6489 | -44 | 13.87 → 13.84 | 0.04 → 0.038 | 933.3 → 927.0 | 2 | 1 | 1 | 0 |
| 52 | 5896 | 5844 | -52 | 13.81 → 13.69 | 0.047 → 0.047 | 982.7 → 974.0 | 2 | 1 | 1 | 0 |
| 53 | 6137 | 6101 | -36 | 13.88 → 13.87 | 0.036 → 0.036 | 1022.8 → 1016.8 | 1 | 0 | 1 | 1 |
| 54 | 5402 | 5362 | -40 | 14.18 → 14.15 | 0.034 → 0.034 | 900.3 → 893.7 | 2 | 0 | 2 | 0 |
| 55 | 4934 | 4841 | -93 | 13.9 → 13.71 | 0.042 → 0.04 | 986.8 → 968.2 | 2 | 0 | 3 | 0 |
| 56 | 3695 | 3635 | -60 | 14.1 → 13.98 | 0.042 → 0.042 | 923.8 → 908.8 | 2 | 1 | 1 | 0 |
| 57 | 3836 | 3775 | -61 | 14.15 → 14.03 | 0.037 → 0.033 | 959.0 → 943.8 | 4 | 2 | 0 | 1 |
| 58 | 3730 | 3661 | -69 | 13.51 → 13.41 | 0.04 → 0.04 | 932.5 → 915.2 | 3 | 1 | 2 | 0 |
| 59 | 4026 | 3949 | -77 | 14.13 → 13.9 | 0.035 → 0.032 | 1006.5 → 987.2 | 4 | 1 | 0 | 0 |
| 60 | 5296 | 5178 | -118 | 14.09 → 13.92 | 0.04 → 0.035 | 882.7 → 863.0 | 6 | 3 | 3 | 0 |
| total | 153382 | 151801 | -1581 | | | | 57 | 31 | 46 | 6 |

## 9. Reserve — found, and held back to stay on the brief numbers

Fifty-three candidates. Thirty-nine were applied and then restored when the running totals passed the brief (they are the non-focus chapters' share). Seven are held because ch42 and ch43 sit on the 13.3 mean floor, and one more (ch53:205) was simply not applied. Six were restored because the sentence-level probe count rose with them. Line numbers are baseline lines.

| ch:line (baseline) | target | candidate |
|---|---|---|
| 31:53 | P1 as-had | cut "as he had taken it up at a ford" |
| 32:89 | P1 as-had | cut "as a man of Thornwater had once got a hand between" |
| 33:77 | P2 at-once | "did not take them away at once" -> "did not take them away" |
| 33:151 | P1 as-had | cut "as she had lain on a mountain" |
| 33:235 | habit let-stand | "He let it stand" -> "He left it"  [restored: the sentence-level probe count rose with this change] |
| 34:123 | P2 at-once | "reached for her pencil at once" -> "reached for her pencil" |
| 34:273 | P2 look | "Cael read them twice." -> "Cael read them." |
| 35:317 | P1 as-had | cut "as she had pressed on Lira's shin under a rock" |
| 35:365 | P1 as-had | cut "as eight had sat down at Oxhollow" |
| 39:265 | P2 pause/look | "looked at him for some time, as" -> "looked at him as" |
| 40:5 | P2 pause | "enjoyed that for the length of a few breaths" -> "enjoyed that" |
| 40:211 | P2 pause | "For a breath only the spit" -> "Only the spit" |
| 42:47 | P3 hand | Seln "with his hands behind him" (held: mean floor) |
| 42:89 | P1 as-had | "as she had taken it by lantern at a stone" (held: ch42 mean at the floor) |
| 42:139 | P1 which-was | "she did what she had made up her mind on the ladder to do, which was to say the thing" (held: mean floor) |
| 43:11 | P1 as-had | "as a one-armed man read a line under an eave" (held: ch43 mean at the 13.3 floor) |
| 43:59 | P2 pause | "she let a good while go by before she spoke" (held: mean floor) |
| 43:237 | P1 as-had | "as it had on a rim" (held: mean floor) |
| 43:329 | P1 as-had | "as it had once stayed for a breath on the top of his head in a loft" (held: mean floor) |
| 44:9 | P1 as-had | cut "as she had sat at a board with a goat on it" |
| 44:53 | P2 look | "rested on him for the length of a breath" -> "rested on him" |
| 44:123 | P1 as-had | cut "as he had sat on the first night of the listening" |
| 44:137 | P2 pause | "for some time afterward" -> "afterward" |
| 44:239 | P1 that-was | cut "That was all." |
| 45:11 | P1 as-had | cut "as he had stood on every morning that they had spent behind that fence" |
| 45:43 | P2 pause | "for some time he left it shut" -> "he left it shut" |
| 45:115 | P1 as-had | cut "as he had felt a yard do it once, at an academy on a hill" |
| 46:5 | P2 pause | cut "for some time" |
| 46:5 | P1 as-had | cut "as he had looked through the first on an inn's boards" |
| 46:213 | P1 as-had | cut "as he had written them on another paper twenty-two days before" |
| 46:275 | P1 that-was | "That was the part of it that he had not been able to make..." -> "He had never been able to make four friends understand that part of it" |
| 47:31 | P2 at-once | "it came at once, low and hoarse" -> "it came low and hoarse" |
| 47:41 | P1 as-had | cut "as they had lain on a sill at Thornwater" |
| 47:193 | P1 as-had | cut "what he had seen on her face in a yard, when she unloaded a mule: it was" |
| 48:221 | P1 as-had | cut "as he had told it at a stake on the Fallow" |
| 48:247 | P1 as-had | cut "as he had once given five people the order of a watch" |
| 49:17 | P1 as-had | cut "as he had grunted on the Fallow" |
| 49:77 | P2 at-once | "understand all of it at once, as" -> "understand all of it, as" |
| 49:247 | P1 as-had | cut "as Cael had seen her do once before, at the rim of a white floor, with a strip of her own shirt in her teeth" |
| 50:159 | P2 at-once | "said Seln at once" -> "said Seln" |
| 50:243 | P2 at-once | "paid for it at once" -> "paid for it" |
| 51:159 | P1 as-had | cut "as it had come at the stone on the Fallow" |
| 51:219 | P2 pause/look | cut "He looked at that for a little." |
| 51:247 | P1 as-had | cut "as he had set down a question at an inn's door two nights before" |
| 51:353 | P1 restatement (Teague) | cut ": that he had seen a man walk out of the Quiet and declare" (scene just shown at :239-249)  [restored: the sentence-level probe count rose with this change] |
| 52:95 | P2 pause | "for some time she did not move" -> "she did not move" |
| 53:139 | P1 as-had | cut "as she had set one on the Fallow and one between two bars of iron" |
| 53:205 | P1 as-had | "as she had said it at two other stones" |
| 53:361 | P2 pause/look | "looked at him for some time, and then" -> "looked at him, and then"  [restored: the sentence-level probe count rose with this change] |
| 53:381 | P1 as-had | cut "as he had written one at another stake three days' walk behind him" |
| 54:65 | P1 as-had | cut "as he had once pitched a single word down two hundred yards of old road"  [restored: the sentence-level probe count rose with this change] |
| 54:213 | P2 at-once | "told him the price at once, low" -> "told him the price, low"  [restored: the sentence-level probe count rose with this change] |
| 58:111 | habit let-stand | cut "and he let it stand"  [restored: the sentence-level probe count rose with this change] |

## 10. Every applied edit

Line numbers are baseline (`pre-lanes/`) lines.

| ch:line (baseline) | target | change |
|---|---|---|
| 31:29 | habit put-by | "put it by for whoever kept findings" -> "left it for" |
| 33:177 | P1 that-was | cut "That was the camp." |
| 34:23 | P3 price | "it was the same price each time ... paid it" -> "it came out the same each time ... paid" |
| 34:95 | P3 entered | "never once entered his head" -> "never once occurred to him" |
| 34:183 | P3 hand | cut "with its hands hanging" (repeat of :119) |
| 34:247 | P2 pause | cut "Seln was silent for a breath." |
| 35:125 | P3 count | cut "since he could not have helped it" (the count of her eight crossings stands) |
| 35:143 | P2 look/pause | "held his eye for as long as it takes to count three" -> "held his eye" |
| 35:223 | P3 hand | "sat on a pannier with his hands on his knees and gave orders" -> "sat on a pannier and gave orders" (repeat of :29) |
| 35:291 | P1 which-was | "she did what she had done when five came in from a ford, which was to go along them" -> "and went along them" |
| 35:335 | P2 pause | cut "It took her as long as it takes to count five." |
| 39:15 | P3 hand | cut "with her right hand over the sling" (resting hand; repeat of ch36:33) |
| 39:181 | P1 as-had | cut "as he had kept hers on a gravel bar" |
| 39:241 | P3 price/bill | cut "A bill had always come afterward... shown the price beforehand." (cost already shown at :229) |
| 40:49 | P2 at-once | "then, all at once, as he saw a bout" -> "then, as he saw a bout" |
| 40:109 | P1 as-had | cut "and she went at this one as she had once gone at a restricted shelf" |
| 40:227 | P1 as-had | cut "as he had once read out the tags on a researcher's bundles" |
| 40:317 | P3 hand | cut beat "He had his hands behind him." (Seln; speech joined) |
| 40:329 | P1 as-had | cut "as it had once given her that much at a ford" |
| 40:337 | habit set-by | "He set that by" -> "He kept that" |
| 41:13 | P1 as-had | cut "as he had carried them to a box" |
| 41:39 | P1 as-had | cut "They went at it as they had once gone at a library on the same trestle." |
| 41:61 | P3 hand | "a sheet of thin paper in his hand that had" -> "a sheet of thin paper that had" |
| 41:85 | P1 restatement | cut "She could still taste that apple... since Ternhall." (apple lesson already at :55 and :83) |
| 41:121 | P2 look | cut "It took about as long as it took her to count a bench." |
| 41:127 | P2 pause | cut beat "The healer was silent for a breath." (speech joined, words unchanged) |
| 41:145 | P3 cost re-priced | Oryn's days re-totalled after she has just said them -> "He had the sum, and he was to do nothing with it." |
| 41:145 | P3 hand | cut "Cael turned a slip of bark over in his fingers." (slip-of-bark business x3 in ch41-43) |
| 41:149 | P1 as-had | cut "as he had crossed it once with a peeled stick" |
| 41:169 | P1 which-was | "good words for what they were, which was a warning" -> "good words for a warning" |
| 41:191 | P3 hand | cut "She had the pencil in her hand." |
| 41:195 | P2 look/pause | cut "She looked at it for some time." |
| 41:199 | P1 restatement | cut "It was the right grammar. It was a word for a process..." (said at :197 and aloud at :277) |
| 41:201 | P2 at-once | "distrusted it at once, for the fit" -> "distrusted it for the fit" |
| 41:245 | P1 as-had | cut "as she had once read a line of his" |
| 41:271 | P3 hand | cut "with his hands behind him" (Seln, resting hands) |
| 41:289 | P1 retrospective | clerk/capitals gloss (repeat of ch33:269) -> "A word in capitals on a file had shut a door on a boy." |
| 42:43 | P2 pause-beat | cut "It lay on the cold air among the sacks." (repeat of the "it lay on..." landing beat) |
| 42:63 | P2 pause/look | "studied the sixth row for some time" -> "studied the sixth row" |
| 42:125 | P1 as-had | cut "as she had told him against a bar of iron" |
| 42:193 | P3 count | cut "She counted them, since there was nothing else to count." |
| 42:297 | P2 at-once | "She saw that at once, and" -> "She saw that, and" |
| 42:315 | P1 restatement | cut ": three lies and a truth, with a step on the fourth..." (drill explained twice in ch39) |
| 42:319 | P1 as-had | cut "as she had waited at the lip of a gravel bar with a river in front of her" |
| 43:15 | P1 which-was | "the leaf, which was the shortest thing" -> "the leaf, the shortest thing" |
| 43:29 | P1 restatement | query/paper/stake line re-told from ch34:275 -> one clause ": a query, and a paper under a broker's seal, and a stake" |
| 43:107 | P2 at-once | "could not answer her at once" -> "could not answer her" |
| 43:107 | P1 restatement | ladder/leaf/slips recap (ch41:275) trimmed to one clause |
| 43:121 | P3 count/sum | cut "He had done the sum on the ladder, and he did it again now, since he could not help it." |
| 43:135 | P1 gloss | cut "It was not praise, and Lira did not take it for any." (repeat of ch35:207) |
| 43:151 | P3 hand | cut beat "She rubbed her palms together." (Oryn's seventh; speech joined) |
| 43:237 | P3 hand | cut "He stood at a wicket with his hands shut." |
| 43:241 | P1 retrospective | cut "He thought of a girl who had run a quarter-mile of that fence..." (told at ch42:197) |
| 43:291 | P2 pause | cut "She was silent for the length of a few breaths." |
| 43:329 | P2 at-once | "She said it at once, and without" -> "She said it without" |
| 44:47 | P3 hand | cut beat "She rubbed her hands together slowly." (speech joined; palms go up at :49) |
| 44:71 | P2 pause | cut "for the length of several breaths" |
| 44:73 | P1 retrospective | seat/clerk/file gloss trimmed (third telling); cut "as Karis had left them on a trestle" |
| 44:103 | P3 hand | cut "with her hands on her knees" |
| 44:279 | P1 restatement | Oryn's eight crossings re-listed (shown at ch35:121-139) -> cut the list |
| 45:57 | P3 count | "stopped on the crown of it and counted what was there" -> "stopped on the crown of it to see what was there" |
| 45:83 | P2 pause | cut "They stood with it on the hill for a breath." |
| 45:83 | P1 restatement | Oryn's ask-a-carter instruction re-told (ch44:115, :73) -> "She was a day from where they stood." |
| 45:165 | P1 gloss | cut "It was not a thing that any registry seat would have said." |
| 45:165 | habit set-by | cut "and he set it by, to be looked at later" |
| 45:191 | P2 pause | cut "For the space of a breath there was only the fire." |
| 45:209 | P1 retrospective | cut "who had watched her ring three blanks on a calfskin and write a word beside two of them" (she says it at :211) |
| 45:217 | P3 hand | cut "with his hands at his back" (Seln) |
| 46:7 | P3 hand | cut "and her right hand over the knot of her sling" (the vote keeps it at :167) |
| 46:57 | P2 pause | "let that stand by itself for a breath" -> "left it there" (also let-stand habit) |
| 46:59 | P3 hand | cut beat "Her right hand had closed on the knot." (speech joined) |
| 46:71 | P3 hand | cut "and rubbed the four dark lines on his fingers with his thumb" (Brom's fourth) |
| 46:93 | P3 hand | cut "She had her notebook shut under both hands, as she had held it at an inn's boards." (repeat of :39) |
| 46:119 | P3 hand | cut beat "Seln folded his hands on the two sheets." (speech joined) |
| 46:123 | habit set-by | "he set them all by" -> "he used none of them" |
| 46:131 | P1 coda | cut "It lay there among them in the firelight like a tool on a bench." |
| 46:225 | P3 hand | "Cael stood with nothing in his hands, and he knew" -> "Cael knew" |
| 46:227 | P1 as-had | cut "as a healer had once said that her table was turned" |
| 46:309 | P3 entered | "and he entered it as it stood" -> "and he did not pretend otherwise" |
| 47:139 | P2 pause | cut "In the time that it takes to draw a bucket" (repeat of ch43:145) |
| 47:181 | P2 pause | "stood there for about as long as it takes to count twenty" -> "stood there" (same measure at ch42:111) |
| 48:129 | P3 count | "counted what there was, as he counted anything" -> "looked at what there was, as he looked at anything" |
| 48:241 | P3 hand | cut beat "He folded his hands." (Seln; speech joined) |
| 50:29 | P3 count | cut "Cael counted them, since he could not help it:" (Seln counts them aloud at :31) |
| 50:231 | P2 at-once | cut "and he saw that at once" |
| 50:231 | P3 price | cut "and saw the price of it" (the cost is the next sentence) |
| 51:119 | P1 as-had | cut "and Cael watched her do what he had seen her do at a rock on the Fallow, eight times in one grey morning, when she thought that nobody saw" |
| 51:173 | P3 hand | cut beat "Seln folded his hands." (speech joined) |
| 51:279 | P1 gloss (Teague) | cut "He had been turning that over ever since." |
| 51:293 | P2 pause/look (Teague) | "looked at him for some time" -> "looked at him" |
| 52:15 | P1 gloss | cut "He had one word for a thing that he could neither refuse nor repay, and he had already given it to this man once." ("Noted" explained at ch46:251) |
| 52:111 | P2 at-once | "She said it at once, without" -> "She said it without" |
| 52:229 | P3 hand | cut "and both her hands were open at her sides" |
| 52:301 | P1 as-had | cut "and it lay in that cold room as her three facts had once lain on a trestle" |
| 53:63 | P1 restatement | cut "The great boot slid in the mud as it had skated on the ice, and her right arm went out..." (repeat of ch45:15) |
| 53:79 | habit let-stand | "He let it stand." -> "He left it so." |
| 53:351 | P3 hand | cut beat "She had her hands round her knees." (speech joined) |
| 54:25 | P1 as-had | cut "as he had once taken in a floor from a rail" |
| 54:107 | P1 as-had | cut "as he had understood a stair under a floor" |
| 54:123 | P3 count | cut "since he counted everything" |
| 54:289 | P3 count | cut "That made four. Cael had counted them without meaning to. He was counting very little else;" (Lira has just called "Four") |
| 55:9 | P1 as-had | cut "as she had looked at it outside another stone" |
| 55:27 | P3 cost re-priced | cut "Cael had heard her say on a mountain that her reserve was a purse... knew it to the grain." (her reserve priced again; shown by the count of a hundred) |
| 55:101 | P1 as-had | cut "as she had once studied him in a yard" |
| 55:129 | P3 hand | cut beat "Her right hand moved on the stock, a finger's breadth, and lay still." (verbatim repeat of ch50:59; speech joined) |
| 55:153 | P3 bill | "wrote the day's bill" -> "wrote the day's log" (bill already at :51) |
| 56:7 | P1 which-was | "as it had been done at the Stair, with one difference, which was that" -> "as at the Stair, with one difference:" |
| 56:47 | P2 look | "looked at her for as long as it takes to draw one breath" -> "looked at her" |
| 56:79 | P1 restatement | cut Teague's re-telling "They had gone as people go who have practised leaving... nothing above the height of a boot." (told at ch51:343-351) |
| 56:135 | P3 count | cut "He counted, as he counted before he did anything, and" (count kept once: his own, then the camp) |
| 57:25 | P1 retrospective | cut "and she had learned from a man with apple trees to tell those two apart" (apple lesson, fifth telling) |
| 57:25 | habit let-stand | "and let it stand" -> "and left it" |
| 57:43 | P1 as-had | cut "as it had stayed there for five days" |
| 57:71 | P1 that-was | cut "That was the thing which she kept returning to, as a tongue goes back to a tooth." |
| 57:97 | P1 as-had | cut "as she had at a grey stone six days before" |
| 57:139 | P2 at-once | "did not turn round at once" -> "did not turn round" |
| 57:195 | P2 pause | cut "For a breath there was only the fire." |
| 58:35 | P1 restatement | cut "She had told them at a mill what she would do on the day that the round could not spare her, and what they were to say to it." (ch47:209) |
| 58:41 | P3 count | cut "He counted, since he could not walk beside anybody without counting." (the fifty paces stand at :43 and :87) |
| 58:77 | P1 as-had | cut "as he had gone ahead on every road since a shelf" |
| 58:119 | P2 at-once | "which he did not at once believe" -> "which he could not at first believe" |
| 58:185 | P1 restatement | "no call for anybody's foot. The line was marked...; no foot was needed to find it." -> one sentence |
| 58:205 | P3 hand | cut "with her right hand shut on the strap of the bow" |
| 59:17 | P1 retrospective | cut "who had learned that crew's sound on a hundred roads and had learned it again at a fork with a pair of boots gone out of it" (ch57:163, ch58:83) |
| 59:75 | P2 pause | "sat for some time with his hand over" -> "sat with his hand over" |
| 59:81 | P1 restatement | cut "She had stopped with her pencil over a leaf, and looked at her own cuff..." (shown at ch57:35-37) |
| 59:105 | P1 as-had | cut "as she had once held a flake from the footing of a city's gate" |
| 59:197 | P1 as-had | cut "as he had once read a bailiff's list on a counter" |
| 60:17 | P1 as-had | cut "as it had lain on a floor under the ground" |
| 60:25 | P3 hand | cut beat "Karis leaned on the deal with both palms." (speech joined) |
| 60:49 | P1 as-had | cut "as he had stood at a ford on the fourth day past the Line" |
| 60:69 | P2 look | "read it standing in the snow, and then he read it again" -> "read it standing in the snow" (Pike's double look stays at :57) |
| 60:73 | P1 as-had | cut beat "She was looking at the brass as she had once looked at a founding stone." |
| 60:87 | P3 hand | cut "with his hands behind him" (Seln) |
| 60:103 | P1 restatement | cut "She had told a girl in a yard that a beast should not be named, and had learned at a wicket how little that helped." (ch44:259-261) |
| 60:141 | P1 as-had | cut "as he had stood on every evening that she could remember" |
| 60:173 | P3 hand | cut "with her hands under her arms" |
| 60:189 | P2 pause/look | "looked at it for some time after" -> "looked at it after" |
| 60:227 | P2 pause | cut "Nobody spoke for a breath." |
| 60:243 | P1 as-had | cut "as she had bent beside a fire in the dark" |
