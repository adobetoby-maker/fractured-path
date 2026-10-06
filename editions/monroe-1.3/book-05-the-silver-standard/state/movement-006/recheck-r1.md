# Recheck r1 — Book 5, Movement 6 (chapters 33–39), after same-author repair r1

**Seat:** Claude Fable (claude-fable-5-1), standing in for Sol (Codex quota exhausted). Fresh context. Read the full current movement (seven chapters), diffed each against `pre-repair/`, verified every brief item and every coordinator ruling against the page, and reran the four tools named in the template. No manuscript file was edited and git was not run.

---

## VERDICT: CLOSE WITH LINE FIXES

**Scope:** three one-line fixes, none structural, none touching an exchange or a protected line.

1. **ch39** — the clause repair r1 added for Rooke ends "That was hers to choose." The last woman named in the sentence before it is Lira, so on one hearing "hers" can attach to the wrong fighter. Name Karis.
2. **ch37, E2 interval** — "He had taken six contacts on them in the second exchange as well." The page narrates three of Marek's contacts in E2 (the half-beat, the pivot, the board). This is the same checkable-count class the brief fixed in E1 ("eight" → "every contact of that exchange"); the reviewers missed its twin one paragraph on. Make it uncountable in the same way.
3. **ch37, the broadside** — `*0–3 · 2–1 · 1–2 · 1–3*` is the only middle-dot and the only en-dash score in narrated prose anywhere in the edition (the one other digit–digit run, B3 ch21, is a date range on a drill sheet). A narrator has to invent a reading for it. Spell it the way the clerk calls it and the way Rooke reads it in ch36.

One optional echo fix is listed at the end. Everything the brief required is on the page, the arithmetic now adds up in every bout, overlap is 0 unprotected, gates are 0, skeleton is 1%, and all nine M6 protected patterns match once in both current and pre-repair text.

---

## (1) Brief items — each against the diff

### Coordinator rulings

| # | Ruling | On the page | Status |
|---|---|---|---|
| 1 | Calendar accepted; change nothing in M6 | No calendar change in any diff. T5–T10 day words all consistent (see §2). | RESOLVED (nothing to do) |
| 2 | Fair-day veteran is she | ch36 unchanged on this: "a fair-day fighter … she still had the fair-day fighter's habit"; ch38 now "against a fighter the gallery-sheets called buried" (no "man"). | RESOLVED |
| 3 | #39 departures approved, dependent on 1(iii) | 1(iii) delivered; see below. | RESOLVED |
| 4 | New canon approved (lattice PROVISIONAL, left shoulder, figures, Velmere route, scratch offer) | All present and unchanged by the repair; ledger block records them. | RESOLVED |
| 5 | Brom's registry form: `Registry tier at entry: Copper.`, drop "Rank One" | ch38 L7 diff: `-Registry tier at entry: Copper, Rank One.` → `+Registry tier at entry: Copper.` | RESOLVED |

### Priority 1 — fight ledgers

**(i) ch35 E4, the burst count — RESOLVED.**
Diff L241: `-with the last of her floor-sense and a half-burst she could not afford` → `+on foot, with the last of her floor-sense and three hard strides`. Diff L249: `-She spent her last burst, and then she spent the burst after the last` → `+She spent the burst after the last`. The page now spends: survey burst E1 (L67, L109), banked burst at the third corner E2 (L129; "one burst left" L159), "the last burst of her rate" E3 (L199), Rooke's three fingers at the E3 interval (L213), then exactly one over: "the burst after the last, the one she did not have" (L249). Rooke's "a burst you hadn't got" (ch36 L97, singular) is now true, as is "tightening round the burst she had not had" (ch35 L275) and the ledger's "one burst over her rate of three". Kept as required: "She spent the burst after the last", "Nothing she gave up was given. All of it had to be taken.", the three fingers.

**(ii) ch37 E1, the fifth stake — RESOLVED.**
Diff L111: `-And the fifth went somewhere Cael had never charted at all.` → `+And the fifth went to a gap Cael had charted only on the oak at home, where the whole floor gave, and had never thought to look for here.` This is the fourth of Cael's four by the kitchen door (L31, the back heel "on any floor that gave at all"), so "He found six. I knew about four." (L315) now holds: Marek's six = shoulder, half-beat, pivot, left-turn start, heel board, breath; Cael's four = half-beat, left turn, shoulder, heel; the two unknown = pivot and breath. "He found the gap in the ground Brom had chosen himself" (L119) kept.

**(iii) ch37 E3, the last point — RESOLVED, and 3–1 reads on first pass.**
Diff L201: `-and paid for it as he had paid for it every time before. Brom's return took the third point.` → `+His touch there came a hair late, a glance off the forearm rather than a strike, and no flag rose for it. Brom's return did not glance. It took the third point.` E3 as narrated: Marek 0–1 (L171), Brom 1–1 (L177), Brom 2–1 (L187), the sixth-gap pair both unflagged (L193, "the panel let both lie"), Marek's glance unflagged, Brom's return 3–1 (L201–203). Bout 7–6 after three (L203), 9–6 after two points of E4 (L267), 10–6 (L283). "No fighter on earth could draw level from four points down with a single exchange left" (L267) is now arithmetically true (margin four, a fifth exchange worth at most three), and Umber's "a point from the end of everything" (L255) lands at 9–6. Matches the ledger's "1–3 / 3–2 / 3–1 / 3–0 = 10–6 in four".

### Priority 2 — the shoulder gate closes once — RESOLVED (subtraction only)

- **(a) cut** — Diff L213: the forward-flash "Cael, going back through his charts that night, would find …" is gone. What remains is live: Marek walks every gap but one (L209–215), "Brom … watched Marek not look. Then he breathed out" (L217).
- **(b) kept** — Umber's section is byte-identical except the struck-judge line (optional item). "the honesty of the work" (L233) and "A trick was a thing done once to a man who did not know. This was a thing built in plain sight." (L247) present.
- **(c) trimmed** — Diff L275: `-at the cheapest gap on the floor, the one he was sure of, the one he had not needed to check.` → `+at the gap he was sure of.` Diff L279: "For three exchanges Brom had let that shoulder go cheap … The redirect was complete." → `+Everything the morning had paid into Brom's forearms came out of them at once, at the one angle he had kept cheap for exactly this.` plus the strongbox lid (L277) and "a sound the whole floor heard" (L279). Diff L287: "He had absorbed six clean scores … to sell one number." cut.
- **(d) kept** — L311 "I'd written it to be read that way" whole.
- **(e)** — Diff L325–327: the notebook's con-restating paragraph is cut; the entry now opens "*I sat at the rail today and thought about my own record*" and carries Cael's file. "Brom forged one line, once, in the open, for one bout" stays as Cael's comparison, not a restatement.
- Every exchange and every touch is unchanged (verified: no diff hunk touches L79–203 other than the three fixes above). "He found six. I knew about four. … the best inspection I've ever had." (L315) and the E4 arithmetic paragraph (L267) kept whole.

**Trick-count after repair:** the shoulder's pricing is now explained once from the mark's side (Umber), confirmed once by Brom's own mouth, and felt once at the rail. E4 is still seen twice (Umber, then Cael), but the brief chose to keep Umber's pass and the rail pass is now 15 lines of event, not explanation. This is what was asked.

### Priority 3 — continuity set — all RESOLVED

| Item | Diff evidence |
|---|---|
| ch36 stair | L229 `-While you were all at Brom's bout.` → `+Before Brom's semifinal, while you were all at his quarterfinal.` Karis speaks three times at the semifinal rail (L11, L33) and is now not claimed absent from it. |
| pencil → ink | ch36 L205 `-with my pencil` → `+with my pen`. Agrees with "the ink on her palm, smudged now" (L209) and ch38 L249 "the ink of last night's line … cooked away". Lira writes her own hand in ink (ch33 L229). Her back-room pencil (ch33 L151) is a different object and not contradicted. |
| ch38 Ilsev | L11 `-the bout before that had gone five exchanges against a man the gallery-sheets called buried` → `+against a fighter the gallery-sheets called buried, and a bout in the second round had gone five exchanges`. Agrees with M5 (round two 9–7 in five; ledger L847, L890) and ch36 (semifinal 24/23 in four; the buried sheet is hers). |
| day counts | ch34 L255 `-The day after tomorrow` → `+Tomorrow`; ch35 L9 `-rewound two nights before` → `+rewound the night before`. The little-room scene and the strap-rewinding are T7 (ch34 L261), the bout T8. Both now agree with the ch36/38/39 numbering. |
| ch36 boards | L145 `+You did it twice this morning, in one exchange,` — pays off Lira's "She said I did it twice" (L159) and Cael's "The second time was the corner under the dais" (L161). |
| ch34 Rhagen | L177 `-he said` → `+said Brom`. |
| ch36 "glass" | L7 `-in the fourth glass` → `+in the fourth exchange`. |
| ch38 form | ruling 5, above. |

### Optional items — all taken; checked

| Item | Diff | Note |
|---|---|---|
| ch36 want tag | L173 `+Lira did not look away from the fire. "It's a better want. It costs more."` | Protected item 41's final pair is now contiguous; verified against BOOK_MAP §10 line 60. |
| ch37 Umber judge | L251 `+He had struck a judge from the lists on the eve of the opening … and the five below him knew it.` | Agrees with ledger ("before the opening"). Small echo of "The five below him" two sentences earlier — optional fix below. |
| ch37 eight contacts | L127 `+His forearms had taken every contact of that exchange` | Good. Its twin at L161 ("six contacts … in the second exchange") was not in the brief and is fix 2. |
| ch38 E5 | L185 `+One more touch from Karis would close the fifth and win it. If Ivenne did, there would be more of it, and Karis had very little left for more.` | At 9–9 the exchange stands 2–1 Karis; a Karis touch closes at three (10–9), an Ivenne touch leaves it open. Correct under #39. The author reworded one sentence after a 0.50 skeleton hit; the probe now shows ch38 skeleton 0%. |
| ch36 grey paper | L109 `+the grey paper Withrow used for everything` | Withrow is Halcenvane's chancellor; "registry-grey" was the wrong house. Good. |
| ch34 lattice clause | L35 `+which had nothing to do with the Lattice Path's invisible lines` | Checked against the B4 edition's own words: "Lattice builds things in the air, lad. Lines. You can't see them, mostly, unless the light's right." The edition names the Path "Lattice" (porter, the twenty-two Paths), so "the Lattice Path" is the natural form. Accurate. |
| ch39 Rooke's reason | L131 `+Rooke let it stand. A strained shoulder got worse with every burst, he told Cael afterward, and that was why Lira was on half work. Burnt palms only hurt more. That was hers to choose.` | Reason is sound and inside Rooke's knowledge. "hers" — fix 1. |
| ch33 Ephram | L207 cut "Ephram told them later what it was …"; L215–217 Lira asks at the rail and Ephram answers in his own words. | The three time-frames are gone; the tip survives in dialogue; "She looked as though you'd handed her something" pays off "face change a little". Clean. |

**Declined by the author:** none. **Dangling referents after the cuts:** checked every cut region's neighbours. ch33 L207 "Then he walked off the floor" now follows "their own work" cleanly. ch37 L213–215 ("It was the first gap he had found … Marek did not check it. It was the one he was sure of.") stands without the cut sentence. L275 "the gap he was sure of" and L279 "the one angle he had kept cheap for exactly this" both have Umber's account (L237–241) and L215 before them. L287 "He rolled his right shoulder once … the shoulder Marek had touched first and touched last" is true (L97, L273). ch37 L325 "after the ceremony and the letter" is the pre-existing forward reference to ch39's T9 evening, unchanged. No pronoun, reference or time-word points at something no longer on the page.

---

## (2) Continuity

**Calendar (T5–T10, house days only).** ch33: "the fourth day" (Lira's R2, banked), "the sixth day" (Ephram's R16); ch34 "the next day" (T7), "Tomorrow" (T7→T8); ch35 "the night before" (T7); ch36 "the night before" twice (Lira on the stair T7; Karis's page T7), midnight (T8); ch37 "yesterday" (T8 from T9); ch38 "the ninth day", "the night before" (the burning, T8); ch39 "the ninth day" (plaque), "that same evening", "as Lira had the night before" (T8 vs T9), "the tenth day" (Karis's SF), "the day before" (Brom's final T9 from the ring night T10), "last night" twice (Karis's finding, written T9, read T10). All consistent with the ledger table and the coordinator's T5–T10 ruling. No season, month or metre word anywhere in the seven chapters.

**Counts and figures.** Every bout call matches its narration: Lira QF 1–2 / 3–0 / 3–1 / 3–0 = 10–3; Ephram 1–3 / 2–2 / 1–3 / 2–3 = 6–11; Lira–Zerin 0–3 / 2–1 / 1–2 / 1–3 = 4–9, figures 29/27; Brom QF three exchanges; Brom SF 1–1 / 2–1 / 2–1 / 3–0 = 8–3, figures 24/23; Brom–Marek 1–3 / 3–2 / 3–1 / 3–0 = 10–6, figures 25/25; Karis–Ivenne 0–3 / 3–1 / 1–3 / 3–1 / 3–1 = 10–9, figures 25/24; Karis SF 2–1 / 1–3 / 2–2 / 0–3 = 5–9, figures 27/23. Early closes all satisfy "could not draw level". "Eleven minutes" appears for each board interval. Lira's bursts: three plus one over (above). Brom's gaps: six found, four known (above).

**Knowledge boundaries and reserved truths.** The repair added three pieces of speech (Ephram's tip, Rooke's reason, the lattice clause) and removed text; none approaches the mechanism, the chair, Vastin, Daeva or Kindling counts. The editorial's §4.5 findings stand unchanged. Ilsev's form now mints no rank (ruling 5).

**Protected lines.** All nine M6 patterns in `protected-patterns.txt` (lines 31–39) match exactly once in the current text and once in pre-repair (normalised match, same tool logic). BOOK_MAP §10 items 41, 42 and 43 verified word for word on the page: item 41's four parts (ch36 L141, L143, L145, L169, L173), item 42 (ch36 L123; ch39 L61; ch39 L53), item 43 (ch36 L219–221, L239; ch39 L89–97). The only protected-adjacent change is the tag move in item 41, which improves it.

**Previous movement / later canon.** Brom's round two in five (M5) is now cited correctly in ch38. The fair-day Copper's "Second time's the real rating" and Brom's "Somebody ought to file for her" are untouched. The Velmere line is the map's ten words exactly. Nothing in M6 forecloses M7's re-dated spine.

---

## (3) Formula — reproduced

`python3 editions/monroe-1.3/tools/formula_metrics.py` on chapter-33 … 39 (current):

| Measure | Value | Target |
|---|---|---|
| words_prose | 34,402 | — |
| sentence_mean | 13.52 | 14.6 |
| sentence_median | 9 | 11 |
| share_le5_words | 0.265 | — |
| share_ge40_words | 0.034 | — |
| paragraph_median | 28 | — |
| scene_breaks_marked | 30 | — |
| words_per_scene | 929.8 | 950 |
| flesch_reading_ease | 87.7 | 72.3 |
| flesch_kincaid_grade | 4.38 | 6.8 |

Matches the author's post-repair table (13.52 / 3.4% / 26.5% / 28 / 930). The pre-repair `metrics.txt` was 34,512 words, mean 13.58; the repair removed about 110 words net. The sentence mean and grade sit below target by the same margin they did before repair and in M5; the repair did not move them, and they are not this recheck's finding.

`ed.sh overlap book-05-the-silver-standard 6`: **0 unprotected** shared runs of ≥8 words; 17 protected (allowed).

`ed.sh gates book-05-the-silver-standard 6`: reader_standard=0, metadata=0, modern=0 on all seven chapters (33: 4968 w · 34: 5006 · 35: 4803 · 36: 4436 · 37: 5534 · 38: 5036 · 39: 4696).

`sweep_probe.sh book-05-the-silver-standard 6 6`: TOTAL sentences=1490, **skeleton 1%**, close 7%. By chapter: 33 0%/2% · 34 2%/9% · 35 0%/6% · 36 3%/10% · 37 0%/5% · 38 0%/7% · 39 2%/6%. Target (≤2% skeleton) met on the movement.

---

## (4) Reader clarity

- **Speaker attribution.** Every line of dialogue in the seven chapters is attributable on one pass. The two the brief raised (ch34 "Come on", ch36 the want) are fixed. Ephram's new rail exchange (ch33 L215–217) is tagged on both sides.
- **Referents.** Checked above under "dangling referents". The one weak pronoun is the repair's own "hers" (fix 1).
- **The 13-year-old lens.** The book asks this reader to count, and after repair every count she can check comes out: three bursts and one over; four gaps and six; 7–6 then 10–6; 9–9 and whose touch wins. The one count left that does not come out is E2's "six contacts" (fix 2). The lattice clause is a kindness to a listener who met Lattice in Book 4.
- **Reader Standard.** Unchanged by repair; clean.

---

## (5) Listening proof — every chapter, every changed region

Mechanical pass over all seven files: straight double quotes balance on every paragraph (0 odd); asterisks balance on every paragraph (0 odd); every `---` has a blank line before and after (0 findings); no curly quotes, no three-dot ellipses, no double hyphens, no trailing whitespace; no abbreviations (the only "No." hits are the spoken word); digits appear only in chapter headings and three italic board/form lines (ch36 L135, ch37 L7, ch38 L7).

- **ch33.** Changed region (L207, L215–217): reads cleanly aloud; "runs thin on her left once she shortens the count" is one breath. "the twentieth of Reaping" is a B4 recollection and planned. Clean.
- **ch34.** L35: "a lattice, which had nothing to do with the Lattice Path's invisible lines, and Cael had learned the shape" — the parenthetical lands between commas and does not collide with "lattice" a second time in the sentence. L177 "said Brom" clean. L255 "Tomorrow the two of us" clean. No numerals. Clean.
- **ch35.** L9 "rewound the night before" clean. L241 "on foot, with the last of her floor-sense and three hard strides" — "foot/floor" alliteration is fine aloud. L249 "She spent the burst after the last, the one she did not have" — the sentence now opens on its subject and is easier to voice than before. Clean.
- **ch36.** L7 "in the fourth exchange" clean. L109 "the grey paper Withrow used for everything" clean. L135 board "9." / "4." — narrator says "nine", "four", same precedent as M5's "IRON 9". L145 "You did it twice this morning, in one exchange, in front of my whole house" — three commas, one breath each, Zerin's flat delivery survives. L173 "Lira did not look away from the fire." then the pair: clean. L205 "with my pen, because she'd left hers on the table" — "pen/pens" no collision. L229 "Before Brom's semifinal, while you were all at his quarterfinal." — two "-final" words in one breath; intelligible, slightly heavy; not a fix. Clean.
- **ch37.** L7 `*0–3 · 2–1 · 1–2 · 1–3*` — the one genuine misvoice risk in the movement (fix 3). L111 new sentence is long but single-clause-per-comma. L127 "every contact of that exchange" clean. L201 "came a hair late, a glance off the forearm rather than a strike, and no flag rose for it. Brom's return did not glance." — "glance/glance" is a deliberate turn and reads well. L251 "The five below him would rate it … and the five below him knew it." — echo across two sentences (optional fix). L279 clean. L325 the notebook opens on "I sat at the rail today" — clean join to "Cael wrote that night". Clean apart from fix 3.
- **ch38.** L7 form "Figure: 25." — "twenty-five", planned text. L11 "against a fighter the gallery-sheets called buried, and a bout in the second round had gone five exchanges, and the line …" — three "and"s in a row is Ilsev's ledger cadence and was there before. L185 new E5 sentences: "One more touch from Karis would close the fifth and win it. If Ivenne did, there would be more of it, and Karis had very little left for more." — "more of it / left for more" is a deliberate chime; voices cleanly. Clean.
- **ch39.** L131 the Rooke clause: "That was hers to choose." — fix 1 for referent, not for sound. Everything else unchanged and clean; "Three floors" / "three of us" / "all three" in the closing Log is the chapter's device.

---

## Line fixes (apply on CLOSE)

Each `old` string verified with `grep -c -F` to occur exactly once in its file.

1. `manuscript/chapter-39.md`
   old: `That was hers to choose.`
   new: `That was for Karis to choose.`

2. `manuscript/chapter-37.md`
   old: `He had taken six contacts on them in the second exchange as well, and every one had been a strike he had chosen to take so that he could charge for it`
   new: `He had taken every contact of the second exchange on them as well, and each had been a strike he had chosen to take so that he could charge for it`

3. `manuscript/chapter-37.md`
   old: `*0–3 · 2–1 · 1–2 · 1–3*`
   new: `*nought to three, two to one, one to two, one to three*`

## Optional (coordinator's discretion; listening only)

4. `manuscript/chapter-37.md`
   old: `and the five below him knew it.`
   new: `and the five knew it.`

---

**For the ledger on CLOSE:** the "After Movement 6" block's rulings paragraph already states the post-repair end-state correctly (E3's last Marek touch an unflagged glance; 7–6 after three; one burst over on the diagonal cut on foot; Copper with no rank; the struck judge "before the opening"). Nothing in this recheck changes it. AUTHORSHIP: author claude-opus-5-5; reviews Claude Fable ×2; recheck Claude Fable (for Sol).
