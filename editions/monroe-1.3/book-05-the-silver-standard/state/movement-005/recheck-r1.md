# Recheck r1 — Book 5, Movement 5 "The Concourse" (chapters 27–32)

Reviewer: **Claude Fable, review seat** (fresh context), standing in for the Sol/Codex seat, which is out of quota. The recheck prompt says "Sol, via codex"; read that as Claude Fable here. The author of the draft and of repair r1 is Claude Opus 5.5; I am not the author. Date: 2026-10-05. No manuscript or repository file was modified except this report. No git commands were run.

Read in full: `manuscript/chapter-27.md` … `chapter-32.md` (current text, 32,128 prose words); `REPAIR-BRIEF.md`; `review-editorial.md`; `review-cold.md`; `AUTHOR-REPORT.md` ("## Repair r1"); `pre-repair/chapter-27.md` … `chapter-32.md` (as `diff -U0`); `BOOK_MAP.md` (§2, §8, §10, §12 and the Vastin/Havel rows); `STATE_LEDGER.md` ("AFTER MOVEMENT 5" block with the coordinator rulings, and the year-count rulings); `packets/MOVEMENT-005.md`; `tools/RECHECK-TEMPLATE.md`.

---

## VERDICT: CLOSE WITH LINE FIXES

**Scope:** three one-sentence fixes and one optional phrase, all in ch31–32, none touching a protected line, a count, a figure or a ruling. Two are listening-proof items that the repair's own splices introduced (a "He" that now lands on Brom; a "defend it" that now lands on Havel's notebook). One is the Ephram fifth-exchange sequence, which narrates his third point before the coast Blade's one, against the rule the movement teaches. The optional one tightens the ch31 block geometry. Nothing warrants a second repair: every brief item is RESOLVED on the page, overlap is 0 unprotected, gates are 0, and the formula reproduces to the digit.

For the coordinator at close: the "Author's end-state" half of the STATE_LEDGER "AFTER MOVEMENT 5" block still carries four pre-repair facts (hill house *below*; the Compact row with "two clerks"; Havel's "right thumb-web aches"; Havel "writes nothing" with the seating order in his folder). The rulings block above it already overrides them; the CLOSED note should say so, or strike them.

---

## (1) Brief items — RESOLVED / PARTIAL / NOT, with evidence (diff -U0 vs `pre-repair/`)

### Priority 1 — Brom's fifth exchange: **RESOLVED**
ch32 l.93: the sentence "Then Brom took another, plainly, through the middle, a breath before the bell." is gone (diff `@@ -93 +93 @@`). What remains is the door point ("That was a point."), the hill fighter's sweep ("took one back with a fine low sweep"), and the final fist over the caught wrist (l.95). That is 2–1. l.97 still reads "Two to one. Nine to seven." and l.103 "Brom twenty-four, the hill fighter twenty-three." Totals and figures unchanged. I re-ran the bout: 1–2 · 2–1 · 1–3 · 3–0 · 2–1 = 9–7; after four at 7–6 the trailer could reach 9, so a fifth is required; not level after five, so no figures-decide. The page's own calls ("one to two"; "Three each, on the bout"; "Six to four… with two exchanges left"; "Seven to six") all agree.

### Priority 2 — Seat twelve, three passes: **RESOLVED**
- **Havel** (ch32 l.311–321): 260 words by `wc -w` on the five paragraphs (the author's 249 counts differently; both are "about 250"). It is no longer the seating-order scene. He "signed the attendance sheet"; the one records-officer detail is the sheet "he had ruled himself on the coach coming north, a page for each day of the sitting, twelve lines to a page", which "a steward had brought him… back from the west tower" with line twelve "filled in before he saw it… in a hand he did not know, on every day of the three weeks… *held*", and "The ink was the same from the first page to the last." He names no one. The only inference is about the document, not the person ("written on every page at one sitting, with one pen"); on the grade he says the seating order "told him whose rank was meant and nothing whatever about whose coming." He does not open the notebook ("Ninety pages, four written on. / He did not take it out."). His thumb-ache is cut, so Vastin's left hand (ch29 l.239, unchanged) is the only aching hand in the movement, as the brief asked. "Blank pages are the ones that get written last." still closes the movement (current l.353; pre-repair l.363).
- **Vastin** (ch29): no diff. The aching-hand plant stands at l.239.
- **Cael** (ch32 l.341–349): the plate-by-plate inference ("more senior than every name on every plate, or nobody at all") is cut, and so is the Log's "somebody is sure there will be somebody". What is left is what the glass shows: "a clean pale square… the screw holes… empty… Somebody had sat in it once, at some other sitting, under some other plate." and "A plate, a steward and a brushed seat were all a chair could tell anybody from a public gallery, and this one had told him two of the three." The Log line (l.349) lists the pale square, two screw holes, the brushed seat and the steward. "No name."

### Priority 3 — counts, clocks and clarity: **all RESOLVED**
- **ch30 clock:** l.113 is now "They sat over the program through the middle of the day… with the shutters open on the street." The day now runs: second bell orientation → rules at the side door → the program at the long table through midday → "the end of the afternoon" at the rail (l.129) → "Before the light went" in the ring (l.183) → "The draw was made at dusk that same day" (l.241). No rewind. (The ring scene's "the dark had come right down the tiers" sits tight against the dusk draw; inside a stone bowl that reads as early, and neither reviewer flagged it. Not a repair.)
- **ch32 Compact row:** l.335 now "Ilsev… Havel… The other four observation seats had changed on the rotation every day, badged men and women he did not know. Past them sat two district officers, a liaison man, and two officials of the host city who came and went." Six + two + one + two = eleven plated, twelve held, matching Vastin's plan at ch29 l.229. No clerks. The "changed on the rotation" clause is present.
- **ch28 guesting house:** l.255 "a hill house on the floor above and a southern house below"; l.269–271 the hill house's clerk stops at Halcenvane's door and "went on up the stair" — consistent. Cael's room is "the top of Halcenvane's floor" at both l.241 and l.273. The brief's chosen phrase.
- **ch32 "quarry town's rule":** l.287. Correct (ch17 of this edition).
- **ch27 "twelve more of her":** l.39. Fourteen less Halcenvane and the coast house.
- **ch32 typo + paragraph break:** l.289 "There were colour-sellers with the fourteen houses' ribbons on long poles." and a new paragraph at l.291 "And all through it…".
- **ch31 one banner:** l.185 "They had brought it down from the champion's gate at dawn, and it would go back up over the gate when the opening was done. No house walked behind it." One cloth; Rooke's ch28 "hangs there… until somebody earns the right to take it down" is reconciled by "would go back up".
- **ch30 Rooke's map table:** l.141 "I'll tell you about him once, here, because you're the one of us most likely to end up across a table from him."
- **"Eight thousand" thinned:** now five (ch28 l.37, l.153; ch31 l.31, l.225; ch32 l.187). Was seven. The two cut were the eve ("with not a place left on any bench") and the tunnel ("The whole bowl was humming it under its breath").
- **Optional reaction line:** taken. ch31 l.237–241: Lira's held breath, "She just counted us," she said, very low. "Didn't she." and Brom shifting his weight once. The house now feels the count.
- **Found while reading (author):** ch32 l.291 "There was the favourites' house and its Gold." Correct: Auremont is not the banner-holder (STATE_LEDGER M3 ruling, l.470).
- **Length:** 32,128, inside 30,500–33,000.

---

## (2) Continuity

- **Calendar.** No season name, no month name or order, no metres, no English weekday (grep, word-bounded, case-insensitive: zero hits; the only matches are "colour-guard"). "Fourth-day" (ch29) is the Halcenvane scheme. "the first day of the new month" (ch31 l.133) unnamed. Road days (third, fourth, fifth, sixth, ninth, twelfth, fourteenth, seventeenth, eighteenth), "the fifth morning", "a week before the opening", "the eve", "the third evening", "the next morning… at first light" (T4), "the fourth afternoon/evening" all agree with the ledger's day table. The trial rules post on T4 ("A note for after Norhold", ch32 l.263).
- **Counts.** Fourteen houses; Halcenvane eleventh; forty Auremont riders; twelve seats; six sheets (Karis's 1/2/4/1 tally holds); Hesk's clock an hour fast; the ring "fifty-odd feet, a little longer one way than the other" (the editorial's deferred note on the short side stands, unchanged by r1, for the owner).
- **Year counts not incremented.** Withrow "eighteen years" (ch28 l.29, ch32 l.291); Vastin "forty years" (ch29 l.223, l.247; OWNER #17, no age stated); Umber's thumbnail scratch "a private habit forty years old" (ch31 l.43) and his late master in one line (l.97); the steward's grandmother "Forty years" (ch30 l.219); "three hundred years" for the floor and the mark (C4-allowed). No "four years", no "decades", no system-age figure.
- **Knowledge boundaries.** Cael has the eight-thousand figure from "Rooke's briefing" (ch28 l.153). Daeva's "nineteen" is sheet knowledge (unchanged, passed in review). Havel knows the grade from the seating order and nothing of whose coming; the west-tower sheaf tells him only "held". Vastin infers nothing of makers or Seln. Cael cannot name the chair's occupant and says so ("He could not find the name."). Nobody outside the circle touches the mechanism; Seln knows nothing of it; the Tide anomaly is untouched.
- **Protected lines (verbatim, first where mapped).** §10 item 11, Umber's attestation, ch31 l.275: identical to BOOK_MAP l.339, lowercase italic, one line. Item 40 both parts: ch29 l.141 and ch30 l.355, verbatim. Items 1 and 12 at ch32 l.241, unchanged by r1 (no diff), italic and unsplit. Umber "can't want anything from you" at ch30 l.153. `ed.sh overlap` reports 10 protected runs, all allowed; the five packet lines sit in `protected-patterns.txt`.
- **Reserved truths.** Seat twelve's occupant withheld; Daeva's face withheld; the hidden cost carried three times, never explained (ch27 l.227 unchanged); Karis's "door somebody built on purpose" means the drafters only, the slip stays unopened.
- **#38 ratings.** Lira 26 / Ash 24; Brom 24 / hill 23. All in 22–27. "eleven minutes later" ×3.
- **#39 continental format.** Stated once (ch30 l.71), with the accepted detail: exchange closes at the bell or at three points; the bout stops when the trailer cannot draw level; level after five → figures. Every bout on the page re-checked under it: Lira 0–2 · 2–1 · 3–1 · 3–0 = 8–4, over in four (trailer at 4 could reach 7); Karis 3–0 · 2–1 · 3–0 = 8–1, stopped after three (trailer could reach 7), not after two (5–1, trailer could reach 10); Brom I 9–0 after three (not after two: 6–0, trailer could reach 9); Brom II above; Ephram 2–1 · 1–1 · 0–2 · 3–0 · 3–1 = 9–5, fifth required (6–4, trailer could reach 7). Lira's E3 and Brom's E3 both narrate the opponent's single point before the third that closes the exchange — correct. **Ephram's E5 does not** (fix 3 below). Exhibitions keep the old rules (Rooke, ch30 l.97). No bout for third (Gault, l.101–103).
- **#40 public capabilities.** Wind at four of five on the waystation clay and the read; Ember unused; Pressure unasked ("The right shoulder had not been asked for anything all day"); Compression and Shadow on no floor; the record of five unchanged. "the read and the compound gaze together" (ch31 l.201) is BOOK_MAP vocabulary (l.252, l.268), not a new capability.
- **Staging (rulings 3).** Banner last, colour-guard alone, holder unnamed; Auremont's file reversed so Daeva leads (ch31 l.181); draw at dusk on orientation day; trial rules on T4. All on the page.
- **New canon (ruling 5).** Umber about forty years at the seals, his master in one line; "the Halcenvane wall" as a broadside nickname signed with a printer's mark; Karis not saying Ivenne's name (ch30 l.321). All present. r1 adds, in the coordinator's ledger block already: the attendance sheet via the west tower; the banner down at dawn and back after; the north-side line; Lira's "She just counted us."
- **No new names.** The diff introduces none; every new role is by role.
- **Block positions (ch31 l.199).** All houses along the north side facing the dais (south); Auremont "at the far end of the line, where the north side curved toward the east tower"; "Halcenvane's stood at the other end"; a hundred yards between; Cael "at the edge of the floor" (l.265); Daeva's look "straight down the hundred yards of the line to the eleventh block" (l.235). Coherent for a reader. One looseness for exactness only: Halcenvane is the eleventh of fourteen in file order, and "the eleventh block" names it so; if the blocks stand in file order, the eleventh is not "the other end" from the fourteenth. No reader will compute it; the optional fix 4 removes the claim without touching the hundred yards or the ruling.
- **One hair, no fix:** the four rotating observation seats sit under chairs that each have "a brass plate… with a name cut into it" (ch32 l.337, unchanged). The brief's own clause produced this; a reader may assume the plates travel with the rotation. Below the fix line.
- **Seam with ch26 and later books.** Unchanged by r1; the editorial's seam checks (snowdrops, "at the orientation, by lamplight", the trial rules "not before the orientation", Rooke's "fifth place… until a clerk at Norhold") still hold. M7's "Somebody announced it for him" sits comfortably under Havel's pre-filled sheaf.

---

## (3) Formula — reproduced

`python3 editions/monroe-1.3/tools/formula_metrics.py` on the six chapters (my run, this session):

| Measure | Observed | Author's r1 report |
|---|---|---|
| words_prose | 32,128 | 32,128 |
| sentences | 2,303 | — |
| sentence_mean / median | 13.95 / 10 | 13.95 |
| share ≤5 / ≥40 words | 0.257 / 0.030 | 25.7% / 3.0% |
| paragraph median | 28 | 28 |
| scene breaks marked / words per scene | 29 / 917.9 | 917.9 |
| FRE / FK | 87.6 / 4.5 | 87.6 / 4.50 |

`ed.sh overlap book-05-the-silver-standard 5`: **0 unprotected** shared runs ≥8 words; 10 protected (allowed).
`ed.sh gates book-05-the-silver-standard 5`: reader_standard 0, metadata 0, modern 0 on all six chapters (ch27 5,095 · ch28 4,760 · ch29 4,899 · ch30 4,654 · ch31 6,226 · ch32 6,572).
`sweep_probe.sh book-05-the-silver-standard 5 5`: TOTAL 1,417 sentences, skeleton **1%**, close **5%** (per chapter: 0/4, 2/4, 0/3, 1/4, 0/4, 1/8). Within ≤5% / ≤13%.

All four match the author's table exactly.

---

## (4) Reader clarity

- **Speaker attribution.** Every line added by r1 is attributed or unambiguous by turn: "She just counted us," she said / Nobody in the block answered her. Brom shifted… The three-plus-speaker scenes (the program at the long table; Rooke's council; the rail after Lira's bout) are unchanged and clean. Two-speaker alternations without tags (ch27 l.55–59 Karis/Brom; ch32 l.283 "Yours opens.") resolve by turn.
- **Referents.** Two new splice points leave a pronoun pointing the wrong way by ear (fixes 1 and 2): ch31 l.243 "He put it in the observation notebook" now follows a paragraph whose subject is Brom; ch32 l.325 "Cael saw a steward defend it" now follows "He did not take it out" (the notebook). Both resolve within a sentence or two on the page; neither should be left for a narrator. Everything else: "It came down the row" (the sheet), "Except one", "They had brought it down" (the colour-guard) are clear.
- **The 13-year-old lens.** The Havel page now reads as a different scene from Vastin's (a sheet, a hand, the same ink) rather than the same scene twice; the row counts to eleven on one pass; the Log lists four things a glass can see and stops. Brom's fifth exchange counts right by ear. The ch30 day runs forward. Lira's "She just counted us." gives the young reader the dread the notebook alone could not. Nothing added is outside the Reader Standard.
- **Reader Standard.** Clean language throughout (gates 0); the new lines carry no violence, no gore, nothing unkind; the handshakes and the gallery standing for the hill fighter remain.
- **Not repaired, deferred to the owner (unchanged by r1, per the brief):** "The tournament was still nine days off" (ch27 l.293); "fifty-odd feet" for 52×48 (ch30 l.191); Vastin's "a week before the opening" on a Fourth-day; three bout-losers "looking at his hands". None is a clarity fault a reader would stop on.

---

## (5) Listening proof — every chapter

Mechanical probes over all six files: straight double quotes balance on every paragraph (0 odd lines); asterisks balance on every paragraph (0 odd lines; the lowercase italic attestation and the three italic board lines are whole); every `---` has a blank line before and after (0 findings); no curly/straight quote mixing (0 curly); no digits outside the three board lines (`IRON 9`, `COPPER 1`, `IRON 3` — a narrator says "Iron nine", and they are planned text, unchanged); no abbreviations (the only hits are "No." as a spoken word). "theater" (ch32 l.297) is the edition's spelling (book 4 uses it six times; the packet quotes the line so) — not a fix.

- **ch27.** Clean. "Early," in pencil; the Log's quoted "Early," inside italics closes. "Twelve more of her" reads cleanly aloud.
- **ch28.** Clean. "the top of Halcenvane's floor in a guesting-house" (l.241) says "Halcenvane's floor" twelve lines before the reader is told Halcenvane has a floor (l.253); it is intelligible and is the brief's phrase. "a hill house on the floor above and a southern house below" — one breath, no collision.
- **ch29.** Clean. No diff. "pre-*sold*" voices as stress on "sold".
- **ch30.** Clean. "through the middle of the day… with the shutters open on the street" voices well; "I'll tell you about him once, here," has the comma a narrator needs.
- **ch31.** One join to fix (fix 1). Otherwise clean: "They had brought it down from the champion's gate at dawn" — "They" is the colour-guard in the sentence before; "where the north side curved toward the east tower" is one image; "straight down the hundred yards of the line to the eleventh block" voices in one run. Lira's "Didn't she." as a statement with a full stop is right by ear.
- **ch32.** One join to fix (fix 2); one sequence to fix (fix 3). Otherwise clean: the city paragraph now breaks before "And all through it"; "There were colour-sellers" reads; "the quarry town's rule"; "the favourites' house" voices as "the favourites house", unambiguous. Havel's "nothing whatever about whose coming" is heard as "who's coming", which is the sense. "Except one." lands. "Nothing had happened yet." then the rule, then "Cael saw a steward defend…" — fine once "it" is named.
- **Homographs / ear collisions.** "read" (past and present) is the book's habit and is set by context everywhere I checked; "par from a pothole" is deliberate; "the wall" / "the door" pair is Brom's and clear.
- **Broken joins.** Only the two above. The ch32 l.289/291 break, the ch30 l.113 re-timing, the ch31 l.185 banner clause and the l.199 geometry all join cleanly to what follows.

---

## Line fixes (each old string verified with grep to match exactly once; each new string verified absent)

1. `manuscript/chapter-31.md`
   old: `He put it in the observation notebook that evening, and then into the Log, the same words in both.`
   new: `Cael put it in the observation notebook that evening, and then into the Log, the same words in both.`
   (The paragraph before is now Brom's. By ear "He" lands on Brom.)

2. `manuscript/chapter-32.md`
   old: `Cael saw a steward defend it that same evening.`
   new: `Cael saw a steward defend seat twelve that same evening.`
   (The sentence before the break is "He did not take it out." — the notebook. "it" must not be the notebook across a scene break.)

3. `manuscript/chapter-32.md`
   old: `Ephram took three more. The coast Blade took one, a fine touch high on the shoulder that Ephram did not mind in the least.`
   new: `He took one, a fine touch high on the shoulder that Ephram did not mind in the least. Ephram took three more.`
   (Under the stated rule the exchange closes at Ephram's third point; the coast Blade's one must come before it, as Lira's E3 and Brom's E3 already narrate. "He" is the coast Blade, subject of the sentence before. Total 9–5 unchanged.)

4. *(optional, exactness only; the coordinator may skip it)* `manuscript/chapter-31.md`
   old: `Halcenvane's stood at the other end.`
   new: `Halcenvane's stood well down the line from it.`
   (Halcenvane is the eleventh of fourteen and "the eleventh block"; "the other end" over-states its place in a line of fourteen. The hundred yards and the ruling are untouched.)
