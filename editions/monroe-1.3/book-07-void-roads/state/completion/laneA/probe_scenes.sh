#!/bin/bash
# usage: probe_scenes.sh DIR  -> per-scene probe lines for chapters 1-30 found in DIR (runs the official probe tool only)
cd /Users/drive/fractured-path-monroe13
B=editions/monroe-1.3/book-07-void-roads; L=$B/state/completion/laneA
for i in $(seq 1 30); do
  if [ $i -le 7 ]; then m=1; elif [ $i -le 14 ]; then m=2; elif [ $i -le 22 ]; then m=3; else m=4; fi
  f=$1/chapter-$(printf %02d $i).md
  python3 editions/monroe-1.3/tools/skeleton_probe.py --source $(cat $L/src-m$m.paths) -- $f | grep -v TOTAL | awk -v c=$i '/scene/{n=$3; sub("n=","",n); s=$4; sub("skeleton=","",s); sub("%","",s); k=$5; sub("close=","",k); sub("%.*","",k); printf "ch%02d s%s n=%s skel=%d close=%d\n", c, $2, n, int(s*n/100+0.5), int(k*n/100+0.5)}'
done
