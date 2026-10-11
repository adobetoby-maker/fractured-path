#!/bin/bash
# usage (from the worktree root): probe_scenes.sh DIRNAME   -> per-chapter and per-scene probe numbers (no text) for movements 5-8
B=book-07-void-roads; E=editions/monroe-1.3/$B; d=$1
for m in 5 6 7 8; do
  P=$E/packets/MOVEMENT-00$m.md
  r=$(grep -m1 -oE 'Chapters: [0-9]+–[0-9]+' $P | grep -oE '[0-9]+' | tr '\n' ' '); set -- $r
  src=$(python3 editions/monroe-1.3/tools/probe_sources.py "$P" "$B")
  ms=$(for c in $(seq $1 $2); do printf "$E/$d/chapter-%02d.md " $c; done)
  python3 editions/monroe-1.3/tools/skeleton_probe.py --source $src -- $ms
done
