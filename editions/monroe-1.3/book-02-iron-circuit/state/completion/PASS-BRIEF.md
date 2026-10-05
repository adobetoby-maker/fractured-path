# Book 2 — completion pass, Step 3: same-author texture pass (from the whole-arc read)

**Source.** `whole-arc-read.md` (Claude Fable, a straight read of ch1–60), §§3, 4 and 9, with the counts in
`whole-arc-notes.md`. The book holds as one arc:
- every protected line is exact and placed;
- the consent boundary holds from ch32;
- every tally matches the page;
- the fragment count runs 2 → 3 → 4, with session nine once;
- the Reader Standard is met;
- no month or road-season is named.

**Already applied by the coordinator (do not redo):** the read's 16 line fixes (§8):
- Dace's tenure is twelve years throughout;
- Keth was watched three months throughout;
- Reydan Kindled at fourteen (yard from ten, academy from eleven);
- Red Cap is "he";
- "A year and more ago I came over the hills";
- the letters' home;
- the §8.2 line made whole (ch28);
- "I'll write when I arrive" (ch57);
- the Ulric and clerk's-account memories made true (ch58, ch60).

Re-read each in context and smooth any join.

The pass runs in two lanes. Each edits only its own chapters.

## Both lanes — Priority 1: thin the simile and gesture repertoire (§3, items 1–10)

**Cap similes.** The explanatory "the way a X does Y" (351 in the book) and "as if / as though" (251 + 45) are
capped TOGETHER at three per chapter, and never two on one gesture. Keep the character-specific firsts:
- Brom's builder-grandmother floor (ch16);
- Hesk checking a drawing (ch6);
- Vell's *begin* (ch2).

Cut the rest where the sentence already shows the gesture, or rewrite it in the character's own register. Use
"just as" where a bare "as" could be heard as "while".

**Cut fillers.** Cut "exactly" (168), "plainly" (57), "honestly" (31) and the measured pause ("for a long
time/moment/while" 96, "for a while" 70) wherever the sentence stands without them. Keep exactness where it is the
subject (the straightedge, Vell's lines, Keth's cut). Keep the pauses after session nine and on the stone after
Reydan.

**Give the tags back to their owners.**
- "Did not look up / without looking up" (86) belongs to Vell and Dace again.
- Brom gets one tag per scene, mouth or neck, not both. Keep the first mouth-corner (ch17) and the first red neck
  (ch28).
- "Like a man who…" (32): two or three per movement at most.
- Hand-width measures (27 + 33): keep the fan (ch7), Lira's notched stick, Keth's cut (ch39–40) and Ulric's turn
  (ch58).
- The lock formula: "two *ands*" is a motif and stays wherever a count belongs. "Bright stillness" appears at most
  once per bout.

**Small verbatim repeats** listed under §3: take them first ("as if it owed him money" twice; "as if it had done
something he had not asked it to" five times; "You're grey / Go and eat" works twice, so thin the run).

**Length.** Expect to lose 2,000–3,000 words across the book.

## Lane A — chapters 1–30
- Priority 1, as above. This lane carries the fan, the lock formula's first uses, and Vell's tags.
- Seams (Priority 3): reread ch1–3 for Dace's twelve years and the Ulric silence, and ch28 for the §8.2 beat.

## Lane B — chapters 31–60
- Priority 1, as above. This lane carries Brom's tags, the "like a man who" family, and the "You're grey / Go and
  eat" run.
- **Priority 2.**
  - Lose 600–800 words between Havel's reading of the manual's table (ch33) and Coss's month of opening other men's
    files (ch35). The watcher's three sightings (ch34), the read-back and the knock (ch36) should not be separated by
    three still sections.
  - Keep every beat: the burnt draft, the corridor nod, the index, the fourteen paces.
  - In ch43, add ONE line of Cael's own stake in the last section before the three-week jump to ch44, so the term's
    clock is heard while Lira's loss is paid.
  - Add or remove no scene breaks.
- Seams (Priority 3): reread ch45–50 for Dace's twelve years; ch36–37 and ch45–48 for Keth's three months; ch44,
  ch51 and ch54 for Reydan's ages; ch48 and ch60 for the clerk's account; ch57–58 for Ulric and the promise to
  Hesk. Every quoted or remembered line must point at a real first occurrence.

## Both lanes

**Method.** By reading, in place, never by script.

**Protect.**
- Every protected line (BOOK_MAP §9 and §8 items, quoted exactly).
- The Iron-adjacent and Compression notices.
- Every bout's exchanges and landing beats: Brom (ch24–26), Keth (ch39–40), Bede, Maud, Reydan (ch52–53).
- Session nine and its *Note* line.
- Every tally, count and date, and every line that a later chapter or Book 3 quotes.
- The redirect shoulder is the RIGHT (#36).
- Bede and Maud stay as they are (owner-pending placeholders).

**Count.** Count each target before and after with grep, within your range, and report both.

**After.**
- `ed.sh overlap book-02-iron-circuit N` stays at 0 unprotected for every movement in range.
- `ed.sh gates` stays at 0.
- `tools/sweep_probe.sh book-02-iron-circuit F L` does not rise.
- Run `formula_metrics.py` on your range. Hold the mean ≥ 13.3, ≥40w ≤ 4.5%, and 850–1,050 words per scene.
- Write `LANE-A-REPORT.md` or `LANE-B-REPORT.md` here in `state/completion/`.
- No git commands.
