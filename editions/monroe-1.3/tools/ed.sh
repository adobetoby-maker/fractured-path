#!/usr/bin/env bash
# Monroe 1.3 / O'Connor 1.3 edition driver for The Fractured Path.
#
#   ed.sh compile BOOK N START COUNT [PREV]   compile movement N prompt (Opus author)
#   ed.sh review  BOOK N                      metrics + compile editorial and cold-read reviews (REVIEW_SEAT=codex launches Sol)
#   ed.sh wait    BOOK N                      block until both reviews exist or their codex runs die
#   ed.sh show    BOOK N                      print both review files' heads
#   ed.sh gates   BOOK N                      reader-standard / metadata / modern-register greps
#   ed.sh metrics BOOK N                      formula metrics for the movement's chapters
#   ed.sh overlap BOOK N                      source-reuse runs (10+ words) for the movement
#   ed.sh words   BOOK                        per-chapter and total word counts for the edition book
#
# BOOK is the directory name, e.g. book-03-no-path-given. N is the movement number.
# The movement's chapter range is read from state/movement-NNN/range (written by compile).
set -euo pipefail
ROOT=/Users/drive/fractured-path-monroe13
ED=$ROOT/editions/monroe-1.3
COMPILER=/Users/drive/penname/pennamecodexv3/scripts/build_oconnor_prompt.py
cmd=${1:?command}; BOOK=${2:?book}
B=$ED/$BOOK
pad() { printf "%03d" "$((10#$1))"; }

chapters_of() { # N -> absolute chapter paths for the movement
  local st="$B/state/movement-$(pad $1)"; read -r s c < "$st/range"
  for ((i=s; i<s+c; i++)); do printf "%s\n" "$B/manuscript/chapter-$(printf %02d $i).md"; done
}

case "$cmd" in
  compile)
    N=${3:?n}; S=${4:?start}; C=${5:?count}; PREV=${6:-}
    st="$B/state/movement-$(pad $N)"; mkdir -p "$st"; echo "$S $C" > "$st/range"
    args=(movement --root "$ROOT" --author opus --book-id "fractured-path-$BOOK-monroe13"
          --series-id fractured-path-monroe13 --packet "editions/monroe-1.3/$BOOK/packets/MOVEMENT-$(pad $N).md"
          --start "$S" --count "$C" --chapter-dir "editions/monroe-1.3/$BOOK/manuscript"
          --context editions/monroe-1.3/EDITION_BRIEF.md --context "editions/monroe-1.3/$BOOK/BOOK_MAP.md"
          --context "editions/monroe-1.3/$BOOK/STATE_LEDGER.md" --context universe/CANON_RULES.md
          --output "${st#$ROOT/}/compiled-prompt.md")
    [ -n "$PREV" ] && args+=(--previous "$PREV")
    (cd "$ROOT" && python3 "$COMPILER" "${args[@]}")
    echo "compiled: $st/compiled-prompt.md ($(wc -c < "$st/compiled-prompt.md") bytes); chapters $S..$((S+C-1))"
    ;;
  metrics)
    N=${3:?n}; python3 "$ED/tools/formula_metrics.py" $(chapters_of "$N") ;;
  gates)
    N=${3:?n}
    for f in $(chapters_of "$N"); do
      [ -f "$f" ] || { echo "MISSING $f"; continue; }
      rs=$( (grep -o -i -w -E 'damn|damned|hell|bastard|bitch|shit|fuck[a-z]*|piss[a-z]*|arse|ass|crap|bloody|goddamn|christ|whore|slut|cock|bugger|sod' "$f" || true) | wc -l | tr -d ' ')
      md=$(grep -c -E 'End of Chapter|approximately.*words|word count|DRAFT|TODO|\[LEAD\]|\[FRIEND\]' "$f" || true)
      mo=$(grep -ciE 'okay,? so|literally|basically|gonna' "$f" || true)
      printf "%s words=%s reader_standard=%s metadata=%s modern=%s\n" "$(basename "$f")" "$(wc -w < "$f" | tr -d ' ')" "$rs" "$md" "$mo"
    done ;;
  review)
    N=${3:?n}; st="$B/state/movement-$(pad $N)"
    CH=(); while IFS= read -r line; do CH+=("$line"); done < <(chapters_of "$N")
    for f in "${CH[@]}"; do [ -s "$f" ] || { echo "missing chapter $f"; exit 1; }; done
    python3 "$ED/tools/formula_metrics.py" "${CH[@]}" > "$st/metrics.txt"
    python3 "$ED/tools/source_overlap.py" --book "$ROOT/books/$BOOK" --map "$B/BOOK_MAP.md" --allow "$B/protected-patterns.txt" \
      "${CH[@]}" > "$st/source-overlap.tsv" 2> "$st/source-overlap.summary" || true
    rel=(); for f in "${CH[@]}"; do rel+=(--chapter "${f#$ROOT/}"); done
    (cd "$ROOT" && python3 "$COMPILER" review --root "$ROOT" --author opus "${rel[@]}" --formula-check \
       --context editions/monroe-1.3/EDITION_BRIEF.md --context "editions/monroe-1.3/$BOOK/BOOK_MAP.md" \
       --context "editions/monroe-1.3/$BOOK/STATE_LEDGER.md" --context universe/CANON_RULES.md \
       --context universe/UNIVERSE_BIBLE.md --context "editions/monroe-1.3/$BOOK/packets/MOVEMENT-$(pad $N).md" \
       --output "${st#$ROOT/}/review-editorial-prompt.md")
    (cd "$ROOT" && python3 "$COMPILER" review --root "$ROOT" --author opus "${rel[@]}" \
       --output "${st#$ROOT/}/review-cold-prompt.md")
    for kind in editorial cold; do
      w="$st/review-$kind-wrapper.md"
      {
        echo "You are the review seat for a Monroe Jackson 1.3 / O'Connor 1.3 movement of The Fractured Path."
        echo "Do not modify any repository file. Read the compiled review prompt below in full and follow it exactly."
        if [ "$kind" = editorial ]; then
          echo "This is the EDITORIAL pass (continuity/story + numerical formula alignment). Canon evidence is supplied."
          echo "Measured formula metrics for these chapters (tools/formula_metrics.py; method in its docstring) are below — use them; do not re-estimate:"
          echo '```'; cat "$st/metrics.txt"; echo '```'
          echo "Also check the Reader Standard (thirteen-year-old reader; see EDITION_BRIEF) and every protected-wording line in BOOK_MAP that falls inside this movement."
          echo "Source reuse (tools/source_overlap.py; runs of 10+ words shared with the current edition, protected wording excluded) — $(cat "$st/source-overlap.summary"). Full list: $st/source-overlap.tsv. Any unprotected reuse is a finding; the edition's prose must be new."
        else
          echo "This is a fresh-context COLD READ: manuscript only, no canon. Label it a simulated cold read, not a real audience measurement."
        fi
        echo "Write your complete review as markdown to: $st/review-$kind.md (create that one file; nothing else)."
        echo "End it with a section '## Repair brief' giving at most three priorities, each with location, observed issue, effect on the reader, proposed scope, and a strength to preserve."
        echo; echo "--- COMPILED REVIEW PROMPT FILE: $st/review-$kind-prompt.md (read it in full) ---"
      } > "$w"
      if [ "${REVIEW_SEAT:-agent}" = codex ]; then
        nohup codex exec --cd "$ROOT" --skip-git-repo-check -o "$st/review-$kind.lastmsg.md" "$(cat "$w")" \
          < /dev/null > "$st/review-$kind.stdout.log" 2>&1 &
        echo $! > "$st/review-$kind.pid"; echo "launched Sol $kind review pid $(cat "$st/review-$kind.pid")"
      else
        echo "compiled $kind review: wrapper $w (launch with an Agent seat; REVIEW_SEAT=codex uses Sol)"
      fi
    done ;;
  wait)
    N=${3:?n}; st="$B/state/movement-$(pad $N)"
    for kind in editorial cold; do
      until [ -s "$st/review-$kind.md" ] || ! kill -0 "$(cat "$st/review-$kind.pid")" 2>/dev/null; do sleep 30; done
      echo "$kind: $( [ -s "$st/review-$kind.md" ] && echo "written ($(wc -w < "$st/review-$kind.md") words)" || echo "codex exited without a review file")"
    done ;;
  show)
    N=${3:?n}; st="$B/state/movement-$(pad $N)"
    for kind in editorial cold; do echo "=================== $kind"; sed -n '/## Repair brief/,$p' "$st/review-$kind.md" 2>/dev/null | head -60; done ;;
  overlap)
    N=${3:?n}; CH=(); while IFS= read -r line; do CH+=("$line"); done < <(chapters_of "$N")
    python3 "$ED/tools/source_overlap.py" --book "$ROOT/books/$BOOK" --map "$B/BOOK_MAP.md" --allow "$B/protected-patterns.txt" "${CH[@]}" ;;
  words)
    for f in "$B"/manuscript/chapter-*.md; do [ -f "$f" ] && printf "%s %s\n" "$(basename "$f")" "$(wc -w < "$f" | tr -d ' ')"; done
    echo "total $(cat "$B"/manuscript/chapter-*.md 2>/dev/null | wc -w | tr -d ' ')" ;;
  *) echo "unknown command $cmd"; exit 2 ;;
esac
