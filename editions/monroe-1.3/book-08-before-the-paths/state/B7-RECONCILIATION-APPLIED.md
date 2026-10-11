> Built by TAC (reconciliation-apply seat, claude-sonnet) — 2026-10-11

# Book 8 plan — Book 7 reconciliation APPLIED

Companion to `B7-RECONCILIATION-AUDIT.md`, `B7-RECONCILIATION-H-RERUN.md` (Sol, amendments 1–28) and `B7-RECONCILIATION-COORDINATOR-OVERRIDES.md` (P1–P4). The overrides governed wherever they differ from the list.

Files edited: `BOOK_MAP.md`; `STATE_LEDGER.md`; `packets/MOVEMENT-001.md` … `MOVEMENT-009.md`; this file (new). The eleven plan files were copied by plain `cp` before any edit to `state/pre-B7-reconciliation/` (packets in its `packets/` subfolder); that folder is the diff baseline. No manuscript, no Book 6 or Book 7 file, no `OWNER-DECISIONS.md`, nothing under `books/` or `v3-runs/` was touched. No git command of any kind was run (comparison used plain `diff` and a read-only Python `difflib` pass; one verification grep was interrupted by the owner and re-run in another form).

Method: every change was made with the Edit tool by exact text match; no bulk regex was run over any plan file. Line numbers below are CURRENT line numbers (after this pass) unless marked "baseline". `BM` = `BOOK_MAP.md`, `SL` = `STATE_LEDGER.md`, `M1` … `M9` = `packets/MOVEMENT-00N.md`.

Marking: changes are marked inline `[B7-reconciled 2026-10-11: <amendment number>]`, placed directly after the changed phrase in plan text and AFTER the whole unit in protected text (never inside protected words). Changes to protected lines under a standing decision carry `[B7-reconciled 2026-10-11: OWNER-pending #48]`. Owner items carry `[OWNER-pending #52]` … `[OWNER-pending #58]` with their words untouched.

Status words: applied (text changed and marked); annotated (words untouched, owner mark added); held (not changed or applied by interpretation; see section 4); not applied per P1 (override kept the words verbatim).

## 1. Amendments 1–28

| # | File:line (current) and text changed | Status | Note |
|---|---|---|---|
| 1 | M1–M9, the O3 no-source note inserted verbatim above `- Read before drafting:` (line 10 in each of the nine packets, the read bullet follows at line 12; M1 has two notes, so its read bullet is at line 14) | applied | Nine notes, one per packet. Each is followed by `[B7-reconciled 2026-10-11: amendment 1]` outside the quoted note. The note is a blockquote paragraph with a blank line each side, so it splits the bullet list in two (H16). No read-list bullet deleted |
| 2 | M1:12 (second blockquote), the O6 birthday note, immediately below the O3 note | applied | One only, in M1 |
| 3 | BM:7, provenance paragraph replaced | applied | |
| 4 | BM:21-30, the whole Book 7 entry block replaced (When/where; Cael; The five at Lowmarch; Objects/accounts; Letters/animals; Oryn; Teague's crew; The Quieting; Pike/the Compact; Who knows) | applied | Text is the list's, verbatim. The block now has ten bullets (the list's). The heading at BM:19 was not in the list and is unchanged (H14). Information in the old Compact bullet that the new block does not carry is listed in H3 |
| 5 | BM:36 `about 1,107 yards across`; BM:40 Oryn ending quote to `"After the thaw: bring the map, and lie still when I say."` (mark OWNER-pending #48); BM:41 Teague ending quote to `"After the next thaw. Whatever's on the next line. My crew comes."` (mark OWNER-pending #48); BM:41 `[OWNER-pending #54]` after `His name was said once by the broad man and is never written.` | applied; the #54 sentence annotated | The two quotes are restatements of Tier A 22; see section 2 |
| 6 | BM, 25 non-protected substitutions: spine 1 (BM:53) `The cold-term frame`, `The cold stay is priced`; spine 2 (BM:54) `cold-term board`; spine 38 (BM:90) `about 1,107 yards across (159 cords)`; Vastin ending (BM:39) `the thirtieth day of Oryn's treatment month`; Thornwater (BM:58) `first stops after the thaw`; crest (BM:85) `Not one cold term`; expansion rows BM:108, 110; learning arc 1 (BM:119) `during the cold term`; BM:129 `The cold months`, `The cold-term board`; BM:130 `prepares for the road after the thaw`; BM:134 `read himself twice earlier at the Hall`; BM:149 `Holds the after-thaw term.`; BM:150 (cast row Pike) `Prices the cold term.`; BM:169 `Put the cold term on the page`; BM:194 `M1: a cold night`; BM:197 `M1: the upper inn during the cold term`; BM:208 `Cold stay priced (76)`; BM:217 `Teague's after-thaw term`; BM:277 `The cold-term inventory and practice`; BM:323 `fifty-five yards below`; BM:458 `New cold-term, Treswick and leg episodes`; spine 36 (BM:88) `The tall woman speaks to the six for the first time.`; spine 37 (BM:89) left, see below | applied; spine 37 annotated per P1 | Spine 37 `The log (§10, "the whole year").` stays verbatim with `[OWNER-pending #58]` (P1.4), not `all these days`. BM:85 `Not one cold term` restates the protected M8 unit (section 2, restatements) |
| 7.1 | BM:58 spine 6 `"Five months and twenty days."` | not applied per P1.1; annotated | Words verbatim; `[OWNER-pending #56]` after the quoted interval |
| 7.2 | BM:65 spine 13 | applied | Now `the date matches his Kindling day; "six years" is the office's survey-record rounding; no numeric span since Kindling is computed` |
| 7.3 | BM:119 learning arc 1, the Tide sentence and the two final sentences | applied | Interpretation of "Tide/final two sentences": H5 |
| 7.4 | BM:259 capabilities table, `The ten (entry)` row, cost cell | applied | |
| 7.5 | BM:73 spine 21 `"I was fourteen. I'm nineteen. I'm not there yet either."` | not applied per P1.2 | Verbatim, no mark |
| 8 | BM:380-387 Tier B callbacks: Karis ruler (`chapter-52.md:311`), Karis pattern (`chapter-57.md:99`; `chapter-60.md:251`), Oryn (mark OWNER-pending #48), Hesk note, Teague and Pike (mark OWNER-pending #48), still-place inventory, kit's ledger | applied (with H1, H2) | The block is eight bullets, not seven; the Vastin (B6) bullet is not in the list's replacement and was kept verbatim in its place |
| 9 | BM protected text (13 listed rows) | 7 applied (P2); 6 not applied (P1); see section 2 and 3 | Applied: Tier A 17; Tier A 22; Ch1 closing log; S12 log; S17 log (all with OWNER-pending #48 mark). Not applied per P1: Thornwater `Five months and twenty days.` (#56); S20 `since I was fourteen` (no mark); S20 `my Path worked` (#57); S22 `the whole year` log and parenthetical (#58); S23 `His Path did not die` (#57); closing prose `the whole year` (#58) and `a machine that lit for everyone but him` (#57) |
| 10 | BM owner marks: S5 `#52` (BM:395); S8 `#53` (BM:398); S24 ledger `#55` (BM:411); C11 `#55` (BM:448); young-one cast row `#54` (BM:151); Teague boundary `#54` (BM:197); sequence lock `#54` (BM:465) | annotated | Words untouched |
| 11.1 | BM:438 C1 | applied | Interpretation: H4 |
| 11.2 | BM:439 C2 `Edition:` policy portion, to the paragraph's end | applied | The trailing italic sentence went with it; `[OWNER-pending #53]` is in the new text |
| 11.3 | BM:441 C4 `Book 7 edition chapter 60's note (chapter-60.md:67)` | applied | |
| 11.4 | BM:448-449 C12 | applied | |
| 11.5 | BM:490 §15 | applied | Mark OWNER-pending #48 after the amended sentence |
| 11.6 | BM:498 run note | applied | |
| 12 | SL:3 authority header | applied | |
| 13 | SL:7 entry heading; SL:13-22 Bodies table (ten rows) | applied | Header rows of the table kept. Teague row keeps `[OWNER-pending #54]` |
| 14 | SL:24-48 Knowledge section | applied | The section now has per-person paragraphs and the terminology box. Dropped content: H3 |
| 15 | SL:50-62 Resources and accounts (heading renamed) | applied | |
| 16 | SL:66-80 fragment table rows 1-10 and the still-place row, and the paragraph after | applied | The list's replacement repeats the table header row; the original header is identical and kept once (H6). The old two-sentence paragraph became the deployment paragraph |
| 17 | SL:86 Lira; SL:90 Oryn; SL:98 fourth-site thread; SL:102 Oryn's debt thread; SL:105 Teague term; SL:108 carried list | applied | SL:108 the `; ` separator went with the deleted item (H7) |
| 18 | M1:16-17 read bullet (reviewer-only seam evidence); M1:22 `## Where we enter` paragraph replaced | applied | |
| 19 | M1: `C (cold term)` (17); `Put the cold term on the page` (26); `The cold stay priced`, `cold-term board` (29); `cold road` (30); `across the cold term` (32); `through the cold term` (35); `cold night` (40); `cold term takes` (54); Tide working-inventory clause (33); numeric rule (49); closing pressure `Since his Kindling, Cael has stayed out of registries.` (58, mark OWNER-pending #48); Thornwater quote (36) | applied; Thornwater quote not applied per P1.1 | Thornwater quote verbatim with `[OWNER-pending #56]` |
| 20 | M2:20 `first post-thaw stop`; M2:27 `the road after the thaw`; M2:31 `at a table before we left Ostrand` | applied | The Karis callback is protected: mark OWNER-pending #48 after the unit |
| 21 | M3:30 sum clause; M3:35 `Seln's locked case stays shut, unopened and undecided.`; M3:45 consent clause | applied | |
| 22 | M4 | applied (O3 only) | No other change required |
| 23 | M5:34 `"I was fourteen. I'm nineteen. I'm not there yet either."`; M5:42 `the locked case's weight`; `The contents stay unknown.` | the `fourteen` line not applied per P1.2; case wording applied | `The contents stay unknown.` stays as written |
| 24 | M6 | applied (O3 only) | |
| 25 | M7 | applied (O3 only) | |
| 26 | M8:14 read bullet; M8:31 `earlier at the Hall`; M8:34 `Not one cold term` (mark OWNER-pending #48 after the unit); M8:51 `Seln's locked case stays shut and unopened.`; M8:69 `since he was fourteen` | applied except `since he was fourteen` | Not applied per P1.2 (a restatement of the S20 line); verbatim, no mark |
| 27 | M9:29 `for the first time` (applied); M9:37 `("the whole year")` kept, `[OWNER-pending #58]`; M9:42 dawn bullet Teague and Oryn quotes (applied, each with mark OWNER-pending #48); M9:8 `[OWNER-pending #54]`; M9:32 `[OWNER-pending #54]`; M9:56 `[OWNER-pending #55]` | applied; `("the whole year")` not applied per P1.4 | `for the first time in a year` was plan instruction, not inside a protected quotation, so the phrase was applied |
| 28 | Verification | run | Section 5 |

Counts of `B7-reconciled` marks (current): see section 6.

## 2. Protected lines changed (the owner's restore list)

Seven protected lines in `BOOK_MAP.md` and two protected units in the packets were changed, all under standing decisions: #18 (a year count since Kindling, extended by #48) for three; #48 (named seasons, as in Books 5-7) for six. Each carries `[B7-reconciled 2026-10-11: OWNER-pending #48]` after the unit. The baseline line numbers are in `state/pre-B7-reconciliation/`. The full OLD and NEW lines are reproduced in the appendix at the end of this report (generated from the baseline and current files, so they are exact).

| # | File: baseline line to current line | Protected unit | OLD (changed words) | NEW (changed words) | Authority |
|---|---|---|---|---|---|
| 1 | BM: 364 to 366 | Tier A 17, pole two | `For five years I thought the system forgot to make room for me` | `Since my Kindling I thought the system forgot to make room for me` | #18 (extended by #48) |
| 2 | BM: 369 to 371 | Tier A 22, departures | `Spring's over,` / `Next spring.` / `Spring. Bring the map. Lie still when I say.` | `The thaw's past,` / `After the next thaw.` / `After the thaw: bring the map, and lie still when I say.` | #48 |
| 3 | BM: 389 to 391 | Tier C, Ch1 closing log (270th) | `I've spent five years staying out of registries because a registry is where they file you.` | `Since my Kindling I've stayed out of registries because a registry is where they file you.` | #18 |
| 4 | BM: 400 to 402 | Tier C, S12 log | `I've spent five years learning to give ground and disappear.` | `Since my Kindling I've learned to give ground and disappear.` | #18 |
| 5 | BM: 403 to 405 | Tier C, S17 log | `Teague's crew came for spring like he said` | `Teague's crew came after the thaw like he said` | #48 |
| 6 | BM: 380 to 382 | Tier B, Oryn's letter | `Spring: bring the map, and lie still when I say.` | `After the thaw: bring the map, and lie still when I say.` | #48 |
| 7 | BM: 382 to 384 | Tier B, Teague | `Spring. Whatever's on that bearing. My crew comes.` | `After the thaw. Whatever's on that bearing. My crew comes.` | #48 |
| 8 | M2: 28 to 31 | Karis callback (Tier A 4-5 scene) | `I said so at a table in the autumn` | `I said so at a table before we left Ostrand` | #48 |
| 9 | M8: 31 to 34 | Seln, the crest | `Not one winter.` | `Not one cold term.` | #48 |

### Non-protected restatements and dependents of the changed protected words

If the owner restores a protected line, restore these with it.

| File: baseline to current | Old to new |
|---|---|
| BM: 38 to 40 | Oryn ending quote `"Spring. Bring the map. Lie still when I say."` to `"After the thaw: bring the map, and lie still when I say."` (mark #48) |
| BM: 39 to 41 | Teague ending quote `"Next spring. Whatever's on the next line. My crew comes."` to `"After the next thaw. Whatever's on the next line. My crew comes."` (mark #48) |
| BM: 25 and 38 to the entry block (BM:21-30) | `"Spring. Whatever's on that bearing. My crew comes." / "Noted."` and `Spring. Bring the map. Lie still when I say.` replaced by the Book 7 current wording (`After the thaw. …`; `After the thaw: bring the map, and lie still when I say. — O.`) |
| BM: 83 to 85 | Spine 33 `Not one winter` to `Not one cold term` |
| BM: 488 to 490 | §15 `"Spring. Bring the map."` / `"Next spring"` to `"After the thaw: bring the map, and lie still when I say."` / `"After the next thaw"` (mark #48) |
| M1: 53 to 58 | `Cael has spent five years staying out of registries.` to `Since his Kindling, Cael has stayed out of registries.` (mark #48; restates Ch1 closing log) |
| M9: 39 to 42 | Teague `"Next spring … My crew comes."` to `"After the next thaw … My crew comes."`; Oryn `"Spring. Bring the map. Lie still when I say."` to `"After the thaw: bring the map, and lie still when I say."` (marks #48) |

### Tier B callbacks retargeted to Book 7's current prose (not an owner-restore item; authority D2/A12)

BM baseline 378, 379, 381, 384, 385 to current 380, 381, 383, 386, 387. The Karis ruler line, the Karis pattern line and the Hesk note keep their words (only the source pointer changed). The still-place inventory callback grows from `Not the Quiet. Not a fragment. Older than the log. Observation continues.` to the full surviving log text (`chapter-60.md:39`), with Oryn's order now `Write it down and stop touching it.` and the Tide rule and kit's ledger pointers retargeted. Baseline bullet 383 (the Vastin B6 sentence) was kept unchanged (H1).

## 3. Owner items left untouched (words verbatim, marks added)

Current line numbers. Each protected unit is quoted exactly as it stands.

| Item | Unit (verbatim) | Locations |
|---|---|---|
| #52 | `right for five years or wrong for five years` | BM:395 (S5) |
| #53 | `it took four years and a hearing to walk out` | BM:398 (S8); the C2 policy text at BM:439 names it under `[OWNER-pending #53]` |
| #54 | `The young one` is named once at his death and the name is never written: `His name was said once by the broad man and is never written.` | BM:41 (ending); BM:151 (cast row `(Teague's; unnamed; his name is never written)`); BM:197 (`**The young one's name.**`); BM:465 (`**The young one's name is never written** (said once, by the broad man, in the stream-bed).`); SL:19 (Teague's crew row); M9:8 (`**The young one's name is said once, in the stream-bed, and is never written.**`); M9:32 (`The broad man says the name, once.`) |
| #55 | `Tell Lira's family I said so` | BM:411 (S24 letter, mark after `— C."`); BM:448 (C11); M9:56 |
| #56 | `"Five months and twenty days."` | BM:58 (spine 6); BM:392 (Thornwater, Tier C); M1:36 |
| #57 | `Because every other site, my Path worked while everyone's died.` (BM:407, S20 close; mark after the speech); `His Path did not die. It also did not *notice* it should have.` (BM:410, S23 close); `a machine that lit for everyone but him` (BM:412, closing prose) | BM:407, BM:410, BM:412 |
| #58 | `I've spent the whole year wanting` (BM:409, S22 log; mark after the log); `("the whole year", never "the whole book".)` (BM:409, S22 parenthetical; second mark); `He had spent the whole year learning` (BM:412, closing prose); the restatements `The log (§10, "the whole year").` (BM:89, spine 37) and `**The log, verbatim** ("the whole year").` (M9:37) | BM:89, BM:409 (two marks), BM:412, M9:37 |

Protected lines left verbatim under P1 with NO owner mark (ages are canon, P1.2):

| Unit | Locations |
|---|---|
| `"I was fourteen. I'm nineteen. I'm not there yet either."` | BM:73 (spine 21); M5:34 |
| `More than I've wanted anything since I was fourteen.` | BM:407 (S20 close) |
| `since he was fourteen` (restates the S20 line) | M8:69 |

Distinct protected lines held verbatim under P1: nine (Five months; `I was fourteen…`; `More than I've wanted anything since I was fourteen.`; the three Path/machine lines; the three `whole year` lines: S22 log, S22 parenthetical, closing prose). Counting their restatements and recurrences (BM spine 6, 21, 37, M1:36, M5:34, M8:69, M9:37) the verbatim occurrences total fifteen.

## 4. Held or ambiguous

| # | Where | What was found | What was done |
|---|---|---|---|
| H1 | Amendment 8 | The list calls the Tier B block "seven-bullet" and its replacement has seven bullets, but the block is eight bullets: baseline 378-385 includes `Vastin (B6): "I knew the system was imperfect. I didn't know it was designed to be."` (a protected Tier B unit also referenced in SL and M2). The replacement does not carry it | Replacement applied in two edits around it. The Vastin (B6) bullet is kept verbatim at BM:385. Coordinator to confirm it was meant to stay |
| H2 | Amendment 8 | The old Karis-ruler bullet carried a parenthetical (`in Ch1's form; S5, S15 and S20 use "A measurement is a fact about a ruler. Not about the hand that held it."`) that the replacement drops | Applied exactly; the parenthetical is gone. The two variant forms of the sentence are still in Tier C S5/S15/S20 |
| H3 | Amendments 4 and 14 | The replacements drop content the old text carried: BM old Compact bullet (`it has reached across the Line twice, on paper and in person`; `The asset-restriction is pending`; `Vastin is still inside, writing nothing, with one window in Book 7`); SL old Knowledge items (`The faceless faction has reached twice…`; `Asset-restriction is pending`; `Book 6's sentence from Vastin`; `Karis's sub-layer: "under every station on the continent"`; and the whole `He does not know:` paragraph, including `that instruments will read wrong in his hands. The last is discovered on the 168th`). The new Bodies-table Vastin row and the new Compact paragraph do carry part of this | Applied exactly. Coordinator to decide whether any of these protections (the 168th discovery, asset-restriction pending, the faction reaches) should be restored to the entry text |
| H4 | Amendment 11.1 | "Replace its first two sentences" is ambiguous (label plus first sentence, or the two sentences after the label) | Replaced the two sentences after the label (`The source states "Fifty-three, or near it"…` and `The universe ledger records 53.`) with the list's two. The label is kept. The old `OWNER-DECISIONS #8/#17 default: …` sentence follows, so #8/#17 is named twice; harmless |
| H5 | Amendment 7.3 | "Replace the Tide/final two sentences only" | Replaced the Tide sentence and the two sentences after it (`**Invent no new numeric ceilings.**` and `Costs are qualitative unless canon gives a number.`) with the list's two sentences. The Costs-are-qualitative sentence is gone, as it would contradict the new rule |
| H6 | Amendment 16 | The replacement text repeats the table header row | The original header (identical) is kept once; only the rows and the paragraph were replaced |
| H7 | Amendment 17.6 | "Delete only `Brom's advancement review`" leaves a dangling `; ` | The preceding `; ` was removed too. A mark sits where the item was |
| H8 | Amendment 6 / 26 | `read himself twice in the autumn` becomes `read himself twice earlier at the Hall` in a bullet that is already "The Hall's marsh, where…" (BM:134, M8:28) | Applied as listed; wording is slightly redundant |
| H9 | Unlisted metric figure | M9:38 `1,012 across` (no unit). BM now says `about 1,107 yards`; the packet still gives the old metric number | Not in the list and not matched by the grep; left. Coordinator to rule |
| H10 | Amendment 28 check 4 | `nothing owed` hits at BM:22 (the list's own negation, `` `nothing owed` is false``) and BM:34 (`123 marks; nothing owed`, the Book 8 END state, not the entry) | BM:22 resolved by design. BM:34 is an end-of-book fact outside the list; left |
| H11 | Residual stale entry facts outside the list | BM:119 learning arc 1 and M1:33 still say `Ember, never used`, `Storm asleep`, `Anchor used both ways`, `Shadow's idle draw and the seal`, against the new ledger (Ember point billed the left palm; Storm laid lanes; Anchor once each way). BM:460 (§13 lock) says Oryn `has read him three times (sack, table, marsh's edge)`, against the new entry (Cael self-read three times; Oryn read twice, each after ask) | Not in the list; left. Coordinator to rule |
| H12 | Residual `cache` wording outside the list | BM:74, 78, 145, 195 (twice), 432, 439 (`the cache carried "four years"`, a quoted source example), M5:38, M6:32 still say `cache`; amendments 21, 23, 26 changed only the cited packet sentences | Left. Coordinator may extend `locked case` |
| H13 | #54 mention not in amendment 10/27 | BM:88 (spine 36) `The name is said once.` carries no `[OWNER-pending #54]` | Not in the list; left unmarked |
| H14 | BM:19 heading | `### Entry (Book 7 close; source Ch1 opens on the hundred and thirty-first day past the Line)` is not in the list; `source Ch1` is Book 8's own source chapter | Unchanged |
| H15 | P1 recurrences | `since I was fourteen` / `I was fourteen…` remain in BM:73, 407, M5:34, M8:69 | Verbatim by P1.2, no mark |
| H16 | Amendment 1 form | The packets keep the read list as a bullet; the note is a blockquote paragraph between bullets, so the markdown list is split | Placed immediately above the read bullet as instructed; no bullet deleted |
| H17 | SL numerals | SL uses `27` where the list's text says `27`; the word `twenty-seven` is in BM only | As listed |
| H18 | Check 3 grep | `meter` matches `perimeter` at BM:195, BM:325, M8:51 | False positives |
| H19 | Check 5 grep | `Ring and Stair` appears in BM only (SL says `Ring, Stair`) | Present in the plan files as a set |
| H20 | Source pointers | M9:13 `chapter-23.md`, `chapter-24.md` and BM:7, BM:32 `chapter-24.md`, `Ch24` are Book 8's own source chapters (reviewer-only), not Book 7 pointers | No change |

## 5. Amendment 28 verification (as amended by P4), over the eleven plan files

1. O3 notes: exactly nine (`NO-SOURCE drafting, binding`: one each in M1-M9; none in BM or SL). Birthday note: exactly one (M1). PASS.
2. Named seasons: `autumn|winter|summer` (case-insensitive) over the eleven files: 0 hits. `spring`: 11 hits, all literal water springs or the 280th spring scene: BM:65, 80, 121, 144, 195, 221, 235; M3:30, 35, 49; M7:28. No seasonal `spring` remains. PASS.
3. Metric: `400 m|1,012 m|metre|meter`: 3 hits, all `perimeter` (BM:195, BM:325, M8:51), false positives. A wider scan found one unit-less figure: M9:38 `1,012 across` (H9). `440 yards and two strides` present in BM and SL. PASS with H9.
4. `unranked by choice|owes Cael|reader cannot read the reader|nothing owed|His Path works|Book 7 Ch14|Book 7 Ch15|B7 Ch20|B7 Ch23|B7 Ch24`: 2 hits, both `nothing owed` (BM:22 the list's explicit negation; BM:34 the Book 8 end state; H10). All other patterns 0. PASS with H10.
5. Required entry hits: `twenty-seven` (BM 2); `Ring and Stair` (BM 1); `It's paid` or `PAID` (BM 2, M1 1); `440 yards and two strides` (BM 1, SL 1); `stake 32` (BM 1, SL 1); `stake 34` (BM 1, SL 3); `52` (BM, SL, M1); `11 Ring / 29 Stair / 12 Hall` (BM 1, SL 1); `first boat of the thaw` (BM 1, SL 1); `brown mule` (BM 1, SL 1, M1 1); `grey jenny` (BM 1, SL 2); `60 yards of four-strand rope` (BM 1, SL 1); `locked case` (BM 1, SL 1, M1, M3, M5, M8 1 each). PASS.
6. The restore table (section 2) lists only P2 changes: the nine protected units above. The two Book 7 callbacks changed by amendment 8 under #48 are rows 6 and 7. PASS.
7. Owner marks present: `[OWNER-pending #52]` 1; `#53` 2; `#54` 7; `#55` 3; `#56` 3; `#57` 3; `#58` 5. None of the protected words altered (the words of every unit are as at baseline; section 3). PASS.
8. P4 addition: `Since the Ring`, `all these days`, `their Arbiters stopped and my fragments still worked`, `His Arbiter was dark before the line`, `whose plate lit eleven seconds late`: 0 hits in all eleven files. PASS.

## 6. Notes

- Mark counts (`B7-reconciled`): see the table appended below.
- The coordinator's override P4 says "the ten plan files"; there are eleven (BM, SL and nine packets), and all eleven were searched.
- Next fixed checkpoint: coordinator rulings on H1, H3, H9, H11, H12, then #52 before M3, #53 before M4, #54 and #55 before M9, #56 before M2 or M3 (Thornwater), #57 before M8-M9, #58 before M9.

## Appendix A. Full OLD and NEW lines of the protected units in section 2

Generated from `state/pre-B7-reconciliation/` and the current files. Each OLD/NEW pair is one whole line.

### A1. `BOOK_MAP.md` baseline line 364 to current line 366 — Tier A 17, pole two (#18)

OLD:

````text
17. **Pole two (S16):** Lira: "So the whole time they weren't afraid you'd break something. They were afraid you'd *exist*." Cael: "For five years I thought the system forgot to make room for me," … "It didn't forget. It was *built* so there'd be no room. Four hundred years of a whole world, so that I wouldn't happen." … "I happened anyway." / Lira: "Yeah." … "Now what." / Cael: "Now we find out how old the oldest one is. Karis has a bearing and the marks, and the records to read them against. There's a site at the end of the line that's been quiet since they built the machine." … "I want to stand in the middle of it."
````

NEW:

````text
17. **Pole two (S16):** Lira: "So the whole time they weren't afraid you'd break something. They were afraid you'd *exist*." Cael: "Since my Kindling I thought the system forgot to make room for me," … "It didn't forget. It was *built* so there'd be no room. Four hundred years of a whole world, so that I wouldn't happen." … "I happened anyway." / Lira: "Yeah." … "Now what." / Cael: "Now we find out how old the oldest one is. Karis has a bearing and the marks, and the records to read them against. There's a site at the end of the line that's been quiet since they built the machine." … "I want to stand in the middle of it." [B7-reconciled 2026-10-11: OWNER-pending #48]
````

### A2. `BOOK_MAP.md` baseline line 369 to current line 371 — Tier A 22, departures (#48)

OLD:

````text
22. **Departures (S24):** Teague: "Spring's over," / "Noted," / "Next spring." … "Whatever's on the next line. My crew comes." / Oryn: "The day I have to." / "Noted," / "Everybody says that." … "They'll carry. They'll hurt," … "Spring. Bring the map. Lie still when I say." / Seln: "Six. Six and no mule. Nothing behind. Nothing beside." / "West," Cael said. / "West," said Brom, and picked up the box. / "Twenty-nine tomorrow," / "Thirty's the month,"
````

NEW:

````text
22. **Departures (S24):** Teague: "The thaw's past," / "Noted," / "After the next thaw." … "Whatever's on the next line. My crew comes." / Oryn: "The day I have to." / "Noted," / "Everybody says that." … "They'll carry. They'll hurt," … "After the thaw: bring the map, and lie still when I say." / Seln: "Six. Six and no mule. Nothing behind. Nothing beside." / "West," Cael said. / "West," said Brom, and picked up the box. / "Twenty-nine tomorrow," / "Thirty's the month," [B7-reconciled 2026-10-11: OWNER-pending #48]
````

### A3. `BOOK_MAP.md` baseline line 389 to current line 391 — Tier C, Ch1 closing log and the 168th log (#18)

OLD:

````text
- **Ch1 closing log (270th):** "The ferry runs when the ice goes. Karis has a bearing, an index she can't read, and a language she can't read, and she says the answers are in a border archive nobody's opened since before the Compact. I've spent five years staying out of registries because a registry is where they file you. She wants me to walk into the oldest one on the continent. The kit reads everyone but me. So does the world, mostly. Nineteen. Ice goes next week. West, and inside, for the first time since the academy above Ostrand — which is a sentence I did not think I'd write again." And the 168th: "Claim: something. Evidence: a cord, two edges, a hair. Ruling: hold."
````

NEW:

````text
- **Ch1 closing log (270th):** "The ferry runs when the ice goes. Karis has a bearing, an index she can't read, and a language she can't read, and she says the answers are in a border archive nobody's opened since before the Compact. Since my Kindling I've stayed out of registries because a registry is where they file you. She wants me to walk into the oldest one on the continent. The kit reads everyone but me. So does the world, mostly. Nineteen. Ice goes next week. West, and inside, for the first time since the academy above Ostrand — which is a sentence I did not think I'd write again." [B7-reconciled 2026-10-11: OWNER-pending #48] And the 168th: "Claim: something. Evidence: a cord, two edges, a hair. Ruling: hold."
````

### A4. `BOOK_MAP.md` baseline line 400 to current line 402 — Tier C, S12 (#18)

OLD:

````text
- **S12:** "I put the wall in front of it anyway. I'd like that entered somewhere, since I'm not the one who keeps the ledger any more." / "It's entered," Log: "Eleventh. Iron Wall, from Vastin, in an alley, while he held a line for us with nothing behind him but the decision to. It's not Brom's — Brom gets harder, this holds. I've spent five years learning to give ground and disappear. Now I've got the opposite in me, from the man who spent forty years being the wall they put in front of people like me. He held it for us instead. I don't have a word for what that is. I wrote it down anyway."
````

NEW:

````text
- **S12:** "I put the wall in front of it anyway. I'd like that entered somewhere, since I'm not the one who keeps the ledger any more." / "It's entered," Log: "Eleventh. Iron Wall, from Vastin, in an alley, while he held a line for us with nothing behind him but the decision to. It's not Brom's — Brom gets harder, this holds. Since my Kindling I've learned to give ground and disappear. Now I've got the opposite in me, from the man who spent forty years being the wall they put in front of people like me. He held it for us instead. I don't have a word for what that is. I wrote it down anyway." [B7-reconciled 2026-10-11: OWNER-pending #48]
````

### A5. `BOOK_MAP.md` baseline line 403 to current line 405 — Tier C, S17 log (#48)

OLD:

````text
- **S17 log:** "Karis cracked the grade. The sites are ranked by age and the bearing runs oldest-last — somebody laid them out in order, and the order runs into the deep edge, toward the first one they ever made. Second-tier's the fourth site, the one the Compact fenced. Third-tier's out past it, on the line, quiet for centuries. Teague's crew came for spring like he said — ten of us now, and he's still better at this than I am, and the ledger still says so. Two crews, one bearing, and a straightedge my guardian sent me because my grandmother said a man who catalogues everything eventually needs to draw a line through it. Turns out she was right about the line. Turns out the line was already drawn four hundred years ago. We're just the first to follow it to the end." Also: "Two words," … "Both of them ours." / "Noted."
````

NEW:

````text
- **S17 log:** "Karis cracked the grade. The sites are ranked by age and the bearing runs oldest-last — somebody laid them out in order, and the order runs into the deep edge, toward the first one they ever made. Second-tier's the fourth site, the one the Compact fenced. Third-tier's out past it, on the line, quiet for centuries. Teague's crew came after the thaw like he said — ten of us now, and he's still better at this than I am, and the ledger still says so. Two crews, one bearing, and a straightedge my guardian sent me because my grandmother said a man who catalogues everything eventually needs to draw a line through it. Turns out she was right about the line. Turns out the line was already drawn four hundred years ago. We're just the first to follow it to the end." [B7-reconciled 2026-10-11: OWNER-pending #48] Also: "Two words," … "Both of them ours." / "Noted."
````

### A6. `BOOK_MAP.md` baseline line 380 to current line 382 — Tier B, Oryn (#48)

OLD:

````text
- Oryn (B7 Ch23): "Find me at Thornwater." / "Bring the map." Oryn's letter (B7 Ch24): "Route's whole. The knee held. Nobody died of three weeks. Spring: bring the map, and lie still when I say. — O." / "Six, by letter."
````

NEW:

````text
- Oryn (B7 edition `chapter-58.md:51–55`; `chapter-60.md:215,229`): `Find me at Thornwater.` / `Bring the map.` Her letter: `Route's whole. The knee held. Nobody died of three weeks. After the thaw: bring the map, and lie still when I say. — O.` / `Six, by letter.` [B7-reconciled 2026-10-11: OWNER-pending #48]
````

### A7. `BOOK_MAP.md` baseline line 382 to current line 384 — Tier B, Teague and Pike (#48)

OLD:

````text
- Teague (B7 Ch24): "Spring. Whatever's on that bearing. My crew comes." / "Noted." Pike (B7 Ch24): "I've kept this ledger thirty years. First time it's been wrong about a crew by being too small."
````

NEW:

````text
- Teague and Pike (B7 edition `chapter-59.md:199,221–225`): `After the thaw. Whatever's on that bearing. My crew comes.` / `Noted.` / `I've kept this ledger thirty years. First time it's been wrong about a crew by being too small.` [B7-reconciled 2026-10-11: OWNER-pending #48]
````

### A8. `packets/MOVEMENT-002.md` baseline line 28 to current line 31 — Karis callback (#48)

OLD:

````text
- **The long table** (midday). The Seln–Vastin doorway exchange, verbatim; these are their first words to each other. Vastin says the short thing: he resigned or walked out. Brom: "Three hundred miles is a demonstration." The layer: Karis supplies its existence ("Under every station on the continent. I said so at a table in the autumn"). Vastin's new fact: "Not *will not*. *Cannot.* There is no key." The name is a citation to a designer, and the trail ends at Treswick. Vastin then has nothing to do. Lira asks "Why us." Oryn notices the knee: "Then I still haven't asked." "What follows you": nothing that crosses the Line, and the Stair's rim "is not mine". Cael remembers the Book 6 sentence and says only, "Ask him the thing you want to ask him." Karis asks. **Close (verbatim).**
````

NEW:

````text
- **The long table** (midday). The Seln–Vastin doorway exchange, verbatim; these are their first words to each other. Vastin says the short thing: he resigned or walked out. Brom: "Three hundred miles is a demonstration." The layer: Karis supplies its existence ("Under every station on the continent. I said so at a table before we left Ostrand") [B7-reconciled 2026-10-11: OWNER-pending #48]. Vastin's new fact: "Not *will not*. *Cannot.* There is no key." The name is a citation to a designer, and the trail ends at Treswick. Vastin then has nothing to do. Lira asks "Why us." Oryn notices the knee: "Then I still haven't asked." "What follows you": nothing that crosses the Line, and the Stair's rim "is not mine". Cael remembers the Book 6 sentence and says only, "Ask him the thing you want to ask him." Karis asks. **Close (verbatim).**
````

### A9. `packets/MOVEMENT-008.md` baseline line 31 to current line 34 — Seln at the crest (#48)

OLD:

````text
- **The crest.** The watch-post: hut, fire, kit under a hide, two timbers, seven hoods, two crossbows, one low practitioner. "They knew." Seln: "That iron's been in the ground years. Not one winter." Teague: "Drawn?" Cael draws it. "Nobody declares. Nobody dies. They're seven people on a posting. Noted?" / Teague's **first "Noted."**
````

NEW:

````text
- **The crest.** The watch-post: hut, fire, kit under a hide, two timbers, seven hoods, two crossbows, one low practitioner. "They knew." Seln: "That iron's been in the ground years. Not one cold term." [B7-reconciled 2026-10-11: OWNER-pending #48] Teague: "Drawn?" Cael draws it. "Nobody declares. Nobody dies. They're seven people on a posting. Noted?" / Teague's **first "Noted."**
````

## Appendix B. Mark counts (occurrences)

| File | `B7-reconciled` | of which `OWNER-pending #48` | owner marks `[OWNER-pending #5x]` |
|---|---|---|---|
| `BOOK_MAP.md` | 61 | 10 | 18 |
| `STATE_LEDGER.md` | 32 | 0 | 1 |
| `packets/MOVEMENT-001.md` | 15 | 1 | 1 |
| `packets/MOVEMENT-002.md` | 4 | 1 | 0 |
| `packets/MOVEMENT-003.md` | 4 | 0 | 0 |
| `packets/MOVEMENT-004.md` | 1 | 0 | 0 |
| `packets/MOVEMENT-005.md` | 2 | 0 | 0 |
| `packets/MOVEMENT-006.md` | 1 | 0 | 0 |
| `packets/MOVEMENT-007.md` | 1 | 0 | 0 |
| `packets/MOVEMENT-008.md` | 5 | 1 | 0 |
| `packets/MOVEMENT-009.md` | 4 | 2 | 4 |
| total | 130 | 15 | 24 |

## 6. Coordinator rulings on the held and open items (Claude Opus 5.5, 2026-10-11)

Marked inline `[B7-reconciled 2026-10-11: coordinator ruling]`.

- **H1:** the Vastin (B6) Tier B bullet stays, verbatim. Confirmed.
- **H2, H4–H8, H10, H14–H20:** accepted as applied.
- **H3 — restored.** BOOK_MAP's Compact bullet again says the Compact has reached across the Line twice (on paper; in person on the Stair's rim), that the asset-restriction is pending, and that Vastin is still inside, writing nothing. STATE_LEDGER again carries "He does not know: …" including that instruments will read wrong in his hands, discovered on the 168th (Book 7 ends with them reading true), the faction's two reaches, and Vastin's Book 6 sentence. NOT restored: "Karis's sub-layer… since Ostrand" and "the carvings command rather than describe" as Karis's knowledge at entry — neither is on the page in the edition's Books 6–7.
- **H9:** MOVEMENT-009's "1,012 across" is now "about 1,107 yards across" (#48), matching BOOK_MAP.
- **H11:** the working inventory no longer says "Ember, never used" or "Storm asleep" (both were used in Book 7); "Anchor used both ways" stands (once each way). BOOK_MAP's lock about Oryn reading Cael is annotated with the edition's actual readings rather than rewritten.
- **H12:** "cache" stays. It is the edition's own word for the contents of Seln's case (Book 6).
- **H13:** the spine's "The name is said once." carries `[OWNER-pending #54]` where the phrase stands.

**Release:** Book 7 is locked. Book 8 Movement 1 is released for no-source drafting. Owner items: #52 before Movement 3; #53 before Movement 4; #56 where Thornwater falls; #54, #55, #57 and #58 before Movements 8–9. Each protected line stays word for word under its default until the owner rules.
