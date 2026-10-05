# Book 2 completion pass — Lane A report (ch1–30)

Author seat: Monroe Jackson 1.3 / O'Connor 1.3.0 (Opus). Date: 2026-10-05.

I read every chapter in full, in order, and revised it in place. Every change is an old-to-new pair that I wrote after reading the sentence in context. Each old string had to match exactly once, or nothing was written. There was no script and no global find-and-replace. I edited only `manuscript/chapter-01.md` … `chapter-30.md`, and ran no git commands. The before snapshot is in my scratchpad (`b2-laneA-texture/orig/`).

## 1. Priority 1 counts, ch1–30 (grep, before → after)

| Target | Before | After | Notes |
|---|---|---|---|
| "the way (a/you/he/she…)" simile family* | 199 | 74 | Most of the 74 are literal ("the way he had come", "the way I rule everything") or in speech. |
| "as if" | 112 | 37 | |
| "as though" | 40 | 14 | |
| **Explanatory similes per chapter (way + as if + as though, real ones, by reading)** | 7–20 | **≤3 in every chapter** | No two on one gesture. |
| "exactly" | 80 | 29 | The 29 that stay are where exactness is the subject: the clock's drum, Lira's matched pace, the lock's length, copying a notice, Havel's precision, the redirect's timing, Brom's tell, and three hedges ("not sorry, exactly"). |
| "plainly" | 28 | 0 | "watch plainly" is now the method word "watch plain" (ch12, ch13). |
| "honestly" | 19 | 1 | Kept: ch16, "kept honestly" (the keeper's honesty is the subject). |
| "for a long time/moment/while" | 35 | 0 | |
| "for a while" | 38 | 1 | Kept: ch30, "does not mean to get up for a while" (idiom). |
| "did not look up / without looking up" | 14 | 6 | All six are Vell's now (ch4 ×2, ch14, ch17, ch19, ch23). Taken back from the reading-room keeper, the betting man ×2, the heavyset man ×2, Coss's daughter and Brom. |
| "like a man/woman who" | 15 | 9 | M1 1 (Vell's speech); M2 2 (ch11, ch14); M3 3 (ch17, ch20, ch21, the last a deliberate echo of ch17); M4 3 (ch24; two in Lira's speech). |
| hand's width/breadth | 19 | 5 | Kept: Lira's stick, measured on the straw (ch1, ch6, ch28, ch30) and the burst's third-of-the-ground (ch24). |
| finger/hair/straw widths | 11 | 1 | Kept: ch18, Brom's knee tell, as first measured. The notched-stick "fingers' widths" (ch8) is kept but not counted by the grep. |
| two *ands* | 15 | 15 | Motif; untouched. |
| "bright stillness" | 4 | 3 | Once per bout: Orvet's Blade (ch19), Brom (ch24), the Shield (ch30). The ch17 alcove drill now has "clear stillness". |
| Brom mouth-corner | 4 (+2 variants) | one per scene | First (ch17) kept. ch21 had two in one scene; one cut. ch28: the red neck (the first, kept) and a mouth-corner shared a scene, so the mouth-corner after §8.2 was cut. |
| Red neck | 1 + ch28 | ch28 only | The ch4 guild man's "red from the collar up" was cut, so the first red neck is Brom's (ch28). |
| "as if it owed him money" | 1 (+ variant) | 1 | ch2 Dace kept. ch12's "like it owed you money" is now "like it had told you a lie" (the forgery theme). |
| "as if it had done something he had not asked it to" | 2 | 1 | ch21 Wendel kept. ch22 Brom keeps only the callback "as Wendel had looked at his own right foot". |
| "Go and eat" | 3 | 2 | ch23: Vell said it twice in one scene; the first was cut so "Once." / "Go and eat." lands. |
| "You're grey" | 0 | 0 | Lane B's run. |

*Pattern: `\bthe way (a|an|you|he|she|they|it|his|her|men|man|women|people|one|someone|some|boys|children|we|i)\b`.

Also thinned (just under the ten):
- "plum": the ch9 first and the ch10 "as Vell had promised" stay, and so does Lira's arm in ch27. Mid-book plums in ch12, ch23 and ch27 (two) now say bruised, purple or blue.
- "like weather": now only the heavyset man's and Lira's lines. Removed from Brom ×2, the betting man ×2, the fruit woman, Cael's narration about Orvet, and the reading-room scene.
- The carter's horse-look (ch16): cut. Its two callbacks (ch21, ch26) were re-pointed.
- Repeated stair/missing-step, cracked jug, dog, sack and bucket similes: one of each kept.

Kept as required: Brom's builder-grandmother floor (ch16), Hesk checking a drawing (ch6), Vell's *begin* (ch2), the fan (ch7), the lock's first uses (ch5).

## 2. Words

| | Before | After | Change |
|---|---|---|---|
| ch1–30 (`wc -w`) | 147,145 | 145,166 | −1,979 |
| formula_metrics words_total | 146,816 | 144,837 | −1,979 |

By chapter: ch01 −113, 02 −28, 03 −25, 04 −10, 05 −44, 06 −17, 07 −142, 08 −52, 09 −61, 10 −124, 11 −56, 12 −60, 13 −46, 14 −42, 15 −100, 16 −53, 17 −44, 18 −60, 19 −67, 20 −35, 21 −63, 22 −105, 23 −85, 24 −114, 25 −119, 26 −58, 27 −76, 28 −78, 29 −54, 30 −48.

## 3. formula_metrics.py, ch1–30

| Measure | Before | After | Held to |
|---|---|---|---|
| sentence_mean | 13.85 | 13.65 | ≥13.3 ✓ |
| share ≥40 words | 3.7% | 3.5% | ≤4.5% ✓ |
| words per scene | 895.2 | 883.2 | 850–1,050 ✓ |
| share ≤5 words | 30.5% | 30.7% | ≤~34% |
| paragraph median | 28 | 28 | |
| Flesch RE / FK grade | 91.4 / 3.95 | 91.6 / 3.87 | |

No scene breaks were added or removed (134 both times).

## 4. Overlap, movements 1–4 (`ed.sh overlap book-02-iron-circuit N`)

| Movement | Before | After |
|---|---|---|
| M1 | 0 unprotected (5 protected) | 0 unprotected (5 protected) |
| M2 | 0 (4) | 0 (4) |
| M3 | 0 (2) | 0 (2) |
| M4 | 0 (7) | 0 (7) |
| ch30 (M5, run directly) | 0 | 0 |

One 8-word run appeared mid-pass in ch17 ("he said it the way a man reads"). I rewrote it, and it is 0 now.

## 5. Gates

`ed.sh gates` for M1–4: reader_standard=0, metadata=0, modern=0 on all 29 chapters. ch30 reader-standard grep: 0.

## 6. sweep_probe.sh book-02-iron-circuit 1 4 (skeleton / close)

| Movement | Before | After |
|---|---|---|
| M1 | 0% / 13% | 0% / 12% |
| M2 | 1% / 7% | 1% / 7% |
| M3 | 0% / 8% | 0% / 8% |
| M4 | 1% / 12% | 1% / 11% |

No figure rose. Two rewrites created new skeleton matches against the source, and both were rewritten again before the final run:
- ch4: "She looked at him with the spoon in her hand."
- ch8: "Dace rubbed out a dot … somewhere else."

## 7. Protected lines

I checked these after the pass; each is present and exact:
- the BOOK_MAP §8 lines in range: 2, 7, 11, 12, 13, 18–25;
- the Iron-adjacent notice (ch28);
- the Wind FRAGMENT UPDATE (ch7, recopied in ch8);
- "No reason for this page.";
- Havel's checklist;
- the floor exchange, all lines;
- "Show me the log sometime." / "Maybe.";
- the three mornings, the whole Log read in an alcove, the teaching day, and "stop being careful".

No bout exchange, landing beat, tally, count or date was changed.

**One join smoothed, ch25.** The floor exchange's last line had a tag splitting it: "Good." / tag / "I like problems I can't solve." It is now "Good. I like problems I can't solve." with the tag after it. This is the same treatment §8 fix 3 gave §8.2 in ch28.

## 8. Seams reread (Priority 3)

- **ch1–3, Dace's twelve years.** Confirmed: "the twelfth year running" (ch1); "Not in twelve years" and "for twelve years" (ch3); "in twelve years" (ch15). No twenty anywhere in range.
- **ch1–3, the Ulric silence.** Confirmed. ch1 has "I'd like to know what you were watching instead." / "I know," and then nothing, so ch58's "Cael had given him nothing" points at a real first occurrence. No other Ulric memory in ch1–30 contradicts it.
- **Changed, ch30.** "nodded slowly, as Ulric had nodded in the spring" misremembered ch1, where Ulric does not nod; he goes to his corner with his jaw set. It also named a season. Cut to "nodded slowly".
- **ch28, the §8.2 beat.** Confirmed: "Good. That means you get to choose the word." is whole. To keep one Brom tag per scene (the red neck is the first and stays), I removed the mouth-corner beat that fix 3 had moved after the line. The line now ends its section. Nothing in ch1–60 or BOOK_MAP quotes that beat. Lira's recall later in ch28 still matches.
- **Coordinator's fixes in range, reread in context.**
  - Fix 1, ch10 "where the last one was": the join reads cleanly.
  - Fix 2, ch22 Red Cap "he": clean.
  - Fix 3, ch28: as above.
  - ch30 "with the others" is still correct by then.
- **Callbacks re-pointed after cuts.**
  - ch21 and ch26: the carter's look.
  - ch22: Wendel's foot.
  - ch22: the "stair a little higher than counted", which still points at ch17's kept simile.
  - ch10 → ch21: the dock partner's nod.

## 9. Changelist by chapter

Every chapter: explanatory similes cut to ≤3, and fillers and measured pauses cut where the sentence stands without them. Beyond that:

- **ch1** Envelope, burst-string and river-academy-man similes kept. Cut: sack, key, door-lean, the roof-beam gloss, the guard settling, Lira's fire / checking-shut / confirmed-figure. Vell's look rewritten without the stacked "as if".
- **ch2** Kept begin / word-person / owed-money. Cut: the dog at the door, "as though" ×2 on the rungs.
- **ch3** Cut "as if by magic" and the measuring-the-street simile. The heavyset man keeps weather; "exactly" ×2 cut.
- **ch4** "honestly" and the guild man's red neck cut, so the red neck is Brom's. Stone-in-a-boot moved to its one use (ch8).
- **ch5** Lock trials: two *ands* untouched. Five similes cut, including the cup-catch and the letter "might go off".
- **ch6** "plainly" and "honestly" cut; the Hesk-drawing simile kept; Joren's declaration keeps one "exactly".
- **ch7** The fan kept. Twelve similes cut, including the hole-in-a-fence, the coat-pocket search and the fingernail measure.
- **ch8** Four "the way" habit-comparisons made plain; the bucket and the Dace simile cut. "honestly" ×2 cut.
- **ch9** Hand measures ×2 and the fingernail cut; "as if he were somebody's grandfather" cut.
- **ch10** Price-of-bread kept, "plainly" cut. Dog, wheel, knot-pull kept to one; seven cut.
- **ch11** The betting man's "did not look up" returned to Vell; the stair face cut.
- **ch12** The dog ears cut; the owed-money repeat now "told you a lie"; "watch plain".
- **ch13** Cracked-jug kept as its one use; the cat simile cut; hand's breadth ×2 cut.
- **ch14** "exactly" thinned from 10 to 4, kept on the clock's drum and Lira's matched pace. The betting man's look-up tag cut; weather taken off the fruit woman.
- **ch15** Five Havel / Red Cap similes cut. Havel's "exactly" kept as character.
- **ch16** Builder floor kept; the carter, the "Gold ran down…" and the book-down similes cut.
- **ch17** First mouth-corner kept. Stair-rail and cracked-jug repeats cut. Drill "bright stillness" is now "clear stillness". Coss's daughter's look-up tag cut.
- **ch18** Reading-room keeper's look-up cut; the gatepost repeat cut; Keth's mouth-corner (a Brom tag) is now "almost smiled".
- **ch19** The stair-face and sum-face repeats cut; three pauses cut.
- **ch20** The bow simile kept; the sack breath cut; "honestly" cut.
- **ch21** Brom's two mouth tags in one scene cut to one. Dace's carter callback re-pointed. The sister's and the betting man's similes cut.
- **ch22** Vell's dipped-pen correction kept. Brom's "did not look up" cut. The gate-kick and wandered-into-margins similes cut.
- **ch23** Plum is now purple; Vell's double "go and eat" thinned. Weather taken off Brom and the betting man.
- **ch24** Brom bout: exchanges untouched; the barley, bolted-arm, dog and book-with-wet-ink similes cut.
- **ch25** Floor-exchange join smoothed (§7). The shelf-in-the-dark and stair-missed repeats cut; "honestly" ×2 cut.
- **ch26** The carter callback cut; four "as if/though" cut; "honestly" ×2 cut.
- **ch27** The weather tag off Brom; plum ×2 is now blue. The help / introduced / sound-stopped similes cut.
- **ch28** One Brom tag per scene (neck kept, mouth-corner cut); Brom's "did not look up" cut. Lira's "counted his own teeth" repeat replaced.
- **ch29** Second dog, cracked jug, waiting-at-the-door and figure-off-a-slate cut. Weather taken off Brom.
- **ch30** The false Ulric memory removed; hand and finger measures ×2 cut; the pigeons cut. Orvet no longer "weather" in Cael's narration.

## 10. Not done / for the coordinator

- The `--allow` file `book-02-iron-circuit/protected-patterns.txt` does not exist. `ed.sh overlap` runs without it, using BOOK_MAP §8 only.
- The Book 1 back-cover line (*They're not separate things…*) does not appear verbatim in ch1–30, before or after this pass. ch1 refers to the "fence" line in the back cover instead. Unchanged, and noted for whoever checks §8.31.
- Lane B owns M5's overlap and sweep figures. I edited ch30 (in M5) and checked its overlap directly: 0.
