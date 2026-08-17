# Sync frontmatter (settled format)

This format is settled — do not restyle it. Keys are lowercase **with spaces**
(`home vault`, not `home_vault`); the vault list is a **comma-separated string**,
not a YAML array. The owner stamps new notes in Obsidian with a Templater
shortcut that writes exactly these fields; librarian stamps must be
indistinguishable from the owner's.

```yaml
---
id: 80203c276b13
created: 2026-08-04 23:43:43
home vault: personal
sync vaults: personal, work
type: note
---
```

## Field rules

| Field | Rule |
|---|---|
| `id` | 12 hex chars = 6 random bytes (`openssl rand -hex 6`). Collision-**checked** (search all reachable vaults before stamping), not collision-resistant. Never content-derived — it must survive edits. Never timestamp-derived — same-minute notes collide systematically. |
| `created` | `YYYY-MM-DD HH:mm:ss`, from the file's creation date or the note's own Timeline section. Add only when actually known; never guess. Date-only values appear in older notes and are acceptable. |
| `home vault` | The authoritative origin vault — typically the personal master for personal-origin notes. |
| `sync vaults` | Every vault the note belongs in, **including the home vault**. `<none>` = managed but deliberately unsynced. |
| `type` | Optional; values only from `taxonomy.md`. Not every note needs one, and having one does not itself mean synced. |
| `differences allowed` | Optional. `true` = copies are expected to diverge; a hash mismatch is an alive-check, not a problem. Absent = copies must match. |
| `private` | Optional. `true` = never propagate to any other vault. A soft signal — its absence proves nothing (see the Judgment section of SKILL.md). |

## Stamping example

Before (note with existing frontmatter — add only what's missing, preserve
everything present):

```yaml
---
aliases: [CBOM kickoff]
author: Gene
---
```

After:

```yaml
---
aliases: [CBOM kickoff]
author: Gene
id: 3f91c2e07ab4
created: 2026-08-07 09:15:00
home vault: personal
sync vaults: personal, work
---
```

A note with **no** frontmatter gets a new block at the very top containing only
the sync fields; the body starts exactly where it started before — byte-for-byte.

## Legacy patterns — flag for normalization, never imitate

- `home_vault:` / `sync_vaults:` (snake_case, from early designs)
- `sync_vaults: [coc-work]` (YAML arrays)
- ULIDs or 8-hex ids

When found, list them in the review report; normalize only on instruction.
