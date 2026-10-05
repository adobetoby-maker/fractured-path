# CLOSE WITH LINE FIXES

Scope: one count correction in `manuscript/chapter-13.md` (`four bad nights` → `three bad nights`). No second manuscript repair is warranted. When the fix is applied, the latest `STATE_LEDGER.md` Movement 2 block should also be synchronized; it currently repeats the same bad count.

## (1) Brief items

### Priority 1 — counts and calendar

1. **RESOLVED — ch8 false-feed calendar.** The zero-context diff changes “for the fortnight that came after” to “for the week of sessions after,” and changes “on the thirtieth evening” to “On the thirty-first evening, after the tenth session.” Starting on day 22, the three-session discovery and seven further session days now end on day 31. The joins remain possible: the low-hall visit is day 33 and the baseline is day 48.

2. **RESOLVED — ch9 practice-bout rule.** The diff replaces “three exchanges, each to a clean touch or called even” with “first to three clean touches, with any exchange the instructor could not split called even and run again.” The developed bout's four exchanges and three-to-one result now obey the stated rule.

3. **RESOLVED — ch10 timber/stone arithmetic.** The diff removes “Call it a third off, session for session” and substitutes: “The same bill buys a third more work; burst for burst, each one costs about a quarter less.” Four bursts for the former cost of three is now expressed on both valid denominators. “Four free” and the full landing beat remain intact.

4. **RESOLVED — ch9→ch10 rewind and win counts.** The ch9 diff changes “Inside ten days she had fought nine and won nine” to “By the thirty-fourth day, ten days after she signed, she had fought nine and won nine.” Ch10 now opens the earlier scene with “on the twenty-eighth day, back in Lira's first week on the ladder, when her line in the practice register still held only three wins.” The page then gives eight and nil on day 32 and nine wins on day 34.

### Priority 2 — source distance and say-it-once

1. **RESOLVED — source distance.** The required probe fell from the pre-repair total of 20% close to 6% close, with 1% skeleton overlap. Current chapter close shares are 4%, 3%, 5%, 5%, 6%, 9%, and 9%; the highest scene is the protected-heavy ch14 officer scene at 22%, about 14% after protected wording is excluded. As a representative zero-context change, ch12's repeated lead-in—“He walked back to the second quadrangle in the dusk with that sentence going round in his head like a cart wheel, and that night he did not sleep, and the night after he slept very little”—becomes “He walked back to the second quadrangle in the dusk with that sentence turning in his head, and for three nights afterward he slept badly.” The surrounding argument is rebuilt rather than synonym-swapped. Required overlap is 0 unprotected runs.

2. **RESOLVED — ch12 low-line/high-line repetition.** The zero-context diff removes the scene break and the repeated solitary rehearsal. The old third-night opening, “On the third night he lay looking at the ceiling and worked out, for the first time with complete clarity, the two ways it could be made to cheat,” becomes the compressed “By the third night he could see the two ways to cheat it, one low and one high, and he could see neither was right, and he could not yet see what was.” The group debate now begins immediately on the fourth evening, about 330 words into the chapter. The ethical distinction, Brom's objection, and Lira's third option survive.

### Priority 3 — rhythm and density

**PARTIAL — the requested light pass improved the movement without reaching every directional target.** The diff joins repetitions such as “He had read all three before. He had read them...” into “He had read all three before, on the first night...” Sentence mean rises from 13.08 to 13.18, inside the 13–15.5 working range but still below the 14.6 formula target; median remains 9. “That” falls from about 112 to 97 per 10k, still above the secondary hint of 92. Progression vocabulary rises from about 83 to 85 per 10k rather than the packet's approximate 90. Two same-time/place scenes were merged; seven sub-850-word scenes remain because their time or location changes. At 4.2%, the share of sentences at least forty words long is already near the 4.5% working ceiling, so further mechanical joining would trade one formula pressure for another.

### Length

**RESOLVED.** Formula prose count is 32,363 words, inside the required 32,000–34,500 band.

## (2) Continuity

- **Calendar:** Day 22 begins Brom's floor work; the tenth false-feed session and wall scene fall on day 31; Lira's register sequence is three wins on day 28, eight on day 32, and nine on day 34; the Lattice encounter is day 33; the five-week wall is day 35; the baseline is day 48; Ephram's deferral is day 49; the copying-table/card scene is day 51. “A fortnight ago” for day 33→48 and “most of a month” for day 22→49 are sound.
- **Counts and apparatus:** The practice bout is first to three and ends three to one. Four times nineteen is seventy-six. The baseline supplies six trials; Wind is four free, the fifth billed, and the sixth wide/slow. The read is eleven of twelve, then twelve of twelve cold. These agree with the book map and downstream six-ceiling canon.
- **Body state:** The plate release leaves the right shoulder/forearm affected through the end of the week; the baseline hip thread is gone by the following noon. Ch14 preserves the guarded arm. No injury vanishes early.
- **Knowledge boundaries:** The panel sees only Wind and the Iron-adjacent read. Pressure is withheld; Compression and Ember stay off the floor. Seln receives the authorized brief, never learns the mechanism, never opens the banded case, and does not state a motive. “Colder country” appears once. No reserved term or truth is released.
- **Protected wording:** The mapped lines remain exact at their first required occurrences, including “I found the wall. It has students.”, Gault's full baseline note, his protected door speech, Ephram's public deferral, “Fair. Same terms I'd offer.”, the officer/Seln exchange, Seln's brief, and the final TA log line. Required overlap reports eight protected runs and no unprotected run.
- **Residual defect:** Ch12 establishes “for three nights afterward he slept badly,” the debate on “the fourth evening,” sleep “for the first time in four nights,” and later “kept Cael awake for three nights.” Ch13 nevertheless says “four bad nights.” The author's r1 report says this was intended to agree with “three bad nights and the fourth-night sleep”; it does not. The latest ledger repeats “four bad nights,” so the manuscript line and that ledger shorthand should both resolve to three.

## (3) Formula

Commands reproduced:

```text
python3 editions/monroe-1.3/tools/formula_metrics.py editions/monroe-1.3/book-04-copper-crown/manuscript/chapter-{08..14}.md
bash editions/monroe-1.3/tools/ed.sh overlap book-04-copper-crown 2
bash editions/monroe-1.3/tools/ed.sh gates book-04-copper-crown 2
bash editions/monroe-1.3/tools/sweep_probe.sh book-04-copper-crown 2 2
```

`formula_metrics.py`:

```text
chapters 7
words_total 32363
words_prose 32363
words_in_system_notices 0
sentences 2456
sentence_mean 13.18 (target 14.6)
sentence_median 9.0 (target 11)
sentence_sd_pop 11.64
share_le5_words 0.3
share_ge40_words 0.042
paragraphs 798
paragraph_mean 40.56
paragraph_median 27.0
scene_breaks_marked 28
scene_breaks_per_10k 8.65
words_per_scene 924.7 (target 950)
flesch_reading_ease 86.9 (target 72.3)
flesch_kincaid_grade 4.42 (target 6.8)
```

Overlap: **0 unprotected shared runs of at least eight words; 8 protected runs allowed.**

Gates: **0 reader-standard, 0 metadata, and 0 modern-language hits in every chapter.** Chapter word counts reported by the gate are 4,710 / 4,494 / 4,588 / 4,448 / 4,112 / 4,290 / 5,794.

Sweep probe:

| Chapter | Sentences | Skeleton | Close |
|---|---:|---:|---:|
| 8 | 193 | 1% | 4% |
| 9 | 185 | 1% | 3% |
| 10 | 186 | 0% | 5% |
| 11 | 176 | 2% | 5% |
| 12 | 178 | 0% | 6% |
| 13 | 191 | 2% | 9% |
| 14 | 264 | 2% | 9% |
| **Total** | **1,373** | **1%** | **6%** |

The formula pass is safe to close with the one continuity line fix. Its remaining deviations are directional rhythm/style targets, not gate or overlap failures.

## (4) Reader clarity

- **Speaker attribution:** Dialogue remains attributable in the multi-person rooms. The ch12 common-room sequence uses named turns and distinctive voices; the ch13 panel procedure distinguishes Gault, the Mire instructor, the operator, and Cael; the ch14 officer/Seln exchange remains explicit.
- **Referents:** The four active tracks remain separable: Brom's false-feed repair, Lira's ladder record, Cael's audit/baseline, and Seln's covered arrival. Apparatus pronouns resolve locally. Timeline cues now prevent ch10 from reading as if it follows day 34.
- **Thirteen-year-old lens:** Institutional abstractions are cashed out through visible objects and actions—the open register, chalk rings, brass grid, keyed door, tags, signatures, and filed note. The low/high-line dilemma is now stated once in concrete consequences before Lira supplies the third option. No specialized term must be understood before the scene demonstrates it.
- **Reader Standard:** The automated gate is zero in all seven chapters. The only clarity fault found is the three-night/four-night count, addressed below.

## (5) Listening proof

Every changed region and every chapter was read for joins and by ear. Straight quotation marks and asterisks are even both by chapter and by line. All 28 `---` breaks have blank space on both sides. No prose numeral needs expansion; chapter numbers occur only in headings. No broken join remains.

- **Chapter 8:** 168 quotation marks, 28 asterisks, 4 clean breaks. The revised “week of sessions” and “thirty-first evening, after the tenth session” sequence is audible without having to back-count. Capitalized Path language and ordinary weather uses do not collide.
- **Chapter 9:** 200 quotation marks, 12 asterisks, 4 clean breaks. “First to three clean touches,” the four exchanges, and the spoken three-to-one outcome agree by ear. “Most of two minutes” is distinct from Lira's later “minute and a half.”
- **Chapter 10:** 160 quotation marks, 54 asterisks, 4 clean breaks. The rewind cue lands before the register detail. “A third more work” and “about a quarter less” give the denominator explicitly and do not sound contradictory.
- **Chapter 11:** 142 quotation marks, 56 asterisks, 4 clean breaks. Capitalized `Lattice` is unambiguous in context; past-tense `read` is cued by syntax. The recomposed low-hall and wall joins are intact.
- **Chapter 12:** 170 quotation marks, 28 asterisks, 3 clean breaks. The compressed night sequence and debate join cleanly; speakers and the three-night duration remain audible. No abbreviation or numeral intrudes.
- **Chapter 13:** 124 quotation marks, 36 asterisks, 4 clean breaks. Trial transitions and the protected note read cleanly. The only listening/continuity snag is “four bad nights,” which contradicts the repeated audible count of three in ch12.
- **Chapter 14:** 136 quotation marks, 46 asterisks, 5 clean breaks. Seln's cutaway transitions are clean, and ordinary `wind` versus the Wind Path is clear from sentence context. `TA` is the only prose abbreviation; in the final italicized log entry it reads unambiguously as “T-A.” No homograph or ear collision requires a change.

## Exact line fixes

1. `manuscript/chapter-13.md`
   old: `Four short sentences, against four bad nights and an hour of held breath and a shoulder that would complain until the week was out.`
   new: `Four short sentences, against three bad nights and an hour of held breath and a shoulder that would complain until the week was out.`
