# Repair brief — Book 2, Movement 6 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Sol (review seat). The cold read saw the
manuscript only.

**Verdict.** Both reviewers would continue. Keth is the movement's heart: the unpaid ring, the uninvited read
refused, *I like him*. The Keth bout earns its length, changing the problem in every exchange. Bede turns Keth's
warning into a fair loss, and Lira's bout is a second emotional centre, not an afterpiece. The editorial confirms:
- every protected line is exact;
- the pulse goes from one in three to about half, earned on the page;
- the consent boundary holds (the ring, the dock partner, Lira's no-pulse request);
- no reserved truth is prepaid;
- Reader Standard passes;
- overlap is 0 unprotected.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings
- **Bede and Maud (editorial finding 2): closed by policy.** OWNER-DECISIONS #3 lists them as proposals pending
  approval. The edition's standing practice (also used for Book 3's Oona, Hobb and Gerda, decision #12, and for
  Book 4's Abbot and Gwen) is to draft under the screened proposal, so that one find-and-replace applies the
  owner's choice. No change.
- **"Three months" of watching Keth (editorial finding 1): KEEP "three months".** Closed Movement 5 already says
  "Three months of habit had done it" (ch36). Closed text governs over the packet's approximate "four", and no
  later book quotes the figure. No change. Keep all five references consistent with ch36.
- **Your flags.** Accepted:
  1. The four reworded packet lines.
  2. The Keth-bout "first time" as the first calm, cost-free unasked Wind burst.
  3. Bede's third-exchange win, with the rating unmoved.
  4. Coss's officers' table and procedure.
  5. POV share as drafted.
- **Lira (flag 5): ACCEPTED with a boundary.** "Done walking to their gate" means she stops *asking*. Make sure
  nothing in ch43 says or implies she no longer *needs* Fenmark's admission or has chosen Greyvane. Movement 8
  owns both.
- **The scout (flag 6): CUT the name-at-the-door line.** She gives no name at all in Ardenmere. Dace can say she
  wouldn't give one, if a line is needed there.

## Priority 1 — The Keth-bout accounting (cold; medium-high confidence)
The bout as narrated shows eight knocks and four answers:
- exchange two: six knocks, three answers;
- exchange four: two knocks, one answer.

The ch41 Log says *Pulse: nine knocked, five answered.* Because Cael's accounting is presented as exact, make
the page and the Log agree. Either place one more clearly answered knock in the bout (exchange one or three,
where it doesn't disturb the turning beats), or correct the Log to eight and four. Choose whichever reads truer.
Check the movement's other running pulse tallies for the same agreement, including the ch37 opening ratio and
any later restatements.

## Priority 2 — Say it once (cold)
- **ch38.** The validation work (the barge lad, Orvet's woman, the alcove repetitions, the written accounting)
  explains the join/knock relationship several times before the bout. Keep each test's event and result, and
  state the mechanism once, at its clearest point.
- **ch41, the Coss turn.** Add one compact orienting clause where "The word came to Coss secondhand" begins,
  tying him to the file he monitors and his note upward, so a reader re-places him at once. Keep the full choice
  at the officers' table.
- **ch43.** After the bout and Vell's ruling, the honest-measure-versus-official-card point is restated several
  times. Cut one layer of recap, preferably Cael's restatement of Lira's conclusion. Keep Lira's own realization,
  the lamp, Hesk's coat image, the courier hook and the final line ("*I didn't send it. It went.*").

## Priority 3 — Sentence weight, by hand, where you are already working (editorial)
The movement is inside every working range: sentence mean 13.55, ≥40-word share 3.6%, 1,033 words per scene.
But the median is 9 and Flesch-Kincaid is 3.62, near the floor of 3.5–6, so the narration can sound younger than
the crossover register. Meanwhile the long tactical paragraphs still carry heavy load.

In the editorial's named passages:
- ch39, Cael's plan through the smear and Keth's short cut;
- ch40, the false gifts through the strike;
- ch42, Cael building his own page;
- ch43, Lira's catch through the long speech of about 160 words.

There, join runs of clipped narration clauses that are one thought into clearly subordinated sentences, and
split paragraphs only where the thought genuinely turns. Do not touch spoken rhythms, landing beats, or the
length of any fight. Do not add jargon, and do not chase Flesch. Keep the ≥40-word share at or under 4.5%, and
words per scene within 850–1,050. Splitting a long paragraph is fine; adding a scene break is not needed.

**Length.** Finish within 35,000–37,500 words.

## After the repair
Run:
- `ed.sh overlap book-02-iron-circuit 6` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-02-iron-circuit 6 6` (stay ≤ 5% skeleton);
- `formula_metrics.py` on the seven chapters.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- before/after metrics;
- the bout tally as reconciled;
- the changelist, by chapter.

Edit only ch37–43 and AUTHOR-REPORT.md. Run no git commands.
