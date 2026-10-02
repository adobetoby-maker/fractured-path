# Repair brief — Book 1, Movement 8 (one consolidated same-author repair)

Sources: `review-editorial.md` and `review-cold.md` (both Claude Fable 5.1, fresh context; the
cold read is manuscript-only). Both would keep reading — the cold reader "without hesitation", on
"not stopping, and not stopping". Ilsev is the best new character; the flag is the right quiet
escalation; Dessa II is fully trackable; Lira's tin is the emotional peak of the quiet week;
"I've only seen the paper afterward" is the sharpest dread in six chapters. The event-list method
held: the editorial spot-check found Ilsev new prose and about one sentence in eight source-shaped
in the Coss table scene only. Reader Standard passes; protected lines exact; overlap 0. Pre-repair
text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

**Rulings on your flags:** length (+19%) earned — book projects ~315k, no cut; Dessa II at ~3,300
stands (optional ~120-word trim where the clock-tell is explained twice); Hesk's letter on the page
is consistent with BOOK_MAP §7 (M9 must have Cael open it and quote it only as he reads; its "I'll
say so properly when I've found them" must be paid in M9); Coss's knowledge correct; both cutaways
earned (Coss ~3,050 left for M9); all new canon approved **except the Fenrow Tide girl** (Tide is
flow architecture and healing, per ch01's Alis — fixed below).

**Already applied by the coordinator (do not redo):** editorial line fixes 1–10 — ch48 "six weeks
ago" and "three months ago"; ch49 "three months ago"; ch51 "not two weeks ago"; ch53 "three weeks
ago" (the tin); ch49 and ch50 the sweep-code knowledge boundary (Cael never saw Coss's book — the
evidence is now Coss's *I don't know*; the count stays three); ch50 the Fenrow girl without a Path
name; ch49 "Her copy had been cut a long time ago."; ch48 the summons "on Thursday, the day after
tomorrow". Re-read those lines in context and smooth any join they disturb.

**Protect:** every exchange of Dessa II and its landing beats; Ilsev's evaluation and the flag;
"And you're in front of me"; the bread woman's name under the barrels; the old man's yard; Lira's
tin and "I trust Dessa's water cup"; the Pressure tests at the trough; Coss's brown coat, the pin,
the pie nobody eats, the dropped stitch of breath, "I can't see who's walking", "I don't know
anything about a flag" as a true sentence that stops at the edge; "I'm not leaving" decided fast;
Lira's "It's only people"; Hesk's clock and the loose spring; every protected line.

## Priority 1 — Two located story fixes (cold read)

- **ch50, Lira's laugh lands on a line nobody said.** Cael retells "Ilsev telling him to find a
  subject who read less", which Ilsev never says in ch49. Either give Ilsev the line in ch49 (it
  fits after "Then somebody ought to have written Part Six with him in it") or retell a line she
  did say. Keep the laugh and its withdrawal "because he had not laughed".
- **ch53, the threat arrives three times in speech** (Coss's desk, the pie stall, the roof). Cut
  the roof retelling to its first clause and let Lira cut him off, so the third pass is a beat.
  Optional: one concrete, unexplained footprint of "the view" in the three-week summary before Coss
  names it (e.g. somebody at the tollhouse asking which Sundays the Cinder House runs a card) — no
  explanation, Cael need not notice; nothing that implies a maker, watcher or system. Consider
  softening Lira's flat "He doesn't know" so it does not erase what the pie stall's stillness built.

## Priority 2 — Say it once

- **ch52 errand boys** (~900 words): cut by about a third. Keep the thirty-one tickets, "I watched
  you from the post", the two piles that never cross, "Not because I want to", "I didn't carry
  anything that mattered", and the boys sitting closer than people who hated each other needed to.
  Lose either the coin-pushing-and-pie or the renewed bet; compress the ch53 restatement to a
  clause, keeping one callback.
- ch53 Hesk coda: the clock parable is explained twice (his head, then the letter) — keep one.
- Optional: ch48's letter to Hesk recaps the Feryn loss the reader has just lived — trim to what is
  new; Dessa II's clock explained twice (~120 words).

## Priority 3 — Rhythm and source-shaped sentences

- ≥40-word share 5.0% (ceiling 4.5%): split about thirteen of the fifteen narration sentences the
  editorial review names in §10 (ch48 ×2, ch49 ×2, ch50 ×2, ch52 ×3, ch53 ×6) at real turns of
  thought; the ch48 sentence listing what "remain there" would cost stays long. Join ten to fifteen
  clipped narration runs elsewhere so the mean holds ≥13. Drop about thirty "said"s in the three
  two-speaker scenes (Ilsev, the table in ch52, the pie stall).
- ch53 Coss table scene and Log: five source-shaped sentences (editorial §8 and line fixes 11–13).
  Recompose them in your own construction from Coss's idiom (procedure, roads, prints in snow) and
  Cael's Log voice — the reviewer's wordings are offered, not required.

**Length.** Finish within 32,000–33,500 words.

## After the repair

Run `editions/monroe-1.3/tools/ed.sh overlap book-01-the-shattered 8` (must stay 0 unprotected),
`ed.sh gates`, and `python3 editions/monroe-1.3/tools/formula_metrics.py` on the six chapters, then
append "## Repair r1" to `AUTHOR-REPORT.md` (before/after metrics, overlap summary, the Ilsev-line
choice, whether you added the footprint and what it is, changelist by chapter). Edit only the six
chapter files and AUTHOR-REPORT.md. No git commands.
