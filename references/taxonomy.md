# Type taxonomy (example — adapt per installation)

Sync is driven by **frontmatter metadata only**. Tags play no role in sync
control, ever.

A note's `type` determines its sync behavior and where it lives in each vault.
The taxonomy is owner-curated and deliberately small — the librarian proposes new
types via the issues note and never invents one. Taxonomies may differ per vault;
the owner's live version belongs with the vault registry (a managed note in the
agent vault). The table below is a starting example any installation can adapt.

**No real taxonomy note yet?** Same as the vault registry: stop before
placing anything by type, and offer to seed one — see "Building your own
type→folder table" below — rather than asking the owner to enumerate types
from memory.

## Sync behaviors

- **verbatim** — copies are byte-identical across declared vaults; hash mismatch
  = out of sync.
- **behavioral** — the file itself is not copied; the type carries a procedure
  instead (see `daily` below).
- **none** — never leaves its home vault.

## Example types

| type | behavior | identity rule | example location |
|---|---|---|---|
| `daily` | behavioral | date | the folder set in Obsidian's Daily-notes setting. Daily notes are data sources, not sync units — the meeting/project notes they link are what sync. |
| `meeting` | verbatim | people + date — two meeting notes matching both are the same meeting, regardless of title or vault | `meetings/` in the relevant work vault |
| `person` | none | name + aliases — a person note is a different entity per vault (work-you and personal-you know different things about them) | `people/` |
| `article` | verbatim | source URL | `clippings/` or `articles/` |
| `project` | verbatim, often `differences allowed: true` | project name | `projects/` |
| `policy` | verbatim | name | shared vault, `policies/` or root |
| `note` (topic) | verbatim | title + aliases | `notes/` |

## Placement rules

- Type has a mapped location in the destination vault → place there.
- No mapping → the destination's inbox, and say which you chose in the log.
- Flat, property-organized vaults (kepano-style: minimal folders, a `category`
  property) work fine — a "location" can be a property rule instead of a folder.
- Not every note needs a type, and having one does not itself mean synced —
  `sync vaults` alone declares membership.
- Some types are legitimately general (`note`, `project note`) and turn up
  scattered across several folders — that's normal, not a straggler. Flag
  scatter only for types meant to be narrow.

## Building your own type→folder table

Don't hand-maintain the taxonomy from memory — generate it. `scripts/type-aggregator.py`
counts notes per (`type`, folder) pair, showing where each type actually
lives, so real stragglers (a narrow type spread across more folders than it
should be) are visible at a glance. Not a live query — re-run and re-paste
when the taxonomy needs a refresh.

```
python3 scripts/type-aggregator.py --vault <vault_path>
python3 scripts/type-aggregator.py --vault <vault_path> --fixed  # fixed-width text instead of a markdown table
```

Paste the output into a note kept with the vault registry — that table, not
the example above, is what the librarian reads for placement decisions once
one exists.
