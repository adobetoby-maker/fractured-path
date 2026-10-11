> Built by TAC (reconciliation-apply seat, claude-sonnet) — 2026-10-11

# Book 7 plan — Book 6 reconciliation APPLIED

Companion to `B6-RECONCILIATION-AUDIT.md`, `B6-RECONCILIATION-F-RERUN.md` (Sol) and `B6-RECONCILIATION-COORDINATOR-OVERRIDES.md`. The coordinator overrides O1–O6 governed wherever they differ from the list. Every change in the plan files is marked inline `[B6-reconciled 2026-10-11: <audit item>]`. Protected lines changed under item 8 or O4 carry `[B6-reconciled 2026-10-11: OWNER-pending #48]` after the line. Owner items carry `[OWNER-pending #49]` (OI-1) or `[OWNER-pending #50]` (OI-2) after the line, with their words untouched.

Files edited: `BOOK_MAP.md`; `STATE_LEDGER.md`; `packets/MOVEMENT-001.md` … `MOVEMENT-008.md`; this file (new). The ten plan files were copied before any edit to `state/pre-B6-reconciliation/` (packets in its `packets/` subfolder); that folder is the diff baseline. No manuscript, no Book 6 file, no `OWNER-DECISIONS.md`, nothing under `books/` was touched. No git command of any kind was run (the baseline is a plain `cp`; the comparison used plain `diff` and a read-only Python `difflib` pass).

Method: every change was made with the Edit tool by exact text match; no bulk regex was run over any plan file. Line numbers below are **current** line numbers (after this pass). `BOOK_MAP.md` kept its line count (no line shift); `STATE_LEDGER.md` and the packets grew by the inserted lines. `BM` = `BOOK_MAP.md`, `SL` = `STATE_LEDGER.md`, `M1` … `M8` = `packets/MOVEMENT-00N.md`.

Status words: **applied** (text changed and marked); **annotated** (text unchanged, a note or mark added); **held** (not changed; reason given); **not applied (O4)** (a listed substitution the coordinator ruled out: generic `season` / `month` left as written).

## 1. Amendment items 1–16

### Item 1 — seam sources (A1, F2.6)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| BM:7 | `Seams read: Book 6 Ch23–24 (entry) and Book 8 Ch1 (exit).` became `Seams read: edition Book 6 chapters 48–60, with the AFTER MOVEMENT 8 and AFTER MOVEMENT 9 coordinator rulings/CLOSED notes governing the entry; Book 8 Ch1 governs the exit.` | applied | |
| BM:15 | Heading became `### Entry (edition Book 6 CLOSED prose — B6 ch48–60, especially ch55–60; Book 7 Ch1 opens on the same ground)` | applied | |
| BM:120 | Movement-table cell `B6 Ch23–24 (seam); B7 Ch1–2` became `edition B6 ch55–60 + CLOSED M8/M9 ledger seam; B7 Ch1–2` | applied | |

### Item 2 — BM §1 Entry bullets (D1–D5, N1–N4, C3), with O1 and O2

| File:line | Text changed | Status | Note |
|---|---|---|---|
| BM:17 Where/when | Replaced with the list text (second camp, first fire, Sixth-day, edition B6 ch58–60) | applied | |
| BM:18 Party: FIVE | Replaced (Ephram stayed, shoulder set, a month in a sling) | applied | "a month" is generic, kept per O4 |
| BM:19 Cael | Replaced. Satchel inventory: current log (about a third of its leaves left); full old volume, with Hesk's letters under its front board; observation notebook; two held no-return-address letters to Hesk and Vell | applied | **O1:** `the sealed Velmere letter` struck from the inventory. The front-board clause is O1's own wording for the satchel; it is used here and in SL:119 (the two full inventories), not in the compressed M1:19 |
| BM:20 The seal | Replaced (seeing carried west; Cael leaves it sealed past the Line; deployment since the Line is none) | applied | |
| BM:21 Companions | Replaced. Lira Iron R1 retained, Silver evaluation declined; Brom Iron finding unsigned; Karis Iron R3 retained and the lapsed list; Seln fifteen years' service, no notice or form, four keys, edition B6 ch37, recognition, twice-more count two | applied | **O1:** the Brom sentence added verbatim: `He left the last Velmere letter sealed and unopened on his table at Halcenvane, with the unsigned finding; he carries no family letter east (edition B6 ch56).` **O2:** `carries the locked case` became `brought the locked case east in his own satchel; it now rides under the canvas.` |
| BM:22 Who knows | Replaced (mechanism: five; cache/falsification: five plus Vastin; Ephram) | applied | |
| BM:23 Objects | Replaced (two-wheeled cart; brown gelding with one white foot; three numbered boxes and Seln's locked case under one canvas; pooled purse; two no-return-address letters; Daeva's reply; sheet and route-book records) | applied | **O2:** `three numbered boxes and Seln's locked case under one canvas` stays as the list writes it |
| BM:24 Compact posture | Replaced (`Status: active non-compliance, observation priority escalated.`; served within the hour; fifth line author unnamed; Vastin Archmarshal/certifying office; Gault evaluator of record) | applied | |

### Item 3 — STATE_LEDGER entry source, calendar, clock (A1, D4, N1, A2) and O6

| File:line | Text changed | Status | Note |
|---|---|---|---|
| SL:3 | Replaced with the list text (CLOSED edition Book 6 prose, chapters 48–60, coordinator rulings govern) | applied | |
| SL:11 | `Now:` bullet replaced (second camp, first fire, edition B6 ch59–60) | applied | |
| SL:54 | `Seasons:` bullet replaced by `Weather/road clock:` (warm-road days give way to hard-cold days; first snow on the 129th; ferry inbound about the 60th and 91st, outbound 102nd, last run 130th) | applied | The word `monthly` is gone with the season words |
| SL:53 | **O6:** sub-bullet added under the `eighteen until the 102nd` line: the birthday note | applied | Same sentence as the M6 note, including its bold lead |

### Item 4 — Cael body and capability inventory (A4–A5, B1–B3, C1, D1)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| SL:61 General row | Added the bruise and the cleared ten-count bill | applied | |
| SL:72 Iron row | Appended the air-or-body/ground sentence and the Storm-lane sentence | applied | |
| SL:75 Shadow row | Source `Seln (B4 Ch13)` to `Seln (edition B4 ch34)`; final use sentence replaced | applied | Bold lead `Book 7 uses it exactly twice:` kept as formatting |
| SL:76 Storm row | Replaced whole row | applied | |
| SL:77 Anchor row | Replaced whole row | applied | |
| SL:78 Blade row | Source to `Ephram (edition B6 ch54)`; appended `Notice exact at edition B6 ch54:145-152; first integration pull is the yard-gate lintel, named and quieted.` | applied | A full stop was added after the italic `earnest — non-hostile` so the appended sentence does not run on. See section 4, H8 |
| SL:62 Left forearm row | Pointer `(B6 Ch24)` to `(edition B6 ch58, ch60)` | applied (not in the list) | Retargeted by the list's own basis for the bruise (F2.3: ch58, ch60); the quoted phrase `the colour of a bad plum` is the source edition's wording and is not verbatim in the edition |
| SL:64 Attention row | `B6 Ch23` pointer | **held** | See section 4, H1: the one remaining item-16 hit |

### Item 5 — file line, companions, knowledge (B5, C2–C3, D2, N6)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| SL:87 | `The file reads *Active non-compliance. Observation priority escalated.*` became `The file reads *Status: active non-compliance, observation priority escalated.*` | applied | |
| SL:95 Karis | Standing replaced (Iron R3 retained; the lapsed list) | applied | |
| SL:96 Seln | Whole row replaced | applied | |
| SL:101 | New paragraph after the `Who knows the mechanism` line: cache/falsification history | applied | |
| SL:94 Brom | **O1:** sentence appended to the standing cell: `He left the last Velmere letter sealed and unopened on his table at Halcenvane, with the unsigned finding; he carries no family letter east (edition B6 ch56).` | applied | Not in the list; added by O1 |

### Item 6 — object and letter custody (D3, D5, N3–N4, N7), with O1

| File:line | Text changed | Status | Note |
|---|---|---|---|
| SL:119 | Hesk's satchel bullet replaced: current Power Log (about a third of its leaves left); full old volume, with Hesk's letters under its front board; observation notebook; two held no-return-address letters | applied | **O1:** no Velmere letter |
| SL:120 | Karis's boxes bullet replaced | applied | |
| SL:121 | New bullet: Lira's route book | applied | |
| SL:123 | `*Owner ruling pending.*` replaced by `OWNER #23 governs: sell cart and gelding in Lowmarch's first week; put the sale and remaining Book 6 purse into a sealed reserve the crew does not live on.` Pointer `(B6 Ch24)` to `(edition B6 ch56, ch60)` | applied | The pointer retarget is not in the list; it follows the list's basis (ch56:169-197, ch60:173-187) |
| SL:124 | Letters bullet replaced | applied | |
| SL:122 Seln's case | `Seln's locked case on its strap … never off him` | **held** (not touched) | O2 says it clarifies item 6, but the list's item 6 has no line for the case. See section 4, H6 |

### Item 7 — MOVEMENT-001 (A1, A3–A5, D1–D4, N1–N4, N7), with O1, O2, O3

| File:line | Text changed | Status | Note |
|---|---|---|---|
| M1:13 | **O3** note inserted verbatim above the Read line | applied | |
| M1:15 | Read line: Book 6 `chapter-23.md`, `chapter-24.md` replaced by `edition Book 6 manuscript/chapter-54.md–chapter-60.md and the Book 6 STATE_LEDGER AFTER MOVEMENT 8 and AFTER MOVEMENT 9 blocks (coordinator rulings/CLOSED notes) — the seam read`; BM reference now `§§1, 5, 7, 9, 10 and ruled C1` | applied | B7 source chapter-01/02 stay in the line but are labelled `(coordinator/reviewer reference only; see the note above)` so they are not presented as author reading |
| M1:19 | Where we enter replaced | applied | **O1:** `sealed Velmere letter` struck. **O2:** `three numbered boxes and Seln's locked case under one canvas` kept |
| M1:23 | `turns four years of not-using into` to `turns the discipline of not using into` | applied | |
| M1:26 | `C1 (default unless the owner rules otherwise)` to `OWNER #23 / C1 (binding)`; the two sentences on the reserve and `in hand` replaced by `The sale and remaining Book 6 purse become the sealed reserve; the board purse alone is “in hand.”` | applied | Interpretation: see section 4, H3 |
| M1:29 | Storm and Anchor text inserted after `each with its rent:` | applied | Position: see section 4, H4 |

### Item 8 — first pole, `since Kindling` (A3; OWNER #18)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| BM:273 (protected) | `I've spent four years being the case the instruments couldn't parse` to `Since my Kindling I've been the case the instruments couldn't parse` | applied | Listed in section 2. `MOVEMENT-001` line already corrected by item 7 |

### Item 9 — named seasons and metric units (A2; OWNER #42), narrowed by O4

Applied (every named season and metric unit; marks sit after the line for protected lines):

| File:line | Old to new | Status | Note |
|---|---|---|---|
| BM:40 | `"Spring. Whatever's on that bearing. My crew comes."` to `"After the thaw. …"`; `winters at Lowmarch` to `stays at Lowmarch through the cold term`; `for the winter` to `for the cold term` | applied | Restates protected Ch24; marked `OWNER-pending #48` |
| BM:43 | `four hundred metres' radius` to `about four hundred and forty yards' radius` | applied | |
| BM:59 | `forty meters` to `forty-five yards`; `a hundred meters` to `a hundred and ten yards` | applied | |
| BM:165 | `winter fence` to `cold-term fence`; `a spring term` to `an after-thaw term` | applied | Article changed so the phrase reads |
| BM:206 | `forty meters` to `forty-five yards` | applied | |
| BM:240 | `Teague's spring term` to `Teague's after-thaw term` | applied | Callback description updated; `a tape and a season` and `this season` stay (O4) |
| BM:269 (protected) | `Spring: bring the map` to `After the thaw: bring the map` | applied | Section 2 |
| BM:284 (protected) | `autumn, ` deleted | applied | Section 2 |
| BM:307 (protected) | `Twelve hundred and fifty-six meters, and a piece.` to `One thousand three hundred and seventy-four yards, and a piece.`; `A winter either side.` to `A cold term either side.` | applied | Section 2 |
| BM:317 (protected) | `Two hundred meters and a stride` to `Two hundred and twenty yards and a stride` | applied | Section 2 |
| BM:321 (protected) | Three spoken `Spring` to `After the thaw`; `winter road` to `cold road` | applied | Section 2. The list says `both` spoken Spring occurrences; the line has three (Teague; Brom twice). All three are named-season uses and all were changed. The Path clause is untouched (OI-1) |
| BM:334 | `200 m` to `about 220 yards` | applied | |
| BM:338 | `400 m` to `about 440 yards` | applied | |
| BM:351 | `which winters in the ferryman's shed` to `which stays in the ferryman's shed through the cold term` | applied (not in the list) | Found by the item-16 grep; same substitution as BM:40 |
| SL:54 | via item 3 | applied | |
| M1:30 | `forty meters` to `forty-five yards`; `a hundred meters` to `a hundred and ten yards` | applied | `last month` left (O4) |
| M1:51 | `autumn road` to `cold road` | applied | |
| M2:18, M2:39 | `autumn road` to `cold road` | applied | |
| M4:30 | `A winter either side` to `A cold term either side` | applied | Restates protected Ch10; marked `OWNER-pending #48` |
| M4:49 | `a hundred and forty meters` to `a hundred and fifty yards`; `two hundred meters` to `two hundred and twenty yards` | applied | |
| M5:24 | `four meters` to `thirteen feet`; `a hundred and twenty meters` to `a hundred and thirty yards`; `two meters` to `six feet` | applied | |
| M6:49 | `in the back of autumn` to `in the hard-cold days` | applied | |
| M7:30 | `five winters of scale` to `five cold terms of scale` | applied | |
| M7:31 | `forty meters` to `forty-five yards` | applied | |
| M8:24 | `high autumn` to `the last mild days` | applied | |
| M8:25 | `a hundred and seventy meters` to `a hundred and eighty-five yards` | applied | The literal water `spring` in the same line is kept |
| M8:34 | `winter fence` to `cold-term fence`; spoken `Spring` to `After the thaw` | applied | The spoken word restates protected Ch24; marked `OWNER-pending #48` |
| M8:49 | `last autumn` to `last mild days` | applied | |
| M8:53 | `spring term` to `after-thaw term` | applied | |

Not applied (O4: the only target is the generic word `season` or `month`; left exactly as written, in protected and unprotected text alike):

BM:34 `not three times this season`; BM:39 and BM:94 `season line`; BM:60 and protected BM:272 `Season's open`; BM:79 `season's order`; BM:222 `season order`; protected BM:274 `once a month`; protected BM:300 `this month`; protected BM:304 `a tape and a season`, `inside a season`; protected BM:308 `holds nothing for a season`, `a tape and a season`; protected BM:316 `this season`; protected BM:318 `this season`; M1:30 `last month`; M1:31 `Season's open`; M3 `a month`, `a tape and a season`; M5 `a tape and a season`, `slung for the season`; M7:16 `season's order`; M8:34 `season line`.
O4 said protected lines 304, 307, 308 and 321 mix both kinds. In fact 304 and 308 contain only generic `season` words, so they are unchanged; 307 and 321 contain both and only the named-season and metric parts changed.

### Item 10 — capability logic (B1–B3)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| BM:187 | Appended `At Gold weight, choose air or body/ground; never both. A Storm lane uses the air read and suspends body/ground reading until relinquished.` | applied | |
| BM:188 | `circle and Oryn only` to `the informed B6 circle only; Oryn cannot see or attribute the use` | applied | |
| BM:189 | Appended `Perception is sure at about ten feet, faint at twelve, absent at fourteen; do not infer unbinding reach from perception.` | applied | |
| M5:24 | `Shadow, once, ten strides (circle and Oryn only)` replaced by the Oryn-screened sentence | applied | The markdown bold around `Shadow, once, ten strides` sits between the words; the replacement keeps the bold and ends it before the full stop |
| M5:24 | `From within ten feet,` prefixed to `Anchor's perception sees Karis's points before they light` | applied | |
| M5:24 | After `Storm seeding the rut` inserted `the Iron/body read already released to the air and unavailable under his soles until the lane is relinquished` | applied | A comma was added before the inserted clause |
| M7:31 | `Anchor let off at ten meters as perception, then as a hand` replaced by `Once Cael is within ten feet of the knot, Anchor perception finds it; he then makes the separate purposeful unbinding, without assigning that action a measured reach, rate or price` | applied | The final full stop of the replacement was dropped so the original colon and `**the knot found and released**` still follow |

### Item 11 — non-protected Quiet/Kindling text (B4, B7)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| BM:100 | `stops every Path but mine` to `stops every live Arbiter but leaves my fragments answering` | applied | |
| BM:123 | `a line every Path in the party stops at but his` to `a line that stops every live Arbiter in the party while his already-dark Arbiter stays dark and his fragments answer` | applied | |
| BM:194 | Arbiter row replaced | applied | |
| M4:22 | Same replacement as BM:123 (`except his` form) | applied | |
| M6:26 | Opening and the `Nobody has ever attached a condition` sentence replaced | applied | The list's replacement is one block; its retelling and sources sentences replace the opening, its last sentence replaces the `Nobody has ever …` sentence. The bold lead `The telling on the table` is kept |
| BM:279–282, 287, 312, 321 | Not changed | n/a | OI-1; section 3 |

### Item 12 — Seln continuity (B5–B6, C2)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| BM:21, SL:96 | edition B6 ch37, recognition, twice-more count two | applied | Via items 2 and 5 |
| BM:145 | `six years carrying a case` to `twelve years carrying the case` | applied | `His fifteen years` describes service and stays |
| M7:9 | `six years carrying a case` to `twelve years carrying the case` | applied | |
| BM:314, M7:27 | Protected `Six years I've wanted a face` | not changed | OI-2; marked `[OWNER-pending #50]`; section 3 |

### Item 13 — acquisition citations and pointers (C1, D1)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| SL:75, 76, 77, 78 | Shadow `edition B4 ch34`; Storm `edition B5 ch56`; Anchor `edition B6 ch31/ch33/ch38`; Blade `edition B6 ch54` | applied | Via item 4 |
| BM:220 | `B6 Ch13` to `edition B6 ch31/ch33/ch38` | applied | |
| BM:354 | `B6 Ch23's "continental Copper title"` to `edition B6 ch55–57's "continental Copper title"` | applied (not in the list) | An item-16 hit; retargeted by item 13's rule that standings point to edition B6 ch55–57. The quoted phrase is not verbatim in the edition |
| other source-edition pointers | `B1 Ch15`, `B1 Ch16`, `B1 Ch17`, `B2 Ch13`, `B2 Ch24`, `B3 Ch13`, `B2 Ch19`; `(B6 Ch24)` at SL:150 and BM:350; `first camp` at BM:56 | held | Outside the list and outside item 16's patterns; section 4, H9 |

### Item 14 — Gault's note stays west (D5, N5)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| M6:29 | `Pike's Fallow copy by carter; "Six went in. Six came out." beside Gault's last note.` replaced by the list text (`arrives by carter … is not among the party's papers`) | applied | Bold lead kept; curly quotes as in the list |

### Item 15 — C1 recorded as decided (N7)

| File:line | Text changed | Status | Note |
|---|---|---|---|
| BM:350 | `Recommend (default)` to `OWNER #23 (binding)`; the `*Alternative:* …` paragraph and `**Owner call.**` deleted; `This is no longer pending.` added after the board-purse explanation | applied | |
| BM:379 | Run-note bullet replaced by `Drafting may begin on the OWNER #23 C1 ruling once the B6 reconciliation amendments are applied. C2 and C3 remain staged as planned; C8 is the only optional later preference in this paragraph.` | applied | The whole bullet was replaced; see section 4, H5 |

### Item 16 — consistency searches

Results are in section 5.

### Coordinator overrides, where they acted

| Override | Where | Status |
|---|---|---|
| O1 Velmere letter | Struck from the Cael/satchel inventories in BM:19, SL:119, M1:19; Brom sentence added at BM:21 and SL:94 | applied |
| O2 Seln's case | BM:21 `brought the locked case east in his own satchel; it now rides under the canvas`; `Seln's locked case under one canvas` kept in BM:23 and M1:19 | applied |
| O3 no-source note | Inserted verbatim above the `Read before drafting` line in all eight packets (M1:13, M2:12, M3:12, M4:12, M5:12, M6:12, M7:12, M8:12); M1's seam read replaced | applied |
| O4 narrowing | Item 9 above | applied |
| O5 owner items | Marks only; section 3 | applied |
| O6 birthday | M6:14 (below the O3 note, above the Read line); SL:53 as a bullet under the `eighteen until the 102nd` line | applied |

## 2. Protected lines changed (the owner's restore list)

Six protected lines in `BOOK_MAP.md` §10 were changed. Authority: **#18** (extended to Book 7 by #48) for the first pole at BM:273; **#48 / coordinator O4** (named seasons and metric units; the same minimal mandatory changes Books 5 and 6 applied to protected text) for the other five. Each carries `[B6-reconciled 2026-10-11: OWNER-pending #48]` at the end of the line. The baseline line number equals the current line number. Full OLD text is in `state/pre-B6-reconciliation/BOOK_MAP.md` at the same line number; the full OLD and NEW lines are reproduced below so the list is self-contained.

| BM line | Protected unit | Change (old to new) | Authority |
|---|---|---|---|
| 269 | Oryn's letter (Ch24) | `Spring: bring the map` to `After the thaw: bring the map` | #48 / O4 |
| 273 | Ch2 first pole | `I've spent four years being the case the instruments couldn't parse` to `Since my Kindling I've been the case the instruments couldn't parse` | #18 (item 8) |
| 284 | Ch14 birthday line | `in the steading's common room, autumn, the fire lit for us` to `in the steading's common room, the fire lit for us` | #48 / O4 |
| 307 | Ch10 exchanges | `Twelve hundred and fifty-six meters, and a piece.` to `One thousand three hundred and seventy-four yards, and a piece.`; `A winter either side.` to `A cold term either side.` | #48 / O4 |
| 317 | Ch20 exchanges | `Two hundred meters and a stride, to the stride.` to `Two hundred and twenty yards and a stride, to the stride.` | #48 / O4 |
| 321 | Ch24 exchanges and closing | `Spring. Whatever's on that bearing` to `After the thaw. Whatever's on that bearing`; `he's got the winter road` to `he's got the cold road`; Brom `"Spring,"` to `"After the thaw,"`; Brom `"Spring."` to `"After the thaw."` (closing) | #48 / O4 |


### BM:269 — Ch24 Oryn's letter

OLD:

````text
- **Oryn's letter (Ch24):** *Route's whole. The knee held. Nobody died of three weeks. Spring: bring the map, and lie still when I say. — O.* — then: Six, by letter. (The architecture and series docs still quote "eleven days"; prose and Book 8 say **three weeks**. See C6.)
````

NEW:

````text
- **Oryn's letter (Ch24):** *Route's whole. The knee held. Nobody died of three weeks. After the thaw: bring the map, and lie still when I say. — O.* — then: Six, by letter. (The architecture and series docs still quote "eleven days"; prose and Book 8 say **three weeks**. See C6.) [B6-reconciled 2026-10-11: OWNER-pending #48]
````

### BM:273 — Ch2 first pole

OLD:

````text
- Ch2, the first pole: *No instrument out here reads me. No Arbiter station, no assessment panel, no registry seat with a seal on it. The board reads what we did. I've spent four years being the case the instruments couldn't parse, and it turns out the cure was a country with no instruments. Write it plainly, because it's true: I'm free. First time.*
````

NEW:

````text
- Ch2, the first pole: *No instrument out here reads me. No Arbiter station, no assessment panel, no registry seat with a seal on it. The board reads what we did. Since my Kindling I've been the case the instruments couldn't parse, and it turns out the cure was a country with no instruments. Write it plainly, because it's true: I'm free. First time.* [B6-reconciled 2026-10-11: OWNER-pending #48]
````

### BM:284 — Ch14 birthday line

OLD:

````text
- Ch14, the birthday line: *Hundred and second day past the Line. Nineteen. Written at Thornwater, in the steading's common room, autumn, the fire lit for us. Witnesses: four of my own, and a healer who's a stop.*
````

NEW:

````text
- Ch14, the birthday line: *Hundred and second day past the Line. Nineteen. Written at Thornwater, in the steading's common room, the fire lit for us. Witnesses: four of my own, and a healer who's a stop.* [B6-reconciled 2026-10-11: OWNER-pending #48]
````

### BM:307 — Ch10 exchanges

OLD:

````text
- Ch10: Karis: "Sixty-two cords and twenty strides," … "Twelve hundred and fifty-six meters, and a piece." … "A circle is a made shape." — Lira: "like a clock that stopped and started again without losing the time." — Seln: "You drive them where you've measured to. Not where you've measured from." … "Five years in the weather. A winter either side." — Brom: "Skin." — Karis: "It costs nothing. There's nothing to spend." — Seln: "I've a knife and fifteen years. It was never most of what I do." — Oryn: "Nothing. Not nothing in him. Nothing in my hands." … "A healer's hands stop working there." — Cael: "It was dark before," … "It's dark now." — Karis: "None I own. And I own more than the registry prints." — Seln: "They live in here because nothing that walks in can fight."
````

NEW:

````text
- Ch10: Karis: "Sixty-two cords and twenty strides," … "One thousand three hundred and seventy-four yards, and a piece." … "A circle is a made shape." — Lira: "like a clock that stopped and started again without losing the time." — Seln: "You drive them where you've measured to. Not where you've measured from." … "Five years in the weather. A cold term either side." — Brom: "Skin." — Karis: "It costs nothing. There's nothing to spend." — Seln: "I've a knife and fifteen years. It was never most of what I do." — Oryn: "Nothing. Not nothing in him. Nothing in my hands." … "A healer's hands stop working there." — Cael: "It was dark before," … "It's dark now." — Karis: "None I own. And I own more than the registry prints." — Seln: "They live in here because nothing that walks in can fight." [B6-reconciled 2026-10-11: OWNER-pending #48]
````

### BM:317 — Ch20 exchanges

OLD:

````text
- Ch20: Teague: "We'll hold it till you're up." / "Noted" — Oryn: "What are they" / Karis: "Lines," — Karis: "He tried to drive it. Twice, by the head. It wouldn't go. Nothing goes into this." — Seln: "Nobody leaves a registry kit. It's signed out. You don't get another." … "I don't know what this is in, and I'm not going to say." — Karis: "Forty-one," … "every ten cords and a piece. Two hundred meters and a stride, to the stride." … "The floor was carved by somebody who knew the circle's size," … "A measurement is a fact about a ruler, not about the hand that held it."
````

NEW:

````text
- Ch20: Teague: "We'll hold it till you're up." / "Noted" — Oryn: "What are they" / Karis: "Lines," — Karis: "He tried to drive it. Twice, by the head. It wouldn't go. Nothing goes into this." — Seln: "Nobody leaves a registry kit. It's signed out. You don't get another." … "I don't know what this is in, and I'm not going to say." — Karis: "Forty-one," … "every ten cords and a piece. Two hundred and twenty yards and a stride, to the stride." … "The floor was carved by somebody who knew the circle's size," … "A measurement is a fact about a ruler, not about the hand that held it." [B6-reconciled 2026-10-11: OWNER-pending #48]
````

### BM:321 — Ch24 exchanges and closing

OLD:

````text
- Ch24: Pike: "Teague says you need a column I don't have. I've kept this ledger thirty years. First time it's been wrong about a crew by being too small." — the carters: "Eleventh," / "Aye," — Teague: "Spring. Whatever's on that bearing. My crew comes." / "Noted," — Pike: "Fence. Forty. Teague says it's yours if you want it; he's got the winter road," / Brom: "Ours," — Lira: "She'll say when," / Brom: "Spring," — *The sites were on an alignment. Not random.* — Karis: "Someone made this pattern." (said once; nobody answers) — **Closing, exact:** "I have ten things that aren't a Path," Cael said, eventually, to nobody in particular, "no tier, no rank, no file I can see — and five people, one of them on a route, who've walked into the quiet three times and come out." He turned it over once and let it stand. "And a line on a map that somebody drew before there was a registry to draw one." / Lira, one-armed, feeding the fire: "Then we follow it." / Brom: "Spring." / Karis, writing: "Noted." / Down the fire, the man who used to file reports about him watched the snow on the ferry landing with evident professional approval and said nothing, which — from him — was home. / Nothing out here had read him. At three floors older than any registry, every Path in the party had stopped at a line and his had not; a fourth had been paced from outside and not crossed. Nobody alive — least of all him — knew why. Someone had made the pattern. That was as far as anyone could say.
````

NEW:

````text
- Ch24: Pike: "Teague says you need a column I don't have. I've kept this ledger thirty years. First time it's been wrong about a crew by being too small." — the carters: "Eleventh," / "Aye," — Teague: "After the thaw. Whatever's on that bearing. My crew comes." / "Noted," — Pike: "Fence. Forty. Teague says it's yours if you want it; he's got the cold road," / Brom: "Ours," — Lira: "She'll say when," / Brom: "After the thaw," — *The sites were on an alignment. Not random.* — Karis: "Someone made this pattern." (said once; nobody answers) — **Closing, exact:** "I have ten things that aren't a Path," Cael said, eventually, to nobody in particular, "no tier, no rank, no file I can see — and five people, one of them on a route, who've walked into the quiet three times and come out." He turned it over once and let it stand. "And a line on a map that somebody drew before there was a registry to draw one." / Lira, one-armed, feeding the fire: "Then we follow it." / Brom: "After the thaw." / Karis, writing: "Noted." / Down the fire, the man who used to file reports about him watched the snow on the ferry landing with evident professional approval and said nothing, which — from him — was home. / Nothing out here had read him. At three floors older than any registry, every Path in the party had stopped at a line and his had not; a fourth had been paced from outside and not crossed. Nobody alive — least of all him — knew why. Someone had made the pattern. That was as far as anyone could say. [B6-reconciled 2026-10-11: OWNER-pending #48] [OWNER-pending #49]
````

### Non-protected restatements and dependents of the changed protected words

These are plan text (not §10) that repeat or describe the changed protected words. If the owner restores a protected line, restore these with it.

| File:line | Old to new |
|---|---|
| BM:40 | `"Spring. Whatever's on that bearing. My crew comes."` to `"After the thaw. Whatever's on that bearing. My crew comes."`; `winters at Lowmarch` to `stays at Lowmarch through the cold term`; `for the winter` to `for the cold term` |
| BM:165 | `winter fence` to `cold-term fence`; `a spring term` to `an after-thaw term` |
| BM:240 | `Teague's spring term` to `Teague's after-thaw term` |
| BM:351 | `which winters in the ferryman's shed` to `which stays in the ferryman's shed through the cold term` |
| M4:30 | `A winter either side` to `A cold term either side` |
| M8:34 | `The winter fence` to `The cold-term fence`; `"Spring."` to `"After the thaw."` |
| M8:53 | `A captain's spring term` to `A captain's after-thaw term` |

Protected lines that O4 left exactly as written (they hold only generic `season` or `month`): BM:272, 274, 300, 304, 308, 316, 318.

## 3. Owner items left untouched

The words of every line below are unchanged. Each carries the mark after the line.

### OI-1 — protected Quiet/Kindling lines (`[OWNER-pending #49]`, OWNER-DECISIONS #49)


- `BOOK_MAP.md:279` (whole line, unchanged):

````text
- Ch9, at the stone: *Quiet ground. Karis's Arbiter stopped at a line she can mark with a rock. So did Lira's, Brom's, Seln's, Oryn's — same line, same step. Mine didn't. Mine's been stopped since I was fourteen. I don't know what that means. Nobody asked. Tomorrow we go in.* [OWNER-pending #49]
````

- `BOOK_MAP.md:280` (whole line, unchanged):

````text
- Ch10: *The circle is perfect. The stakes are the registry's. The dogs are inside. Everyone's Path dies at the line and mine didn't, and I've told nobody, and I'm going to need to think about why I haven't. Not tonight. Tonight we're inside the one place on the continent where a stillhound can't lose.* [OWNER-pending #49]
````

- `BOOK_MAP.md:281` (whole line, unchanged):

````text
- Ch11, the Book 9 plant: *Everyone else's went to sleep at the stone. Mine has been asleep since I was fourteen. Out here that makes me the only one who's awake.* [OWNER-pending #49]
````

- `BOOK_MAP.md:282` (whole line, unchanged):

````text
- Ch12: *I'm not keeping it secret. I'm keeping it unfiled. There's a difference. Lira said later. Later is when I have a sentence. The answer might be: because whatever I am isn't a Path. I've known that since I was fourteen. Out there it was a flag. In there it's the only thing that works. I don't have a word for what that makes me, and I'm not going to invent one at a camp with Lira's arm two hours old.* [OWNER-pending #49]
````

- `BOOK_MAP.md:287` (whole line, unchanged):

````text
- Ch16, the second pole: *Nothing out here reads me. And at a line you can mark with a rock, every Path in this camp stops, and mine doesn't. Karis won't write her hypothesis. I won't write mine. We're going to find the other circles. Pike said nobody goes in twice. Tomorrow makes three.* [OWNER-pending #49]
````

- `BOOK_MAP.md:312` (Ch15; the conflicting clause, quoted exactly from the unchanged line): `*one dark since fourteen; no change either side of the line; stated by him, not tested by me*`

- `BOOK_MAP.md:321` (Ch24 closing paragraph, the conflicting sentence quoted exactly from the unchanged text; the same line also carries the #48 season changes in section 2): `Nothing out here had read him. At three floors older than any registry, every Path in the party had stopped at a line and his had not; a fourth had been paced from outside and not crossed. Nobody aliv`


### OI-2 — `Six years I've wanted a face` (`[OWNER-pending #50]`, OWNER-DECISIONS #50)

- `BOOK_MAP.md:314` (Ch17): `People have faces. Six years I've wanted a face.` The whole Ch17 line is unchanged; the mark is at its end.
- `packets/MOVEMENT-007.md:27`: `**Seln: "Take it… People have faces. Six years I've wanted a face."** [OWNER-pending #50]` The words are unchanged; the mark follows the quotation.

Companion non-protected change (item 12): `BOOK_MAP.md:145` and `MOVEMENT-007.md:9` now say `twelve years carrying the case`.

## 4. Held or ambiguous

| # | Where | What was found | What was done |
|---|---|---|---|
| H1 | SL:64 (Attention row) | `("the habits stay"; B6 Ch23)` is the one remaining item-16 hit. The pointer is a source-edition chapter and the quoted phrase `the habits stay` is not in the edition's Book 6. The nearest edition passage found is B6 ch57:123 (`by habit, to count the people behind him by touch … there were none`). Item 13 has no rule for this topic | **Held.** Text left; an inline `[B6-reconciled … HELD]` note added. Coordinator to rule the retarget (suggested: `edition B6 ch57`) |
| H2 | SL:62, SL:123, BM:354 | Source pointers `(B6 Ch24)`, `(B6 Ch24)`, `B6 Ch23's` were not in the list; BM:354 is an item-16 hit | Retargeted by the list's own bases (F2.3 and item 13's rules), each marked. Quoted phrases in SL:62 and BM:354 are the source edition's, not verbatim in the edition |
| H3 | M1:26 | Item 7 says `replace the final implication of a pending choice with: …`. The pending-choice language is the heading (replaced) and the sentences on the reserve and `in hand` | I replaced the two sentences (`The sale and what is left … for … pays.`) with the list text. The phrase `that Brom's rule keeps them from living on` is therefore gone from this packet |
| H4 | M1:29 | Item 7 says insert the Storm and Anchor text `after each with its rent`. The inserted text begins `Storm:` and has no joining punctuation | Inserted after the colon that follows `each with its rent`, so the original list (`Shadow drifting at dusk …`) follows it. No words added |
| H5 | BM:379 | Item 15 says replace `the sentence requiring an owner ruling on C1` with a two-sentence text. The bullet had three sentences (`Drafting may begin on the defaults.`, the C1 sentence, `C2, C3 and C8 can be ruled on …`) and the replacement covers all three | The whole bullet was replaced. Replacing only the middle sentence would have left a duplicate `Drafting may begin` and a contradicting C2/C3 sentence |
| H6 | SL:122 | O2 says the Seln case wording clarifies item 6, but item 6 does not touch this line, which still reads `Seln's locked case on its strap … carried on every road, never off him`. That conflicts with the O2 reading (his own satchel to the shelf, then under the canvas) | **Held**, untouched. Coordinator to rule |
| H7 | SL:123 | The cart bullet still carries the label `**C1 default:**` immediately before the new `OWNER #23 governs:` sentence. The list replaces only the final sentence | Label left as is. Coordinator may drop `default` |
| H8 | SL:78 (Blade row) | After the append the row still reads `Integrated` and `engagement field earnest — non-hostile`, while the exact notice (F1.5) reads `Integration: partial` and `Engagement: adversarial, earnest — non-hostile` | Not changed (not in the list). Coordinator to rule whether the row's status and engagement cell should follow the notice |
| H9 | Residual source-edition pointers, not covered by item 16's patterns | BM:56 spine row 1 `The road from the first camp` (the shelf is now the second camp, first fire); BM:350 `B6 Ch24 ends with "A cart …"`; SL:150 `(B6 Ch24)`; SL:70–74, 79 and SL:93 acquisition and knowledge pointers `B1 Ch15`, `B1 Ch16`, `B1 Ch17`, `B2 Ch13`, `B2 Ch24`, `B3 Ch13`, `B2 Ch19` | **Held**, not in the list. Coordinator to rule |
| H10 | Item 16 `chapter-23.md` / `chapter-24.md` | Hits in M4:5, M8:14 and BM:7 are Book 7's own chapter files (`manuscript/chapter-23.md` in M4:5; `B7 source` chapter lists in M8:14 and BM:7), not Book 6 chapters | False positives; no change |
| H11 | M5:33 (`Five witnesses to the Ring and no one else`) | Six people stand at the Ring (the five travelers and Oryn). The item-10 Shadow sentence now says Oryn has no sightline; the witness sentence was not in the list | Not changed. Observation only |
| H12 | M1:15 | O3 asks that B7 source chapter-01/02 not be presented as author reading. The line keeps them (they are the coordinator's and reviewers' references per the O3 note) and labels them | Applied with the label; coordinator may prefer to delete the two references from M1's line |

## 5. Item 16 — final grep results (ten plan files)

Command class: fixed-string `grep -nF` for the twelve list patterns over `BOOK_MAP.md`, `STATE_LEDGER.md`, `packets/MOVEMENT-001.md` … `008.md`.

| Pattern | Hits | Detail |
|---|---|---|
| `B6 Ch23` | 1 | SL:64 — **held**, H1 |
| `chapter-23.md` | 2 | M4:5, M8:14 — Book 7's own chapters (H10); not Book 6 |
| `chapter-24.md` | 2 | BM:7, M8:14 — Book 7's own chapters (H10); not Book 6 |
| `first camp beyond` | 0 | |
| `eleven-minute` | 0 | |
| `ranking forfeited` | 0 | |
| `left the Compact in form` | 0 | |
| `late thirties` | 0 | |
| `Active non-compliance. Observation priority escalated.` | 0 | |
| `since B6 Ch15` | 0 | |
| `circle and Oryn only` | 0 | |
| `ten meters` | 0 | |
| `six years carrying a case` | 0 | |

O4-adjusted season and metric search (word boundaries, case-insensitive; `autumn|winter|summer|meter|metre`, `spring` as a season, plus kilometre/km/cm/mm/kg and `\d m` units): **0 true hits.** Raw substring hits: `meter` 14 (all in `perimeter`), `MM` 1 (the `YYYY-MM-DD` template at SL:176), `spring` 1 (M8:25, the literal water spring). `fall` appears only as a verb or noun (M2:23 `pools that fall away`; BM:308 `not a fall`). No English month name or weekday name occurs in the ten files. Generic hits expected and left under O4: `season` 27, `month` 10 (counts include marks that quote them).

`Velmere` across the ten files: four lines, none says the letter travels. SL:94 and BM:21 say it was left sealed and unopened on Brom's table at Halcenvane with the unsigned finding and that Brom carries no family letter east; BM:19 and SL:119 name it only in a mark (`the Velmere letter is not carried`).

## 6. Verification notes

- Every inserted coordinator note (O3 in all eight packets; O6 in M6 and SL) was checked as an exact substring of the override file's text.
- `BOOK_MAP.md` has the same number of lines as the baseline (381 lines before and after); no table row gained or lost a pipe cell (the one misplaced mark on the Arbiter row was corrected inside the cell).
- Mark counts (`B6-reconciled`): BM 37; SL 23; M1 8; M2 3; M3 1; M4 4; M5 7; M6 6; M7 5; M8 7. `OWNER-pending #48`: 7 in BM (six protected lines plus the BM:40 restatement) + M4:30 + M8:34. `OWNER-pending #49`: 7 (BM:279, 280, 281, 282, 287, 312, 321). `OWNER-pending #50`: 2 (BM:314, M7:27).
- Next fixed checkpoint: the coordinator rulings on H1, H6, H8, H9; then OI-1 before Movement 4 and OI-2 before Movement 7.

## 6. Coordinator rulings on the held and open items (Claude Opus 5.5, 2026-10-11)

Marked inline `[B6-reconciled 2026-10-11: coordinator ruling]`.

1. **SL "Attention" row ("the habits stay"; B6 Ch23):** the quoted phrase and the source pointer are dropped. Now: "The habit kept, its reason gone: the last watcher turned back at the provincial marker (edition B6 ch59)".
2. **SL Seln's locked case:** brought east in his own post satchel; under the cart's canvas with the boxes since the shelf; back on its strap and on him once the cart is sold in Lowmarch's first week (#23). Never opened in this book.
3. **SL Blade row:** status follows the notice (*Integration: partial*), still settling on the road east; engagement field *adversarial, earnest — non-hostile*.
4. **Stale pointers:** BM "The road from the first camp" is now "from the shelf (the second camp past the Line)"; BM C1's "B6 Ch24 ends with …" quotation is replaced by a plain statement of the edition's ch60 end state; SL "found family's grammar (B6 Ch24)" now cites edition B6 ch58–60 and carries Book 6's actual rota (two watches of four hours, two to a watch, the fifth sleeps through and changes each night; not set aside for anyone's judgment). The fragment table's rows 1–5 keep source-edition chapter numbers under a note saying so.
5. **The apply seat's three interpretations** (M1 reserve / "in hand" sentences; M1 insertion after the colon; BM run-notes bullet replaced whole): accepted.
6. **M5 "Five witnesses to the Ring and no one else":** now "Five witnesses to the Shadow use at the Ring and no one else: Oryn is at the Ring but is screened and cannot see or attribute it."

**Release:** Book 7 Movement 1 is released for no-source drafting. Owner items #49 (before Movement 4) and #50 (before Movement 7) stay open with the protected lines verbatim.
