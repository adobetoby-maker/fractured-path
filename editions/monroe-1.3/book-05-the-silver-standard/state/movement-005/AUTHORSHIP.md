# AUTHORSHIP — Book 5, Movement 5 "The Concourse" (chapters 27–32)

| Field | Value |
|---|---|
| Public byline | Monroe Jackson |
| Seat | `oconnor` 1.3.0 |
| Foundation | Monroe Jackson 1.3.0 |
| Requested author | Opus (Claude Opus 5.5) |
| Actual runtime model | `claude-opus-5-5` (Claude Opus 5.5), as stated in this session's environment. Run as a delegated agent session launched by the coordinator. |
| Packet | `editions/monroe-1.3/book-05-the-silver-standard/state/movement-005/compiled-prompt.md` (movement brief: `editions/monroe-1.3/book-05-the-silver-standard/packets/MOVEMENT-005.md`, with the coordinator's #39 note at its head) |
| Coordinator rulings | Six rulings sent with the task: the continental format (#39) stated once, no third-place bouts (#40), the Copper bracket finishing before the rest day (C14); ratings #38 and the public-capability count (#40); world rules (no season names, "A note for after Norhold.", feet and yards, no incremented year counts, house weekdays); the withheld material (Daeva at distance, Umber, Vastin, Havel, Karis's door, the initials); no new names; protected wording. Applied wherever they differ from the packet. |
| Edition | `monroe-1.3` |
| Book | The Fractured Path, Book 5 — The Silver Standard (fifth movement; middle third) |
| Chapters | `editions/monroe-1.3/book-05-the-silver-standard/manuscript/chapter-27.md` … `chapter-32.md` |
| Date | 2026-10-05 |

**One session.** One author drafted all six chapters in one session and one context. No other model drafted any part of them, and no subagents were used.

**Reading before drafting.**
- The compiled prompt, read in full in pages. That covered the profile and formula §§2–6 and 8–9, the movement brief, the preceding chapter (ch26), the edition brief, BOOK_MAP §§1–14 with every `[B4-reconciled]` mark, and STATE_LEDGER ENTRY and AFTER MOVEMENTS 1–4 with their coordinator rulings. It also covered CANON_RULES and the owner voice.
- `manuscript/chapter-25.md` in full; ch26 was read in full inside the compiled prompt.
- `OWNER-DECISIONS.md` #35–#40, and Movement 4's `AUTHORSHIP.md` and `AUTHOR-REPORT.md` for the shape of these files.
- Targeted greps of this edition. In Book 5 I checked the banner-holder ruling (M3 review: Auremont is not the holder; the banner stays unassigned) and Umber's one earlier mention (ch5). I also checked Vastin's files order (ch24) and Havel's notebook and hand (ch25). In Book 4's ledger I checked Havel's four entries and the three-line rule break, and Ilsev and Havel at the Halcenvane inspection. In Book 3's map I checked Karis at Ternhall, including the rule that she never says her training partner's name. I checked the Ash, Rune and Stone Path usages across the edition.
- Source `books/book-05-the-silver-standard/chapters/chapter-08.md` and `chapter-09.md`, read once in full for events and people. Then they were closed. `CHAPTER_ARCHITECTURE.md` was grepped once for the Daeva first-read reference (see owner flag 1).

**Method.**
- After the single source read I wrote a private event list and a day calendar in my own words. They are in the session scratchpad, outside the repo (`b5m5/events.md`).
- I drafted from that list and BOOK_MAP, and did not reopen the source chapters. My only later exposure to source sentences was through the probe's `--show` output and a small helper (`b5m5/close.py`) that lists the pairs at 0.35 and above so that close passages could be found and rebuilt.
- Protected wording was copied from BOOK_MAP §10. Packet-quoted lines were copied from the packet and the coordinator's rulings.
- Each chapter was probed as soon as its first draft existed, and flagged passages were rebuilt before the next chapter was begun (table below).

**Per-chapter probe (skeleton / close), first draft → final.**

| Chapter | First draft | Rebuilt | Final |
|---|---|---|---|
| 27 | 0% / 6% | Not rebuilt for reuse. It was redrafted for rhythm: sentence mean 11.5 → 13.2, and "said" tags halved. | 0% / 4% |
| 28 | 4% / 14% | Rebuilt: Withrow's lines around her sentence, the Norhold-arrival opening, Lira's two Fenmark lines, the banner Log (rewritten whole), the privacy Log, and Karis's "walls" line. | 2% / 4% |
| 29 | 4% / 11% (Auremont scene 18% / 21%) | The Auremont arrival was redrafted whole from a new entry point: Cael turns his back and reads the crowd. Also rebuilt: the woodcutter and Seln lines, Ephram's tag line, the barrow price, and the Log. | 0% / 3% |
| 30 | 9% / 15% | Rebuilt: Rooke on Umber; the ring visit's opening and the steward (the bricked-door plant kept as an image, re-composed); the draw's Lira, Brom and Karis beats; the demonstration frame; the Log. | 1% / 4% |
| 31 | 6% / 16% (procession scenes 15–21% / 31–36%) | The procession, the first read and the locking were redrafted whole. The new structure has the tunnel and the marshals' list, the read's four questions, and Umber arriving "carrying a box". Also rebuilt: Lira's opening and interval lines and the margin note. | 0% / 4% |
| 32 | 17% / 29% (the filings to the Compact row) | The whole second half was redrafted from beats. Karis's economics is now a bank image, the council runs Rhagen-first with the showman's timing, and the trial rules are met at the board at first light. The city walk now opens on "the wall", and the Compact row on a steward clearing the chair. Havel's cutaway was moved ahead of Cael's row scene. | 1% / 8% |

Every remaining skeleton hit is a protected line or a packet line. They are the attestation, *Squads shall be drawn…*, Withrow's sentence, "This city is the system with the roof off.", "Somebody in the seeding office reads past the paper", "Twice is starting to look like a door somebody built on purpose.", "And when the theater and the mechanism are the same thing?", and "Blank pages are the ones that get written last."

**How scripts were used.**
- Exact before→after strings that I wrote by hand, applied by a script that failed on any miss.
- Whole new passages written by hand and spliced in.
- Listing long paragraphs, long sentences, close pairs and tic counts for me to read.
- Every paragraph break was chosen by reading. I named the line and the sentence at which each paragraph turned, and a helper (`b5m5/brk.py`) applied only that break. It asserts that the text is unchanged apart from whitespace and italics markers.
- One batch of hand-chosen breaks in ch30 fell inside speeches. A quote-and-italics checker caught it, and those eight breaks were rejoined.
- No rule split or joined text automatically. Speech, Log lines and protected text were left whole.

**Final checks** (all run after the last edit):
- `ed.sh overlap book-05-the-silver-standard 5`: **5 unprotected**, 5 protected. All five unprotected runs are packet-quoted lines kept whole, as ruling 6 directs. They are listed with proposed patterns in AUTHOR-REPORT.md. Every other shared run was rebuilt.
- `ed.sh gates book-05-the-silver-standard 5`: reader_standard=0, metadata=0, modern=0 on all six chapters.
- `sweep_probe.sh book-05-the-silver-standard 5 5`: **skeleton 1%, close 5%**, on 1,430 sentences.
- `formula_metrics.py` was run on ch27–32 and on ch1–32. The results are in AUTHOR-REPORT.md.

**Files written.** Only the six chapter files and these two state files were written in the repo. STATE_LEDGER, BOOK_MAP, the packets and `protected-patterns.txt` were not touched. Scratch files are in the session scratchpad only. **No git commands of any kind were run.**
