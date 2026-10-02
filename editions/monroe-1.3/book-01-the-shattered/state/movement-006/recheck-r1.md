# Recheck r1 — Book 1, Movement 6 (chapters 34–40)

Seat: review (Claude Fable 5.1), targeted recheck of the author's Repair r1 (Claude Opus 5.5, 2026-10-02).
Scope: the brief's findings and the changed joins only. Every changed region was located by `diff` against
`pre-repair/` and read with its surrounding text; the seven repaired chapters were then read in full.
Tools rerun: `ed.sh overlap book-01-the-shattered 6`, `ed.sh gates book-01-the-shattered 6`,
`formula_metrics.py` on the seven chapters.

## Verdict: CLOSE WITH LINE FIXES

Three required line fixes (one broken quotation mark, one count the repair introduced, one callback the
repair pointed at the wrong place) and one optional. No unresolved concrete defect remains that needs the
author back in the text. No second repair.

---

## (a) Brief items

### Priority 1 — counts and line fixes

| Item | Status | Location / evidence |
|---|---|---|
| ch38 "fought four times" → three | RESOLVED | ch38:91 "In twenty-two days he had fought three times" (kiln boy, Renn, Sarel). |
| ch38 "two weeks ago" → three weeks | RESOLVED | ch38:7 "three weeks ago"; agrees with ch37:33, ch37:381, ch38:101. |
| ch38 "a week since Sarel" on a Thursday → four days | RESOLVED | ch38:219 "It's four days since Sarel" (Sarel Sunday, Vell's table Thursday). |
| ch36 "never heard of the yard" → never seen | RESOLVED | ch36:9 "He had never seen Dessa, or the yard." |
| ch34 "wrote down later" vs nameless Log entry | RESOLVED | ch34:225 "which Cael heard and did not keep"; ch34:287 "*The kiln boy (I didn't keep his name)*". |
| Log Seventh/Eighth vs ledger "five bouts" / "three of seven" | RESOLVED | ch34:285 "the seventh entry in the Log and only his sixth bout, because the Log had counted Baro, whom he had only watched, and Vell's book counted nothing it had not seen fought." Verified against the Log itself: *1. Renn* (ch14), *2. Brenna* (ch15), *3. Baro … Watched* (ch15), *4. Amrit* (ch16), *5. Petra* (ch17), *6. Dessa* (ch26) — six entries, five fought, one win. ch36:235 "three of seven in this book now, and two of them inside a week" = ledger 5 + kiln boy + Renn, wins Dessa/kiln boy/Renn, the last two on day 7 and day 12. ch40:239 Seventh–Twelfth, "Four wins and two losses. Six bouts in six weeks"; ch40:353 "Six bouts in them, four won." All agree. |
| Corbin's fifth: one clause placing the turned shield arm before "Cael was inside" | RESOLVED | ch40:141 "To cut across to his right he had turned a quarter away from the boy, and his left arm, the shield arm, had gone round with him across the front of his own body." precedes ch40:143 "Cael was inside." |

### Priority 2 — say it once; make Talis a search

| Item | Status | Location / evidence |
|---|---|---|
| Hesk cutaway: cut one of three Dessa-letter readings | RESOLVED | ch36:5–15: one fast reading in the doorway, one slow reading at the bench with the file; the kitchen-table third reading is gone. "Very slightly too neat" kept (ch36:17). |
| Don't quote the fear paragraph in ch36 | RESOLVED | ch36:215 "wrote down the step in the street, and the week-late fear, in four sentences" — referred to, not quoted. (But see new defect D2: the paragraph ch39 quotes has six sentences.) |
| Each letter passage once, where it lands hardest | RESOLVED | "A win you built…" only at ch35:205 (ch36 now "wrote one line about building"). Fear paragraph only at ch39:53/57. Joren's heels only ch39:73; Alis's basins only ch39:75 (ch36:217 "put in Joren's heels and Alis's basins"). Pre-repair had each twice; grep confirms once now. |
| Cutaway length (~5,100 against ~3,000) | PARTIAL | Now about 4,490 by the author's count. The brief's concrete cuts are made; the remaining length is Joren's fifty minutes, Alis's four washings and the review, which the brief did not ask to cut. The author has flagged the M8 allocation as a coordinator planning note. Not a defect for a second repair. |
| Aftermath refrains: keep Renn, differentiate Sarel and Corbin | RESOLVED | Renn keeps "could not find his breath anywhere. / He found it." (ch35:333–335), "not biting them" (ch35:339), "took two tries" (ch35:399). Sarel: ch37:185 "old pain woken up, the kind that knows the way … counting his breaths in, one, two, until there were enough of them to stand on"; ch37:189 Lira "saying something, the same few words over and over … probably been *chin in*". Corbin: ch40:107 arms folded across her chest (but see D3 — the callback's location is wrong). grep: no "knuckle"/"breath anywhere"/"tries" refrain survives outside the Renn instance. |
| Sarel's look copies Renn's | RESOLVED | ch37:149 "looking at the empty dirt around him, the whole ring of it … the way a scaffold walker looks at the boards she has left to stand on" — her own, and it sets up the fourth exchange's "made the place small". |
| Talis bout as a search | RESOLVED | ch38:243–267. (1) shoulders: "The shoulders told the truth about a strike he never threw … *Not the shoulders.*" (2) hands: "*The hands come last. Everything's already decided by the time the hands know about it.*" (3) face/temper, provoked on purpose: "*Not the face. Not the temper.* He had gone down the whole of Talis from the shoulders to the belt, the way you go down a column, and every line was empty." (4) "watched everything at once, and it made no difference" → the beam-end strike. The search order follows the Log list at ch38:231. The cheek-on-the-dirt discovery (ch38:269–285) and Lira's stake (ch38:291–305) are unchanged. Length kept: ch38 6,106 → 6,075. |
| Light trims: ch38 board re-narration; ch39 montage; ch40 roll-call | RESOLVED | ch38:5–13 (board section compressed; Lira's own view, the desk and the skewer woman kept). ch39:91 (drain crust, wheezing man, Doss's pipe, post-to-the-right gone; no later line in M6 depends on them — "Doss" has 0 hits in ch34–40). ch40:7 (Dellin and Brenna cut from the rope; Renn and Dessa kept; Renn's later shout at ch40:187 and Dessa's bench at ch40:183 still land). |
| Total trim ~1,500–2,000 | PARTIAL (not a defect) | Net 45,021 → 43,937 = 1,084 by the tool, because Priority 3 added connective tissue and long sentences. Final length 43,937 is inside the 42,500–44,500 window. |

### Priority 3 — rhythm

RESOLVED. Rerun of `formula_metrics.py`: words 43,937; sentence mean 13.27 (range 13–15.5); ≥40-word share 4.2%
(range 2.5–4.5); words per scene 896.7 (42 breaks). Speech, Log entries and the fights' landing beats are as they were
(checked in every bout). Reporting verbs 509 → 424 by the author's grep; tags were dropped only where the paragraph
already names the speaker — I found no line whose speaker became unclear.

---

## (b) Bouts, the Talis search, the aftermaths

Every decisive exchange is intact; none has a cut inside it.

| Bout | Decisive exchange | Lines | Change inside it |
|---|---|---|---|
| Kiln boy | third | ch34:239–245 | two sentence joins in narration; the beat ("stopped it with his knuckles touching the boy's jaw") unchanged. |
| Renn | fifth | ch35:349–377 | none. The five problems (from the mark / false heel / sweep / figure-thrown-left / front heel) all stand, and the front-heel discovery at ch35:343–347 is untouched. |
| Sarel | sixth (and the collapse of the method at ch37:113–121, the third's moving, the fourth's "made the place small") | ch37:193–201 | none. |
| Talis | fourth | ch38:267–271 | rewritten as asked; the landing ("cheek against the dirt and every bit of air gone") unchanged. |
| Dellin | fourth | ch39:255–271 | none; the scene break after "Called" was removed and the aftermath follows cleanly. |
| Corbin | fifth, truth/lie/truth | ch40:133–163 | one clause added before "Cael was inside" (asked for). The hand going up and "Conceded" unchanged. |

The Talis bout now reads as a search: each exchange opens with where he looks, the exchange empties that place, and the
italic rulings cross it off, so that the ground answering from his cheekbone lands as the one place he never looked.

The aftermath passages no longer repeat each other: Renn (breath found, two tries, knuckles not bitten), Sarel (old pain
knowing the way, breaths counted, Lira's mouth saying *chin in*), Corbin (arms folded as if cold). Each is now its own.

---

## (c) Joins, merges, splits

**Defect, must fix — ch37:63, a stray quotation mark splits Lira's line in two.**
`Lira turned her head and looked at him at last. "Then you'll have found that. "That's still something. Go on."`
The second `"` before `That's` opens a quotation that is never closed as intended; as printed the line reads as two
fragments. Fix below (F1).

Merges, checked and sound:

- ch35:41 "Vell said Sunday, an hour later, at her table." — the quay scene runs straight into Vell's table. Renn had
  just said "Ten o'clock. I'll be at her table with my hair combed", so the hour, the combed hair and the half-shaved
  beard follow; speakers in the table exchange are all tagged. Clean.
- ch39:43–45 Yeni goes down the stairs → "Hesk's letter had come on the Friday…" with no break. "He took it out now, on
  the cot" carries him back from the floor without a seam. Clean.
- ch39:271–273 "Called … Unrated." → "For a moment the yard did not seem sure what it had seen." Clean.
- ch36:5–15 the two-reading cutaway: "read it again, with Ressa's oven hinge in the vice … a stroke of the file for
  every line" and later "on that second reading, slower, with the file going" agree. The truncated quotation
  "*In the third I went into it,*" matches the Dessa letter at ch27:85–87 word for word. Clean.

Joins that make a new claim, verified against the book:

- ch34:9 "a more senior man came along the merchant road with a thin file" — matches ch33's "a person more senior than
  Coss would come out along the merchant road … with a file that was too thin". Clean.
- ch37:247 "It was what she had said after Petra, counting, every time one more." — ch17:225 has Vell after Petra:
  "Four … Five. Six. Seven … Every time one more." Correct (Amrit rightly dropped).
- ch38:5 "the three charcoal strokes beside it" — established at ch33:199. Clean.
- ch36:213 "and what *remain on the book* meant" — the referent is the reviewing officer's "The matter will remain on
  the book" / "On the book. Open." at ch36:195–199, two paragraphs above. Readable; ch39:47 restates it. No fix.
- ch39:145 "going back through the Log, where the entries were, a Thursday and a Sunday in the third week, among the
  bouts he wrote down" — a little clotted, but the meaning is intact. No fix required.

No fragment, no speaker separated from a line, and no sentence that changed meaning was found beyond F1.

---

## (d) New defects introduced by the repair

**D1 (= F1)** ch37:63 broken quotation, above.

**D2 — ch36:215 "in four sentences" against the paragraph ch39 quotes.** The repair replaced the quoted fear paragraph
with a count. The paragraph as printed at ch39:53 and ch39:57 is six sentences ("When your letter came…"; "It was all
over by then."; "You had already done it…"; "It made no difference."; "That's the post…"; "But you asked me once…").
A reader who counts, in a book that counts, trips. Fix F2.

**D3 — ch40:107 callback points at the wrong place.** "the way she had stood at the board on the morning she heard his
whole name, as if she were cold all at once." The morning she heard his whole name is ch29:161–171, at the post in the
yard ("She stood in the frost … took her hands out of her pockets and folded her arms instead, tightly, as though she
were cold all at once"). She was not at the board; the ch33 board scene is Cael alone, and she arrives at its end. The
gesture and "cold all at once" are right; the location is a dangling referent. Fix F3.

**D4 (minor, optional) — a new echo of the kind the brief was repairing.** ch38:263 (new) "felt it all the way to his
teeth" against ch40:83 (pre-existing) "he felt it all the way up into his teeth", eleven days apart in story time and
two chapters apart on the page. Fix F4 if wanted; the overlap tool does not see it (under ten words).

Counts, otherwise: all agree. Day ladder from ch37:21 (Saturday = eighteenth morning since the board) gives board
morning Wednesday day 1; kiln boy Tuesday day 7; Renn Sunday 12; Sarel Sunday 19; Lira's room Wednesday 22
("twenty-two days spent, and twenty left"); rule morning and Talis watched Thursday 23 ("four days since Sarel");
Talis Sunday 26 ("Wednesday, four days ago" in ch39:67); Dellin Thursday 30; Corbin Thursday 37 ("eleven days ago"
for Talis); letter Saturday 39 ("thirty-ninth night"); assessed-Copper Tuesday 42 ("the forty-second day"). Weeks: "three
weeks ago" for the Brenna bout from day 22 and from the rule morning is consistent across ch37/ch38/ch39. Log entries
vs ledger bouts: see Priority 1 above. Hesk letter passages: each once.

Protected wording: the `FRAGMENT ACQUIRED` block at ch40:256–258 is byte-identical to pre-repair and to BOOK_MAP §7
(em dash, spacing, "Tier equivalent: unknown."). "mine are mine" ×3 (ch38:135, ch40:291, ch40:425) and "It was five."
(ch40:371) exact. "Statute 14, Section 9" (ch36:161) exact. No other §7 Tier A/B string lives in chapters 34–40, and
none did pre-repair (both trees grepped). The italic report-voice tallies and "You *ruled*" are unchanged.

Reader Standard: `ed.sh gates` rerun — reader_standard=0, metadata=0, modern=0 on all seven chapters.
Source reuse: `ed.sh overlap` rerun — 0 unprotected shared runs of ≥10 words; 0 protected runs.

---

## (e) Second repair?

Not warranted. The brief's concrete items are resolved; the two PARTIALs (cutaway length, gross trim figure) are
planning notes, not defects in the text. The three real defects (D1–D3) are single-line and are fully specified below.

---

## Line fixes

Each old text occurs exactly once in its file (verified by grep). `\n\n` marks a paragraph break (none needed here).

**F1 — required.** `manuscript/chapter-37.md`
- old: `"Then you'll have found that. "That's still something. Go on."`
- new: `"Then you'll have found that. That's still something. Go on."`

**F2 — required.** `manuscript/chapter-36.md`
- old: `in four sentences, and did not soften any of them`
- new: `in six sentences, and did not soften any of them`

**F3 — required.** `manuscript/chapter-40.md`
- old: `the way she had stood at the board on the morning she heard his whole name`
- new: `the way she had stood at the post on the morning she heard his whole name`

**F4 — optional (minor echo).** `manuscript/chapter-38.md`
- old: `Cael got his forearms in the way of it and felt it all the way to his teeth.`
- new: `Cael got his forearms in the way of it and felt it jar them both to the shoulder.`

After applying: rerun `ed.sh gates book-01-the-shattered 6` and `ed.sh overlap book-01-the-shattered 6` (no change
expected), and note the fixes under Repair r1 in `AUTHOR-REPORT.md`.
