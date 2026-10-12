# REPAIR REPORT r1 — Book 8, Movement 8 "The Sunken Span" (ch47–53)

Author seat: O'Connor 1.3 (Monroe 1.3 voice), `claude-opus-5-5`. Date: 2026-10-12.
Baseline: `pre-repair-r1/`. Nothing committed, nothing pushed. Files touched: `manuscript/chapter-47.md … chapter-53.md`, `state/movement-008/AUTHOR-REPORT.md`, and this file.

## 1. Method, and what was and was not read

- Read in full: `REPAIR-BRIEF.md`, `plan-audit-apply.md`, `source-tracking.md`, `review-editorial.md`, `review-cold.md`.
- `plan-audit.md`: findings only (lines 1–139 and 161–248). **Not read:** the "Minimal-versus-full source notes" table (140–160) and the "Exact line fixes" list (249 to the end).
- Nothing under `books/` or `v3-runs/` was opened.
- **Source-derived words that reached me through the permitted reads**, declared so that the recheck can look for them: `source-tracking.md` quotes two short phrases of the old text ("The floors face the line…" and "Whoever cut them knew where the next one was."), and the audit's findings describe some old staging in prose (which speaker had which line; that the old text used the bad leg). None of those words is on the page. The C2 recomposition was built to move away from the second phrase, not toward it (see C2).
- Rhythm was tuned by hand, sentence by sentence, with exact-string replacements. No rule-based splitting or joining was run.

## 2. Results, as printed

Formula metrics (`formula_metrics.py`, marker lines stripped):

| ch | words | sentence mean (13.3–14.2) | ≥40-word share (2.5–4.5%) | words/scene (850–1,050) | scenes |
|---|---|---|---|---|---|
| 47 | 5,016 | 13.74 | 3.8% | 1,003 | 5 |
| 48 | 5,405 | 13.79 | 4.1% | 901 | 6 |
| 49 | 5,573 | 14.00 | 2.8% | 929 | 6 |
| 50 | 5,755 | 14.11 | 3.9% | 959 | 6 |
| 51 | 5,541 | 13.65 | 3.9% | 924 | 6 |
| 52 | 5,154 | 14.08 | 2.7% | 1,031 | 5 |
| 53 | 4,690 | 13.79 | 4.4% | 938 | 5 |

Movement: 37,134 words by the metric's count; 2,675 sentences; mean 13.88; ≥40 share 3.7%; 952 words/scene. Every chapter is inside all three working ranges.

`ed.sh gates book-08-before-the-paths 8`:

```
chapter-47.md words=5027 reader_standard=0 metadata=0 modern=0
chapter-48.md words=5416 reader_standard=0 metadata=0 modern=0
chapter-49.md words=5586 reader_standard=0 metadata=0 modern=0
chapter-50.md words=5766 reader_standard=0 metadata=0 modern=0
chapter-51.md words=5552 reader_standard=0 metadata=0 modern=0
chapter-52.md words=5165 reader_standard=0 metadata=0 modern=0
chapter-53.md words=4703 reader_standard=0 metadata=0 modern=0
```

`ed.sh overlap book-08-before-the-paths 8`:

```
# summary: 0 unprotected shared runs of >= 8 words; 20 protected runs (allowed)
```

`{{JOIN}}`: 0 in every chapter. `[[TIER-B`: 0 in every chapter.

**The movement did not grow.** By `wc -w`: 37,243 at baseline, 37,215 now (−28).

| ch | baseline | now | change | why |
|---|---|---|---|---|
| 47 | 5,047 | 5,027 | −20 | make-up of the twelve added; four cuts pay for it |
| 48 | 5,436 | 5,416 | −20 | role ties; two cuts |
| 49 | 5,597 | 5,586 | −11 | two joins; one cut |
| 50 | 5,608 | 5,766 | +158 | four restored units needed staging (B3–B6) and the positions paragraph; cuts recovered part |
| 51 | 5,553 | 5,552 | −1 | ties and one join against one cut |
| 52 | 5,186 | 5,165 | −21 | C1 and C2 recomposed; orienting clauses; cuts |
| 53 | 4,816 | 4,703 | −113 | C1: the counted reduction is gone |

Chapter 50 is the one chapter that is longer. It carries four of the ten restorations, and three of them (the entry, the handing-over, the call across the iron) had no staging at all on the baseline page.

Protected units: 37 strings checked, each whole and once. Teague's `"Noted," said Teague.` stands twice by design (49:169, to Cael's term; 51:23, to Oryn).

## 3. Section B — the joins

| # | Where | What stands now |
|---|---|---|
| B1 | 49:97 | `"They knew," said Karis, under her breath.` Seln's answer follows as before. |
| B2 | 49:167 | The term stands with no tag. The lead-in carries it ("He gave it as a term…"), and Teague's "Noted" answers at 49:169. |
| B3 | 50:115–117 | `"Through," said Teague.` then: "He said it to the place where two timbers had stood, and not to his arm." |
| B4 | 50:173–177 | Framed as Cael's entry, in his head, "before a boot went over, and in the tense that it would have to be true in afterward"; the fixed sentence alone in italics. Karis's "And theirs?" / "Nothing that we do not…" exchange above it is cut, as the brief allowed, so the line is said once. Her "It is ground." stays. |
| B5 | 50:179–185 | Teague turns his head "for the first time that morning" to the boy behind his left shoulder: "You've stood on three of them. I've stood on none. Say how." / `"By count," said Cael.` The words "This isn't field" are not used. The crossing follows as written. |
| B6 | 50:253–259 | Called by the watch's empty-handed man, "thick through a cloth… as a person calls to a child on thin ice"; `"We've been in three times," said Cael.` with one line glossing *we* as the crew that has stood on three floors. |
| B7 | 51:21–27 | Oryn / `"Noted," said Teague.` / "He had not looked round at her." / `"Everybody says that now," said Oryn, to the timber under her.` The cutaway's "three short sentences" was checked against the restored speech: it is three sentences. |
| B8 | 51:327–329 | "She read it off the stone, once, as she read a figure." / `"Through," said Karis.` |
| B9 | 52:255–261 | Brom asks who the somebody else is, "that can say no to a thing like that, and put wax on it." / `"The Compact," said Vastin.` / join: he hears how that sounds on a hillside, and his eyes go once more to the two wafers / `"Yes. Part of it."` He names neither seal. |
| B10 | 53:287–303 | Join 1 (53:293): "She took her finger from the paper, and looked up at him." Join 2 (53:301): "He found that he knew, and he told her." Cael's "And it's on the line" is tagged plainly. The fixed last line follows. |
| B11 | 51:63; 51:339; 53:171, 53:217 | Left exactly as the coordinator set them. Checked: Lira's line has no plank; Karis looks under the hide and comes back saying nothing; "for years" twice, and no "five years" anywhere. |

## 4. Section C — recomposed

**C1, the year.**

- *Blanket (52:125–135).* She recognises the two signs as a year written by its first letters and says that she has "exactly one other year in that count", at the head of a thing she read aloud once. Her eyes go to the pebble on the folded copy; "She did not reach for it, and she did not turn back a leaf of her notebook." She says that she will not lay the one beside the other on a blanket, will work it that night alone, and will say a figure once. Gone: the side-by-side comparison, "the same two letters", "the same hundred", "I think that I do". The thumbnail ring stands.
- *Night (53:159–169).* "She worked it through on the lid, twice, with her left hand kept off the wood. / It would not close… a year that is written by its first letters is a year with a door left open in it." Her entry: "*not shown to be the same year; shown to be near it.*" To the nearest hundred, "or near it", once. Gone: "eleven", the row of candidates, "fourth from the top", and the sentence that placed the year within a few years of the leaf's ruling. Everything from "It came to her as she blotted the line" onward is untouched, and so are the two pages on the lid (A2).

**C2, the tracked chain (was 52:79–101; now 52:73–97).** The order of perception is turned round and the inference changes hands.

1. Cael has it by the brass first: nothing on the blanket lies across that strip. He says "They go east."
2. Karis enters only "that the rows agree with the brass, and which way", as his, unchecked.
3. "On to the next" is Lira's ("Then they point on… Each one at the next."), and Karis refuses it on the page: going east the next is the older every time, so a thing that leans at what was there before it "may as well be looking back as going on. I have that they lie one way. I have not what for."

The fact the plan needs (the rows lean along the bearing) is kept. The maker-facing conclusion is offered and declined, and is left for a later page.

**C3, anchors for a listener.**

- *How twelve is made:* 47:9–11, once. Twelve and a mule; six on one side of a contract with an old man counted among them now, a captain's four on the other; "two healers, whom the count of ten left out, since a healer is not sent." The same paragraph ties "Teague's boy, the youngest of his four" and "the broad man with the crossbow, whom his own crew called the bow".
- *Role to person at re-entries:* 47:29, 47:153; 48:25 ("The broad man, the bow of Teague's crew"), 48:199; 49:15, 49:291; 51:5; 51:85, 51:87 and 51:147 (the Teague cutaway: "that was the broad man, nearest the door, with his leg on a board", "The spear, his tall man", "The other boy, the one with the book" for Cael); 53:5, 53:39. "The boy" unqualified is now Cael only where Teague's boy is not in the scene.
- *Before the fastest action:* 50:7, one paragraph of positions as a captain set them, each of Teague's four tied to his weapon; 50:219 renames the four on the shale at the turn.
- *The blanket's three turns:* 52:41 ("She meant to lay the whole line out upon it as it lay across the country."); 52:113 ("The country was laid out; what she wanted of the blanket now was a year."); 52:217 ("The blanket's last work that day was his.").
- *Which paper:* "the folded copy" (52:133, 52:193), "six of the office's sheets… one out of each taped row of the flat" (52:115), "the oldest of the flat's six taped rows" (52:217). The hide, the fourteen wall sheets and the torn ruled leaf keep the names they had.

**C4.** No cadence pass was undertaken.

## 5. Cuts made so that the movement should not grow

- ch47: the "sore place" paragraph at the hall; "It had not altered by a blade."; Cael's fifty-paces memory at the cairn; the hare-and-cart sentence about Teague compressed.
- ch48: the "read, and nothing else" paragraph trimmed; "Whenever the file stood, he heard the two of them stop on the one tap."
- ch49: "He had said it to himself as much as to her."
- ch50: the "And theirs?" exchange (B4); the timbers-carted sentence; the "beaten" sentences; the light-relit sentences; "It had been lying beside them…".
- ch51: the boy's "second helping" paragraph.
- ch52: Brom's "All of what?" exchange, folded into Karis's line; the made-things sentences; most of the last "Nobody pried" paragraph.
- ch53: the counted reduction (C1); "He had first seen that skin on a board in a meadow, with one ring."

None of these carried a plan beat or a protected unit.

## 6. Slips I made during the repair and corrected

- The first application of the joins took the movement to 37,425 and put ch52 out of range (mean 14.30; 1,052 words/scene). Offsetting cuts and five hand splits brought it back.
- A new phrase gave the wrong interval for the broad man's "aye"; it is removed. "Aye" is still his one word to the six, on the 305th.
- "Teague had turned his head at last" (crossing) contradicted the new, earlier head-turn at B5; it now reads "Teague's head had come farther round… to where his own boy stood" (50:203).

## 7. KEPT items, confirmed untouched

The read at the seep and deployment thirty-three; Karis's night with the two pages and "*Second page: nothing entered.*"; the gloss after the log; Seln's "There is one to a year."; Oryn not told of the thirteenth; everything listed at A6.

## 8. For the coordinator

1. **`AUTHOR-REPORT.md`** is refreshed in "New canon minted" and "State at movement end" only (eighteen replacements, each flagged "(r1)" where it changes a fact). Its per-chapter table, "Markers left" and "Owner flags" are still the first draft's and are marked as such in a note at its head; this report's section 2 has the current figures.
2. **Facts that changed for Movement 9's author:** Teague handed Cael the ground past the iron ("Say how." / "By count"); Cael answered the watch's call; Teague has said "Noted" twice; Karis has the agreement of the rows with the brass and has refused "the next" (Lira offered it); Karis has said nothing aloud about the year beyond "one other year in that count", has "near it" and not a number of candidates on her page, and said the figure once at the close; both "Compact" lines are Vastin's; Karis holds no bar, so no stake thirty-four travels with the six.
3. **One judgement to check:** at B2 the term carries no attribution tag at all. The lead-in names Cael as the speaker and Teague answers him, but if the recheck wants a tag for a listener, `said Cael` after "Noted?" costs two words.
4. **`EVENT-LIST.md`** was written before the audit and was not in the brief; I have not revised it. Where it differs from this report, this report is current.
