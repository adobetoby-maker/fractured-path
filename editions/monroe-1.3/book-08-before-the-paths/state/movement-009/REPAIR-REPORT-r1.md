# REPAIR REPORT r1 — Book 8, Movement 9 "The Center" (ch54–60)

Author seat: O'Connor 1.3 (Monroe 1.3 voice), `claude-opus-5-5`. Date: 2026-10-12.
Baseline: `pre-repair-r1/`. Nothing committed, nothing pushed. Files touched: `manuscript/chapter-54.md`, `-55`, `-57`, `-58`, `-59`, `-60` (chapter 56 is untouched), `state/movement-009/AUTHOR-REPORT.md` (a head note; "New canon minted" and "State at movement end" refreshed), and this file.

## 1. Method, and what was and was not read

- Read in full: `REPAIR-BRIEF.md`, `plan-audit-apply.md`, `review-editorial.md`, `review-cold.md`.
- `plan-audit.md`: findings only (lines 1–171 and 207–342). **Not read:** §5.2 "Minimal restorations and protected-source notes" (172–206) and the "Exact line fixes" list (343 to the end).
- `source-tracking.md`: the verdict, the count table and the two prose notes on the tracked passages. **Not read:** the rows of the "Tracked passages" table (28–31), which quote the old text.
- Nothing under `books/` or `v3-runs/` was opened.
- **Source-derived matter that reached me through the permitted reads**, declared so that the recheck can look for it: `source-tracking.md`'s prose notes describe the old order of the two tracked passages (the altered slope, its bare face, Seln found on it, a third of the way up and flat to the rock; and the four links of the win sentence), and the audit's unit table says which speaker the old text gave each restored line and that its tag after the road line was "he said". No sentence of the old text was read. Both recompositions were built to move away from the described orders, and the first takes its new entry from the brief's own suggestion (Seln first, by grit and Teague's eyes, and the reason afterward).
- Rhythm and length were tuned by hand, sentence by sentence, with exact-string replacements that I wrote for each place. No rule-based splitting or joining was run.

## 2. Results, as printed

Formula metrics (`formula_metrics.py`, files as they stand; there are no marker lines left to strip):

| ch | words | sentence mean (13.3–14.2) | ≥40-word share (2.5–4.5%) | words/scene (850–1,050) | scenes |
|---|---|---|---|---|---|
| 54 | 5,666 | 13.56 | 3.6% | 944 | 6 |
| 55 | 5,497 | 13.92 | 4.1% | 916 | 6 |
| 56 | 4,736 | 13.77 | 3.8% | 947 | 5 |
| 57 | 5,103 | 14.14 | 3.0% | 1,021 | 5 |
| 58 | 5,798 | 13.77 | 2.9% | 966 | 6 |
| 59 | 5,218 | 13.84 | 3.7% | 870 | 6 |
| 60 | 4,484 | 13.51 | 3.0% | 897 | 5 |

Movement: 36,502 words by the metric's count; 2,648 sentences; mean 13.78; ≥40 share 3.4%; 936 words/scene. Every chapter is inside all three working ranges.

`ed.sh gates book-08-before-the-paths 9`:

```
chapter-54.md words=5677 reader_standard=0 metadata=0 modern=0
chapter-55.md words=5509 reader_standard=0 metadata=0 modern=0
chapter-56.md words=4745 reader_standard=0 metadata=0 modern=0
chapter-57.md words=5114 reader_standard=0 metadata=0 modern=0
chapter-58.md words=5810 reader_standard=0 metadata=0 modern=0
chapter-59.md words=5231 reader_standard=0 metadata=0 modern=0
chapter-60.md words=4499 reader_standard=0 metadata=0 modern=0
```

`ed.sh overlap book-08-before-the-paths 9`:

```
# summary: 0 unprotected shared runs of >= 8 words; 17 protected runs (allowed)
```

`{{JOIN}}`: 0 in every chapter. `[[TIER-B`: 0 in every chapter.

`sweep_probe.sh book-08-before-the-paths 9 9`, once, without SHOW: skeleton 3%, close 16% (ch55 2% / 17%).

**The movement did not grow.** By `wc -w`: 36,606 at baseline, 36,585 now (−21).

| ch | baseline | now | change | why |
|---|---|---|---|---|
| 54 | 5,681 | 5,677 | −4 | the join round "It's through."; one sentence about three sticks cut to pay for it |
| 55 | 5,440 | 5,509 | +69 | C1 (the reveal re-ordered; the summing sentence gone; the listener's anchor); six small cuts recover most of it |
| 56 | 4,745 | 4,745 | 0 | untouched |
| 57 | 5,121 | 5,114 | −7 | the lead-in to the restored sentence and the "length" anchor; three small cuts |
| 58 | 5,846 | 5,810 | −36 | four joins and the "length" anchor; five cuts (the stumps' spacing remark; a paragraph about made things at the round's end; two short sentences; one clause) |
| 59 | 5,228 | 5,231 | +3 | C3 turned |
| 60 | 4,545 | 4,499 | −46 | three joins and one line for Karis; a paragraph of second thoughts at the ledger cut, and Karis's speech about writing shortened |

Protected units: 62 strings checked against the repaired chapters, each whole and once, except `"Noted," said Cael.` / `"Noted," Cael said.`, which stand once in each departure by design. The closing prose is byte-identical to the baseline's last line and is still the last thing in chapter 60. Chapter 58 ends on `"Wait here," he said, and did not look back, and walked toward the center of the oldest quiet, alone.` Chapter 55 ends on `It was not ink.`

## 3. Section B — the joins

| # | Where | What stands now |
|---|---|---|
| B1 | 54:93–97 | After his thought of the wall across a road, "He laid the burnt stick down upon the charcoal, along the floor, from the one mouth to the other." / `"It's through," Cael said.` / "He had not ruled on anything, since the field was another man's. He had only said where the line went, as the one who had drawn it." Teague's "Then here's what I see in it" answers. |
| B2 | 55:375–377 | No lead-in sentence was added. The paragraph before now ends "…in the mouth of a gap, where the line ran out between two walls.", so that the last line's "It" has the line directly before it. `It was not ink.` is the chapter's last line and is not explained. |
| B3 | 57:225–229 | "But he knew what he had been handed. It came to one sentence, and he let himself have the one." / the restored sentence, alone / "He did not go a step past that." |
| B4 | 58:183–185 | "Nobody else on that rock could have said the next thing; and for the space of a breath she did not say it either." / `"The others are copies," said Karis.` (so that her two speeches are not tagged back to back). |
| B5 | 58:307–311 | Vastin's first part as applied; then "He lifted his eyes from the cut, and looked along it to the left hand, and to the right, for as far as it could be seen."; then the second part. His crossing follows as written. |
| B6 | 58:325–329 | `"Nothing," Oryn said. "Everything, round it."` / "She had said that to the floor. She turned her head, and said the rest to him." / `"Same as you."` Unanswered, as before. |
| B7 | 58:347–353 | `"My crew's stood at four of these. It's stood at enough," Teague said.` / "He looked round then, as he had looked round on a shelf beside a row of iron, at the boy who stood where his left shoulder would have been." / `"Field's mine. This isn't field."` / "It was the ruling that he had given at that fence, in two words, when he asked to be told how." |
| B8 | 58:369–381 | Attributions trimmed to what a listener needs: `"Every other one, yours worked and ours died," she said.` (the paragraph before is hers); `"Yes."` and `"You think this one's different."` untagged; `he said` kept inside Cael's two-part speech, where the comma requires a tag. The three narration lines stand as printed and nothing follows the last. |
| B9 | 59:243–245 | As applied; no change was needed round it. |
| B10 | 60:149–157 | As applied, with the one beat: "He let that stand for a breath, as he had once let its fellow stand in a yard full of snow." |
| B11 | 60:215–229 | `"The day I have to," Oryn said.` / `"Noted," Cael said.` / `"Everybody says that."` / "Her eyes had gone to the box that stood nearest his feet, and from the box to the place where her tape lay under his shirt." / `"They'll carry. They'll hurt," she said.` / "Then she gave him the rest, as she had once sent it to him on a strip of bark, and she did not soften a word of it." / the term. An earlier sentence that had her look at the tape and the box before his question is cut, so that the look happens once. |
| B12 | 60:187–191 | The scar line has its own paragraph after she turns the palm to the light, and Karis answers it: "I have a use for lines." (mine; seven words). 59:147 and 60:17 are as the coordinator applied them. |

Two further lines were brought to the letter of the map, since the editorial read noted them: `"Right."` (58:275) and `"It's the first one."` (58:291) now stand with their own full stops and no tag; the speaker is clear from the sentence before each.

## 4. Section C — recomposed

1. **55:65–81, the swept bank and Seln (order broken).** New order: Cael counts heads after the fall and is one short → the place at the bank's foot is empty → grit runs past the roof's high corner, and Teague's eyes are already up → a boot-sole and a hand against the hill, gone behind the roof's edge → "He understood only then what the man was climbing." → the bank is gone to bare rock (*Take the quilt off*) → "Seln had seen it before the dust was down, and had said nothing, and gone." → Teague's eyes come down the slab → "Bow,". There is no measure of how far up he is and no word of how he lies on the rock.
   **55:305–309, the summing of the win.** The sentence is gone and nothing replaces it as a summary. After Seln's "Nine." and the note that it was the first time he had raised his voice, Cael sees the cost: "Forty feet under the shelf a roof of dust still lay on the air, with a brown coat at its low end. Nobody had yet told the old man that he might leave off." The two causes are left where the action already put them (the fall sweeping the bank, 55:73; Seln over the lip at the seventh flight, 55:199).
2. **60:281.** "He had asked for no place among them, that morning or on any other, and nobody had offered him one." None of "admitted", "join" or "belong" is used here or anywhere in chapters 59–60 of him.
3. **59:73.** Turned: "The whole bare floor leaned, as a line of cut signs leans, steadily; and he could not have said what it leaned at."
4. **Anchors.** The two hurt big men, once more in the gap (55:81): "He meant his own: the broad man, with the shin on a board. Brom was in the middle yet, with linen round the stub of a bolt in his left forearm." A length, at first use: 57:115, "A length was the whole cord run out to its last knot, which was twenty strides; four knots more were twenty again."; 58:75, "That was a length: the whole cord, which was twenty strides."
5. The editorial's cadence pass was not undertaken. The closing prose was not touched.

## 5. What else changed, so that the recheck has all of it

- **Cut to hold the length (all mine, none protected):** 54, the sentence likening the file to a house for the sick; 55, "A captain had ordered it from the shelf, in three words.", the clause about what Oryn said above a weir, "That was the nature of it…" (Vastin says as much himself in chapter 56), and "on a ridge, with his arm in linen" (which was also wrong: the lesson was at the dead hold, before the arm went on its slat); 57, "She had no more than that…", "Nobody spoke for a little…", and one stage direction inside Cael's speech; 58, the remark that the stumps are unevenly set and Karis's wish to compare them with the Fallow's (she now only writes down the second and third), the paragraph about every made thing he had handled, "He turned from that…", the end of the sentence about his bootlaces, and the clause about Lira's face; 60, the paragraph in which he goes over whether the push had paid a little of the debt (the ledger's own line already rules it), and most of Karis's speech about sending a line of her own.
- **A fact corrected in passing (55:73):** "The people on that shelf had just taken it off for him" (it had read "Three people", and the shelf holds nine).
- **Minted in repair:** Karis's "I have a use for lines." (60:191). Nothing else.
- **No fact of the calendar, the bodies, the purse, the loads, the fragments or the deployment changed.** Thirteen fragments; deployment thirty-five; purse 123.

## 6. Standing constraints, re-checked on the repaired text

No season, month-name or weekday name. No possessive before "Path" in narration outside the protected line at 58:379. "Forty years" only inside Vastin's protected line (58:307). "Four hundred years" only in the closing prose. No "Architect", *terminal*, *circuit*, *infrastructure*, "recurrence", "primordial" or "tomb". "The court" lower-case wherever it stands. The young one is unnamed; no new proper name. Teague and Vastin are untold; *still* / *set* / *bones* and the shape are told to nobody; the leaf is quoted by nobody and laid against nothing; the third sentence is nowhere but in the closing prose's own words. Vastin has asked for no place and been offered none.
