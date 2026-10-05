# Repair brief — Book 4, Movement 6 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Sol (review seat). The cold read saw the
manuscript only.

**Verdict.** Both reviewers would continue. What they singled out:
- **The opening.** The road-grey / registry-grey reveal and the isolated "Archmarshal Vastin" catch at once.
- **The best surprise.** Paperwork becomes credible combat: Bracken's defense has tactics, an opponent, failure
  conditions and an emotional payoff for Karis.
- **Rooke.** "Right about the wrong half" is a difficult adult choosing accountability.
- **Lira.** She is near-coequal, with independent agency: she refuses Cael's pages, the tallow slide is hers, and
  she climbs the tier only to watch him.

The editorial confirms:
- the calendar holds: the 9th, the 10th and the 12th, with the final on the 19th and the evaluation on the 20th;
- the tournament rules hold, and Fiske keeps the crown;
- every protected line is exact;
- the Reader Standard passes;
- overlap is 0 unprotected.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags (all ACCEPTED)
1. **Semifinals on the ninth (Lira–Fiske) and the tenth (Brom–Merrick).** This follows M4's canon that the top
   line fights earlier and gets a day's more rest. Note that the hip will be ten days old at the final, not nine.
   The M8 packet will be corrected.
2. **Lira's hip and the tallow skill.** Lira's deep hip strain on Fiske's slick and the foundry tallow-floor
   skill are accepted, along with four days off the hip.
3. **Vastin named at the reading,** with no age.
4. **The inspection schedule on the page:** records 12th–15th, facility 14th, observation 20th. M7 will match it.
5. **Karis's slate draws the three columns.** The insight and the Log stay Cael's.
6. **Progression vocabulary.** Report both counts, as you did.
7. **Gwen's aunt's story.** Gwen remains a placeholder under decision #11.
8. **The hall-three slip** is known only to Brom and Cael on the page. The wing observer at the rail did not read
   it as anything.
9. **Withrow's grain-store story.**
10. **The documentary defense is done in the days available** (d169–173). "Eleven days" is not binding.

## Priority 1 — The record of five (editorial; verified continuity finding)
In ch43 ("And what does the record let you show?"), Cael says the five are "all on paper somewhere already. Vell
has them in her ledger. Greyvane's panel noted them. The transcript has them." The narration then repeats "five
things that were already on paper".

Edition canon says otherwise:
- ch12 and the M2 ledger: "Two capabilities are on the public record". The hearing transcript carries the Wind
  framework and the Iron read, plus Ember in one late, thin exhibit.
- The academy's filed baseline (M2, day 48) took Wind, the Iron read and the plate (Pressure withheld at the
  plate). Compression is ringed as untested on a floor that answers. Ember stays off the floor by agreement with
  Karis.

**Ruling.** Keep the movement's turn: hiding and honesty become the same operation, because the evaluation can
honestly show growth in five things that already exist on some paper, while only the sixth is new to every
record. Make the inventory TRUE paper by paper:
- **The public transcript:** Wind and the Iron read, and a thin Ember exhibit.
- **Greyvane's filed baseline:** the Wind numbers, the Iron read, the plate (withheld, so flat), and Compression
  as a ringed, untested line.
- **The circuit record Vell copied** (Book 2): his bouts, including the public Pressure-adjacent delivery and the
  Compression that finished the Reydan bout. Cael may know the record exists without quoting it.

Two capabilities are public. All five have a paper trail. None of the five would be new to the evaluation; the
sixth would be new to everything.

Rewrite only the ch43 lines and the narration that carry this, plus any ch42–44 echo, so the conclusion rests on
what is true. M8's evaluation follows the plan:
- growth measured in five against the baseline file;
- the plate flat;
- Ember the early surprise, read above what the Greyvane exhibit supports.

Nothing in this movement should contradict that.

## Priority 2 — Clarity and say-it-once (both reviewers)
- **ch38 anchors (cold).** Add at most two short sentences:
  - one early, tying "going thin" to what is observable (people's attention sliding off him, the exposure that
    follows);
  - one clean reminder of what an adverse provision evaluation would change (the enrollment rests on it).

  No recap, and no glossary paragraph.
- **"Hold ordinary," said once per voice (cold).** Gault's "changes nothing", Rooke's "keep doing it", Bracken's
  "dull month", Withrow's address and the three signs of the bluff's temperature all restate the instruction.
  Trim or sharpen the one or two confirmatory paragraphs where a beat adds no new relationship, risk or tactic.
  Keep both semifinals, Bracken's file logic, Rooke's confession, Withrow's public ownership and all protected
  lines.
- **ch39, the file (both).** Certified copies, the sealed verification, the independent negative search, the
  directive and the index arrive as variations on one proof principle. Give each step one plain sentence of
  purpose: what it protects against. Let Karis's satisfaction and "same weapon, held the other way round" carry the
  meaning. Trim the third explanation of the principle.
- **ch44, the countdown (cold).** From "On the morning after the file was closed" to "They come tomorrow", the
  "three days" summary sits awkwardly against the ninth-day close and the twelfth-day arrival. Make the transition
  exact, with one explicit date or the right span. Do not expand the scene.

## Priority 3 — Cadence, by hand, where you are already working (editorial)
The sentence mean of 13.23 is at the floor, and the ≥40-word share of 4.4% is at the ceiling.
- Do NOT lengthen the long tail. Join related short narration into clear medium-length sentences of 18–30 words.
- Split any 45-plus-word narration sentence that carries two thoughts.
- Never touch dialogue or landing beats.
- Aim for a mean of about 13.6 and a ≥40-word share of 4.0% or less, with words per scene still 850–1,050.

**Length.** Finish within 30,500–33,000 words.

## After the repair
Run:
- `ed.sh overlap book-04-copper-crown 6` (0 unprotected; this will also regenerate `source-overlap.tsv`, which the
  editorial found empty);
- `ed.sh gates`;
- `sweep_probe.sh book-04-copper-crown 6 6` (≤ 5% skeleton, ≤ 13% close);
- `formula_metrics.py` on the seven chapters.

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the paper-by-paper record of five, as now written;
- before/after metrics;
- the changelist, by chapter.

Edit only ch38–44 and AUTHOR-REPORT.md. Run no git commands.
