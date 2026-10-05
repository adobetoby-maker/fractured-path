# Book 4 completion pass, Step 3: Lane B report (ch32–62)

> Built by TAC (Monroe Jackson 1.3 author seat, O'Connor 1.3.0), 2026-10-05

**Scope.**
- I edited only `manuscript/chapter-32.md` … `chapter-62.md`.
- I ran no git commands.

**Method.**
- I read each chapter in full, in order, then revised it in place.
- Every change is a sentence I wrote after reading. Each one went in as an exact old→new replacement.
- The helper that applied them refuses any old string that does not occur exactly once, and any batch with one bad string is rejected whole.
- There was no global find-and-replace and no scripted splitting or joining.

**Snapshot.** The pre-pass copies of ch32–62 are in the session scratchpad (`b4LB/before/`). All "before" figures below were taken from them.

---

## 1. Priority 1: counts before and after (grep, ch32–62 only)

| Target | Before | After | Notes |
|---|---|---|---|
| "the way a/an/one/some/people/other … " (explanatory simile, strict) | 65 | 29 | `\bthe way (a\|an\|one\|some\|somebody\|someone\|people\|men\|women\|other\|children\|any) ` |
| "the way …" (any non-directional use; includes manner and habit) | 199 | 134 | Broad count, for reference. Most of what remains is manner ("the way he read everything"), not simile. |
| "as if" | 79 | 36 | |
| "as though" | 28 | 19 | |
| **Cap: strict "the way" plus "as if/though" per chapter** | max **11** (ch34); 22 chapters over 3 | max **3**; 0 chapters over 3 | Speech counts toward the cap. The two-similes-on-one-gesture cases are all gone (e.g. ch35 missing stair, ch40 Mire boy, ch43 pane, ch48 drift). |
| "exactly" | 119 | 37 | Every remaining one is exactness as the subject (Bracken, the brass, Havel's recording, Vastin's knot, the clerk's precision), speech, or the protected slip. |
| Measured pause: "for a (long/short/little) moment/while/time" | 115 | 76 | Kept in the records sittings, the twelve-by-fourteen room, the finding, and real beats. |
| "without a word" | 12 | 1 | ch38 "without a word added" means verbatim, so it stays. |
| "did not look up" | 13 | 0 | Changed for Seln (ch48, ch62), the wing woman (ch43, ch47), Karis (ch58), the clerk (ch54), Havel (ch44, ch57). "Did not look round" (a different gesture) stands. |
| "without looking up" | 5 | 1 | The one kept is Bracken's (ch51). |
| "He wrote it that night" | 3 | 0 | The frame was varied (ch39, ch44, ch59, ch62, among others). Every Log entry is kept word for word. |
| "wrote it/that down" | 18 | 17 | Nearly all are in characters' speech or are the Log's own voice. |
| "That was all." / "That was the whole of it" | 7 | 3 | |
| "nodded once" | 7 | 0 | |
| "as if it owed him money" / "seemed to owe him money" | 1 + 1 | 0 | ch53, ch60. ch36's "like it owes you money" in Lira's speech stays: it is her register and her first use. |
| "checking that it was attached" | 1 | 0 | ch49 |
| "like water round a post" / "as water parts round a post" | 2 | 0 | ch38, ch45 |
| "which from Brom/Rooke was a speech/celebration" | 4 | 2 | Kept ch41 (Rooke) and ch50 (Brom, "a celebration"). Cut ch43 and ch61. |
| Barge horn "long note and two short" | ch37, 38, 41, 42, 45, 62 | ch37, 42, 62 | Thinned in the middle (ch38, ch41, ch45). The ch42 Lira minute keeps its unanswered horn. |
| "Stair in the dark" figure (ch35's missing-stair image, reused) | 7 | 0 extra | Kept ch35's dialogue only. Cut the narrated repeats in ch35, 47, 49, 51, 52, 54, 55. |
| "stake" | 11 | 12 | This rose by one because the field-stake image moved into ch44 (see below). The re-explanations in ch45, ch51 and ch54 are now clauses. |

**The stake and the corner, explained once.**
- ch44:
  - This is where Cael first "sets the stake", so it carries the one full explanation.
  - "one small hard corner of his attention … told it to stay there, as a man sets a stake in a field before he lets the horses out."
  - The field image moved here from ch45.
- ch45 now reads: "set the stake, and only when it was settled …"
- ch51 now reads: "The hold was where he had put it before dawn." The table-cloth simile is cut.
- ch54 keeps one clause at the evaluation ("driven the stake in while his eyes were still shut … as he had every morning since the stair"). The six-names / full-cup paragraph is cut.
- ch38's re-explanation of rent and minding is reduced to two sentences.
- The "one cup / one purse" re-explanation stays:
  - its first full statement (ch47);
  - one clause in ch48;
  - Cael's spoken line in ch53.
- It is cut to a clause in ch51 and ch55.

### The elevens

**Removed, the lane B list (all done):**
- **Porters' eleven minutes.** ch55:145 and :155 now read "a quarter of an hour". ch59 now reads "the quarter of an hour" at both places (:111 and :127), to match.
- **Eleven thumbnail marks.** ch53 is now **ten**:
  - "there were ten"; "But it's ten"; "all ten times";
  - `*ten of ten*`;
  - in the Log, "Drifts: ten by Lira's thumbnail … all ten in the gaps".
  - "Nine were nothing much" still adds up.
  - ch62's "a whole chair-back of Lira's thumbnail marks" carries no number.
- **Eleven crosses.** ch47 is now **seven** ("I've made seven this term. Two of them were for sneezing." / *Seven crosses in a term. Two for sneezing.*).
- **Eleven years of indexes.**
  - ch39 now reads "a dozen years of indexes" and "all twelve years of indexes".
  - ch45 now reads "a dozen years of attendance lists", to match.
  - ch39's "a dedication, eleven years ago" is now "eight years ago".
- **Eleven provision files.** ch32 now reads "There aren't a dozen provision files in the whole place". Nine closed, one Silver, and his own still add up.
- **"Eleven more chairs".** ch38 is now Karis's precise "nine more chairs" (eleven names minus the ordinary visit's two). Brom echoes it.
- **"Lira has done it eleven times".** ch56 now reads "more times than I'd like to count".
- **The supersession clerk's eleven minutes.** ch60 now reads "It took ten." and "At the end of the ten minutes".

**Also removed (not canon; the read lists most of them as reached-for):**
- ch32: the fire-watch boy, "perhaps eleven", is now "perhaps ten".
- ch34: "eleven feet" ×3 is now "a flight below" / "one flight of stairs" / "a flight above".
  - The brief puts "eleven feet" in lane A's list, but it occurs only in ch34.
- ch35: in the porter-count game, "got eleven, and wrote eleven" is now "thirteen". Seln's answer of nine is unchanged.
- ch40: Withrow's address, "eleven minutes" ×2, is now "twelve minutes". The read's §3 names it as reached-for.
- ch40: "eleven paces of open boards", recalling ch28, is now "across the open boards". ch28 is lane A's and is untouched.
- ch47: the counsel's "eleventh question" and "eleven questions" are now "fourteenth" and "fourteen". This keeps "eleven questions" for Vastin.
- ch48: "document eleven" (Bracken's comparing sheet) is now "document fourteen". It occurs nowhere else.

**Kept (canon or protected):**
- carrel eleven (ch32, 35, 45, 56, 61);
- eleven weeks (ch32, 39, 50, 56);
- the eleven words of the incident report (ch32);
- the delegation's eleven names, strangers and people (ch38, 40, 43, 44, 45, 46, 47, 48);
- eleven days (ch57, 58, 59, 61);
- Ilsev's eleven minutes (ch49 ×2, ch52) and eleven months (ch49 ×2);
- eleven seconds, and four minutes and eleven seconds (ch42, ch52);
- Lira's eleven bouts unbeaten (ch52);
- "eleven of twelve", "eleven calls in twelve" and "eleven clear of twelve" (ch53, 55, 62);
- subsection eleven (ch56 ×2);
- the eleven questions and "the eleventh asked" (ch56, 57, 58, 59, 62);
- Gault's protected "in eleven years" (ch56);
- the eleven clauses of article forty-one and "stopped at eleven" (ch48), plus the protected finding (ch49);
- 311 sheets (ch42, 44, 50);
- the eleventh of Sowing (ch37 ×3, ch62);
- the 9–11 record ("Eleven to you", ch43);
- "two different pages numbered eleven" (ch44, from the M6 recheck);
- the middle-bag counts out of eleven (ch34, ch35, ch62 inventory; Compression canon);
- "Day eleven" (ch36, the ledger's day count);
- ordinals in sequences (ch33 "tenth and eleventh" steps; ch35 "the eleventh" run; ch47 "Ten. Eleven. Twelve." drill count; ch44 "the eleventh" date).

**Count: 127 → 91.** 36 removed.

---

## 2. Words

- **wc: 150,337 → 148,156 (−2,181).**
- formula_metrics words_total: 150,006 → 147,827.

| ch | before | after | Δ | ch | before | after | Δ |
|---|---|---|---|---|---|---|---|
| 32 | 4655 | 4640 | −15 | 48 | 5587 | 5508 | −79 |
| 33 | 5172 | 5151 | −21 | 49 | 6826 | 6355 | **−471** |
| 34 | 4570 | 4512 | −58 | 50 | 3142 | 3091 | −51 |
| 35 | 4445 | 4377 | −68 | 51 | 5504 | 5382 | −122 |
| 36 | 4912 | 4831 | −81 | 52 | 5491 | 5434 | −57 |
| 37 | 4552 | 4505 | −47 | 53 | 5139 | 5127 | −12 |
| 38 | 4487 | 4384 | −103 | 54 | 4547 | 4416 | −131 |
| 39 | 4071 | 4066 | −5 | 55 | 5153 | 5130 | −23 |
| 40 | 3922 | 3858 | −64 | 56 | 4830 | 4812 | −18 |
| 41 | 3704 | 3658 | −46 | 57 | 5244 | 5241 | −3 |
| 42 | 4696 | 4645 | −51 | 58 | 5011 | 5008 | −3 |
| 43 | 4960 | 4917 | −43 | 59 | 5366 | 5363 | −3 |
| 44 | 5781 | 5657 | −124 | 60 | 4805 | 4778 | −27 |
| 45 | 5706 | 5611 | −95 | 61 | 4668 | 4659 | −9 |
| 46 | 4114 | 4046 | −68 | 62 | 4728 | 4720 | −8 |
| 47 | 4549 | 4274 | **−275** | | | | |

## 3. formula_metrics.py, ch32–62

| Measure | Before | After | Held to |
|---|---|---|---|
| sentence mean | 13.61 | **13.47** | ≥ 13.3 ✓ |
| sentence median | 10.0 | 10.0 | |
| ≤5-word share | 0.281 | 0.284 | ≤ ~0.34 |
| ≥40-word share | 0.037 | **0.035** | ≤ 4.5% ✓ |
| paragraph median | 26 | 26 | ≤ ~30 |
| scene breaks | 130 | 128 | Only ch49 changed (8 → 6, the sanctioned fold) |
| words per scene | 931.7 | **929.7** | 850–1,050 ✓ |
| FRE / FK | 86.9 / 4.52 | 87.1 / 4.46 | |

## 4. Overlap, gates, sweep

**`ed.sh overlap book-04-copper-crown N`**

| N | Result |
|---|---|
| M5 | 0 unprotected; 18 protected |
| M6 | 0 unprotected; 9 protected |
| M7 | 0 unprotected; 9 protected |
| M8 | 0 unprotected; 13 protected |
| M9 | 0 unprotected; 32 protected |

The protected-run counts match the pre-pass counts exactly.

**`ed.sh gates`, M5–M9.** All 33 chapter rows read reader_standard=0, metadata=0, modern=0.

**`sweep_probe.sh book-04-copper-crown 5 9`** (skeleton / close):

| Movement | Brief's ceiling | Before (my baseline) | After |
|---|---|---|---|
| M5 (ch30–37) | 1% / 12% | 1% / 12% | **1% / 12%** |
| M6 (ch38–44) | 1% / 10% | 1% / 10% | **1% / 10%** |
| M7 (ch45–50) | 1% / 11% | 1% / 11% | **1% / 11%** |
| M8 (ch51–56) | 2% / 7% | 2% / 7% | **2% / 7%** |
| M9 (ch57–62) | 2% / 9% | 2% / 8% | **2% / 8%** |

**How the sweep stayed level.**
- My first after-run showed M5 at 13% and M8 at 8%. Most of that came from cutting words: shorter sentences began to match generic source sentences.
- I diffed close sentences chapter by chapter with the probe's own matcher.
- I recomposed every new close sentence and checked each candidate with the same ratio.
- Every chapter in ch32–62 now has a close count at or below its starting count.
  - Two examples: ch48 is 35 → 31, and ch49 is 44 → 37.
  - One line had reached skeleton (0.55): ch48's Ilsev seating line. It was recomposed.
- Note: M5's figure includes ch30–31, which lane A was editing during this pass:
  - ch30 went 12% → 13%;
  - ch31 went 12% → 14% (202 → 200 sentences).
- M5 holds at 12% with those included.

---

## 5. Priority 2

**ch47: −275 words (4,549 → 4,274).**
- The Ilsev window's four-volume anecdote (the hens, nineteen fillings-in, about 190 words) is now one sentence:
  - "Years ago, at a district station two days' ride from anywhere, she had watched a beautiful four-year observer's log bring a practitioner's whole file down, for no worse reason than that it had no holes in it; honest records are full of small holes."
- Her four questions and the cross answer still rest on it.
- The rest came from priority 1 cuts in the chapter and a tighter opening to her window.

**ch49: −471 words (6,826 → 6,355). The finding is now reached in section six, not eight.**
- **Cael's first recess folded into Ilsev's section.**
  - The break is gone, and the beat stays where it was, between the windows.
  - Ilsev's last paragraph looks across at the enrollee. Then a name-led paragraph hands over to Cael ("Cael had spent the recess on that hard chair…").
  - That paragraph keeps the beat's content: the two who kept their places, the form, about eleven minutes by his breaths, the tea in four swallows, "not his to know", the stake.
  - Nothing leaks: he learns nothing of the return.
- **Havel's logging folded into his own window.**
  - The break between the logging (end of the first recess) and his notebook entry (second recess) is gone.
  - The courier and the docket are compressed, and the carter-and-wheel simile is cut.
  - Mark four is kept word for word, in place and unseen by Havel: "Up the table, past the counsel, the Archmarshal's pen rose from his folder while Havel was entering the referral. … Havel did not see it. He was looking at his ledger, which was his work."
  - Cael's later count still records it as seen from the wall.
  - Havel's protected line is unchanged.
- **Scene breaks: 8 → 6.** This is the only break change in lane B.
  - It conflicts on its face with "No scene breaks added or removed", but the ch49 fold cannot be done without it.
  - I read the fold instruction as the sanctioned exception. No cutaway is cut.

**ch45: one line of Cael's own stake, placed at the end of breakfast, just before the Vastin window:**
> Cael ate. In seven days it would be his own turn on the oak, with an Archmarshal at the rail, and if the five came out no bigger than his baseline, the one true sentence anybody had ever written about him would stop being true.

The line mirrors the chapter's earlier "In six days she would walk out onto the oak…" for Lira. The day count holds: the thirteenth, with the evaluation on the twentieth.

---

## 6. Seams reread

| Seam | Confirmed / changed |
|---|---|
| **ch34, rule two** | **Confirmed.** It now reads word for word as the ch23 minute: *A directed acquisition permitted only within earnest engagement the subject begins himself, close, in the ordinary course of his assignment; any reach to be awake and directed.* The gloss ("*The subject begins himself*", "*Awake and directed*") and the five-finger count fit it. |
| **ch48, ch58, ch62, Seln's hands** | **Confirmed**, with one change:<br>• ch48 and ch62: the copying table and the recess sheet are in "the round copying hand".<br>• ch58: the slate is in the round copying hand. His index is in "his fourth hand", the product hand, which agrees with ch41's "upright, plain hand that he kept for product".<br>• **Changed:** ch58's cipher page read "in the fifth hand, sloping downhill to the right". "Sloping" belongs to the merchant's wrapper hand (ch28), so it now reads "in the fifth hand, the shorthand that had grown out of the cramped one", agreeing with ch30.<br>• Also changed: ch48's Seln "did not look up" ×3 is now "did not raise his head". |
| **ch51–52, ch56, Lira's certificate** | **Confirmed:**<br>• ch51: "a certificate three years old";<br>• ch52: "three years ago" / "It was three years old";<br>• ch56: "in years";<br>• ch51 and ch60: she was fourteen at Fenmark, with ninety breaths and nine stand-ups;<br>• ch60: the supersession;<br>• all agree with ch25. |
| **ch54–55, the baseline month** | **Confirmed.** Every reference is "second month" or "the baseline" (ch54 ×8, ch55 ×8). ch43, ch48 ×2, ch49, ch57 ×2 and ch62 ×2 agree too. "First month" survives only for the term's opening weeks: the fame tally (ch36, ch40), the Rooke page (ch38), Merrick's habit (ch46), and Cael's sequence choice (ch43). |
| **Also found and fixed** | **ch40, Ephram's deferral.** It read "In the first month" ×2, but the deferral is d49 (ch14), and ch61 has "In the second month I stood up there … in front of sixty people". Both ch40 lines now say "second month", and "with half the bluff hearing it" is now "with sixty people hearing it".<br>**ch59.** Vastin's struck verdict was written "within two minutes of the frame failing", but ch55 has the notebook come out while the porters were bolting the reserve frame. It now reads "within minutes".<br>**ch61.** "Most of a year he'd carried a promise" now reads "All season". The promise was made in the second month. |

**Checked and unchanged:**
- "decision point" once (ch54); "unbound" once (ch50);
- the C7 framing (ch62);
- no English weekday names;
- no season tied to Halcenvane: "winter coat" (ch32) is a garment, and ch49's "in an autumn" and ch51's "one cold Greyvane winter" are closed-book memory;
- no month order;
- all six notices and documents, verbatim;
- every bout's exchanges and landing beats;
- the evaluation's six trials and figures; the interview questions;
- Gwen and Abbot untouched.

A 96-string check of the BOOK_MAP §10 lines found every one present at its starting count (three are split by dialogue tags in the original and were 0→0 by construction).

---

## 7. Changelist by chapter

- **32.** The boy's age is now ten. The provision files are now "not a dozen". Three similes are cut. Seln's "without looking up" is cut.
- **33.** Three "exactly" are cut. Pauses are thinned. Brom's "without a word" is cut. Gwen's "without looking up" is cut.
- **34.** "Eleven feet" ×3 is now "a flight". The similes go from 11 to 3: sailor, ferryman, heart, lightning, bag, the door-shut quiet, the "as if" lines. The tier line is recomposed. Three new close lines are recomposed.
- **35.** The soldier, missing-stair and room-went-still similes are cut. The porter-count game is now thirteen. Two "nodded once" are cut.
- **36.** The tray, shelf, sun, cat and bricks similes are cut. Two "exactly" are cut.
- **37.** Pauses are thinned. The crowd-gate and statue similes are cut. "Getting it exactly right" is cut.
- **38.** The rent/minding re-explanation is trimmed. "Water round a post" is cut. "Nine more chairs". The barge is cut. Five similes are cut.
- **39.** Index years are now a dozen or twelve, and the dedication is "eight years ago". The Log frame is varied.
- **40.** Ephram is now "second month" ×2. Withrow's address is now twelve minutes. "Eleven paces" is cut. Five similes are cut. Four "exactly" are cut.
- **41.** Three similes are cut. Two pauses are cut. The barge is cut.
- **42.** The cat, carpenter-joint, stair, thunder and held-breath similes are cut. The "exactly" set is trimmed.
- **43.** The pane door and low beam are cut. "Huh. For Brom, that was a speech" is cut. The wing woman's "did not look up" is changed. Three "exactly" are cut.
- **44.** The single stake explanation now carries the field image. Havel's coin, pencil and service-coats similes are cut. Vastin's arrival similes are trimmed. Eight "exactly" are cut.
- **45.** The stake is now a clause. **The one added stake line.** "Out of a dozen years". "Water round a post" is cut. Similes are cut.
- **46.** Five similes are cut. Three "exactly" are cut. Two pauses are cut.
- **47.** **The anecdote is now one sentence.** The crosses are now seven. The counsel's questions are now fourteen. Similes and pauses are cut.
- **48.** Seln's look-up is changed. "Document fourteen". Six "exactly" are cut. Similes are cut. The Ilsev seating line is recomposed.
- **49.** **The two folds.** Similes are cut, including the latch kept and the carter cut. The "attached" and "make sure" gestures are cut. Pauses are cut.
- **50.** The strange-house, door-knock and delegation similes are cut. Pauses are cut.
- **51.** The stake and cup re-explanations are now clauses. The crowd, wedding, stair and card similes are cut.
- **52.** Four "exactly" are cut. Two similes are cut. "That was all of it" is cut. The practitioner's look-up is changed.
- **53.** The thumbnail marks are now ten (×7). "Owed him money" is cut.
- **54.** The stake paragraph is now a clause. The clerk's look-up is changed. The stair and loose-tread similes are cut. "A sneeze while it was still happening".
- **55.** The porters' wait is now a quarter of an hour. The cup clause is cut. A missed-stair image is cut. Four "exactly" are cut.
- **56.** "More times than I'd like to count". Three "exactly" are cut. Two similes are cut.
- **57.** Havel's "not look up" is changed. "Nodded once" is cut. One simile is cut.
- **58.** The cipher-hand seam. Karis's look-up is changed. Two "without a word" are cut. Two "exactly" are cut.
- **59.** The porters' wait is now a quarter of an hour ×2. "Within minutes". "That was all" is cut. The Log frame is varied.
- **60.** The supersession is now ten minutes. "Owe him money" is cut. The man's look-up is changed. "Nodded once" ×2 is cut.
- **61.** "All season". "That was all" is cut. "Which from Brom was a long speech" is cut.
- **62.** The Log frame is varied. "That was all" ×2 is cut. Seln's look-up is changed. Two "exactly" are cut.

---

## 8. For the coordinator: ledger and records to update

The STATE_LEDGER still records these figures, which have now changed:
- line 597: Withrow's address, "eleven minutes", is now twelve;
- line 797: "eleven this term, two for sneezing", is now seven;
- lines 831 and 874: "the eleven minutes" (porters), now a quarter of an hour;
- lines 866 and 909: "eleven rehearsal drifts", "eleven thumbnail marks", now ten;
- line 916: "ch53 `*eleven of eleven*`", now `*ten of ten*`;
- M7's "counsel 11" questions, now fourteen;
- the read's §1 "three spelling differences on document eleven", now document fourteen;
- the supersession's eleven minutes, now ten.

Three more items, for the record:
- The ch40 "second month" fix for Ephram's deferral is new to the ledger. It agrees with ch14 (d49) and ch61.
- PASS-BRIEF lists "eleven feet" under lane A, but it occurs only in ch34. Lane B removed it.
- No file outside ch32–62 was touched, apart from this report.
