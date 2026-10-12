#!/bin/bash
# Lane A helper: count each target pool in chapters 1-30 of a directory (read-only).
# usage: bash counts.sh <dir>
D="$1"
FILES=()
for i in $(seq -w 1 30); do FILES+=("$D/chapter-$i.md"); done
cnt(){ cat "${FILES[@]}" | grep -oiE "$1" | wc -l | tr -d ' '; }
while IFS='|' read -r label pat; do
  printf '%-28s %s\n' "$label" "$(cnt "$pat")"
done <<'PATS'
old man|old man
small pale woman|small pale woman
big man|big man
quiet man|quiet man
as a/an man/person/...|\bas an? (man|person|woman|boy|girl)\b
He found that|He found that
nobody said/spoke/answered|nobody (said|spoke|answered)
did not look|(did not|didn.t) look
count*|\bcount(ed|ing|s)?\b
enter/entered/entry|\b(enter|entered|entry|entries|enters|entering)\b
price/bill|\b(price|priced|prices|pricing|bill|bills|billed)\b
flat|\bflat\b
finger/hair measures|(finger.?s?.(width|breadth)|width of (a|one|two|three) fingers?|breadth of a (finger|hair)|hair.s.(width|breadth)|by a hair|to a hair|width of a hair)
thumbs in belts|thumbs? [a-z ]{0,12}belt
told it no & kin|told (it|them|him|her|the [a-z]+) no\b
PATS
echo "words: $(cat "${FILES[@]}" | wc -w | tr -d ' ')"
