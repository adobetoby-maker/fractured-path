# Recheck r1 — Book 5 "The Silver Standard", Movement 7 (chapters 40–46)

**Seat:** Claude Fable, standing in for Sol (Codex quota exhausted). Targeted recheck after same-author repair r1 (`claude-opus-5-5`), per `tools/RECHECK-TEMPLATE.md` and `recheck-prompt.md`. No manuscript file was modified; no git command was run.

**Read:** all seven current chapters in full; `diff -U0` of each against `pre-repair/`; REPAIR-BRIEF.md (rulings included); review-editorial.md §6 and review-cold.md; AUTHOR-REPORT.md "## Repair r1"; BOOK_MAP §6 (M6-redated spine) and §10; STATE_LEDGER's "AFTER MOVEMENT 7" rulings block; packets/MOVEMENT-007.md; source chapters 13–15 for the P1 spot-check.

---

## Verdict: CLOSE WITH LINE FIXES

Scope: five word- or clause-level fixes, each inside one paragraph, no scene changed. Three are residual source-tracking the probe cannot see (one is the closing clause of the re-composed ¶122; two are paragraphs the editorial's table named only partly). Two are referents the repair's own re-compositions left pointing at a noun that is no longer, or not yet, on the page. Nothing structural. Every brief item is RESOLVED on the page; the four tools reproduce the author's figures exactly.

---

## 1. Brief items (diff -U0 vs `pre-repair/`)

### Coordinator rulings
| Ruling | Status | Evidence on the page |
|---|---|---|
| 1 Team-trial format as Rooke states it once; 2–2 with the ledger to Auremont, no unit figure | RESOLVED (unchanged, as ruled) | ch45 ¶113 states it once; ch46 "Two exchanges to Halcenvane. Two to Auremont. And the trial … went to the whole objective ledger." No figure posted. Rhagen's loss is left for M8. |
| 2 The ring: this build stands | RESOLVED | ch40 untouched; ch45 ¶167 the posts come out, the plugs go back. No "rebuilt" language in M7. |
| 3 Vastin: title, "forty years", no age, no conclusion, no threat; office ≈ two days by post road | RESOLVED | ch43 keeps "forty years" (×2), no age, no threat. "He had missed the first bout by two days. He had known he would." fits the two-day road. Cael's "crossed the country" (¶107) is his own hyperbole, pre-existing. |
| 4 The read at its limit catches air, no mechanism | RESOLVED (untouched) | ch46 ¶223–227 unchanged: "it read something that was not a person. It gave him half a second." |
| 5 New canon approved; Bracken fixed | RESOLVED | see P2.7 below. |
| 6 No printed date, no year increments | RESOLVED | "He had turned it some time in the night"; no date anywhere; "a year, near enough" stands. |

### Priority 1 — Source tracking
| Item | Status | Evidence |
|---|---|---|
| ch46 ¶122 re-composed, new order, "the way he looked at things" gone in every tense, "She was reading him." kept | PARTIAL → fix 3 | New ¶243 opens on her eyes (feet, hands, shoulders, face), then his recognition, then "She was reading him."; new ¶245 opens "Nobody ever had." The banned phrase is absent (`grep -c "the way he looked at things"` = 0 in all seven chapters). But ¶245's last sentence still follows the source's final clause in content and order: source "an instrument encountering data outside its tables and electing, before eight thousand witnesses, to stop and read" → manuscript "She had come across something that was on none of her tables, and in front of eight thousand people she had stopped to find out what it was." Tables → eight thousand → stop → find out, clause for clause. Fix 3 inverts it and drops the "eight thousand … stopped", which ¶239 already says. |
| ch40 Rooke, "Let him write down…" | RESOLVED | "By the eleventh, every Rhagen book open in those tiers says the same two words about you. Feet. Fire. Good." Entry through the books, not the survey's conclusion. |
| ch41 Karis's notebook | RESOLVED | "The pencil lay in the fold of Karis's notebook, where it had lain untouched since she sat down." |
| ch43 supper | RESOLVED (see fix 2 for a referent) | "Supper was half eaten before anybody said Vastin's name, and it was Cael who said it." |
| ch43 log, "checking it with his own eyes" | RESOLVED | "So he got on a coach." |
| ch43 likeness-seller, two sentences | RESOLVED | Enters through "The wind off the water was flapping a row of printed faces on a cord"; "Daeva of Auremont flapped in the middle of the row, and the man had only a thin stack of her left under a stone on his board." The second keeps the source's two facts (middle; nearly sold out) but the construction is new. |
| ch44 Seln's bench | RESOLVED | Enters through Brom: "Without looking up from his plate he put out one wrapped hand and moved the pot of mussels six inches along the table, to the empty end of the bench beside him." Then "the end of the bench was not empty any longer." The later duplicate pot-move is gone ("Brom went back to his plate."). |
| ch44 heading | RESOLVED | "It's still the heading. Nothing since has made me want a better one." |
| ch45 inventory | RESOLVED | "Against both Silvers it was the one thing I never ran short of." The closing question is also re-composed ("the entry I wrote at the window after the captain … This book can carry it from here."), which stops ch45 restating protected item 22. |
| ch45 Ternhall cup | RESOLVED | "Then, at the foot of the far colonnade, a cup went up. It rose only a little way and stayed there. Cael followed it down to the hand that held it, and the hand to a russet sleeve…" Source order (two Irons → read → turned → found → lifted) is reversed (cup → hand → sleeve → who). |
| ch45 criers' sentence | PARTIAL → fix 5 | The named sentence is re-composed ("a crier's voice went up under an awning, and then another"). The rest of the paragraph still runs the source's beats in the source's order: "listened to them as he listened to anything that had prices in it" ↔ "listened to them the way he listened to any market"; then price on Auremont / price on the final / price on the exchanges / no price on the fifth name / two criers cry it as a feature. Words varied, shape kept. Fix 5 re-enters through the framed sign. |
| ch45 the Gold | RESOLVED (see fix 1 for a referent) | "Auremont had not filed its squad yet. When it did, whatever else the list held, it would hold her, and there was no rule anywhere in the trial's pages to keep a Gold off the floor." |
| ch45 Brom at the barrier | RESOLVED | "He leaned on it, every few strides, the whole length of it, the way a man leans on a fence to find the post that gives." Brom's "Two gaps … elbows." untouched. |
| ch45 warm-up | RESOLVED | "Then he put the notebook away. Gault was waving at him from the gate with the tape, and he went." Nothing in ch46 depended on the cut "page stayed shut … until the third exchange" (ch46 ¶315 carries it: "I had it on paper this morning and didn't know what it was."). |
| ch46 filing | RESOLVED | "The fifth name went up on the board at the noon bell, after the other four … Nobody had made much of the first four." |
| ch46 two exchanges | RESOLVED (see fix 4 for the sibling sentence) | "The marshals had chalked them both up beside the bluff's name, in a sanctioned book … and no clerk alive could rub them out again." |
| ch46 Lira's architecture sentence | RESOLVED | "Half a beat early was Lira's whole trade … The lane did not take steps." Note: this sits inside the brief's keep range ("The read caught something wrong" → "It gave him half a second") and was also in the P1 table; the author re-composed the tabled sentence and left the rest of the range alone, which is the right reading of the conflict. The triple "did the right thing again, and it was the right thing again, and it was no use again" remains the source's cadence ("correct twice more … did not matter twice more"); it is inside the keep range, so I leave it to the coordinator. |
| ch46 Cael's thought | RESOLVED | "*We built a house on this floor* … *She came in by a road it hasn't got a door for.*" |
| ch46 "Then she was gone…" | RESOLVED | "The roar came back into his ears all at once. She had turned away inside it, already moving…" |
| ch46 Ephram at the pump | RESOLVED | "And she was ahead. She had the exchange, and the floor, and the whole bowl on its feet for her, and she gave up a whole second of it to stand there and look at you." Item 46 verbatim; "Like we look at you. Like you look at everything." kept; "It had four more sentences and Lira cut them." kept. |
| Keeps: "Early."; the lane sequence; Brom's gaps; Ephram from "I've watched you from the rail" | RESOLVED | ch46 ¶73 "Early."; ¶175–227 untouched except the tabled Lira sentence; ch45 ¶233 untouched; ch46 ¶327 opens as before. All fights untouched (ch40 E1, ch41 E2–E4, ch42 E1–E4 except the east/west swap, ch46 E1–E4). |

**Spot-check of the author's "every remaining ≥0.40 pair is protected, packet or noise":** I re-ran the probe's matching with the threshold lowered to 0.40 across all seven chapters against source ch13–15. Every pair at 0.50 or above is a protected or packet line (items 22, 23, 25, 44, 45, 46; "Squads shall be drawn…"; "Approve it before somebody makes me invent something"; "costs double what it scores"; Hesk's note; the Seln line at 0.89 with "thirteen"). Every pair between 0.40 and 0.49 is a short common-word sentence matched to an unrelated source sentence ("It was not surprise and it was not fear." ↔ "It was a gift, and it was the most expensive kind she had."; "The second time was in the north bay." ↔ "He put out his hand, the second time in their lives."; "He put his finger on the red box." ↔ "He put his hand flat on the face-down sheet."). The claim holds at the tool's level. The two residual tracks below sit under the probe's reach: in one the source sentence is seven tokens and never enters the probe's list; in the other the match is paragraph-shaped, not sentence-shaped.

- ch46 ¶39: "They were not five better fighters than the five in blue. … But for that exchange, and the one after it, they were a better *squad*, and it showed itself from the first call." ↔ source "They were not the better five fighters. They were — for two exchanges, in front of the packed bowl and every scout on the continent — the better *unit*, and the difference declared itself from the first objective call." Same source sentence the editorial tabled for ch46 s3; the author re-composed the s3 sibling and this one still follows it. Fix 4.
- ch45 ¶69, the criers' paragraph as above. Fix 5.

### Priority 2 — Continuity and referents
| Item | Status | Evidence |
|---|---|---|
| 1 ch44 → ch45 cart | RESOLVED | ch45: "He had carried it back from the harbour under his arm, the whole length of the quays, and up the stair". ch44's close ("He was not behind them. He was at the end.") untouched. |
| 2 "Brom held it first of the three" | RESOLVED | ch44 ¶225. Karis "took it last and kept it longest" stands. |
| 3 "Cael sat with the book on his knees" | RESOLVED | ch44 ¶245. |
| 4 Vastin "sixteen" | RESOLVED | ch43 ¶39 "very few of them had been sixteen." Cael's "I'm seventeen in about two hours" (¶111) is that night. |
| 5 Whole-name signature as a wager | RESOLVED | ch43 ¶105 "and I'd wager he signed it with his whole name." |
| 6 The draw's count | RESOLVED | ch45 ¶47 "the houses highest on the count as it stood when the brackets reached their finals." Ranking unchanged. |
| 7 Bracken, "twice since the bluff" | RESOLVED | ch45 ¶207. |
| 8 Rooke, "five Irons" | RESOLVED | ch45 ¶155 "Stopping it isn't a thing any five of you can do". No "Irons" applied to the squad anywhere in M7 (`grep` "five Irons" / "full of Irons" = 0). The author's report also mentions changing "a Gold off a floor full of Irons" → "a Gold off the floor"; that string is in neither pre-repair nor current text, so the report over-describes, harmlessly. |
| 9 ch43 Vastin trim | RESOLVED | ch43 is 3,653 words (was 3,966); the cutaway ≈1,540. The four-exchange re-narration is gone (−14/+4 lines in the diff). Kept whole: the loose-board walk; "Vastin watched the boy, as he had once sat four feet from him…"; "The boy declined to be told a story … not one person in the building was looking at it."; both entries (*Second exchange…*; *Closing. Everything I saw today, I already had a word for.*); the unread face, now tied to the touch in the light; "He had never once read one without letting it lean on whatever he had seen before it."; "It was only the place where the findings stopped."; Cael's "A man who trusted the papers…". |

**Dangling-reference check on the cuts and rewrites (the prompt's second point of care):**
- ch43 Vastin: after the trim, "He opened the book again at the end" has its antecedent ("He opened his book and wrote", ¶45); "he had not written that down either" (¶77) has its antecedent (the unread face, ¶51); "his own two lines" (¶71) matches two entries. "In the third exchange the boy took a touch standing in the light" relies on ch42, which the reader has just read. The jump from "Vastin watched the boy" straight to "What he saw in the second exchange" skips the first exchange without comment; acceptable as a cut-to, not a broken join. Clean.
- ch45 cart line: "under his arm, the whole length of the quays, and up the stair" — agrees with ch44's line along the quays and the river gate. Clean.
- ch46 category line: "Two Silvers had filed. There would not be a third from anybody who still had a tier to lose." follows "There was nobody below Gold left in this city…" without a dangling "it". Clean. This cut is also why the overlap tool's protected count fell from 19 to 18: the dropped protected run was "waited three hundred years for a bout that", i.e. BOOK_MAP item 47 (Umber, M8). Intended.
- ch44 Seln's clock: "He had heard Lira on the stair the evening before" now sits with "the house still asleep above him" at first bell, and with the proprietor's "I opened the door at eleven and she was standing on the step". Clean. The cut "with Brom" leaves no orphan; Brom's cake and his seat are independently established.
- ch45 warm-up cut: see P1 table; nothing in ch46 points back at a page being opened "in the third exchange".
- Two referents the re-compositions themselves introduced: ch45 ¶77 "it would hold her" arrives before any noun for her in the chapter (the pre-repair sentence named "the tournament's one Gold" first) — fix 1; ch43 ¶83 "before anybody said Vastin's name" is followed by Cael saying "The Archmarshal came himself", not the name — fix 2.

### Optional items (all taken by the author)
| Item | Status | Note |
|---|---|---|
| ch46 category line | RESOLVED | as above; item 47 stays fresh for M8. |
| ch42 the light | RESOLVED, physically right | Windows stay high on the west. Early afternoon the bars lie along the ring's west side (steep sun); as the sun drops they slide east ("they move east as the sun drops"; "lay across the middle of the ring and the eastern slope of the crown"); the spin goes "toward the west rail", the herding "east and up the crown, into the bright bar". All six places agree. |
| ch43 "Closing." | RESOLVED | no homograph aloud. |
| ch44 Seln's clock | RESOLVED | above. |
| ch46 routes | RESOLVED | "some through the first gap in the barrier and some round its western end". |
| ch42 day counts | RESOLVED, and the T-count agrees | ch42 scene 1 is T12: "the day after tomorrow" = T14; "two days off" = T14; Rooke "on the second afternoon" = T13, "the third day's inside Gault's four" (T12–T15, third = T14); ch43 "the fourth of Gault's four days" = T15. |

---

## 2. Continuity

- **Calendar (BOOK_MAP §6 M6-redated; STATE_LEDGER M7 rulings):** captain T11, duelist T14, Vastin T14, rest day T15, trial T16. Checked every T-bearing phrase: "He had missed the first bout by two days" (T13 arrival vs T11); "the fourteenth day"; "the chair was held for him for thirteen days" (T1–T13); "His own office's notice of travel reached the west tower yesterday at noon" (T13); ch46 "The Archmarshal had been in it two days before" (T16 − T14); Brom's cake "three days ago… the morning after your first bout" (T12 → T15). No year increment, no season word, no month word, no printed date (`grep -ciE` on the usual season/month list = 0 across the movement).
- **Counts:** bursts 4 of 4 on T11, none after (ch42 "He never burst"; ch46 "two steps, not a burst"); Ember two contacts, both on Rhagen; Compression banked twice at a handspan; the exhibitions 2–1 each, ending at the second touch; the trial 2–2 and the ledger. Figures 30/27 and 28/25 unchanged.
- **Knowledge boundaries:** Vastin never writes what he does not know; the table learns the chair's history only from Seln; nobody names the lane; Cael's log says "Don't know." Unchanged by the repair.
- **Protected lines (BOOK_MAP §10) inside M7:** items 1, 12 (both halves), 22, 23, 24, 25, 33, 44, 45, 46 verified verbatim on the page after repair; the overlap tool's protected list is identical before and after except for the intended item-47 cut. Reserved truths untouched (no Tide, no conversation with Daeva, no mechanism for the lane, Compression still unseen).
- **Later-book canon:** Vastin's "forty years" and the two-day road agree with the M8 "clears his calendar" seed ("There was a calendar on his desk, and a great deal of it would want moving"). Brom is Copper everywhere a tier is attached to him.
- **Pre-existing, not introduced by r1, for the coordinator's judgment only:** ch43 ¶87 has Lira watching the twelfth chair "through the whole bout" and missing "the best touch", while ch42 ¶191 has her at the rail seeing the first-exchange cut. One word ("most of the bout") would settle it; I have not made it a fix because the editorial passed it and the brief did not name it.

---

## 3. Formula (reproduced)

- `formula_metrics.py` on chapters 40–46: words 34,884; sentences 2,528; mean 13.80; median 9; ≤5 words 29.2%; ≥40 words 4.4%; paragraphs 923, median 27; 31 scene breaks; 918 words per scene; FK 4.38; FRE 88.3. Identical to the author's report.
- `ed.sh overlap book-05-the-silver-standard 7`: 1 unprotected run (ch43 ¶50, "the office notes that the chair was held for him for", 11w — the Seln line, allowed per the brief because the run stops before the ruled "thirteen"); 18 protected. The 19→18 change is the item-47 cut, as explained above.
- `ed.sh gates book-05-the-silver-standard 7`: reader_standard 0, metadata 0, modern 0 on all seven chapters.
- `sweep_probe.sh book-05-the-silver-standard 7 7`: TOTAL sentences 1,480, skeleton 2%, close 9% (ch40 2/8, ch41 3/12, ch42 0/7, ch43 1/7, ch44 1/9, ch45 3/8, ch46 1/9). Matches the author. The band is short of the brief's 7% target; the ≥0.40 audit above shows what remains is noise plus protected text, and fixes 3–5 remove the three sub-threshold tracks I could find by reading.
- Tooling note for the coordinator (not a manuscript fix): `protected-patterns.txt` carries the Seln line with "thirteen days before he sat in it", so the regex can never match the 11-word run the tool reports. Adding the bare pattern `the office notes that the chair was held for him for` would stop the book-level sweep re-flagging it, as review-editorial §7 asked.

---

## 4. Reader clarity

- **Attribution:** every spoken line in the changed regions has a named or unambiguous speaker. ch44 ¶115–117 ("Brom saw it too. Without looking up from his plate…") reads as Brom noticing and keeping his head down so as not to make a thing of it; a good beat, not a slip.
- **Referents:** the two re-composition referents are fixes 1 and 2. "The roar came back into his ears all at once" (ch46 ¶251) implies a silence the page never states; a reader supplies it from the stop and I do not count it as a dangle. "The fifth name … her name" (ch46 ¶3–9) is a deliberate withholding resolved at ¶23.
- **The thirteen-year-old lens:** the Vastin trim removes the one place the cold read said attention thinned; the cutaway now moves from the walk to the judgment to the two notes to the stair without idling. "Feet. Fire. Good." lands aloud. The new Seln-bench entry through the mussel pot is clearer than the old, because the reader now sees why Seln sits where he sits.
- **Reader Standard:** gates 0; nothing coarse in any changed line.

---

## 5. Listening proof (every chapter, scripted and by ear)

- **Balanced quotes and italics:** scripted per paragraph — no unbalanced `"` and no unbalanced `*` in any of the seven chapters.
- **`---` spacing:** every rule stands alone with a blank line on each side; 31 rules.
- **Numerals and abbreviations:** the only digit in prose is "Gold Rank 3" in Cael's log (ch46 ¶349), which is protected item 25 verbatim and voices as "rank three"; no abbreviations.
- **Homographs and ear collisions:** "Closing." replaces "Close." (ch43). The repair introduces "The wind off the water was flapping" (ch43 ¶157) a page before ch44's "wind a gate"; both resolve on the next word. "Feet. Fire. Good." is three clean stresses. "read" (noun/past) is the book's own word and is never ambiguous in the changed lines. "chalked them both up … in a sanctioned book" (ch46 ¶133) mixes chalk and ink by ear; the idiom carries it and I have not made it a fix.
- **Broken joins:** none found at any diff boundary; each hunk's first and last sentence was read against its neighbours. ch43 ¶41→43 is a cut-to, not a break.

---

## 6. Line fixes (each old string verified with grep to match exactly once)

1. `manuscript/chapter-45.md`
   old: `it would hold her, and there was no rule anywhere in the trial's pages to keep a Gold off the floor`
   new: `it would hold the Gold, and there was no rule anywhere in the trial's pages to keep her off the floor`

2. `manuscript/chapter-43.md`
   old: `Supper was half eaten before anybody said Vastin's name, and it was Cael who said it.`
   new: `Supper was half eaten before anybody spoke of Vastin, and it was Cael who did.`

3. `manuscript/chapter-46.md`
   old: `She had come across something that was on none of her tables, and in front of eight thousand people she had stopped to find out what it was.`
   new: `She meant to find out what he was before she went on, because he was on none of her tables.`

4. `manuscript/chapter-46.md`
   old: `They were not five better fighters than the five in blue. Nobody in the building thought that, least of all the five of them. But for that exchange, and the one after it, they were a better *squad*, and it showed itself from the first call.`
   new: `It showed from the opening call, before anybody in the tiers had a word for it. Fighter for fighter, the five in blue were the better five, and nobody in the building thought otherwise, least of all the five in plain colours. What Halcenvane had that afternoon, for that exchange and the one after it, was a *squad*.`

5. `manuscript/chapter-45.md`
   old: `Cael listened to them as he listened to anything that had prices in it. There was a price on Auremont to win the semifinal, and it was very short. There was a price on Auremont to take the final. There was a price on how many exchanges the semifinal would run. Under the long row of chalked boards, at the end, the little framed sign was still hanging where it had hung all sitting, in neat white paint. *NO BOOK ON THE DEMONSTRATION BOUTS.* And two of the criers, noticing it, had begun to cry it as a selling point.`
   new: `The little framed sign still hung at the end of the long row of chalked boards, where it had hung all sitting, in neat white paint. *NO BOOK ON THE DEMONSTRATION BOUTS.* Cael read the boards above it as he read anything with a figure on it. Auremont to win the semifinal, at a price so short it was hardly a price at all. Auremont to take the final. How many exchanges the semifinal would run. And two of the criers, who had read the little sign as often as anybody, had begun to cry it as a selling point.`

Fixes 1 and 2 are referents; fixes 3–5 are the residual source-tracking. After fix 5 the paragraph still runs into the crier's shout ("No price on the fifth man of the bluff!") and Ephram's "They've made you a feature" without alteration.
