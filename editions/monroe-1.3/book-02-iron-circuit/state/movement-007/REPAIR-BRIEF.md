# Repair brief — Book 2, Movement 7 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Sol (review seat). The cold read saw the
manuscript only.

**Verdict.** Both reviewers would continue immediately. They name these strengths:
- Reydan reads the Ironyard by its feet and its silences: dangerous without cruelty, and an unusually clean
  antagonist hook.
- Ansel's account becomes his voluntary round, and "declining to be interesting" becomes a usable tactic. He
  gains the most in the least space.
- Session nine changes the pressure without solving anything.
- Cael's growth is ethical as well as tactical. He asks leave every time, and he ends intending to win.

The editorial confirms the following:
- every protected line is exact;
- Reydan is 22, Iron R8, burst-compression Pressure;
- the scout is unnamed and does not approach;
- the count is three fragments plus one anomaly;
- Lira is provisional;
- session nine happens once, with "description, not diagnosis", no still place and no taking theory;
- the Reader Standard passes;
- overlap is 0 unprotected.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags (all ACCEPTED)
1. **The courier link: ACCEPTED.** The up-river keeper asked for Cael's line at Reydan's request, and lends Dace
   the old written report, which must go back. Keep the packet's beat that a growing version of the story reached
   Reydan (a Bronze R1 beaten by a boy with no Path). The keeper's request comes after that and does not replace it.
2. **Reydan in his father's paid yard from ten (twelve years at twenty-two): ACCEPTED.**
3. **Ansel, about 27, a former Bronze from a coast house, Path unstated: ACCEPTED.** The dock partner being in the
   hall is also accepted.
4. **Brom at eleven questioning the man his uncle beat: ACCEPTED.** It is consistent with "trained his body from
   twelve" (decision #4), because questioning is not training.
5. **The Hesk workshop memory at nine: ACCEPTED.**
6. **Crowd kept soft (room for four hundred, plus the street): ACCEPTED.** Movement 8 reaches about six hundred.
7. **Bede and Maud: placeholder policy, as before.**

## Priority 1 — The countdown and two line defects
1. **Countdown (editorial; the cold read disagrees, so verify by your own day table).** Ch45 fixes the bout
   "two weeks from yesterday. Tuesday fortnight." The plan is Wednesday evening, so ch46 is Thursday, the first
   morning.
   - The editorial counts ch51's "eleventh / twelfth / thirteenth day" as Sunday / Monday / Tuesday. That would
     put the night before on the bout day.
   - The cold read counts it as a clean run from Wednesday to Monday night.
   - Write out the thirteen days, weekday by weekday, and check every ordinal ("the second morning", "the sixth
     evening", the session numbers, rest days, the eleventh to thirteenth days) and every "tomorrow".
   - If the editorial is right, fix the smallest set of ordinals or the one schedule reference. Do not move or
     recast scenes, and keep the shoulder-rest arithmetic intact.
   - Record the table in your report either way.
2. **ch51, two line fixes.**
   - Close the quotation mark on Dace's paragraph ending "Go away. You're one more body, and I'm counting you."
   - Repair the emphasis in the Wind inventory, "two* ands*", so it reads "two *ands*".
   - Also scan all eight chapters for any other unclosed quote or malformed italics.

## Priority 2 — Say it once (both reviewers)
- **ch45–48.** Reydan's academy polish, his refusal to repeat himself, and his advantage over Cael's bench-built
  method are each explained in full by several people: Cael's notebook after Dace's challenge, Brom's supper
  explanation, Ansel's cookshop account, and the clerk's nine-page report.
  - Let each source add only what is new to it. Ansel brings memory and cost; the report brings "declined to be
    interesting".
  - Compress repeated interpretation only. Keep every scene, every developed drill, Ansel's account and round,
    and the report's crucial evidence.
- **ch47–48.** After each tally, cut interpretive sentences that restate what the drill has just shown. Keep every
  tally that establishes progression.
- **ch44–46, orientation (cold).** At the first necessary recurrence of an earlier name or label (most
  concentrated in ch45's list from Feryn through Talis), either add a brief appositive or drop a name that isn't
  needed where its tier or function alone carries the point. Do not add a glossary paragraph.
- **ch51, the inventory.** Keep the body-state audit, the exact remaining costs, the anomaly exclusion, the
  three-read plan, the plan line (exact), and the final quiet with fear. Compress clauses that repeat limits
  established in ch47–50, so the turn to intending to win lands cleanly.

## Priority 3 — Sentence weight, by hand, where you are already working
The sentence mean of 13.19 sits just inside the range, and ch46, ch47 and ch50 are each under 13 on their own.
The ≥40-word share is 3.5%; words per scene are 947; the paragraph median is 29 and the paragraph mean is 45.
- In the explanatory narration of ch46, ch47, ch48 and ch50, join adjacent statements that are one thought.
- Split only the longest paragraphs, and only where the thought turns.
- Never touch dialogue, landing beats or protected wording.
- Bring the movement mean comfortably inside the range (about 13.5 or higher) without raising the ≥40-word
  share above 4.5%. Do not raise the paragraph median.

**Length.** Finish within 36,500–38,500 words. Trimming in P2 is expected.

## After the repair
Run:
- `ed.sh overlap book-02-iron-circuit 7` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-02-iron-circuit 7 7` (stay ≤ 5% skeleton);
- `formula_metrics.py` on the eight chapters.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the weekday-by-weekday table;
- before/after metrics;
- the changelist, by chapter.

Edit only ch44–51 and AUTHOR-REPORT.md. Run no git commands.
