# Book 3 — line and listening proof: running notes

Reader: Codex (Sol seat), 2026-10-04. Scope: `manuscript/chapter-01.md` … `chapter-61.md`, read in order for Breeze TTS: one segment per paragraph, scene breaks as long pauses, italics stripped, and fenced blocks flattened one line at a time.

**Manuscript files are read-only for this pass.** Proposed changes belong only in `listening-proof.md` after an exact single-match check and a protected-wording check.

## Governing material read

- Book 1 `listening-proof.md` (structure and judgment model)
- `COMPLETION-PLAN.md`; Lane A, Lane B, Lane 1, and Lane 2 reports
- `EDITION_BRIEF.md` (Reader Standard and audio-first rule)
- `OWNER-DECISIONS.md` #29 and #33
- `BOOK_MAP.md` §9.1–9.2; `protected-patterns.txt`
- `audio/fpaudio.py`
- Book Narrator 1.2.5-CI skill and its complete workflow

## Mechanical baseline before the sequential read

- 61 chapter files; 287,943 whitespace-counted words.
- Straight quotes: two odd-count paragraphs only, ch21 line 203 and ch59 line 9. Both are openings of legitimate multi-paragraph speeches; the final paragraph of each speech closes the quote.
- Curly quotes: 0. Odd asterisk paragraphs: 0. Underscores: 0.
- Scene breaks with missing blank-line padding: 0.
- Lower-case prose paragraph starts: 0.
- Fenced blocks: three (ch1 Compression notice, ch11 Drawn Channel declaration, ch36 Ember notice), six fence lines total.
- Paragraphs over 700 flattened characters: 181 (inventory to be reproduced in the final proof; length alone is not a defect).
- Initial doubled-token scan: seven grammatical/intentional forms (`that that`, five `had had`, `predecessor's predecessor's`) and one aloud stumble in ch49: `carried it in in three tied stacks`.
- Abbreviation search: no `D1`, `D6`, `wk`, `Cu`, `Br`, or `R1`–`R6` manuscript occurrences. Numeral-bearing prose/log lines remain to be judged in context.

## Sequential reading log

| Chapters | Status | Notes |
|---|---|---|
| 01–08 | complete | Academy arrival, first suppers, sittings, and training exchanges clear aloud. Vell/Velmere and Wray/Greyvane remain distinguishable by grammar and role. |
| 09–20 | complete | Karis introduction, archive/table conversations, notices, assessments, and Edran sequence clear. No unattributed speaker changes. |
| 21–31 | complete | ch21 odd quote is a legitimate continued Karis speech. Agreement, binder, ring, and multi-voice meal scenes remain attributable. |
| 32–41 | complete | Match preparation, unbroken ch36 match, system notice, Log/binder entries, and aftermath checked after italic stripping. |
| 42–53 | complete | Warden arrival, archive casework, deposition, case-building suppers, and hearing-eve scenes clear. One true doubled-word stumble in ch49. |
| 54–59 | complete; second pass complete | Hearing speaker-attribution pass complete. ch59 odd quote is the legitimate opening of the continued ruling. The recorder dashes are record notation, not spoken punctuation. |
| 60–61 | complete | Closing suppers/table talk, logs, correspondence, and final four-person wall scene clear aloud. |

## Resolved findings

1. ch49: `the Warden's aide had carried it in in three tied stacks and gone away again.` is a true oral stumble. Proposed replacement: `the Warden's aide had brought it in three tied stacks and gone away again.` The old string occurs exactly once and is not protected.

## End-state checks

- Quote balance: no defects. The only paragraph-local odd counts are the two valid continued quotations in ch21 and ch59.
- Speaker attribution: no text fixes required, including ch54–59 and the recurring four-person suppers. Hearing questions are anchored by role, address, or response; the ruling is unmistakably Yorlan's quoted record.
- Ear collisions: no Coss/Doss, Karis/Kestrel, or Havel/Halvern co-presence. Doss, Kestrel, and Halvern do not occur in Book 3. Vell/Velmere and Wray/Greyvane do co-occur, but remain clear without renaming or prose repair. The remaining requested names are separated by role, syntax, and scene.
- Homographs: `wound` is always WOWND; `lead` is LEED throughout; ch23 `bow` is BOH (weapon), ch59 `bow` is BAU (gesture). `read`, `record`, and `live` resolve from grammar. No text fix required.
- `as` audit: temporal uses remain intelligible as temporal; manner/comparison uses do not create false simultaneity after the texture-pass conversions. No text fix required.
- Formatting: all `---` breaks are padded correctly. Three fenced notices need direction handling. Italic Log, binder, charter, and record passages remain intelligible when asterisks are stripped. `[SHATTERED]` occurs in the protected ch59 ruling and must be voiced without brackets.
- Numerals: `41-7843-V` needs digit-by-digit direction. Ranks, clause numbers, bell/week counts, box counts, and the ch21 numeric drill are clear when read as words. No manuscript occurrences of D1, D6, wk, Cu, Br, or R1–R6.
- Broken joins/typos: no lower-case paragraph starts, clipped joins, stray Markdown, doubled spaces, tabs, or punctuation collisions. The ch49 duplicate `in` is the sole required text repair.
- Protected wording: all Book 3 protected lines and protected-pattern candidates were checked and left untouched.
