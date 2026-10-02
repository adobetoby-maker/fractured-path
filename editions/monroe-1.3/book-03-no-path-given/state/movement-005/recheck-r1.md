# Recheck r1 — Book 3, Movement 5 (chapters 32–39)

Review seat: Claude Fable 5.1 (targeted recheck of Repair r1; author Claude Opus 5.5). Date: 2026-10-02.
Scope: the brief's findings and every changed region (word-level diff of each chapter against `pre-repair/`), not a fresh review. No manuscript file was touched.

**Verdict: CLOSE WITH LINE FIXES** (three small; one is a pre-existing slip found in a moved paragraph, two are optional tightenings). No second repair.

Tool re-runs (read-only): `ed.sh overlap book-03-no-path-given 5` → 0 unprotected shared runs, 5 protected (allowed). `ed.sh gates` → reader_standard=0, metadata=0, modern=0 on all eight files. `formula_metrics.py` on the eight chapters → 39,894 words; mean 13.09; ≥40-word share 4.0%; 31 scene breaks; 1,022.9 words per scene — matches the author's table. Scene breaks per chapter pre→post: 32 (5→4), 33 (6→4), 34 (6→5), 35 (6→3), 36 (3→2), 37 (6→5), 38 (7→4), 39 (6→4). None removed inside the match (ch36's two remaining breaks are the gate→yard and the halt→settling, as before).

---

## (a) Brief items

| # | Item | Status | Where / note |
|---|---|---|---|
| 1 | ch36 "pressure-sense he had taken from Brom" | RESOLVED | ch36 ¶ "It came up along his skin…": "It was the weight-read he had taken from Brom and taught to find a body's lean through linen and felt and an oak post." The Pressure-adjacent fragment, named two pages earlier as "banked and unspent," no longer collides. |
| 2 | ch35 Oona refused leave vs front bench | RESOLVED (leave granted) | ch35: "They said yes, if I make it up on Saturday." / "I'll be sorry about Saturday. I've already decided." The joke survives. See (e) for the three-chapter check. |
| 3 | ch36 "the next quarter of an hour" vs Book 4 "one hour" | RESOLVED | ch36 gate ¶: "However long the match went, two of the people at that rail had walked him as far as the gate." No duration is asserted anywhere in ch36–37 for the match itself (ch37's "one hour" / "rest of the hour" / "Twice in one hour" are the morning drill; "About eighteen hours after the match" is the log). Nothing now contradicts Book 4 ch9's "Six weeks of demonstration sessions plus one hour of genuine engagement." |
| 4 | ch32 "three weeks ago" | RESOLVED | "On this wall," she said, "a fortnight ago, I told you something." |
| 5 | ch33 "Is that what it's called?" | RESOLVED | Brom: "Anybody who's ever beaten a—" / Cael: "A lattice. The instructor says that's Ternhall's word." / Brom: "Edran uses it too. I asked her, after, whether it was a declaration, and it isn't." Cael now supplies the word the instructor gave him two pages earlier; Brom's hesitation on "a—" motivates the supply. Reads cleanly. |
| 6 | ch37 Karis "You told me…" | RESOLVED | "You've been keeping something," she said slowly. Cael's reply ("I told Lira I was keeping it. Not you. I never told you there was anything.") still lands as a clarification of who knew; set up by his own "I said I'd tell you something… On the first day after." |
| 7 | ch34 Wray "on Thursday" | RESOLVED | "You'll spend a great deal at the sitting." |
| 8 | ch36 "on the earth… at the height of his ankle" | RESOLVED | "The first point bloomed on the earth a pace to his right, where the framework would have sent him, and the second went down a pace behind his left heel." |
| 9 | Typos: ch36 "gates, By supper"; ch37 "bottom of."; the dropped "it" (cold read 1765) | RESOLVED | ch36: "…emptying its noise out through the gates. By supper it would have turned into six stories…". ch37: "…could not get to the bottom of it." The cold read's line 1765 is the same "bottom of." item, so the dropped word is this one and is fixed. |
| 10 | Optional: cut "It came on Thursday" | RESOLVED | ch39: "It's new," he said. "I don't understand it yet." |
| 11 | Optional: trim the notice-column personification | RESOLVED, one phrase still agentive | ch36: "Wherever the notices were kept, it seemed, a column had been ruled for this from the start." (hedged, fine) and "…except this one, which had had a line for the difference all along and had left it blank through four notices, and had written in it today." The archivist's patience and the "known the difference" are gone; the record remains the grammatical subject of "had written in it," a trace of agency. Offered as optional line fix 3 below; not a violation of §10 on its own (no maker, no watcher named). |
| 12 | P2 — one clause of cause for the Iron read's jump | RESOLVED | See (b). |
| 13 | P2 — the lit channels' death made Karis's own | RESOLVED | See (b). |
| 14 | ch36 near-reuse of source ch13 (about a dozen sentences) | RESOLVED | The tabled phrasings are absent from ch36 ("public drafts," "Closer was not close," "feelings later," "archivist," "weather on a window," "debt collected," "wall loses to water," "fear dressed as calm," "weather from another valley" — each 0 hits), replaced by the author's own figures ("only ever studied the copy the other kept for show," "Nearer was still not near enough," "in one hard payment," "as a bank goes under a slow river," "the rules, the arithmetic, and under both something held so still it might have been fright," "as if it belonged to some other afternoon," "as rain happens near a field"). None of the new figures appear in source ch13. Overlap tool confirms 0 unprotected ≥10-word runs. |
| 15 | Trims: supper recap; Karis's archive speech; two repeated similes | RESOLVED | ch36: "Karis was at a table of her own by the far window, alone, as she had announced she would be…" (the three-sentence recap gone). ch38: speech now ends "That's all I can say out loud. The rest I've written, because I couldn't say it without it coming out sounding like something it isn't." — it states only what the paragraph does not, then hands over the page. "dealer laying out cards": exactly one in ch39 (supper now "counted them out… on her fingers," which also agrees with the kept "sixth finger… thumb of her other hand"). "wall somebody meant to keep": exactly one (ch36 rail); ch39 now "planted like a gatepost." |
| 16 | Priority 3 rhythm: joins, 10–15 long sentences, seven merges | RESOLVED | Metrics verified above. Seven listed merges all present (ch32 supper→wall; ch33 Edran inside the study run; ch34 night three→wall; ch35 evening→supper; ch36 inventory→breakfast; ch37 note→Quenna's room; ch38 yard→quiet room) plus seven more, all same-place same-occasion; none inside the match. Speech and landing beats unchanged (diffed: "Halt." / "Position." / "Opponent," / "Reset," / "Match halted… Called a draw." all verbatim). |
| 17 | Coordinator ruling: "six hundred" stays | RESOLVED | ch37 ¶ "He had carried the oldest of the four…": "…a ferocity that had once stood across from him in front of six hundred people and nearly ended him." Kept. The match crowd remains "three hundred people, or near it." |
| 18 | Length 39,000–41,500 | RESOLVED | 39,981 (wc) / 39,894 (tool). |

---

## (b) The match (ch36)

**One unbroken scene.** From "The formal yard was fuller than it had been for the exhibition" to "Nobody in the yard seemed to care about the ruling at all" there is no scene break and no cut-away. Every exchange is intact and in order: first exchange (points round him → first channel behind his heel → second, third → south chalk → "Halt." "Position." "Opponent," → the release discovery → "Reset,"); second (the read opened → "The world changed texture." → she sees it and moves her floor out → the short channel → "He woke the fragment." → "He chose it." / "He went through." → the reach → "His hand closed on cold air a finger's width from her coat." → "Halt." "Position." "Opponent," → walk back, the bill); third ("She came to finish it." → early ground → pairs → left wall, right folded → bait → "He was inside her lattice." → "Sixteen." → "Out of angles." → time-dilation → "So he stopped running." → "He reached for it." → palm on the earth → "Her point arrived into it a breath later, and would not take." → "The lattice went out of time." → "Karis stopped." → "She began to laugh." → "Match halted… Called a draw."). The ~250 words of time-dilation before the reach are kept whole (the four paragraphs from "Time did what it does" to "He reached for it," only "the way"→"as" inside them). Coda beats kept: the settling, the notice (P1 exact), "He had a handle," the exchange with Karis, Lira's hand on her breastbone, Brom's nod, the binder entry (§9.2 anchor exact).

**New causal clause 1 — the Iron read.** Two sentences carry it: at the reset, "But in the quiet room every point had been a demonstration, laid for a ledger with nothing behind it, and he had never once had the read open inside a real fight"; and at the start of exchange two, "At full economy every point she laid was a whole commitment, thrown down close and fast with everything she had behind it. A committed point leaned on the air as hard as a fighter's weight leans before a strike; the read had been made for exactly that." Consistent with the teaching: ch33 Brom at the rail ("You can feel the air's decided before she has. It leans."), ch33's "Never join what you can still move," ch34's post work (the read finds a lean through felt and oak), and the unchanged "Three times in twelve. Twice in the last session." The reliability is now a property of her full-economy points, not of him getting better — which is exactly Book 4 ch9's "at full economy" and keeps the reach itself unexplained by skill. Karis's side (ch38 first notebook: "the candidate had read her near points before they lit, and… she had moved her floor outward in the second exchange to answer it") agrees, and her move outward is still what sets up the short channel. The read's range limit ("well beyond where any read could feel the air lean") survives.

**New causal clause 2 — the lit channels' death.** "Her whole assembly had been built to light in one sequence… and she had been holding every lit channel on that same count. Her off hand had gone still for the fourth beat, and the fourth beat did not come." Then: "The count she had been holding everything on was gone, and her grip on the lit channels went with it, so that they faltered and went dark one after another as she lost them." The deaths are hers. This is consistent with what the chapter already establishes about held channels — at the first reset "The channels dimmed and went out, one after another, as she released them," and in exchange two "two long channels died, released" — so a channel lives on her hold. ch38 from her side: "she had been holding every lit channel on that count, and that when the count broke she had lost her hold on all of them at once, and they had gone out." One nuance, not a defect: her ledger says the hold went "all at once"; the yard shows them going dark "one after another." Both can be true (grip lost at once, the dying a run of hisses), and the ledger is the terser instrument. ch33's lattice ("lit across section two all at once with a sound like a drawn breath") and the rule she showed him ("A point won't take where there's still heat standing") are unchanged and still load-bearing.

**Reveal limits.** No maker, no theory of the mechanism beyond "trying with everything she had" and the binder sentence; Quenna states nothing; the notice is read by Cael only. Book 4 echoes hold: "one hour" (no contradiction), "sustained observation plus genuine stakes" (ch37's read-aloud binder entry: "It takes what's used on me… the stakes aren't the weather round it"), "it completed because I was trying" (ch36: "She was trying with everything she had, all of it, in front of three chairs and three hundred people" / "There was only Karis, trying with everything she had").

---

## (c) The drop's cost — three breaths, chosen up front

Consistent at every mention, and the scaling is now a clean ladder:

- **Plant, whole push sent home** (ch30, unchanged): "I counted six breaths, and you weren't taking any of them." — the bruise ch36's inventory still carries ("the bruise from the whole push had finally gone").
- **The drop test** (ch34, unchanged): a quarter of a palm strike, woken before the strike, let go: "a tightness across the breastbone, like a strap pulled one notch, for the length of one breath"; "Two of three. Cost: one breath." Lira told before; "I'm choosing the size first. A quarter."
- **The taper's tally** (ch35): "the drop at two of three for one breath and a strap."
- **Hobb's crossing** (ch33, unchanged): the channel's push "threw him back a full step… It had spent itself on him, all at once, as a trap spends itself on the foot that springs it."
- **The match** (ch36): "He chose the size first, as he had promised Lira he always would, and he chose all of it, the whole of Hobb's stove door and not a quarter, more than he had ever let go of in his life." … "The fragment closed on the push in the same instant, the whole of it, the size he had chosen… the shove that had put Hobb back a full step did not put him back at all." … "The drop's bill came due on the walk, and it was bigger than any it had ever sent him, because he had let go of more than ever before. A strap pulled tight across his breastbone for three breaths instead of one, and then it eased." … "The crossing had cost a burn he would feel for a fortnight, and three breaths, and something else that was harder to name."
- **Lira's count** (ch37): "you were through before I got to two and reaching for her. Then on the walk back I counted three, the way I counted six on Brom's floor, and you weren't taking any of them, and I couldn't breathe till you did." — the crossing itself about one breath, the bill three on the walk back; her "the way I counted six on Brom's floor" now quotes ch30 exactly.
- **Heat is not force** (coordinator ruling) survives: "The heat it could not touch."

One wording stretch, offered as optional fix 2: ch34 has him *tell* Lira he is choosing the size first; it is not a promise to "always" do so. "as he had promised Lira he always would" overstates by one word.

---

## (d) Merges, splits and joins — fragments, dangling referents, separated speakers, changed meaning

Every changed region was read with context. Findings:

- **No fragment left by a split.** The ~70 splits (ch33–38) all fall at clause joints; spot-checked the ch36 reset ("At the mark he counted what he had left, Vell's way, the counting first and the feeling after."), the ch34 drop ("He did it as he had learned to on the night of the fast catch, before anything moved: the gathering begun low in his chest and held there half-ready…" — appositive after a colon, reads aloud), ch37 ("Neither of them said the thing they were walking round until the end, when she said it coiling the rope from the pump, with her back to him."), ch38 ("She did not go down to the midday meal, all the same." — "all the same" answers "she was going to do as she was told" in the previous paragraph).
- **No speaker separated from a line.** The merged runs keep attributions: ch32 "Both," said Brom, who had gone back to his barley…; ch34 "Eleven," said Lira, who was breathing hard too…; ch37 "That's the condition," said Karis at last, very quietly.; ch39 Lira's six stories still counted on fingers.
- **Referents.** ch32 "Oona was in front of it before the first bell" — "it" is the new sheet of the preceding paragraph (now immediately adjacent after the move; cleaner than before). ch37 "He had carried the oldest of the four since Ardenmere" — "the four" is "The four older ones" of the previous paragraph. ch33 "The second thing Cael learned that week was how she talked." — the first thing ("Karis had no accidents") still precedes it with the Edran scene now folded between; the ordinal survives.
- **Meaning preserved.** ch33's lattice-lighting sentence: "…laid four more points in the space of a breath. Then she joined everything she had, so that the channels lit… too many and too fast for Cael to count before he saw what they had made. He counted sixteen points." — channels uncounted, points counted; same facts as before. ch34 "Six touched him on the third night… having done what he had not believed possible" — same. ch35 taper compression keeps every listed tell in the one sentence ("the tells and the timings and the four words and the rule about cold air and the number sixteen").
- **One pre-existing slip in a moved paragraph** (not introduced by the repair; present in `pre-repair/` too): ch32 Oona reads "*By her written consent*" off the posted sheet, but the sheet as quoted two paragraphs above does not contain those words ("Opponent: Karis, Ember Path, Iron Rank Three. Conditions to be posted. Week sixteen."). Line fix 1 below adds the phrase to the sheet; cheapest side to fix and it keeps Oona's "That means she asked."

---

## (e) New defects

- **Continuity (day/time).** ch35: the conditions are posted "on the Tuesday of the sixteenth week"; the merged "session in section four that afternoon" is therefore the Tuesday session, agreeing with "On the Tuesday night he redrew every chart" and "On the Wednesday afternoon." ch32: the sheet goes up "By the next morning"; Oona before the first bell; the rumor market "By the midday meal" the same day; Edran "two days later." Clean.
- **Oona's attendance.** ch35 (Wednesday evening): leave granted, Saturday make-up, "I'll be on the front bench." ch36: "And on the front bench, squeezed between two first-years taller than she was, Oona, with her slate on her knees and both hands pressed flat on top of it." and, in the third exchange, "somewhere on the front bench Oona's slate creaking under her pressed hands." ch39 (Sunday): "I was on the front bench… I was close. Closer than the panel. When you went down on one knee… There was a light under your hand. Not hers. Yours." Consistent across all three. Her Saturday make-up block (week 16) and "Oona Kindles on Saturday" / "Six days" (week 17, said on Sunday) are different Saturdays; no clash.
- **Reader Standard.** gates=0; nothing in the changed text adds an oath, gore, or innuendo. The burn remains "felt, not lingered on" (three sentences at the crossing, Wray's measurement in ch37).
- **Protected lines — all exact.** P1 (ch36, the five-line notice, fenced, verbatim); P2 (ch37, verbatim); P3 (ch37: "What I need to know — not for the file, for me — is whether you can *not* do it. In front of people who wish you harm." / "I don't know yet."); P18 (ch32, inside the consent, verbatim). §9.2 anchors in this movement: "Fifth fragment. First one I chose. Everything before this was the architecture acting. This one was me." (ch36); "I need to understand what I'm actually doing before it gets someone killed." (ch39); "You just started choosing." / "It's a heavier word than I expected." — "Most of the good ones are." (ch39). All verbatim.
- **Canon.** No new fragment, no new name, Iron Skin spelled in full; "Acquisition: directed" only in Cael's reading and the binder; Quenna's record P2 unchanged.

---

## (f) Second repair?

No. Every brief item is resolved; the two new causal clauses hold from both sides; the drop's cost is consistent across ch30, ch33–37; the match is one scene with every beat; no merge or split leaves a fragment or orphan. The three line fixes below are small, exact, and do not chase an average.

---

## Line fixes (each old text occurs exactly once in its file)

**1. ch32 — pre-existing: put "by her written consent" on the sheet Oona reads it from.**
File: `manuscript/chapter-32.md`
Old: `Opponent: Karis, Ember Path, Iron Rank Three. Conditions to be posted. Week sixteen.`
New: `Opponent: Karis, Ember Path, Iron Rank Three, by her written consent. Conditions to be posted. Week sixteen.`

**2. ch36 — optional: ch34 has a statement, not a standing promise.**
File: `manuscript/chapter-36.md`
Old: `as he had promised Lira he always would`
New: `as he had told Lira he would`

**3. ch36 — optional: remove the last trace of the record as writer (§10: no watcher implied).**
File: `manuscript/chapter-36.md`
Old: `and had written in it today.`
New: `and today the line was not blank.`
