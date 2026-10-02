# Repair brief — Book 1, Movement 2 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context;
the cold read is manuscript-only). Both would keep reading; the Renn bout's reveal discipline
is the movement's strongest work. No verified canon violation; Reader Standard passes; source
reuse 0. Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place.

**Rulings on your three flagged choices — all accepted:** Cael stays out of Vell's ledger
until Darrow; the cart is written as bare fact, uncounted, and Renn's third exchange stays
unexamined; "Secondweek" stands. (The conditions they create for Movements 3–9 have been
written into those packets.)

**Protect:** every exchange of the Renn bout (do not shorten any); Vell's ch13 cutaway whole;
"Nearly all of it… two things in the corner"; "Find out what it costs her"; Lira's "eleven
minutes"; the bridge and the board in ch8; every protected line in BOOK_MAP §7.

## Priority 1 — Say it once at chapter ends, and give one ch8 set piece a consequence

- End-of-chapter recaps restate what the reader has just watched: ch13's walk home re-lists
  Renn's tells Cael has already said aloud (the debut is told four times after "Match."); the
  ch11 night read-back; the ch9 closing entry. Cut each to the one item that is still
  unsorted. About 500–700 words come out, which also pays most of the 7% overage.
- Ch8's three street set pieces (the mangle-mender, the old man, the answer-seller) share one
  shape — watch, epigram, leave — and none pays inside the movement. Tighten one of them, and
  give another a small live consequence later in the movement (ch12 is the natural place).

## Priority 2 — Set the decision to fight against the rules it breaks; signpost the POV turns

- Cael's decision to fight breaks two rules the reader has heard: his own rise entry ("Show
  nobody anything… Find work") and Hesk's Tier B "Don't let anyone see you move" (placed in
  Movement 1, ch3). Neither is recalled. Give it three to six sentences in the ch11 night
  scene, and one clause in ch13 after three people have seen him move. Do not coin or
  pre-echo the later "being seen" line (that belongs to Hesk's letter, Movement 9).
- The POV handoffs (to Hesk at ch10's open, back to Cael mid-chapter; to Vell mid-ch13) are
  marked only by a rule and a first sentence. Signpost each in its first line (a name and a
  place, early). Do not split chapters (it would renumber the book). Cut nothing from either
  cutaway.
- Line strains: drop the year count in Lira's "second year / fourth-year" academy arithmetic
  (it fights Kindling at fourteen); "Book said one" in Vell's cutaway reads as her own
  ledger — make it Marrow's book or the slate; restore the Tier B exchange "You almost had
  him in the second exchange." / "I wasn't trying to win. I was trying to learn how he
  moves." / "Oh. That's actually smarter." so no tag falls inside a protected line (tags may
  sit before or after it); keep Lira's lodging unspecified.

## Priority 3 — Rhythm and breaks

Measured: mean 13.16 but median 8 (bimodal); ≤5-word share 34.5% (~28%); ≥40-word 5.1%
(3.3%); 719 words per scene, 45 breaks (~950); paragraph median 24 (~18); ~92 tags per 10k.
Remove the five section rules inside the Renn bout (it is one continuous contest) and merge
six to eight more breaks in ch8 and ch10. Join clipped narrative runs in ch8 and ch10 only;
leave dialogue and the hits' short beats alone. Bring a few of the longest sentences back
under forty words where they carry two thoughts. Shorten the longest paragraphs.

**Length.** Finish within 35,000–37,000 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-01-the-shattered 2` (must stay at 0
unprotected) and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the seven chapters,
then append "## Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, overlap summary,
changelist by chapter). Edit only the seven chapter files and AUTHOR-REPORT.md.
