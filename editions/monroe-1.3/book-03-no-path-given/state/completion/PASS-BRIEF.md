# Book 3 — completion pass, same-author texture pass (from the whole-arc read)

**Source.** `whole-arc-read.md` (Fable 5.1, a straight read of ch1–61), §§3, 4 and 9, with the
counts in `whole-arc-notes.md`. The book holds as one arc: the calendar is clean, P1–P20 are exact
and placed, there are no knowledge leaks, and the Reader Standard is met. The coordinator has
already applied the read's 24 line fixes, which also settles its Priority 3 (including the
ledger). Do not redo them.

The pass runs in two lanes. Each edits only its own chapters.

## Both lanes — Priority 1: thin the simile and gesture repertoire (§3, items 1–10)

**Simile caps.**
- Cap the explanatory "the way a X does Y" and "as if" at about two per chapter. The book had 237 of the first.
- Use one depth, as Book 1 did: roughly halve "the way", keep the instrument similes, the similes inside the match and the sittings, and the first instance of each figure.
- Convert to "as …" or "like …" only where the comparison earns its place. Prefer cutting a generic one. Use "just as" where a bare "as" could be heard as "while".

**Filler words.** Cut "for a long time / a moment", "exactly" and "did not look up" wherever the sentence stands without them. Keep any pause that times a real beat.

**Documents.** Let a document be read once, unless the reading is the beat. Keep ch2, ch16, ch36, ch49 and ch61.

**Tags.** Give Oona, Karis and Prynn one gesture-tag each per scene. Rewrite the rest in the character's own register, or cut them.

**Length.** Expect to lose 2,000–3,000 words across the book.

## Lane 1 — chapters 1–31

- Priority 1, as above.
- **Priority 2.**
  - Tighten ch27–31. ch28's reported week of nulls and ch31's twenty-second session overlap with the ledger read-back ch28 already did; lose about 1,000 words between them.
  - Let Cael's "part of me is waiting" surface once more in ch30, so his stakes stay live while Gerda's are paid.
  - Add or remove no scene breaks.

## Lane 2 — chapters 32–61

- Priority 1, as above.
- **Priority 2.**
  - Tighten the Havel coach cutaway (ch47) and the Karis card cutaway (ch50) by a few hundred words each. Keep every beat.
  - The aim: the deposition (ch49) and the find (ch51) are not separated by two still chapters.
  - Add or remove no scene breaks.

## Both lanes

**Method.** By reading, in place, never by script.

**Protect.**
- Every protected line (BOOK_MAP §9, `protected-patterns.txt`).
- The match (ch36) and the two sittings (ch54–59): every exchange and every landing beat.
- Yorlan's formula; the deposition lines; the box-seven count.
- Every fact, count and date, and every line a later chapter or Book 4 quotes.

**Count.** Count each target before and after with grep, within your range.

**After.**
- `ed.sh overlap` stays at 0 unprotected for every movement in range.
- `ed.sh gates` stays at 0.
- `tools/sweep_probe.sh` does not rise.
- Run `formula_metrics.py` on your range.
- Write `LANE-1-REPORT.md` or `LANE-2-REPORT.md`.
- No git commands.
