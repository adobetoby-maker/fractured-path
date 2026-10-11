#!/bin/bash
# usage: counts.sh DIR   (DIR holds chapter-31.md .. chapter-60.md) — read-only target counts for Lane B
D=$1
files=$(for c in $(seq 31 60); do printf "%s/chapter-%02d.md " "$D" $c; done)
cnt() { cat $files | grep -o -i -E "$1" | wc -l | tr -d ' '; }
echo "that_was $(cnt '\bthat was\b')"
echo "which_was $(cnt '\bwhich was\b')"
echo "as_X_had $(cnt "\bas (he|she|they|it|I|we|you|[A-Z][a-z]+|[A-Z][a-z]+'s [a-z]+|the [a-z]+|the [a-z]+ [a-z]+|his [a-z]+|her [a-z]+|their [a-z]+|a [a-z]+|a [a-z]+ [a-z]+) (had|has)\b")"
echo "at_once $(cnt '\bat once\b')"
echo "pauses $(cnt "\bfor a (long )?(moment|while|breath|time)\b|\bafter a (long )?(while|moment|time)\b|\bfor some time\b|\bfor a count of\b|\bfor the (length|space|count) of\b|\ba breath's length\b|\bfor (one|two|three|four|five|six) (breaths?|counts?)\b|\bfor a (slow )?count\b")"
echo "looks $(cnt "\blook(ed|s|ing)? [^.;:!?]{0,60}\b(once|twice|again|a second time)\b|\b(second|third) look\b|\blooked (once|twice|again)\b")"
echo "hand $(cnt '\bhands?\b')"
echo "count $(cnt '\bcount(s|ed|ing)?\b')"
echo "enter $(cnt '\benter(s|ed|ing)?\b|\bentry\b|\bentries\b')"
echo "price $(cnt '\bpric(e|es|ed|ing)\b')"
echo "cost_bill $(cnt '\bcost(s|ing)?\b|\bbill(s|ed|ing)?\b')"
echo "let_it_stand $(cnt '\blet (it|that|them|this) stand\b')"
echo "put_set_by $(cnt '\b(put|set) (it|that|them|this) by\b')"
echo "as_if_though $(cnt '\bas (if|though)\b')"
echo "words $(cat $files | wc -w | tr -d ' ')"
