#!/bin/bash
# usage: metrics.sh DIR — per-chapter words (wc -w), sentence mean, >=40 share, words/scene
D="$1"
for n in $(seq 31 60); do
python3 editions/monroe-1.3/tools/formula_metrics.py "$D/chapter-$n.md" --json | python3 -c "
import json,sys
d=json.load(sys.stdin)
d=d[0] if isinstance(d,list) else d
print('ch$n', 'words', d['words_total'], 'mean', d['sentence_mean'], 'ge40', d['share_ge40_words'], 'wps', d['words_per_scene'])"
done
