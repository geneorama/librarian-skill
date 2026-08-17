Example base for monitoring notes that need to be synced. 

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


