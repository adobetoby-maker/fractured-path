# Lane B report: Book 1 completion pass, ch14–47 (M3–M7)

Author: Claude Opus 5.5 (O'Connor 1.3 seat, Monroe Jackson). Date: 2026-10-02.
Scope: `manuscript/chapter-14.md` through `chapter-47.md`. Lane A's chapters (1–13) were not touched. No git commands were run.

## Result against the targets

| Target | Result |
|---|---|
| Every chapter ≤5% skeleton | **Met.** Maximum is 2% (ch15, ch16, ch42). 21 of 34 chapters are at 0%. |
| No scene above 12% | **Met.** The highest is ch32 s3 at 7%: 1 of 14 sentences, and that sentence is the protected line. |
| No unprotected sentence ≥0.65 | **Met.** The 5 sentences still ≥0.65 are all protected (listed below). |
| `ed.sh overlap` 0 unprotected, M3–M7 | **Met: 0 / 0 / 0 / 0 / 0.** The baseline was 45 unprotected 8-word runs, most of them left over from movements closed under the 10-word gate. |
| `ed.sh gates` M3–M7 | **0** reader-standard, **0** metadata and **0** modern-register hits in every chapter. |

These sentences are still at ≥0.65, and every one is protected:
- ch17 s6 and ch19 s2: *Hesk wrote: your body is going to learn before your mind does.* This is protected-patterns "body is going to learn".
- ch20 s2: "The circuit doesn't care what the registry says." This is BOOK_MAP §7 Tier B.
- ch32 s3: "Get stronger. Build a reason for people to notice if I disappear." This is Tier B.
- ch47 s1: "When you figure it out, I want to know." This is Tier A.

## Probe, before and after, per chapter (`sweep_probe.sh`, skeleton %)

| Ch | Before | After | | Ch | Before | After | | Ch | Before | After |
|---|---|---|---|---|---|---|---|---|---|---|
| 14 | 0 | 0 | | 26 | **11** | 0 | | 38 | 0 | 0 |
| 15 | 2 | 2 | | 27 | 0 | 0 | | 39 | 0 | 0 |
| 16 | 2 | 2 | | 28 | 2 | 1 | | 40 | 2 | 1 |
| 17 | 1 | 1 | | 29 | 0 | 0 | | 41 | 1 | 1 |
| 18 | 0 | 0 | | 30 | 2 | 1 | | 42 | 4 | 2 |
| 19 | 3 | 1 | | 31 | 2 | 1 | | 43 | 4 | 0 |
| 20 | **17** | 0 | | 32 | **8** | 1 | | 44 | 1 | 1 |
| 21 | 1 | 1 | | 33 | 1 | 1 | | 45 | 1 | 1 |
| 22 | 1 | 0 | | 34 | 0 | 0 | | 46 | **9** | 0 |
| 23 | 1 | 0 | | 35 | 0 | 0 | | 47 | **12** | 0 |
| 24 | 0 | 0 | | 36 | 0 | 0 | | | | |
| 25 | **16** | 0 | | 37 | 0 | 0 | | | | |

Movement totals: M3 1%, M4 0%, M5 1%, M6 0%, M7 1%.

## Rebuilt scenes: probe, words, event list, change in construction

| Scene | Skeleton before → after | Words before → after (±10%) |
|---|---|---|
| ch20 s1 | 23% → 0% | 2,056 → 2,247 (+9.3%) |
| ch20 s4 | 18% → 0% | 875 → 956 (+9.3%) |
| ch25 s3 | 21% → 0% | 1,331 → 1,430 (+7.4%) |
| ch25 s6 | 27% → 0% | 847 → 929 (+9.7%) |
| ch25 s7 | 17% → 0% | 231 → 216 (−6.5%) |
| ch26 s4 | 31% → 0% | 1,033 → 1,045 (+1.2%) |
| ch32 s3 | 17% → 7% (the protected line only) | 429 → 469 (+9.3%) |
| ch43 s3 | 16% → 0% | 986 → 1,045 (+6.0%) |
| ch47 s2 | 20% → 0% | 1,898 → 1,985 (+4.6%) |

Each line below gives the event list in brief, then what changed in the construction.

- **ch20 s1** (day 29, dawn, mist; Lira and the Arbiter).
  - *Events:* Cael asks how the Arbiter works. Lira breaks off at "always", and he tells her about the eleven seconds, the lamp going out, four weeks of not trying and the midnight yard where he "stopped counting". She has known the word since the board: the crate, less than a pie, the four lines, "like reading letters". Not a bad draw, no draw. His answer on the map: worse and better. "Yesterday": she will not ask, and it did not frighten her. She lists his page: Vell's book, Marrow's slate, the Log, her. Her four-item report goes in the middle column as evidence, "a worse Arbiter… but it's yours". On the wall she asks what it was like inside, and he says it felt finished, and the breaking came from Pellin and the gate guard.
  - *Construction:* The new entry is Cael watching her do her morning Arbiter check, which he now recognizes. His confession comes before her disclosure, which is the reverse of the source. The "page" and the report come before the wall question, and the scene ends on that question rather than starting the reflection with it.
- **ch20 s4** (the night of day 29).
  - *Events:* Supper at Torvin's without Lira, who has a sparring hour she will not name. The meal sits lighter, because of the hand on his shoulder and the question nobody had asked. Front of the Log: her report and *Ruling: getting better. Somebody's checking.* Back: stopped counting, no page, Lira knows, the question moved it an inch, her circuit line, build inside it. The house settles to Torvin's word. He is no longer the only one, and he sleeps without keeping watch.
  - *Construction:* The scene opens on the ruling being written, then steps back to supper, then returns to the back pages. The protected circuit line now goes into the Log in Cael's hand inside a longer sentence. This matches the M3 ledger, which has the back entry "ending *The circuit doesn't care what the registry says*".
- **ch25 s3** (Dessa I, first two exchanges).
  - *Events:* Vell's call. In the first exchange Cael asks at three-quarter pace: the gatepost forearm, the frame turning in one piece, feints that work three times and then not at all. She will not strike or chase; the count is four and four; spending and banking. The second exchange is built to make her rebuild her frame about thirty times on his clock. A thumb's width too near, the well. Benches jeer. The late back foot shows in the second exchange, not at the end; the count is six and six. Every urge says go; the four pages say impatience is her income; he banks it.
  - *Construction:* The first exchange opens on its result ("cost two knuckles and bought one number") and is told as a sequence of questions and answers. The second exchange leads with its theory, "the bill run up on his clock", before the execution. Every sentence is new.
- **ch25 s6** (aftermath with Dessa).
  - *Events:* The yard's noise and his name being tried out. Dessa tests her jaw and waves off the cup. She says: both Sundays, the measured window, the sweep counted, not luck, the cleanest read since she came to the yard (ch27's letter relies on this), "What's your Path?", "Nothing to register", she had a boy like him ready, no book on him, she would sooner face a known Path. "Rematch?" "Not yet… watch you work it. Then we'll talk." She tells him to eat. She never looks at the crowd, takes the water and nods to the pie boy. Then the shaking, reaching for nothing, the stance in the wrong coat, the reset like a gauge, and filing it as *Second instance*.
  - *Construction:* He goes to Dessa first. The shaking, the reaching and the filing, which open the source scene, now close it, alone in the circle after she leaves. The jaw "would keep" beat is kept for ch29's echo.
- **ch25 s7** (Vell's ledger).
  - *Events:* At the table he reads the private line upside down; the spoken record above it is "Conceded from the dirt", "Witnessed and entered". The formal line still has no name. Vell blots the line, shuts the book on her thumb and says the protected line.
  - *Construction:* The scene opens on the private line, read upside down, and gives the spoken record afterwards. Vell's note is reworded. "It's a compliment. Don't spend it." now runs unbroken; the attribution that split it was removed.
- **ch26 s4** (the step under the lantern).
  - *Events:* The win is "a data point". "And underneath?" He built the third exchange and owns every reason. The fourth was not his: "Borrowed", set down like a cup in the dark. "Maybe. I don't know yet." Her sized silence; the district does not care what the registry says. He has been counting from the wrong place and stopped tonight. He will not guess. When he knows she is first, before Hesk, and she would have been offended otherwise. The real smile, the knock on the Renn shoulder, the knuckle bitten at the rope (aligned with ch27), the real-vegetables stew, half a pie, "Nobody tells you that either", smiling on the stairs.
  - *Construction:* The new entry is Cael on the stairs, counting the two half-answers (*instinct*, *I don't know*) and deciding against a third. In the source that reflection sits in the middle of the scene.
- **ch32 s3** (end of Coss's evaluation).
  - *Events:* Coss closes the folder. Cael thanks him and understands it was correctness, not kindness. "Don't thank me… I can buy you time"; the answer is not his to buy. Off the record: what will Cael do with six weeks? He weighs it and gives the protected line. Coss's face. The paper by the desk's left front leg: "It's the leg." "So it has." The stair, the clerk's string, never a word about the yards.
  - *Construction:* Coss stands first. "Don't thank me" answers the thanks at once instead of coming at the end. The off-the-record question comes after he has stood, so the leg and the yards close the scene.
- **ch43 s3** (Vell offers Feryn).
  - *Events:* Day 110, before the bread. Feryn, Bronze Rank 2, Pressure, comes in three weeks. Vell has signed for Cael: assessed-Copper "a fortnight since", "so will I at the rope" (kept; superseded in M9 per the plan). Then the tour: interesting opponents, any rating a keeper signs for, a purse, a gate, one Monday noon. She does not put people in; they ask. Pressure is heavy and like weather: three cities, five years, a one-armed man at nineteen. "Who could I watch?" Lira laughs; the age-in-the-sum speech. Nobody is entering. Friday. "You're standing in my light."
  - *Construction:* The new entry is the shut ledger, with the pie-boy summons told after. Vell names Cael before she explains Feryn's tour; in the source the signing comes after.
- **ch47 s2** (the Pressure notice, night 131/132).
  - *Events:* Slow walk home; he does not go to Lira's (door locks both ways). Yeni turns the lamp toward him. The front of the Log gets the 15th entry and the 14th bout in Vell's book (Baro), the four exchanges and *Reading is necessary. Reading isn't enough.* The back gets *Sixth instance*. The notice comes, exact. He reads it three times, beside the Wind one. The arithmetic: three months against one bout. The held grip. The second-fragment entry, *Might. One data point.*, Kestrel reread with a fourth reason, the questions, and "a hand whose only business was putting me on the ground". The cost, the loss line, "never lost anything and felt less like I'd lost it", and the two things side by side.
  - *Construction:* The scene opens on the notice arriving, then goes back through the walk and the front entries to reach it again. One event is added to support ch47 s3 ("both notices one under the other"): Cael copies the Pressure notice into the back of the Log with the Wind notice written out above it.

## Sentence recomposition outside the rebuilt scenes

About 150 sentences were recomposed outside the nine scenes: every one listed at ≥0.65, the 0.50–0.64 ones that kept a chapter or scene over target, and every 8-word overlap run. Each was re-shaped or folded into its neighbour, not given a synonym swap.

The main concentrations:
- **ch25:** s1, s2, s4 and s5 (15 sentences), plus 6 overlap runs.
- **ch46:** 20 sentences in the Feryn bout.
- **ch47 s1:** 11 sentences at Amrit's.
- **ch32:** s1–s2 (10 sentences).
- **ch20:** s2–s3 (6 sentences).
- **ch42:** 5 sentences.
- **ch19:** 6 sentences.
- **ch26:** s2–s3 (5 sentences).

Single sentences or pairs were recomposed in ch15–18, 21–24, 27, 28, 30, 31, 33, 34, 38–40 and 43. Movement 6 needed only 5 overlap runs (ch34, 38, 39, 40 ×2) and no skeleton work.

Ledger-quoted wording kept on purpose:
- "Two instances is a pattern" (ch26 s3, now struck as before).
- "Reading is necessary. Reading isn't enough."
- "I stood in front of Bronze panels for a year": 0.60, kept as M7 repair canon.
- "Good call." / "I know."
- "thirty-ninth night".
- "Talis, Stone Path, Copper Rank 4".

ch31 needs one decision from the coordinator. The archive subheading (*Deprecated and Non-Standard Designations, Pre-Compact Era Holdovers*) was a 9-word source run.
- **In ch31:** Cael now recognizes it in narration ("the deprecated designations and the non-standard ones, and beneath them, in a smaller hand, *Pre-Compact Era Holdovers*"). This keeps BOOK_MAP §8's protected phrase exactly.
- **In ch4 (Lane A):** the full heading still appears verbatim.
- **Decision needed:** whether the heading should be protected and both chapters made to quote it identically. If so, add it to `protected-patterns.txt` and restore ch31's italic line.

## Referents checked (grepped to ch60 before rewriting)

- **ch20:**
  - ch22:183 "a worse Arbiter than the real one" (said on the first morning) and ch22:233 "less than a pie", both kept.
  - ch22:117 "until he stopped counting", kept.
  - ch22:181 "where she had told him on the first morning they belonged" (her reports go in the evidence column), kept.
  - ch27:95 "her hand on his shoulder in the mist", "keeping them in the grey half… until the morning she did", "reading the notice twice… *This is built*". s2 is unchanged in substance; the hand stays in s2 and the shade reason in s3.
  - The M3 ledger's day-29 back entry, reproduced.
  - The board meeting in ch9 ("the day you told me at the board").
- **ch25:**
  - ch26:33 "Dessa told you to eat something" and ch26:261 "Nobody tells you that either", both kept.
  - ch27:87 "cleanest read anyone had made on her since she came to the yard" and Vell's "compliment… not to spend it", kept.
  - ch29:373 Dessa working her jaw "and seemed to decide it would keep", kept.
  - ch27:135–171 the long side, the cut across, the groove at his heel (s5 unchanged in events).
  - ch50:173 and ch45:173 Dessa on the benches watching him ("Then we'll talk"), kept.
  - ch51:53 the late foot, kept.
  - ch58:195 Vell's *Atypical* tally (untouched; it lives in ch23).
- **ch26:**
  - ch41:149 "put down *borrowed* under the lantern after Dessa", kept.
  - ch43:29 "first, before you, before anybody", kept.
  - ch27:89 "real vegetables", kept.
  - ch27:95 Lira "biting her knuckle at the rope". The source's "bench" was aligned to "rope".
  - ch29:201 "going into the gap like walking through a door in the dark" (untouched).
- **ch32:**
  - ch33:29 "an unpopular report", kept.
  - ch33:37/61 "asked nothing about the yards", kept.
  - ch33:181 the folded paper by the desk's left front leg, kept.
  - The M5 ledger's "I can buy you time…", kept.
- **ch43:**
  - ch46:29/33 "any opponent with a rating a keeper would sign" / "interesting opponents", kept.
  - ch46:259 "three cities", kept.
  - ch47:19 the one-armed man, wet night, nineteen, kept.
  - ch44:167 Pressure "like weather", kept.
  - ch50:71 "You're standing in my light", kept.
  - Assessment timing: "a fortnight since" on day 110 against ch46's "five weeks gone" on day 131. They agree.
- **ch47:**
  - ch47 s3 "both notices one under the other", "the arithmetic, and the grip, and the one data point, and Kestrel at the wrong door", all supported.
  - ch48:71 the Hesk letter (one bout against three months; the hand held "a second longer"), consistent.
  - ch50:235 "one data point", kept.
  - The M7 ledger: the 15th entry and 14th bout, *Sixth instance*, *Reading is necessary…*, *Kestrel, reread… the wrong door*, the loss line, "thirty-seven nights ago", all kept.
- **ch46:** One POV slip from the first pass was caught and fixed: "the man at the rope" became "who it was at the rope", since Feryn is seeing the boy.

No fact, name, number, day or calendar item was changed.

## Metrics (`formula_metrics.py`)

The whole lane (ch14–47) after the pass:
- 177,623 words (+777).
- Sentence mean 13.27 (was 13.16).
- ≥40-word share 3.8% (was 3.6%).
- ≤5-word share 33.4%.
- Words per scene 934.9.
- Paragraph median 26.
- FK grade 3.85.
- Flesch reading ease 91.1.

| Movement | Sentence mean | ≥40-word share | Words per scene |
|---|---|---|---|
| M3 (ch14–20) | 12.89 → 13.14 | 3.9 → 4.1% | 977 → 985 |
| M4 (ch21–27) | 13.05 → 13.23 | 3.0 → 3.1% | 870 → 875 |
| M5 (ch28–33) | 13.11 → 13.21 | 2.7 → 2.9% | 969 → 972 |
| M6 (ch34–40) | 13.27 → 13.27 | 4.2 → 4.1% | 897 → 897 |
| M7 (ch41–47) | 13.44 → 13.45 | 4.2 → 4.1% | 969 → 973 |

Every movement is inside the working ranges on the three primary measures. M6's ≤5-word share (36.6%) was already above the ~34% guide and is unchanged.

Per-chapter rhythm, for chapters this pass touched heavily:
- **ch20:** mean 11.28 → 13.03 and ≥40-word share 1.9 → 3.2%, both now in range.
- **ch25:** 12.64 → 13.63 and 1.6 → 2.7%, both in range.
- **ch32:** 12.39 → 13.06 and 1.3 → 2.7%, both in range.
- **ch26:** 11.42 → 11.75, still below range.
- **ch43:** 11.52 → 11.67, still below range.

Measured one at a time, many chapters in the lane sit outside the working ranges:
- **Sentence mean below 13:** ch15, 17, 22, 23, 26, 29, 30, 33, 35, 37, 39, 43, 44.
- **Sentence mean above 15.5:** ch21, 38, 41.
- **≥40-word share below 2.5%:** ch15, 23, 26, 27, 28, 33, 43.
- **≥40-word share above 4.5%:** ch14, 16, 19, 21, 36, 38, 39, 41, 42, 47.

None of this was introduced by the pass. In every case the chapter was already outside the range, or, where it moved, it moved toward the range. The movements average inside the ranges. Bringing single chapters into range would be a rhythm repair across chapters this pass had no source-distance reason to open. Recommend: decide in Step 2 whether chapter-level ranges are binding.

Words per scene: ch20 (1,230) and ch46 (2,856, which is one long fight scene) were above 1,050 before this pass and still are. The rebuilds kept within ±10% of each scene's length.

Close paraphrase (≥0.35) is not a target, but it remains 14–24% in ch20, 25, 26, 46 and 47, against the reviewers' ~11% clean band. Most of it is shared plot vocabulary in retold beats (fight terms, names, the notice). The whole-arc reader may want to look at it.
