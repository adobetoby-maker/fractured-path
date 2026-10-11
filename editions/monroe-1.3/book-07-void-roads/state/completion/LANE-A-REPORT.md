# Book 7 — completion pass, Step 3: Lane A report (ch1–30, movements 1–4)

Author seat: Claude Opus 5.5 (O'Connor 1.3 seat), same-author texture pass. Date: 2026-10-11.
Brief: `PASS-BRIEF.md`. Baseline: `state/completion/pre-lanes/`. Working files: `state/completion/laneA/`.

Method: read ch1–30 in order, every word, and edited in place with the Edit tool, one sentence at a
time. No script wrote to a manuscript file. No git command was run. Nothing under `books/` or
`v3-runs/` was opened; the overlap and probe tools read the source. Only `manuscript/chapter-01.md`
to `chapter-30.md` were edited.

## 1. Result in one view

| Target | Brief | Applied |
|---|---|---|
| Priority 1 — retrospective interpretation | 35–45 | **45** (24 in ch15–22, 8 in ch27–30, 11 in ch1–14, 2 in ch23–26) |
| Priority 2 — attention and pause choreography | 25–30 | **26** (13 measured pauses, 6 "at once", 7 repeated looks) |
| Priority 3 — motif spill | 35–45 | **43** (21 hands, 6 counts, 5 "entered", 8 price/cost/rent/paid, 3 "put by / let stand") |
| Total edits | | **114** |
| Words (wc) | | 153,433 → 152,182 (**−1,251**) |

No new material. No scene cut, moved or re-staged. Nothing was lengthened to chase a measure. The
recasts come to fewer than 200 words of wording in all; everything else is removal. Three recasts
leave a sentence a few words longer than it was: ch7:371–373 joins two short sentences into one of
twelve words; ch15:71 is one word longer; ch18:135 carries "thirty grey heaps" onto the sentence
before, in place of a 26-word sentence.

Priority 1 by kind: 19 "as [someone] had…" callbacks; 8 "That was…" codas; 2 "which was"; 16 other
retrospective glosses (a present look or line explained through an earlier scene, or a spoken
finding restated by the narration).

## 2. Counts before and after (grep, ch1–30, case-insensitive)

Patterns are in `laneA/count.sh`. My "as [someone] had" pattern is wider than the brief's (it also
takes "would have / might have" and "the/his/her + noun"), so its pool is larger than the brief's 104.

| Pool | Before | After | Change |
|---|---|---|---|
| "that was" | 155 | 143 | −12 |
| "as [someone] had / would have" | 180 | 159 | −21 |
| "which was" | 46 | 43 | −3 |
| "at once" | 43 | 37 | −6 |
| measured pauses (for a moment / while / breath / count; after a while; for some time) | 66 | 57 | −9 |
| repeated looks (looked … once / twice / again; second look) | 29 | 27 | −2 |
| hand / hands | 687 | 665 | −22 |
| count-family | 279 | 270 | −9 |
| enter-family | 44 | 39 | −5 |
| price-family | 53 | 51 | −2 |
| bill / cost | 82 | 76 | −6 |
| "let it stand" | 3 | 2 | −1 |
| "put / set it by" | 3 | 1 | −2 |
| "as if / as though" | 52 | 51 | −1 |

The grep changes are smaller than the edit counts in places because several edits removed a habit
my patterns do not spell (a look "a second time", "the space of a breath", "for as long as it would
have taken to count ten", "paid the rent", "an expression he had not seen since…").

## 3. Per chapter: edits, words, metrics

Edits by priority, words by `wc`, sentence mean and ≥40-word share by `tools/formula_metrics.py`.
Scene breaks are unchanged in every chapter.

| Ch | P1 | P2 | P3 | Words before | after | Δ | Mean before | after | ≥40 before | after | Scenes b/a | w/scene before | after |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | 1 | 2 | 1 | 5429 | 5414 | -15 | 13.68 | 13.68 | 4.0% | 4.1% | 4/4 | 1083 | 1080 |
| 02 | 0 | 3 | 1 | 4644 | 4624 | -20 | 13.92 | 13.90 | 4.2% | 4.2% | 4/4 | 927 | 923 |
| 03 | 0 | 3 | 1 | 4820 | 4798 | -22 | 13.39 | 13.33 | 4.5% | 4.2% | 4/4 | 962 | 957 |
| 04 | 0 | 2 | 0 | 6433 | 6423 | -10 | 14.02 | 14.00 | 4.4% | 4.4% | 5/5 | 1070 | 1069 |
| 05 | 2 | 0 | 0 | 4706 | 4690 | -16 | 14.72 | 14.67 | 4.7% | 4.7% | 4/4 | 939 | 936 |
| 06 | 1 | 2 | 1 | 4992 | 4964 | -28 | 14.79 | 14.71 | 4.7% | 4.7% | 4/4 | 997 | 991 |
| 07 | 3 | 1 | 1 | 6176 | 6151 | -25 | 13.89 | 13.89 | 3.8% | 3.8% | 6/6 | 881 | 877 |
| 08 | 1 | 1 | 1 | 5442 | 5428 | -14 | 14.26 | 14.26 | 3.1% | 3.2% | 4/4 | 1086 | 1084 |
| 09 | 0 | 1 | 1 | 4843 | 4840 | -3 | 13.02 | 13.01 | 4.3% | 4.3% | 4/4 | 966 | 966 |
| 10 | 1 | 0 | 2 | 5051 | 5025 | -26 | 15.75 | 15.67 | 5.0% | 5.0% | 4/4 | 1008 | 1003 |
| 11 | 1 | 1 | 0 | 5789 | 5760 | -29 | 13.34 | 13.31 | 4.6% | 4.6% | 5/5 | 963 | 958 |
| 12 | 0 | 2 | 3 | 5124 | 5092 | -32 | 13.64 | 13.55 | 4.0% | 4.0% | 4/4 | 1023 | 1017 |
| 13 | 0 | 1 | 4 | 4642 | 4606 | -36 | 13.20 | 13.13 | 3.4% | 3.4% | 4/4 | 926 | 919 |
| 14 | 1 | 1 | 3 | 6161 | 6120 | -41 | 13.14 | 13.05 | 4.3% | 4.1% | 5/5 | 1025 | 1018 |
| 15 | 5 | 1 | 2 | 4617 | 4547 | -70 | 14.13 | 14.01 | 4.0% | 4.0% | 4/4 | 922 | 908 |
| 16 | 2 | 1 | 3 | 4475 | 4404 | -71 | 14.13 | 13.95 | 3.5% | 3.2% | 4/4 | 893 | 879 |
| 17 | 3 | 1 | 2 | 4677 | 4582 | -95 | 14.10 | 13.89 | 4.2% | 4.0% | 5/5 | 778 | 762 |
| 18 | 3 | 0 | 2 | 3460 | 3341 | -119 | 13.70 | 13.39 | 3.6% | 3.6% | 2/2 | 1151 | 1111 |
| 19 | 2 | 0 | 1 | 5768 | 5746 | -22 | 14.50 | 14.44 | 4.5% | 4.3% | 5/5 | 959 | 956 |
| 20 | 3 | 1 | 1 | 5756 | 5627 | -129 | 13.52 | 13.37 | 3.5% | 3.3% | 6/6 | 821 | 802 |
| 21 | 4 | 0 | 1 | 6125 | 6011 | -114 | 13.99 | 13.86 | 4.1% | 4.2% | 5/5 | 1019 | 1000 |
| 22 | 2 | 0 | 1 | 6561 | 6521 | -40 | 14.18 | 14.09 | 4.1% | 4.1% | 6/6 | 936 | 930 |
| 23 | 1 | 0 | 1 | 4895 | 4875 | -20 | 14.24 | 14.18 | 3.2% | 3.2% | 4/4 | 977 | 973 |
| 24 | 1 | 1 | 4 | 4683 | 4584 | -99 | 13.98 | 13.77 | 5.7% | 5.1% | 4/4 | 934 | 914 |
| 25 | 0 | 1 | 2 | 4661 | 4651 | -10 | 13.80 | 13.77 | 3.0% | 3.0% | 4/4 | 930 | 928 |
| 26 | 0 | 0 | 2 | 4684 | 4667 | -17 | 13.82 | 13.81 | 5.3% | 5.3% | 4/4 | 934 | 931 |
| 27 | 2 | 0 | 0 | 4547 | 4498 | -49 | 13.70 | 13.59 | 3.6% | 3.3% | 4/4 | 907 | 897 |
| 28 | 2 | 0 | 1 | 4376 | 4341 | -35 | 14.08 | 13.97 | 4.5% | 4.2% | 4/4 | 873 | 866 |
| 29 | 3 | 0 | 1 | 5028 | 4999 | -29 | 13.49 | 13.44 | 4.3% | 4.0% | 4/4 | 1003 | 998 |
| 30 | 1 | 0 | 0 | 4868 | 4853 | -15 | 14.29 | 14.24 | 3.5% | 3.5% | 4/4 | 971 | 968 |

Lane totals (formula_metrics on ch1–30): words 153,110 → 151,859; sentences 10,996 → 10,967;
sentence mean 13.92 → 13.85; ≥40-word share 4.1% → 4.0%; ≤5-word share 27.3% → 27.3%;
words per scene 956.9 → 949.1; 130 scene breaks before and after.

Reading the metric columns against the brief:

- **Every chapter that was inside 13.3–14.2 is still inside it.** The low edge: ch11 13.31, ch3 13.33,
  ch20 13.37, ch18 13.39.
- **ch10 (named outlier) moved inward**, 15.75 → 15.67. ch5, ch6, ch19, ch23 and ch30, which sat
  above the range, also moved inward (ch23 is now inside it at 14.18); ch8 is unchanged at 14.26.
- **Three chapters that were already below 13.3 went slightly lower:** ch13 13.20 → 13.13,
  ch14 13.14 → 13.05, ch9 13.02 → 13.01. These are the clause cuts of Priority 3 (hands) in chapters
  of short speech. I did not join sentences to pull the number back. See ruling 2.
- **≥40-word share:** no chapter crossed 4.5%. The five that were above it at baseline are unchanged
  or lower (ch5 4.7, ch6 4.7, ch10 5.0, ch11 4.6, ch26 5.3 unchanged; ch24 5.7 → 5.1).

## 4. Checks (movements 1–4)

| Check | Result |
|---|---|
| `ed.sh overlap` M1–M4 | **0 unprotected** in all four; protected runs 17 / 15 / 28 / 36, the same as baseline |
| `ed.sh gates` M1–M4 | **0** reader-standard, **0** metadata, **0** modern-register hits in all 30 chapters |
| `sweep_probe.sh … 1 4` | Movement totals unchanged: skeleton 1 / 2 / 2 / 4%, close 13 / 19 / 22 / 22%. Skeleton unchanged in every chapter. See the note below for two chapters |
| Protected text | **PASS** on seven position and identity checks (below) |
| Season / month / weekday, metric units, "his Path" for Cael, new names | None introduced. The three "spring" hits (a water spring, a mechanical spring) and six "his Path" hits (Brom, Seln, a Force) are the baseline's own and unchanged |

**Probe note.** The printed "close" share moved by one point in six chapters: down in ch4, ch15,
ch22 and ch28; **up in ch17 (18 → 19%) and ch21 (22 → 23%)**. In those two the number of close
sentences is exactly what it was (39 and 59). The share rose because I cut sentences the probe does
not count as close (the glosses), so the same count is divided by fewer sentences (212 → 208;
265 → 261). I checked this per scene with the official probe (`laneA/probe_scenes.sh`): **no scene
of the 160 has more close or skeleton sentences than at baseline**, and across the lane close
sentences fell from 1,251 to 1,235 while skeleton stayed at 168.

Getting there took one repair round worth knowing about: the first per-scene run showed ten scenes
with one more "close" sentence each. In every case a sentence I had shortened now sat nearer some
short source sentence by the probe's ratio. I tested each on a trial copy (`laneA/trial.py`, which
runs the official probe and prints only counts), then re-composed five (ch13:229, ch17:15, ch18:137,
ch19:141, ch26:93), shortened one below the probe's floor (ch21:285) and restored four to baseline
(ch5:35, ch10:77, ch22:173, ch29:89). Lane B may want the same per-scene check.

**How the protected text was verified** (`laneA/verify_protected.py`, output in
`laneA/verify-protected.out`; it reads only `pre-lanes/`, `manuscript/`, `protected-patterns.txt`
and `BOOK_MAP.md`):

1. All 51 patterns in `protected-patterns.txt`: the 22 that fall in ch1–30 match the same number of
   times before and after.
2. Every italic segment (logs, letters, slips, ledger lines, documents): 350 segments, identical as
   a multiset in every chapter.
3. All 27 "Deployment since the Line" lines identical and in order (none → one).
4. All speech: the 33,973 words inside quotation marks are the same words in the same order in
   every chapter. Two speeches were joined where a hand beat between them was cut (ch2:241,
   ch26:89); no spoken word changed.
5. BOOK_MAP §10: of its 287 quoted or italic units, the 91 that stand in ch1–30 all stand unchanged.
6. By position: 1,958 tokens of ch1–30 lie inside a §10 unit or a pattern match; none of the 133
   changed hunks deletes, replaces or splits one.
7. Numbers: no primary count, day, date, distance or sum changed. Some cut callbacks carried a
   back-reference to an earlier day or count that is still stated where it happened (ch7:157 "the
   fourteenth day"; ch15:53 "the ninth day and the forty-ninth"; ch15:185 "the fifty-ninth night";
   ch21:91 "seven narrowings"; ch27:255 "the fifth day … the fifty-third"). ch18:135 keeps its
   "thirty". The script lists every number word inside removed text in `verify-protected.out`.

## 5. Declined, and why

- **ch2:149 and ch24:25** are named in the brief as double looks to recast, but both are Pike's own,
  and the brief also says to keep Pike's rereading. I left ch2:149 (it founds the signature) and kept
  the double look at ch24:25 in fewer words ("He looked, twice over, at…"), which also takes a
  50-word sentence under 40. ch11:321 (the steading's woman over Seln) is recast as asked.
- **All speech and all italic text** left alone, including the hand beats that sit inside protected
  exchanges.
- **The ford (ch10) and the collapse (ch19):** no action shortened; clause-level callbacks only.
  ch19:37 "That was what he remembered" and ch19:255 "That was how it seemed" stay: removing either
  sentence lifts that chapter's ≥40-word share past 4.5%.
- **Glosses kept on purpose for a 13-year-old's one pass:** ch30:211 (what the den under the floor
  means), ch28:135 (the three things now on one line), ch28:235 (what a stake at the far end of a
  measure tells you), ch20:165 and ch20:343–345 (the first question; she is not an instrument),
  ch29:219–229 and :243–309 (his test and his silence).
- **Motif uses left as designed:** healing contact and every asking; Pike's board; Cael's log and
  "rent"; Karis's measurements and counts; Seln's report idiom; Brom's arithmetic; Teague's pricing;
  the "nine hands" figure; "since he could no more have helped it than breathing" at ch16:251 (its
  repeat at ch24:145 is the one cut).
- **ch24:251** (the "account was square" paragraph) is ledger gloss I would thin, but it quotes
  Pike's line in italics; I left the paragraph whole.

## 6. Reserve — found, deserving, not applied

Held back to stay on the brief's numbers, or because the edit failed a metric or the probe. Line
numbers are the baseline's.

**Priority 1.** To keep the cap of 45 and put the weight where the brief asks, twelve early edits
were applied and then restored to baseline; they head this list.
- Restored: ch1:29 "which was the log's word"; ch2:37 "as the courier had looked at it"; ch3:87 "as
  Cael had known he would"; ch3:237 "which was the whole of Brom's Path"; ch4:111 "as she had read
  over it since Ardenmere"; ch5:221 "That was the method."; ch5:255 "as he had learned to do on sixty
  feet of oak"; ch6:73 "a sound like the wheel had made"; ch8:145 "the face that he had worn to count
  his posts"; ch9:15 "as she had stood there once with a lantern"; ch10:89 "as she had counted to
  ninety"; ch12:221 "as he had gone through the other one". Also ch11:91 (the "east tier of a yard"
  callback), restored because the cut took ch11 under 13.3.
- Never applied: ch5:189; ch5:227; ch8:251; ch10:37; ch10:121 "That was the whole of what it was
  doing."; ch11:73; ch11:221; ch11:331; ch12:95; ch12:321; ch13:341; ch15:5; ch17:75; ch17:205;
  ch18:67 and ch22:255 "That was the first thing"; ch19:37; ch19:255; ch21:183; ch23:135; ch23:209;
  ch24:133; ch25:37; ch25:77; ch25:129 "Cael knew the look of it…"; ch26:103 (the noun and six
  numbers, a near repeat of ch7:293); ch26:197; ch26:207; ch26:251; ch27:19; ch27:73; ch27:191;
  ch29:21; ch29:191.
- The single loudest survivor is "the east tier of a yard": seven uses in the lane; two cut
  (ch23:69, ch29:17), five stand (ch1:329, ch5:223, ch11:91, ch13:199, ch15:67).

**Priority 2.** ch5:35 and ch10:77 (applied, restored: probe); ch6:131; ch6:195; ch11:247; ch13:39;
ch13:259; ch21:81; ch23:13; ch23:71; ch27:65 (Lira reads a letter twice with her lips, the third
such look; the two earlier ones, ch6:177 and ch15:11, are cut); ch27:79; and "a breath longer than
the [answer / words / line] needed" at ch15:93, ch25:153 and ch29:49.

**Priority 3.** ch22:173 "saw him put it by" and ch29:89 Seln's "hands behind him" (applied,
restored: probe); ch30:117, the same Seln posture. That posture stood ten times in the lane; five are
cut (ch14:175, ch15:103, ch16:17, ch24:227, ch28:229) and five stand (ch13:237, ch27:159, ch29:89,
ch29:301, ch30:117; the "for once" at ch27:207 needs at least the early ones). Hand
beats inside speech, left because cutting them joins two speeches: ch3:25, ch9:71, ch13:309, ch16:39,
ch17:245, ch18:145. ch23:123 "He entered it all the same."

## 7. For a coordinator ruling

1. **Probe, ch17 and ch21.** The printed close share is one point higher in each, with no close
   sentence added (section 4). If "does not rise" must hold for the printed figure, three cut
   sentences in ch17 and two or three in ch21 would have to go back; I advise leaving them, since
   they are the lane's clearest cases of narration restating a spoken finding.
2. **ch13 and ch14 means.** Both were below the working range before the pass and are 0.07 and 0.09
   lower now. Restoring the hand cuts would undo Priority 3 there; joining sentences would be
   surgery for a number. I left them and report them.
3. **Pike's double looks named in the brief** (ch2:149, ch24:25): handled as "keep Pike", described
   in section 5. Say if you wanted them recast outright.
4. **Distribution of Priority 1.** 32 of 45 are in ch15–22 and ch27–30. If you would rather have the
   twelve restored early edits as well, they are listed and each is a one-clause cut; the lane would
   then stand at 57.

## 8. Joins for a second ear in the listening proof

- **ch20:73–77.** With the gloss gone, two of Lira's speeches follow each other; the second carries
  "said Lira presently".
- **ch17:135–139.** The slab falls and the next sound is Karis: "What did you see?"
- **ch21:243–247.** Oryn's "It's who I don't know about." runs straight into "Karis had waited as
  long as she was able."
- **ch24:201–205.** The three things on the oak, then Lira's "Why's it under your stone?"
- **ch2:241 and ch26:89.** One speech each where a hand beat was cut and the quotation now runs on.
- **ch18:55–59.** "It was five feet nine." / "He had expected nothing else." / "They took her through
  an inch at a time."
- **ch15:251–253.** The slope, then "Can it be done?"
- **ch22:125.** "He did not say it. He had no right to the sentence."
- **ch1:197–201.** The log, "Under it he added the other. It was getting to be a habit.", the
  Deployment line.
- **ch24:25.** "He looked, twice over, at a strange cart with three boxes on it…"
- **ch21:285.** "The fire ticked. Lira was watching the healer."

## 9. Every edit

Baseline line numbers. "…" inside a cell joins the parts of one edit. Full context is in
`laneA/diff-NN.txt` and `laneA/edits-worddiff.tsv`.

| ch:line (baseline) | Pri | removed | put in its place |
|---|---|---|---|
| ch1:51 | P3 | box, and rested there. | box. |
| ch1:61 | P1 | woke." That was fair. He | woke." He |
| ch1:197 | P2 | didn't.* He looked at the last line a while. Then … other, which | didn't.* Under it … other. It |
| ch1:241 | P2 | it at once, | it, |
| ch2:27 | P2 | after a while | (cut) |
| ch2:57 | P2 | saw it almost at once, and | (cut) |
| ch2:195 | P2 | no longer than a breath, | (cut) |
| ch2:241 | P3 | why." He turned his big hands over. "And | why. And |
| ch3:13 | P2 | spoke at once, | spoke, |
| ch3:91 | P2 | round, and he went on looking at it for some time. "There's | round. "There's |
| ch3:145 | P3 | sight, and his hands hung between his knees. "We | sight. "We |
| ch3:163 | P2 | fire for a while, | fire, |
| ch4:203 | P2 | along his fence once more, and then | (cut) |
| ch4:265 | P2 | himself for a moment, | himself, |
| ch5:5 | P1 | off, as they had kept forty yards behind three carts on a road. | off. |
| ch5:235 | P1 | That was worth having, … it was all that he had. | He had that much, … no more. |
| ch6:35 | P3 | what that cost her, and it was a good deal more than a pencil had. The | the effort. The |
| ch6:105 | P2 | the same that she had given him over a lantern, | (cut) |
| ch6:137 | P1 | is.* That was the form, and it | is.* The form |
| ch6:177 | P2 | twice | (cut) |
| ch7:89 | P2 | it for the space of a breath, | it, |
| ch7:157 | P1 | twice, with the same look that had followed him down the meadow on the fourteenth day. "Same | twice. "Same |
| ch7:255 | P1 | map. That was all. Nobody | map. Nobody |
| ch7:345 | P3 | entered | marked |
| ch7:371 | P1 | shut. That was the item he … on. He | shut. He … on that item, and he |
| ch8:139 | P1 | river. That was new as well. On | river. On |
| ch8:171 | P2 | it for some time. "Thirteenth | it. "Thirteenth |
| ch8:265 | P3 | up with her hands on her hips. | up. |
| ch9:45 | P3 | it. Cael counted | it. There were |
| ch9:157 | P2 | for some time that | it |
| ch10:85 | P3 | all, and he put that by to think about when he had the time. They | all. They |
| ch10:217 | P1 | discharge, as she had felt it a hundred times across a harness room; | discharge; |
| ch10:285 | P3 | let it stand. "Four | gave way. "Four |
| ch11:169 | P1 | length. That was how it had turned beside a white stone, by the reading of the ground, and that was how it tur… | length. It |
| ch11:321 | P2 | once, and then again more closely, | (cut) |
| ch12:163 | P2 |  … at once, … then | had … too fast, …  |
| ch12:215 | P2 | twice, | (cut) |
| ch12:285 | P3 | it, and she entered it in her head beside the rest. | it. |
| ch12:329 | P3 | something. That was what the other way cost, and she made herself price it honestly, for it | something. It |
| ch12:357 | P3 | tail-board with her hands in her lap, | tail-board, |
| ch13:79 | P3 | afterward, and had put it by for the evening. The | afterward. The |
| ch13:93 | P2 | moved at once. | moved. |
| ch13:129 | P3 | tonight." Cael thought that it … that it had been paid for at a ford; and he | tonight." It … Cael |
| ch13:191 | P3 | asked. Seln looked at his hands. Cael | asked. Cael |
| ch13:227 | P3 | plank. He counted them twice, since eleven … had … been able to | plank. Eleven … could …  |
| ch14:13 | P2 | for a breath … side, as she had looked at him across a wash. |  … side. |
| ch14:175 | P3 | halting-ground with his hands behind him, | halting-ground, |
| ch14:179 | P1 | with an expression he had not seen on her since a barn. "It's | hungrily. "It's |
| ch14:233 | P3 | him with her white hands on the stone. "I | him. "I |
| ch14:371 | P3 | bar with her hands on her hips. "It | bar. "It |
| ch15:11 | P2 | reading a second time, | (cut) |
| ch15:53 | P1 | right, as he had gone along it on the ninth day and on the forty-ninth. There | right. There |
| ch15:55 | P1 | read, as he had once sorted a board in Ardenmere by what each card would cost him. | read. |
| ch15:59 | P1 | plainest, which was that | plainest: |
| ch15:71 | P3 | entered … as a want, | did not hide … from himself, |
| ch15:103 | P3 | had his hands clasped behind him and | stood with |
| ch15:185 | P1 | lip, as they had on the fifty-ninth night. Seln | lip. Seln |
| ch15:251 | P1 | it. Cael knew that face. He had seen it turned on a wagon in a wash with three wheels and a river coming. "Can | it. "Can |
| ch16:17 | P3 | fingers, and he stood with his hands behind him. "I | fingers. "I |
| ch16:41 | P3 | slope for a long count. | slope. |
| ch16:163 | P3 | cost him something | was hard |
| ch16:191 | P1 | there. He had kept a log through every term since his Kindling, and all of it had been called watching; and it… | there. "What's |
| ch16:237 | P1 | floated, as he had said she would. | floated. |
| ch16:243 | P2 | still for as long as it would have taken to count ten. | still. |
| ch17:15 | P1 | leader, and he did it … thinking, as he had done it at a ford with the light going. | leader … thinking. |
| ch17:43 | P2 | ring for some time. "I | ring. "I |
| ch17:135 | P1 | went. He turned that over while the last of the plates ran out below. He had been watching one animal, on purp… | went. "What |
| ch17:237 | P3 | paid for. He | struck off. He |
| ch17:239 | P1 | spoke, which was his way of saying that the thing bore. "The | spoke. "The |
| ch17:259 | P3 | with his big hands hanging between his knees, | (cut) |
| ch18:57 | P1 | else. But he understood, getting up, what she had asked of him at the slab two days before: a hand that might … | else. They |
| ch18:81 | P1 | cart as he had looked at a rung of ash in a barn. | cart. |
| ch18:135 | P3 | up. He did not need to count what was on that shelf, and he counted it all the same, and it came to thirty. Se… | up, with thirty grey heaps along it. Seln sat beside |
| ch18:137 | P3 | laid, and … was sitting beside it with his hands on his knees. He | that … had laid. He |
| ch18:161 | P1 | ledge as he had seen her look along a painted floor at Norhold before the bell. | ledge. |
| ch19:23 | P3 | lifted and his hands quite still on the shaft, | lifted, |
| ch19:141 | P1 |  … as he had spent a breath on a gravel bar, | the whole of …  |
| ch19:249 | P1 | colour, as she had read a sprung floor. She | colour. She |
| ch20:35 | P3 | He counted the boxes a second time, since they had cost what they had cost. | (cut) |
| ch20:73 | P1 | there." He knew what she was telling him. He had given her the order of it at the wall's end, the ledge and th… | there." "Karis |
| ch20:149 | P1 | floor, as she had once lifted it in a valley full of frogs. "On | floor. "On |
| ch20:291 | P2 | answered at once. | answered. |
| ch20:367 | P1 | He had been a good many words in his time. He had been a flag on a board and a level on an advisory, and one w… | (cut) |
| ch21:91 | P1 | It had asked at every sill and coping since a river, and at seven narrowings, and here | Here |
| ch21:243 | P1 | about." Cael turned that over. He had counted a great many things in his life, strides and fighters and watche… | about." Karis |
| ch21:253 | P1 | open. She looked as she had looked in a cart-yard, when a woman dropped three sentences in passing and drove a… | open. "Then |
| ch21:285 | P1 | looking at her with an expression that Cael had not seen on her since a sheet of sailcloth by a hearth. "Did | watching the healer. "Did |
| ch21:315 | P3 | her hand on … mule's shoulder. It |  … mule. It |
| ch22:125 | P1 | it, and it was not like the things he had left unsaid at a fire; he was not sparing himself. … sentence, and t… | it. … sentence. She |
| ch22:133 | P3 | once, as to a thing entered. | once. |
| ch22:319 | P1 | finger, as he had nodded once from a sill. | finger. |
| ch23:69 | P1 | now, as he had had it from the east tier of a yard, watching a good pair work. | now. |
| ch23:113 | P3 | and priced it | (cut) |
| ch24:25 | P2 | looked … arm; and then he looked at all of it a second time, as he did. "You're | looked, twice over, … arm. "You're |
| ch24:101 | P3 | with his two hands hanging open, | (cut) |
| ch24:145 | P3 | since he could no more have helped it than breathing, | (cut) |
| ch24:201 | P1 | cask. None of them had been meant for the others' company. The woman with the barley had never looked at her h… | cask. "Why's |
| ch24:227 | P3 | end with his hands behind him, | end, |
| ch24:249 | P3 | with his hands hanging | (cut) |
| ch25:49 | P3 | entered | took |
| ch25:125 | P3 | with both hands on the shut notebook, | (cut) |
| ch25:179 | P2 | money." For some time the | money." The |
| ch26:89 | P3 | out." He looked at his own hands. "*Quieter.* | out. *Quieter.* |
| ch26:93 | P3 | and paid the rent on it, and had never yet spent it. "Read | unspent. "Read |
| ch27:151 | P1 | east, with an expression that he knew. She had been given a rule, and under the rule there had once been a fin… | east. "The |
| ch27:255 | P1 | as it had come up beside a turf fire on the fifth day and at a ford on the fifty-third, | (cut) |
| ch28:131 | P1 | had asked about doorways for a year, and about every sill and rim on a mountain; it | (cut) |
| ch28:209 | P1 | weight, as she had once read out the width of a shelf. "A | weight. "A |
| ch28:229 | P3 | stood with his hands behind him and | (cut) |
| ch29:17 | P1 | from the east tier of a yard, | (cut) |
| ch29:49 | P3 | nine, with its rent paid; | nine; |
| ch29:133 | P1 | as it had stood up once at the mouth of a ledge, | (cut) |
| ch29:133 | P1 | hissed. That was the whole of it. He | hissed. He |
| ch30:193 | P1 | side, as Cael had seen him read a wet margin beside a pool on a mountain. "This | side. "This |

## 10. Files in `state/completion/laneA/`

Baselines and results: `base-*` and `after-*` (overlap, gates, probe, per-scene probe counts, counts,
metrics); `diff-NN.txt` (each chapter against `pre-lanes/`); `edits-worddiff.tsv`; `edit-list.md`;
`tally.tsv`; `words-perch.md`; `metrics-perch.md`; `verify-protected.out`.
Read-only helpers: `count.sh`, `worddiff.py`, `verify_protected.py`, `probe_scenes.sh`, `trial.py`
(the last two only run the official probe; `src-m*.paths` holds the source file paths the packets
name, no source text). None of them writes to the manuscript.
