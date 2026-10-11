# Book 7 completion pass — plan (coordinator, 2026-10-11)

**Book 7 "Void Roads":** ch1–60. Movements 1–7 are closed and published; M8 (ch53–60) is in
same-author repair r1. This plan runs once M8 closes. Review seat: Sol (gpt-5.6-sol, ChatGPT plan).
The whole book was drafted by the no-source method; every movement had a Sol source-distance read.

## Step 1 — Source-distance sweep: judged inside Step 2

`skeleton-sweep.txt` (M1–M7, closed text): M1 1%/13%, M2 2%/19%, M3 2%/22%, M4 4%/22%, M5 6%/21%,
M6 3%/18%, M7 3%/18% (skeleton / close). Overlap is 0 unprotected in every movement. Nine chapters
reach 6% skeleton or more (ch25, 26, 33, 34, 36, 37, 44, 46, 52). Each carries whole protected
units the plan audits restored from the source, which score as exact matches; each movement's own
Sol read found its tracked passages and all were resolved at recheck. The whole-arc read's §11
re-judges those nine chapters by reading, with protected text excluded. Append M8's line before
Step 2.

## Step 2 — Whole-arc read (Sol, fresh context)

Prompt: `whole-arc-read-prompt.md`. Output: `whole-arc-read.md`, notes in `whole-arc-notes.md`.
It carries a dedicated section on the consent thread (the tenth fragment, the telling, Millrace,
the debt, "the wrist not read") for the Reader Standard.

## Step 3 — Same-author texture pass

Two Opus lanes, ch1–30 and ch31–60, scoped by the read's priorities in `PASS-BRIEF.md`. The
coordinator applies the read's line fixes first and re-runs overlap after EVERY applied fix.

## Step 4 — Line and listening proof (Sol)

Prompt: `listening-proof-prompt.md` (finalised from the seed after the lanes).

## Step 5 — Lock and publish

1. `HASHES.sha256`, `DIRECTOR_CUT_READY.md`, tag `monroe13-book07-text-locked`.
2. `publish_verify.sh 7 60 "…" --complete` (guards: gates, overlap, no markers; waits for every
   chapter to match). 60/60 live against the bound hashes.
3. Then Book 8: re-run §H of `book-08-before-the-paths/state/B7-RECONCILIATION-AUDIT.md` against
   the locked M7–M8, apply the amendments with the coordinator overrides, record owner items,
   launch Movement 1.
