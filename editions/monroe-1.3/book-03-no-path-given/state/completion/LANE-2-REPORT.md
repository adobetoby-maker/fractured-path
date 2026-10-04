# Book 3 — completion pass, Lane 2 report (chapters 32–61)

Author: Claude Opus 5.5 (O'Connor 1.3 seat, writing as Monroe Jackson), 2026-10-02 to 10-04.

**Brief.** `PASS-BRIEF.md`, Lane 2.

**Read first:**
- `whole-arc-read.md` §§3, 4 and 9;
- `whole-arc-notes.md`;
- `LANE-1-REPORT.md`;
- O'Connor `VOICE.md`;
- `EDITION_BRIEF.md`;
- `BOOK_MAP.md` §9;
- `protected-patterns.txt`.

**Files edited.** `manuscript/chapter-32.md` … `chapter-61.md` and this report. Nothing else was touched. No git command was run. The coordinator's line fixes (§8, fixes 6–13 and 19 in this range) were left as they stood.

**Method.** Every change was made by reading the paragraph and hand-writing the replacement, applied as an exact single-match Edit. No sed, regex or script touched prose. Before work began, ch32–61 were snapshotted to the session scratchpad (`L2/before/`), and every before/after figure below compares that snapshot with the finished files. The helpers, all read-only, live in `L2/`:
- `count2.sh`, Lane 1's grep counts;
- `perch.sh`, per-chapter counts;
- `closecheck.py`, Lane 1's skeleton method re-pointed at the M5–M8 source chapters.

**Who did what.**
- The lane author did ch47–53, including both Priority 2 cutaways and the ch51 stillness.
- Same-seat workers (Opus 5.5, with a shared brief and keep-list in `L2/WORKER-BRIEF.md`) did Priority 1 in ch32–39, ch40–41, ch42–46 and ch54–61.
- The first set of workers was stopped by the weekly usage limit partway through. At that point ch32–39, ch42–45 and ch54–58 were done, and ch40–41, ch46 and ch59–61 were untouched.
- After the reset, the lane author re-read every word-diff from the stopped workers for broken or half-finished paragraphs. None was found. Two new workers then did ch40, ch41 and ch46, and ch59–61.
- The lane author reviewed all the diffs, made the corrections in §6, and finished the depth sweep (§1, last paragraph).

## 1. Texture counts (grep, ch32–61, case-insensitive)

| Target | Before | After | Change |
|---|---|---|---|
| Words, ch32–61 (`wc`) | 148,910 | 146,173 | −2,737 |
| **"the way" (every use)** | **171** | **107** | **−37%** |
| — with a generic subject | 36 | 22 | −39% |
| **"as if" / "as though"** | **136** | **87** | **−36%** |
| — "as if it/she/he/they had/were" | 58 | 36 | |
| "a long time" | 57 | 24 | |
| "a long moment" | 26 | 8 | |
| "for a moment" | 49 | 12 | |
| "for a while" | 46 | 10 | |
| "for some time" | 13 | 4 | |
| **Duration pads, total** | **191** | **58** | **−70%** |
| — "for a long time/moment/while" | 57 | 21 | −63% |
| **"found that"** | **39** | **1** | **−97%** |
| **"exactly"** | **123** | **69** | **−44%** |
| Document re-readings (the grep) | 42 | 29 | −31% (see below) |
| "a third time" | 15 | 7 | |
| "three times" | 32 | 32 | all counts or speech |
| "did not look up" / "without looking up" | 33 | 22 | |
| finger's / hand's width, hair's breadth | 26 | 16 | the Ember-test measures, ch40–41, are untouched |
| "a hair" | 18 | 12 | |
| "squared" | 14 | 13 | |
| "went (very) still" | 9 | 4 | |
| Oona: "whole (serious) face" | 7 | 1 | ch41, the §3 keep |
| Oona: "slate under her arm" | 10 | 5 | ch41 and ch59 kept |
| Brom's "did him for a laugh" | 1 | 1 | ch49, the §3 keep |
| the bread's "larger half" | 5 | 2 | ch39 (the rule) kept |
| "with great dignity/seriousness" | 5 | 0 | |
| "I'd think less of you" | 2 | 1 | ch32 kept (§6) |
| "patient as a gatepost" / "planted like a gatepost" | 2 | 0 | ch27 is the first |
| "the square/plain hand he kept" | 5 | 2 | ch36 and ch53, the §3 keeps |
| *Watched:* "like a" | 65 | 64 | |
| *Watched:* "as" | 850 | 801 | |

**Against Lane 1's depth (ch1–31).**

| Target | Lane 1 | Lane 2 |
|---|---|---|
| Duration pads | −69% | −70% |
| "found that" | −95% | −97% |
| "exactly" | −44% | −44% |
| "as if" | −38% | −36% |
| "the way" | −46% | −37% |
| Re-reads | about half | −31% by the grep |

Two targets are shallower than Lane 1's.

**"the way" (−37%).** The before count is "every use". In this half a large share of those uses cannot be cut:
- literal or route uses, about 18 ("all the way", "on the way", "out of the way", "by the way it had come");
- speech, about 15 ("the way it's meant to be used", "the way it was built to be used", "the way we'd made it", "the way you feel a step in the dark");
- similes inside the match (ch36) and the sittings (ch54–58);
- the P5 narration (ch61);
- the §3 first-figure keeps: the instructor's farmer (ch33), the reflection in a dark window (ch41), Brom's yard-search (ch52), Havel's carter and wheel (ch52), and Coss's measured-twice head-shake (ch50).

Of the explanatory, cuttable glosses, roughly two-thirds were cut or converted. The last pass converted five to "as" ("just as" where "as" could be heard as "while"). Those were glosses that earned their comparison (ch47, ch49, ch51, ch52, ch57); in the same pass two were cut outright (ch38, ch45), one cut by recasting the sentence (ch44), and two converted to "like" (ch37, ch55).

**Re-reads (−31% by the grep).** The grep over-counts in this half:
- negations ("did not read it again", "did not stop to read it twice");
- speech ("I read it three times looking for anything interesting");
- procedure that is the beat: Prynn's "Again" at the door (ch52), and Yorlan's provision read twice, which is hearing canon (ch54).

Narrative re-readings that were not the beat were cut to one reading, or to two where the second reading turns the scene:
- Prynn's notice: three readings → two (ch48);
- the inventory notice: three → one (ch43);
- Quenna's conditions: three → one (ch35);
- the find, "a third time … and then a fourth" → one more reading (ch51);
- Karis's finding: three → two (ch53);
- Karis's consent: four → one (ch32);
- Cael's page (ch38).

These are kept as the beat:
- the notice's "four … a fifth" (ch36);
- the deposition and Ilsev's query (ch49);
- Ilsev's third reading in the Havel cutaway (ch52, part of the cutaway plan);
- Brom's page "twice; a third reading was beyond him" (ch53);
- Hesk's letter (ch61).

## 2. Priority 2 — the two M7 cutaways

| Cutaway | Before | After | Change |
|---|---|---|---|
| ch47, the Havel coach and gate (the 2nd and 3rd scenes) | 1,304 | 1,100 | −204 |
| ch50, the Karis card cutaway (the 3rd and 4th scenes) | 2,817 | 2,555 | −262 |
| ch47 whole chapter | 4,395 | 4,132 | −263 |
| ch50 whole chapter | 5,007 | 4,698 | −309 |

No scene breaks were added or removed (all 30 chapters keep their scene-break counts).

**ch47, Havel.**
- The case, Yorlan, Ilsev and the asleep records officer are compressed into four paragraphs.
- The case's contents list is kept, and so is the sand-glass, which the hearing uses.
- "Every recorder carried one" and "heavier than it looked" are cut.
- Yorlan's three hearings and his never raising his voice are kept as one sentence.
- "It was an academy, then, though not much of one" is folded into the new-building joke.
- At the gate:
  - the inn-papers sentence is shortened;
  - the provost's "as if neither needed much introduction" is cut;
  - "He walked on a few paces" is cut;
  - the step and the wall view are recast tighter.
- Kept verbatim: both notebook entries (*File and subject do not match. Marker origin not found. Noted.* and *Asked. Told to stop. Stopped.*); "a boy of fifteen"; "Assessor Havel," … "Recording officer now, I see. You've a new grade."; "It suits you. You were always careful."; Yorlan's two questions with "The record is public."; and "Noted".
- Also kept: the met-once corridor line, and "one short reply in that hand by heart".
- The Cael-side wall scene is a different viewpoint on the same moment and is untouched apart from Priority 1.

**ch50, Karis.**
- The card system's five places are now one sentence; the dot, ring and struck-ring marks are kept whole.
- The waystation runs paragraph is compressed, keeping:
  - "how many sacks of oats";
  - the nineteen-year weather log;
  - "And, sometimes, what they were.".
- The clerk-learning paragraph is merged with the naming. All four epithets are kept whole (Long Tails, the Blotter, Small Hand, the crosshatched sevens).
- The clerks' arrival is tightened.
- "She stood a moment longer…found that she minded" is recast.
- The overlap explanation is compressed:
  - the weather log's last line, the double date and the accession register are kept;
  - the three-step count is now one sentence, and Prynn's silent check is kept.
- The "date, not the reason" paragraph loses its student simile and is folded to one denial sentence. It still says the date means nothing about anyone who passed through, which is the knowledge boundary.
- The Ternhall paragraph is compressed. The partner stays unnamed and "her hand on a wall, wanting the floor" is kept.
- Prynn's count/marks/sign is kept whole, and so is "It tasted like Brom.".
- The third clerk's sentences-not-boxes, the margin correction, "four volumes … a dot in each corner", and the last paragraph opening the next volume are all kept.

**The aim.** It was that the deposition (ch49) and the find (ch51) not be separated by two still chapters. Together the two cutaways and ch48 lose about 540 words.

## 3. "Went still, as she went still before an ignition"

- **ch30** (the first, Lane 1's keep): untouched.
- **ch37:** the word-for-word repeat "Karis went still, as she went still before an ignition, all of her listening at once." is now "Karis laid her grey fingertips flat on her knees and kept them there." That is Karis's own register: the grey fingertips are her cost (ch28), shown on the morning she learns the fragment came from her.
- **ch51:** this edition has no word-for-word repeat here. The stillness at the find was a long gloss, "All of her had gone quiet at once … He had seen her go still like that once before". It is recast without "still": "the eyes and lips and breath had all stopped together" … "He had seen her stop like that once before, in the formal yard". The match callback is kept.
- **ch52:** at box seven, "Karis go still: not the stillness of the night before, but a smaller one" is now "Karis hold a breath and let it go again".

## 4. Changelist

"Conv." means a "the way" or "as if" simile was recast as "as" or "like", with the image kept.

- **ch32:**
  - Cut:
    - Hobb's gatepost;
    - "with great dignity";
    - the plain-hand line;
    - Karis's consent re-reads;
    - Lira's triple reading (now one slow reading);
    - six pads;
    - "found that";
    - five "exactly".
  - Kept: P18 exact, "Show enough to pass. Bank everything that matters.", and Cael's "I'd think less of you".
- **ch33:**
  - Cut:
    - five pads;
    - three "exactly";
    - Brom's meal "as if";
    - the lattice re-statement.
  - Kept:
    - the instructor's farmer and stray dog (the §3 keep);
    - the first "trap … foot that springs it";
    - "Never join what you can still move" and "Stop her before she composes".
- **ch34:**
  - Cut:
    - three pads;
    - two "exactly";
    - "found that" ×2;
    - Lira's "went very still";
    - "a hair";
    - the drawn circle's hand's width.
  - The bag-drill exchanges are untouched.
- **ch35:**
  - Quenna's conditions are now read once.
  - Cut:
    - "found that" ×3;
    - "with great seriousness";
    - Oona's "great care";
    - two "did not look up";
    - pads.
  - Kept: every fact (rota, "walk out … on your own feet", the honey thief, the barley clause, "Fight me … don't catalogue").
- **ch36:**
  - The match is untouched as one unbroken scene: every exchange, landing beat and simile, P1 with its "four … a fifth" reading, and the log. Only the framing was touched.
  - Framing cuts:
    - the banked-coals and water-round-a-rock tails at breakfast;
    - two pads;
    - "found that";
    - "beats like a second heart" and "not a hair further", both after the halt.
  - The "hand he kept" (a §3 keep) is untouched.
- **ch37:**
  - The ignition-stillness repeat is rewritten (§3).
  - Cut:
    - six pads;
    - three "exactly";
    - the stone-he-never-agreed simile (which echoed the source);
    - the letter-in-your-coat and light-at-a-new-angle similes.
  - Conv. ×1 (the craftsman's tools).
  - Kept: P2 and P3 exact, the coordinator's "I won't ask. I have my ideas.", Naveth's "age me", and the warm fragment.
- **ch38:**
  - Cut:
    - "found that" ×4;
    - five pads;
    - the Ternhall-partner "the way a person speaks a fraction early" (the partner is still present and still unnamed);
    - the note re-read from three to two;
    - one result-checking gloss.
  - Kept: the paragraph, the first notebook and the supplementary entry exact.
- **ch39:**
  - Cut:
    - five pads;
    - "with great dignity" (now "solemnly");
    - the plain-hand line;
    - Brom's gatepost;
    - Gerda's clause simile;
    - Prynn's "square to the edge, exactly".
  - Kept: the bread rule and its "larger half", the §9.2 log line and completion, Brom's lines, and the three clean days.
- **ch40:**
  - Cut:
    - all seven pads;
    - "found that" ×4;
    - five "as if" glosses (the pump trough, the chalk line, the mark scored in wood, the list, and one more);
    - the hearth "the way";
    - Brom's "without looking up";
    - "with great dignity";
    - the plain-hand line.
  - Kept: every hair, finger's-width and hand's-width measure, 104/109, "a spark", "You're pale. Sleep tonight." and the mother's shoulders.
- **ch41:**
  - Cut:
    - five pads;
    - five "exactly";
    - "found that" ×2;
    - the repeated "as if told where to put them";
    - "the way weather comes".
  - Kept:
    - "A year and some", Anchor and Copper, "It's ordinary", and Oona's whole face and slate (the §3 keeps);
    - the Coss cutaway whole: the approval timing, the credential, and the daughter letter "going up into the hills".
- **ch42:**
  - Cut:
    - seven pads;
    - two "exactly";
    - Karis's pressing-hands "as if";
    - the aide's "as if";
    - the scale simile.
  - Re-composed three sentences that had turned source-close (§5).
  - Kept: "'Warden' was never a town title", Coss's "You were fourteen … This is also the job." and the coordinator's Quenna fix.
- **ch43:**
  - The notice is read once, and its last line again.
  - Cut:
    - Oona's whole face and two slate tags;
    - Naveth's squaring gloss and "as though it might lift";
    - four pads;
    - two "exactly";
    - the opponent-declaration "as if".
  - Kept: the notice text, "This is your enrollment, not mine to trade.", Naveth's lever, and "He has it over *me*."
- **ch44:**
  - Cut:
    - four pads;
    - two "as if";
    - Karis's square-to-the-page;
    - Prynn's and the narrator's "without looking up" ×1;
    - the noise-has-stopped gloss.
  - Kept: "a hope with a citation", the log "New opponent …", the READERS card, and "One thing, not two."
- **ch45:**
  - Cut:
    - Prynn's "went very still" gloss;
    - three pads;
    - "the larger half";
    - the stance simile;
    - Ilsev's citation gloss;
    - one re-read.
  - Kept: P15, Prynn's sixty-years line exact, the coordinator's two fixes, the gauntlet exchanges, and Brom's GAUNTLET column.
- **ch46:**
  - Cut:
    - seven pads;
    - four "exactly";
    - Gerda's clause simile;
    - the rotating seat's nod simile;
    - Oona's whole serious face and two slate tags;
    - Quenna's "did not look up";
    - the hand-he-kept line.
  - "Read it a dozen times" is now "could have said it with his eyes shut".
  - Kept: P17 ×2, "Spend it on purpose", "*I'm not going to argue my enrollment is valid.*", Hobb "three" / "Three times.", the files 9/6/11/4, and the sitting.
- **ch47:**
  - Priority 2, above.
  - Cut:
    - six pads;
    - "found that" ×2;
    - four "as if";
    - Quenna's "did not look up" (now "told it the rest").
  - Conv. ×2.
  - Kept: the outline read "from the top … again from the bottom" (the beat), Quenna's three rules verbatim, the drill, and Karis's "Four."
- **ch48:**
  - Prynn's notice: three readings → two.
  - Cut:
    - "as a man states the weather";
    - seven pads;
    - Brom's and Lira's "the way" tails;
    - two "as if".
  - Prynn's second "did not look up" is now "went on writing".
  - Kept:
    - the contest exchange by exchange;
    - "Every amendment is a confession";
    - the protected "Their code forgot …" / "takes my shelves";
    - the signed line per box;
    - "on a list can be counted";
    - the stub line exact;
    - the sickroom simile;
    - Karis's knife "as if she had done it before".
- **ch49:**
  - The deposition is untouched: every question and answer, "Three", "a classification question", "that's what a record is", "Four weeks", "No", the nine dashes, "the door the provision had", and Coss's "for some time" (speech).
  - Cut:
    - "found that" ×3;
    - six pads;
    - four "as if";
    - two Karis "the way" glosses;
    - "He did not hear anything, exactly".
  - Conv. ×3.
  - Kept: Brom's chest-laugh (the §3 keep), Ilsev's query (P16 shape) exact, and Havel's "read it twice" (the beat).
- **ch50:**
  - Priority 2, above.
  - Cut:
    - Coss's "as if reading a line off a sheet";
    - four pads;
    - "found himself";
    - Karis's squaring "the way";
    - "the way Lira counted the rumor market".
  - Coss's "I'd think less of you" is now "I'd have thought the worse of you" (§6).
  - Kept: the lending book, "eleven letters", "Five days.", "six places", the refused categories, "about four hundred years" and the hand on the wall.
- **ch51:**
  - The stillness is recast (§3).
  - The register re-read "a third time … and then a fourth" is now "He went through it once more before any of it would go in."
  - Oona: cut the slate ×2, her whole face (now "watched him all the way to the door"), "with great dignity", and "for some time".
  - Cut:
    - Edran's rail gloss;
    - the parting-crowd gloss;
    - the hair's breadth;
    - four pads;
    - "found that" ×3.
  - Kept:
    - P12 and the annotation exact;
    - Cael's older copy exact;
    - "*Shattered* is an editorial choice. The question is whose.";
    - the three copies read aloud;
    - "Custom isn't code";
    - the wind-on-the-page image;
    - "Neither of them said anything for a long time" (the find's landing beat).
- **ch52:**
  - Cut:
    - Brom's "whole face" (an Oona tag on Brom);
    - the hair-and-paper-knife gloss;
    - three pads;
    - four "exactly";
    - two "as if";
    - Lira's larger half;
    - the shoulder-after-a-bout and stance glosses.
  - The box-seven stillness is recast (§3). Conv. ×2.
  - Kept:
    - Yorlan's formula and "The panel notes it";
    - the fourteen openings;
    - the six places;
    - box seven with nine volumes;
    - "Fifty-three boxes … Four hundred and some";
    - "can't be unread by a cart";
    - the marbled line;
    - "Put them back yourself.";
    - the return and referral texts exact;
    - Ilsev's third reading;
    - "Not only me this time.";
    - "a hole in the world" and its answer;
    - "It amends";
    - "Find out. Tonight.";
    - Brom-as-Coss's "silent for a long moment, in the way Coss was silent" (the rehearsal).
- **ch53:**
  - Cut:
    - eight pads;
    - "found that";
    - Karis's second squaring;
    - Brom's weight-lift gloss;
    - one "exactly".
  - Karis's finding: re-read three → two. Brom's page: "read it twice … a third reading was beyond him".
  - Kept:
    - "Custom" / "Is not code";
    - forty-one;
    - Brom's page with its protected line;
    - "I won that bout";
    - "Findings to date …" exact;
    - the coordinator's records-line fix;
    - "This is real. Start from that.";
    - the log line exact;
    - the square hand (a §3 keep).
- **ch54–58** (the sittings):
  - Every exchange and landing beat is untouched, and Yorlan's formula is verbatim twice. The deposition read-back and its nine-count silence, P13, P15, P20, the pivot lines, the stipulation line, "Cite the schedule entry." / "There isn't one …" and the gavel are all intact.
  - Cut in framing, corridors, the recess and the Lira cutaway's narration:
    - about 15 pads;
    - "found that" ×8;
    - six "exactly";
    - Coss's "as if he were reading a line off a sheet" (now "evenly, with no paper in his hand");
    - two larger halves.
  - Kept: Lira's heel of bread "off a market stall" (ch54, the §3 keep), and the pauses that time the room.
- **ch59–61:**
  - Cut:
    - nine of ch59's thirteen pads;
    - "the way a good door shuts";
    - Oona's whole face;
    - the clerk's weather;
    - Wray's weather-board gauge variant;
    - "found that" ×3;
    - Lira's long moment;
    - the notice read twice.
  - Kept:
    - P14 verbatim and the gavel once;
    - Coss's five minutes;
    - Brom's page returned;
    - "correct form";
    - Oona's slate (the §3 keep);
    - the report and the struck daughter line;
    - the faceless desk;
    - Naveth's clerical-error lines;
    - clause one;
    - 93/95/94 and the letting-go;
    - P4, P5 (including its narration), P10, P11 and P19 (read three times, the beat);
    - the Vell letter and the box-seven count;
    - the last line.

## 5. Checks

**`ed.sh overlap`.**

| Movement | Unprotected runs | Protected runs |
|---|---|---|
| M5 | 0 | 7 |
| M6 | 0 | 5 |
| M7 | 0 | 12 |
| M8 | 0 | 19 |

All are unchanged from before.

**`ed.sh gates`, M5–M8.** reader_standard, metadata and modern are 0 in all 30 chapters.

**Skeleton probe** (`sweep_probe.sh book-03-no-path-given 5 8`):

| Movement | Before: skeleton / close | After: skeleton / close |
|---|---|---|
| M5 | 1% / 13% | 1% / 13% |
| M6 | 2% / 17% | 2% / 16% |
| M7 | 2% / 12% | 2% / 11% |
| M8 | 2% / 19% | 2% / 19% |

- No movement rose, and no chapter's percentage rose.
- Raw counts by `closecheck.py`: no chapter's skeleton or close count rose. Across ch32–61 skeleton went from 124 to 118 and close from 929 to 875.
- The first closecheck after the stopped workers showed raw rises in six chapters: ch33, ch36, ch37 and ch43 (close +1/+1/+2/+1), and ch54 and ch55 (skeleton +1, plus ch54 close +1). The lane author re-composed each newly close sentence by hand and brought all six back to or below their before counts. About 40 sentences were re-composed across the lane in total.
- Eight sentences are still listed as NEW, all in chapters whose raw count fell. Seven score 0.35–0.38 against unrelated short source lines. The eighth is ch60 Brom's "… 'is under his desk.'" (0.52); the original tag scored 0.57 against the same source line, and the protected words dominate the score.

**Protected text.** 54 protected strings were grepped before and after: P1–P20 fragments, the §9.2 anchors, Yorlan's opening, "Fifty-three boxes", "forty-one", "nine dashes", "It amends", "Spend it on purpose", "a hope with a citation", "He fights like you" and the records line. All counts are equal except "I'd think less of you" (2 → 1, deliberate, §6). Every `protected-patterns.txt` pattern in range is unchanged, and scene breaks are unchanged in all 30 chapters.

## 6. Formula metrics (`formula_metrics.py`, ch32–61)

| Measure | Before | After | Working range |
|---|---|---|---|
| Words | 148,580 | 145,843 | — |
| Sentences | 11,231 | 11,188 | — |
| Sentence mean | 13.23 | 13.03 | 13–15.5 |
| Sentence median | 9 | 9 | — |
| ≤5-word share | 30.8% | 31.1% | up to ~34% |
| ≥40-word share | 3.7% | 3.5% | 2.5–4.5% |
| Paragraph median | 25 | 25 | up to ~30 |
| Words per scene | 917.2 | 900.3 | 850–1,050 |
| Flesch Reading Ease | 86.9 | 87.0 | — |
| Flesch–Kincaid grade | 4.43 | 4.36 | 3.5–6 |

**By movement** (sentence mean · ≥40 share · words/scene):

| Movement | Before | After |
|---|---|---|
| M5 | 13.00 · 4.0% · 1,028 | 12.83 · 3.8% · 1,013 |
| M6 | 13.01 · 4.2% · 907 | 12.78 · 3.9% · 887 |
| M7 | 13.08 · 3.6% · 862 | 12.83 · 3.5% · 838 |
| M8 | 13.89 · 2.9% · 878 | 13.76 · 2.8% · 870 |

**The lane as a whole** stays inside every working range.

**Sentence mean.** As in Lane 1, it drops about 0.2. Cutting a simile tail or a pad shortens its sentence, and nothing was joined to compensate, under "No scripted prose surgery". M5–M7 now sit at 12.8, just under the 13.0 floor, as Lane 1's M3 and M4 do.

**M7's words per scene (838).** This is just under 850, because Priority 2 took about 570 words out of ch47 and ch50 without touching a scene break, as the brief requires. I did not join sentences or move breaks to chase either number.

## 7. Flags for the coordinator

1. **The ch47 Havel tightening was done before the usage cutoff.** The cutoff note listed it as not done, but it was on disk at −204 in the cutaway. It was not redone; it is reported in §2.
2. **"I'd think less of you."** ch32 (Cael) stands as the last link of the chain ch3, ch17, ch32. ch50's Coss repeat, "If you'd stood behind my door with a glass to the wood for three weeks, I'd think less of you", is now "I'd have thought the worse of you". It is the same beat in Coss's register, and no later chapter quotes it.
3. **ch51 had no word-for-word ignition repeat in this edition** (see §3). The stillness gloss there and at box seven (ch52) was thinned instead.
4. **ch57, a worker's slip, reverted.** A worker had changed "as Karis had made him do eleven times" to "as he had practised it", which dropped a count. The lane author restored the original wording. The ch52 rehearsal sets the eleven ("she made him say the concession … eleven times"), and ch57's "flat, the way Karis had made him say it eleven times" pays it.
5. **ch40's "as if it were a mark scored in wood" is cut.** ch46's "like a mark scored in wood" (the D6 rings) is therefore now the first use. It was never a deliberate callback; restore ch40's if wanted.
6. **ch46's "Lira went very still" is now "Lira went quiet".** "He had known she would" still follows it correctly.
7. **"the way" at −37% and the re-read grep at −31%** are shallower than Lane 1's figures. The reasons are in §1. If parity is wanted, the remaining explanatory candidates are few and mostly first figures. I would not cut further without the owner's eye.
8. **Rhythm:** M5–M7 sentence means are now 12.8, and M7 words per scene is 838 (§6). These are meter-only and were not forced.
