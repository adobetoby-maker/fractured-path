#!/bin/bash
# Skeleton-probe every closed movement of a book against the source chapters its packet names.
# usage: [SHOW=1] sweep_probe.sh BOOK FIRST_MOVEMENT LAST_MOVEMENT   (SHOW=1 lists scenes and matched pairs)
B=$1; E=editions/monroe-1.3/$B
for m in $(seq $2 $3); do
  P=$E/packets/MOVEMENT-$(printf %03d $m).md
  r=$(grep -m1 -oE 'Chapters: [0-9]+–[0-9]+' $P | grep -oE '[0-9]+' | tr '\n' ' ')
  set -- $r; lo=$1; hi=$2
  src=$(python3 editions/monroe-1.3/tools/probe_sources.py "$P" "$B")
  [ -z "$src" ] && { echo "== $B M$m: NO SOURCE CHAPTERS FOUND in packet"; continue; }
  ms=$(for c in $(seq $lo $hi); do printf "$E/manuscript/chapter-%02d.md " $c; done)
  echo "== $B M$m (ch$lo–$hi)"
  if [ -n "$SHOW" ]; then
    python3 editions/monroe-1.3/tools/skeleton_probe.py --show --source $src -- $ms
  else
    python3 editions/monroe-1.3/tools/skeleton_probe.py --source $src -- $ms | grep -vE '^\s+scene'
  fi
done
