# Book 6 completion pass — plan (coordinator, 2026-10-11)

**Book 6 "The Compact's Hand":** ch1–60. Movements 1–8 are closed and published; M9 (ch55–60) is in
same-author repair r1. This plan runs once M9 closes. Review seat: Sol (gpt-5.6-sol, ChatGPT plan).

## Step 1 — Source-distance sweep: NOT NEEDED

From `skeleton-sweep.txt` (M1–M8, closed text): M1 2%/11%, M2 1%/8%, M3 1%/13%, M4 1%/10%,
M5 1%/11%, M6 2%/14%, M7 1%/16%, M8 1%/11% (skeleton / close). Overlap is 0 unprotected in every
movement. One chapter reaches 6% skeleton: ch7, and all eleven of its matched pairs are protected
text (the challenge's first page, Tier A lines, the first pole). M7's 16% close band was read by
Sol at close as 0 genuine tracked passages. Append M9's post-repair line before Step 2.

## Step 2 — Whole-arc read (Sol, fresh context)

Prompt: `whole-arc-read-prompt.md`. Output: `whole-arc-read.md`, notes in `whole-arc-notes.md`.

## Step 3 — Same-author texture pass

Two Opus lanes, ch1–30 and ch31–60, scoped by the read's priorities in `PASS-BRIEF.md`. The
coordinator applies the read's line fixes first. Lanes do not open source chapters.

## Step 4 — Line and listening proof (Sol)

Prompt: `listening-proof-prompt.md`, modelled on Book 5's.

## Step 5 — Lock and publish

1. `HASHES.sha256`, `DIRECTOR_CUT_READY.md`, tag `monroe13-book06-text-locked`.
2. `pwa_publish.py 6 60 --complete` into a clean worktree; verify 60/60 live and byte-identical.
3. Then Book 7: re-run §F of `book-07-void-roads/state/B6-RECONCILIATION-AUDIT.md` against the
   locked M8–M9, apply the amendments, record owner items, launch Movement 1.
