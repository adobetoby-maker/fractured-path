# Repair brief — Book 1, Movement 1 (one consolidated same-author repair)

Sources: `review-editorial.md` (Fable 5.1, fresh-context editorial pass with canon and
measured formula) and `review-cold.md` (Fable 5.1, manuscript-only simulated cold read).
Both reviewers would keep reading. The pre-repair edition is frozen in `pre-repair/`.
Repair in reading order, in place. Do not shorten the developed scenes: the low-wall
tussle, the Tuesday reel, the eleven-second count, the depot, the cart, the rise.

## Coordinator rulings on the reviewers' open questions

- Hesk's "I was younger than you'd think" Ardenmere visit is in source Ch3 (line 177).
  **Keep it.**
- The Arbiter after the word must be **dark**, not dim — BOOK_MAP §1's binding end state
  ("dark since the word") and Movement 3's staging depend on it. The cat-in-a-chair image
  may move somewhere it can stay.
- The Ch2 reel's "circuit" / "circuit rating" for a sanctioned regional competition
  collides with the word BOOK_MAP §6 reserves for Vell's unofficial ladder. Rename the
  reel's competition in plain words (for example "the regional bracket", "a sanctioned
  rating") so "circuit" first means Vell's ladder in Movement 2.

## Priority 1 — Change gear: rhythm and reading level, all six chapters

Measured (tools/formula_metrics.py): sentence mean 8.77 (target 14.6); ≤5-word sentences
41% (target ~28%); ≥40-word 0.3% (target ~3.3%); FK 2.8 (target 6.8); 717 words per scene
(target ~950); reporting verbs ~111/10k (target ~41). Paragraph median 15 is close — keep
paragraphs short.

- Join runs of three or four clipped statements that are one thought into compound and
  complex sentences with a clear hierarchy. Concentrate first on the thought-runs the
  editorial review names: Ch1 Tallow Lane; Ch4 the archive and the walk home; Ch5 the walk
  to the depot; Ch6 the wall reading and the second day.
- Give each chapter three to five deliberately long, readable sentences (forty words or
  more) where an action or a thought earns them — the bracket test, the light on Lantern
  Street, the fires coming out.
- Merge about ten of the 35 scene breaks (Ch5's nine first, then Ch3's seven).
- Drop "said" where a two-speaker run already makes the speaker clear.
- **Protect the landings** — they are the ~28% the formula wants: the eleven-second count;
  "Joren sat down in the street."; "He went."; "Go on," the guard said; the page-seven list;
  "That," he said, "is the right answer." / "Then I'll take it." / "Four."

## Priority 2 — Continuity, canon and rule gaps (line-level)

- Calendar around the inserted Day 1: Ch4 "in the side room yesterday" and "Yesterday
  morning his number…" → two days ago; Ch5 "Two nights ago…" (×2) → four nights ago;
  Ch5 "Yesterday. I said I would." → the day after. Check every other time word.
- Ch3: Alis never described her classification as arriving "in her chest before her ears"
  — cut it or give it to someone who did. Cut the doublet "behind his breastbone, behind
  his sternum".
- Ch3: the sigil goes dark after the word (ruling above).
- Ch2: the reel's competition renamed off "circuit" (ruling above).
- One sentence each, wherever it reads most naturally (cold read): what triggers a
  Kindling (Ch1 "Path woke" vs the Ch3 circle — "in the circle" in passing will do); a
  baseline for "eleven seconds late" against Pellin's "three to fifteen minutes"; why Cael
  must leave Denvash rather than live in its own Unranked quarter.

## Priority 3 — Say it once, and use the room for story (Ch3–6)

- The middle run of Hesk and Cael two-handers (Ch3 tea → Ch4 workshop → Ch4 bedroom →
  Ch5 breakfast → Ch5 depot) replays the same emotional transaction. Give each of these
  scenes a different job — information, a practical task, a joke, a refusal, a gift — so no
  two land the same beat. Fold the bedroom Ardenmere briefing into the Ch3 tea; keep the
  bracket gift and "I didn't do something else" exactly.
- Un-double the Tuesdays realization: it should arrive once, in Ch6 with the leather book,
  where it is the movement's one new turn. In Ch3 the side room may let Cael *almost*
  connect it, or not at all; the letter should not restate it.
- Refrains: keep one "Perform competence" (the carter scene), one "dead within weeks" in
  Ch6 (the rise), and cut the third "your body will learn before your mind does" and the
  extra "still finding out" (keep the carter scene's coinage and its laugh). Thin the
  "He noted that / He filed it / He made himself" paragraph-closers where the sentence
  before already shows the noticing. Halve the "the way…" simile tails, keeping the ones
  that do character work.
- Ch6: quote each notebook entry in full (protected) but give Cael one reflection per
  entry, not one per sentence. On the second day keep the hawk, the sheep and the climb,
  and replace the recount of the four with the one new thought ("*Weeks.* Not years.").

**Length.** The movement's budget is ~30,000 words and the book needs its full 300,000.
Where you cut recap, use the room for something new on the page that the brief already
allows (a Denvash moment, an incident of the road, Cael and Hesk doing a task together)
— chapters 2 and 5 run short and can take it. Never pad. Aim to finish within
28,500–31,500 words.

## After the repair

Re-run `python3 editions/monroe-1.3/tools/formula_metrics.py` on the six chapters and add
the before/after numbers, the rulings applied, and a short changelist (by chapter) to the
end of `AUTHOR-REPORT.md` under "## Repair r1". Edit only the six chapter files and
AUTHOR-REPORT.md.
