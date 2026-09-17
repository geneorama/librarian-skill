---
name: librarian
description: Find, identify, copy, update, and compare notes between Obsidian vaults using stable IDs and whole-file SHA-256 checks.
---

# Librarian

Keep notes in sync while preserving their contents and meaning.
Use judgment to find notes, choose placement, explain differences, and recommend changes.
The person who creates or uses a note supplies decisions that its contents cannot establish.
Requests can come from that person or through another agent.

## Start with the current instructions

Read the local workflow referenced by the session or startup instructions before acting.
Read its current operational section again after compaction or when the user changes it.
Current user instructions take precedence over the workflow, which takes precedence over this general skill.
Historical notes and examples do not override current instructions.

Local paths, vault roles, templates, and placement conventions belong in accessible local notes or configuration outside the installed skill.
See [Local setup](references/vaults.md) when that context is missing.
Use known context without requiring a new registry or setup exercise.

Establish the working vault, the other vault, and which copies the agent can access.
The working vault is where the user is working, regardless of the agent's current directory.

| Request | Direction |
|---|---|
| “Sync this file” or “bring it over” | Other vault → working vault |
| “Update with my changes” | Working vault → other vault |
| Explicit source and destination | Follow the stated direction |

Retain this context across requests and handoffs.
State the resolved direction and destination path when acting.
Ask only when the request and available context leave the direction unclear.
The workflow note's own `sync vaults` field does not select destinations for other notes.

The user can lack access to a vault that the agent can reach.
If the agent cannot reach a required copy, report that operation as pending and identify the missing access.
Do not substitute a stale copy or claim a completed sync.

## Find and identify

Use MCP or a working Obsidian CLI for search, links, and graph context.
Use the filesystem for file edits and transfers. Use `rg` for focused text searches when appropriate.

EXACT SEARCH finds the requested note and its counterpart.
Match registered notes by `id`, including notes whose names or folders differ.
Confirm that an ID occurs in the note's actual frontmatter, not an example inside its body.

For an unregistered note, search names, aliases, titles, and distinctive text.
Use relevant links, backlinks, dates, people, and source URLs to distinguish candidates.
These are clues to identity, not proof that similar notes are interchangeable.
Keep searches focused on the request and expand them when the evidence requires it.

IDENTIFY adds missing sync fields after checking for an existing counterpart.
Reuse an existing ID across corresponding copies.
If neither copy has an ID, assign one shared ID after establishing that they represent the same note.
If different notes have the same ID, report the collision before copying.

Use the local templates as examples of field names, values, and note structure.
See [Frontmatter](references/frontmatter.md) before assigning fields.
Use existing types and propose a new type only when there is a clear gap.
An empty note can be intentional and valuable.

## Compare: hash, diff, read

RECONCILE establishes whether corresponding files match.

1. Hash the complete file with SHA-256, including frontmatter and every byte of whitespace.
2. If hashes differ, show the mechanical diff without excluding whitespace or metadata.
3. Read the relevant contents and explain what the differences mean.

```bash
# Read-only: hash both complete files, including metadata.
sha256sum '/absolute/source/note.md' '/absolute/target/note.md'

# Read-only: show differences without whitespace exclusions.
diff -u -- '/absolute/source/note.md' '/absolute/target/note.md'
```

The same `sha256sum` command works on a third copy, an older file, or a file outside Obsidian.
Use Linux or Git Bash on Windows for these commands.
Both commands must succeed in reading the files. A diff exit status of 1 means differences, not an execution failure.

Describe concrete differences: a missing phone number, a rewritten section, reordered metadata, a changed link, or a non-breaking space.
Expose invisible characters on the affected lines when necessary.
Do not dismiss whitespace differences or remove them from the report.

Consider whether text is original writing, a clipped source, or generated material when proposing a resolution.
Do not infer authority from punctuation or writing style alone.
File dates and `home vault` provide context, but neither proves which content to keep.
Different hashes establish a difference, not that both copies changed independently.

When links differ, establish what each link resolves to in each vault.
A filename change can redirect links to a different note even when the wording looks similar.
An unresolved link can be an intentional placeholder. Do not create a note just to satisfy it.

## Copy, update, and place

COPY inserts a missing counterpart. UPDATE / REPLACE brings an existing counterpart up to date.
For an explicit update, compare the copies and carry out the requested direction when the evidence supports it.
If the target contains competing changes, explain them and propose a specific resolution.
An approved merge is part of this workflow.

Copy the selected file with filesystem tools, such as `cp -p`, preserving dates where possible.
Complete needed metadata edits before copying.
For a merge, make the approved changes to one copy, then copy that completed file.
After the final edit, hash both complete files and confirm that they match.
If either file changes during review or copying, compare the current versions before continuing.

Preserve the source text during transfer. Do not rewrite, summarize, reformat, or normalize it.
For clipped articles, preserve the quoted source below the separator and the user's notes above it.
If a concern needs an annotation, propose a separate note above the source or in the report.
Keep the concern, suggested follow-up, and available session reference distinct from the source text.

PLACEMENT uses the destination's conventions and the note's type.
For example, an article in the source's `Clippings` folder belongs in the destination's established articles folder.
Do not reproduce the source folder structure automatically.
Use existing folders and confirm a new folder when the request does not already specify it.
Report missing linked images or PDFs. Copy them when the request includes those resources, then compare their whole-file hashes too.

Daily notes are not sync units. A request can refer to durable notes listed in a daily note without copying the daily note.
For personal-to-work transfers, flag personal material that conflicts with the requested work scope before copying it.
Propose any trimming or separate work version explicitly.

## Move, rename, and delete

MOVE changes placement. Check path-qualified links as well as filename uniqueness before moving a note.
A rename needs Obsidian's link updates. Let the user rename manually when the CLI is unavailable or unreliable.
Do not substitute a shell rename that leaves those links unchanged.

Removing a vault from `sync vaults` expresses that the note no longer belongs there.
During the pilot, present the removal and compare current metadata before acting, since copies can contain competing membership edits.
DELETE moves the selected copy to `+sync/DELETE` for manual deletion when requested or approved.
Confirm that the retained content and intended membership are correct before removal.
The note remains in the vault until that manual deletion finishes.

A missing copy is different from an unresolved link.
Absence alone does not establish whether a copy was deleted or has never been created.
Use the request and available history to decide whether to restore it or ask.

## Report and continue

Report the note, direction, actual destination, changes made, and whole-file hash result.
For a mismatch, show the relevant diff and a recommendation that the user can accept or correct.
If a difference is intentionally retained, report the reason and keep its status distinct from a hash match.
Approval of one difference does not excuse new differences in the same note.

Routine requests concern the named notes. Run a wider review or batch only when requested.
For more than ten affected files, present the count and obtain confirmation for that scope.
Count source metadata edits, linked notes, and resources as well as destination copies.
Use the requested batch size when presenting proposals.
Keep pending decisions visible in the conversation or designated handoff note.
Write a separate sync log only when the local workflow requests one.

For a membership report, compare declared `sync vaults` with actual placements by ID.
The existing Base example and small reporting scripts are optional aids described in [README.md](README.md).
