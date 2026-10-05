# Repair brief — Book 2, Movement 4 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`. Both are by Sol, the review seat; the cold read saw the manuscript only.

**Verdict.** Both reviewers would continue (the editorial reviewer "without hesitation"). Things to keep:
- The Brom bout fails honestly by Movement 3's mechanics.
- Cael calls the loss himself.
- The new three-person relationship.
- The *Carrying* column and its emptiness.

Source distance is clean: probe 1% / 12%, overlap 0. Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags

**The plan's failure — ACCEPTED as honouring "the lag was the post's wood":**
- The recovery is real, but each hard answer throws Cael out of reach of the gap.
- Half the gap he timed was the rope swinging the post back.
- Against fast men, Brom breathes on his read, not on contact.

**Also accepted:**
- Cael lifting his own hand: "Called. Hand up. Fourth exchange."
- New canon:
  - **the "lean"**, a first-touch tell of stop versus send-back, which Brom didn't know and can fake at about a beat's cost;
  - **Iron-adjacent opening once, unasked,** on Lira through the wall, and shut at once;
  - **the "Carrying" Log column.**
- The texture: the twice-kept main-floor book, 26 lamps, about four hundred in the crowd, the lead seam.
- Lira keeps her distance from Brom ("I like him" reserved for M5).
- The three packet lines reworded for the gate. None is quoted in a later book, so keep them as written.

## Priority 1 — The spoken word, and Brom's cutaway (both reviews)

1. **ch26, market wall: `"I'm [SHATTERED]," said Cael.`**
   - The edition's convention: brackets and capitals only in documents read verbatim. Spoken, it is the plain word, as in Book 3 ("Where's shattered?").
   - Make it Cael saying the word himself, unbracketed.
   - Check the rest of ch23–29 for any other spoken or thought bracketed token.
   - Keep the reciprocal disclosure exactly as it stands.
2. **ch25, Brom's cutaway** (from the opening / "Brom had known what the boy was carrying from the first blow" through "Then the third exchange" and the replay).
   - Cut the re-summary of exchanges one and two, and of the disappearance, which ch24 has just rendered.
   - Reach Brom-only knowledge sooner:
     - he throws opponents beyond the gap deliberately;
     - he detects Cael holding Pressure back;
     - his own experience of the third-exchange absence.
   - Keep the cutaway, all of Brom's permitted knowledge, and the full third-exchange interiority.

## Priority 2 — One clean comparison (cold read)

The third-exchange disappearance (ch25) and the new Iron-adjacent read (ch28 notice, ch29 first controlled uses) are different things. The page never sets them side by side, so a reader may take the fragment for the explanation of the anomaly.

Add one brief comparison in Cael's ch28 or ch29 Log reasoning. It should say what each one is and is not, by evidence. Leave the disappearance unexplained, and theorise no source for it.

## Priority 3 — Rhythm and density in ch27–29 (editorial)

- **Restatements.** The fixed-cross explanations and the longer Power Log summaries restate the same touch/hold/turn sequence in equally weighted clauses. Say it once, and let the Log summarise only what is new.
- **Joins.** Join flat runs where they are one thought.
- **Paragraphs.** Break the densest paragraphs at thought turns (paragraph mean ≈41).

Do not touch speech, the notice, or the bout's beats.

**Length.** Finish within 35,500–38,000 words.

## After the repair

- Run:
  - `ed.sh overlap book-02-iron-circuit 4` (must stay 0 unprotected);
  - `ed.sh gates`;
  - `sweep_probe.sh book-02-iron-circuit 4 4`;
  - `formula_metrics.py` on ch23–29.
- Append "## Repair r1" to `AUTHOR-REPORT.md`.
- Edit only ch23–29 and the report. No git commands.
