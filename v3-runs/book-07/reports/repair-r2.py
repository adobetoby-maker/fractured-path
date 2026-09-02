import re
p='books/book-07-void-roads/CHAPTER_ARCHITECTURE.md'; s=open(p,encoding='utf-8').read()
MISS=[]
def rep(old,new,exact=1):
    global s
    n=s.count(old)
    if n!=exact: MISS.append(f"COUNT {n} (want {exact}): {old[:100]}"); return
    s=s.replace(old,new)
def repall(old,new):
    global s
    if old not in s: MISS.append("ABSENT: "+old[:100]); return
    s=s.replace(old,new)

# ---- E01 (remaining) ----
rep("**Arc: Nothing out here measures me → the oldest thing out here measures only me**",
    "**Arc: Nothing out here measures me → the oldest thing out here doesn't measure me either, and it measures everything else**")
rep("*No instrument out here reads me* → *The oldest instrument out here reads only me.*",
    "*No instrument out here reads me* → *The oldest thing out here doesn't read me either — and it reads everything else.*")
rep("and *something older than the registry paced these circles before there was a registry — and it does not hold me.*",
    "and *every Path in the party died at a line somebody paced before there was a registry, and mine didn't, and nobody alive knows why.*")
rep("There aren't any banks in you. It isn't that you're broken. It's that there's nothing here shaped like the thing I read.\" She stops.",
    "I can't find the banks in you. I've looked for twenty minutes. It isn't that you're broken. It's that I can't find anything shaped like the thing I read.\" She stops.")
rep("Ten currents, the way Oryn said: banks nowhere, channels nowhere, ten flows moving through an architecture that does not constrain them.",
    "Ten currents, the way Oryn said: he cannot find the banks either, cannot find where one flow stops and the next begins, and the not-finding is described as what it is — a limit of the reading, his and hers — and not as a fact about the architecture.")
rep("\"Inside the circle, I'm the only one who works. They built a floor to make us helpless. They don't know they built it for me.\"",
    "\"Inside the circle, I'm the only one who works. They chose a floor that makes the rest of you helpless. They don't know it doesn't do anything to me.\"")
rep("Nothing out here had read him. Except the oldest thing out here — and nobody alive, least of all him, knew what it had read.",
    "Nothing out here had read him. Four floors older than any registry had let every Path in the party die at a line and let his stand, and nobody alive — least of all him — knew why. Someone had made the pattern. That was as far as anyone could say.")
rep("but that something older than measurement paced these floors first — and whatever it measured, it does not hold him.",
    "but that something older than measurement paced these floors first, every Path in the party fails inside them, his does not, and nobody — including him — is permitted a *why* on the page.")
rep("\"Nothing out here reads me. Except the oldest thing out here, which reads nothing else. Karis won't write her hypothesis.",
    "\"Nothing out here reads me. The oldest thing out here doesn't either — and it reads everyone else at a line you can mark with a rock. Karis won't write her hypothesis.")
rep("landed finally over the map, Ch24 — *the oldest instrument out here reads only me*.",
    "landed finally over the map, Ch24 — *the oldest thing out here doesn't read me either, and it reads everything else*.")

# ---- E03 (remaining) ----
rep("the reading takes minutes, not seconds, and the patient must be still;",
    "the reading has two modes, taught in Ch7 before either is load-bearing: the *surface* reading — hands on the hurt, seconds, finds injury and the Path beneath it — and the *deep* reading — both hands, the healer's whole current run through the whole architecture, minutes, patient still and uninjured, at a mending's cost; whole-architecture knowledge is available ONLY from the deep reading;")
rep("he could know, in a second, what a Bronze Force practitioner who stopped reporting six years ago is built like, and whether the not-reporting left a mark.",
    "he could know — not in a second; in the minutes the deep reading takes, with Teague still and willing, which Teague is not and has not been asked to be — what a Bronze Force practitioner who stopped reporting six years ago is built like, and whether the not-reporting left a mark. The surface reading, a hand on the wrist, would give him Teague's Path and nothing more; even that he does not take.")

# ---- E05 (remaining): cold-test the Anchor point ----
rep("Seln's finding, entered on Karis's page: it is blind; it reads *weight on the floor*; it strikes where the weight is; and it strikes *what stays* — a stone that lands and settles gets hit, a stone that skips gets ignored. The rule the fight will run on, taught cold.",
    "Seln's finding, entered on Karis's page: it is blind; it reads *weight on the floor*; it strikes where the weight is; and it strikes *what stays* — a stone that lands and settles gets hit, a stone that skips gets ignored. And the third trial, Cael's, run from the wall's top with Karis timing it: an Anchor-adjacent fixed point laid on the flooded floor twenty paces out — the binding taken from the Ostrand road, which fixes a point *against* the surface it is laid on, and which since B6 Ch14 has wanted to fix points in ordinary doorways — and the water answers at the point, and keeps answering, and keeps answering after every stone has gone quiet, because a fixed point is weight that never stops arriving. Karis: \"It reads that as the heaviest thing on the floor.\" Cael, releasing it: \"It reads that as the thing that *stays*.\" The rule the fight will run on, taught cold, including the one piece of it that is his.")

# ---- E07 (remaining): make Shadow explicit on the Stair approach ----
rep("He walks up into the bowl with the full suite held to nothing, a body among bodies, invisible to a team scanning for declarations that cannot exist here, and reaches the perimeter's lattice,",
    "He walks up into the bowl with the suite held to nothing but one thing — Shadow-adjacent, presence thinned to nothing, movement folded into the bowl's dusk, the fragment whose public seal the book has kept and keeps here by its whole function: the rim team is scanning for declarations that cannot exist inside the line, and the one declaration that does exist is the one whose entire craft is not being seen; they never perceive him, and what is never perceived cannot be attributed — and reaches the perimeter's lattice,")

# ---- N02 ----
rep("She does not learn the mechanism until Chapter 16, and consents to what she cannot know about in Chapter 13",
    "She learns the mechanism in Chapter 14 (the circle's wider council is Chapter 16), and consents to what she cannot know about in Chapter 13")

# ---- N03: Lira's arm state ----
rep("and the mending run *at the line* by lamplight because there is no moving Lira further — an hour, the worst she has healed in two years, and it costs her the way the traverse cost her and more; she sits down on the road afterward and does not get up for a while, and Lira keeps the arm.",
    "and the mending run *at the line* by lamplight because there is no moving Lira further — an hour, the worst she has healed in two years, and it costs her the way the traverse cost her and more; she sits down on the road afterward and does not get up for a while, and Lira keeps the arm. The state, defined on the page because the book will carry it for ten chapters (charter §2.8): the vessels closed, the deep tear closed, the arm *saved* — and a healer's mend of that depth bears no load for a season; Oryn's order, in her register, is that the arm is not to be used to hold, strike, or catch until she says, and Lira fights one-armed from here to the first snow.")
rep("*Close on (dialogue):* Lira, on the road, the arm whole and the ankle not,",
    "*Close on (dialogue):* Lira, on the road, the arm saved and slung and the ankle not,")
rep("Lira's arm reopened;","the mend on Lira's forearm reopened where she caught herself on the stair, which is exactly what Oryn said it would do if it held anything;")
rep("Lira — Wind Path, Iron R1 formal; forearm bitten through (Ch11) and mended (Ch13); ankle gone three times and mended once (Ch6) — she fights one-armed from Ch11 through Ch21 and the book carries it (charter §2.8);",
    "Lira — Wind Path, Iron R1 formal; forearm bitten through and saved by an hour's mending at the line (Ch11), load-restricted by Oryn's order for the season, the mend reopened at the Stair (Ch19) and closed again outside the line; ankle gone three times (Ch3, Ch6, Ch11) and mended once (Ch6) — she fights one-armed from Ch11 through Ch24 and the book carries it (charter §2.8);")

# ---- N01: roster normalization (five before Oryn, six after) ----
rep("**Companions introduced: Oryn (Tide Path, Iron-tier, traveling healer — the seventh and last chair; the roster is complete after this book)**",
    "**Companions introduced: Oryn (Tide Path, Iron-tier, traveling healer — the sixth and last chair; the roster is complete after this book). Party entering the book: FIVE — Cael, Lira, Brom, Karis, Seln (see the seam note in the Continuity Checkpoint on Book 6's \"six\")**")
for old,new in [
 ("The six of them walk it at dusk, the carter behind","The five of them walk it at dusk, the carter behind"),
 ("a mile of road, six practitioners with everything they own held in check","a mile of road, five practitioners with everything they own held in check"),
 ("Teague reads the six of them the way Cael reads everyone","Teague reads the five of them the way Cael reads everyone"),
 ("*Stillhound pack, Thornwater ford: cleared. Five confirmed. Crew of six, four injured, none lost. Price paid.* Cael reads it and writes beneath the copy: \"First honest number anyone's written about us in a year. It says four of six got hurt. It's right.\"",
  "*Stillhound pack, Thornwater ford: cleared. Five confirmed. Crew of five, four injured, none lost. Price paid.* Cael reads it and writes beneath the copy: \"First honest number anyone's written about us in a year. It says four of five got hurt. It's right.\""),
 ("what it would cost the six of them","what it would cost the five of them"),
 ("The walk up is the book's first true freedom chapter, and the prose should let it be one: five days of high country","The walk up is the book's first true freedom chapter, and the prose should let it be one: five days of high country"),
 ("\"You cleared Thornwater's ford with six and lost a cart on the high bench with five.\"","\"You cleared Thornwater's ford with five and lost a cart on the high bench with five.\""),
 ("The council, that night, at Lowmarch's inn, six voices:","The council, that night, at Lowmarch's inn, five voices:"),
 ("Seven on the road. The book is honest that this is the first time the seventh chair has walked with the six, and does not underline it.","Six on the road. The book is honest that this is the first time the sixth chair has walked with the five, and does not underline it."),
 ("Five practitioners with no Paths and a healer with no hands watched the seventh use his","Four practitioners with no Paths and a healer with no hands watched the sixth use his"),
 ("six people saw; he has told nobody","five people saw; he has told nobody"),
 ("I have five people who saw what I did inside, and one healer","I have four people who saw what I did inside, and one healer"),
 ("The circle, that night, seven for the first time — Oryn included","The circle, that night, six for the first time — Oryn included"),
 ("at a site where the poster knows six practitioners will be five bodies and one anomaly","at a site where the poster knows five practitioners will be four bodies and one anomaly"),
 ("*Close on:* the Long Stair's ridge at dusk, the seven of them,","*Close on:* the Long Stair's ridge at dusk, the six of them,"),
 ("where six people with no Paths can hold a doorway against six people with Paths","where five people with no Paths can hold a doorway against six people with Paths"),
 ("and a crew of seven alive in a place","and a crew of six alive in a place"),
 ("and the seven of them back down the stair with lamps","and the six of them back down the stair with lamps"),
 ("high autumn, the void roads emptying for winter, the seven of them on a bearing","high autumn, the void roads emptying for winter, the six of them on a bearing"),
 ("\"Bring the map.\" Six on the bearing.","\"Bring the map.\" Five on the bearing."),
 ("*Crew of seven. Ford cleared,","*Crew of six. Ford cleared,"),
 ("and six people, one of them on a route, who've walked into the quiet three times and come out.","and five people, one of them on a route, who've walked into the quiet three times and come out."),
 ("the circle's third expansion (Karis B3, Seln B6, Oryn B7) — seven people;","the circle's third expansion (Karis B3, Seln B6, Oryn B7) — six people;"),
 ("Seven, by letter. The chapter lets the seventh chair be filled by post","Six, by letter. The chapter lets the sixth chair be filled by post"),
 ("the seven of them in a steading's common room","the six of them in a steading's common room"),
 ("seven intelligent people look at the largest fact","six intelligent people look at the largest fact"),
 ("and the seventh chair filled on her terms, not the book's","and the sixth chair filled on her terms, not the book's"),
 ("**Oryn (the seventh companion — differentiation note, structural):**","**Oryn (the sixth companion — differentiation note, structural):**"),
 ("The seventh chair, filled — by a woman","The sixth chair, filled — by a woman"),
 ("**Book 7 delivery (Oryn joins — the seventh chair):**","**Book 7 delivery (Oryn joins — the sixth chair):**"),
]:
    rep(old,new)

# ---- seam note for Book 6's count ----
rep("- [ ] **Age handled deliberately — no silent drift:** Cael is eighteen at Chapter 1",
    "- [ ] **SEAM DEFECT INHERITED FROM BOOK 6's ARCHITECTURE — flagged, NOT repaired here (Book 6 is being drafted on another machine):** Book 6's cards count \"the six of them\" from Ch8 onward, \"six hands, unanimous\" (Ch17), \"Six of us. No desks.\" (Ch24), and \"five people who signed out\" in its last line — but only FIVE people cross the Line: Cael, Lira, Brom, Karis, Seln (Ephram stays, Ch20–21; nobody else resigns). The count appears to be carried over from Book 5's six-person delegation (which included Ephram). Book 7 normalizes to the true roster — five travelers entering, six after Oryn (Ch9) — and every card, ledger entry, witness count, and chair number in this document uses those figures. Book 6's drafting team should resolve its own count before its prose freezes; if Book 6's prose settles on six for a reason this document cannot see, this checkpoint and Book 7's Chapter 1 must be re-verified (editor findings N01, r2).\n- [ ] **Age handled deliberately — no silent drift:** Cael is eighteen at Chapter 1")

if MISS:
    print("MISSES:"); [print(" -",m) for m in MISS]
else:
    open(p,'w',encoding='utf-8').write(s); print("OK",len(s.split()))
