# Book 2 completion pass — plan (coordinator, 2026-10-05)

**Book 2 "Iron Circuit"** is drafted, ch1–60. Movement 8 is in recheck on the Fable seat. Sol is out of
quota until Oct 9, so every review step in this pass uses a fresh-context Claude Fable seat.

## Step 1 — Source-distance sweep: NOT NEEDED
Every Book 2 movement was drafted with the event-list method and the per-chapter probe. The sweep against each
packet's source chapters (`skeleton-sweep.txt`) gives:

| Movement | Skeleton | Close |
|---|---|---|
| M1 | 0% | 13% |
| M2 | 1% | 7% |
| M3 | 0% | 8% |
| M4 | 1% | 12% |
| M5 | 0% | 5% |
| M6 | 0% | 5% |
| M7 | 1% | 6% |
| M8 | 1% | 10% |

No chapter reaches 8% skeleton, and overlap is 0 unprotected in every movement. Book 3 needed lanes A and B;
Book 2 does not.

## Step 2 — Whole-arc read (Fable, fresh context)
Book 3's `state/completion/whole-arc-read.md` is the model to follow. Read straight through ch1–60. Read
BOOK_MAP, the ledger's coordinator rulings and every movement end-state, OWNER-DECISIONS (#3, #4, #36), Book 1
ch59–60, and the closed edition Book 3 ch1–2. The read covers:
- continuity across movements;
- quotations checked against their first occurrence;
- knowledge boundaries;
- the consent boundary (canon from ch32);
- pulse and redirect tallies;
- book-wide repetition (the worst ten habits);
- arc and pacing;
- protected lines;
- the Reader Standard;
- rhythm outliers.

It ends with exact line fixes and at most three cross-movement priorities. Book 3-side errata the read finds are
added to the #36 queue, not applied.

## Step 3 — Same-author texture pass (Opus, two lanes: ch1–30 and ch31–60)
This step comes from the read's priorities. The coordinator applies the read's line fixes first.

## Step 4 — Line and listening proof (Fable)
Book 1's and Book 3's `listening-proof.md` are the models. Every chapter is checked for:
- quotes;
- ear collisions (Coss/Doss, Darrow/Marrow, Brom/Bede, Keth/Keth's marks);
- notices and code blocks;
- the spoken "Shattered" (brackets only in documents read verbatim);
- numerals and abbreviations;
- `---` spacing;
- paragraphs over 700 characters.

It also produces a pronunciation lexicon table, carrying forward #33.

## Step 5 — Lock and publish
1. Write `HASHES.sha256`, the book hash, `DIRECTOR_CUT_READY.md` and the tag `monroe13-book02-text-locked`.
2. Publish all 60 chapters with `pwa_publish.py 2 60 --complete`. This drops "in progress".
3. Verify the published files are byte-identical to the locked text, and verify the app live.
4. Apply the queued Book 3 v1.1 erratum (#36: ch22 and ch35 exchange/notice wording). Then re-hash Book 3,
   reissue its DIRECTOR_CUT_READY, retag it, and republish.
