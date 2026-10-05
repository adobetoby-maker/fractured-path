# Repair brief — Book 2, Movement 3 (one consolidated same-author repair)

**Sources.** This brief consolidates `review-editorial.md` and `review-cold.md`. Both are by Sol, the edition's review seat; the cold read saw the manuscript only.

**Verdict.** Both reviewers would continue; the editorial reviewer said "without hesitation". The movement earns that through character and method, not by withholding the fight:
- Lira's win over Wendel.
- Vell's written correction ("The fault is the keeper's").
- "Something I've never seen before".
- Lira's correction on the step.

Source distance is clean: 0% skeleton, 9% close, overlap 0. Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your flags

Accepted:
- **Coss's grey slip.** It is gone from the file; he believes its code now sits as the unsigned second line, but cannot be sure because he never wrote it down; a second empty log page; no upward note; no contact with Cael. This ties Book 1's slip to Book 2 M2's unsigned middle line, and the recheck verifies it against the edition's Book 1 ch60.
- **The reworded packet quotes.**
- **Brom's limited-range read.** It is consistent with the later Iron-adjacent notice.
- **No running Copper-formal count.**
- **The invented texture:** Brom's copper a round, Wendel's guild pin, Corrin's "like a gatepost", Hesk's mill-wheel "slack", Lira lending her dock partner.
- **The Coss cutaway at about 2,000 words.** Do not pad it.
- **The cutaway share** (19% this movement, about 12% for the book): accepted. The tightening below lowers it.

## Priority 1 — Make the mechanic exact (cold read)

In ch18, ch20 and ch22 — from "A newcomer's fist landed" and the pre-impact breath observation, through the reset/account theory, to the four-strike plan — Brom's hardening has three distinct intervals:
1. activation before contact;
2. latency after contact;
3. recovery before the next hardening.

The text does not keep them apart, yet the decisive tactic depends on exactly one of them.

Fix this on the page:
- Define each interval once, at the moment Cael observes it, with one concrete tell each.
- Make the four-strike plan name which interval the low fourth strike exploits, and why: reaction time, depleted capacity, or physical reset.
- Keep it a hypothesis Cael is not sure of. Do not resolve how the bout goes.

## Priority 2 — Say it once (both reviews)

- **The plan** ("Pressure locked", "Wind as insurance", the widening gap, the low fourth strike) is fully explained in the ch19 opening inventory, the ch21 bench and plan discussion, the main-floor walk, and the ch22 written plan.
  - Keep the ch19 discovery and the ch21 interpersonal planning scene.
  - Cut the ch22 written plan to what is genuinely new: the commitment, the failure conditions, and the trust in Brom.
  - Elsewhere, let later passages complicate the plan rather than summarise it.
- **The ch17 Coss cutaway** (from "The return came up to Coss" to the daughter's map, including the long-room file inspection and the second empty log page):
  - Compress the repeated uncertainty and silence paragraphs.
  - Give the cold reader one concrete point of contact with the present early in the cutaway, without disclosing anything reserved.
  - Keep both scenes and every knowledge boundary.

## Priority 3 — Rhythm in the training chapters (editorial)

From ch18's first failed gaze session through ch20's coverage/reset work, the explanatory runs are flat: median 9, Reading Ease 91.8. Where a sequence of equally weighted declaratives forms one causal thought, join it into a hierarchical sentence. Keep the mechanics clear. Do not touch speech or bout beats.

**Length.** Finish within 34,500–37,000 words.

## After the repair

Run:
- `ed.sh overlap book-02-iron-circuit 3` — must stay at 0 unprotected;
- `ed.sh gates`;
- `sweep_probe.sh book-02-iron-circuit 3 3` — must not rise;
- `formula_metrics.py` on ch16–22.

Then append "## Repair r1" to `AUTHOR-REPORT.md`, with:
- before/after metrics;
- the three intervals as now defined;
- a changelist.

Edit only ch16–22 and the report. Run no git commands.
