# Repair brief — Book 2, Movement 2 (one consolidated same-author repair)

**Sources and verdict.** This brief consolidates `review-editorial.md` and `review-cold.md`, both
written by Sol, the edition's review seat (the cold read saw the manuscript only). Both reviewers
would continue, scoring keep-reading at 9 and 9/10. They name these as the strongest moments:
- the stranger stepping into the ten-degree blind spot;
- "You're writing the wrong things.";
- Lira's clock fight;
- the unsigned middle line ("The line between them had nobody's.").

Source distance is clean (probe 1%, overlap 0). Pre-repair text is frozen in `pre-repair/`.
Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags

- **Packet quote changed by one word:** keep as written.
- **"The clock":** accepted as an Ironyard epithet, not a name. The owner may override it.
- **Calendar:** late autumn before midwinter, with no months named, is the edition's calendar.
  BOOK_MAP §11 s is reconciled to it.
- **Cutaway share (16% this movement):** accepted. The book-level share is about 9%.
- **New canon:** all accepted, with one exception — Havel's count of earlier files (Priority 1).

## Priority 1 — Canon: Havel's comparison files (editorial)

Ch14 l.201 ("He had handled five files of this classification in four years… A [SHATTERED] f…")
and ch15 l.237 ("He had handled five files of this class") imply five earlier `[SHATTERED]`
subjects. Canon has four before Cael, all dead within weeks (UNIVERSE_BIBLE; Book 1 ch4/ch6;
Book 2 ch4).

Re-found Havel's basis for comparison so it fits canon, for example:
- the four archived historical files he has read;
- or thin passive-monitoring files of other kinds.

Keep the inference that a thin file means somebody keeps it thin. Keep the implication that no
earlier subject lived long enough to be monitored. Nothing reserved may be disclosed.

## Priority 2 — Say it once (cold read and editorial)

- **ch12, from "There were hooks in the margins…"** through the forged hinge, the gaze-cost
  measurement and Keth. Compress the repeated definitions and conclusions. Keep every causal
  discovery, every physical demonstration and the ten-degree payoff.
- **ch13, after "You're writing the wrong things".** Let the what/when/why insight land sooner:
  - remove or combine a few explanatory echoes;
  - keep Dessa as the live test and at least one older-page reinterpretation;
  - keep the sharp final recognition that Cael himself can be watched.
- **The ch14 Havel cutaway and ch15's market approach.**
  - Add the lightest temporal handrail at ch15's opening, so it reads as a braid, not a rewind.
  - Tighten only the duplicated orientation and observation, so each view adds what the other
    cannot: Havel's procedural foreignness, Cael's tactical reading.
  - Consolidate the final Havel cutaway's repeated market interpretations.
  - Keep both viewpoints and the marker decision.

## Priority 3 — Rhythm (editorial)

Sentence mean 12.42 (range 13–15.5); ≥40-word share 1.5% (range 2.5–4.5%). Do a
sentence-by-sentence pass:
- join runs of narration that are one thought;
- add a limited number of clearly hierarchical long sentences (aim for about 3%);
- concentrate this in Cael's reflective passages, Havel's procedural passages, and the set-ups
  in ch12–15.

Never split or join speech. Keep the fight beats short. Tags: you brought them to about 59 per
10k; drop more only where the speaker is plainly clear.

**Length.** Finish within 34,500–36,500 words.

## After the repair

- Run `ed.sh overlap book-02-iron-circuit 2` (must stay at 0 unprotected), `ed.sh gates`,
  `tools/sweep_probe.sh book-02-iron-circuit 2 2` (must not rise; the source resolver is now
  fixed) and `formula_metrics.py` on ch9–15.
- Append "## Repair r1" to `AUTHOR-REPORT.md`: before/after metrics, Havel's new basis, and a
  changelist by chapter.
- Edit only ch9–15 and the report. Run no git commands.
