# AUTHORSHIP — Book 4, Movement 5 "What Seln Keeps" (chapters 30–37)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment |
| Packet | `editions/monroe-1.3/book-04-copper-crown/state/movement-005/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-04-copper-crown/packets/MOVEMENT-005.md`) |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 4 — Copper Crown |
| Chapters | `editions/monroe-1.3/book-04-copper-crown/manuscript/chapter-30.md` … `chapter-37.md` |
| Date | 2026-10-05 |

One session. No other author drafted any chapter. The coordinator's seven rulings in the task message governed where they differed from the packet.

**Reading before drafting.**
- The compiled prompt in full (1,695 lines, read in pages). It covers the profile, the formula §§2–6 and 8–9, the movement brief, the preceding chapter, the edition brief, BOOK_MAP §§1–14, STATE_LEDGER through "After Movement 4" with its coordinator rulings, CANON_RULES and the owner voice.
- Movement 4's last two chapters in full (`chapter-28.md`, `chapter-29.md`), plus `state/movement-004/AUTHORSHIP.md` and `AUTHOR-REPORT.md` for the shape of these files.
- `editions/monroe-1.3/OWNER-DECISIONS.md`: #9 and #18 (since his Kindling, no number); #10; #11 (Gwen is a placeholder).
- Source `books/book-04-copper-crown/chapters/chapter-12.md`, `chapter-13.md` and `chapter-14.md`, each read once in full and then closed. For the Ember numbers, B3 was checked through the edition's own text (B3 ch37–39: about eighteen hours, two Wind misfires, Lira's three-clean-days rule) rather than the source B3 chapter, because the edition re-staged that acquisition.
- Targeted greps of the edition for continuity: Seln's last spoken words to Cael (ch14, d51); the small case (ch14); Brom's exercise sheet (ch26); Brom's sister, grandmother and the pear fork (B2 ch16, ch26, ch32); Hesk (B1 ch3–5; B3 ch61's letter); "the quiet" and the Iron read settling "outward" (B2 ch28); the desk clerk; counsel's gender; the bells.

**Method.** After the single source read, I wrote a private event list in my own words (session scratchpad, outside the repo: `m5b4/events.md`). It set out a calendar, each chapter's scenes and entry points, and my own inventions. Drafting worked from that list, BOOK_MAP and Movement 4. Protected wording was copied from BOOK_MAP only. The source chapters were not reopened while drafting or rebuilding. Afterward only the probe's matched-pair output and my close-band lister were read (the lister applies the probe's own method in the 0.35–0.50 band).

**Honest note on source distance.** As the coordinator warned, first drafts tracked the source from memory, worst in the Seln window, the counter, the climax, the misfire and chart scenes, and the birthday. I probed every chapter right after drafting it and before starting the next. Every flagged passage was rebuilt by hand from the event list with new staging, not word swaps. Skeleton / close by stage:

| Chapter | First draft | Rebuild(s) | Final | What changed |
|---|---|---|---|---|
| 30 | 23% / 48% | 6 / 28 → 4 / 16 | 3% / 13% | Seln's entry recast as a measured table (*Range / Interval / Heading*), the landlady who took the cipher for a diary, the carbons laid out like patience; the counter's three layers as a carbon set; scenes merged; hall-three scene added |
| 31 | 11% / 31% | 1 / 23 → 1 / 16 | 1% / 12% | The rotations argument re-voiced ("It answers paper with people"); Karis's fourth road; the plan written by four people; Brom's pie for the man with the knee; long sentences joined by reading |
| 32 | 13% / 30% | 4 / 16 | 0% / 10% | The slate re-entered through the boy's flat-footed four and Cael's own lit-buildings chart; Karis meets him on the walk and tells it drawers-first; door geometry made consistent |
| 33 | 9% / 30% | 0 / 20 | 0% / 11% | The night-two write-up rebuilt as "what I did not hear / what I did hear"; Brom's grandmother and the cough at the door |
| 34 | 27% / 54% | 4 / 30 → 4 / 20 → 1 / 13 | 1% / 12% | Rule counted on five fingers; the basin of dark water; the failure scene opens on the fire-watch's question; Seln's lines recomposed except the packet's "Sit down on the step…" |
| 35 | 28% / 51% | whole chapter rewritten → 8 / 24 → 3 / 15 | 2% / 13% | Lira and Brom told within the hour; the misfire re-staged ("Is that one?", "Tell me what it was like"); new unit session; the chart scene made Socratic ("Now what do you conclude?" / "No.") |
| 36 | 28% / 50% | 9 / 25 → 1 / 17 | 1% / 14% | The idle-state reasoning moved into a conversation with Lira ("rent"); chalk columns on the wash-house wall; Brom blindfolded with Rooke's wrap; the ladder exercise added; the debt worked as two columns |
| 37 | 20% / 35% | whole chapter rewritten → 4 / 22 → 2 / 18 | 2% / 14% | Fiske at the board at dawn; Lira's how (Karis's column at Greyvane); new food and the pear story; Karis's own legend headings; the grandmother line; the letter to Hesk |

Scripts were used only to list flagged sentences and to apply exact before→after strings written by hand; they failed on any miss. Rhythm joins, about 45 in ch31 and ch35, were each chosen by reading, in narration only, at points where one thought had been clipped. Speech was left as spoken.

**Scratchpad note.** Helpers live under a unique folder (`m5b4/`) in the session scratchpad: the event list, the close-band lister, and scene staging files. Nothing from them was written into the repo.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-04-copper-crown 5`: 0 unprotected, 18 protected.
- `ed.sh gates book-04-copper-crown 5`: reader_standard=0, metadata=0, modern=0 on all eight chapters.
- `sweep_probe.sh book-04-copper-crown 5 5`: skeleton 1%, close 12%, on 1,626 sentences (exact: 1.3% / 12.6%).
- `formula_metrics.py` on ch30–37: see AUTHOR-REPORT.md.

Only the eight chapter files and these two state files were written in the repo. No git commands were run. STATE_LEDGER was not edited; its end-state is in AUTHOR-REPORT.md.
