# Recheck r1 — Book 3, Movement 1 (after the author's Repair r1)

Review seat: Claude Fable 5.1 (targeted recheck, not a fresh review). Author of record: Claude Opus 5.5. 2026-10-01.

Read in order: REPAIR-BRIEF.md; AUTHOR-REPORT.md "## Repair r1"; manuscript/chapter-01.md … chapter-08.md in full against the frozen copies in pre-repair/ (diff per chapter; every changed region read in context); BOOK_MAP.md §9 and packets/MOVEMENT-001.md for the protected wording; review-editorial.md §4.2 F1–F8 and review-cold.md §4 for the itemized slips. Tools re-run: `ed.sh overlap book-03-no-path-given 1`, `ed.sh gates book-03-no-path-given 1`, `formula_metrics.py` on the eight chapters. No manuscript file was modified.

## Verdict

**CLOSE WITH LINE FIXES.** Every brief item is resolved or honestly reported as residue. The 107 mechanical splits leave no fragment, no dangling referent and no sentence that has changed meaning. The repair introduced one concrete continuity defect (Ch1 attempt count, see C1) and one audible echo (Ch3, C2); both are single-sentence fixes. Two pre-existing slips in Ch7 surfaced while checking the joins and are offered as optional fixes. Nothing here warrants a second repair pass.

## Protected wording — all exact

| Item | Location | Status |
|---|---|---|
| P6 category line *unclassified observer*, gloss *has not yet undergone formal Kindling assessment*, three readings, tea going cold | ch2 lines 147–161 | Exact. Three readings on the page; tea lukewarm, then colder. |
| P7 "Enrolled. The word is doing a lot of work." | ch2 line 261 | Exact. |
| Wray's D1 record "Unorthodox architecture. Consistent execution. No safety concerns." | ch7 line 121 (spoken), ch7 line 205 (repeated), ch8 line 67 (log) | Exact, all three. |
| Naveth anchor 1 "Every student in this building is someone's clerical error, Cael. You're simply the largest one we've ever had the nerve to sign for." | ch3 line 111 | Exact. |
| Naveth anchor 2 "Quenna is the one who priced you." | ch3 line 131 | Exact. |
| Tide line "Session nine. Could not reproduce. Still don't know what that was." | ch1 line 130 | Exact. |
| Compression notice (B2 Ch24) | ch1 lines 119–124 | Byte-identical to books/book-02-iron-circuit/chapters/chapter-24.md lines 12–15. |

Protected scenes (Ch4 Wray session; Brom vs Hobb; D1 and "He chose. He chose nothing."; the Oona exchange and "Where's shattered?"; Naveth's ledger) are intact — joins only, events and lines unchanged. Packet phrases ("Faster opponents give me less body to read", "Show enough to pass. Bank everything that matters.", "panel speed", "The floor just watched something else.", the Edran exchange, "I think I have a teacher.", "You'll want to come back.") all present verbatim.

## (a) Brief items

**Priority 1**

| Item | Result | Location / note |
|---|---|---|
| Source reuse (37 unprotected runs) | RESOLVED | Re-ran overlap: `0 unprotected shared runs of >= 10 words; 2 protected runs (allowed)` — the Tide line and Naveth's anchors, which the script's protected list does not know. Matches the author's report. |
| Reveal pacing (F1) | RESOLVED | ch6 line 99: each fragment has a source name; "They had arrived the way weather arrives, without asking and without explaining"; nothing about watching or stakes anywhere in the eight files (grep clean). |
| Brom's injured side | RESOLVED | Right everywhere: bait opens the right (ch4 line 71), strike lands on right ribs (line 75), right elbow tucked (line 111), ch6 line 181/183, ch8 lines 141 and 287. The ch4 line 43 angle test (strikes from Brom's left; he turns right and is left open on the left) is a different, earlier condition and is not a contradiction. |
| "three days ago" | RESOLVED | ch6 line 181 "four days ago"; line 217 "four days". Strike is day 2 (ch3 ends on day 2 with Cael going to find Brom), Brom's room is night of day 6. |
| Sixth bell vs floors closing | RESOLVED | ch4 line 111 "the sixth, the last of the floor blocks" — consistent with ch3 line 17 (fifth and sixth are the floors). |
| Ch5 scene order vs "the night before" | RESOLVED | ch4 line 187 puts the ceilings argument on day 3 supper; ch5 line 199 "the night before, after Brom's argument about ceilings over the barley" on the day-4 morning. Clock holds. |
| Dropped-word sentence (archive door; actually ch3, not ch5) | RESOLVED | ch3 line 183 "set into a frame whose stones had been cut by different hands, in a different century, from the walls on either side of it." Grammatical. (See C2 for the new echo in the same sentence.) |
| Prynn "thirty years" | RESOLVED | ch6 line 47 "Every year or two, for sixty years." Also cures the cold read's cosmetic note (opening unerringly to the page now matches the frequency). |
| Rank "by his tag" | RESOLVED | ch8 line 137 "Copper Rank Eight by the board". |
| Ch6 Edran / girls on the stair | RESOLVED | ch6 line 131 "to Naveth or the gate clerk or anyone who asked across a desk". Edran and Hobb appear only in ch8 (grep: 0 hits in ch1–7). |
| "a year and a half" ×10 → 2–3 | RESOLVED (to 0) | Zero uses. The brief allowed two or three; the author found no sentence needed one. Acceptable under BOOK_MAP §12.16. |

**Priority 2**

| Item | Result | Location / note |
|---|---|---|
| The outside reader given a face | RESOLVED | ch2 lines 199–209 (triplicate form, *Registry Copy, for Notation*, Quenna initials it, brown envelope to the regional registry office, third-day post, "Usually… Usually."); ch3 line 209 (the calendar line as a count: "Today was the second day. The eighth was six mornings off, and the brown envelope… would go down the hill on the third"); ch2 line 315 (Hesk's letter in the same bag); ch5 line 265 (post went down "yesterday" on the day-4 notice — correct); ch6 line 75 and ch7 line 151 (the patient figure at the far end of the envelope's road); ch8 lines 85–101 (*Received for Notation* card, purple date stamp, unknown initials, reference number, back up the hill on day 9, shown day 10). No Coss, no Level 4. "Regional registry office" only. Physical, dated, within canon. |
| Lira's standings bout (626 words → ~1,800 allowance) | RESOLVED | ch8 lines 159–187, roughly 1,250 words in the ring. Exchanges three (feint low then high; the rear-heel plant tell; he stops planting) and four (she denies him distance inside his elbows, walks him in an arc, ducks the last planted push, two fingers to the breastbone, heel on the chalk) are now on the page. Left shoulder taken on purpose; consistent with line 195 "good shoulder" and the cold cloth at line 221. |
| Ch8's second week shown | RESOLVED | ch8 lines 79–101 (the supervised hour where Quenna writes less, then the card) and 105–131 (the page format, Hobb from the drill board, Brom's "I'll forget it"). The told summary is gone. |
| Room: registry-history folded; bell recitation once; restating logs converted; door cap 3; ounce cap 1 | RESOLVED | ch5 line 43 carries "never closed an account" and "every amendment is a confession" in the taxonomy instructor's mouth; "Keep it" at line 105. Bells recited once (ch3 line 17); the tour no longer repeats them. Counts: "a door shutting in another room" 3 (ch1 67, ch6 189, ch7 57); "not one ounce" 1 (ch4 9); the ch3 stair, ch4 end, ch5 Lira-dot, ch6 refusal and ch8 Hobb logs are now narration or a single turning line. |

**Priority 3 — rhythm and economy.** Re-measured: sentence mean 13.44 (from 9.66; target 14.6), ≤5-word share 33.7% (from 38.6%; ~28%), ≥40-word share 4.6% (from 1.1%; 3.3%), scene breaks 30 (from 68), 963 words per scene (target ~950), paragraph median 18, FK 4.83. All eight figures match the author's table. Word count 36,738 by `wc`, inside 35,000–39,000. The residue the author reports (mean 1.2 short; short-line share 6 points high, almost all one-to-three-word dialogue; ≥40 share above target in ch7–8) is real and is the right place to stop — the remaining short lines are character ("Yes." "I know." "Again.") and merging them would cost more than the average gains. PARTIAL against the numeric targets; CLOSED as a judgment.

## (b) The 107 mechanical splits

The splits were made against the mid-repair text (the 8.1% overshoot), not the frozen copy, so they do not show in a pre/post diff; I located them by their signature in the repaired text (a sentence boundary followed by And / But / Then / Not / Which, or a short verbless sentence) and read each junction in context. Finding: **no split leaves a fragment, a dangling referent, or a sentence that no longer means what it did.** The ones that look most mechanical, each checked and acceptable as written:

- ch1 line 154: "Ten ranks in each tier, with Rank Ten as the threshold. And to cross from one tier into the next you needed two things…" — verbless recitation beat followed by an And-sentence. Free-indirect listing voice; reads as Cael running the ladder in his head. Keep.
- ch1 line 262: "A gate of iron-strapped oak, newer, set into it. And beyond the wall a few roofs…" — deliberate cataloguing (the paragraph is about Cael cataloguing). Keep.
- ch2 line 267: "…only bumped his arm with hers once. And then the seventh bell rang…" — clean. Keep.
- ch3 line 17: "Then the rule about the residence wing after the eighth bell, which was that there was no residence wing after the eighth bell…" — verbless, but it is the joke's shape. Keep.
- ch4 line 53: "The strikes looked the same at first… But they were short: each one began properly and stopped…" — clean. Keep.
- ch7 line 9: "…the boy nodded once, and Wray returned to her chair. Then he settled his weight and waited…" — the pronoun "he" follows a sentence ending on Wray; gender disambiguates, and "the boy" is the prior clause's subject. Keep.
- ch7 line 63 (split from the pre-repair single sentence): "It spilled out of him harmlessly, as it had on the first road morning when he felt it sliding toward his knee. His forearm took the blow the ordinary way that any forearm takes a blow…" — the split is clean; the factual slip in the first half is pre-existing (see P1 below).

The verbless flags elsewhere (ch1 "Days old. Bad at everything."; ch6 "Small. The same every time. Dull, with any luck."; ch8 "Anger burned out. Curiosity kept a notebook.") are deliberate beats that pre-date the repair and land.

## (c) New defects introduced by the repair

**C1 — ch1 attempt count now contradicts the opening try (concrete, fix required).** The repair recast the tally so it adds up ("twelve tries; catches on 7, 10 and 12; one misroute to the shoulder on 4") but wrote, at line 45, "They went on until they had made twelve tries between them… On the first three nothing caught at all; the fragment sat in him like a word on the tip of the tongue, present and unreachable." The opening try (lines 17–27) *is* try one of the twelve ("went on until… twelve"), and in it the fragment catches — "he held a piece of Brom's push the way a person holds water in cupped hands" — and he drops it to keep it out of the knee. Pre-repair this was not a contradiction because the frozen text said "They did it eleven more times. The first three failed cleanly," so "first three" meant tries 2–4. The fix is one phrase: "On the next two nothing caught at all". Tally then: 1 dropped (knee), 2–3 nothing, 4 shoulder, 5–6 nothing (early), 7 catch, 8–9 nothing, 10 catch, 11 nothing, 12 catch — three in twelve, "most of the twelve were failures," "the tries in between went nowhere, because he had reached a breath too early" all hold.

**C2 — ch3 line 183, "on the grounds" twice in two sentences (echo, minor).** Repairing the dropped-word sentence produced: "The archive was the oldest thing on the grounds. It sat at the end of a short passage off the main hall, behind a door darker than any other on the grounds, iron-banded and heavy…" The frozen text had "darker than any other door Cael had seen here." Audible read aloud. One-phrase fix below.

**C3 — ch6 line 5, Quenna's "Spend your four days on yourself" now said on an explicit day 5 (borderline, optional).** The repair pinned the corridor talk to "The morning after the notice" (day 5; the notice is day 4, "He had four days to decide"). Said on the morning of day 5, "your four days" is three days and a morning. A listener will not count; a systems-minded reader might. Optional fix below keeps her count and cadence.

**Checked and clean:**
- *Registry Copy, for Notation* / *Received for Notation* trace: consistent across ch2 (envelope sealed, third-day post, "Usually"), ch3 (the count), ch4 line 165 (Lira: post goes out on the third day), ch5 line 265 (post went down yesterday on day 4), ch6/ch7 (the figure at the far end of the envelope's road), ch8 (card back day 9, shown day 10, "Usually" callback, card kept in Quenna's folder; line 287 inventory agrees). The round trip of about a week is plausible. Carbon-copy paper is in-universe (books/book-04 chapter-11 has "the month's product carbons").
- The card's "long reference number" versus the packet's "no routing code yet": not a violation — the M2 routing code (BOOK_MAP item 16, "matches no listed tier") is a different object — but the planner should decide now whether the M2 code is or is not the same number, since the card is new canon (author flags it; I second the flag).
- Hobb named only in ch8 (0 hits ch1–7); Edran only in ch8; the stray mid-repair "Hobb" in ch6 is gone ("the broad Stone student").
- Repeated beats: the ch7 lines 185/187 echo ("That's why the girls on the stair said good morning." said by Cael, then by Lira) and the ch1 echo pairs ("Shoulder."/"Shoulder.", "Three in twelve."×2, "Like a ledger."×2, "It's small"×2) are all in the frozen text — a pre-existing tic, not a repair artifact; note for a later pass if the owner wants it thinned. "Furniture" for Hobb: 4 uses pre and post, unchanged. The new ch8 line 101 image ("a door close somewhere at the far end of it, and knowing that someone else was home") rhymes the outside reader with the Compression knock; it is a different sentence, the exact phrase is capped at three as asked, and I read the rhyme as intended. No fix.
- Reader Standard: `ed.sh gates` reader_standard=0, metadata=0, modern=0 on all eight; my own oath/profanity grep is clean; the Lira–Brom cold-cloth beat stays as drafted.
- Protected lines: see table above — none altered.
- Scope: only the eight chapter files and AUTHOR-REPORT.md changed in state/ and manuscript/ for this movement. (manuscript/chapter-09.md through chapter-11.md appeared in the directory during this recheck, timestamped after the repair — Movement 2 in progress; range for this movement is `1 8`; they were not read.)

## Pre-existing slips found while checking the joins (not in the brief; optional)

**P1 — ch7 line 63 "as it had on the first road morning when he felt it sliding toward his knee."** On the first road morning the force went *into* the knee ("the joint that still remembered being used as a drain", ch1 line 23; log "Knee on day one", line 105). The harmless spill he is recalling happened on the third and last road morning (ch1 lines 23–27). Identical in the frozen text (pre-repair line 117).

**P2 — ch7 line 117 "He had spent a week watching Brom be hit by this boy."** Hobb hit Brom once, on day 2; Wray "didn't let him hit me again" (ch6 line 211); and ch8 line 111 has Cael watching Hobb only once before D1. Identical in the frozen text (pre-repair line 201).

Both are one-sentence fixes and both touch continuity the book otherwise keeps with unusual care, so I list them; the coordinator may apply or defer.

## (d) Second repair?

**No.** The one unresolved concrete defect (C1) is a two-word fix; C2 and the Ch7 items are single phrases. Nothing in the brief is NOT RESOLVED. The metric residue is the author's honest stopping point, and chasing it would mean merging short dialogue lines that carry character. Apply the line fixes below and close.

## Line fixes (apply mechanically; each old text matches the manuscript exactly once — verified by grep)

**Required**

1. File: `manuscript/chapter-01.md`
   Old: `On the first three nothing caught at all`
   New: `On the next two nothing caught at all`

2. File: `manuscript/chapter-03.md`
   Old: `behind a door darker than any other on the grounds`
   New: `behind a door darker than any other he had seen here`

**Recommended (pre-existing continuity, outside the brief)**

3. File: `manuscript/chapter-07.md`
   Old: `as it had on the first road morning when he felt it sliding toward his knee`
   New: `as it had on the last road morning when he felt it sliding toward his knee`

4. File: `manuscript/chapter-07.md`
   Old: `He had spent a week watching Brom be hit by this boy, and now had been hit by him himself`
   New: `He had watched this boy put Brom on one knee on their second day here, and now had been hit by him himself`

**Optional (borderline)**

5. File: `manuscript/chapter-06.md`
   Old: `Spend your four days on yourself`
   New: `Spend what's left of your four days on yourself`

After applying: re-run `ed.sh overlap book-03-no-path-given 1` (expect the same 2 protected runs, 0 unprotected) and `ed.sh gates book-03-no-path-given 1` (expect zeros). No metric re-run needed; the fixes change fewer than twenty words.
