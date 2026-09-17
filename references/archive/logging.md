# Logging and escalation

Locations are installation-specific (recorded with the vault registry). Example
convention: a `+sync/` folder in the primary shared vault holding `sync log.md`
and `sync-issues.md`.

## Sync log

One line per action, appended inside the log note's code fence. Fixed vocabulary —
never invent new action words; an unexplained verb makes the log unreadable later.

```text
2026-08-07T14:03:22Z librarian@host sync create personal work 80203c276b13 'CBOM kickoff' 'to inbox; 2 unlinked resources'
2026-08-07T14:05:10Z librarian@host identify write self self 3f91c2e07ab4 'Vendor risk checklist' ''
```

Fields, space-separated, single-quote anything containing spaces:

1. UTC timestamp, ISO with `T` (no space inside the timestamp — it must parse as
   one field)
2. `agent@host`
3. workflow: `identify` | `maintenance` | `sync` | `check`
4. action: `create` | `read` | `write` | `update` | `flag`
5. source vault (`self` when only one vault is involved)
6. destination vault (`self` when only one vault is involved)
7. note id
8. 'note name'
9. 'comment' — only when information would otherwise be lost; empty quotes are
   fine

## Issues note

All problems and questions in one note, one checkbox bullet per issue:

```markdown
- [ ] 2026-08-07 · 80203c276b13 · [[CBOM kickoff]] — conflict: both copies changed
    - evidence: personal modified 2026-08-06 (1a2b…), work modified 2026-08-07 (9f8e…)
    - options: keep personal / keep work / owner merges
```

The owner checks the box or replies inline; act only on the answer. Reference
open issues in later reports — never restate them.
