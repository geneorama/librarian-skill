# Local setup

Keep the live workflow, templates, and installation details where the user can edit them.
The installed skill contains general instructions and fictional examples only.

Startup instructions need a pointer to the current workflow and the local vault paths.
A small file beside the vaults works when they share a parent directory.
Use explicit paths when vaults occupy different directories or drives.
The file can live elsewhere if startup instructions identify its location.

Record only the context needed for the task:

- The live workflow path and any fallback copy.
- Vault names as they appear in `sync vaults`, with paths on this machine.
- The working vault, if it is fixed for that startup location.
- Relevant MCP or CLI connections and actual access limits.
- The sync template and existing type or folder guidance.

See [the local setup example](../config-sample/librarian.local.md).
Its filename is a suggested convention, not a requirement.
Existing startup instructions can supply the same information without another file.

Read the indicated live workflow rather than a pasted copy in startup instructions.
If the live workflow is unavailable, identify the fallback used and its known revision.
If no usable instructions or vault access exist for the operation, report the missing context.

Obsidian Sync can carry a vault between machines after an agent updates a reachable local copy.
That does not give the agent access to another vault on another machine.
Git can supply note history and backups when available.
Neither transport changes note identity or the whole-file comparison requirement.
