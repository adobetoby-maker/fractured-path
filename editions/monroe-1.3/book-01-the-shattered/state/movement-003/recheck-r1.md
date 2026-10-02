# Recheck r1 — Book 1, Movement 3 (ch 14–20)

Review seat: Claude Fable 5.1, targeted recheck after the author's Repair r1 (Claude Opus 5.5), 2026-10-01.
Scope: the brief's items and the changed joins only — not a fresh review. Method: `REPAIR-BRIEF.md`, the
"## Repair r1" section of `AUTHOR-REPORT.md`, then every changed region of the seven chapters read in
inline word-diff against `pre-repair/` (full chapter text with changes marked), BOOK_MAP §7 protected
lines grepped and compared character for character, the ch4 notice text read against ch20's reading,
calendar markers across ch14–20 grepped and traced, `ed.sh overlap` and `formula_metrics.py` re-run.

**Verdict: CLOSE WITH LINE FIXES.** Every brief item is resolved. The repair introduced three small
mechanical defects (a stray quotation mark, a doubled scene-break marker, and a sentence that is now
verbatim identical in ch17 and ch20), plus one idiom slip. All four are one-line fixes. No second
repair is warranted: nothing unresolved is a concrete defect, and the remaining metric drift is inside
the edition brief's "Working ranges and accepted drift" or within a hair of it.

---

## (a) Brief items

### Priority 1

| Item | Status | Location / evidence |
|---|---|---|
| ch17 "walked into a circle four times" → three | RESOLVED | ch17:31 "walked into a circle three times" (Renn, Brenna, Amrit on the morning after Amrit). |
| ch18 cutaway "Three weeks later he had told her about her own left foot" → four mornings later | RESOLVED | ch18:333 "Four days later he had told her about her own left foot". Consistent with the brief's own day-11 ruling and with the pouch arithmetic in ch14 (sum on the tenth; Vell on the fourth morning after Renn). |
| ch16 Amrit "forty years of lifting stockpots" → working years | RESOLVED | ch16:249 "a cook's fist with twenty years of lifting stockpots behind it". He is "somewhere near forty". |
| ch17 day-order wobble around the old man's "Six" | RESOLVED | Re-anchored: Vell books Petra at the table "on the morning after Amrit" (ch17:3); the wager on the wall follows; "In the afternoon of that same day, on the cooper's roof" (ch17:59); Petra watched "that afternoon"; "The next morning, on the way up to the Cinder House" the old man says "Six" (ch17:85–89), in its own section; then "On Sunday". No backward jump. The one small back-step ("He wrote it that night in the front of the Log" precedes "the afternoon of that same day") is signalled explicitly. |
| ch19 "two things… four weeks" | RESOLVED | ch19:87 "carrying two things in a corner for weeks". |
| ch20 Lira's "Nobody in here says you have to leave" vs the ch4 notice | RESOLVED | ch20:165 "Nobody in here tells you to leave the city, or your grandfather. It takes the house off you, in one line, and then it writes down, very exactly, what it would cost him to keep you near, and gives it to him to add up for himself." Matches ch4: residential access above Unranked "revoked effective immediately" (the house, one line), Unranked residence retained (not the city), cohabitation note (the cost to Hesk). The "This is built" point is intact. |
| Pear tree seeded in ch14 | RESOLVED | ch14:133 "under the stunted pear tree in the corner that had given up growing tall and grown wide instead"; ch19:223 calls it back ("crouched wide in its corner by the wall") instead of describing it anew; ch19:251 "The pear tree." |
| Calendar ch17–20: "nearly three weeks" vs "four weeks"; make every marker agree | RESOLVED | Traced (arrival ≈ day 1; Renn ≈ day 8; Brenna Thu ≈ day 13; letter day 19; Amrit day 20; Petra Sunday ≈ day 23; the drop Wednesday ≈ day 26; ch20 Thursday ≈ day 27). Every "three weeks" now measures from Renn / the start of Lira's mornings / the Log (ch17:31 "Not three weeks ago, standing on the rise" at day 21; ch18:245 "every morning for three weeks", "nearly" removed; ch20:131 "one to four inside three weeks", :135 "watching you for three weeks", :189 "bruised three weeks ago", :209 "That was three weeks ago", :279 "written over three weeks"). Every "four weeks" measures from the last Arbiter check at Weaver's Row in Denvash (ch19:199, :201, :309; ch20:65). "a fortnight ago" (ch20:135, the left catch) and "since Weaver's Row" (ch20:245, :275) are consistent. Day markers in ch18 ("the next morning", "two mornings", "three days", "Wednesday") and ch19/20 ("that evening", "yesterday morning", "Last night") agree. |
| Lira's registry-lookup disclosure told twice | RESOLVED | ch18:309–311 now carries only: she knew the word and the four "since the first night", "had never told him how she knew, or that she had gone looking at all", and "decided… that she would tell him, the next time he gave her an opening. Not about this morning; about that." The crate, the pie, the candle, the four lines and "reading somebody's letters" appear once, in ch20:55, and ch20 adds the link "I'd made up my mind yesterday that I would". Cael's "He had not expected that" (ch20:53) now has its surprise. |
| Shade reason out of ch18, into ch20 as hers to give | RESOLVED | ch18:339–341 keeps only "There was the shade, too… Not yet, she thought." ch20:233–239: "You never asked why I start in the shade." / "It was yours." / "It still is. I'm lending it." then the light-lies-less reason and his recognition that she had been teaching it every morning. Pays off ch14:127 ("until then it was hers") exactly. |
| Power limit: Petra's Force shows a cost | RESOLVED | ch17:193 "between exchanges she shook out her right hand at the wrist, once, the way you shake water off it, as though the shove she put into other people came back a little way into her own arm." Placed after the sixth exchange, before the rope's "Seven". |

### Priority 2

| Item | Status | Location / evidence |
|---|---|---|
| "The circuit doesn't care what the registry says" once; title may stay | RESOLVED | Exactly one occurrence in the movement, ch20:171, in Lira's speech, character for character. Her "Out here you're what you can show…" coda is cut (ch20:175 "and said no more"). Cael's Log records it in his own words (ch20:273 "*Nobody at Vell's table has ever asked to see a card. The book only knows what it saw me do.*"). Title "What the Registry Says" stays. ch10's earlier "The circuit doesn't care what your Arbiter said about you" is outside the movement and differently worded. |
| Vary the post-bout ritual once across ch15–17 | RESOLVED | Amrit (ch16) varied: Vell stops writing and watches with the pen lifted (ch16:231) instead of "Vell's pen moved"; "At the rope the noise had changed" removed from that bout; the water-bucket debrief cut to the cloth, the burn advice and the breath line (ch16:303–307); Lira does not walk him home — she wets the cloth, says "The right people clapped… Vell said the right breath", and leaves (ch16:309–311). Brenna and Petra keep the full ritual. No orphan: "How you lose matters", "You conceded… before he burned you", "In the fourth I let you" and "Most people don't see it after either" have no later callback (grepped ch16–20); the deliberate-shimmer point survives in Cael's thought (ch16:253) and Log claim 2. |
| Voice-won't-hold beat: keep one | RESOLVED | Kept ch17:223; ch20:137 is now "He looked at the post for some time before he answered." |
| Two horse similes: keep one | RESOLVED | ch17:107 Marrow's look is now "a shopkeeper gives a scale that has begun… to weigh against him"; ch18:127 "the way a buyer walks round a horse" kept. |
| ch19 anaphora "He thought about…" ×7 → three or four | RESOLVED (over-delivered) | Pre-repair 8 occurrences of the string; post-repair 1 (ch19:273 "He thought about the people who had it."), the rest folded into their neighbours. The shape is thinner than "three or four" but the ledger meditation reads as joined thought, not a list; not a defect. |
| "almost smiled / almost laughed" cluster | RESOLVED | None remain in ch14–20 (grepped). ch15 "It was nearly a laugh." (Brenna) is a different beat and stays. |
| "Boop." | RESOLVED (author's call) | ch15:13 now "Nose," said flatly. |

### Priority 3 — rhythm (reported, not re-scored)

Re-run of `formula_metrics.py` on the seven chapters matches the author's table exactly: 35,157 words;
sentence mean 12.89 / median 8; ≤5-word 33.9%; ≥40-word 3.9%; 30 marked scene breaks, 950 words per
scene; paragraph median 29 / mean 31.8; Flesch 90.8 / FK 3.8. `ed.sh overlap book-01-the-shattered 3`:
"0 unprotected shared runs of >= 10 words; 4 protected runs (allowed)". Against the edition brief's
working ranges: ≥40-word (2.5–4.5) and words/scene (850–1,050) are inside; ≤5-word (≤~34), paragraph
median (≤~30) and FK (3.5–6) are inside the accepted drift; sentence mean 12.89 sits 0.11 under the
13–15.5 range. That is drift, not a defect, and the author's account of why (the three bouts' exchanges,
Lira's clipped speech and the plant are all protected) is accurate. Note that fixing the doubled
scene-break marker in ch19 (below) reduces counted breaks to 29 and raises words/scene to ~1,012 — still
inside the range.

---

## (b) Joins and splits — fragments, dangling referents, separated speakers, changed meaning

All changed regions of the seven chapters were read with context. The joins are clean: dropped tags in
two-person scenes leave the speaker recoverable in every case checked (ch15 "Well?"; ch17 "What were you
looking at?" and "You saw her shoulders."; ch18 "Something broken?"; ch20 "Does it always answer?", "Why
are you asking?", "It's worse because I don't have a map…", "Neither.", "It was yours." / "It still is.").
Reordered passages (ch14 bread, paper stall, columns, balance; ch16 fish-man nod, letter; ch17 wager
opening, roof, sand-bag; ch18 keys, cutaway lookup; ch19 table, ledger meditation, midnight yard; ch20
notice, supper) keep their sense. Two mechanical slips and one idiom slip were found:

1. **ch19:29 — stray opening quotation mark left when the tag was dropped.** Text reads
   `"A man. "Polite. Not from round here, I'd say, by his boots.` (pre-repair: `"A man," he said. "Polite.`).
   The first quote never closes. Fix below.

2. **ch19:157–159 — two consecutive scene-break markers.** The sentence "He thought about writing to
   Hesk." was removed and replaced with a second `---`, so the file now has `---` / blank / `---` / blank
   / "He got as far as taking a clean sheet…". The Hesk section should have one break. Fix below.

3. **ch19:45 — "As far as Torvin had said, he had asked not for a name but for *the circuit kid*".**
   "As far as X had said" is not an idiom; the intended sense is "from what Torvin had said". Fix below.

One cosmetic join, optional: ch19:255 "Silence would have been something there and choosing not to
answer" (pre-repair: two sentences). It parses, but "something there and choosing" is rough on the ear;
a comma for "and" smooths it. Listed as optional.

No sentence was found that no longer means what it did. Protected exchanges and lines are intact (see (c)).

---

## (c) New defects introduced by the repair

- **Calendar:** every "three weeks" / "four weeks" / day marker in ch17–20 agrees (traced in (a)).
- **Lookup disclosure:** ch18 no longer carries the content; ch20 delivers it as news. Confirmed.
- **ch20 notice reading vs ch4:** the quoted line (ch20:159 "*Continued cohabitation by a [SHATTERED]-classified
  individual may affect the standing-holder's guild status pending Compact review.*") is character for
  character ch4:45. Lira's paraphrase (house taken in one line; no order to leave the city or Hesk; the
  cost to him written down) is accurate to ch4:43–45.
- **Amrit aftermath:** no orphaned reference (grepped "how you lose", "let you", "conceded", "walked him
  home", "right breath" across ch16–20). "a girl on a barrel… did not stop until he had walked all the way
  to the table" and "She only came down off the barrel long enough" agree. The Log entry following
  directly on Lira's exit without a scene break (ch16:311–313) is abrupt but readable, and ch17 uses the
  same shape after "Count it." — consistent.
- **Protected lines (BOOK_MAP §7), checked exact:** "How did you know that was coming?" / "I don't know."
  ch18:121/125 (and the italic callback ch18:349–351); "The circuit doesn't care what the registry says."
  ch20:171 once; Hesk's Second entry quoted exactly in ch17:289 and ch19:155 ("your body is going to learn
  before your mind does"); the notice sentence ch4:47 untouched; Petra's "What were you looking at?"
  ch17:237 and the shoulder touch ch20:189; "You could only already be going." ch18:235 and the eleven
  attempts ch18:229; "I'm losing on speed now. Not on seeing." ch17:273; Vell's "A name goes in when the
  yard comes to see it." ch14:311; the Log's Claim / Evidence / Ruling columns with *h*. No Reader
  Standard slip seen in the changed regions; gates reported 0 by the author and nothing contradicts that.
- **New repeat (defect):** ch17:297 now ends "…while Torvin's voice came up through the floorboards with
  its one word and the last line of light under the door went out." — a verbatim match for ch20:281
  "Then Torvin's voice came up through the floorboards with its one word and the last line of light under
  the door went out." Pre-repair, ch17 glossed the word ("said *Lamps* through the floorboards, the way it
  did every night") and only ch20 used "its one word"; the repair collapsed the two to one sentence,
  three chapters apart, and both echo ch7:241–245 where the ritual is established. An audiobook hears it
  twice. Fix below restores ch17's distinct wording.
- **Doubled `---` in ch19** (see (b) 2) also inflates the tool's scene-break count by one.

---

## (d) Second repair?

No. All brief items are resolved; the four defects found are single-line mechanical fixes with no
knock-on; the metric shortfall (sentence mean 12.89 vs 13) is drift of the kind the edition brief
defines, and the brief forbids a repair to chase an average. Close with the line fixes.

---

## Line fixes (exact; each old text matches the manuscript once; `\n\n` = paragraph break)

Required:

1. `manuscript/chapter-19.md`
   old: `"A man. "Polite. Not from round here, I'd say, by his boots.`
   new: `"A man. Polite. Not from round here, I'd say, by his boots.`

2. `manuscript/chapter-19.md`
   old: `---\n\n---\n\nHe got as far as taking a clean sheet`
   new: `---\n\nHe got as far as taking a clean sheet`

3. `manuscript/chapter-17.md`
   old: `In the end he lay on his back under the beam while Torvin's voice came up through the floorboards with its one word and the last line of light under the door went out.`
   new: `In the end he lay on his back under the beam, and Torvin's voice said *Lamps* through the floorboards, the way it did every night, and the last line of light under the door went out.`

4. `manuscript/chapter-19.md`
   old: `As far as Torvin had said, he had asked not for a name`
   new: `From what Torvin had said, he had asked not for a name`

Optional (cosmetic):

5. `manuscript/chapter-19.md`
   old: `Silence would have been something there and choosing not to answer,`
   new: `Silence would have been something there, choosing not to answer,`

After applying: re-run `ed.sh overlap book-01-the-shattered 3` (expect 0 unprotected) and the metrics
(expect 29 scene breaks, ~1,012 words/scene, other figures unchanged within rounding). No further
recheck needed.

---

## Notes for Movement 4 (no action here)

The author's M4 conditions stand: the honest sort unfolding the torn Renn page; Lira's morning report
recurring or visibly lapsing, never supplying a ruling; Petra's wrist shake available to be paid by Lira
later. Add: Lira now says the "it was yours / I'm lending it" shade line in ch20 — M4 should not re-explain
the shade reason; and ch20's "Every morning. You write it down. I'll tell you what I saw" sets the Log's
`(Lira, h)` report as a standing ritual from the first morning of M4.
