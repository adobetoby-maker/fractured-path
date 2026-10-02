# Repair brief — Book 3, Movement 8 (one consolidated same-author repair)

**Sources.** Two reviews feed this brief, `review-editorial.md` and `review-cold.md`. Both are
by Claude Fable 5.1, fresh context; the cold read saw the manuscript only.

**Verdict.** Both readers say the hearing lands and the ending lands. The cold reader would pick
up Book 4: day one's deliberate loss reads as finished, the pivot comes one line after the gallery
moves on, and the recorder's schedule reading turns a list into suspense. Ilsev's "Cite the
schedule entry" / "There isn't one" earns the ruling, and the narrow ruling in the Compact's flat
voice makes it feel true. What you invented is clean and strong: the pen setting the pace, no mark
for an absence, the sampler, the daughter's struck line. Pre-repair text is frozen in
`pre-repair/`. Repair in reading order, in place, by reading — never by script.

**Rulings on your flags:**
- **Karis asks to read the Power Log (ch60): KEEP.** Book 4 ch1 needs the asking on the page,
  and P5's "three people who know all of it" is only true if it happens here.
- **The first-sitting examinations: ACCEPTED as procedure canon.** Edran and Hobb are the
  respondent's witnesses in the second hour. Quenna and Naveth are officers answering for
  documents the panel calls, with Coss then questioning.
- **Box seven: honoured exactly.**
- **Hobb's whole-term thanks: accepted.**
- **Cutaway lengths: accepted. Do not pad.**
- **The Ember "letting-go" stands as the second rewording.** "Decision point" is reserved as the
  third, in Book 4 ch21.
- **New canon: all accepted,** except Coss's conceded-paper line, which is softened.
- **Packet lines:** restored exactly is "If my argument needed any true thing to be false, it would
  be the wrong argument." (now a protected pattern). Every tag-broken line stays as you wrote it.

**Already applied by the coordinator (do not redo):** editorial line fixes 1–20. Re-read each in
context and smooth any join. They are:
- Wray's line read into the record;
- the LOCKED session-nine binder line, and Karis's pages in week 11;
- "three weeks ago";
- the boxed Ember line trimmed;
- the Hobb simile recomposed;
- the restored argument line;
- Cael speaks "shattered" without brackets (the ruling keeps its brackets as a document read
  verbatim);
- Oona's capitals;
- Coss's unsupported district-archive paper softened;
- the worked-example splits in ch54 and ch57.

**Protect:**
- Yorlan's opening formula, verbatim, both times; "the panel notes it", never "I";
- the deposition lines, as read from ch49;
- "It amends." / "Custom is not code"; the hole answer;
- the box-seven count and the one-volume gap;
- Ilsev's "Cite the schedule entry" / "There isn't one";
- the ruling as read;
- Prynn's gap on the shelf;
- every BOOK_MAP §9 protected line;
- everything invented and named above as clean.

## Priority 1 — Recompose the four source-tracked passages (editorial §5)

Read beside source ch21, ch22 and ch24, these follow the source's beats, order and images, reworded
past the gate:

1. **ch56 s3, after the pivot.** The tool-not-expected image, the crowd as weather, and Coss
   packing "as a day gone to plan".
2. **ch57, the Havel block.** Four images: gallery restless-to-attentive, the room "holding the
   list", the examiner checking for completeness, light moving a bench-length.
3. **ch61 s5, Quenna's list and annex memory.**
4. **The wall's status paragraph.**

Rebuild each from your event list, source closed, with new entry points and your own images. Keep
the events and every protected line. Where the packet fixes an order of beats, keep the order and
change the construction.

## Priority 2 — The ending ends once; clarity (cold read)

- **The ch61 wall scene.** Cut the narrator's paragraph that restates Quenna's four-person forecast
  item by item; the final exchange should follow a silence, not a recap.
- **The nine codas in ch61.** Thin them so the book ends once: the final scene partly repeats the
  one before it. Keep these:
  - Hesk's letter;
  - the Vell letter;
  - Prynn's gap on the shelf;
  - Edran's rematch;
  - "This might actually be enough" / "It always is".
- **"The Warden".** Bind it to Coss at first use in ch55.
- **Three late echoes in ch60–61.** Give each a half-clause of handle without disclosing anything:
  - "Q.'s question";
  - "a box drawn round two lines … in two hands";
  - Karis's Sunday sheet, "So that's where it went".
- **Say it once.**
  - The win is explained as "narrow and jurisdictional" three times (Cael, Coss, Karis). Keep the
    one that lands.
  - The fighter/mason/stone metaphor family for Coss runs a dozen-plus times across ch54–59. Thin it.
- **ch59, "before the gavel had come down a second time".** No strike is shown on day two; fix
  the line or show the strike.

## Priority 3 — ≥40-word share 5.8% → ≤4.5%

Split about forty sentences by reading. They cluster in:
- ch54 s2–s5 (about twenty available);
- ch57 s1 and s5;
- ch55 s3;
- ch60 s2 and s6.

Fixes 17–20 are worked examples. Never split a spoken line. Keep the 67-word "Every Path and every
tier" whole. Hold the sentence mean ≥13 by joining clipped runs where a split leaves them.

**Length.** Finish within 36,000–38,500 words.

## After the repair

Run the checks:
- `editions/monroe-1.3/tools/ed.sh overlap book-03-no-path-given 8` — must stay at 0 unprotected;
- `ed.sh gates`;
- the skeleton probe as in your original task — stay at 5% or below, and aim the close share
  toward ~12%;
- `formula_metrics.py` on the eight chapters.

Then append "## Repair r1" to `AUTHOR-REPORT.md` with:
- before/after metrics;
- overlap and probe results;
- which codas were cut or merged;
- the changelist, by chapter.

Edit only the eight chapter files and AUTHOR-REPORT.md. Run no git commands, not even read-only
ones.
