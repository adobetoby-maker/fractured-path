#!/bin/bash
# Book 7 loop driver. Usage: loop.sh <cmd> <NN> [r]
set -e
ROOT=/Users/drive/fractured-path; P=/Users/drive/penname/pennamecodexv3; B=$ROOT/v3-runs/book-07
cmd=$1; N=$2; R=${3:-1}
case $cmd in
  compile-author)  # validate packet, compile author prompt
    pk=$B/packets/ch$N.json; [ "$R" != "1" ] && pk=$B/packets/ch$N-repair-r$R.json
    python3 -B $P/scripts/validate.py $P/contracts/scene-packet.schema.json $pk >/dev/null && echo "packet valid: $pk"
    out=$B/packets/ch$N-author-prompt-r$R.md
    python3 -B $P/scripts/build_prompt.py author --packet $pk --root $ROOT > $out && echo "author prompt: $out ($(wc -c < $out) bytes)";;
  run-editor)  # validate author report, compile editor prompt, launch codex (Sol) detached
    pk=$B/packets/ch$N.json; [ "$R" != "1" ] && pk=$B/packets/ch$N-repair-r$R.json
    rep=$B/reports/ch$N-author-r$R.json
    python3 -B $P/scripts/validate.py $P/contracts/author-report.schema.json $rep >/dev/null && echo "author report valid"
    python3 -B $P/scripts/build_prompt.py editor --packet $pk --root $ROOT > $B/packets/ch$N-editor-prompt-r$R.md && echo "editor prompt compiled"
    sed "s|__PROMPT__|v3-runs/book-07/packets/ch$N-editor-prompt-r$R.md|g; s|__OUT__|v3-runs/book-07/reports/ch$N-editor-r$R.json|g; s|__PREV__|$( [ "$R" != "1" ] && echo "Your prior report on this scene is at v3-runs/book-07/reports/ch$N-editor-r$((R-1)).json and the verifier decisions at v3-runs/book-07/reports/ch$N-verifier-r$((R-1)).json; the pre-repair draft is in CONTEXT. Confirm each verified finding is repaired (quote), confirm no unrelated passage changed and every recorded strength survived, then re-run the full gate set." || echo "This is a first review of a fresh draft." )|" $B/editor-wrapper.template.md > $B/packets/ch$N-editor-wrapper-r$R.md
    grep -q '"auth_mode"[[:space:]]*:[[:space:]]*"chatgpt"' ~/.codex/auth.json 2>/dev/null || { echo "REFUSING: codex not on ChatGPT-plan login (auth.json missing or not auth_mode=chatgpt; Toby, 2026-09-04) — use the Opus review seat" >&2; exit 3; }
    nohup env -u OPENAI_API_KEY codex exec --cd $ROOT --skip-git-repo-check -o $B/reports/ch$N-editor-r$R.lastmsg.md "$(cat $B/packets/ch$N-editor-wrapper-r$R.md)" < /dev/null > $B/reports/ch$N-editor-r$R.stdout.log 2>&1 &
    echo $! > $B/reports/ch$N-editor-r$R.pid; echo "editor launched pid $(cat $B/reports/ch$N-editor-r$R.pid)";;
  wait-editor)  # block until report exists or process dies
    PID=$(cat $B/reports/ch$N-editor-r$R.pid); until [ -s $B/reports/ch$N-editor-r$R.json ] || ! kill -0 $PID 2>/dev/null; do sleep 5; done
    [ -s $B/reports/ch$N-editor-r$R.json ] && echo "EDITOR r$R READY ch$N" || { echo "EDITOR EXITED WITHOUT REPORT ch$N r$R"; tail -c 800 $B/reports/ch$N-editor-r$R.stdout.log; };;
  show-editor)
    python3 -B $P/scripts/validate.py $P/contracts/editor-report.schema.json $B/reports/ch$N-editor-r$R.json >/dev/null && echo "editor report valid"
    python3 - "$B/reports/ch$N-editor-r$R.json" << 'PY'
import json,sys;r=json.load(open(sys.argv[1]))
print('VERDICT:',r.get('verdict'))
fs=r.get('findings',r.get('proposed_findings',[]))
print('findings:',len(fs))
for f in fs:
    print('\n---',f.get('id'),f.get('severity'),'|',f.get('gate'));print('EVIDENCE:',f.get('evidence'));print('CONSEQUENCE:',f.get('consequence'));print('REPAIR:',f.get('repair_target'))
print('\nSTRENGTHS:');[print(' -',s[:220]) for s in r.get('strengths',[])]
print('\nTASTE:');[print(' -',s[:300]) for s in r.get('taste_concerns',[])]
PY
    ;;
  gates)  # series voice-charter greps on a chapter file
    f=$B/drafts/ch$N.md; echo "READER STANDARD (banned words, must be 0): $(grep -o -i -w -E 'damn|damned|hell|bastard|bitch|shit|fuck[a-z]*|piss[a-z]*|arse|ass|crap|bloody|goddamn|christ|whore|slut|cock|bugger|sod' "$f" | wc -l | tr -d ' ')"; echo "words: $(wc -w < $f)"; echo "metadata: $(grep -c 'End of Chapter\|approximately.*words\|word count\|DRAFT\|TODO' $f)"; echo "summary: $(grep -ci 'heard about it later\|learned afterward\|was told later\|found out later\|by the time he heard' $f)"; echo "modern: $(grep -ciE 'okay,? so|literally|basically|gonna' $f)"; echo "feel/grow: $(grep -ciE 'felt (sad|angry|afraid|happy|a wave of)|realized how much he had (changed|grown)|was no longer the (boy|girl|person) who' $f)"
    for p in "jaw tightened" "laughed once" "without humor" "stomach tightened" "stomach dropped" "There it was" "That was true" "Also true" "sounded almost" "held this" "which was, in its own way" "at the pitch"; do c=$(grep -ic "$p" $f || true); [ "$c" != "0" ] && echo "TIC $p: $c"; done; echo "tics done";;
  close)  # splice and record
    cp $B/drafts/ch$N.md $ROOT/books/book-07-void-roads/chapters/chapter-$N.md && echo "spliced chapter-$N.md ($(wc -w < $B/drafts/ch$N.md) words)";;
esac
