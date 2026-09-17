# Frontmatter

The local sync template defines the field format.
Read it before adding fields. Preserve existing values and unrelated metadata.
Apply only the needed edits to the file, then compare the final whole-file hashes after copying.

The `_sync_fields_javascript` pattern adds a field only when that property is absent.
It preserves existing IDs and dates, uses the active vault as the origin, and leaves a missing type blank for later judgment.
Its configured destination names are installation data, not public defaults.
Read the template as a standard without assuming that reserializing YAML preserves the original bytes.

| Field | Meaning and format |
|---|---|
| `id` | Stable note identity, normally 12 lowercase hexadecimal characters |
| `created` | Known creation date, normally `YYYY-MM-DD HH:mm:ss` |
| `home vault` | The note's origin, not an automatic choice of authoritative content |
| `sync vaults` | Intended vault membership, as a comma-separated string |
| `type` | An existing type appropriate to the note and its placement |

Use these keys with spaces. Do not change the list into a YAML array.
An existing date-only value can remain date-only. Do not invent an unknown creation date.
An existing blank field needs interpretation, not automatic replacement.
Use the local convention for deliberately unsynced notes.
Having an ID or type alone does not request synchronization.
Every synced Markdown note needs a unique logical ID, shared with its corresponding copies.
The `sync vaults` field declares membership. Linked binaries are included without these note fields.

```bash
# Read-only: generate a candidate ID for a note that needs a new identity.
openssl rand -hex 6
```

Before assigning it, check for a matching note and ID collisions in reachable vaults.
Reuse the counterpart's ID when one already exists.
Do not replace an existing ID merely because its format differs from the template.
Report conflicting identities before changing them.

The following is a fictional example. Use the actual template and known metadata for a real note.

```yaml
---
id: a1b2c3d4e5f6
created: 2026-01-15 09:30:00
home vault: personal
sync vaults: personal, work
type: article
---
```
