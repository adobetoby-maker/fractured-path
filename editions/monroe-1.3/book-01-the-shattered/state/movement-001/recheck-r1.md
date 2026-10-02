# Recheck r1 — Book 1, Movement 1 (targeted, post-repair)

Reviewer: Claude Fable 5.1 (review seat). Author of repair: Claude Opus 5.5. Date: 2026-10-01.
Scope: the REPAIR-BRIEF items, the changed joins, the mechanical paragraph splits in Ch3–6, and BOOK_MAP §7. Not a fresh review. No manuscript file was modified.

Method: read all six repaired chapters in full; diffed each against `pre-repair/` (the repair is a near-complete rewrite of every chapter, so each changed region was read in context rather than as a hunk); re-ran `tools/formula_metrics.py` (numbers match the AUTHOR-REPORT table exactly: mean 13.82, ≤5 30.7%, ≥40 2.1%, 24 breaks, 29,512 words); grepped every §7 line in post and pre; grepped the refrains and banned words.

## Verdict: CLOSE WITH LINE FIXES

No second repair. One brief item is incorrectly applied (a one-word calendar fix), one repair-introduced continuity slip (one line), one Markdown-breaking paragraph split, and six paragraph breaks that land on the wrong sentence. All are mechanical. The developed scenes are intact and the new material (the reel jam, the lock gauge, the Unranked-quarter exchange, the "You're early" refusal) joins cleanly.

---

## (a) Brief items

### Coordinator rulings

| Ruling | Status | Location |
|---|---|---|
| Hesk's Ardenmere visit kept ("Once. A long time ago." / "Loud… I was younger than you'd think") | RESOLVED | Ch3 ll.325–331 (folded from the old Ch4 bedroom) |
| Arbiter **dark** after the word; cat-in-a-chair image moved | RESOLVED | Ch3 l.137–139 "went out, the way a lamp goes out when the wick is pinched"; l.173 "It was not silence… It was just absence."; cat image now Hesk sitting, l.183 |
| Reel competition renamed off "circuit" | RESOLVED | "sanctioned regional season" (Ch2 l.117), "regional athletics office" (l.181), "by his sanctioned rating" (l.207). `circuit` = 0 occurrences in the movement (pre: 4) |

### Priority 1 — rhythm and reading level

| Item | Status | Note |
|---|---|---|
| Join clipped runs into hierarchical sentences (Tallow Lane, archive + walk home, walk to depot, wall reading + second day) | RESOLVED | Tallow Lane Ch1 ll.123–133; archive Ch4 ll.105–149; depot walk Ch5 ll.51–87; wall reading Ch6 ll.31–87; second day ll.205–217. Sentence mean 8.77 → 13.82 |
| 3–5 deliberate ≥40-word sentences per chapter where earned | RESOLVED | e.g. bracket test Ch1 l.73; the six pushes l.356; Lantern Street Ch5 l.161; the fires Ch6 l.241; the Tuesdays paragraph l.79. 2.1% vs 3.3% target, every chapter has ≥3 — acceptable, not to be chased |
| Merge ~10 of 35 scene breaks (Ch5 first, then Ch3) | RESOLVED | 35 → 24. Ch5 9 → 4, Ch3 7 → 4 |
| Drop "said" in clear two-speaker runs | PARTIAL | ~111 → ~97/10k. Author declared this unresolved with reasons (audio attribution). Not a concrete defect; do not chase |
| Protect the landings | RESOLVED | Eleven-second count intact (Ch3 ll.97–127); "Joren sat down in the street." (Ch1 l.306); "He went." (Ch5 l.243); "Go on," the guard said (l.257); the page-seven list (Ch1 ll.7–29); "That," he said, "is the right answer." (l.115); "Then I'll take it." (l.219); "Four." (l.139) |
| Reading level FK 6.8 | NOT RESOLVED (declared) | 4.8. Author correctly left it for owner direction — closing it means inflating vocabulary against the 13-year-old standard. Agree |

### Priority 2 — continuity, canon, rule gaps

| Item | Status | Location |
|---|---|---|
| Ch4 "in the side room yesterday" → two days ago | RESOLVED | Ch4 l.57 "in the side room two days ago" |
| Ch4 "Yesterday morning his number…" → two days ago | **NOT RESOLVED (wrong value)** | Ch4 l.115 reads "when **three** mornings ago, before the circle, his number had meant nothing to anyone." Ch4's archive afternoon is Day 4 (the notice "came on the second morning" after Kindling; the side room is "two days ago"). The circle was Day 2 morning = **two** mornings ago. Fix 2 below |
| Ch5 "Two nights ago…" ×2 → four nights ago | RESOLVED | Ch5 l.75 ×2. Checked: reel night = Day 1; departure = Day 5 morning; four nights |
| Ch5 "Yesterday. I said I would." → the day after | RESOLVED | Ch5 l.143 |
| Every other time word | RESOLVED | Checked: Ch1 "two days ago"/"both mornings since"/"these two days"; Ch3 "two or three days" for the notice (arrives Day 4); Ch5 "two days to say everything"; Ch6 "three days ago, in a room with a crooked tree" (Day 5 evening → Day 2) and "a day out of Denvash". All consistent. One pre-existing muddle survives — see optional fix 12 |
| Ch3 Alis "in her chest before her ears" cut/reattributed | RESOLVED | Now Joren's "heavy, good heavy" (Ch3 l.131); 0 occurrences of "before her ears" |
| "behind his breastbone, behind his sternum" doublet | RESOLVED | `sternum` = 0 |
| Ch3 sigil dark | RESOLVED | above |
| Ch2 circuit | RESOLVED | above |
| What triggers a Kindling (the circle) | RESOLVED | Ch1 l.35 "you stood in the circle at a certification office, and your Path woke there" |
| Baseline for "eleven seconds late" | RESOLVED | Ch3 l.67 Pellin: "usually done before you've finished a breath; with the paperwork… between three and fifteen minutes"; Cael registers it at "Three" (l.101) |
| Why Cael must leave Denvash rather than its Unranked quarter | RESOLVED | Ch4 ll.65–67: the quarter by the tanneries; the review "counts people, not houses"; every Denvash gate pulls the record; Ardenmere's Unranked District has no gate. Ch3 l.319 sets it up |

### Priority 3 — say it once

| Item | Status | Location / note |
|---|---|---|
| Hesk–Cael two-handers each given a different job | RESOLVED | Ch3 tea = information (notice timing + full Ardenmere briefing); Ch4 workshop = Hesk's confession of the fourth file, a name and a promise; Ch4 bedroom = the three gifts + the refusal ("You're not behind… You're early"); Ch5 breakfast = one practical line + the voice joke + the bracket; Fen Street lock = a task done together; depot = farewell. No two land the same beat |
| Fold bedroom Ardenmere briefing into Ch3 tea; keep bracket gift and "I didn't do something else" exactly | RESOLVED | Ch3 ll.307–333; Ch4 l.99 exact; Ch5 ll.29–41 |
| Tuesdays realised once, in Ch6; Ch3 almost-connects or not; letter does not restate | RESOLVED | Ch3 ll.221–223 the tug "gone before he could follow it"; Ch6 ll.77–81 the one realisation; letter l.177 "I read the one about watching someone who does." Ch2 l.363 lists what Hesk did without stating why — correct |
| Refrains: one "Perform competence" (carter); one "dead within weeks" in Ch6; cut spoken "learn before your mind"; cut extra "still finding out" | RESOLVED | "Perform competence" = protected entry + carter (Ch6 l.147). "dead within weeks" = Ch6 rise entry (protected) + one at Ch4 l.133, which is the narration of the entry being read two lines above — an echo at the source, not a refrain; acceptable. "learn before your mind" = 2, both protected notebook lines. "still finding out" = carter's coinage + his laugh only (Ch6 ll.149–151) |
| Thin "He noted / He filed it / He made himself" closers; halve "the way…" tails | RESOLVED | "He noted that" 0; "filed it" 2 (both doing work); "He made himself" 1; "the way…" ~29 from 56 |
| Ch6: entries in full, one reflection per entry; second day keeps hawk/sheep/climb, recount replaced by "*Weeks.* Not years." | RESOLVED | Entries ll.43, 51–53, 61–63, 73 exact; reflections at 45–47, 55–57, 65–69. Second day ll.205–217 |
| Length 28,500–31,500 | RESOLVED | 29,579 (wc) |

---

## (b) Mechanical paragraph splits (Ch3–6)

The author split any narration paragraph over ~95 words "at the sentence nearest the midpoint". These are the author's own post-join paragraphs, so they have no single pre-repair parent; judged by reading. Ch3: no bad split found. The following break the thought, a referent, or the rhythm. Each gets a fix below; the fix is always to **move the break** to the sentence boundary that respects the thought, never to add words (except fix 8, which restores a dropped verb).

| # | Where | What breaks | Better point |
|---|---|---|---|
| 1 | Ch4 ll.15–17 | The break falls **inside an italic run**: `*Hello. I got [SHATTERED]… what it does.` ¶ `Show me how to fall down properly.* Every version…` Splits Cael's imagined speech mid-run and leaves an unclosed `*` in one paragraph and an unopened `*` in the next (Markdown renders both wrong). | After `properly.*` |
| 3 | Ch4 ll.133–135 | "…and three of them had been dead within weeks." ¶ "One was not accounted for. This was not a policy…" The three-and-one enumeration is one thought; the break strands "One". | After "One was not accounted for." |
| 4 | Ch4 ll.169–171 | "…They hardly ever did. Hesk's hands went back to the housing in the vice…" ¶ "They were a craftsman's hands…" The hands sentence is stranded at the tail of the paragraph about the choice; "They" opens the next paragraph with its antecedent on the wrong side. | Before "Hesk's hands went back" |
| 5 | Ch4 ll.209–211 | "…The second carried the year he had first noticed the gap…" ¶ "The five pages about the wall had felt like an essay…" The five pages belong to the second notebook; the break separates them, and the first/second/third ladder loses its rungs. | Before "The third was the current one" |
| 6 | Ch5 ll.5–7 | "…A cupboard closed with a soft, deliberate click." ¶ "It was the cupboard by the stove…" "It" opens a paragraph with its referent across the break. | Before "Cael knew this house's sounds" |
| 8 | Ch5 ll.135–137 | "…most of them maps to places that did not exist." ¶ "One of them, Cael remembered, a list of every word…" The break orphans "One of them" from "most of them", and the join dropped the verb (pre: "had been a list"), leaving a verbless fragment at a paragraph head; then "The gap was still there" (present action) sits in the memory paragraph. | Before "The gap was still there." and restore "had been" |
| 9 | Ch6 ll.67–69 | "…He had named what his own hands were doing…" ¶ "He had copied the archive entry… And Hesk did not think any of that was hiding." Three "He had…" examples split 2+1, with the turn ("And Hesk did not think…") buried mid-paragraph. | Before "And Hesk did not think" |
| 10 | Ch6 ll.125–127 | "…a good deal less than the least, if you asked him." ¶ "Get up, lad, get up on the bench… So Cael got up on the bench…" The free-indirect "Get up, lad…" is the driver's insistence and belongs with it; the new paragraph should begin with Cael's action. | Before "So Cael got up" |

Splits checked and judged sound: Ch4 141/143 (the two "He thought about" paragraphs), 147/149 (the turn to "He decided something else"); Ch5 51/53, 75–79, 85/87, 161/163 (the Lantern Street light; the "It caught…" paragraph reads as a deliberate second beat), 185/187; Ch6 5/7, 9/11, 45/47, 55/57, 153/155, 227/229, 233/235.

---

## (c) New defects introduced by the repair

1. **Ch5 l.21 vs Ch6 l.169 (continuity).** New breakfast business: "Hesk spread preserves on his bread with great care." The pre-existing letter line in Ch6 says "Ressa put an extra loaf in… I think you knew she would, and that's why you didn't take any for yourself this morning. I noticed." Pre-repair, Hesk is never shown eating bread at breakfast, so the letter held. Now it doesn't. Fix 7 (one line in Ch5; the letter line does character work and should stay).
2. **Ch4 l.115 calendar** — wrong value ("three mornings ago"); see Priority 2. Fix 2.
3. **Ch4 ll.15–17 italic split** — see (b) #1. Fix 1.
4. **Ch3 l.57 (minor, legibility).** The join dropped the verb: pre "set into the boards, **was** a circle of pale wood…" → post "set into the boards, a circle of pale wood… where years of feet had stood." A verbless fragment opening a paragraph right after a complete inventory sentence reads as a dropped word, not a device. Optional fix 11.

Checked and clean: no protected line altered (every §7 Tier A and Tier B line sourced in Ch1–6 is present and character-exact in post — the registry entry, the two starred page-seven lines, the registration number, *whatever it is, we figure it out.*, both Ch3 plants, the notice's four protected elements, the archive dispositions, "You're not behind…", all six notebook lines including the added *When you don't know what you can do yet…*, the gate entry and its corollary); no repeated beat introduced (the Ch6 rise's "four entries, three of which had ended in a few weeks… He was the fifth" at l.247 pre-exists and is the beat the brief told the author to keep); "Once. A long time ago." now answers both "the person you saw" (Ch2 l.91) and "you've been there" (Ch3 l.327) — both pre-existed (Ch2/Ch4) and the fold has moved them a chapter closer; this reads as the same event answered the same way, not a tic, and I'd leave it; Ch3 l.345 "Last week on the roof… if it comes to it" is the pre-repair line reworded so it no longer pre-empts the Tuesdays turn — good; Rooted Stance, "both mornings since", Pellin's stamp on the card closing the gate-guard gap, the reel jam and the shim, the Fen Street lock — all join cleanly with what precedes and follows them.

---

## (d) Second repair?

**No.** Nothing here needs the author back. Every item is a one-line edit or a paragraph-break move, listed exactly below for the coordinator to apply. The remaining metric gaps (FK, reporting verbs, ≥40 share) are declared and reasoned; chasing them would be chasing an average.

---

## Line fixes (apply in this order; `¶` = blank line / paragraph break)

**Required (1–10)**

1. `manuscript/chapter-04.md` (ll.15–17)
   old: `No, I don't know what it does.` ¶ `Show me how to fall down properly.* Every version he built`
   new: `No, I don't know what it does. Show me how to fall down properly.*` ¶ `Every version he built`

2. `manuscript/chapter-04.md` (l.115)
   old: `when three mornings ago, before the circle,`
   new: `when two mornings ago, before the circle,`

3. `manuscript/chapter-04.md` (ll.133–135)
   old: `and three of them had been dead within weeks.` ¶ `One was not accounted for. This was not a policy`
   new: `and three of them had been dead within weeks. One was not accounted for.` ¶ `This was not a policy`

4. `manuscript/chapter-04.md` (ll.169–171)
   old: `They hardly ever did. Hesk's hands went back to the housing in the vice and moved through the work without hurry.` ¶ `They were a craftsman's hands,`
   new: `They hardly ever did.` ¶ `Hesk's hands went back to the housing in the vice and moved through the work without hurry. They were a craftsman's hands,`

5. `manuscript/chapter-04.md` (ll.209–211)
   old: `between the Outer District and the Inner one.` ¶ `The five pages about the wall had felt like an essay when he wrote them and felt now more like a warning he had written to himself without knowing who it was for. The third was the current one,`
   new: `between the Outer District and the Inner one. The five pages about the wall had felt like an essay when he wrote them and felt now more like a warning he had written to himself without knowing who it was for.` ¶ `The third was the current one,`

6. `manuscript/chapter-05.md` (ll.5–7)
   old: `A cupboard closed with a soft, deliberate click.` ¶ `It was the cupboard by the stove, whose latch had worked loose two winters ago, so that if you shut it firmly it rattled for a full minute afterward, and Hesk always closed it with two fingers. Cael knew this house's sounds`
   new: `A cupboard closed with a soft, deliberate click. It was the cupboard by the stove, whose latch had worked loose two winters ago, so that if you shut it firmly it rattled for a full minute afterward, and Hesk always closed it with two fingers.` ¶ `Cael knew this house's sounds`

7. `manuscript/chapter-05.md` (l.21)
   old: `Hesk spread preserves on his bread with great care.`
   new: `Hesk pushed the preserves across the table with great care.`

8. `manuscript/chapter-05.md` (ll.135–137)
   old: `most of them maps to places that did not exist.` ¶ `One of them, Cael remembered, a list of every word Joren knew that rhymed with *canal*, which had come to four, two of them made up. The gap was still there.`
   new: `most of them maps to places that did not exist. One of them, Cael remembered, had been a list of every word Joren knew that rhymed with *canal*, which had come to four, two of them made up.` ¶ `The gap was still there.`

9. `manuscript/chapter-06.md` (ll.67–69)
   old: `instead of feeling it.` ¶ `He had copied the archive entry in his neatest writing so that he would not have to simply sit there and know it. And Hesk did not think`
   new: `instead of feeling it. He had copied the archive entry in his neatest writing so that he would not have to simply sit there and know it.` ¶ `And Hesk did not think`

10. `manuscript/chapter-06.md` (ll.125–127)
    old: `if you asked him.` ¶ `Get up, lad, get up on the bench, and here, have the turnip, it's yours, it's got your name on it now. So Cael got up`
    new: `if you asked him. Get up, lad, get up on the bench, and here, have the turnip, it's yours, it's got your name on it now.` ¶ `So Cael got up`

**Optional (coordinator's call)**

11. `manuscript/chapter-03.md` (l.57) — restore the verb the join dropped
    old: `In the middle of the floor, set into the boards, a circle of pale wood`
    new: `In the middle of the floor, set into the boards, was a circle of pale wood`

12. `manuscript/chapter-05.md` (l.15) — **pre-existing**, not a repair defect, but the repair now states "no gate" at Ardenmere's Unranked District as plot mechanism three times (Ch3 l.319, Ch4 l.67, Ch6 l.269), which makes this line louder than it was. Cael also spends the first night at the waystation, so "arrive after dark on the first night" has no referent.
    old: `"Ardenmere's gate opens at dawn and closes at full dark, and I'm not to arrive after dark on the first night," Cael said.`
    new: `"The waystation bars its door at full dark, and I'm not to be on the road after dark on the first night," Cael said.`

After applying 1–10, no paragraph in Ch4–6 exceeds ~110 words; none of the moves touches a protected line, a landing, or a scene break.
