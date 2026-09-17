This Base lists notes with a type, home vault, or sync membership.
It includes candidates that are not yet registered for sync.
Confirm `id` and intended `sync vaults` before using an entry for a transfer.

```
filters:
  or:
    - note.type
    - note["home vault"]
    - note["sync vaults"]
views:
  - type: table
    name: Managed notes
    order:
      - file.name
      - created
      - id
      - type
      - home vault
      - sync vaults
    sort:
      - property: file.name
        direction: ASC
      - property: type
        direction: ASC
    columnSize:
      file.name: 247
      note.created: 104
```

