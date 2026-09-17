# Issues / proposals

Open ideas not yet folded into the skill. One item per heading. Discuss, then
either apply to the relevant reference file or drop.

## Proposal: initial setup instruction

Agent needs a small pointer for first run: rely on the docs, guide the owner
through setup per README/references rather than repeating setup steps in
SKILL.md itself.

## Note: frontmatter-patch rule needs work

Owner-guided direct edit (today, home vault originals) is different from
agent deciding to edit unsupervised — rule needs to say so. Also: hash-verify
skipped today by owner choice, no linting in place yet. Linting rules to
consider are not generic (line breaks, unicode/CJK handling) — owner has a
linting note in home vault to check first.

## Proposal: no vault registry → stop and ask

Agent needs a vault registry before doing anything. No registry → stop, ask
owner to initialize. Propose seeding it from config the agent already has.
Possible: check / suggest vault registry based on MCP connections.

## Proposal: new ground rule — use context, don't be clueless

Infer from what's already there before asking. Applies to registry/taxonomy
bootstrap and beyond. Candidate for SKILL.md ground rules.

## Proposal: no taxonomy → stop and ask

Same gap as registry. No real taxonomy note yet → stop, ask owner to
initialize, propose seeding it (see next item).

## Proposal: generate the type→folder table instead of hand-writing it

Idea: script that walks a vault, reads frontmatter `type` per note, counts
notes per (`type`, folder) pair, and prints a table. Purpose: surface
where each type actually lives, so real taxonomy stragglers (a type that's
supposed to be narrow but is spread across many folders) are visible at a
glance.

Note: general types (`note`, `project note`) scattering across several
folders is expected, not a straggler — only narrow types splitting are worth
flagging.

```python
import os, re, yaml
from collections import Counter

VAULT = "/path/to/your/vault"  # point at any vault root
counts = Counter()

fm_re = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)

for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fn in files:
        if not fn.endswith('.md'):
            continue
        path = os.path.join(root, fn)
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                head = f.read(4000)
        except Exception:
            continue
        m = fm_re.match(head)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:
            continue
        t = fm.get('type')
        if not t:
            continue
        folder = os.path.relpath(root, VAULT)
        if folder == '.':
            folder = '(root)'
        counts[(t, folder)] += 1

rows = sorted(counts.items(), key=lambda kv: (kv[0][0], -kv[1]))
print(f"{'type':<15} {'folder':<45} {'count':>5}")
print("-" * 67)
for (t, folder), c in rows:
    print(f"{t:<15} {folder:<45} {c:>5}")
print("-" * 67)
print("total typed files:", sum(counts.values()))
```

Not yet decided: where this belongs (taxonomy.md? a standalone tool doc?
just this issues note as reference?) and whether the skill should generate
this itself vs. the owner running it manually.
