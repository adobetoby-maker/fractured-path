# Repair brief — Book 1, Movement 3 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context;
the cold read is manuscript-only). Both would keep reading — the cold reader "without
hesitation"; lens scores 7–9. No canon violation; Reader Standard passes; source reuse 0;
protected wording exact. Pre-repair text frozen in `pre-repair/`. Repair in reading order, in
place, by reading (no scripted splitting).

**Rulings on your flagged items — all kept:** the mender's piecework, "Red Cap" (a description,
never a name), the Log's Claim / Evidence / Ruling columns with *h*, Lira's morning report, the
opponent descriptions, the pear tree. Lira's cutaway is inside the Book 3 limit and her
knowledge boundary. The first counted instance reads exactly as asked. Vell's "A name goes in
when the yard comes to see it." stays. The four-weeks calendar is correct. (Conditions these
create for Movement 4 are in that packet.)

**Protect:** every exchange of the three losses (Brenna, Amrit Sole, Petra Voss); Petra's "What
were you looking at?" and the shoulder touch; the eleven-attempt drop recreation; "You could
only already be going."; "I'm losing on speed now. Not on seeing."; the Log's columns; every
protected line ("How did you know that was coming?" / "I don't know."; "The circuit doesn't care
what the registry says."; Hesk's Second entry; the notice sentence).

## Priority 1 — Line fixes and one disclosure told twice

- **Exact fixes (editorial review, Priority 2):** ch17 "walked into a circle four times" →
  three; ch18 cutaway "Three weeks later he had told her about her own left foot" → it was four
  mornings later (day 11); ch16 Amrit's "forty years of lifting stockpots" (he is about forty —
  make it his working years); ch17 the day-order wobble around the old man's "Six"; ch19 "two
  things… four weeks"; ch20 Lira's "Nobody in here says you have to leave" contradicts the ch4
  notice ("revoked effective immediately") — keep her "built" point and fix the first sentence
  with a half-line; seed the pear tree in ch14 so it is there before it matters.
- **Calendar, ch17–20 (cold read):** "nearly three weeks" vs "four weeks" wobbles; ch17's third
  section jumps back a day without a signal. Make every marker agree.
- **Lira's registry-lookup disclosure is told twice.** Her "crate of books, less than a pie,
  four lines, reading somebody's letters" is in her ch18 cutaway and again almost word for word
  to Cael in ch20, so ch20's "He had not expected that" has no surprise for the reader. Keep it
  in ch20; in ch18 let her decide to tell him, without the content. The shade reason (set up in
  ch14 as hers to give) belongs to ch20 too — take it out of her ch18 interior.
- **Power limit:** Petra's Force shows no cost across seven exchanges; one line (a shaken wrist,
  a flexed hand) settles the Bible's provisional Force recoil.

## Priority 2 — What an audiobook hears twice

- "The circuit doesn't care what the registry says" appears three times plus the chapter
  title. Keep the protected line once, where it lands hardest; the title may stay.
- Vary the post-bout ritual once across ch15–17: "At the table, Vell's pen moved" / "At the rope
  the noise had changed" / the water-bucket debrief / the walk home with Lira repeat identically
  after Brenna, Amrit and Petra. Change one instance's shape; keep each debrief's content.
- The voice-won't-hold beat (ch17 after Vell; ch20 after Lira) — keep one. The two horse
  similes (ch17, ch18) — keep one. Ch19's anaphora ("He thought about…" ×7) — keep the
  shape, cut it to three or four. Thin the "almost smiled / almost laughed" cluster. "Boop." is
  your call.

## Priority 3 — Rhythm, by reading

Measured: mean 11.33 / median 7 (14.6 / 11); ≤5-word 35.8% (~28%); ≥40-word 2.7% (3.3%); 836
words per scene; paragraph median 24 (~18); FK 3.2; ~92 tags per 10k. Work the narrative runs
between beats — ch17 after the wager and after the bout; ch19's ledger meditation; ch20's
closing reflection; ch15 around Baro — joining clipped statements that are one thought into
full, well-built sentences, and add a few deliberate long sentences where an action or thought
earns them. Drop tags in two-person scenes where the speaker is clear. Break the longest
reflective paragraphs in ch18–19 where the thought turns. Leave the fights' beats and Lira's
clipped speech alone.

**Length.** Finish within 35,000–37,000 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-01-the-shattered 3` (must stay 0
unprotected) and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the seven chapters,
then append "## Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, overlap summary,
changelist by chapter). Edit only the seven chapter files and AUTHOR-REPORT.md.
