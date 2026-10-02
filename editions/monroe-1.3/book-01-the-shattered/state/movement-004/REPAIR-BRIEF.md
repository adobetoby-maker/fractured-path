# Repair brief — Book 1, Movement 4 (light, same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the
cold read is manuscript-only). Both would keep reading "without hesitation"; scores 7–9; the
strongest writing is the ch26 ledger confession and the west-cart ending. No canon or Reader
Standard violation; every packet note met; all three primary rhythm measures in range; overlap
0. The editorial review calls for line fixes only. Pre-repair text frozen in `pre-repair/`.

**Rulings on your flags:** the Vell cutaway (3,343) and the Dessa bout (~3,070) are earned —
do not trim the bout; the post, the clerk's "Torvin's", Vell's "atypical" tally and successor
notes, Doss's details and Alis at the healers' are approved; the old yard-owner's "Four… You
went the long side." is earned; the open items stay open. (Notes for Movements 5–9 are in those
packets.)

**Protect:** the Dessa bout at full length; the honest sort; the ch26 ledger confession; the
west-cart ending; Lira's report; the old man; Dessa's exchange; Vell's line.

## Priority 1 — Line fixes (editorial review)

- Bout count: ch26 "Six bouts, one win" → "Five bouts, one win"; ch27 letter "It was the sixth
  bout" → "fifth". (He has fought five; the Log's entry 6 is not a bout count.)
- Ch24, second Sunday: the tell paragraph says the back foot comes down *before* the frame
  finishes forming, then the next sentence, the Log line and ch25 all say it comes down *late*.
  Fix the word order and punctuation so the bout's one load-bearing fact is said one way.
- Audio clarity: ch21 — state the turn back up the second row so the shadowing geometry holds;
  ch21 — drop the second "cracked" lantern referent; ch23 — reword Marrow's "Iron-rated" so
  "Iron" means only the Path in that chapter (it merges with "the Fenrow Iron" by ear); ch25 —
  trim the four-"back" sentence at the pivot.
- Optional: soften Vell's "not much older than the Wind girl was now".

## Priority 2 — One beat Cael owes (cold read)

Cael learns (ch22 end / ch23 roof) that the carriers' clerk gave up Torvin's as the house with
letters west to Denvash — then never weighs it, Lira is never shown hearing it, and in ch27 he
posts to Denvash through that same clerk without a flicker. Add one short beat (a few lines,
wherever it sits most naturally between ch23 and the ch27 hut) where he and Lira name the
choice and he decides, eyes open — keep posting through the clerk, or not, with a reason.

## Priority 3 — Say the bout once more, not five times

After ch25 the bout is replayed five times. Compress the two replays that add nothing new: the
ch26 Log recap of exchanges 1–3 and the ch27 brothers' retelling. Keep Lira's report, the old
man, Dessa's exchange and Vell's line.

**Length.** Stay within 34,000–35,500 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-01-the-shattered 4` (must stay 0
unprotected) and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the seven chapters,
then append "## Repair r1" to `AUTHOR-REPORT.md` (metrics, overlap summary, where the new beat
sits and what Cael decides, changelist). Edit only the seven chapter files and AUTHOR-REPORT.md.
