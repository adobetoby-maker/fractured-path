# Repair brief — Book 3, Movement 4 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the
cold read is manuscript-only). Both would keep reading "without hesitation"; the high-water marks
are chapter 24's one sheet and chapter 27's "Correctly"; Gerda is the movement's surprise. No canon
violation (P8, P9 and "real, unexplained, keep" verbatim; the Tide anomaly handled within limits;
no "directed"; Karis has never seen the binder); Reader Standard passes; overlap 0. The restart
seam (ch27→28) is clean; the day-count errors fall in the resumed chapters. Pre-repair text is
frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

**Rulings on your seven flagged items — all accepted:** "more than two" told to Karis (and the
stakes hypothesis withheld — Book 4 ch9 requires it); the nulls as invited watching off every
record; Gerda's arc closed here; the twenty-two nulls from week 9 with "We are missing a
condition" at session 22; only Quenna's note (the proposal is week 12); Wray's ceiling-curve
redraw; the Lira cutaway at ~3,630 words — do not pad it.

**Protect:** chapter 24's one sheet; chapter 27's "Correctly"; Gerda's arc; the tells paragraph
in ch28 as that chapter's destination; the ch29 wall statement of the hypothesis and the
session-22 silence; Quenna's note; Karis's "I want it to be me"; every protected line.

## Priority 1 — Chronology and line fixes (resumed chapters first)

- Ch28 ¶1 calls week 10 "the first week of the nulls" — it is the second.
- Week 10 shows ten sessions against "nearly every day… two of the days two" — make the count
  and the description agree.
- Session 16 has no day (15 is Tuesday night, 17 Wednesday dawn) — give it one.
- The fast catch is narrated in ch30 on Monday night *after* ch29 has shown a Tuesday and a
  Wednesday with no aftermath — move it to Wednesday night, with the bad supervised session on
  Thursday. Ch30's backtrack to "the Tuesday session" after ch29's Wednesday session 17 goes too.
- Ch25: the first quiet-room session runs at "sixth bell" before the terms are written "that
  evening" — fix the order (a two-word date fix).
- Ch31: Oona's "a little under seven weeks" → six.
- [Drawn Channel] is laid "along the air" — the declaration says "along any surface"; fix it.
- Prynn certifies outside her stated afternoons — fix the time or the afternoon.
- Small unrecovered referents a returning reader trips on: "the refusal and the stranger's
  note", "the covenant", the first arrangement's clause numbers — a few words each to recover
  them.

## Priority 2 — Say the hypothesis twice, open ch28 inside a session, give Lira's feeling words

- **Ch28's opening** (sessions 5–10 as a variable list; sessions 13–14 never placed) is the one
  place both reader lenses put the book down. Open inside a session; compress the catalogue to a
  binder margin; place 13–14 in a line; keep the tells paragraph as the chapter's destination.
- **The withheld hypothesis** is restated four times in near-identical words (ch29 wall, ch29
  session 16, ch31 session 22, ch31 wall), and the final binder entry reprises ch29 verbatim, so
  the movement ends on recap rather than on Quenna's note and Karis's "I want it to be me". Keep
  the ch29 wall and the session-22 silence as the two load-bearing statements; trim the rest so
  the movement ends on the note and Karis's line.
- **Lira's three elided speeches** (ch27 §4, ch28 §3, ch30 §1–2) read together as a feeling the
  edition does not let her name, and "not repeatable… with second-years near it" implies language
  a thirteen-year-old's book must not carry. Give one of the three its actual content, in her
  words; change "not repeatable" to "sharp".
- **Progression vocabulary** (27 per 10k against ~42 planned): add terms only where a speaker or
  a record would really use them — Karis's ledger headers, Quenna's record lines, the two end logs.
  About 33–35 per 10k is honest; do not force more.

## Priority 3 — Long sentences, by reading

The ≥40-word share is 6.7% against a 2.5–4.5% range. It clusters in ch24 §2–4 (Lira's reflective
paragraphs, which also drift out of her register into Cael's), ch25 §4–5, ch26 §1 and §4–5, ch28
§1 and §6, ch31 §2; ch30–31 need little. Split by reading at the natural joint, and keep Lira's
paragraphs in her own register. Keep sentence mean and words per scene in range (now 13.87 and
854).

**Length.** Finish within 36,000–38,500 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-03-no-path-given 4` (must stay 0 unprotected)
and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the eight chapters, then append "##
Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, overlap summary, the null calendar day by
day for weeks 9–11, which Lira speech you gave content to, changelist by chapter). Edit only the
eight chapter files and AUTHOR-REPORT.md.
