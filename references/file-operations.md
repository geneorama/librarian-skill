# File operations

## Linked binaries

Local binaries referenced through file links in notes should be synced as well. 
Copy missing binaries (pdfs and images) into the destination's established resource folder.
If the same filename exists but has different bytes, report the conflict and explain diference.
Do not infer the authoritative copy from dates alone or add note IDs to binaries.
After copying, confirm each binary's whole-file hash and the note's links to it.
Report missing or unreadable resources even if the Markdown copies match.

## Moves and removals

Move or rename existing files within a vault only when requested.
Before a folder move, establish the source and destination vaults.
List and count all affected files, including hidden files.
Apply the workflow's confirmation threshold to that full count.
Choosing a folder for a few notes does not authorize moving the folder or its other contents.

A rename needs Obsidian's link updates. Let the user rename manually when the CLI is unavailable or unreliable.
Do not substitute a shell rename that leaves those links unchanged.

Removing a vault from `sync vaults` expresses that the note no longer belongs there.
During the pilot, present the removal and compare the current copies' `sync vaults` values before acting.
If they differ, use the request and available history to establish the intended list of vaults.
Confirm that the retained content and the intended list are correct before removal.

DELETE moves the selected copy to `+sync/DELETE` for manual deletion when requested or approved.
The note remains in the vault until that manual deletion finishes.
A missing file alone does not establish whether a copy was deleted or has never been created.
Use the request and available history to decide whether to restore it or ask.
