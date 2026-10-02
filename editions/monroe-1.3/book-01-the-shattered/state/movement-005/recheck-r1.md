# Recheck r1 — Book 1, Movement 5 (chapters 28–33)

Review seat: Claude Fable 5.1, targeted recheck of the author's Repair r1 (author: Claude Opus 5.5), 2026-10-02.
Scope: the brief's items and every changed region, found by diffing `manuscript/chapter-28..33.md` against `pre-repair/`. Not a fresh review. No manuscript file was modified.

**Verdict: CLOSE WITH LINE FIXES** (two line fixes, listed at the end). No second repair.

Tool checks, run read-only: `ed.sh gates` — reader_standard 0, metadata 0, modern 0 on all six; `source_overlap.py` — 0 unprotected shared runs of ≥10 words, 2 protected (allowed); `formula_metrics.py` — 28,111 words, sentence mean 13.11, ≥40-word share 2.7%, 23 marked breaks, 969 words/scene, FK 4.1. These reproduce the author's after-table exactly.

---

## (a) Brief items

### Priority 1 — counted time and clarity

| Item | Status | Location / evidence |
|---|---|---|
| ch29 "three weeks" since Cael's Brenna bout → five | RESOLVED | ch29 L321 "Some time in the five weeks since he had gone in on her dip"; L363 "She had spent five weeks training it out of herself". No "three weeks" remains in ch29. Day 15 → day 53 = 38 days. |
| ch30 "four nights ago" → three | RESOLVED | ch30 L177 "He had promised a girl on a step three nights ago" (promise day 50, now Sunday night day 53). |
| ch31 "forty hours left" → mid-thirties | RESOLVED | ch31 L87 "There were thirty-odd hours left by his count" (Monday morning to Tuesday dusk). |
| ch33 "four days of weather" → three | RESOLVED | ch33 L199 "gone pale in three days of weather, was Sunday's result" (Sunday 53 → Wednesday 56). |
| cold read's "second afternoon" (ch30 opener) | RESOLVED | ch30 L3 "On his third afternoon in Ardenmere, and his second of walking it". Arrival day 51 = first afternoon; day 52 walk and "Second day" log (ch28 L225); Sunday day 53 = third. Agrees with ch30 L29 "walked the district for two days", ch31 L103 "He's been here three days", L191 "first night and his third", "Saturday afternoon" at the lane of yards. |
| ch29 re-describes Brenna's shield | RESOLVED | ch29 L297 now "The shine came up off her left forearm as he remembered it, and she came off her mark and walked it at Lira." The second-exchange "level, a hand off the forearm" still reads without the cut description. |
| "wrote it on the wall by the pump" | RESOLVED | ch29 L247 "He wrote it up sitting on the low wall by the pump in Torvin's yard, in the margin". |
| flashback tense (cold read L363) | RESOLVED | ch29 L54 "He had been standing on the landing … He had looked past the clerk's shoulder"; the rest of the paragraph was already past perfect, so it is now one tense. |
| gloss "the four" at first appearance | RESOLVED | ch33 L163 "The four times something had moved him that he had not chosen were still in the back of the Log, numbered: the cart, Renn, the drop, Dessa." This is the only "the four" in that sense in M5 (the others are "the four lanes" and ch31's "the four words", which is the doorframe, established in ch8/ch14/ch24). |

### Priority 2 — say it once; Coss to ~6.2k

| Item | Status | Location / evidence |
|---|---|---|
| Trim ch28 second-day survey 500–800 words | RESOLVED | ch28 L209–221: the survey is down to the quarrels, the Paths at work, the carriers' clerk (whole), the fishwives' "circuit", the yard lane, the log. Ch28 4,311 words; Coss POV ~6.4k against ~6.2k asked — close enough, and the brief protected the recognition and the readings. |
| Doorstep lesson taught twice → once | PARTIAL | ch30 L17 carries the lesson in full ("pushing at that face got you nothing but a district that remembered you had pushed …"). But ch28 L183 still states it in miniature: "Coss had learned long ago what pushing a man like this would buy him. It bought a smaller answer and a longer memory. He did not push." The middle sentence is the lesson. Line fix 1 cuts it, leaving the beat (he does not push) and letting ch30 teach it once. |
| ch32: cut Coss's "how unusual" explanation and closing aphorism/counsel | RESOLVED | ch32 L150 now one line, "You've cited it the way it's written. All of it. Do you know how unusual that is?" → "I had a day and a reason to be careful." → "A day," Coss said after him. → "And most of a night." Speaker chain intact. The eleven-years / training-office / "In a cellar. Under my desk." speech, "the other thing is worse", "the cleverest thing … or the most dangerous", and the "use every one of them … They want something settled" counsel are gone. Kept: the three readings, "Closed one way or closed the other", the stamp held too long, "Don't ask me again", the leg, and "Don't thank me," Coss said. He looked at the window. "I can buy you time. I can't buy you the answer to whatever they're actually asking. That part's yours." — which still answers Cael's "Thank you" at L188. |
| ch33: front-of-Log to two lines; letter's index route to its result | RESOLVED | ch33 L59–61: two closed italic lines (*Fifty-fifth day. … Six weeks.* / *Coss asked nothing about the yards. Says he doesn't know who asked for the sweep. …*). Letter L150: "I read the law in the registry's reading room until I found where it doesn't fit me. A standard evaluation can only assess a classification the framework recognizes, and mine isn't one." The appendix line (L157) is kept, as the report says. "Make myself expensive" (L209) arrives sooner. |

### Priority 3 — rhythm

| Item | Status | Evidence |
|---|---|---|
| Join ~10 scene breaks, mainly inside the ch29 bout | RESOLVED | Rules per chapter, live/pre: 28: 6/7, 29: 5/10, 30: 3/7, 31: 3/5, 32: 2/5, 33: 4/5 (16 joined). Ch29's remaining rules are at L73, 143, 225, 253 and 397 — the bout runs unbroken from "The yard was fuller" (L255) to "Called," said Vell (L395), with the rule before the aftermath kept. Every exchange and Vell's "Begin" for the fifth is present. 23 units at 969 words/scene is inside 850–1,050; the author's reason for stopping short of 34–35 (it would drop below the range) is sound. |
| Split ~20 long sentences at a real turn | RESOLVED | ≥40-word share 5.3% → 2.7%, inside 2.5–4.5. I checked every split in the diffs; see (b). Sentence mean 13.11 sits at the floor of 13–15.5 and is reported honestly as such. |
| Length 27,500–30,000 | RESOLVED | 28,111 (tool) / 28,175 (wc). |

### Coordinator ruling — Lira's Compact-paper line

RESOLVED. ch32 L61: "That's good," she said. "That's very good. They made us read Compact paper at the academy, pages of it, so we'd know what a guild letter looked like when we got one." She made a face at the memory. — Nothing about her life before the academy; "academy" occurs nowhere else in the six chapters, so nothing contradicts it. The sentence "She did not say anything more about that life; she never did." is gone.

---

## (b) Splits, joins and merged scenes — every changed region read in context

Checked every hunk in all six diffs for fragments, dangling referents, separated speakers, broken bout exchanges, or changed meaning. Findings:

- **ch33 L217–219 (Tier B echo).** `"You've been reading that board for eleven minutes."` now stands as its own paragraph with no tag, and the beat `Lira came up beside him with the bread under her good arm.` is the next paragraph. The protected line is exact (the pre-repair had "said Lira, coming up beside him" inside it, which the repair rightly removed). The speaker is now inferred from the following beat and from "I wasn't counting," he said. It resolves, but the beat is the speaker cue and belongs on the line. Line fix 2 joins them without touching the protected wording.
- **ch28 L211 "The Compact did not count porters."** The porter example that used to precede it ("a porter lifting a barrel by its rim with one hand") was cut, so the line is now abrupt. It is anchored by ch7 L35 (the heavyset porter lifting barrels by the rim), so it reads as a callback rather than a dangle. No fix required.
- All other joins hold: ch28 desk → file (rule removed after "looked at them all together"); ch29 supper → "Cael did not hear much of the rest of supper" → past-perfect flashback; ch30 summons → "Then he wrote his preliminary report" (L63), Torvin → "He read it standing, by the range" (L146), "He shut the Log." → "Yeni was awake.", Yeni's directions → "The rain barrel was where she had said" (L202–204, "she" is Yeni two paragraphs up); ch31 "opened the door." → "The room was half under the ground" (L26–27, paragraph break intact), first seam → second seam; ch32 dream → frost, "He went up the stair sideways" → "The room at the top" (L102–104, break intact), "Something moved in his face" → "Coss read it."; ch33 Log → "Then he closed the Log … Vell would still be at her table." → "She was." (L94–96).
- Every split I read lands on a real turn and keeps its meaning: e.g. ch29 L137 "But Torvin's dark coat had been creased from two days on a cart, and the grey coat had been brushed. The grey coat had walked the market on the thirty-sixth day, while the dark coat was two days' road away at least."; ch31 L137 "The regulation said so in its own words. You only had to follow it from a note at the foot of a page to a brittle book nobody had copied in nineteen years, and on to an appendix that had come loose from its binding."; ch32 L147 the seven-weeks clause moved to its own sentence after the glance at the floor, where "it" is still that glance.
- Bout: no exchange touched beyond the splits listed by the author (the eyes on Brenna's boots, the five-weeks sentence, the skipped-middle sentence, Brenna's exit), each of which I read; the beats, the "Three. It took her three" exit and Vell's calls are unchanged.

---

## (c) New defects introduced by the repair

**Counted intervals vs the movement's own day count.** All agree. Anchors: Kindling day 0 ("fifty-odd days ago" on day 51, ch28 L23); gate entry day 3; Cael–Brenna bout day 15; grey coat day 36; roof day 38; Hesk writes day 44; promise on the step day 50; Coss and Hesk's letter arrive Friday day 51; Saturday 52 lodging house, walk, lane of yards, "Second day" log; Sunday 53 third afternoon, bout, summons "well into Sunday night" → "Forty-three hours" to Tuesday dusk, "three nights ago", "five weeks", "seven weeks"; Monday 54 reading room, "thirty-odd hours", "three days" here, "first night and his third"; Tuesday 55 evaluation, *Fifty-fifth day*, Cinder House "it was a Tuesday", letter, Coss's second report; Wednesday 56 board, "three days of weather", "noon tomorrow, the fifty-sixth day", "about the seventieth … a third gone", "Six weeks was forty-two days". Pre-existing and untouched, noted only: ch28 L29 "about three weeks after the gate entry" (~day 24) against Halvern's "Came about three weeks back" at L121 (~day 30) — both "about", not a repair defect.

**Coss trims — orphans.** None. The doorstep lesson: see PARTIAL above (still in two places, not orphaned). "I can buy you time. I can't buy you the answer …" stays (ch32 L210). Ch33's coda no longer leans on a cut promise: L173 "Then he wrote the sentence he had known since the afternoon that he would have to write." followed by the sentence itself (L175); "a boy in a cellar" at L177 is Coss's own narration and Lira's "in a cellar" at ch32 L61 is kept, so the word has its antecedent. The cut mender's doorframe in ch28 orphans nothing in ch31 L7 (Cael's POV; the doorframe is established at ch8 L151, ch14 L225, ch24 L127). The cut "Lira, h: in three days he asked nobody in the yards anything" leaves the Log's "Coss asked nothing about the yards" standing on its own, which is enough. Ch33's "the card and the two results" and Lira's "the new card and the two results" agree with each other (Lira over Brenna; Cael over Dessa).

**Lira's softened line** says nothing about her life before the academy (quoted above).

**Protected lines.** Every §7 fragment present in these chapters is byte-identical between pre-repair and live: ch28 L23 *Caelen Hesk-ward. Registration 41-7843-V.* (Tier A, exact); ch28 L25 and ch31 L81 "Statute 14, Section 9"; ch30 L147 the summons address with the registration; ch30 L255 *Forty-eight hours. Find the seam.* (exact); ch32 L203 "Get stronger. Build a reason for people to notice if I disappear." (exact); ch33 L217 "You've been reading that board for eleven minutes." (exact, now whole). No other §7 line falls in M5.

**Reader Standard / registers.** Gates 0/0/0 on all six. Nothing in the changed regions introduces a modern register.

**Author report accuracy.** The changelist matches the diffs; the "appendix line kept" claim is true (ch33 L157); the metrics table reproduces.

---

## (d) Second repair?

Not warranted. The only unresolved concrete item is the doorstep lesson's three-sentence residue in ch28, which is a one-sentence cut; the ch33 attribution is a paragraph join that keeps the protected line exact. Both are line fixes. Nothing else is unresolved, and the averages are inside range or honestly reported at the floor.

---

## Line fixes (each old text matches the manuscript exactly once)

**Fix 1 — `manuscript/chapter-28.md`** (doorstep lesson to ch30 only)
- old: `Coss had learned long ago what pushing a man like this would buy him. It bought a smaller answer and a longer memory. He did not push.`
- new: `Coss had learned long ago what pushing a man like this would buy him. He did not push.`

**Fix 2 — `manuscript/chapter-33.md`** (attach the speaker beat to the Tier B line; protected wording unchanged)
- old: `"You've been reading that board for eleven minutes."\n\nLira came up beside him with the bread under her good arm.`
- new: `"You've been reading that board for eleven minutes." Lira came up beside him with the bread under her good arm.`

After applying: re-run `ed.sh overlap book-01-the-shattered 5` (expect 0 unprotected) and `ed.sh gates`; no metric moves more than a rounding step (−12 words, one fewer paragraph).
