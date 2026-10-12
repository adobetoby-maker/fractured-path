# REPAIR REPORT r1 — Book 8, Movement 6 "Before the Paths" (chapters 34–40)

Author: claude-opus-5-5 (same seat, same session as the draft). Method: NO-SOURCE. Repaired 2026-10-12, from `REPAIR-BRIEF.md` against the baseline `pre-repair-r1/`.

## What was read

- `REPAIR-BRIEF.md` and `plan-audit-apply.md` in full; the four Sol reads in full (`plan-audit.md`, `source-tracking.md`, `review-editorial.md`, `review-cold.md`), as the brief directs.
- **Source-derived text seen, and how it was handled.** No file under `books/` or `v3-runs/` was opened. Two of the reads quote the old text, and I have therefore seen it: `source-tracking.md` gives the opening words of five source sentences; `plan-audit.md`'s exact-fix list prints the source's fuller wording for Cleon's speech at the board, for "There…", for Karis's aside in the leaf and at the scraped place, for her title sentence, and for Seln's speech at the fire. The brief rules those fuller forms out and gives me the sense to carry instead. Every join below was composed from the brief's statement of sense and from this edition's own staging, not from those quotations; where I could see that a word of mine echoed one of them it was changed (Cleon's "a pile of chippings" was first "a heap"). The overlap gate reads 0 unprotected.

## Result

| Ch | Scenes | Words | Mean | ≥40 | ≤5 | Words/scene | Baseline words | Lines changed vs baseline |
|---|---|---|---|---|---|---|---|---|
| 34 | 5 | 4,891 | 13.78 | 2.8% | 24.8% | 978 | 4,923 | 22 |
| 35 | 6 | 5,697 | 13.40 | 2.8% | 29.4% | 950 | 5,687 | 84 |
| 36 | 6 | 5,794 | 14.13 | 2.7% | 23.9% | 966 | 5,794 | 4 |
| 37 | 7 | 5,974 | 13.52 | 3.2% | 25.1% | 853 | 6,044 | 40 |
| 38 | 5 | 4,634 | 13.51 | 2.9% | 24.8% | 927 | 4,521 | 50 |
| 39 | 5 | 4,867 | 13.67 | 3.1% | 23.0% | 973 | 4,853 | 20 |
| 40 | 5 | 4,295 | 13.46 | 3.1% | 27.9% | 859 | 4,309 | 126 |
| **Movement** | 39 | **36,152** | 13.64 | 2.9% | 25.6% | 927 | 36,131 | |

- **Every chapter is inside the three working ranges** (mean 13.3–14.2; forty-plus 2.5–4.5%; 850–1,050 words a scene). Chapters 37 (853) and 40 (859) sit near the floor of the scene range; chapter 35 (13.40) and chapter 40 (13.46) near the floor of the mean. Further cuts to either would take them out.
- **The movement did not grow:** 36,152 against a baseline of 36,131 (+21 words). The joins and the two cues added about 520 words; the recompositions and nine trims took out about 500.
- `ed.sh gates book-08-before-the-paths 6`: all seven chapters `reader_standard=0 metadata=0 modern=0`.
- `ed.sh overlap book-08-before-the-paths 6`: **0 unprotected**; 27 protected.
- `grep -c '{{JOIN}}'`: 0 in every chapter. `grep -c 'TIER-B'`: 0 in every chapter.
- No scene, day, route, sum, injury or reveal was re-staged. One piece of blocking changed, as the brief allowed: Cael sits before Vastin speaks at the fire (see B12).

## A. Kept, untouched

The twelfth's unbidden leaning (the chamber, the rope-walk, the bridge and hinge, the dividers, "It'd look at a spoon", the table, the inventory's "it looks before I've said that it may", the leaf); the chronicle read as far as the hole and marked, Karis then Cleon; *The Architect* spoken once by Karis; all thirteen flags. Chapter 36 was changed only by two sentence divisions for the mean (it stood at exactly 14.2); nothing in the tail was reworded.

## B. Joins written (the protected words are exactly as the coordinator set them)

1. **35:15–31, Cleon's speech.** The three fixed pieces stand in order, each on its own line. Between them, in my words: of the tally-book, "A load came in at a gate. It was paid on, and when the day was done a clerk put it down. He might have begun at the head of his column or the foot of it; it'd be the same tally. There's not a mark on that leaf that's waiting for anything."; of the sheet, "Whoever cut this set each sign where it is for the sake of the one after it. Take them out of their order and you've a pile of chippings. Leave them in it, and you're handed on, sign to sign, whether you can read a letter of it or not. I don't read it. I'm walked down it." He looks from the book to the sheet once more before "This is a stair." The word "bearer" does not occur in chapter 35.
2. **35:49, "There".** Cleon's. The paragraph before it now ends with the finger going "slower and slower; and above the last sign of the run it stopped." The attribution reads `"There," said the man.` (Cael is the subject of the sentences on either side.) "It came at that word." stands.
3. **35:225.** Unchanged from the coordinator's line. I tried "he said, to himself" and the overlap gate then read the unit as unprotected; the coordinator's attribution is restored.
4. **35:237–247, the warning.** A lead-in places him ("The man stood at the table's corner, where he had set the cup down, with his face to the plank. He spoke to the oak."). First join: "The reed lay along the table's edge, and he squared it with one finger, to the grain." Second: the plan's own "He stopped." and "The square finger had come off the reed." "He went back to the carving." follows as before.
5. **37:195, the cups.** Cael's. Vastin now ends his remark, "I have kept the count at a great many boards. I should have struck both." Cael answers across the table. After it: he "had not known that he knew it until it was out"; Vastin, "I see that it is… I was never shown the book."; Brom fills the cup. Brom's "That's so" no longer answered anything and is gone.
6. **38:109–119, the leaf.** First half: `…the rivers ran wrong*" — her breath had given out upon a comma, and she took another without lifting her finger — "*there came one…` (nothing of the record is added or missing). Second half: after `"*And the* — "` her finger stops above the one stroke; she says, in her own voice, "It is scraped. A word as wide as four of his letters, or five. I have the first stroke of it, and nothing after."; the finger goes on; the record resumes. The object is not described again.
7. **38:153, the title.** A one-line join before it: the pencil's butt goes from the head of the skin to the pale place.
8. **38:167, "Older. Made. Us."** Karis's, said. Before it she shuts three fingers into her palm, one at a time, "as a big man had counted findings at a spring". My sentence after it ("It was three words. Cael counted them…") stands.
9. **38:221, Vastin from the box.** The restored line sits between my lead-in and Karis's "Two pages," with no change.
10. **39:181–185, the street.** Both lines Seln's. Cael gives two sentences "as a carter gives a load to the man who is to take the other shaft" — "It's one man's work. All of it; the tiers, and the rest. He says so himself." and "And he says who it was built against. It wasn't a house. It was a sort of people." — and Seln answers each with one of the fixed lines, then says nothing for ten paces. His later line is adjusted to match ("I have had two sentences, which is as much as I trust from any mouth").
11. **40:87, Seln at the fire.** One speech, ending on the fixed sentence: he came into the town with a thing undecided; "There is a house on that hill which would give a great deal to have it laid upon its ledge; and I have asked myself on a good many nights what it was that I kept it out of."; "I had only ever seen that house from the inside of its own books. It stands upon this. I know now what the office is for, which I did not know at noon; and I had rather know it and carry the thing, than carry it blind." The hand shuts on the strap. No count of years; the case on his chest, shut; nothing in it named.
12. **40:121–147, Vastin.** First join, his own words: "I held that for the whole of my service, and was easy in it. Above Ostrand I was shown that the fault was meant. I called it corrupt; I put down a seal upon that word, and walked three hundred miles on it, and thought that I had come to the floor." Second: "He had gone hoarse; he lifted his eyes from the fire for the last of it, and not before." Before "I would have.": "The raw hands had tightened upon the ash; he could have left it there, and it would have been true." **"Sitting across the fire":** Cael now comes round the basket for the page when Seln holds it out and sits on the bucket nobody had used; he is seated when Vastin speaks, and he **gets up off the bucket** to say pole two, which makes the standing a thing he does. Vastin's "You stood up to say it… I sat for mine" in the last scene is now literal.
13. **40:185–217, pole two.** "He had breath left for three words." / "It was Lira, and she had not taken her eyes off him since he got up." / "He stopped there, since the rest of it was not a plan."
14. **37, the light.** The coordinator's three-sentence paragraph is left as it stands; I added nothing to it.

## C. Chains broken (order changed, facts kept)

1. **35, the acquisition.** New order: the word; then, at the tail of his eye, the board's four rows gone aslant, which he takes for the lamp; he looks at his hand and the flame has not moved; then the fifth row and *Goes*; then he knows it and whose it is; then the turned-page image; then his eyes on his knuckles. The recital of how the earlier fragments came is gone from the scene (the stair passage already sets the twelfth beside the others by their fields).
2. **35, the inward test.** New order: the lamp understood; the debt (he will know tomorrow where the finger is going, and must tell); *sixteen*; the made things offering; and last, near the bell, the one temptation, refused in a single present choice on Oryn's order alone. Cleon's limit is no longer set beside it as a second authority.
3. **37, the slip.** Entered late: the smell of paper burning, a white corner with a line and a half of close writing, ash, "Closed."; then a question (Lira: "What is?" / "It is in the dish."); then what Cael works out afterward. Purse and word unchanged.
4. **38, before the reading.** No count of passes. Three unlike checks: a new sign laid against the tall book; "Does it sit, or does it go?" put to Cleon ("Sits. The lot of it sits… Somebody's telling you what was done. He's not telling you to do it."); a word at the foot covered with her glove, predicted, and uncovered. "I can read it." and the single reading stand.
5. **40, Lira and the page.** She reads once, unwatched (Cael watches eight bowls cool and hears one word go by four times); the paper is folded; she says her line to the fire; then the hole and the ruled box; then her thumb on the place and the look across. Cael's recognition is moved into the next scene, under Brom's slow reading.

## D. Orientation cues

1. **Chapter 34, first scene.** Seln names the risk before the ruling ("a bar at the foot of it, and a beam, and a man who writes") and Cael says why he chooses it; Karis's working sheets "were wanted on his tables at the second bell", with three days of the week left; the card is spelled out (one bearer, Karis; a figure of four that means Cael, Lira, Brom and the old man by count; Seln on no card). Vastin's private word about the beam is shortened so that it does not say the same thing twice.
2. **Chapter 37, Oryn.** Her scene opens: "On the evening of that same day, the two hundred and ninety-second, and four gates north of a fork-stone, Oryn was asked to stand by for a child in her fourteenth year." The approach to the bench is one paragraph; a patient who was "an old woman" is now a grandfather, so that the hold's old woman is the only one.

## Trims made to pay for the joins

Chapter 34: the unbroomed third alley; the neck that had not set; "Bring me whatever walks out…"; "Nobody laughed…"; the tail of Seln's repeated ruling. Chapter 35: a duplicated "groom's knowledge of a horse". Chapter 37: Vastin's remark over the dividers; "Cael ate until he could not…"; a line on the tall books; the paragraph on not opening the dividers, shortened. Chapter 38: the Denvash habit in the room's catalogue; the old man's placing; Lira's hand into her coat at the close; two short lines of Karis's. Chapter 39: three sentences of Vastin's cutaway (now 2,243 words). Chapter 40: half of the paragraph on Brom's scale.

## Standing constraints, re-checked on the repaired text

- "four hundred": 38:155 (Karis's paraphrase) and 40:185 (pole two). Exactly two.
- "Architect": 38:147, once. "un-bound": 38:109 (twice) and 38:119 (twice), the leaf; 38:159, Karis's paraphrase; 38:259, her copy. No "unbound".
- *terminal*, *circuit*, *infrastructure*: none. "bearer": only of the card's bearer in chapter 34 (the edition's own term for Karis on the provision's form); never of a sign.
- No possessive before "Path"; no season, month or weekday name; no metric unit; no count of years since the Kindling; no new span of years; no new name. "Cleon" and "Cael" never stand in one line.
- The leaf is quoted by nobody after the reading. Vastin's restored reach is broken off by Karis's "Two pages," as before, and his sentence stays stopped in the cutaway. Nothing joins the leaf to sigils, plates, Arbiters or stations; the light has no likeness.
- Twelve fragments; deployment thirty-two; purse 130; the eleventh undeployed and untold; the twelfth never on a person and never inward; Shadow sealed; the case shut and unnamed; the warning in no book.

## Files

Changed: `manuscript/chapter-34.md` … `chapter-40.md`; `state/movement-006/AUTHOR-REPORT.md` ("New canon minted" and "State at movement end" refreshed, with r1 entries marked; the other sections are the draft's record and still describe the markers as they stood). Written: this file. No git command was run. Nothing outside the seven chapters and `state/movement-006/` was touched.
