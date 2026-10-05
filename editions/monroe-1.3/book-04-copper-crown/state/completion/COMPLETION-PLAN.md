# Book 4 completion pass — plan (coordinator, 2026-10-05)

**Book 4 "Copper Crown"** is drafted: ch1–62, about 294,000 words. All nine movements are closed. Sol is out of
quota until Oct 9, so every review step in this pass uses a fresh-context Claude Fable seat.

## Step 1 — Source-distance sweep: NOT NEEDED
The sweep (`skeleton-sweep.txt`), skeleton / close:

| Movement | Skeleton | Close |
|---|---|---|
| M1 | 1% | 13% |
| M2 | 1% | 6% |
| M3 | 1% | 13% |
| M4 | 1% | 13% |
| M5 | 1% | 12% |
| M6 | 1% | 10% |
| M7 | 1% | 11% |
| M8 | 2% | 7% |
| M9 | 2% | 9% |

No chapter reaches 6% skeleton, and overlap is 0 unprotected in every movement.

## Step 2 — Whole-arc read (Fable, fresh context)
Model the read on Book 3's and Book 2's `state/completion/whole-arc-read.md`. Read ch1–62 straight through. The read
also receives these queued items:
- **The baseline month.** The baseline is the forty-eighth day (ch12), which is the SECOND month. "First month" for the
  baseline survives at ch43:201, ch49:195 and about 15 uses in ch54–55. Rule once and give line fixes. Note that "the
  first month" is also used loosely elsewhere for the term's opening weeks; those may stand where they do not refer to
  the baseline.
- **OWNER-DECISIONS #35** (Sowing/Reaping): verify that no month order or cross-month day count appears anywhere.
- **Placeholders.** Gwen and Abbot are owner-pending placeholders, not findings.

## Step 3 — Same-author texture pass
Two Opus lanes: ch1–31 and ch32–62. Their scope comes from the read's priorities; the coordinator applies the read's
line fixes first.

## Step 4 — Line and listening proof (Fable)
Model it on Book 2's prompt (`book-02-iron-circuit/state/completion/listening-proof-prompt.md`).

## Step 5 — Lock and publish
1. Write `HASHES.sha256`, `DIRECTOR_CUT_READY.md` and the tag `monroe13-book04-text-locked`.
2. Publish with `pwa_publish.py 4 62 --complete`, then verify the published copy is byte-identical and live.
3. Then apply the Book 5 reconciliation (`book-05-the-silver-standard/state/B4-RECONCILIATION-AUDIT.md`) to the Book 5
   map and packets, and launch Book 5 Movement 1.
