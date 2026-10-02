#!/bin/bash
# Skeleton-probe every closed movement of a book against the source chapters its packet names.
# usage: sweep_probe.sh BOOK FIRST_MOVEMENT LAST_MOVEMENT
B=$1; E=editions/monroe-1.3/$B
for m in $(seq $2 $3); do
  P=$E/packets/MOVEMENT-$(printf %03d $m).md
  r=$(grep -m1 -oE 'Chapters: [0-9]+–[0-9]+' $P | grep -oE '[0-9]+' | tr '\n' ' ')
  set -- $r; lo=$1; hi=$2
  src=$(grep -m1 'Read before drafting' $P | grep -oE 'chapter-[0-9]+\.md' | sort -u | sed "s#^#books/$B/chapters/#")
  if [ -z "$src" ]; then  # Book 3 style: "Source chapters to read first, in full: 1, 2, 3 (and ...)"
    src=$(grep -m1 'Source chapters to read first' $P | sed 's/.*in full://; s/(.*//' | grep -oE '[0-9]+' | while read n; do printf "books/$B/chapters/chapter-%02d.md\n" $n; done)
  fi
  [ -z "$src" ] && { echo "== $B M$m: NO SOURCE CHAPTERS FOUND in packet"; continue; }
  ms=$(for c in $(seq $lo $hi); do printf "$E/manuscript/chapter-%02d.md " $c; done)
  echo "== $B M$m (ch$lo–$hi)"
  python3 editions/monroe-1.3/tools/skeleton_probe.py --source $src -- $ms | grep -vE '^\s+scene' 
done
