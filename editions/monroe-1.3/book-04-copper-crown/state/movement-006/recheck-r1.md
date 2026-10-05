# Recheck r1 — Book 4, Movement 6 "Notice" (chapters 38–44)

Review seat: **Claude Fable** (standing in for the Sol/Codex seat, which is out of quota), fresh context, 2026-10-05. Author of the movement and of repair r1: Claude Opus 5.5. Inputs read in full: the seven current chapters; `diff -U0` of each against `pre-repair/`; `REPAIR-BRIEF.md`; `review-editorial.md`; `review-cold.md`; `AUTHOR-REPORT.md` (through "## Repair r1"); `BOOK_MAP.md`; `STATE_LEDGER.md` (entry state, every "After Movement" block, and the pending "After Movement 6" block); `packets/MOVEMENT-006.md`. No manuscript or repository file was modified; no git command was run.

---

## VERDICT: CLOSE WITH LINE FIXES

Scope: three line fixes, all in narration or Log text, none inside protected wording, none inside dialogue that carries a packet line. Every brief item is RESOLVED. Continuity holds against BOOK_MAP, both ledger blocks and the packet. All four commands reproduce the author's figures exactly. The listening proof passes on every chapter apart from the three items below, two of which predate the repair.

---

## (1) Brief items

### Priority 1 — The record of five (ch43) — **RESOLVED**

Pre-repair (diff `-` at ch43 line 219):
> "They're all on paper somewhere already. Vell has them in her ledger. Greyvane's panel noted them. The transcript has them. And none of the sixth. … If the gallery sees a thing on that floor, it has to have seen it on paper first."

Current (diff `+` at ch43 lines 219–223):
> "Not all on the same paper, though." He made himself go through it sheet by sheet, the way she would have. "The transcript anybody can buy holds two of them, the Wind and the read, and that one thin Ember exhibit at the back that nobody ever reads. Gault's baseline holds the Wind numbers and the read, and the plate, where I held the Pressure back, so that line's flat, and a Compression line he ringed because the floor never gave him a fair test of it. And Vell copied the circuit record at Ardenmere. Every bout I fought is in it, the Pressure I used in public and the Compression that finished Reydan."
> "So two are public," said Karis.
> "Two are public. All five are on paper somewhere, and not one of them would be news to a panel that read everything." … "The sixth is new to every record there is."

Narration echo (line 241): "in five things that were already on paper" → "in five things that already had a trail of paper behind them somewhere".

Checked paper by paper against the ruling and the pending ledger block (STATE_LEDGER line 583):
- Public transcript: Wind + Iron read + thin Ember exhibit — matches the entry state ("Public record of capability … Nothing else").
- Filed baseline: Wind numbers, the read, the plate flat (Pressure held back), Compression ringed as untested — matches "After Movement 2" ("Pressure withheld at the plate. Compression untested on a floor that answers (ringed). Ember off the floor"). Ember is correctly NOT on the baseline.
- Vell's circuit record: the public Pressure-adjacent delivery and the Compression that finished Reydan; Cael names it without quoting it.
- "Two are public" is said aloud. The sixth is new to everything. The CONTROL answer ("the next ordinary step from something already on paper") remains true under the corrected inventory. The turn (hiding and honesty as one job) is kept.
- The author wrote "Gault's baseline" where the coordinator's message said "Greyvane's"; the brief itself says "the academy's filed baseline (M2, day 48)" and the pending ledger block says "Gault's filed baseline at Halcenvane". Gault is correct.
- No other echo of the five exists in ch42 or ch44 (grep: "Vell" and "Reydan" occur only at ch43 line 219). Nothing contradicts M8's plan (growth in five against the baseline, plate flat, Ember the early surprise).

### Priority 2 — ch38 anchors (cold) — **RESOLVED**
Exactly two sentences added, no recap, no glossary:
- line 11: "If he stopped paying, he went thin: eyes slid off him as if he were not there, and sooner or later somebody whose trade was noticing would notice."
- line 65: "His enrollment stood on that evaluation every term; if it went against him, he would be a boy with no school and no standing again."

### Priority 2 — "Hold ordinary", once per voice — **RESOLVED**
- ch38 line 219: Brom's "Rooke said keep doing it, and Gault said keep doing it, and the registrar's going to say keep doing it…" is cut; his beat is now only "more chairs".
- ch38 line 225: the window recount ("He had held ordinary all day, through a courier and a name and a covered walk with Rooke in it, and the bumps column for the day said *none*…") is cut to one sentence before the Log.
- ch40 lines 97–99: the fame paragraph's restatement ("He minded the half-metre of air round himself exactly as he had on the quietest morning … the bumps column said *none* on all three days. The rent was what it always was…") is cut to the looks, the edges and "It only made it lonelier."
- Kept, as required: Gault, Rooke, Bracken, Withrow's ownership, the protected Log listing the three men, Jask, both semifinals.

### Priority 2 — ch39, the file — **RESOLVED**
One plain purpose sentence per step, each naming what it protects against:
- copies (line 39): "That protected against the first thing a hostile reader would say, which was that the whole chain rested on one girl's handwriting."
- independent search (line 41): "It protected against the next thing a hostile reader would say: that Karis had found what she wanted to find."
- directive (line 53): "It protected against a reader who knew only the four pages everybody quoted, and would say that a repeal might be hiding in the rest."
- index (line 55): "It protected against the plainest danger of all, a reader too tired or too hurried to find the one sheet that mattered."
The third explanation of the principle (the "He had built plans for a hundred bouts…" paragraph) is deleted (diff `-61,2`). The Log is cut from five sentences to one plus the kept "same weapon, held the other way round" line (line 63–65). Karis's satisfaction (line 59) is untouched.

### Priority 2 — ch44, the countdown — **RESOLVED**
- line 3: "On the tenth of Reaping, the morning after the file was closed…"
- line 9: "That was how the days went, from the closing of the file on the ninth to the eve of the twelfth."
- line 15: "three days without performing, the ninth and the tenth and the eleventh … on the evening of the eleventh"
- line 23 (eve Log, unchanged and now anchored): "They come tomorrow. Final in eight days. The twentieth, nine." — 11th→19th = 8, 11th→20th = 9. Correct.
The scene is not expanded.

### Priority 3 — Cadence — **RESOLVED**
Reproduced (see §3): mean 13.23 → **13.61** (aim ≈13.6); ≥40-word share 4.4% → **3.7%** (aim ≤4.0%); words/scene 1,017.8 (850–1,050); prose words 31,551; wc 31,621 (30,500–33,000). I read every join in the diff: all are narration; none touches dialogue, a Log line, a landing beat or protected text. The long minute (ch42 lines 171–203) and both semifinal exchange sequences are byte-identical to pre-repair. Splits are at a natural turn in every case I checked (e.g. ch38 line 25, ch39 line 43, ch42 line 5, ch44 line 63).

### After-the-repair checks — **RESOLVED**
Overlap, gates, sweep and formula all reproduced (§3). The regenerated `source-overlap.tsv` is 0 bytes; the author's explanation (the script writes only unprotected rows to the tsv and the protected count to the summary on stderr) matches what `ed.sh overlap` printed to me ("0 unprotected … 9 protected"). This is a tool property, not a manuscript finding.

### Coordinator rulings 1–10 — all honoured on the page
1. Semifinals the ninth (ch40 board line 13; ch42 line 3 "the ninth of Reaping") and the tenth (ch41 line 61, 83; ch43). 2. Deep hip strain, "clicked once, on the oil", four days off (ch42 lines 241–245); tallow casting-floor skill (ch42 line 191). 3. "Archmarshal Vastin" named at the reading (ch38 line 87); no age anywhere (grep "sixty|fifty-one": none). 4. Schedule on the page: sittings 12th–15th, facilities the 14th, observation the 20th (ch40 line 17). 5. Karis draws the three columns on her slate; the "they don't fight" insight and the Log are Cael's (ch43 lines 193–253). 6. Both vocabulary counts reported (AUTHOR-REPORT). 7. Gwen's aunt stays an anecdote (ch40 line 117). 8. The slip known only to Brom and Cael; the observer "turned a page and wrote on" (ch43 line 285). 9. Withrow's grain store (ch38 line 109). 10. Defense done in the days available; "six days" (ch42 line 5).

---

## (2) Continuity

**Calendar.** Matches the pending ledger block day for day: d168 courier/reading (Third-day, unit at the sixth bell); d170 Fifth-day board; d172 Seventh-day (Seln's requisition, Lira's room "If I win tomorrow"); d173 the ninth (file closed at the second bell; Lira–Fiske at the fourth bell); d174 the tenth (Brom–Merrick; "Nine days"); d175 the eleventh (slip; Brom "Nine days from now … three hours"; "Three nights ago" the cross — d172, correct; "two days ago" Merrick on the stair — d172, correct); d176 the twelfth (arrival at the fourth bell; close "seven days … eight"). Gwen's "on Third-day" for the next unit = d175, consistent with the weekly Third-day unit. Seln's bundle "would wait four days" from d172 = d176. Lira's "nine days" is counted from the tenth, as the ruling allows; the hip will be ten days old at the final, as the coordinator noted for M8. No Sowing date, no month order, no Sowing→Reaping count (#35). "A month back" for session fifteen (d141→d173 = 32 days) is fair.

**Counts and rules.** Eleven names (escort 4 + clerks 3 + counsel + records officer + senior seat + Vastin). 311 sheets, four boxes, 41 pages. Top-line semifinal on the final's terms, four exchanges, draw keeps the holder (ch41 Log; ch42 line 153); ladder semifinal first to three (ch43 line 25). Fiske remains champion until the final (ch42 line 219). Lira–Brom 9–11. Brom's forearms and right shoulder carried into ch43. Lira's hip: strain → ice → stick → bottom step → tier against orders; bandage used on the batons.

**Knowledge boundaries.** Mechanism: Lira, Brom, Karis only. Seln's window names no motive and does not open the case; the "designation … graded well above" sentence is at his lawful altitude. Havel: three entries, "above his clearance", two rises; no market stranger, no Iron Skin watcher, no Level 4 explanation. Vastin: rank, name and collar only. Lira's window: hip and Fiske only; nothing of any slip.

**Protected lines.** Every protected line for Ch15–16 greps exactly once in the current text (scope and "commencing on the twelfth day of Reaping"; Withrow; Gault; Bracken ×2; the Coss Log; "What he kept, he kept."; Brom's two sentences split only by a tag, as the editorial accepted; Quenna's question; "New opponent. No tells. Begin."). Packet lines likewise ("It's the nineteenth." appears twice, both Karis, by design).

**Reserved truths.** grep for "decision point", "colder country", "four years", "since he was twelve", "Sowing", "UNBOUND", "Tide", "Quieting", "Architect", "one signature": none in ch38–44.

**One pre-existing internal contradiction found (not a brief item; fix 1 below).** ch40 line 55, the Log: "Three men told me the same thing **on the same day**, in three different rooms … Bracken over his counter **the next morning**." Gault and Rooke spoke on d168; Bracken on d169 (ch39 line 3). The sentence contradicts itself. It is Cael's own text, not the protected paragraph above it.

**Noted, no fix.** ch39 counts the defense's days from the reading day ("the fourth evening" = d171, "the fifth afternoon" = d172) while the section opens "On the morning after the reading"; the ledger's d171/d172 placements hold and no reader will count. The registrar's outer office is across the quadrangle from the records hall (ch38 line 233, ch44 line 93), so Bracken "on the step" of the records hall saying the file is "on a shelf in my outer office" is consistent.

---

## (3) Formula

Reproduced 2026-10-05 from the working directory:

```
python3 editions/monroe-1.3/tools/formula_metrics.py <ch38..44>
words_total 31551 · prose 31551 · sentences 2319
sentence_mean 13.61 · median 9 · sd 11.33
share_le5_words 0.297 · share_ge40_words 0.037
paragraph_median 24 · paragraph_mean 38.52
scene_breaks_marked 24 · per_10k 7.61 · words_per_scene 1017.8
flesch_reading_ease 86.4 · flesch_kincaid_grade 4.59
```
Identical to the author's "After r1" table.

- `ed.sh overlap book-04-copper-crown 6`: **0 unprotected shared runs of ≥8 words; 9 protected runs (allowed).**
- `ed.sh gates book-04-copper-crown 6`: reader_standard=0, metadata=0, modern=0 on all seven chapters (wc 4487 / 4071 / 3923 / 3704 / 4696 / 4960 / 5780 = 31,621).
- `sweep_probe.sh book-04-copper-crown 6 6`: TOTAL sentences=1367, **skeleton 1%, close 10%**; by chapter 1/10 · 2/11 · 2/12 · 1/9 · 1/7 · 2/9 · 0/13 (≤5% / ≤13% met; ch44 close sits at the ceiling, 13%, as before the repair).

All working ranges pass: mean 13.61 (13–15.5), ≥40 share 3.7% (2.5–4.5), ≤5 share 29.7% (≤~34), paragraph median 24 (≤~30), FK 4.59 (3.5–6), words/scene 1,017.8 (850–1,050). FRE 86.4 remains high, as in M1–M5; reported, not chased.

---

## (4) Reader clarity (thirteen-year-old lens, Reader Standard)

- **Speaker attribution.** The reading names each speaker or uses a fixed label (the Stone man, the law lecturer, the counsel). The new ch43 record passage alternates Cael/Karis with tags on the turn ("So two are public," said Karis). Both semifinals name the table's call at every touch. The arrival gives every carriage and person a referent before a pronoun.
- **Referents.** "the read" is introduced as "the Iron read" before the short form; "the plate" was planted in M2 and ch43 line 201 re-anchors "Gault took my baseline in the first month". "Vell" and "Reydan" appear once each; the sentence says what the paper is, so a reader who has forgotten the names still gets the point (a record of his bouts exists). The two ch38 anchors give the cold entrant "thin" as something observable and the evaluation as the thing the enrollment stands on.
- **The file.** With one purpose sentence per step the ch39 sequence now reads as four defences against four kinds of hostile reader, and Karis's half-glass test and "same weapon, held the other way round" carry the meaning, as the brief asked.
- **Reader Standard.** Gates 0. No profanity; violence with cost (hip, forearms) and no gore; fear named honestly ("Frightened", "Yes"); adults own their choices (Rooke, Withrow, Bracken); no romance beyond warmth ("You stayed").

---

## (5) Listening proof (every chapter)

Mechanical scan (per paragraph: odd double-quote count, odd asterisk count, `---` neighbours, numerals, abbreviations, curly quotes) on all seven chapters, then a read of every changed region:

- **Quotes / italics:** balanced in every paragraph of every chapter. No curly quotes.
- **Scene breaks:** 4 / 3 / 3 / 3 / 3 / 4 / 4 marked `---`, each with a blank line before and after. Every file ends with a newline.
- **Numerals:** ch38 `*41*` (Gwen's slate figure, already spoken as "forty-one" in the same sentence); ch42 `*4 of 4*` / `*311*` (box-lid lettering, immediately voiced as "Three hundred and eleven sheets"). Acceptable as inscriptions.
- **Abbreviations:** ch39 line 25 `*41 pp. — tabbed — DO NOT RE-SORT*` — "pp." will be misvoiced by a narrator (fix 2). The regex hits on "No." in ch39/ch41 are the word "No" at sentence end, not abbreviations.
- **Ear collisions / broken joins:** ch44 line 29 "two different page eleven" is ungrammatical aloud (fix 3; pre-existing). All r1 joins read cleanly; "Nobody answered that, though down on the river a barge called…" and "Lira was quiet for a moment, and then…" are improvements. The Havel window's "The registrar, Havel thought; he had read the name in the papers." is fine aloud.
- **Ambiguous speakers:** none found. The one "He gave him the list" (ch39 line 43) follows "Bracken took a clerk" and resolves on the ear.

---

## Line fixes (each old string verified with grep to match exactly once in its file)

1. `manuscript/chapter-40.md`
   old: `Three men told me the same thing on the same day, in three different rooms, and none of them asked the others first.`
   new: `Three men told me the same thing inside a day, in three different rooms, and none of them asked the others first.`

2. `manuscript/chapter-39.md`
   old: `*41 pp. — tabbed — DO NOT RE-SORT*`
   new: `*41 pages — tabbed — DO NOT RE-SORT*`

3. `manuscript/chapter-44.md`
   old: `two different page eleven`
   new: `two different pages numbered eleven`

Fix 1 is inside Cael's Log, below (not within) the protected "Last time the Compact…" paragraph. Fixes 2 and 3 are narration. None changes a count, a date, a protected line or a packet line.
