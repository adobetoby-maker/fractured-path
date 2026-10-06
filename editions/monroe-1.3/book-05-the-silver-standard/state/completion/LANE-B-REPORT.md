# Book 5 completion pass, Step 3: Lane B report (ch31–60)

Seat: O'Connor 1.3 author (Claude Opus 5.5), same-author texture pass.
Method: I read every chapter from ch31 to ch60 in full and in order. Each change was chosen by reading and applied as an exact-string replacement in place, one sentence at a time. No pattern was ever applied across the range.
Scope: only ch31–60 were edited. I changed no file in ch1–30, made no git calls and printed no secrets.

## 1. Priority 1 counts (grep over ch31–60, before → after)

Patterns are case-insensitive `grep -oiE`, using the script `scratchpad/b5-laneB/count.sh`. The baseline was taken from an untouched copy of ch31–60, made before the first edit.

| Target | Before | After | Notes |
|---|---|---|---|
| square / squared | 71 | 40 | Nearly all of the 40 are now nouns: the square hall, the pale square on seat twelve, square brackets, the court's square. The gesture stays with Seln (ch32, 33, 43, 54; the strip in ch53 is kept whole), Ilsev's form (ch38) and Umber (ch31, 50). ch60:129 is inside the convening window and was left. |
| flat / flatly | 90 | 35 | About one a chapter. Kept where it is physical or is the point: Hesk's book lies flat (ch44), the lane's pressed air, Rooke's tap on card four, Vastin's hand. |
| superlative-ever (regex) | 27 | 12 | Of the 12, three are protected (ch39 Ivenne's "best document", ch59 "fairest instrument ever built", ch59 "First honest warning"). One is a keep: Daeva's "never in her life been so happy" (ch57). The other eight are not superlatives; the regex only catches "ever" or "never in her life". Karis's "worst moment of her life" (ch56) is kept; the regex misses it. Lane B now holds exactly its two. |
| "as X ⟨verb⟩ everything" | 9 | 3 | Kept: Brom's first "honestly, as he considered everything" (ch37) and Ilsev's only one (ch58). The third hit is "as though that settled everything" (ch36), which is not the gloss. Cut: Karis ×3, Seln, Brom ×2, Vastin, Zerin, Lira, Cael. |
| for a (long) moment | 62 | 41 | Kept freely in ch57 and ch58. Elsewhere only where the pause carries a beat. |
| for a while | 40 | 30 | |
| Nobody said anything | 17 | 8 | |
| said nothing / did not say anything | 34 | 24 | |
| Nobody spoke | 5 | 5 | Left as written. Three come before a protected or pivotal line (Withrow's "parts", "The doctrine is filling", "Approve it…"). The other two are Withrow's toast (ch52) and the rail during the match (ch55). |
| a fraction | 17 | 10 | Now one per bout. Some became "half a beat", the book's own unit, so "half a beat" went from 28 to 32. |
| a stride | 49 | 26 | Shares now with "a pace", "a yard" and "an arm's length". The trial-floor callback "a stride's length" is kept. |
| eleven / eleventh | 53 | 39 | Every move in the brief is done (see §2). Canon kept: the roster's eleven names, eleven minutes, eleven questions, eleven relocations and "Nobody ever gives us eleven", the entry's eleven words, eleventh of fourteen, the eleventh bell, the lock-keeper's eleven verses and Seln's "Eleven", and "On the eleventh day" (a date). |
| ears | 7 | 5 | Only one Ephram ears line is left in Lane B: the coast Blade's handshake (ch32:153), kept as the brief's "one handshake". The stout man and the Auremont head lost their red ears. The other four hits are "ears popped" and the like. |
| crowd-sound simile | 2 | 1 | I also thinned similes the grep misses: the juggler (ch55), the song (ch42), the horse race (ch35), the graveside (ch56). Each bout now has at most one. |
| to nobody (in particular) | 9 | 2 | Left: the keeper's cheese "for nobody in particular" (ch52, dialogue) and ch53's "looking at nothing in particular". |
| nodded (,) once | 14 | 5 | Kept: Umber like a carpenter (ch31), Brom with the plaque (ch39), Rooke on "Silver is not a bigger Iron" (ch40), the captain on the crown (ch41, kept because ch59 calls it back) and the captain in ch59. |
| very still | 12 | 3 | Kept: Ivenne's face (ch38, set against Karis's "stiller"), Daeva at "Neither number is us" (ch52) and the house lying still (ch53). |
| which from X was | 3 | 1 | Bracken's remark (ch60). Brom's "close to a declaration" (ch34) uses "in", so the grep misses it. |
| He/She found that he/she | 7 | 2 | |
| That was all. / That was the whole of it. | 4 | 2 | Kept in ch58, "That was all. But it was a great deal.", inside the hour. |
| like a man who | 6 | 3 | |
| rain on a roof | 3 | 1 | Kept in ch40, the Rhagen block writing. ch50 became a mill-race; ch58's clocks became a dry, steady pattering. |
| pond / stone-into | 2 | 0 | Both pond uses in ch56 are gone. ch40's "stones into a lake" is kept as Lane B's one. |
| like a dog that | 2 | 0 | ch55 is now a slow clock and ch59 a kettle. ch32's comic "as a dog goes for a dropped sausage" is kept as Lane B's one dog. |
| horse (buyer / backed / fair) | 3 | 1 | Kept: ch35's buyer, as Lane B's half of the pair. The race simile (ch35) and the horse fair (ch36) are gone. |
| sum-checked nod | 3 | 1 | Kept: Brom's long nod (ch41:269). ch41:57 (the captain) and ch59:133 are gone; ch58's "figure came out right" nod went with them. |
| a wave breaking / turning | 3 | 2 | ch31's pair is kept as one image with its own callback ("That had been a wave breaking"). ch59's wave is gone. |
| "wrote it that night / at the window" | 4 | 1 | Kept: the pivot entry "at the window" (ch41). I varied about a dozen other introductions (ch31, 32, 33, 36, 38, 46, 50, 60). Every entry is still there. |
| wrote it down | 14 | 13 | |

The back room's rocking table and pump are now named at most every other visit: ch33 names both; ch41 the pump only; ch48 both; ch53 neither; ch58 the table; ch59 neither.

## 2. The elevens moved (for the ledger)

| Place | Was | Now |
|---|---|---|
| ch33:109, :259 | Zerin, "Eleven exchanges" | "Ten exchanges" (both) |
| ch34:237 | Zerin's commercial file, eleven pages; read the first ten; the eleventh kept back | **seven** pages; the first six; the seventh |
| ch49:81 | the enrollee's (Cael's) shop file, "Eleven pages in grey board" | "Nine pages". Lane A's clerk's notebook (ch18) is now "Twenty pages", so all three documents differ. |
| ch44:43 | the proprietor "opened the door at eleven" | "at ten" (not on the brief's list) |
| ch44:183 | Seln's whistling clerk, "eleven days by coach" | "nine days by coach" |
| ch51:9 | the hill's crown, "the eleven paces at its middle" | "the ten paces" |
| ch51:227 | "Eleven houses heard their sittings first." | Cut. "Halcenvane was twelfth to be read." stands alone. |
| ch53:51–53 | "eleven more in that" / "wanted the eleven" | "a dozen more" / "wanted the dozen" |
| ch53:65 | "The eleventh thing… under ten others" | "The tenth thing… under nine others" (not on the brief's list) |
| ch56:109 | "eleven seconds by a carter's count" | "ten seconds" |
| ch60:135 | "There were eleven of them now" (the guesses) | "a dozen" |

STATE_LEDGER still carries the old figures at lines 1068, 1111, 1163, 1373, 1550 and 1743. Two other ledger facts changed. The bay at each gate of the first ring is now "a yard deep" in ch40 (×3) and ch41 (×1); it was "a stride". The ledger's "ledgers turned face down 'like men at a graveside'" (line 1743) has lost its simile.

## 3. Priority 2: economy

- **ch51.** I cut the first exchange's recap of the semifinal's shapes to one sentence. That sentence is Ephram's trade, with Lira ready and not early, Brom two strides wide, Karis's door downhill and Cael reading. I also trimmed the guard paragraph and the uphill paragraph. Every touch and holding in the exchange is kept, along with the exchange to Rhagen by a handful of quarter-minutes. Lines 79–105 went from 603 to about 374 words, and the chapter lost 200. The second exchange is untouched.
- **ch47.** Nothing added. I made five line trims only (one moment, the superlative, a "stride", Lira's "never in her life" gloss, one "like a man who").

## 4. Priority 3: source-shaped passages, each within its present length, no fact changed, no scene break added or removed

- **ch57, the panel night** (2,293 words before, 2,290 after). The handcart, the nine precedents and "only one of them" are now heard in the room, in simple past, from Umber's present at the window. The cart comes round the turn of the stair. The oldest judge says "The short sheets will do," and the rating clerk answers "Very likely… I would like the room to be able to say that we looked." His clerk says "Nine… Nine in three hundred years" and reads the list out, slowing at the eighty-first cycle. Umber asks "Will the eighty-first serve?" and she answers "I found only one of them." Then "It was a little after the seventh bell…", and the rest of the night stays in pluperfect summary. The "under" over "by" passage, *The Chief Adjudicator paused.* and the observation-right minute line are untouched.
- **ch49, Daeva's history** (1,576 + 20 words before, 1,567 + 27 after). It now runs from her present. At the glass she goes to her travelling case and puts her hand into the lining, so the paragraph that ends the scene before the break changed by one sentence. The passage then runs:
  1. the exercise sheet she keeps, and the coast exercise at fifteen;
  2. the marbled notebook's line at seventeen;
  3. the registry page of youngests, read from the top down to its first line;
  4. the garden: thirteen, the pear tree, "Am I early, or are you late?";
  5. the registry's rare coin, and Auremont since twelve;
  6. *Specimen.*, as the notebook's word;
  7. "It had been four years since the coast."

  Every fact is kept: thirteen, the garden court, twelve, six years, seven in the program, Specimen, the Gold Rank Six on the coast, the twelve drills, the month of mornings, "Seven days after that bout". One small fix: the old text put the older registry lines "Above" the top line of a page "kept from the bottom up". They now sit "Below" it. The scene after the break now opens "She went back to the glass, and to the trial." "Most awake two exchanges of her life" became a comparative, so the superlative cap holds.
- **ch56, the aftermath list** (421 words before, 367 after). The catalogue is now two seen moments. The first, outside and in Ephram's telling, is one moment in the outer court: the crier on the barrel stops at *and the boy —* for ten seconds by a carter's count, and in the same ten seconds the betting men behind him turn their ledgers face down. Then come the tower stairs' "he hasn't got that" in four accents. The second, inside, is what Cael can see from the north barrier: nine still pens, the scribe looking at his pen, and Havel standing without knowing it. The "rings from a stone in a pond" frame and the graveside simile are gone.
- **ch60, the convening.** Left as it is, by design.

## 5. Seams checked

- **ch53 / ch58, the two cases.** In ch53 Seln opens "his own pen-case" (three references, smooth in context). In ch58:115 "The locked case… apart from the pen-case beside it. He had not opened it." Consistent. I made no change to the coordinator's lines.
- **ch31 / ch59, the guard.**
  - ch31:185 has four men in grey, two on either side; ch31:209 has the colour-guard at the tail.
  - ch51:225 (standings) has "one of the colour-guard at either side", which makes two.
  - At ch59:155 (closing) I smoothed one join. The old sentence, "two of them… as it had been carried in alone on the first day", could be read as two on the first day too. It now reads "…two of them, one at either side. As on the first day, no house walked behind it." That echoes ch31's "No house walked behind it."
- **ch60, the leaf list.** "…and the minute, and the pole, and the rule, and the warning…" reads cleanly.
- **ch60, the Fiske line (ch60:191).** The coordinator's clause said Lira "would be at the Iron bracket next cycle whether Fiske watched it or not". That contradicts ch60:75, "Silver bracket. Next cycle.", and the protected "be there". I changed it to "would be in the Silver bracket next cycle whether Fiske watched it or not". The thread still closes in the Hesk's-book paragraph.
- **ch41 → ch59, the captain's nod.** While thinning ch41 I removed the captain's sum-nod. ch59:133 calls back "as he had nodded on the crown", so I restored a bare "Then he nodded, once," in ch41:57.

## 6. Protection checks

- All 52 regex patterns in `protected-patterns.txt` give identical match counts before and after over ch31–60.
- I checked 63 §10 strings (Log entries, spoken lines, Hesk's and Vell's letters, the notice's neighbours, *Overdue.*, the board line, the entry, the convening lines, *Specimen.*, "Am I early", "Thank you for the form" and others). Every count is unchanged.
- The FRAGMENT ACQUIRED code block in ch56 is byte-identical.
- I compared every "X to Y" score, "N each", figure word (twenty-/thirty-) and T-/d-number per chapter. All are unchanged.
- The only italic text that changed is Log wording I chose to vary. None of it is protected: the openings of the ch31, 33 and 36 entries, the bay depth in the ch40 note, one ch53 entry line and the ch60 inventory's "quiet thing" line.
- No season, month or weekday names were added; the only hits are the verbs "may" and "march" and the word "maybe". No metric words, no new names.
- Bede, Maud, Gwen and Abbot do not appear in ch31–60.

## 7. Checks in "After"

- **overlap** (`bash tools/ed.sh overlap book-05-the-silver-standard N`): M5, M6, M7, M8 and M9 all show 0 unprotected shared runs both before and after. Protected runs are 10, 17, 19, 27 and 34, unchanged.
- **gates** (`ed.sh gates`, M5–M9): every chapter shows reader_standard=0, metadata=0 and modern=0, before and after.
- **sweep_probe** (`sweep_probe.sh book-05-the-silver-standard 5 9`, from the worktree root): no movement total rose.
  - Skeleton: M5 1→1, M6 1→1, M7 2→2, M8 2→2, M9 2→2.
  - Close: M5 5→5, M6 7→6, M7 9→9, M8 11→11, M9 15→15.
  - Single chapters moved by one point: ch37, ch41, ch43, ch45 and ch59 rose by 1, and ch49's skeleton went 0→1. ch32, ch46, ch49 (close), ch57 and ch60 fell by 1. These are rounding on slightly fewer sentences. (ch29 rose 3→4 in the M5 total, but ch29 is Lane A's.)
- **formula_metrics.py** on ch31–60:

| Metric | Before | After | Hold |
|---|---|---|---|
| Sentence mean | 13.59 | 13.55 | ≥ 13.3 |
| Share ≥ 40 words | 3.6% | 3.5% | ≤ 4.5% |
| Words per scene | 932.2 | 926.1 | 850–1,050 |
| Share ≤ 5 words | 0.267 | 0.268 | |

## 8. Words lost

By `wc`, ch31–60 went from 149,487 to 148,518, a loss of **969** (the metrics tool says 149,149 → 148,180). ch51 lost 200 under Priority 2. ch41 lost 94, mostly the back room's repeated description. The other chapters lost between 5 and 55 each. ch49 gained 1 within the re-ordered passage.

This is the low end of the two lanes' 2,000–3,000. I took the repertoire out sentence by sentence and did not take paragraphs.

## 9. Workspace note for the coordinator

On the first counting run Lane B used the shared top-level scratchpad. A `sed` meant for Lane B's own script touched the top-level `scratchpad/count.sh`, which Lane A had written seconds before, and overwrote `scratchpad/before.txt`.
- **The sed.** If Lane A's line was exactly `'nodded once'`, it now reads `'nodded,? once'`.
- **before.txt.** I regenerated it at 23:48 by running Lane A's script on ch01–30. At that time the only change to those chapters was the coordinator's 23:44:44 fixes, so the baseline matches the text before Lane A's edits.
- **Lane A.** I left `scratchpad/NOTE-FROM-LANE-B.txt` for Lane A.
- **Lane B's files.** After that, Lane B worked only in `scratchpad/b5-laneB/` (orig copy, count.sh, before/after counts, overlap, gates, sweep and metrics).
- **orig/.** My copy of ch31–60 also overwrote `chapter-31…60.md` in the shared `scratchpad/orig/`, which held an earlier session's copies (dated 09:38).
