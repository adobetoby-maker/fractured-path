#!/bin/bash
# Launch the four Sol (codex, ChatGPT plan) reads on a frozen first draft of a movement and wait for them:
# editorial + cold (via ed.sh review), source-distance read, and plan / canon / protected-text audit.
# usage: sol_reads.sh BOOK N FIRST_CH LAST_CH [audit-notes-file]      (run from anywhere)
set -e
ROOT=/Users/drive/fractured-path-monroe13; E=editions/monroe-1.3
B=$1; N=$2; F=$3; L=$4; NN=$(printf %03d $N); S=$E/$B/state/movement-$NN; FF=$(printf %02d $F); LL=$(printf %02d $L)
NOTES=""; [ -n "$5" ] && NOTES="$(cat "$5")"
cd $ROOT
SRC=$(python3 $E/tools/probe_sources.py $E/$B/packets/MOVEMENT-$NN.md $B | tr '\n' ' ')
NEXT=$(printf %03d $((N+1)))
cat > $S/source-tracking-prompt.md <<P
You are Sol, the independent source-distance reader for the Monroe 1.3 edition of The Fractured Path, $B, Movement $N (chapters $F–$L). Work in $ROOT.

Background: drafted WITHOUT the author opening the source (events from the packet, the edition BOOK_MAP and STATE_LEDGER only). Protected units from the BOOK_MAP's protected-text section and packet-quoted lines are placed verbatim by design and are listed in protected-patterns.txt or quoted in the map — exclude them. Judge only the author's own prose. Verify independently.

Read the source chapters for this movement: $SRC
Read the manuscript: $E/$B/manuscript/chapter-$FF.md … chapter-$LL.md. For calibration, also run the probe with pair output: from the worktree root, \`SHOW=1 bash $E/tools/sweep_probe.sh $B $N $N\`.

By READING, side by side, find every passage that keeps a source sentence's content and order (its beats in the same sequence), whether the words are varied, the sentence is split, or near-verbatim. Do not count:
- protected or packet lines ($E/$B/protected-patterns.txt; the BOOK_MAP's protected-text section; lines quoted in packets/MOVEMENT-$NN.md);
- facts and events the plan requires, so long as their telling is new;
- common-word coincidences.

Write $S/source-tracking.md containing:
1. A verdict: the count of genuine tracked passages per chapter and per scene.
2. A table with these columns: chapter:line, the manuscript opening words, the source sentence it follows (file:line plus the opening words), and the kind (varied / split / near-verbatim). For each, describe the chain of beats in one or two sentences so the author can break it WITHOUT opening the source.
3. For each densely tracked scene, a suggested new entry point or order of beats that would make it the author's own.

Do not edit any manuscript file. Run no git commands.
P
cat > $S/plan-audit-prompt.md <<P
You are Sol, the independent plan, canon and protected-text auditor for the Monroe 1.3 edition of The Fractured Path, $B, Movement $N (chapters $F–$L). Work in $ROOT. Do not modify any file except the one output named below. Run no git commands.

The author (Claude Opus 5.5) drafted without opening the source, from the packet, the edition plan and the edition's own closed chapters. Verify the draft against everything it must agree with, and supply exact fixes.

## Read
Under $E/:
- OWNER-DECISIONS.md, all of it.
- $B/BOOK_MAP.md, STATE_LEDGER.md (every AFTER MOVEMENT block: coordinator rulings and CLOSED notes govern), packets/MOVEMENT-$NN.md, and the next packet packets/MOVEMENT-$NEXT.md if it exists.
- $B/state/movement-$NN/EVENT-LIST.md, AUTHOR-REPORT.md, AUTHORSHIP.md.
- $B/manuscript/chapter-$FF.md … chapter-$LL.md, every word; and the book's earlier closed chapters as needed for continuity (at least the previous movement in full).
- For protected text only: the source chapters ($SRC) to check each protected unit's full wording.

## Audit
1. **Continuity with the closed text.** People, places, day counts, bodies and injuries, standings, every object, letter and sum of money, the fragment inventory and deployment count, who knows what. Report any contradiction with chapter:line on both sides.
2. **The movement plan.** Every packet beat and every "must remain true / withheld" item: present, in order, nothing withheld spent early. Rule on each flag in AUTHOR-REPORT's "Owner flags".
3. **The calendar.** Every day count in these chapters against the BOOK_MAP and STATE_LEDGER day tables and the previous movement.
4. **Standing defaults.** No season names, month names or order, English weekday names; no metric units; no year count since Kindling; Cael's age as the ledger gives it; never "his Path" for Cael; Reader Standard (a 13-year-old reader).
5. **Protected text.** For every protected unit the BOOK_MAP assigns to these chapters and every packet-quoted line: present, once, in the right place, word for word as the map now gives it (including [B6-reconciled] wordings)? Where the map quotes a unit only in part, compare the manuscript with the source's full unit: did the author compose words the protected unit already has? Supply the exact protected text as a fix where so. A protected document must not be printed twice.
6. **New canon minted** (AUTHOR-REPORT list): for each item, does it contradict the universe bible, the map, or any later packet? Rule KEEP / AMEND / CUT, with an exact fix for AMEND or CUT.
7. **Names.** Any named person, place or animal the plan does not name is a finding (the owner supplies names).
8. **Next-movement inheritance.** List what the next movement's author must inherit from the surviving prose that its packet does not already carry.
$NOTES

## Write
$S/plan-audit.md: a verdict FIRST (RATIFY / RATIFY WITH LINE FIXES / REPAIR, with scope), then sections 1–8, then exact line fixes in exactly this format, each old string verified with grep to match exactly once in its file:
N. \`manuscript/chapter-NN.md\`
   old: \`...\`
   new: \`...\`
Use \\n for a line break inside a fix. Give chapter:line for every claim. Never propose a fix inside a protected unit except to restore its exact wording.
P
(cd $E && REVIEW_SEAT=codex bash tools/ed.sh review $B $N 2>&1 | tail -2)
for k in source-tracking plan-audit; do
  env -u OPENAI_API_KEY -u OPENAI_BASE_URL nohup codex exec -m "${SOL_MODEL:-gpt-6.1-sol}" -c model_reasoning_effort="${SOL_EFFORT:-high}" --cd $ROOT --skip-git-repo-check -o $S/$k.lastmsg.md "$(cat $S/$k-prompt.md)" < /dev/null > $S/$k.stdout.log 2>&1 &
  echo $! > $S/$k.pid
done
for k in review-editorial review-cold source-tracking plan-audit; do
  p=$(cat $S/$k.pid); while kill -0 $p 2>/dev/null; do perl -e 'select(undef,undef,undef,5)'; done
  echo "== $k"; [ -s $S/$k.md ] && echo "written ($(wc -w < $S/$k.md) words)" || echo "MISSING $S/$k.md"
  head -12 $S/$k.lastmsg.md 2>/dev/null | cut -c1-500
done
