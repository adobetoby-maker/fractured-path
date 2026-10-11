#!/usr/bin/env python3
"""At a movement's close, refresh the author-sourced subsections of its AFTER MOVEMENT block in STATE_LEDGER.md
("### New canon minted" and "### State at movement end") from the AUTHOR-REPORT as updated after repair, so the
ledger does not keep pre-repair facts. Coordinator rulings, review record and inheritance are left untouched.
usage: ledger_refresh.py BOOK_DIR N"""
import re, sys
from pathlib import Path
book, n = Path(sys.argv[1]), int(sys.argv[2])
rep = (book / f"state/movement-{n:03d}/AUTHOR-REPORT.md").read_text()
def sec(text, pat):
    m = re.search(pat, text, re.M)
    if not m: return None
    e = re.search(r"^## ", text[m.end():], re.M)
    return text[m.end(): m.end() + e.start() if e else len(text)].strip()
canon, state = sec(rep, r"^## New canon minted.*$"), sec(rep, r"^## State at movement end.*$")
p = book / "STATE_LEDGER.md"; s = p.read_text()
m = re.search(rf"^## AFTER MOVEMENT {n} —.*$", s, re.M); assert m, "block not found"
e = re.search(r"^## AFTER MOVEMENT ", s[m.end():], re.M)
blk = s[m.start(): m.end() + e.start() if e else len(s)]
def swap(blk, head_pat, body):
    h = re.search(head_pat, blk, re.M)
    if not h or body is None: return blk, False
    nx = re.search(r"^### |^\*\*Movement \d+ CLOSED", blk[h.end():], re.M)
    end = h.end() + nx.start() if nx else len(blk)
    return blk[:h.end()] + "\n" + body + "\n\n" + blk[end:], True
blk2, a = swap(blk, r"^### New canon minted.*$", canon)
blk2, b = swap(blk2, r"^### State at movement end.*$", state)
p.write_text(s.replace(blk, blk2))
print(f"M{n}: canon {'refreshed' if a else 'unchanged'}, state {'refreshed' if b else 'unchanged'}")
