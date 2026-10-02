# Repair brief — Book 3, Movement 2 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context;
the cold read is manuscript-only). Both would keep reading — the cold reader would go
"straight into chapter 17". Reader Standard passes; source reuse 0; protected lines verbatim.
Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading
(no scripted splitting).

**Rulings on your six flagged choices — all accepted:** Coss first meets Cael at the
Ardenmere summons (the current edition's "Denvash intake" line is a source conflict; the
edition follows Book 1); ~80% Cael in this movement is fine (87/13 is book-level); Karis's
[Drawn Channel] stands (pending owner); *Insubordination* is canon; "shall" vs Movement 1's
"should" needs no change (reported speech); Hobb thanked here is fine. "Master Marlowe" is
existing canon (Ternhall lecturer).

**Protect:** the "questions I will not ask" page; the Arbiter-station family; Prynn's "You
read *shall*"; the bout; every protected line; the Karis and Coss cutaways' handoffs.

## Priority 1 — Continuity and two knowledge slips (phrase-level)

- **Karis's calendar** (ch9, ch11, ch13): the seasons do not add up — "late winter" → four
  months → "spent a winter" → the Reydan result "at the start of the summer" → "all winter";
  ch11 says "middle of last winter"; ch13 calls the Iron Eight bout "a few weeks ago". The
  Reydan bout was days before this book (BOOK_MAP §1). Conform every anchor to one calendar.
- **Ch16 knowledge breach:** Karis says she timed Cael "at the sittings, from what you told
  the panel" — she never saw a closed sitting (ch14 has her outside the door; session one
  had no strikes). One or two sentences: she times him from something she did see.
- **Word slips:** ch9 "Iron Skin crest"; ch16 "four times"; ch13 "ran the Ironyard" — check
  each against canon and the movement's own facts (see the editorial review for the exact
  correction).

## Priority 2 — Reveal discipline, and the two places the movement sags

- **Ch16, "There isn't one to hide."** Cael says it to Oona with the crowd still at his back,
  which reverses his public guard from ch8 without the page or the ledger registering it.
  Choose one: (a) make the crowd's hearing it a moment on the page, with its cost, and report
  it in AUTHOR-REPORT as state for Movement 3; or (b) ring the bell earlier so the exchange is
  Oona's alone. (b) is the lighter touch and keeps the guard intact; (a) is acceptable if the
  scene earns it.
- **Ch9's opening:** Karis's retrospective runs ~2,000 words of summary before her POV gets a
  scene. Trim the research block by about a quarter and reach a scene sooner.
- **Ch14, the quiet week** (the movement's one sagging chapter): keep one routing-code
  consultation (Prynn's) and join the two archive visits; drop one of the three reassurance
  talks and the duplicated "shoulders came down" beat.
- **Tics:** "a long moment" (×10) and "exactly as" (×12) — keep two of each, at most.

## Priority 3 — Rhythm (by reading)

Measured: mean 14.0 (good); paragraph median 27 (~18); ≥40-word 5.2% (~3.3%); 796 words per
scene, 39 breaks (~950) — the surplus breaks are ch14's seven (661 words/scene). The long
paragraphs and long sentences live mostly in the ch9 Karis and ch13 Coss cutaways: break the
longest paragraphs where the thought turns, and bring some forty-plus sentences under forty
where they carry two thoughts. Merge ch14's breaks as you join its scenes. Touch no dialogue,
not the bout.

**Length.** Budget ~39,000; the draft is 37,514. Finish within 36,000–39,500 — the Priority 2
trims may be partly spent on the scene ch9 reaches sooner.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-03-no-path-given 2` (must stay 0
unprotected) and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the eight chapters,
then append "## Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, overlap summary, which
option you chose for the Oona line and its state consequence, changelist by chapter). Edit only
the eight chapter files and AUTHOR-REPORT.md.
