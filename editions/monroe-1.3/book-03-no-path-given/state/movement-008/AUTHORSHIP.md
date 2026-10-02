# AUTHORSHIP — Book 3, Movement 008

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | oconnor 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | claude-opus-5-5 (self-reported by the running model) |
| Edition | monroe-1.3 |
| Book | the-fractured-path / book-03-no-path-given |
| Movement packet | editions/monroe-1.3/book-03-no-path-given/packets/MOVEMENT-008.md |
| Compiled prompt | editions/monroe-1.3/book-03-no-path-given/state/movement-008/compiled-prompt.md |
| Date | 2026-10-02 |

## Run

One uninterrupted run, no restart. One coordinator message arrived mid-run (see below).

**Read before drafting.**
- The compiled prompt, in full (2,371 lines, read in four pages).
- Source chapters 21, 22, 23 and 24, and Book 4 ch1, once each, in full, for events.
- This edition's chapters 40–53 in full, myself (no helper digest). Ch53 was also read inside the compiled prompt.
- STATE_LEDGER through "After Movement 7", including the coordinator rulings at its head, inside the compiled prompt.
- The coordinator notes at the end of the M8 packet, inside the compiled prompt.
- Movement 7's AUTHORSHIP.md and AUTHOR-REPORT.md, for shape and for the r1 hand-off.

**Chapters 1–39.** No helper digest was used. I worked from the ledger's movement sections and checked specific facts by grep and short reads:
- ch8 (the week-two inventory's format), ch12 (the four fragment headings), ch15 (Cael's first thanks to Hobb, lines 105–127), ch36 (the Ember notice block), ch1–3 (Vell's ledger rating; "priced"; Quenna's bet).
- Edition Book 1 manuscript: Hesk is Cael's grandfather (ch5, ch14). `universe/STATE_LEDGER.md` row for Hesk.
- Book 4 ch2 line 233 (Naveth's composure "in front of two hundred people").

## Method: drafted from my own event list — with a deviation, reported

I read the five source chapters once, closed them, and wrote a private event list in my own words, scene by scene, in my scratchpad (not in the repository). I did not reopen the source chapter files at any point afterward.

**Deviation.** The first forward draft of the hearing scenes and of week 24 tracked the source closely from memory, even with the files closed. I had read them only a couple of hours before. The first full check showed:
- `ed.sh overlap`: 110 unprotected 8-word runs;
- `skeleton_probe.py`: 13% skeleton overall, with scenes up to 56% (ch61 at 26%).

So I rebuilt the tracked scenes from the event list, with new entry points and new beat orders, rather than patching them:
- ch55, the midday recess (now entered through Brom; Karis, then Brom, then Lira's private question);
- ch57, Yorlan's admission, the concession and the definitions clause (the argument now opens on "The Warden is right.");
- ch58, the whole chapter (the four files now come before the narrowing; the challenge's own phrase is introduced as "the Warden's" line);
- ch59, the ruling's aftermath, Coss's five minutes (now entered at Prynn's books) and the faceless coda;
- ch61, the whole chapter.

After the rebuild I recomposed the remaining listed sentences one at a time, by reading. **Note for the coordinator:** the probe's `--show` output prints the matched source sentence beside each manuscript sentence. I saw those source lines while recomposing. I used them only to move away from them, but it means the source text was in front of me again, a line at a time, in that pass.

## Coordinator message (mid-run)

The coordinator corrected the packet: the custom objection is answered with "It amends." / forty-one / "Custom is not code"; "Somebody writes the law. Nobody ever mended a hole by pretending to stand on it." answers Brom's hole question. Both are used that way round at the hearing:
- ch58: the third assessor asks about "the Warden's gap", and the hole line answers it;
- ch58: Ilsev's custom question is answered with forty-one and P13.

I re-checked ch53's return scene (two armfuls, the card inside the index's cover, the fourteen hearings). Nothing in M8 refers to it.

## Overlap, probe, gates and metrics

`ed.sh overlap book-03-no-path-given 8` was run six times: 110 → 37 → 1 → 0 → 0 → 0. Every listed run was recomposed in context, not synonym-swapped. Some packet-quoted lines with an 8-word source run that BOOK_MAP does not protect were kept in their words but broken by a speech tag or narration. A few were minimally altered. All are listed in AUTHOR-REPORT §4.

`skeleton_probe.py` (source ch21–24 against ch54–61) was run after each pass: 13% → 6% → 2% overall. Final per chapter: 0, 1, 1, 3, 1, 4, 1, 3%.

`ed.sh gates`: reader_standard=0, metadata=0, modern=0 on all eight files.

`formula_metrics.py` was run **once**, after the overlap and probe passes and the scene-break merges. Three small factual corrections were made after that run (AUTHOR-REPORT §5, item 12). They change a few words and no sentence boundaries. I did not re-run the metrics.

One git command was run by mistake: a read-only `git status --short`, chained into the final verification line. Its output was discarded unread, and it changed nothing. No other git commands were run. No files were edited outside the eight chapter files and these two state files. The scratchpad event list is outside the repository.

## Chapter files

- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-54.md
- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-55.md
- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-56.md
- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-57.md
- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-58.md
- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-59.md
- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-60.md
- editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-61.md

## Names

In use, as instructed: Hobb, Oona, Gerda (pending names). Canon names: Yorlan, Ilsev, Havel, Coss, Prynn, Naveth, Quenna, Wray, Edran, Vell, Hesk, Reydan, Feryn. Place names Sarnholt and Wexley are the packet's.

No other names were invented. Every new or recurring acting role is unnamed:
- the academy's counsel;
- the grey-bearded third assessor;
- the observers (two grey registry coats, a woman in dark blue with an academy badge, a guild legal officer, a man with the look of a provost, an old woman in black with a cushion);
- the four watchers (the bench man, the street walker in brown, the coordinator at the well, "the early one");
- the station clerk, the draper, the carrier, the aide;
- the faceless office.

Karis's watcher epithet "the early one" is an epithet, like the clerks' in M7.
