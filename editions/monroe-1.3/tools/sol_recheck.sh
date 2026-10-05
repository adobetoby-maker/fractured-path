#!/bin/bash
# Launch a Sol (codex, ChatGPT plan) recheck of a repaired movement, per tools/RECHECK-TEMPLATE.md.
# usage: sol_recheck.sh BOOK N FIRST_CH LAST_CH [extra-notes-file]
set -e
ROOT=/Users/drive/fractured-path-monroe13; E=editions/monroe-1.3
B=$1; N=$2; F=$3; L=$4; NN=$(printf %03d $N); S=$E/$B/state/movement-$NN
EXTRA=""; [ -n "$5" ] && EXTRA="$(cat "$5")"
cat > $ROOT/$S/recheck-prompt.md <<P
You are the review seat doing a TARGETED RECHECK (Sol, via codex; the author is Claude Opus 5.5). Do not modify any manuscript file. Working directory: $ROOT.

$B, Movement $N (chapters $F–$L) of the Monroe 1.3 edition of The Fractured Path, after the same-author repair r1. Files under $E/$B/:
- brief: state/movement-$NN/REPAIR-BRIEF.md
- reviews: state/movement-$NN/review-editorial.md, review-cold.md
- author's report: state/movement-$NN/AUTHOR-REPORT.md ("## Repair r1")
- pre-repair: state/movement-$NN/pre-repair/
- current text: manuscript/chapter-$(printf %02d $F).md … chapter-$(printf %02d $L).md
- context: BOOK_MAP.md, STATE_LEDGER.md (latest "After Movement" block and the entry state), the movement packet packets/MOVEMENT-$NN.md (incl. coordinator notes), the previous chapters, and the source chapters in books/$B/chapters/.

Read the FULL current movement, then follow $E/tools/RECHECK-TEMPLATE.md exactly: (1) brief items RESOLVED/PARTIAL/NOT with quoted evidence (diff -U0 vs pre-repair); (2) continuity; (3) formula — run \`python3 $E/tools/formula_metrics.py\` on the chapters, \`bash $E/tools/ed.sh overlap $B $N\`, \`bash $E/tools/ed.sh gates $B $N\`, \`bash $E/tools/sweep_probe.sh $B $N $N\`; (4) reader clarity; (5) listening proof on every chapter.
$EXTRA

Write state/movement-$NN/recheck-r1.md: verdict FIRST (CLOSE / CLOSE WITH LINE FIXES / SECOND REPAIR, with scope), then sections (1)–(5), then exact line fixes in exactly this format, each old string verified with grep to match exactly once:
N. \`manuscript/chapter-NN.md\`
   old: \`...\`
   new: \`...\`
P
cd $ROOT && env -u OPENAI_API_KEY -u OPENAI_BASE_URL nohup codex exec --cd $ROOT --skip-git-repo-check -o $S/recheck-r1.lastmsg.md "$(cat $S/recheck-prompt.md)" < /dev/null > $S/recheck-r1.stdout.log 2>&1 &
echo $! > $ROOT/$S/recheck-r1.pid; echo "launched Sol recheck $B M$N pid $(cat $ROOT/$S/recheck-r1.pid)"
