# Book 3 completion pass, Lane A (ch1–23): report

Author: Opus 5.5, O'Connor 1.3 seat. Date: 2026-10-02.
Files edited: `manuscript/chapter-01.md` … `chapter-23.md` only. No git commands were run. No scene breaks were added or removed; each chapter's `---` count is unchanged.

## 1. Results against target

| Check | Target | Before | After |
|---|---|---|---|
| Chapter skeleton share | ≤5% every chapter | 6 chapters over (ch2 8, ch3 9, ch7 7, ch10 23, ch11 29, ch12 11, ch13 15, ch14 12, ch22 12, ch23 14) | every chapter 0–3% |
| Scenes above 12% | none | 19 flagged, plus ch4 s4 at 12.5% | none (highest unrebuilt scene: ch8 s6 at 9%; highest rebuilt scene: ch23 s1 at 5%, made up of two protected log lines and two sentences at 0.50) |
| Unprotected sentences ≥0.65 | none | 168 listed at ≥0.65 in ch1–23, all but a handful unprotected | none |
| `ed.sh overlap` (8-word runs), M1/M2/M3 | 0 unprotected | 14 / 11 / 17 | 0 / 0 / 0 |
| `ed.sh gates`, M1–M3 | 0 | 0 | 0 (reader standard 0, metadata 0, modern 0 in all 23 chapters) |

Six sentences still score 1.00 against the source. All six are protected wording:
- P7, "The word is doing a lot of work." (ch2)
- the two §9.2 Naveth lines (ch3)
- the §9.2 log line "…walls they think they own." (ch14)
- the two protected sentences of the §9.2 log "If it can be directed…" (ch23)

## 2. Probe before and after, by chapter

Run with `SHOW=1 bash editions/monroe-1.3/tools/sweep_probe.sh book-03-no-path-given 1 3`. Each cell is the skeleton share, before → after.

| Ch | Before → after | Ch | Before → after | Ch | Before → after |
|---|---|---|---|---|---|
| 1 | 3% → 2% | 9 | 2% → 2% | 17 | 4% → 0% |
| 2 | 8% → 1% | 10 | 23% → 0% | 18 | 1% → 1% |
| 3 | 9% → 1% | 11 | 29% → 1% | 19 | 1% → 1% |
| 4 | 4% → 1% | 12 | 11% → 1% | 20 | 4% → 1% |
| 5 | 3% → 2% | 13 | 15% → 2% | 21 | 5% → 0% |
| 6 | 4% → 3% | 14 | 12% → 0% | 22 | 12% → 1% |
| 7 | 7% → 2% | 15 | 0% → 0% | 23 | 14% → 2% |
| 8 | 3% → 2% | 16 | 0% → 0% | | |

Movement totals:
- M1: 5% → 2%
- M2: 12% → 1%
- M3: 5% → 1%

## 3. Rebuilt scenes

| Scene | Probe before → after | Words before → after |
|---|---|---|
| ch3 s2 | 17% → 2% | 1,590 → 1,741 |
| ch7 s4 | 24% → 0% | 547 → 588 |
| ch10 s1 | 17% → 0% | 1,263 → 1,247 |
| ch10 s2 | 50% → 0% | 394 → 425 |
| ch10 s4 | 38% → 0% | 613 → 666 |
| ch10 s5 | 33% → 0% | 535 → 526 |
| ch11 s1 | 43% → 0% | 332 → 348 |
| ch11 s2 | 49% → 4% | 891 → 913 |
| ch11 s3 | 34% → 0% | 768 → 777 |
| ch11 s4 | 33% → 0% | 1,012 → 1,064 |
| ch12 s2 | 31% → 0% | 1,503 → 1,448 |
| ch13 s2 | 18% → 3% | 718 → 720 |
| ch13 s5 | 27% → 0% | 1,635 → 1,524 |
| ch14 s2 | 26% → 0% | 952 → 995 |
| ch14 s5 | 24% → 3% (the protected log line) | 557 → 580 |
| ch21 s5 | 14% → 0% | 900 → 825 |
| ch22 s2 | 24% → 3% | 613 → 636 |
| ch22 s5 | 26% → 2% | 1,046 → 1,044 |
| ch23 s1 | 32% → 5% (two protected log sentences) | 1,737 → 1,777 |

Every rebuilt scene is within ±10% of its old length. The largest moves are ch3 s2 (+9.5%) and ch21 s5 (−8.3%).

### What each scene does, and how it was rebuilt

Each line gives the scene's events in brief, then what changed in how it is built.

- **ch3 s2.** Events: the stair; the office (window to the yard, one chair, the brown alumni shelf); "Why did this academy take the risk?"; the joiner's look; the three ledger entries; Naveth's eleven years and the decade between; one finger, then two (priced right, priced wrong); the protected clerical-error lines; kindness against incentive; what happens when he stops paying off; Quenna priced him and stood surety; the order of the ledger; "Thank me with your assessments." Construction: the scene now opens on the stair. Naveth hands over the alumni book first and explains his history and the model afterwards, so the evidence comes before the argument. The finger-raising moves onto the ledger, as ch17 recalls. Cael's second question became "And when I stop paying off?"
- **ch7 s4.** Events: the slate turned face down; the off-record voice; "Today proves you're real" (kept, because ch42 quotes it); the reader who will want him gone; "You being ready has never been what keeps me up"; the bruise; the chalk ring and the broom; two shown, two held back, one never reached for; two fingers in the smear. Construction: the scene opens on the sound of the slate. The ending paragraph is new.
- **ch10 s1.** Events: "I am."; her name, Path, rank and school; eight months of secondhand accounts; asking to ask; the protected line "Trust is a finding, not a premise"; what a dull day of it would look like; stopping with one word as experimental hygiene; Prynn's tea and "Noted"; take a month. Construction: the catalogue of everyone who has ever looked at him moves from the middle of the conversation to after Karis leaves, so it now answers her parting line. Karis's sources now include "my mother's cousin, who trades wool through Ardenmere", which matches the ledger.
- **ch10 s2.** Events: Prynn, "She looked at the shelves"; the bad tea; two laps of the training hall; the caution, against the fact that she asked; he watches her. Construction: written fresh, with a shorter closing turn.
- **ch10 s4.** Events: the wall; the conversation retold nearly whole; "She asked"; take the month; the category, not the person; the Fenmark file never read; the scar against the argument; terms on paper, "This is what asking looks like"; "Sit with it". Construction: the scene opens on Lira's silence after the telling is finished.
- **ch10 s5.** Events: breakfast; Karis watched Brom's block and asked about "the second half" (ch21 and ch26 depend on this); Velmere; "put that in the scales"; the log entry ("asked before looking"); the verdict against the question; "Weighing it." Construction: written fresh. The verdict passage is now a short argument, where it used to be a list.
- **ch11 s1.** Events: Karis on the landing, placed to one side; she changes the question; "primary evidence"; he says yes; he no longer decides alone; the log line. Construction: the scene opens on the landing. The reflection that he no longer decides alone moves after the yes, as the reason it mattered.
- **ch11 s2.** Events: the scarred table under the bricked-up hay door; the tile players; Brom in the corner; Lira opposite the empty chair; Karis on the half-bell; Brom in favour; Lira's two protected lines and the case-builders. Construction: the scene opens in dialogue, with Lira saying "I'm informed", and the table is described afterwards.
- **ch11 s3.** Events: Karis concedes "I want data"; Marlowe's joke; she asks for a road from the first to the second; Lira weighs it; Lira's look at Cael; his silence; Cael wants it as defence. Construction: beats reordered. Cael now speaks before Lira's verdict, and her "That's a reason I can't argue with" and "Terms" come together in one turn.
- **ch11 s4.** Events: the seven clauses in order, with the barley joke. The texts of clauses 1, 4, 5 and 6 are kept exactly, because ch21, ch22 and ch60 quote them. Also kept: Cael's notes clause as clause 3, Brom's capitals, the reading aloud twice, and the four signatures. Construction: the scene opens on Lira's "Numbers". The discussion is retold around what each person is guarding.
- **ch12 s2.** Events: the two pens and the borrowed stool; Lira unannounced (clause 2); three passes; the pen moves only while he moves; he catches himself adjusting; the cap's click; "Does it feel borrowed, when you use it?" — "I don't know."; Lira in the corridor; "it doesn't look borrowed"; the log. Construction: the scene opens on Karis's equipment. The question is reshaped. The log's last line became *Someday I'll find out. Wanting to won't come into it.*
- **ch13 s2.** Events: Coss reads the notice three times; the notice text (kept exactly); the grey card; the ruled bar and the restricted field; the note sent upward with no answer; the drawer; jurisdiction; the three-sentence quarterly report; the superior who never writes; "by signing a form". Construction: the scene opens on the closed folder under his hands. The district office ("one window on an alley", as ch47 has it) comes after the bar.
- **ch13 s5.** Events: the request reaches Naveth in week 4; the open door; the three items; comply at the last lawful hour; requisition slips, one per office (ch42 depends on the slips); Prynn's afternoons; the white-haired seat away in the north; "Does it work?"; a person or a process; Vell's openings; the history of paper quarrels; pass tomorrow; Karis in the yard, "May I write it down?", "I'll show you the line." Construction: Naveth's strategy ("Does it work?" and "a person or a process") now comes before the slip-making, so the slips illustrate the strategy rather than lead to it.
- **ch14 s2.** Events: the week passes; the honey thief; the binder fills up; Brom walks with him; Quenna, "don't spend the worry before the bill"; the heading for Quenna's sayings; Karis beside him; his handwriting shrinks (ch23's "Your handwriting's back" depends on this); *Cause unknown. Probable.*; "documentation". Construction: the scene opens on the shrinking handwriting, which Karis's observation pays off later.
- **ch14 s5.** Events: the wall at dusk; the bundle on the road; "where I am" (the walls and the door they may knock on); Brom's steward, letter before cart; the protected log; the lamps and the courier. Construction: written fresh, keeping the same beats.
- **ch21 s5.** Events: relief, then fear; she has never seen the binder; "Told you she had a method" (spine wording, kept); "It isn't proof"; Lira's sum; "Thank you"; they leave in order; the floor gives way; "Even them. Even her." Construction: the scene opens on the relief. Lira now says "Later, if you want" aloud, so the scene agrees with ch22, which already said she said it.
- **ch22 s2.** Events: fragments as weather; the not-choosing held him up; the grammar of object and subject; aimable, so a story; appetite (ch23's letter needs the word); Lira, Brom, Feryn, Reydan; worse for not knowing; the lamp, the first page. Construction: the scene opens on the question "if not weather, then what". The weather belief is told backwards from there.
- **ch22 s5.** Events: Brom at the rail counting where Cael has looked; "watched me like a ledger"; Wray does not steal his balance; intent is the difference; "*Aimable* was her word. *Hungry* was never hers. You supplied that part yourself." (the protected tail is kept); the four names; intent only from now; the walk to Lira. Construction: the scene opens in Brom's voice, and his two silent bouts are told after.
- **ch23 s1.** Events: Lira on the frozen wall; the confession; "told me the same day"; nothing to forgive; "It's sums"; what would really cost him; her fears; "Better your hand than nobody's"; "Somebody's been steering"; learn it; "Same rule. Heavier load. It'll hold." (ch31 calls this back); the covenant; the people who keep accounts; the protected log; whom the fear is for. Construction: the scene opens on the crossing of the yard. The protected phrases stand as short sentences of their own, and everything around them is new.

## 4. Other sentences recomposed

Every unprotected sentence in ch1–23 that scored ≥0.65, and enough 0.50–0.64 sentences to bring each chapter to 5% or less, were re-shaped: folded into a neighbouring sentence, reordered, or rebuilt. The chapters touched were ch1, 2, 3 (s4), 4, 5, 6, 7 (s3), 8, 9, 10 (s3), 11 (s5), 12, 13 (s3, s4), 14 (s4), 17, 18, 19, 20 and 21 (s2–s4).

All 42 unprotected 8-word overlap runs were also re-composed.

The changes that touch documents or logs:

- **ch5 notice.** "The candidate will demonstrate at his own election" became "Demonstration at the candidate's own election". The ch5 notice text appears only in ch5. The phrase "at his own election" survives in ch7, ch46 and ch55, which use their own wordings.
- **ch13 challenge draft, first line.** It now reads: *The respondent is enrolled at Greyvane Academy as an unclassified observer, a category its own gloss limits to candidates yet to undergo formal Kindling assessment.* The line appears only in ch13, and later chapters refer to "two true lines", which still holds. The second line is unchanged.
- **ch16.** The petition paraphrase now reads "candidates still waiting on their formal Kindling assessment". The protected gloss wording is unchanged in ch2.
- **ch11 log heading.** It now reads *Changed. Remember that it changed.* No other chapter quotes this heading.
- **ch14 routing-code log, last clause.** Now: *a line in the binder costs less than guessing wrong later about which things mattered.* No other chapter quotes it.
- **ch18 and ch20 logs.** Their wording changed: "a school asking its question out loud", and "Edran withdrew. He did it in the ring…". Neither is quoted elsewhere.

## 5. Referents checked

I grepped ch1–61 for each rebuilt scene's nouns and lines before rewriting it, and kept everything below.

**From ch3 s2:**
- ch17 "He raised one finger, as he had on the first morning with the alumni ledger" and "the joiner's look".
- ch20 and ch37: "Thank me with your assessments", said on his second day.
- ch43: the thin brown alumni books and the worn stair. Only one visitor's chair, as ch43's carried-up chairs require.
- ch42, ch43, ch56: "priced wrong".
- ch60: the two clerical-error lines.

**From ch7 s4:** ch42's quotation, *Today proves you're real.*

**From ch10:**
- ch21 and ch26: Karis asked Brom about "the second half" in her first week.
- ch25: she "asked if she could ask"; eight months of other people's handwriting.
- ch23 and ch39: "asks before she looks". The log keeps "asked before looking".
- ch15: Lira's Fenmark file, which she has never read.

**From ch11:**
- Clause 1 text (ch60), clause 4 text (ch22), clause 5 text (ch21), clause 6 by number (ch14, ch16, ch18, ch21), clause 2 as a witness clause.
- The barley clause (ch25, ch28, ch31).
- The scarred table under the bricked-up hay door, which many later chapters use.
- Volume six, pages forty to fifty-two (ch21).

**From ch12:**
- The borrowed stool and the two pens (ch22, ch25, ch35).
- Sessions at the fifth bell in section four, from the first Thursday of week four (ch21).
- ch61: "Karis asked whether it felt borrowed, and I told her I didn't know."
- "the old knock".

**From ch13:**
- ch59: the note sent upward about the restricted field, and the ruled bar.
- ch47: the district office with one window on an alley.
- ch41: "flat language the form demanded".
- ch42: the requisition slips and the last legal hour.
- ch14 and ch45: the seventh day.

**From ch14:**
- ch23: "Your handwriting's back."
- ch24 and ch35: the honey thief.
- The protected log.

**From ch21–23:**
- ch22: Lira's *later, if you want*.
- ch22: Cael was afraid of watching the Glass pair "like a hand looks at bread". ch29 says he wrote that line in the binder. ch22 s4 was not rebuilt and still has it only as an italic thought; see §7.
- ch23: Hesk's letter leaves out "appetite".
- ch31: "Same rule. Heavier load."
- ch24: "a frozen wall".
- Brom's fetch numbers.

**Canon against the ledger and book map:**
- Wray is a woman.
- Naveth's eleven years and a decade between, with no Greyvane years numbered.
- The Compression non-use at D3 ("a shell on his guard … refused a road").
- The right-side rib bruise.
- Karis has never seen the binder.
- Cael is fifteen. No "year and a half" was added.

## 6. Metrics

`python3 editions/monroe-1.3/tools/formula_metrics.py` was run on ch1–23 together.

| Measure | Before | After | Working range |
|---|---|---|---|
| Sentence mean | 13.47 | 13.31 | 13–15.5 |
| ≥40-word share | 3.9% | 3.7% | 2.5–4.5% |
| Words per scene | 930 | 933 | 850–1,050 |
| ≤5-word share | 32.5% | 32.3% | up to ~34% |
| Paragraph median | 23 | 23 | up to ~30 |
| Flesch Reading Ease | 85.0 | 85.7 | (target 72.3) |
| Flesch-Kincaid grade | 4.75 | 4.62 | 3.5–6 |
| Words | 106,986 | 107,281 | |

Per chapter, for the chapters with rebuilt scenes (sentence mean / ≥40-word share, before → after):

| Ch | Before | After |
|---|---|---|
| 3 | 14.05 / 4.6% | 13.77 / 4.3% |
| 7 | 14.92 / 5.9% | 14.68 / 5.1% |
| 10 | 13.45 / 2.3% | 13.08 / 2.5% |
| 11 | 12.86 / 2.9% | 12.83 / 3.1% |
| 12 | 13.56 / 4.0% | 13.02 / 2.6% |
| 13 | 15.02 / 1.1% | 14.32 / 2.1% |
| 14 | 13.92 / 2.8% | 13.71 / 2.8% |
| 21 | 13.89 / 4.8% | 13.40 / 3.6% |
| 22 | 16.19 / 7.4% | 15.21 / 5.6% |
| 23 | 12.83 / 5.1% | 12.68 / 4.1% |

The chapters that were outside the working ranges before (ch1, 2, 4, 5, 8, 9, 11, 16, 17, 20, 23) are about where they were. Each of ch11 and ch23 has more dialogue than prose, and their speech was kept as people speak. I joined clipped narrative runs in ch10, 11, 14 and 23 by reading them one at a time, not with a script.

## 7. For the coordinator

**Protected-patterns candidates.** Each of these is quoted verbatim in more than one chapter and should stay identical everywhere:
- Clause 1, *The binder is not part of this arrangement, and will not be asked for.* (ch11, ch60)
- Clause 4, *He can say no to any one session without saying no to all of them. No reasons.* (ch11, ch22)
- Clause 5, *No written speculation on how any capability arose.* (ch11, ch21)
- "Today proves you're real." (ch7, ch42)
- "Thank me with your assessments." (ch3, ch20, quoted in ch37)
- The category gloss *has not yet undergone formal Kindling assessment* (P6). It is already in BOOK_MAP, but the overlap tool flags any longer run around it ("who have/had not yet …"). A pattern entry such as `not yet undergone formal kindling assessment` would let later chapters quote it naturally.

**Continuity notes. I saw these and did not change them, because they lie outside the lines this pass rebuilt:**
- ch21 has Brom say "You said bring it back at the end of the month", but ch11 s5 has Karis say only "Bring it back with your own marks in it" (the ledger says month's end). One clause added to ch11 s5 would close it.
- ch29 has Lira quote "like a hand looks at bread" as something Cael wrote in the binder. In ch22 s4 it is only an italic thought. A ch22 or ch23 log line would close it.

**New minor detail minted:**
- The provost's stair has thirty-one steps (ch3, ch13).
- Karis names her mother's wool-trading cousin as one of her sources (ch10). This matches the ledger.
