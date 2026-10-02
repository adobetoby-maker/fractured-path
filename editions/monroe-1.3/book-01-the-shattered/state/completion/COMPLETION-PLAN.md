# Book 1 completion pass — plan (coordinator, 2026-10-02)

Book 1 is drafted in full (ch1–60). Movements 1–7 were drafted before the event-list method; the
skeleton probe (`tools/sweep_probe.sh`, `SHOW=1` listing in `skeleton-sweep.txt`) measured them
against the source chapters each packet names. Movements 8–9, drafted from event lists, measure
0–1%.

## Step 1 — Source-distance sweep (two parallel same-seat authors, Opus)

**Scene rebuilds (skeleton >15% in a scene of ≥10 sentences), from the author's own event list,
source closed:**

| Lane | Scenes |
|---|---|
| A (M1–M2) | ch2 s1 (28%), ch2 s4 (27%); ch5 s2 (18%), s4 (37%), s5 (57%); ch6 s1 (24%), s2 (38%); ch12 s2 (20%); ch13 s1 (24%), s2 (19%), s4 (29%) |
| B (M3–M7) | ch20 s1 (23%), s4 (18%); ch25 s3 (21%), s6 (27%), s7 (17%); ch26 s4 (31%); ch32 s3 (17%); ch43 s3 (16%); ch47 s2 (20%) |

**Sentence recomposition:** every remaining unprotected sentence scoring ≥0.65 in `skeleton-sweep.txt`.
The list has 186 sentences before protected lines are excluded. They are concentrated in ch1, 2, 5, 6,
12, 13, 20, 25, 26, 32, 46 and 47. Protected lines (BOOK_MAP §7, `protected-patterns.txt`) stay
exact.

**Target:** every chapter 5% or below, no scene above 12%. Overlap stays at 0 unprotected and the
gates stay at 0. Each lane edits only its own chapters. The STATE_LEDGER facts and every
cross-chapter referent must survive the rebuild.

## Step 2 — Whole-arc read (Fable 5.1, fresh context)

One reader reads ch1–60 in order. Checks:
- continuity across movements;
- repeated tics and refrains across the book;
- arc pacing;
- every plant paid or deliberately carried to Book 2;
- the knowledge boundaries;
- the Reader Standard.

Output: exact line fixes, plus at most three cross-movement priorities for one same-author pass.

## Step 3 — Line and listening proof (Fable 5.1)

A read-aloud proof of every chapter for the Breeze render. It checks:
- quotation marks and attribution;
- homographs, and names that collide by ear (Halvern/Halden, decision #29);
- italics and log formatting as the narrator will meet them;
- numerals;
- the `---` spacing.

## Step 4 — Close and publish

Book-level metrics. A FINAL STATE_LEDGER block. Commit and push. Then the Breeze render of
ch1–60 → a new edition (`fractured-path-b01-monroe13`) in the reader app.

## Carried in from the Movement 9 recheck (for Step 2, the whole-arc read)

Out of this recheck's scope, but noticed:
1. **"Seven months" is the book's rounding, not a count.** Ardenmere time at the bout is 196 days from arrival; BOOK_MAP §1 says "about seven months". Check that no earlier movement says "six months" for the same span, and that the ledger's "After Movement 9" fixes the day numbers above (vouch day 8; assessed day 97; bout day 200) so later books quote one calendar.
2. **Ledger entry for M9** should record the card decision as canon: the line reads *unrated (vouched)* until the yard comes; the assessment is a margin note; Vell says the name and "Assessed-Copper" at the rope only on the day the yard comes, superseding M7's "so will I at the rope". Also: Lira asks Doss at dawn day 183; Doss's kitchen scene the evening of 183; the chalk-board woman day 184.
3. **Season words.** ch 60 "the mark Ilsev had found in the spring" (Ilsev day 141) against ch 55's "in the winter" for day 97 and the M8 ledger's spring beginning around the pear blossom (~day 178). Decide where winter ends for this book and sweep the three movements that name it.
4. **Darrow's stance** (edition: right foot forward, left back and nailed) differs from source ch 23; the series map should quote the edition's foot, as the editorial already flagged.
5. **Darrow's autumn** ("back up this river in the autumn… he'll want to know") and Feryn's "The coat's not done… I'll not see it till the autumn" both fall in the between-books gap; Book 2's map must stage or lapse them.
6. **Coss's flag, the empty log page and the key** need their Book 6 plant entry; the ledger phrase for the Iron Path should be "the crossing is the reset after each load" so Book 3 ch 8's wording and this one are the same fact.
7. **Feryn's "I've been here a fortnight"** (ch 59, day 201; he arrived day 182 and went down the river twice between) is loose by five days; harmless unless Book 2 counts it.
8. **Reporting verbs** still ~90 per 10k in M9 (target ~41). If the book pass harmonizes density across movements, the multi-speaker scenes here (ch 56 s3, ch 59 s1–3) are where the remainder lives, and fix 3 below adds one back on purpose.
9. **≥40-word share at the ceiling** after the joins; any further joining in a book-level smoothing pass should aim at 15–30-word sentences, as the author notes.

---

