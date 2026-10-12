# Book 8 completion pass — plan (coordinator, 2026-10-12)

**Book 8 "Before the Paths":** ch1–60, nine movements. Movements 1–8 are closed and published; M9 (ch54–60,
the last) closed on 2026-10-12. All nine movements are closed; this plan now runs. Review seat: Sol (gpt-5.6-sol, ChatGPT plan).
The whole book was drafted by the no-source method; every movement had a Sol source-distance read, a plan /
canon / protected-text audit ruled on by the coordinator against the edition's own closed text, one
same-author repair round and a Sol recheck.

## Step 1 — Source-distance sweep: judged inside Step 2

`skeleton-sweep.txt` (M1–M8, closed text; skeleton / close): M1 1%/4%, M2 2%/13%, M3 2%/15%, M4 2%/10%,
M5 3%/14%, M6 3%/18%, M7 1%/13%, M8 2%/9%. Overlap is 0 unprotected in every movement. Two chapters reach
6% skeleton or more: ch38 (7%; the leaf read aloud, whole, protected) and ch40 (6%; the fire and pole two,
protected). The whole-arc read's §11 re-judges every chapter at 6% or more by reading, with protected text
excluded. M9 (closed 2026-10-12): 3%/16%; ch60 reaches 6% (the ledger, the letter and the closing prose, all protected). Three chapters in all at 6% or more: 38, 40, 60.

## Step 2 — Whole-arc read (Sol, fresh context)

Prompt: `whole-arc-read-prompt.md`. Output: `whole-arc-read.md`, notes in `whole-arc-notes.md`.
It carries dedicated sections on (a) the record's limits (BOOK_MAP §9: the leaf once; "four hundred years"
and "the Architect" only at the fixed places; two pages, no line; the chronicle's hole; the deep-layer date)
and (b) the knowledge perimeters and unpaid debts (the eleventh from Vastin, the thirteenth from Teague, the
twelfth told to Cleon; *still* / *set* told to no one), since those are what only a straight read can test.
A run is accepted only if its token use and log size are those of a full read (Book 7's first listening
proof was rejected on that ground).

## Step 3 — Same-author texture pass

Two Opus lanes, ch1–30 and ch31–60, scoped by the read's priorities in `PASS-BRIEF.md`, with `pre-lanes/`
as the baseline. The coordinator applies the read's line fixes first and re-runs overlap after EVERY applied
fix; lane cuts are diffed against `pre-lanes/` and any cut that touches protected text, a plan fact or a
coordinator ruling is restored.

## Step 4 — Line and listening proof (Sol)

Four full-text proofs of fifteen chapters each (`listening-proof-partN-prompt.md`), each returning
scene-boundary evidence (first and last words of sampled scenes, checked verbatim against the files) so
that a short read cannot pass as a full one.

## Step 5 — Lock and publish

1. `HASHES.sha256`, `DIRECTOR_CUT_READY.md` (listing every owner-pending, text-affecting item that stands by
   default: #18, #48, #52–#60 and the older open items), tag `monroe13-book08-text-locked`.
2. `publish_verify.sh 8 60 "…" --complete` (guards: gates, overlap, no markers; waits for every chapter to
   match). 60/60 live against the bound hashes.
3. Never call a moving draft text-locked: DIRECTOR_CUT_READY is signalled only after Steps 2–4 and the hash.
   No audio is generated and no ElevenLabs credits are spent at any step.
