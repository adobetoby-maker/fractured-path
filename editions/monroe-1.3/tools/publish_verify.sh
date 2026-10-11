#!/bin/bash
# Publish accepted chapters 1..N of edition book K to the reader app through a CLEAN worktree of
# boundary-universe origin/main (never the local checkout), build-gated, then verify the live copies.
# usage: publish_verify.sh K N "commit message" [--complete]
# Text/reading only. Generates no audio.
set -u
K=$1; N=$2; MSG=$3; FLAG=${4:-}
ED=/Users/drive/fractured-path-monroe13/editions/monroe-1.3; APP=/Users/drive/boundary-universe
W=${TMPDIR:-/tmp}/bu-pub-$$
BOOK=$(ls -d $ED/book-0$K-* | head -1)
cd $APP && git fetch -q origin && git worktree add -q --detach "$W" origin/main 2>&1 | grep -v "pointers\|public/audio" || true
(cd $ED && PWA_APP="$W" python3 tools/pwa_publish.py $K $N $FLAG) | tail -1
cd "$W" && ln -s $APP/node_modules node_modules
if npm run build 2>&1 | grep -q "Build failed\|error during build"; then echo "BUILD FAILED — nothing pushed"; rm -f node_modules; cd $APP; git worktree remove --force "$W"; exit 1; fi
git add src/lib/catalog.ts src/lib/manuscript-index.ts public/manuscripts/books/fractured-path-monroe-1.3/book-0$K/manuscript
git commit -qm "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" && git push -q origin HEAD:main && echo "pushed $(git log --oneline -1)"
rm -f node_modules; cd $APP && git worktree remove --force "$W"
U=https://books.worker-bee.app/manuscripts/books/fractured-path-monroe-1.3/book-0$K/manuscript
last=$(printf %02d $N); want=$(shasum -a 256 $BOOK/manuscript/chapter-$last.md | cut -d' ' -f1)
for i in $(seq 1 48); do got=$(curl -s "$U/chapter-$last.md?v=$i" | shasum -a 256 | cut -d' ' -f1); [ "$got" = "$want" ] && break; perl -e 'select(undef,undef,undef,10)'; done
perl -e 'select(undef,undef,undef,15)'
bad=0; for c in $(seq 1 $N); do n=$(printf %02d $c); a=$(curl -s "$U/chapter-$n.md?v=$RANDOM" | shasum -a 256 | cut -d' ' -f1); b=$(shasum -a 256 $BOOK/manuscript/chapter-$n.md | cut -d' ' -f1); [ "$a" = "$b" ] || { bad=$((bad+1)); echo "MISMATCH $n"; }; done
echo "live mismatches: $bad/$N; next chapter: $(curl -s -o /dev/null -w '%{http_code}' $U/chapter-$(printf %02d $((N+1))).md)"
