# Recheck r1 — Book 4 "Copper Crown", Movement 7 "Archmarshal" (chapters 45–50)

Review seat: **Claude Fable** (fresh context), standing in for the Sol/Codex seat, which is out of quota. The recheck prompt says "Sol, via codex"; read that as Claude Fable, review seat. Author of record: Claude Opus 5.5 (not this seat). Date: 2026-10-05.

Read in full: `manuscript/chapter-45.md` … `chapter-50.md` (current, 29,862 prose words / 29,929 by wc), every diff `-U0` against `state/movement-007/pre-repair/`, `REPAIR-BRIEF.md`, `review-editorial.md`, `review-cold.md`, `AUTHOR-REPORT.md` ("## Repair r1"), `packets/MOVEMENT-007.md`, `BOOK_MAP.md` §10–12, `STATE_LEDGER.md` (entry state, the M5/M6 closes and the pre-appended M7 block), `protected-patterns.txt`, and the earlier-book lines the ch50 clause depends on (edition B2 ch59, B3 ch10/13/55, B4 ch02/13/42). No manuscript or repository file was modified; no git command was run.

---

## VERDICT: CLOSE WITH LINE FIXES

Scope: **three single-sentence fixes** (listed at the foot, each old string grep-verified to match once). None is a brief failure; two are listening nits introduced or reinforced by r1, one is a pre-existing seating slip that the new Cael beat now sits beside. No second repair. Every Priority 1–3 item is RESOLVED, every coordinator ruling is honoured, the tools reproduce the author's numbers, and the hidden hinge (mark four, seen by Cael and not by Havel) survives exactly where it was.

Housekeeping for the coordinator, not a manuscript matter: `state/movement-007/source-overlap.summary` still reads "10 protected" — it is the author's regenerated pre-repair run (09:46:42, before the 09:47:29 pattern correction). The live run on the current text is **0 unprotected / 9 protected**. Regenerate on close.

---

## (1) Brief items — RESOLVED / PARTIAL / NOT, with evidence (diff vs `pre-repair/`)

### Coordinator rulings

| Ruling | Result | Evidence |
|---|---|---|
| Rejoin Havel's line as one line (pattern-protected) | **RESOLVED** | ch49: `-*Two years.*` / `-*Two of us now.*` / `-*Nothing has ever come back with a name on it.*` → `+*Two years. Two of us now. Nothing has ever come back with a name on it.*`, then `+He looked at the line. It was not like the lines above it.` Exact-string count: 1. Overlap reports the run as protected. |
| Rejoin the close as one line (pattern-protected) | **RESOLVED** | ch50: `-*Four days to the final.*` / `-*Five to the twentieth.*` → `+*Four days to the final. Five to the twentieth.*`; the lead-in changed `three short lines` → `two short lines` (the page now has *Tomorrow, ordinary again.* and the countdown: two). Count: 1. |
| "Half-metre" stays | **RESOLVED** | ch45 l.5 unchanged: "the half-metre of air round his own body". |
| "Eleven months"; second return; second referral | **RESOLVED** (unchanged, confirmed) | ch49 l.31 "That had been eleven months ago."; l.25 "She had met the first two sentences before."; l.33 "sent back the same two sentences, word for word. Then they had added a third"; Havel l.113 "At Greyvane, when the first return came". |
| Havel's fourth entry at the second recess | **RESOLVED** | ch49 l.123–131: "The second recess came at the fourth bell… He dated the fourth and wrote it…". |

### Priority 1 — continuity line fixes

| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | ch45 red bundle: one semester, fourteen sittings, Cael fifteen | **RESOLVED** | `-Two years of demonstration sittings, sheet on sheet.` → `+Fourteen demonstration sittings from a single semester, sheet on sheet.`; `-Two years of a boy's sittings… from month to month… fourteen and then fifteen` → `+One semester of a boy's sittings, fourteen of them… from week to week… when the person producing them is fifteen and growing out of his boots`. Vastin's observation (numbers agreeing too closely; read twice, "noticed himself doing it") survives whole. The string bundle's "over two years" (l.121) and "two years of district filings" (l.155) refer to other officers' paper, not the red bundle: correct. |
| 2 | The inky-knuckled clerk: one seat, both chapters | **RESOLVED** | ch48 l.219 `-on the next chair along` → `+two chairs along from Cael`; l.259 `-The inky-knuckled clerk on the next chair was writing.` → `+The inky-knuckled clerk, two chairs along, was writing.`; ch49 l.267 `two places along` → `two chairs along`. Geometry now closes: row [young][Cael][cold][inky]; two clerks sent off with boxes → `the chairs on either side of Cael stood empty`; inky "had not put it on the empty chair beside his own… He had reached past that chair and across Cael's knees… to lay his folder on the seat beyond" = the young clerk's chair = "the empty chair at his side". Consistent in all three places. |
| 3 | Brom's boxes: nightly cadence sourced | **RESOLVED** (one ear nit, fix 1) | ch45 l.33 `+All season he had done them four a week, but on the night of his semifinal Rooke had put him on one a night until the final, and Karis had ruled a fresh page to match.` Reconciles M4's four-a-week (all nineteen ≈d159–160; round two from d172 per M6) with "one for every night between the semifinals and the final" and ch50's "the round-two exercise for the night". The next sentence now opens "Karis had ruled…" immediately after "Karis had ruled…" — see fix 1. |
| 4 | Havel's "a much younger man" | **RESOLVED** | ch46 l.35 `-when he had been a much younger man with a much worse coat` → `+two years ago, when he had worn a worse coat and been, he sometimes felt, a good deal younger than two years should account for`. His own wry exaggeration, with the C3 "two years" stated in the same sentence. |
| 5 | English weekday names (cold) | **RESOLVED** | ch49 l.27 `-on a Saturday after the fifth bell` → `+on the last day of a week, after the fifth bell`; `-on the Monday courier` → `+on the first courier of the next week`. Grep `monday…sunday` (whole-word, case-insensitive) across ch45–50: **0 hits**. The scheme words present: Fifth-day(s) ×2, Sixth-day ×2, Seventh-day ×1 — all correct for d177/d178/d179 (see §2). |
| 6a | ch47 "Day sixteen" vs "a month" | **RESOLVED** | l.195 `-Day sixteen.` → `+Day sixteen of the ledger; twenty-nine since the stair.` Checked against the ledger: working ledger day one = d163 (M5 table) → d178 = day sixteen; the reach "on the night of d149" (M5 ruling) → d178 − d149 = 29; "paying it for a month" (l.21) holds. (The M5 close's "ninth morning after the stair" = d159 counts from d150, a one-day ambiguity in an approximate figure; it does not touch this entry.) |
| 6b | ch47 the 31st repetition vs "the last one" | **RESOLVED** | l.171 `-At the thirty-first repetition of the left side, which was one more than the drill called for, Brom stopped.` → `+Before the thirtieth repetition of the left side, the last one the drill called for, Brom stopped.`; l.185 "drove the last one in" now is the thirtieth; "Thirty a side"; 54 of 60 unchanged. |
| 7a | ch48 "Seln" anchored at first naming | **RESOLVED** | l.5 `+the teaching assistant, Seln, was writing out somebody's timetable`; l.97 `+Seln, at the copying table, writes true lines about me`. |
| 7b | ch50 "he sat down at the window" after Brom "went up" | **RESOLVED** | l.147 `-when he sat down at the window` → `+when Cael sat down at the window`. |

### Priority 2 — ch49: the return read once; the lead re-anchored

| Item | Result | Evidence |
|---|---|---|
| Drop the second verbatim quotation in Ilsev's Greyvane memory | **RESOLVED** | l.27–29: the old `*No originating authority of record; designation predates file creation.* That had been the answer to her query…` is gone; the paragraph now runs "they had come to her on a sheet laid square on the corner of a long table, in answer to the plainest question her form allowed: who had entered this mark, and on whose authority?" "She had met the first two sentences before." (l.25) carries it. The return's three sentences are set out **once** (l.17–19). The only re-quotation left is the single third sentence inside the three-witnesses beat (l.55 *No action available at this clearance.*), which both reviews asked to keep. |
| Cut Havel's verbatim fourth entry to a one-line summary; keep "Two carriers now…", the broken rule and the protected line, "written by a man", the three cross-referenced sheets, the courier section whole (incl. filing the return in its place) | **RESOLVED** | The 60-word italic entry (`*Halcenvane, the delegation. The senior seat's referral…*`) is removed; now l.131 "It was one line long: the Greyvane referral returned from the chain above, eleven months on, and refiled a level higher inside the recess, both sheets logged and cross-referenced in his own hand." Kept: l.133 "Two carriers now, Havel thought."; l.135 the rule and "Once would not ruin it."; l.137 the protected line; l.139 "written by a man"; l.109 "Three sheets, each pointing at the other two"; l.99–105 the courier section whole, ending "She would come to it in her own order, at the end of everything else. He thought she would want to meet it that way." The three-entry re-read is compressed to one sentence (l.129), with all three earlier entries still named. |
| ONE short Cael beat between the windows (a few hundred words at most) | **RESOLVED** | New section l.89–95, **254 words**, opening on the POV name: "Cael spent that first recess on his hard chair…". |
| The beat leaks nothing to Cael | **RESOLVED** | What he sees: Ilsev "read something from a file", "took out a form and wrote on it for… about eleven minutes", "laid it in the records officer's tray", "drank a cup of tea in four swallows", "whatever she had read had not changed her face at all". What he concludes: "He did not know what it was. It was not his to know… the most ordinary thing in the world… did not even write it on the back of his floor sheet." No word of the return, the designation, the referral, or the level. His "about eleven minutes" by breath-count matches her eleven by the clock without his knowing why it matters: a reader-only rhyme, not a leak. Later (l.185, l.251) he still files mark four as "Havel logging the tray" / "the house's paperwork": wrong in exactly the way the cold read prized. |
| Mark four intact and unseen by Havel | **RESOLVED** | Untouched: l.119 "Up the table, past the counsel, the Archmarshal's pen rose from his folder while Havel was entering the referral. It made one short mark, and was laid down crosswise again. Havel did not see it. He was looking at his ledger, which was his work."; l.185 "A fourth had come at the end of the first recess, when Havel bent over his ledger to log the tray… Cael had seen it from the wall. Havel had not." The Cael beat ends ("He set the stake again, and watched the room fill up.") before Havel collects the tray, so the live mark is not narrated twice. |
| Net −300 to −500 words | **RESOLVED** | ch49 7,163 → 6,829 wc (**−334**). |
| Lead re-anchored (editorial's version of P2) | **RESOLVED** | Cael is off the page for ≈1,946 words (Ilsev) then back for 254, then off for ≈1,274 (Havel). The old 3,800-word absence is now two shorter ones. By section count: Cael ≈3,601 (254 + 1,335 + 744 + 1,268), Ilsev ≈1,946, Havel ≈1,274: Cael now outweighs both windows together (matches the author's ≈3,600 / ≈1,940 / ≈1,270). |

### Priority 3 — anchor the word, once

| Item | Result | Evidence |
|---|---|---|
| ONE factual clause that *Shattered* is the word on Cael's own registry sheet; no theory; no claim about what he is; no "unbound" → nature link | **RESOLVED** | ch50 l.63 `+*Shattered* was the word in brackets on Cael's own registry sheet, beside his number, in the Denvash station's hand. He waited until he was sure she had finished.` One sentence, in Cael's head, flat. Canon-true: B4 ch02 "He wrote the designation in brackets, *[SHATTERED]*, as the station had written it" (after name, number, *Denvash*, date); B2 ch59 "a word in brackets that some clerk in Denvash wrote down"; B3 ch10 "handed down a word in brackets"; B4 ch42 "A clerk behind a long counter there had written a word about him on a form". The STATE_LEDGER M7 ruling (l.727) uses this exact wording. "unbound" grep across ch45–50: **1 hit**, l.61, lower-case, Karis's speech, and she closes it herself in l.67 ("I'm not saying anything about them at all"). Kept exactly: "It's a coincidence with good posture."; Karis's refusal; *Why retire a working method?* alone on the page; Cael's part 3. |

### Length

29,862 prose (29,929 wc), inside 29,000–31,000. Per chapter (wc): 45 5,708 · 46 4,114 · 47 4,549 · 48 5,587 · 49 6,829 · 50 3,142.

---

## (2) Continuity

**Calendar (13th–15th of Reaping; d177–d179; anchor d167 = Second-day).** ch45 "On the thirteenth of Reaping"; ch46 "At the sixth bell, on a Fifth-day?" (d177 = Fifth-day: correct); ch45 l.283 "the fourteenth, hall three, the fourth bell. It was his own ordinary Sixth-day hour" and ch47 "Sixth-day, fourth bell, hall three" (d178 = Sixth-day: correct); ch48 "the second bell of the fifteenth of Reaping". Countdowns reconcile: "Six days" (13th) → "In five days" (ch48, 14th) → "Four days to the final. Five to the twentieth." (15th); Lira's hip "ten days old by the time she fights on it" (injured the 9th). The compilation crossed "two evenings ago" with the stamp "of the twelfth", seen on the 14th: correct. Nothing moved in r1; the author's day table stands.

**Only two public capabilities + the thin Ember exhibit.** ch45 l.125: "A framework of movement that the record called Wind-adjacent… A read along the skin, logged trial by trial. And at the very back, late and thin, one sheet about a spark." Nothing else in any filing or on any record. ch47's wing sheet records "a Copper-baseline redirect drill, done at Copper baseline". Shadow appears only in Cael's private ledger. The "compound gaze" and the coarse Iron read in ch46 are private and unseen.

**Vastin:** no age ("at twenty-three", "four years", "most of his life", the stiff left hand); no detection of Seln's nulls ("a thing about the chair"; the case returned with the stamp and nothing else; the taxonomy refuses to infer); five marks, all on procedure; "He had filed no question." (count 1).

**Ilsev and Havel:** no answer reached; "Two carriers now… neither of them cleared to be given the answer"; her gloss *available: at this clearance* stops at the grammar. Havel's windows touch neither the Book 1 market stranger nor the B2 Iron Skin watcher. (His first entry still reads "a market and a marker": Ardenmere's square, as the editorial judged; the one-word echo is outside the brief and unchanged by r1. No action.)

**Reserved words.** "decision point": 0. "Gwen": 0. "four years": two hits, both legitimate (Vastin's maxim; Ilsev's four-volume log). "sixteen" for Cael: ch49 Withrow "a boy of sixteen" — correct after the eleventh of Sowing. No month order, no Sowing→Reaping count. No new proper names introduced by r1 (Seln and Denvash are existing).

**Protected lines (BOOK_MAP §10, exact-string search, each once unless noted):** *Observer product is testimony about the observer.* · *An evaluation that begins from its conclusion is a report about the evaluator.* · the three margins · "Coss enforced." / "Havel complied." / "Seln operates." / "This one evaluates." / "The Compact finally sent someone who takes notes the way I take notes." · the return's *Determination…* sentence · the grounds sentence · Ilsev's finding (own paragraph; Cael re-quotes its last sentence on the steps, as a callback) · "He is calibrating the instrument. I am the reading." · *Why retire a working method?* (twice, by design) · the C3 line, now one line · the close, now one line. Packet lines exact: "Read's off." / "On purpose." / "Then it's the right kind of off."; "It's good."; "An omission—" / "Is a possibility," (comma-attributed, the same convention the editorial accepted for "Irregular,"); "Then I have what I need."; "I have. I do. I will."; "This one started with the ruler."; *existing assay enrollments*; "Nobody drafts a conversion route for a dead letter."

**Seating and the new beat.** ch48 fixes Havel at the foot nearest Cael, Ilsev immediately above him, the tray at Havel's elbow. The new Cael beat has Ilsev "at the near end of their side" (correct: the foot is Cael's end) and "only two people stayed in their places" — Havel's own window has him away and then "went down the table and collected the tray", so he had left after laying the file; consistent. Ilsev's own window, though, still has her carry the form "down the length of the table" to a tray one place from her chair — a pre-existing slip the new beat now stands beside (fix 2).

**Ledger arithmetic:** confirmed above (P1.6a). **Brom's nineteen:** reconciled (P1.3). **Lira:** off the stick on the 13th; hip ten days old at the final. **Watchers:** two and two, on the bell, unchanged.

---

## (3) Formula — reproduced

`python3 editions/monroe-1.3/tools/formula_metrics.py` on ch45–50 (this seat's run):

```
words_total 29862 · prose 29862 · sentences 2152
sentence_mean 13.88 (target 14.6) · median 10.0 · sd 11.01
share_le5_words 0.252 · share_ge40_words 0.035
paragraph_median 28.5 · paragraph_mean 39.6
scene_breaks_marked 26 · per_10k 8.71 · words_per_scene 933.2 (target 950)
flesch_reading_ease 86.0 · flesch_kincaid_grade 4.71
```

Identical to the author's "After r1" column. In range: mean 13.88 (13–15.5); ≥40-word 3.5% (2.5–4.5); words/scene 933 (850–1,050); ≤5-word 25.2%; paragraph median 28.5 (≤~30); FK 4.71 (3.5–6); FRE high as in every movement, reported not chased.

- `ed.sh overlap book-04-copper-crown 7`: **0 unprotected shared runs of ≥8 words; 9 protected** (the corrected pattern now catches the rejoined Havel line; the two cut re-quotations of the return account for the drop from the pre-repair 10).
- `ed.sh gates book-04-copper-crown 7`: reader_standard=0, metadata=0, modern=0 on all six chapters.
- `sweep_probe.sh book-04-copper-crown 7 7`: **skeleton 1%, close 11%** on 1,332 sentences (ch45 0/10 · 46 0/7 · 47 0/8 · 48 1/14 · 49 3/15 · 50 0/12). Within ≤5% / ≤13%.
- Folder artifact note: `source-overlap.summary` reads "10 protected" and predates the pattern fix; regenerate on close.

---

## (4) Reader clarity

- **Speakers.** Every window opens on its POV name in its first sentence, including the new one ("Cael spent that first recess…") and the re-cut second-recess opener ("At the second recess, again, Cael did not leave his chair."). The sitting attributes by role throughout. The ch50 window-sitter is now "Cael" by name.
- **Referents.** Seln is anchored twice. The clerk is in one seat. "Shattered" is tied to Cael's own sheet in one plain sentence, so Karis's "in a box you drew round it when you were younger" and Cael's part 2 ("The clause I'm enrolled on and the article that changed the old word sit four apart") now land at full weight for a cold reader, and the empty page under her line reads as what it is.
- **The thirteen-year-old lens.** The double window in ch49 is broken by a 254-word return to Cael that is itself a small scene (he counts her minutes by his breaths, decides it is not his to know, sets the stake). The Havel section is shorter and no longer re-narrates what the reader has just watched from inside Ilsev. Ch49 still asks the most of this reader, but the chapter is 334 words lighter where it was heaviest.
- **Reader Standard.** Gates 0/0/0; nothing in r1 adds profanity, violence, romance or cruelty. The movement's moral clarity is unchanged.
- **Knowledge asymmetry (the movement's engine).** Still intact at the level of the noun: the name "Vastin" never appears in a Cael section; Cael never learns what Ilsev filed; the reader alone holds all four pieces.

---

## (5) Listening proof — every chapter, every changed region

Scripted pass on all six files: no odd double-quote counts per paragraph; no unbalanced asterisks; every `---` has a blank line before and after (26 breaks); no abbreviations; the only digits are the numbered-list markers in Cael's two logs (*1.* … *5.*; *1.* … *4.*) and the document header "Priority Level 4" in the return (pre-existing; reads "Level four"). Then by ear, region by region:

- **ch45.** "Fourteen demonstration sittings from a single semester, sheet on sheet." and "One semester of a boy's sittings, fourteen of them, signed in turn…" read cleanly. The boxes sentence lands, but the next sentence opens "Karis had ruled…" straight after "…and Karis had ruled a fresh page to match." — a doubled subject in the ear (fix 1). Vastin's scene-break into the counsel's knock, the three-margin lines in their own paragraphs: clean.
- **ch46.** "two years ago, when he had worn a worse coat and been, he sometimes felt, a good deal younger than two years should account for" — a long clause, but it is Havel's sideways voice and parses on one hearing. Bout calls attributed ("said the table"). Clean.
- **ch47.** "Before the thirtieth repetition of the left side, the last one the drill called for, Brom stopped." — clean. The ledger line "Day sixteen of the ledger; twenty-nine since the stair." reads as two clauses; no misvoicing. "Read's off." / "On purpose." / "Then it's the right kind of off." — each in its own paragraph with Brom and Cael named around them. Clean.
- **ch48.** "the teaching assistant, Seln, was writing" — clean. "two chairs along from Cael, the inky-knuckled clerk sat up very straight" and "The inky-knuckled clerk, two chairs along, was writing." — clean. The sitting: every turn by role. Clean.
- **ch49.** l.13 "He had had it since the eighth bell last night, then, and had let her come to it in its place." — "had had" is fine aloud. l.27 the Greyvane memory is now one long sentence with a colon question; it breathes. l.91 (new beat): "wrote on it for what Cael's count of his own breaths made about eleven minutes" — the one genuine tangle in the new text; a listener has to back up over "for what… made" (fix 3). l.129 the three-entry recap is a semicolon list with italic fragments; it reads as a list and does not break. l.131 the one-line summary: clean. l.137–139 the rejoined line and "He looked at the line." — clean. l.145 "At the second recess, again, Cael did not leave his chair." — the "again" is a good ear-callback to the new beat. l.267 the folder geometry: "He had not put it on the empty chair beside his own, which was nearer his hand. He had reached past that chair and across Cael's knees…" — clean, and the picture now adds up. Homographs: "read" (past) is always disambiguated by tense context. No ambiguous "she" between Ilsev, Withrow and Karis in the afternoon (each named at the turn).
- **ch50.** l.63 "*Shattered* was the word in brackets on Cael's own registry sheet, beside his number, in the Denvash station's hand." — clean, flat, one hearing. l.147 "when Cael sat down at the window" — resolved. l.167 "two short lines" — matches the page. l.171 the close as one line — clean.

Broken joins: none found. Scene-break formatting: none found.

---

## Line fixes

1. `manuscript/chapter-45.md`
   old: `and Karis had ruled a fresh page to match. Karis had ruled the boxes out to the eighteenth, the night before the final, and she had told nobody but Cael why she stopped there.`
   new: `and Karis had ruled a fresh page to match. The boxes ran out to the eighteenth, the night before the final, and she had told nobody but Cael why she stopped there.`

2. `manuscript/chapter-49.md`
   old: `Then she rose, carried it down the length of the table and laid it in the shallow wooden tray at the foot, where the records officer would find it, and came back to her chair.`
   new: `Then she rose, carried it down to the foot of the table and laid it in the shallow wooden tray, where the records officer would find it, and came back to her chair.`

3. `manuscript/chapter-49.md`
   old: `and then took out a form and wrote on it for what Cael's count of his own breaths made about eleven minutes, and carried it down the table,`
   new: `and then took out a form and wrote on it for about eleven minutes, by Cael's count of his own breaths, and carried it down the table,`

Each old string verified with `grep -c -F` to match exactly once in its file. None touches a protected line, a pattern-protected line, the return, the grounds, the finding, the five-mark list, or the drift/folder/foot passage.
