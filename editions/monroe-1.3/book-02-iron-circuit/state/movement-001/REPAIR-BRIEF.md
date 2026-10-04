# Repair brief — Book 2, Movement 1 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`. Both are Sol (GPT via codex, ChatGPT plan),
the edition's usual review seat. The cold read is manuscript-only.

**Verdict.** Both readers would continue: "Keep reading" scores 8 and 9. The movement delivers:
- a genuine progression payoff — the landing lock reclassified as a price, and the tenth trial;
- a lived-in district;
- an emotionally credible partnership, with Lira's broom defence and "Not yet. Nearly.";
- two strong hooks: the watcher-Blade, and Lira's step that doesn't stop.

**Clean.** Source distance is the best yet: 0% skeleton, 0 unprotected 8-word runs. The Reader
Standard passes. Brom is absent, the Compact makes no contact with Cael, and no reserved truth leaks.
Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never
by script.

## Coordinator rulings on your flags

Accepted:
- the venue bridge (the Ironyard as the map has it, beside the edition's Cinder House);
- Vell's back room, cupboard and tally;
- Dace's wall;
- the sweep's route;
- Lira's barn instructor and Fenmark line;
- the half-body growth and the giving face;
- the Darrow-right seam reconciliation — the seam is a property of the *asked* burst, and the old Log
  shows the one exception;
- the watcher-Blade hook;
- Lira's night work;
- Hesk's first letter and Cael's reply;
- Darrow and Feryn at one line each (per owner decision #30);
- the two packet quotes you altered by one word — keep them as you wrote them.

Calendar: keep months unnamed, as you did.

## Priority 1 — The counts and the protected notice (editorial)

- **Copper formals.** The entry state is eleven before Ulric, so after Ulric it is twelve. Fix
  Vell's "That's eleven Copper formals this year" (ch1 l.111) and the Log's "eleven Copper formals;
  Ulric" (ch6 l.63).
- **The landing trials.** Ch5 shows ten activations, but the aftermath (ch5 l.273) and the Log
  (ch6 l.77, 85) record nine, matching BOOK_MAP §6.1's "nine bursts in one hour". Make the page
  true. Either one trial visibly does not activate (show it), or the record says ten — but BOOK_MAP
  says nine, so prefer the first.
- **The protected notice.** Ch8 l.17's REVISIONS entry recopies the FRAGMENT UPDATE in an altered
  form ("… Integration: partial (unchanged)."). Reproduce the protected block exactly as ch7
  l.148–150 has it, and put "integration unchanged" in Cael's own sentence outside it.

## Priority 2 — The Log as recap, and the stakes in the sweep (cold read)

- **Ch6 Power Log** (the WIND-ADJACENT field block through the end of the PRESSURE-ADJACENT entry):
  it restates costs, incidents and conclusions already dramatised in ch1 and ch5, then repeats them
  in Cael's reflection. Compress inside the logged evidence. Let one or two representative entries
  establish the form.
  Keep:
  - the six-field architecture;
  - the left-only clue;
  - the depletion ceiling;
  - Pressure's two faces;
  - the concurrent-function question;
  - the tool / self-record distinction.
- **Ch3 sweep** (officers into the market through the lodgers' book) **and ch4** ("Dace says there
  were two grey coats"). Add one or two present-tense sentences of concrete stake — his rooms, his
  circuit access, something already established — without explaining the secret. Keep the fixed
  route, the district making itself small, and "predictably visible is safer".
- **Ch1, after Ulric calls the bout.** Plant one anonymous, precise glimpse of the watcher: a
  spectator who neither cheers nor groans and watches the landing. Don't name him and don't add a
  scene. This pays off in ch8.

## Priority 3 — Rhythm (editorial)

The ≥40-word share is 6.7%; the range is 2.5–4.5%. Split the overloaded narration sentences by
reading, chiefly:
- the ch2 calibration chains and Dace's board;
- the ch6 Log entries (this overlaps Priority 2);
- the dense explanatory paragraphs elsewhere.

Paragraph at genuine thought turns. Hold the sentence mean at 13 or above by joining nearby
clipped narration where a split leaves it. Never split speech. Keep the scene breaks.

**Length.** Finish within 35,500–38,000 words.

## After the repair

1. Run `editions/monroe-1.3/tools/ed.sh overlap book-02-iron-circuit 1` (must stay at 0
   unprotected), `ed.sh gates`, `tools/sweep_probe.sh book-02-iron-circuit 1 1` (must not rise)
   and `formula_metrics.py` on the eight chapters.
2. Append "## Repair r1" to `AUTHOR-REPORT.md` with the before/after metrics, the trial-count
   choice and a changelist by chapter.
3. Edit only the eight chapter files and AUTHOR-REPORT.md. Run no git commands.
