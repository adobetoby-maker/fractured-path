# AUTHORSHIP — Book 2, Movement 7 "Two Weeks" (chapters 44–51)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-02-iron-circuit/state/movement-007/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-02-iron-circuit/packets/MOVEMENT-007.md`, as compiled) |
| Coordinator rulings | Eight binding rulings delivered with the task (no new names; the consent boundary; session nine once, limits as packeted; pulse figures exact and earned; Lira provisional, Greyvane reserved; "declaration" reserved for the Arbiter, "Shattered" plain; protected wording from the map; Reader Standard and Reydan's facts) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 2 — Iron Circuit |
| Chapters | `editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-44.md` … `chapter-51.md` |
| Date | 2026-10-05 |

**One author, one run.** All eight chapters were written by this model in a single session. No other agent or model touched them, and no subagent was used.

**Reading before drafting.**
- The compiled prompt in full: profile, formula sections 2–6 and 8–9, the packet, the edition brief, BOOK_MAP §§1–12, STATE_LEDGER through "After Movement 6" with every coordinator ruling, CANON_RULES, the owner voice.
- The end of Movement 6: ch42 and ch43 in full.
- M6's AUTHORSHIP and AUTHOR-REPORT, for the report structure.
- Source `books/book-02-iron-circuit/chapters/chapter-18.md`, `chapter-19.md`, `chapter-20.md`, each read once, in full, and then closed. None was reopened.
- Book 3 ch1 and Book 7 ch14/ch24, by grep, for the session-nine lines only (the *Note* line; "Brom's sparring circle that one afternoon"; "no Tide practitioner in the city, at no stakes").
- For continuity, by grep and short reads: Brom's redirect invention (ch16), the taking face (ch6, ch19), the dock partner's history (ch1, ch6, ch10, ch20, ch24), the cookshop and the landing table (ch41), Hesk's workshop (Book 1 ch1–4), Sarel and Talis's ranks (universe ledger), Ansel's registry entry (NAME_REGISTRY), the canon of Reydan's appearance in source ch21–24 (one grep line, for description only; nothing from M8 was used).

**Method.**
1. After the single read of each source chapter I wrote a private event list in my own words in the scratchpad outside the repo (`m7-event-list.md`): first the source's bare events, then my own calendar, tallies and chapter plan for 44–51.
2. I drafted forward from that list and the book map, with the sources closed. Entry points and beat order are mine: the movement opens on Cael at the kitchen table the evening Reydan arrives; the cutaway follows Reydan in at the door; Dace's courier from M6 becomes the cause of the trip; Lira's schedule is a charcoal grid on a carter's bill; Brom finds Ansel through the dock partner; the redirect grows out of Brom's own invention; Lira links the clerk's "declined to be interesting" to Maud; Ansel's round is a public test of patience; a short second Reydan piece precedes the bout.
3. Protected wording (BOOK_MAP §8 items 5, 10, 28, 29 and §3 B6) was copied from the map only.
4. Quoted packet lines that are not in BOOK_MAP and would have shared eight or more words with the source were re-composed (see AUTHOR-REPORT, Checks).

**Per-chapter probe, as instructed.** After each chapter, before starting the next, I ran `skeleton_probe.py --source` the three source chapters `probe_sources.py` resolves for this packet (ch18, ch19, ch20) on that chapter, plus `source_overlap.py --min 8` and `formula_metrics.py` on the same chapter, through a scratchpad helper. Results and rebuilds are tabled in AUTHOR-REPORT. One chapter (ch45) went over the bar on first draft: its supper scene had followed the source's common-room scene from memory (18% skeleton in the scene, 7% in the chapter). The scene was rebuilt from the event list before ch46 was begun.

**Blocking slips fixed as noticed.**
- Dace never said Reydan's name at the wall in the first draft, though Cael then wrote it at the top of a page. Dace now names him.
- Lira's talking knuckle was the left in ch44 and the right in ch46. It is the left throughout.
- Vell's remark first put Reydan at the carters' inn, which is Brom's lodging. Reydan has a room over a saddler's (ch44), and Vell says so.
- Ansel's Log line said he had spoken Reydan's name at the cookshop; he had not. It now says he still could not say the name, so that the round's naming is the first.
- Dace's offer to let Reydan watch Cael's mornings would have broken his "not a menagerie" rule from ch43. It is now a test Dace sets ("Most men in your place would ask me next where he trains"), which Reydan declines.
- The seven tries after session nine were miscounted in the narration (eight described). The narration now describes seven, matching the Log.
- Brom's "twenty a session" was broken by five extra knocks in ch48's first draft. They are gone, and the tally stays at sixteen in twenty.
- Lira's right-foot lesson was "first morning" in the Log and "second morning" at the table. Both say the second morning.
- The hesitation was written twice in ch45 (before supper and again at night). The night scene now finds it already written.
- Hesk's memory first had him mending a chair in a yard. Book 1 gives him a workshop and a bench of housings, so he is fitting a bearing at his bench.
- "Thirteen nights" since Dace's visit was miscounted on the night before the bout. It now says thirteen days.
- The Brom-Velmere line "I nearly did" implied he had washed out. It now says he came down a hill with a bag himself.

**After all eight existed.**
1. The first complete draft measured about 36,600 words with a sentence mean of 12.66, under the working range. I made a by-hand pass on chapters 44–51:
   - narration that was one thought in clipped clauses was joined into single subordinated sentences, about thirty joins, none in speech, landing beats or protected text;
   - a few Log entries were rewritten in Cael's own semicolon style;
   - about 1,300 words of narration were added where the scenes had room: Cael on filing a man who discards what is seen (ch45); the dock partner on the step and the cookshop (ch46); the bruises as a record (ch47); the falling-back of the defending stage (ch49); the knock-with-leave morning and the narrowing before the thirteenth (ch50); the dusk walk by the ropewalk (ch45).
   Every change was composed by hand and applied as an exact string replacement. No sentence or paragraph was split or joined by a rule.
2. Two scene breaks inside Ansel's round were removed (one continuous action) and one added in ch50 (a night after the dusk hour).
3. `ed.sh overlap book-02-iron-circuit 7`: **0 unprotected, 5 protected**.
4. `ed.sh gates book-02-iron-circuit 7`: reader_standard=0, metadata=0, modern=0 on all eight chapters.
5. `sweep_probe.sh book-02-iron-circuit 7 7`: **1% skeleton, 6% close** for the movement.
6. `formula_metrics.py` on the eight chapters, final: mean 13.19, ≥40-word share 3.5%, 946.7 words per scene. **Disclosure:** besides the per-chapter runs inside my helper, I ran it on the movement five times while revising (12.66 → 12.91 → 12.99 → 13.12 → 13.19).

I wrote only the eight chapter files and these two state files, plus scratchpad notes and helpers outside the repo. I ran no git commands.
