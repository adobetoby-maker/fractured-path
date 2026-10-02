# The Fractured Path — Monroe Jackson 1.3 edition (O'Connor 1.3 seat)

Owner direction, 2026-10-01: rewrite the whole Fractured Path series through the
O'Connor 1.3 seat on the Monroe Jackson 1.3 foundation, with Claude Opus 5.5 as the
manuscript author, at about 300,000 words per book. When a book is complete, render
every chapter through Breeze and publish it as a new edition. The current edition
stays exactly as it is; this edition is new and recoverable.

Public byline: Monroe Jackson. Seat: `oconnor` 1.3.0. Foundation: Monroe Jackson 1.3.0.
Requested author: Opus (Claude Opus 5.5). Coordinator: this orchestrator session.
Review seat: Sol (gpt-5.6-sol via `codex exec`) — a different model family from the author.

## What "rewrite" means here

This is a retelling at full length, not a copy-edit. The prose is new. The story is the
same series.

**Keep (canon — binding):**
- Every book's spine: the major events, their order and outcomes, who lives and dies,
  the ending state, ages, the calendar where later books depend on it.
- Cael's fragment acquisitions — which fragment, in which book, under what engagement —
  and the counts at each book's close. The system notice texts that later books quote.
- The SECRET reveal schedule in `universe/CANON_RULES.md` and every reserved truth. A
  rewrite may plant more; it may never disclose earlier than the schedule.
- The universe rules, costs and limits in `universe/UNIVERSE_BIBLE.md`.
- Relationships and their turning points as the existing books establish them.
- Lines a later book quotes or calls back (log entries, notices, signature exchanges).
  The book planner lists these as protected wording.

**Change (the point of the edition):**
- Length: about 300,000 words per book (owner). The existing books are 100–125k. The
  extra ~190k comes from: developed fights given room (1,500–2,500+ words when the
  changing problem earns it); learning encounters and training that show effort turning
  into capability; events the current edition summarizes, put on the page; supporting
  cast given private wants, independent decisions and arcs across the formula's 8–10
  person cast; humor and warmth between people; brief POV cutaways; new episodes that
  fit canon and do not alter any book's end state.
- Shape: open-range movements of six or more chapters, one compact brief per movement,
  no per-chapter cards or per-chapter gates. Roughly 55–65 chapters of ~5,000 words per
  book in 7–9 movements; the author owns chapter boundaries.
- Rhythm: the owner-selected numerical formula (compiled into every prompt). Baseline
  of the current edition, measured by `tools/formula_metrics.py`: sentence mean ~17.5
  (target 14.6), paragraph median ~44 words (target ~18), Flesch RE ~67 (target 72.3),
  FK grade ~8.3 (target 6.8). The edition should move toward the targets.
- POV: about 87% Cael, about 13% brief purposeful cutaways spread over 4–5 named
  characters. Cutaways may never reveal what a reserved-truth boundary withholds.

## Non-negotiable

- **Reader Standard (Gate 27, owner):** written for a thirteen-year-old. Clean language
  (no profanity, obscenity, crude slang or blasphemy, including "damn", "hell" as an
  oath, "bastard" and softer cousins); moral goodness (honesty, courage, loyalty,
  restraint, care for the weak, at a cost; wrong named as wrong; cruelty never
  rewarded); violence with cost, fear and consequence and no gore; no sexual content
  or innuendo. Outranks every voice preference. See `craft/VOICE_CHARTER.md` end section.
- **Names:** keep every existing canon name. The registry's flagged collisions
  (Vell/Velmere, the -vane cluster, Wray/Greyvane, Bracken/Brom) are the owner's call
  and are NOT renamed in this edition. New minor characters the expansion needs may be
  named by the planner, screened by ear against `craft/NAME_REGISTRY.md`, and listed
  under "Names pending owner approval" in the book map. Never invent a name for an
  existing canon role.
- **Audio-first:** this ships as an audiobook. Clear referents, clear attribution,
  names distinct by ear, punctuation that exposes meaning.

## Where things live

- Canon (read-only for this edition): `universe/UNIVERSE_BIBLE.md`,
  `universe/CANON_RULES.md`, `universe/STATE_LEDGER.md`, `craft/NAME_REGISTRY.md`,
  `craft/VOICE_CHARTER.md`, `series/THE_FRACTURED_PATH_SERIES.md`.
- Source edition (the story being retold): `books/<book>/CHAPTER_ARCHITECTURE.md` and
  `books/<book>/chapters/chapter-NN.md`. Read them for events, not for sentences.
- This edition: `editions/monroe-1.3/<book>/` — `BOOK_MAP.md`, `STATE_LEDGER.md`,
  `packets/MOVEMENT-NNN.md`, `manuscript/chapter-NN.md`, `state/movement-NNN/`.
- Series-level edition maps: `editions/monroe-1.3/SERIES_MAP.md`, `CHARACTERS.md`.
- Metrics: `python3 editions/monroe-1.3/tools/formula_metrics.py <chapters...>`.

## Rhythm calibration (measured, 2026-10-01)

Book 1 Movement 1 — the first movement drafted from this brief — overshot the formula in
the short direction: sentence mean 8.8 words (target 14.6), 41% of sentences at five
words or fewer (target ~28%), 0.3% at forty-plus (target ~3.3%), Flesch-Kincaid grade 2.8
(target 6.8), about 106 dialogue tags per 10k words (target ~41). Paragraph median (15)
and scene spacing were close. So, when drafting:

- Let thought, action and description run in full, well-built sentences. Compound and
  complex sentences with a clear hierarchy are the house texture, not the exception.
- Join a run of three or four clipped statements into one sentence when they are one thought.
- Keep short sentences for beats that land — a recognition, a hit, a turn — not as default.
- Give each chapter a few deliberately long, readable sentences (forty words or more)
  where an action or a thought earns the length.
- Drop "he said" / "she said" when the paragraph already makes the speaker clear.
- Keep short paragraphs (median ~18 words) and scene breaks about every 950 words.

## No scripted prose surgery (2026-10-01)

Rhythm and length repairs are done by reading, sentence by sentence, never by a script that
splits sentences or paragraphs at clause or sentence boundaries. Two repairs did that and
each needed a recheck to find the splits that broke a thought. Where the formula and a
character's speech disagree, keep the speech: one-to-three-word dialogue lines and the short
landing beats of a fight are not drift to be repaired.
