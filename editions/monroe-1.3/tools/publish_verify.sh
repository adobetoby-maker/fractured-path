#!/bin/bash
# Publish accepted chapters 1..N of edition book K to the reader app through a CLEAN worktree of
# boundary-universe origin/main (never the local checkout), build-gated, then verify the live copies.
# usage: publish_verify.sh K N "commit message" [pwa_publish flags…]   e.g. --complete, or --new --title … --cover … (all passed through)
# Text/reading only. Generates no audio.
set -u
K=$1; N=$2; MSG=$3; shift 3
ED=/Users/drive/fractured-path-monroe13/editions/monroe-1.3; APP=/Users/drive/boundary-universe
W=${TMPDIR:-/tmp}/bu-pub-$$
BOOK=$(ls -d $ED/book-0$K-* | head -1)
# Guard: never publish text that fails the gates or carries an unprotected source run.
BN=$(basename $BOOK)
for P in $BOOK/packets/MOVEMENT-0*.md; do
  m=$(basename $P .md | sed 's/MOVEMENT-0*//'); hi=$(grep -m1 -oE 'Chapters?:[^0-9]*[0-9]+[^0-9]+[0-9]+' $P | grep -oE '[0-9]+' | tail -1)
  [ -z "$hi" ] && continue; [ "$hi" -gt "$N" ] && continue
  o=$(cd /Users/drive/fractured-path-monroe13 && bash editions/monroe-1.3/tools/ed.sh overlap $BN $m 2>&1 | tail -1 | grep -oE '[0-9]+ unprotected' | cut -d' ' -f1)
  g=$(cd /Users/drive/fractured-path-monroe13 && bash editions/monroe-1.3/tools/ed.sh gates $BN $m | awk '{s+=substr($3,17)+substr($4,10)+substr($5,8)} END{print s+0}')
  if [ "${o:-1}" != "0" ] || [ "$g" != "0" ]; then echo "ABORT: $BN movement $m has overlap=$o gates=$g — nothing published"; exit 2; fi
done
if grep -l "\[\[TIER-B" $(for c in $(seq 1 $N); do printf "$BOOK/manuscript/chapter-%02d.md " $c; done) 2>/dev/null | grep -q .; then echo "ABORT: TIER-B marker present — nothing published"; exit 2; fi
cd $APP && git fetch -q origin && git worktree add -q --detach "$W" origin/main 2>&1 | grep -v "pointers\|public/audio" || true
(cd $ED && PWA_APP="$W" python3 tools/pwa_publish.py $K $N "$@") | tail -1
cd "$W" && ln -s $APP/node_modules node_modules
if npm run build 2>&1 | grep -q "Build failed\|error during build"; then echo "BUILD FAILED — nothing pushed"; rm -f node_modules; cd $APP; git worktree remove --force "$W"; exit 1; fi
git add src/lib/catalog.ts src/lib/manuscript-index.ts public/manuscripts/books/fractured-path-monroe-1.3/book-0$K/manuscript
git commit -qm "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" && git push -q origin HEAD:main && echo "pushed $(git log --oneline -1)"
rm -f node_modules; cd $APP && git worktree remove --force "$W"
U=https://books.worker-bee.app/manuscripts/books/fractured-path-monroe-1.3/book-0$K/manuscript
# Wait for the deploy: re-check every chapter until all match (a previous deploy may already serve some).
bad=1
for try in $(seq 1 40); do
  bad=0; miss=""
  for c in $(seq 1 $N); do n=$(printf %02d $c); a=$(curl -s "$U/chapter-$n.md?v=$RANDOM$try" | shasum -a 256 | cut -d' ' -f1); b=$(shasum -a 256 $BOOK/manuscript/chapter-$n.md | cut -d' ' -f1); [ "$a" = "$b" ] || { bad=$((bad+1)); miss="$miss $n"; }; done
  [ $bad -eq 0 ] && break
  perl -e 'select(undef,undef,undef,15)'
done
[ $bad -eq 0 ] || echo "MISMATCH:$miss"
echo "live mismatches: $bad/$N; next chapter: $(curl -s -o /dev/null -w '%{http_code}' $U/chapter-$(printf %02d $((N+1))).md)"
