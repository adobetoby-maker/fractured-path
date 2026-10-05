# AUTHORSHIP — Book 2, Movement 8 "The Bout and the Road" (chapters 52–60)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-02-iron-circuit/state/movement-008/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-02-iron-circuit/packets/MOVEMENT-008.md`, as compiled) |
| Coordinator rulings | Eight binding rulings delivered with the task: the ending state is BOOK_MAP §1, handing off to the closed edition Book 3 ch1; no new names; Compression involuntary, confirmed by the verbatim notice after a Wind-only final bout, session nine untouched; the consent boundary and a three-redirect cap; Lira's two turns and her provisional rating, Brom on standard enrollment; §11 d/e/q (the knockdown, six hundred, Hesk in days); "declaration" for the Arbiter only, "Shattered" plain, protected wording from the map; the Reader Standard |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 2 — Iron Circuit (final movement) |
| Chapters | `editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-52.md` … `chapter-60.md` |
| Date | 2026-10-05 |

**One author, one run.** All nine chapters were written by this model in a single session. No other agent or model touched them, and no subagent was used.

**Reading before drafting.**
- The compiled prompt in full: the profile, formula sections 2–6 and 8–9, the packet, the edition brief, BOOK_MAP §§1–12, STATE_LEDGER through "After Movement 7" with every coordinator ruling, CANON_RULES, and the owner voice.
- The end of Movement 7: ch50 in full; ch51 in full (inside the compiled prompt).
- M7's AUTHORSHIP and AUTHOR-REPORT, for the report structure.
- Source `books/book-02-iron-circuit/chapters/chapter-21.md` to `chapter-24.md`, each read once, in full, and then closed. None was reopened.
- Edition Book 3 `chapter-01.md` in full (the closed Monroe 1.3 text). By grep: edition Book 3 ch2, ch3, ch5 and ch12 for the hand-off facts (Vell's sheaf, the stranger's note in the binder's back pocket, Brom's stamped record, "six hundred", the Reydan joint). The Compression callback: edition B3 ch9 and ch11 do not carry the line; I found it in edition B3 ch35 and in source B3 ch11 ("at very nearly the last moment it could have arrived and still saved him"). Source B4 ch13 for "six hundred people".
- For continuity, by grep and short reads: Vell's call formula and the north/south marks (ch23–25, ch39–40); the redirect drill (ch47); Brom's Velmere story (ch26); Ulric in ch1–2; the scout's visit count (ch40, ch42, ch51); Ansel's cookshop coppers and "buy the next one" (ch46, ch49); the knock's vocabulary (ch46–48).

**Method.**
1. After the single read of each source chapter I wrote a private event list in my own words in the scratchpad outside the repo (`m8-event-list.md`): first the source's bare events, then my own calendar, tallies (knocks 14/12, Wind 6, giving face 3, redirects 3), POV pieces and chapter plan.
2. I drafted forward from that list and the book map, with the sources closed. The entry points and beat order are mine. The movement opens at Dace's door with the count. Lira's cutaway is at the south rope, under the coaching rule. The reads are struck through as a list in Cael's head. Volume is read as a count, through Hesk's mill wheel. The Compression completes on the undrilled right shoulder. Reydan's cutaway falls on the stone, then in his room, then at the market. Quenna's approach is followed by the log, the district walk, and the three-person table at Lira's landing. Brom's question is about the family form. Cael waits to sign until Hesk answers. The final bout is a Wind-only rematch with Ulric, won at the rope. The notice comes at the desk, then the binder, the leavings and the road.
3. Protected wording (BOOK_MAP §1 closing phrase; §8 items 5, 6, 7, 8, 9, 15, 16, 17, 30, 31) was copied from the map only.
4. Quoted packet lines that are not in BOOK_MAP and would have shared eight or more words with the source were re-composed (see AUTHOR-REPORT, Checks).

**Per-chapter probe, as instructed.** After each chapter, before the next, I ran `skeleton_probe.py --source` on it against the four source chapters `probe_sources.py` resolves for this packet (ch21–24). I also ran `source_overlap.py --min 8` and `formula_metrics.py` on the same chapter, through a scratchpad helper (`probe.sh`). A second helper (`close.py`) listed the 0.35–0.50 pairs the probe does not print. Four chapters went over a bar on first draft, and each was rebuilt before the next chapter was begun: ch53 (13% skeleton, 31% close, 17 runs), ch54 (5%/20%, 4 runs), ch55 (18% close) and ch60 (6%/20%, 3 runs). Smaller rebuilds were made in ch52, 56, 57, 58 and 59. The full table is in AUTHOR-REPORT.

**Blocking slips fixed as noticed.**
- The hip-line tally in ch53 first said "three asked bursts" after three exchanges that had used six. It now says six, and three in the third.
- The giving face's hollow was first placed "under the breastbone", where the redirect's cost lives. It is now "under the ribs", as in the M1 entry, in ch52 and ch53.
- The Log's knock breakdown in ch55 did not add up to twelve. It now reads nine on bursts, two on the count and one on a gathering.
- Session nine was "nine days ago" on the bout night; it was four (day 10 to day 14). This is fixed in two places in ch55.
- Reydan's cutaway first gave him a near-loss at the invitational, against M7's canon that the other house withdrew its boy before the final. It now remembers his one real loss in the river halls, and the withdrawn boy is the one who carried a grievance home.
- Ansel's stew first said Cael had paid at the cookshop. M7 has Brom paying, with Ansel leaving two coppers that Brom returned at the arch. Ansel's name line now builds on the ch49 floor, where he first said it.
- Ch59's scenes ran out of order: Vell's evening came before Brom's afternoon, and Brom already held Vell's leaves. The scenes were reordered (Brom's morning rounds, Vell's evening, Ansel's night, the dawn), and Brom's errand to Vell moved to the afternoon.
- "The night the book began" (ch57, ch58) was a meta phrase; it is replaced with plain time. "God knows" in Vell's speech is removed (Reader Standard).
- Two protected lines had picked up a comma from a speech tag ("Like I had enough." and "The problem being me."). Both now stand exactly as in the map.
- "The Tuesday after next" in ch57, said on day 3, is now "the coming Tuesday".

**After all nine existed.**
1. The full movement measured 39,425 words, with a mean of 13.57, ≥40-word share 3.4% and 896 words per scene. I added three short passages of narration by hand: the street talking on the walk home (ch55), Lira's room (ch56) and the inn's front room (ch56). I also name-anchored seven of Cael's realization beats ("Cael found", "Cael understood") for audio clarity. No sentence or paragraph was split or joined by a rule.
2. `ed.sh overlap book-02-iron-circuit 8`: **0 unprotected, 14 protected**.
3. `ed.sh gates book-02-iron-circuit 8`: reader_standard=0, metadata=0, modern=0 on all nine chapters.
4. `sweep_probe.sh book-02-iron-circuit 8 8`: **1% skeleton, 10% close** for the movement.
5. `formula_metrics.py` on the nine chapters, final: 39,845 words, mean 13.65, ≥40-word share 3.4%, 905.6 words per scene. **Disclosure:** besides the per-chapter runs inside my helper, I ran it on the movement three times while revising (13.57 → 13.58 → 13.65).

I wrote only the nine chapter files and these two state files, plus scratchpad notes and helpers outside the repo. I ran no git commands.
