#!/bin/bash
# usage: metrics.sh DIR — per-chapter words / sentence mean / >=40 share / words per scene (read-only)
D=$1
for c in $(seq 31 60); do f=$(printf "%s/chapter-%02d.md" "$D" $c)
  python3 /Users/drive/fractured-path-monroe13/editions/monroe-1.3/tools/formula_metrics.py "$f" | awk -v c=$c '/^words_total/{w=$2}/^sentence_mean/{m=$2}/^share_ge40/{g=$2}/^words_per_scene/{s=$2}/^scene_breaks_marked/{b=$2}/^share_le5/{l=$2}END{printf "ch%d words=%s mean=%s ge40=%s le5=%s breaks=%s wps=%s\n",c,w,m,g,l,b,s}'
done
