# Repair brief — Book 1, Movement 6 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the
cold read is manuscript-only). Both would keep reading — the cold reader "for the Lira
conversation about the fragment alone". Four of the six bouts are fresh, each for a different
reason (the kiln boy, Renn by five distinct problems, Sarel by the method collapsing, Corbin by the
truth/lie/truth beat); Dellin is deliberately flat and short enough to work; Talis is where it
blurs. No canon or Reader Standard violation; every coordinator note met; overlap 0; the ch33 seam
is clean. Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by
reading — never by script.

**Rulings on your flags:** length is not a defect — the Renn II, Sarel and Corbin overruns are
earned inside the exchanges; the unearned words are repeated letter quotations and parts of the
Hesk cutaway. Hesk's knowledge limits held exactly. The day-62 opener with two prior watches is
right. All the new canon is approved (Corbin's Shield Path; Sarel's and Talis's details; Lira's
room over the widow's chandler's shop; the guild outcome; Alis without her Path until spring; the
notice's arrival and the deliberate step). Lira's habit and its cost are done as asked.

**Protect:** every decisive exchange of every bout; Renn's five problems; Sarel's collapse of the
method; Corbin's truth/lie/truth; the Lira conversation about the fragment; "mine are mine"; the
notice text; the italic report-voice tallies; "It was five."

## Priority 1 — Counts and line fixes

- ch38 "fought four times" → three (it lists three); ch38 "two weeks ago" (cold-read line 1617)
  against "three weeks ago" elsewhere (1563, 1723) → make them agree (three); ch38 "a week since
  Sarel" on a Thursday → four days; ch36 "never heard of the yard" → never *seen* (the Movement 3
  letter told Hesk about the circuit); ch34 "wrote down later" against the nameless Log entry —
  make them agree.
- The Log's "Seventh/Eighth" entries against the ledger's "five bouts" / "three of seven" (ch34
  near 81 and 357; ch36 near 1109) — make the numbering legible: Log entries count instances and
  events, the ledger counts bouts; say which is which where a reader would trip.
- Corbin's fifth exchange: one clause placing his turned shield arm *before* "Cael was inside".

## Priority 2 — Say it once; make Talis a search

- **Hesk's cutaway** (~5,100 against ~3,000): cut one of the three Dessa-letter readings; don't
  quote the fear paragraph in ch36, since ch39 quotes it. Three letter passages appear verbatim
  twice (Hesk's line ch35/36; the fear ch36/39; Joren and Alis ch36/39) — keep each once, where it
  lands hardest.
- **Aftermath refrains:** "could not find his breath anywhere / he found it", "took two / three
  tries", "Lira not biting her knuckle" repeat verbatim after different injuries (ch35, ch37,
  ch40), and Sarel's look (ch37) copies Renn's (ch35). Keep the Renn instance; write what is
  different about the other two.
- **The Talis bout** (ch38): exchanges 1–3 are the same beat with only the landing spot changing.
  Give each exchange one thing Cael rules out on Talis's body, so the reader feels the search
  empty before the dirt answers. Keep the bout's length and the face-on-the-ground discovery.
- Light trims where words stall: ch38's board re-narration; ch39's montage; ch40's roll-call.
- Total trim across this priority: about 1,500–2,000 words, never inside a decisive exchange.

## Priority 3 — Rhythm, by reading

Mean 11.43 and ≥40-word 1.7% are under the working ranges (words per scene 866 is in range).
In the narrative between beats — walking, watching, letters, the yard — join clipped runs that
are one thought into full sentences, and add three to five long readable sentences per chapter
where an action or thought earns them. Drop "said" where the speaker is clear (~113 per 10k).
Keep speech, Log entries and the fights' landing beats as they are.

**Length.** Finish within 42,500–44,500 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-01-the-shattered 6` (must stay 0 unprotected)
and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the seven chapters, then append "##
Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, overlap summary, the Hesk cutaway's new
word count, changelist by chapter). Edit only the seven chapter files and AUTHOR-REPORT.md.
