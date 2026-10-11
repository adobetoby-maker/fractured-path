#!/bin/bash
# usage: count.sh DIR  -> per-pattern totals over chapter-01..30 in DIR (read-only)
D=$1
files=$(for i in $(seq -w 1 30); do echo $D/chapter-$i.md; done)
c() { cat $files | grep -o -i -E "$1" | wc -l | tr -d ' '; }
printf "that_was\t%s\n" "$(c '\bthat was\b')"
printf "as_X_had\t%s\n" "$(c '\bas (he|she|they|it|we|I|you|[A-Z][a-z]+|the [a-z]+|his [a-z]+|her [a-z]+) (had|would have|might have)\b')"
printf "which_was\t%s\n" "$(c '\bwhich was\b')"
printf "at_once\t%s\n" "$(c '\bat once\b')"
printf "measured_pause\t%s\n" "$(c '\bfor a (moment|while|breath|count|long moment|long while|little while|second)\b|\bafter a (while|moment|breath|time)\b|\bfor some time\b|\bfor a count of\b|\bfor the length of\b|\ba breath.?s length\b')"
printf "looks\t%s\n" "$(c '\blook(ed|s|ing)? [^.;:?!\n]{0,60}\b(once|twice|again|a second time)\b|\b(second|another|long) look\b|\blooked (once|twice|again)\b')"
printf "hand\t%s\n" "$(c '\bhands?\b')"
printf "count_family\t%s\n" "$(c '\bcount(s|ed|ing)?\b')"
printf "enter_family\t%s\n" "$(c '\b(enter(s|ed|ing)?|entry|entries)\b')"
printf "price_family\t%s\n" "$(c '\bpric(e|es|ed|ing)\b')"
printf "bill_cost\t%s\n" "$(c '\b(bill(s|ed|ing)?|cost(s|ing)?)\b')"
printf "let_it_stand\t%s\n" "$(c '\blet (it|that|them) stand\b')"
printf "put_set_by\t%s\n" "$(c '\b(put|set) (it|that|them) by\b')"
printf "as_if_though\t%s\n" "$(c '\bas (if|though)\b')"
printf "words\t%s\n" "$(cat $files | wc -w | tr -d ' ')"
