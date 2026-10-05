# Book 3 erratum v1.1 — queued (OWNER-DECISIONS #36), apply only after Book 2 locks

**Why.** Book 3 is not consistent with itself about the Reydan bout. Book 3 ch1, on the road, places the
Compression notice on "the night after his last circuit bout". Four later lines put the arrival "in the third
exchange" and call it "the notice" in the bout. The Book 2 map and the closed Book 2 text are:
- the fourth exchange;
- the fragment arriving involuntarily in the bout;
- the FRAGMENT ACQUIRED notice after the final low-stakes bout (with Ulric).

These five line fixes make Book 3 agree with Book 2 and with its own ch1. Each old string has been verified to
match exactly once.

1. `manuscript/chapter-22.md`
   old: `The hardest fight of his life had produced that notice, in the third exchange, with defeat close enough to touch`
   new: `The hardest fight of his life had produced it, in the fourth exchange, with defeat close enough to touch`
2. `manuscript/chapter-25.md`
   old: `as he had once laid it on Reydan in the third exchange`
   new: `as he had once laid it on Reydan in the fourth exchange`
3. `manuscript/chapter-29.md`
   old: `riding on the third exchange, and the third exchange going wrong, and the notice arriving so late`
   new: `riding on the fourth exchange, and the fourth exchange going wrong, and the thing arriving so late`
4. `manuscript/chapter-35.md`
   old: `in the third exchange of the bout that had ended everything in Ardenmere`
   new: `in the fourth exchange of the bout that had ended everything in Ardenmere`
5. `manuscript/chapter-35.md`
   old: `and the notice had come at the very last moment it could have come`
   new: `and the thing had come at the very last moment it could have come`

**Procedure after applying.**
1. Run `ed.sh overlap` for the affected movements (M3, M4, M5).
2. Re-hash `HASHES.sha256`, reissue `DIRECTOR_CUT_READY.md` as v1.1 with the new book hash, and tag
   `monroe13-book03-text-locked-v1.1`.
3. Republish Book 3 with `pwa_publish.py 3 61 --complete`, then verify the copy is byte-identical and live.
