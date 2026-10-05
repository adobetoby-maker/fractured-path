# Repair brief — Book 2, Movement 8 (one consolidated same-author repair; the book's last)

**Sources.** `review-editorial.md` and `review-cold.md`, both from Claude Fable, fresh context. Fable has the
review seat while Sol is out of quota. The cold read saw the manuscript only.

**Verdict.** Both readers would continue without hesitation. The peaks they name:
- the Reydan bout (the second-exchange forearm hit; exchange four);
- Lira's cutaway at the rope;
- Reydan's chapter, "more interested than hurt";
- Hesk's three-sentence letter;
- Vell's sheaf.

The cold reader checked the ch55 Log against the narrated bout and found it adds up exactly: 14 knocks / 12
answered / 6 Wind / 3 redirects / 3 strikes. Readers trust Cael's arithmetic, and this keeps that trust.

The editorial confirms:
- the ending meets BOOK_MAP §1 item by item;
- protected lines are present (three need restoring, below);
- reserved truths are untouched;
- the Reader Standard passes;
- overlap with the source is 0 unprotected.

Pre-repair text is frozen in `pre-repair/`. Repair in reading order, in place, by reading — never by script.

## Coordinator rulings (OWNER-DECISIONS #36; binding)
**The closed, locked edition Book 3 governs where it is consistent with itself.**
1. **The redirect shoulder is the RIGHT.** Book 3 says this three times: ch1:45, ch1:111 ("each paid for in the
   right shoulder") and ch6:91/201. Book 2 conforms.
   - In **closed M7**, change only the lines that name the side of the redirect drill: ch47:117 "turned his left
     shoulder to it", ch51:159 "favouring his left shoulder", and any other M7 line that puts the redirect groove
     on the left (grep `left shoulder|left arm|groove` in ch44–51). You are authorised for exactly those
     side-words in ch44–51 and nothing else there.
   - In **M8**, all three bout redirects are paid in the right shoulder. The Compression gathers in that same
     shoulder and returns along its channel, so B3 ch1's "the one the Reydan bout had already used hard" is
     literally true.
   - Keep the counts: three redirects, the cap, and the ch55 tally exact.
   - Re-check every M8 body-state line (ch53–58, ch60) for the side. The forearm hit in exchange two stays where
     it is (left forearm).
2. **The track name.** Book 3's gate clerk says "observer track", and Book 2's formal name is "demonstration-
   provision track". Let Quenna or Cael use both once in M8, in one clause, for example the formal name and then
   "the observer track, she called it, the way the gate list would". After that, use either.
3. **The season.** Book 3 opens the road in "early autumn". The B2 map says name no months.
   - In ch60, the departure morning has NO frost and NO snow, and names no season. Use cold, breath and wet
     stone if you need weather.
   - Quenna's "before the first snow on the hill road" (ch57) becomes "before the weather turns on the hill
     road".
   - Remove any other first-snow or frost image on the departure days and on the road.
4. **Exchange and notice.** Keep the map: the fourth exchange; Compression involuntary in the bout; the notice
   after the final low-stakes bout. Book 3's ch22/ch35 wording is queued as a Book 3 erratum. Do nothing on the
   Book 3 side.
5. **Log format.** Four headings per fragment, begun with Compression. ACCEPTED.

The author's other flags are accepted: the ch51 rope positions; Ulric (established); Hesk's reply on day 5, with
Quenna agreeing to wait; Bede and Maud as placeholders; the reworded packet lines.

## Priority 1 — ch60, the roadside tests: re-image them against Book 3 ch1 (editorial)
Scene 5, from "They tested the fragment at the midday rest" to "*Exactly like Wind at the start.*", shares Book 3
ch1's figurative language and sequence:
- a 20-word verbatim run ("had laid a hot iron bar along his collarbones and leaned on it. For two breaths he
  could not fill his lungs");
- "like a door shutting in another room";
- "a weight a man could count";
- "like a flat stone";
- "'Quarter.' / 'Quarter.'";
- success on the seventh try;
- "a road of its own… he chose one for it".

Keep every beat and result:
- inert;
- the piece sent into the knee;
- the early reaches that get nothing;
- the waited-for try, a quarter sent home;
- the cost in shoulder, breastbone and teeth (the RIGHT shoulder now);
- the Log line.

Re-image the push, the knock back, the bill and the two-word exchange in raw, day-one language Cael has not yet
settled into, so that Book 3's images read as the matured versions three days on. Same length. Keep the cat that
"has heard its name and decided not to know it", the teeth, and "*Exactly like Wind at the start.*"

**Then prove it.** Run this check and report it. Zero 8-word runs is the goal; names and short stock phrases
are fine.

```
python3 - <<'PY'
import re
def ng(p,n=8):
    w=re.findall(r"[a-z']+",open(p).read().lower()); return {' '.join(w[i:i+n]) for i in range(len(w)-n+1)}
a=ng('editions/monroe-1.3/book-02-iron-circuit/manuscript/chapter-60.md')
b=ng('editions/monroe-1.3/book-03-no-path-given/manuscript/chapter-01.md')
print(len(a&b)); [print(x) for x in sorted(a&b)]
PY
```

## Priority 2 — Consistency with closed text and protected lines (editorial; cold)
1. **ch59, Ansel.** "he'd been nineteen that year and so had I" contradicts closed ch46 (Ansel "perhaps
   twenty-seven or twenty-eight"; "Nineteen. I was twenty-four."). Give him his age back in one clause.
2. **ch56, Quenna.** "Eight bouts on the main floor, seven won…" Closed ch17's eight-and-seven predates the Cael
   bout, and those bouts were not main-floor cards. Drop the figures, or make them true (nine and eight) without
   "main floor".
3. **ch60, protected lines restored whole.**
   - `"It's a start."` and `"It's more than we had when we got here."` carry a comma where the map has a period.
     Restore each protected sentence whole, with its attribution before or after it.
   - `"I have four things that aren't a Path… This might be enough."` must not be split by a tag. Put the
     attribution and the long walk before the line, and keep the four-line close in its order.
4. **Calendar and figures (cold).**
   - Hesk's Thursday-to-Sunday reply is too fast against a two-day coach each way. Make the days work, or make
     the coach faster in a clause.
   - Dace's "a month" and Quenna's "six nights" must agree, or say why they differ.
   - The narrator's absolute "He never would" about the anonymous regular becomes something Cael believes, not
     the narrator.
   - In ch58, the paragraph order of Tuesday / Monday / Tuesday should run in day order.

## Priority 3 — Say it once; clarity at the notice (both)
- **ch60 (cold).** The Reydan/Cael nod and the carter's shout are narrated twice (about lines 39–43 and 85–87).
  Cut the duplicate on Cael's side.
- **ch58–60 (cold).** The session-nine distinction is proved in ch55. After that, state it at most once more
  (the anomaly leaf, "One anomaly. Still one.").
- **ch59–60 (cold).** The farewell walk repeats signature lines already used in ch55/57 ("Feeling well?", "in my
  light", "Bring it back full"). Thin the market walk so each leaving has one beat that is new. Keep Vell's copied
  record and her offer, Brom's goodbyes, Dace's sealed note, Lira's line and Reydan's nod.
- **ch58, the notice (editorial).**
  - Brom's "It's mine. It's the thing I found in the boat shed." sounds like he is claiming the fragment. Make it
    the trick ("That's my trick… only you did it soft"), and keep Cael's "I didn't do it. It did."
  - "The quiet that had come three times before" is the wrong count. Make it "the quiet that came with every
    notice", or similar.
- **To taste.** Drop a redundant "said X" where the paragraph already names the speaker (Ulric, ch58; the
  cookshop, ch59). Thin "that" in narration only; never touch a spoken line.

**Length.** Finish within 38,500–41,000 words. Keep the bout whole, and keep Lira's and Reydan's cutaways.

## After the repair
Run:
- `ed.sh overlap book-02-iron-circuit 8` (0 unprotected);
- `ed.sh gates`;
- `sweep_probe.sh book-02-iron-circuit 8 8` (≤ 5% skeleton);
- `formula_metrics.py` on ch52–60;
- the B3 ch1 8-gram check above;
- `ed.sh overlap book-02-iron-circuit 7` (M7 must stay at 0 after your side-word edits).

Append "## Repair r1" to AUTHOR-REPORT.md with:
- the shoulder changes, line by line, including M7;
- the B3 8-gram result;
- before/after metrics;
- the changelist, by chapter;
- a final hand-off check against BOOK_MAP §1 and B3 ch1.

Edit only ch52–60, the M7 side-words authorised above, and AUTHOR-REPORT.md. Run no git commands.
