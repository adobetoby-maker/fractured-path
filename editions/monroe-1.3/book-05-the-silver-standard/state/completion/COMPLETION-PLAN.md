# Book 5 completion pass — plan (coordinator, 2026-10-06)

**Book 5 "The Silver Standard":** ch1–60, about 299,000 words.
- Movements 1–8 are closed.
- M9 (ch54–60) is in same-author repair r1. This plan runs once M9 closes.

Sol is out of quota until Oct 9, so every review step uses a fresh-context Claude Fable seat.

## Step 1 — Source-distance sweep: NOT NEEDED (pending M9's post-repair figure)

From `skeleton-sweep.txt` (M1–M8, closed text):

| Movement | Skeleton / close |
|---|---|
| M1 | 2% / 10% |
| M2 | 1% / 6% |
| M3 | 1% / 6% |
| M4 | 0% / 5% |
| M5 | 1% / 5% |
| M6 | 1% / 7% |
| M7 | 2% / 9% |
| M8 | 2% / 11% |

- No chapter in M1–M8 reaches 6% skeleton, and overlap is 0 unprotected in every movement.
- Book 4's closing pass treated close bands up to 13% as passing, with recheck readers confirming the remainder as common-word noise.
- M9 pre-repair reads 2% / 16%, with ch59 at 6% skeleton. Its repair re-composes the tabled trackers. Append M9's post-repair line here before Step 2. If any chapter still reads 6% or more skeleton, sweep that chapter first.

Tool note: `probe_sources.py` was fixed on 2026-10-06 to cut a packet's source clause at a mention of another book. M5–M8 ranges are unchanged.

## Step 2 — Whole-arc read (Fable, fresh context)

Model it on Book 4's `state/completion/whole-arc-read.md`, and read ch1–60 straight through. Queued items for the read:
- **The calendar.** Check every T-number and day count against #41 (BOOK_MAP §6 [M6-redated]).
  - The office's "three weeks" stands as the round figure, and no text states the tournament's length in days.
  - Rooke's "four days … seven" (M5 ch32) is superseded by the ch33 deferral.
- **Formats.**
  - #39: exhibitions; regional; continental points per exchange.
  - The M7 team-trial format, stated once by Rooke in ch45.
  - #40: no individual third place, three capabilities on public floors.
  - Ratings within the #38 bands.
- **Year counts.** Not incremented. Daeva is thirteen / six / seven. Vastin "forty years", with no age stated.
- **Season, month and English weekday names:** none anywhere.
- **Measures:** feet and yards only.
- **Names and pronouns.**
  - The keeper is "he".
  - Lira's burst shoulder is her LEFT.
  - Brom is formal tier Copper, continental Copper champion.
  - Ephram is Iron Rank Six.
- **The Ilsev / Havel / Vastin referral and returns record** across M1–M9, checked against Book 4's record (Greyvane first; Halcenvane on the fifteenth of Reaping).
- **The ring canon** (M8/M9) and the bank minute (ch53) against the match (ch54–56).
- **Placeholders.** Bede, Maud, Gwen and Abbot are owner-pending, not findings.

## Step 3 — Same-author texture pass

Two Opus lanes, ch1–30 and ch31–60. Their scope comes from the read's priorities, and the coordinator applies the read's line fixes first.

## Step 4 — Line and listening proof (Fable)

Model it on Book 4's `listening-proof-prompt.md`.

## Step 5 — Lock and publish

1. Write `HASHES.sha256`, `DIRECTOR_CUT_READY.md` and the tag `monroe13-book05-text-locked`.
2. Run `pwa_publish.py 5 60 --complete`. Verify the published copy is byte-identical and live.
3. Then:
   - re-run §D of `book-06-the-compacts-hand/state/B5-RECONCILIATION-AUDIT.md` against the closed M9;
   - apply the held items, including A11, the "four stamps", which goes to the owner;
   - confirm the apply seat's four option choices (`B5-RECONCILIATION-APPLIED.md` §5);
   - launch Book 6 Movement 1.
