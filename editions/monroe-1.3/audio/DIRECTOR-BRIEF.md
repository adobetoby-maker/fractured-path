# Director brief — Fractured Path (Monroe 1.3 edition) → Breeze direction tracks

You direct the audiobook delivery for chapters of the locked Monroe 1.3 text. You never change a
word. You decide, per segment, who is speaking, how it should be delivered, and how long the pause
after it should be. A single cloned narrator ("Calder", Australian male, Breeze TTS 2) reads
everything. Character voices are register shifts of the same narrator, never impressions.

## The worked example — read it once

The Meridian run directed the same way. Its chapter 1 shows the house style in full:
- `/Users/drive/.local/share/monroe-tts/meridian-run/meridian-ch1/build.py` — the speaker base
  colours (`BASE`), the per-segment overrides (`O`), the pause map (`P`) and the notes;
- `/Users/drive/.local/share/monroe-tts/meridian-run/meridian-ch1/notes.txt` — its shape notes.

Copy the style:
- instructs are short (at most ~25 words after the pace cue);
- concrete on stress ("stress on 'light'", "weight on 'That's mine.'");
- quiet by default;
- interior thought softer;
- scenes close slowly.

## Your inputs, per chapter

- `RUN/<book>-chNN/raw_segs.json` — the segments: id, text, and `brk` (a scene break after this segment).
  RUN is `/Users/drive/.local/share/monroe-tts/fractured-run`.
- `RUN/<book>-chNN/chapter.md` — the chapter as written. Read it in full before directing, as Meridian did.
- `editions/monroe-1.3/audio/book-01-speakers.json` — the book's base colours. Copy them verbatim
  for every speaker you assign. Add a minor speaker in your own spec only, written in the same
  style.
- `editions/monroe-1.3/book-01-the-shattered/state/completion/listening-proof.md`, §2.2, §4 and §5:
  - the pronunciation lexicon;
  - the ear collisions;
  - the POV cutaways;
  - the counts, letters and code blocks.

## Your output, per chapter: `RUN/<book>-chNN/spec.json`

```json
{"summary": "one paragraph: POV(s), the chapter's shape, where it turns, how it ends",
 "speakers": {"Lira": "<verbatim from book-01-speakers.json>", "...": "..."},
 "assign": {"s012": "Lira", "s015": "Cael"},
 "over":   {"s001": ["SLOW", "base narrator, quiet and deliberate; let the opening line sit."],
            "s040": ["BASE", "same narrator, Lira; dry, a small told-you-so; stress on 'post'."]},
 "pause":  {"s014": 850, "s060": 1200},
 "cut":    ["s051"],
 "note":   {"s003": "Inward count; one number per segment."}}
```

**`assign`** — every segment whose text is mainly one character's speech. Leave mixed narration
with a short quote as the narrator, and describe the quote in an `over` colour, e.g. "base
narrator; then Vell, low and spare, on the quoted line". Unlisted segments are the narrator.

**`over`** — use it where the default speaker colour is not enough:
- emotional turns;
- stress words;
- interior thought;
- letters;
- the Log;
- system notices;
- the openings and closings of scenes.

The tiers are `SLOW` (~120 wpm), `BASE` (~130) and `EASY` (~140, light quick speakers only).
- Every colour starts "base narrator…" or "same narrator, <who>…".
- No impressions, no accents, no shouting: "loud" is "firm, not shouted".

**`pause`** — the hierarchy is 330 light, 450 breath, 600 thought (the default), 850 reset, and
1200 landing. Scene breaks (1500) and the chapter end (1200) are automatic. Use 850 for real resets
and 1200 sparingly, for landings.

**`cut`** — an interrupted line whose next speaker cuts in. It gets a 330 ms gap.

## Fractured Path specifics

- **Cael's Power Log and the system notices.** The italic Log lines, and the code-block notices
  (FRAGMENT ACQUIRED and the rest), are flat, even and recited. Use SLOW and a document register:
  "base narrator, flat and even, reading a notice; each field a separate plain statement".
  `[SHATTERED]` is read as the plain word. Brackets are never voiced.
- **Letters.**
  - The salutation ("Cael," / "Hesk,") is quiet.
  - The sign-off "— H." / "— Cael" is a pause, then the initial or name, never "dash".
  - Hesk's letters are in Hesk's colour, read as written words.
- **Counts said inward** (ch3 the circle, ch19 the yard): SLOW, quiet, one number per beat.
  Vell's count in ch58 is aloud, level.
- **Bouts.** The exchanges quicken in BASE. Landing beats ("Darrow knelt.") are SLOW, with an 850
  or 1200 pause after.
- **POV cutaways** (Hesk, Vell, Lira, Coss). At the first segment after the `---`, give a colour
  that signals the new mind, e.g. "base narrator, a shade older and drier, Hesk's own thoughts".
- **Collisions.** Keep Coss (clipped, formal) and Doss (slow, gravelly) apart by register, and the
  same for Darrow (low, heavy) and Marrow (quick, genial). They share scenes in ch30, ch54 and
  ch57–58.

## Then

For each chapter, run:

```
python3 editions/monroe-1.3/audio/fpaudio.py build  <book> <N>
python3 editions/monroe-1.3/audio/fpaudio.py verify <book> <N>
```

`verify` must PASS. It checks the word-lock against the manuscript, segment length, pace cues and
scene breaks, and on a pass it writes `direction.ready`. If it fails on a spec problem, fix the
spec. Never edit `raw_segs.json` or the manuscript.

Write nothing else. Run no git commands.
