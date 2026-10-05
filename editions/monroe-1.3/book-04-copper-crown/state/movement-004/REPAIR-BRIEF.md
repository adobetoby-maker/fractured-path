# Repair brief — Book 4, Movement 4 (one consolidated same-author repair)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Sol (review seat). The cold read saw the
manuscript only.

**Verdict.** Both readers would continue without hesitation. The editorial found no canon breach, no change to
protected wording, no reserved-truth leak and no Reader Standard problem. All protected lines are exact, and the
chronology holds: the pin comes before session fifteen, which is the Fiske seeding bout. Lira's record and
standing, the attention-budget sequence and the knowledge boundaries all verify. Both name the same strengths:
- the ethics meeting as real moral traction (four distinct voices; Cael admits the want);
- the absent grind at the post;
- Seln's protective omission as dramatic irony;
- the Fiske bout changing what each fighter can trust, exchange by exchange;
- Brom's loss turning into a repair, not a disguised win.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings on your owner flags
1. **ABBOT — use the name.** OWNER-DECISIONS #11 lists **Abbot** as the placeholder until approved. The same
   policy applies to Book 2's Bede and Maud: draft under the screened proposal, never a bracket, so that one
   find-and-replace applies the owner's choice. Name him **Abbot** once, where Lira first meets him on the board
   or at the call (ch24). Keep "the Mire boy" and similar where it reads naturally after that.
2. **Top-line challenges are fought on the final's terms: ACCEPTED as canon.** That means four exchanges on
   glass, the winner is whoever holds more touches, and a draw keeps the holder. Movements 6 and 8 must honour it.
3. **Lira on the second line at 6–0, with the Fiske bout as her challenge for the top: ACCEPTED.** The editorial
   verified it against BOOK_MAP.
4. **The dawn Compression drill in a private wash-house sandbag rig: ACCEPTED.**
5. **The Seln window, about 2,080 words: ACCEPTED.** Do not pad it, and do not cut it to the number.
6. **Fiske's "one signature that isn't mine": ACCEPTED as canon** for the advancement evaluation. It is planted
   for Movement 8, where "decision point" stays reserved. Do not explain the mechanism further here.

## Priority 1 — Two definite continuity and clarity fixes
1. **Brom's weekly count (editorial; high confidence).** In ch26, Rooke prescribes "Four a week", and Karis rules
   four boxes per week. Ch29 then has "Brom did his fifth exercise of the week". Make it "fourth", or justify a
   make-up drill in one clause and show how Karis records it.
2. **The standings arithmetic (cold).** The board's "Copper 2 — 6/0" is glossed in ch25 as "Six bouts and six
   wins, one of them the drawn bout". A draw cannot be a win; read aloud, it sounds like an arithmetic error.
   - Ruling: the board figure is **bouts unbeaten / bouts lost**, and a draw counts as unbeaten (ch21 already
     says the drawn bout "counted in the record and moved nobody on the sheet").
   - At the first gloss in ch25, define it in a phrase: six bouts and none lost, five won, and one the drawn bout
     that moved her nowhere. Use the same terms for "Nine and nothing" in ch29.
   - Check the ch27 observer map too. Seln is the ninth dot. Make sure the prose cannot be read as a tenth person
     after nine bodies have been listed.

## Priority 2 — The ethical question is settled once (both reviewers)
From Karis's finding in ch22, through the ch23 debate, to the ch24 opening Log, the movement states the
following three times in close succession:
- the conditions;
- the consent problem;
- the refusal to manufacture an encounter;
- Cael's admitted want;
- the advance accounting.

Compress it so each beat is said once, in its strongest place:
- **ch22** finds and admits ("Yes").
- **ch23** argues and signs.
- **ch24's opening Log** carries only what is new: the signed rules as a short reference, and the insight that
  Cael can build either side of an internal argument to win.

Thin the gift / floor / weapon / fence / bill / room run in ch23. Each moral voice should keep its one governing
image, so a thirteen-year-old hearing it aloud can tell which sentence is the rule. Keep Cael's three numbered
rules as the plain procedural spine. Keep "church, with sums", the horse, the hats list, and every protected line
(Karis's conditions statement, Brom's weapon line, "Last year's me…", Karis's instrument line).

**Secondarily, in ch28:** break Seln's longest warm/cold audit paragraphs where the claim actually turns.
Remove nothing from his four scripts or his file-drawer close.

## Priority 3 — The ending lands once (cold)
After the table calls the bout in ch29, three passages interpret what the victory means: the Fiske
conversation, the lamplit post scene, and Cael's closing Log. Keep the full Fiske exchange (protected), Brom's
forty repetitions, and Cael's uncertainty about leaving Lira alone. Trim only the duplicated crown-versus-
recognition interpretation from the closing Log, so the final image and the sleeping laugh stand.

## Priority 4 — Rhythm, by hand only
- The sentence mean (13.56), ≥40-word share (4.3%) and words per scene (858) are inside the working ranges.
- The median of 9 and the paragraph mean of 40 come from clipped runs sitting beside long analytical
  paragraphs. Where you are already working, join clipped sentences that are one thought, and split analytical
  paragraphs only at a true turn.
- Do not lengthen globally, and do not add vocabulary.
- Hold ≥40w ≤ 4.5%, and do not let words per scene fall below 850. Merge a scene break only if a scene is
  genuinely one movement of thought.

**Length.** Finish within 36,500–38,500 words. Trimming in P2 and P3 is expected.

## After the repair
Run:
- `ed.sh overlap book-04-copper-crown 4` (must stay 0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-04-copper-crown 4 4` (stay ≤ 5% skeleton, and keep close ≤ 13%);
- `formula_metrics.py` on the eight chapters.

Then append "## Repair r1" to `AUTHOR-REPORT.md` with:
- before/after metrics;
- overlap and probe results;
- the changelist, by chapter.

Edit only chapters 22–29 and AUTHOR-REPORT.md. Run no git commands.
