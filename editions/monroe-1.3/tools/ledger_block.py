#!/usr/bin/env python3
"""Append an AFTER MOVEMENT block to a book's STATE_LEDGER.md and carry the audit's next-movement
inheritance into the next packet.
usage: ledger_block.py BOOK_DIR N "chapters A–B, days X–Y" RULINGS.md
RULINGS.md = the coordinator's rulings and review record (markdown, starting at '### Coordinator rulings').
Takes "New canon minted" and "State at movement end" from state/movement-NNN/AUTHOR-REPORT.md and
"…inheritance…" (section 8) from state/movement-NNN/plan-audit.md."""
import re, sys
import datetime
TODAY = datetime.date.today().isoformat()
from pathlib import Path
book, n, span, rul = Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3], Path(sys.argv[4]).read_text().strip()
st = book / f"state/movement-{n:03d}"
rep = (st / "AUTHOR-REPORT.md").read_text()
def sec(text, pat):
    m = re.search(pat, text, re.M)
    if not m: return ""
    e = re.search(r"^## ", text[m.end():], re.M)
    return text[m.end(): m.end() + e.start() if e else len(text)].strip()
canon = sec(rep, r"^## New canon minted.*$")
state = sec(rep, r"^## State at movement end.*$")
pa = (st / "plan-audit.md").read_text()
inh = sec(pa, r"^## 8\..*$")
block = f"""

## AFTER MOVEMENT {n} — {span} (drafted {TODAY}, author claude-opus-5-5, NO-SOURCE method)

{rul}

### New canon minted (author's list)
{canon}

### State at movement end (author; governed by the rulings above and by the surviving prose)
{state}

### Next-movement inheritance (Sol plan audit §8; also written into the next packet)
{inh}
"""
with open(book / "STATE_LEDGER.md", "a") as f: f.write(block)
nxt = book / f"packets/MOVEMENT-{n+1:03d}.md"
if nxt.exists() and inh:
    s = nxt.read_text(); key = "> **[Coordinator note 2026-10-11 — NO-SOURCE drafting, binding.]**"
    if key in s and f"inheritance from Movement {n}'s surviving prose" not in s:
        note = (f"> **[Coordinator note {TODAY} — inheritance from Movement {n}'s surviving prose (Sol plan audit §8), binding.]** "
                f"Read the edition's own closed chapters from disk and STATE_LEDGER \"AFTER MOVEMENT {n}\" before drafting. The audit's list follows.\n>\n"
                + "\n".join("> " + l if l.strip() else ">" for l in inh.split("\n")) + "\n\n")
        i = s.index(key); nxt.write_text(s[:i] + note + s[i:]); print("inheritance note added to", nxt.name)
print("ledger block appended")
