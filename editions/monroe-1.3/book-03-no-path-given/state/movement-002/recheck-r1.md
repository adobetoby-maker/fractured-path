# Recheck r1 — Book 3, Movement 2 (chapters 9–16)

Review seat: Claude Fable 5.1 (targeted recheck of Repair r1; not a fresh review). Author: Claude Opus 5.5.
Read: REPAIR-BRIEF.md; AUTHOR-REPORT.md "## Repair r1"; chapter-09…16.md against `pre-repair/` (paragraph-aware diff of every changed region, each read in context; ch14 and ch16 read whole); BOOK_MAP.md §1, §3, §6, §9–§11.
Tools re-run here: `ed.sh overlap book-03-no-path-given 2` → 0 unprotected shared runs, 1 protected (allowed). `ed.sh gates` → reader_standard=0, metadata=0, modern=0 on all eight files. Words 36,495 (range 36,000–39,500).

## Verdict: CLOSE WITH LINE FIXES

Two small sequencing/referent slips introduced by the restructures (ch14, ch9). Both are one-sentence edits. Nothing warrants a second repair.

---

## (a) Brief items

| # | Item | Result | Location / note |
|---|---|---|---|
| P1.1 | Karis's calendar conformed (ch9, ch11, ch13) | RESOLVED | ch9: Marlowe "late winter" → "three weeks… four months" → clerk asked "in the spring" → "spent the summer killing the entries" → last ledger copy "in the first days of autumn… its newest entry was barely a week old" (= Reydan) → digest "nine days before Ternhall's autumn term, not a week after the reservoir" → "staring at since the winter". ch11: "late last winter". ch13: "only days before the boy went up to Greyvane"; carter's "End of the season" agrees. ch10 "eight months" (kept per editorial review) fits late winter → early autumn. One calendar; every anchor agrees with BOOK_MAP §1 (Reydan days before the book opens) and §3 (Karis arrives week 3). |
| P1.2 | Ch16 knowledge breach | RESOLVED | ch16 l.51: Karis times him from session one, "when you ran the framework with nobody striking… the gap between your eyes settling on where a strike would come from and your feet going." Session one (ch12) is the solo three-pass framework with Karis on the stool and timings in her margin; no Hobb, no sittings, no "what you told the panel" remain. ch16's only other Hobb mentions are Cael's and Brom's. |
| P1.3 | Word slips | RESOLVED | ch9 "a stocky boy the roster listed as Iron Skin" (Path no longer on the crest; "Iron Skin" in full). ch16 "read more times than he had counted" (no longer conflicts with ch14 "five times"). ch13 "the woman who kept the Ironyard's ledger" (Vell keeps the ledger; matches ch9's "ledger keeper"). |
| P2.1 | Ch16 "There isn't one to hide." | RESOLVED — option (b) | ch16 l.263: first bell rings while Oona reads page three; crowd leaves "in twos and threes… until the hall had nearly emptied and the two of them stood alone at the board." "Is it true?" / "There isn't one to hide." follow, "in the emptying hall." l.289 "The bell had stopped… feet went quickly along a corridor toward assembly, late." Nothing after the exchange in ch16 has anyone else hear or react; Cael's reflection concerns Edran's petition only; last line "I think I'll have to" stands as a choice not yet made in public. State consequence as reported: ch8 public guard intact. |
| P2.2 | Ch9 opening reaches a scene sooner; research block trimmed ~¼ | RESOLVED | Karis's section now opens on Marlowe's lecture as a staged scene with dialogue. Measured: Karis retrospective (to the standard desk) 2,521 → 2,033 words (−19%); the research block proper (thread → reservoir) 722 → 456 (−37%). Coach page untouched (verified verbatim). |
| P2.3 | Ch14 quiet week | RESOLVED | Breaks 7 → 4; five scenes as listed in the report. Quenna's post-D2 "second time is always harder" talk cut; Karis's closing "Naveth wouldn't…" cut; "Don't pay for the worry before the bill comes" and "I do documentation" kept. Duplicate shoulders beat (passage) removed; archive one kept. Two archive visits are now one continuous scene (Quenna, then Karis "perhaps an hour" later). Routing code: Naveth reduced to two reported sentences on the stair; Prynn's scene is the one consultation; binder line reads "Naveth says noise. Prynn says keep the page." Arbiter-station family and "You read *shall*" untouched. |
| P2.4 | Tics | RESOLVED | "a long moment" ×2 (ch10 archive; ch14 Prynn). "exactly as" ×2 (ch14 baker; ch15 "exactly as long as it looked"). Counted by grep across the eight files. |
| P3 | Rhythm | RESOLVED as scoped | ≥40-word share 5.2% → 3.2% (target ~3.3%). Long paragraphs broken at thought turns; dialogue and the bout untouched (ch15 edits are four narration-tic removals only). Paragraph median rose 27 → 30 and the author flags it honestly; the brief forbids chasing the average, and reaching ~18 would be a rewrite, not a repair. No action. |
| Length | 36,000–39,500 | PASS | 36,495 (wc) / 36,406 (tool). |

## (b) Paragraph breaks

Every changed region was read with its joins (ch9 1 pure-break region + 16 edit regions; ch10 9+1; ch11 5+2; ch12 12+4; ch13 5+16; ch14 5+16; ch15 0+5; ch16 0+9).

- Speaker separated from their line: **none.** No dialogue paragraph was split or re-joined.
- Split single thought: **none** that reads as a fault. One-sentence paragraphs ("She wrote it in the second notebook, not the first."; ch13 "Through all of it the boy had answered…") are deliberate emphasis and read cleanly aloud.
- Dangling referent at a paragraph opening: **one**, caused by the ch9 reorder rather than a split. The pre-repair scene break (old l.75) sat between the notebooks and "The rumor reached her by way of a joke"; the rumor now opens the section, so the same break (new l.95) falls between the notebooks and the research, and the first line after it — "It took her three weeks to find a real thread…" — reaches back across the break and nine paragraphs of notebook backstory for its object. Fix below (fix 2). Near-misses judged acceptable (antecedent is the preceding paragraph's last clause): ch10 "He did that when he needed his feet to move faster…"; ch10 "This was not that."; ch12 "It described the three passes…" (after "It was dry…").
- System text: the ch13 *Notice of index correspondence* block now opens a paragraph; it is anchored to Coss in the sentence before and the sentence after (§11 two-sentence rule met).

## (c) New defects introduced by the repair

1. **ch14 — day-8 sequence runs "that afternoon → That night → That evening."** New text (l.235): "He kept the page. He built nothing on it. That night he gave it one line in the back pages of the binder…" is followed by the scene break and the pre-existing wall opener (l.243) "That evening the three of them took the wall… while the sky… went from gold to grey," where he gets the binder out "while there was still enough light to see by" and writes the protected log line. Pre-repair, Prynn's visit was "two days later" and the binder line was written on Naveth's morning, so "That evening" had no night before it. Now the night entry is narrated before the dusk entry of the same day. "That night" is the only new word doing the damage; dropping it restores a timing-neutral sentence. (Fix 1.)
2. **ch9 — "a real thread" across the moved scene break** (see (b)). (Fix 2.)
3. Checked and clean: Karis's calendar agrees in every chapter (ch9/10/11/13/15/16 anchors listed above). ch16's timing claim uses only session one. The Oona exchange is private and nothing later in ch16 contradicts it. ch14 restructure leaves no orphan: the cut "in seven days, in my best handwriting" is still carried by ch13 ("the seven days, and the last legal hour") and ch14 l.61 ("in my best hand"); the cut "Nearly everything… working on the rest" is referenced nowhere; "Two nights before the bundle left" → "Two nights later, on the seventh day" is consistent; Prynn "looked… a good deal longer than Naveth had" matches Naveth's "perhaps ten seconds"; "She went out" (Quenna) is a single exit. ch12's two merged scenes join on the same day ("that evening" after Oona's "next morning"). ch13 "had been waiting for it" now appears once (l.59). Protected lines exact: "Trust is a finding, not a premise." (ch10); "You want data." / "We're a family," (ch11); "*They know where I am. They always knew where I was. What's changed is that where I am now has walls they think they own.*" (ch14); "You read *shall*." (ch14); coach page "*Whether I may ask.*" / "*If he says no, the finding is no. Record it and go home.*" (ch9). Reveal limits: nothing new released; "a boy with an odd word on his registry file" is within Coss's knowledge. Reader Standard: gates 0; no oath, innuendo or gore in any new sentence.

Pre-existing, not introduced, no action asked: Lira's "nine days before its autumn term began" (ch9) vs Karis leaving a day or two after a digest that came "nine days before" — hearsay in Lira's mouth, present in both versions. ch16 l.235 "students who should have been at assembly" before a first bell that rings later — present in both versions.

## (d) Second repair

**Not warranted.** Both open items are one-sentence line fixes with no knock-on. The paragraph-median shortfall is a calibration question for the planner, not a defect, and the brief rules out repairing for an average.

---

## Line fixes (apply mechanically; each old text occurs exactly once in its file)

**Fix 1 — `manuscript/chapter-14.md`**
OLD: `He kept the page. He built nothing on it. That night he gave it one line in the back pages of the binder, with no theory attached.`
NEW: `He kept the page. He built nothing on it. He gave it one line in the back pages of the binder, with no theory attached.`

**Fix 2 — `manuscript/chapter-09.md`**
OLD: `It took her three weeks to find a real thread and four months to stop finding contradictions along it.`
NEW: `It took her three weeks to find a real thread behind Marlowe's joke and four months to stop finding contradictions along it.`

Neither touches dialogue, a protected line, or a calendar anchor. Word count after both: +3.
