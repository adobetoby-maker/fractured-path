# Book 7 — Void Roads: Reader Standard audit (Gate 27, retroactive)

Owner requirement recorded 2026-09-05 (craft/VOICE_CHARTER.md "Reader Standard"; craft/THE_AUTHOR.md Gate 27): written for a thirteen-year-old reader — clean language, moral goodness, violence with cost and no gore, no sexual content. Binary; FAIL on any single violation. Book 7's 24 chapters were closed on 2026-09-04, before the gate existed, so the gate is applied here retroactively to the spliced manuscript (`books/book-07-void-roads/chapters/chapter-01.md` … `chapter-24.md`, 118,360 words).

Audited 2026-09-05.

## 1. The loop gate (banned-word grep, must be 0)

`loop.sh gates` word list (`damn|damned|hell|bastard|bitch|shit|fuck*|piss*|arse|ass|crap|bloody|goddamn|christ|whore|slut|cock|bugger|sod`, whole words, case-insensitive) run over all 24 spliced chapters: **0 hits in every chapter.**

Wider sweeps, also 0 or cleared: soft oaths and swearing-as-narration (`swore|swearing|cursed|curse|oath|gods|god|devil|blast|confound|bleeding|sodding|hells`) — the only two hits are "bleeding" in Ch11 in the literal wound sense; sexual/romance markers (`kiss|naked|breast|bed with|lover|lust`) — 0; gore markers (`gore|entrails|guts|viscera|brains|gushed|spurted`) — 0.

## 2. Fresh-context read (the qualitative clauses)

Three fresh-context Opus editor seats read the manuscript in full, eight chapters each, against the standard's four clauses, with instructions to be strict on language / conduct / violence / sexual content and generous on dry humor, hard bargaining, fights that carry cost, clinical injury description, and wrong that the page names as wrong. Reports: `reader-standard-part1.md` (ch01–08), `reader-standard-part2.md` (ch09–16), `reader-standard-part3.md` (ch17–24).

| Part | Chapters | PASS | FAIL | VIOLATION | WATCH |
|---|---|---|---|---|---|
| 1 | 01–08 | 8 | 0 | 0 | 5 |
| 2 | 09–16 | 8 | 0 | 0 | 6 |
| 3 | 17–24 | 8 | 0 | 0 | 4 |
| **Book** | **01–24** | **24** | **0** | **0** | **15** |

**Verdict: Book 7 PASSES Gate 27 — 24/24 chapters, zero violations.** No prose was changed by this audit.

## 3. The WATCH notes (recorded, none actioned)

All fifteen are the readers' "closest approach" notes — each cleared on the page, none a violation. Kept here so a later pass or the audiobook read-through knows where the hardest moments sit:

- Ch02:125 — "heresy" figurative/institutional, no deity invoked (language).
- Ch03:53 — the ford witness's account: a death at one remove ("buried in pieces"), and "got his hand across his own throat somehow" — the healer binds him and he lives; a young reader could momentarily misread the second as self-inflicted. **Clarity candidate** for a later line pass, not a violation.
- Ch06:125 — field-setting of a broken leg, pain by action not description (violence).
- Ch10:215 — den remains, one clause, animal (violence). Ch10:231 — the withheld-truth thread opens and is named as a debt in Cael's own hand (conduct).
- Ch11:53 — the blade into the stillhound behind the ear, flat and functional, cost immediate (violence). Ch11:67 — "what was coming out of it" refuses to name blood (violence).
- Ch13:73 / :83 — Cael reads Oryn knowing she cannot consent to what she cannot know; the wrong is named as wrong by him and by three others, and he names his own cowardice as the real reason (conduct — the reason it passes).
- Ch19:165 — bolt-head cut from the shaft and the shaft drawn back, in the healer's clinical register, cost on the page (violence).
- Ch20:135 — the crew keeps the recovered kit and ledger while refusing the three hundred; the reasoning is argued on the page (conduct).
- Ch21:127 — Brom's mark gone dark through the coat: the one place blood is on the page in part 3, two clauses, stakes only (violence).
- Ch22:61 — the wrist read, consent asked and granted, diagnostic register throughout (sexual — cleared).

## 4. Seat note

The Sol editor seat (gpt-5.6-sol via `codex exec`) was unavailable for this audit — `codex login status` reports "Not logged in" and the ChatGPT-plan OAuth flow cannot be run non-interactively — so the read was done on the Opus fallback seat named in the penname-editor skill, the same seat the peer session used to close Ch21–24 and to run the seams, checkpoint and secrets audits on 2026-09-04.
