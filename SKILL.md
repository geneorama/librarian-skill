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

The pilot covers interactive, directly requested work, including explicitly requested batches.
Run the workflow's applicable preconditions before a cross-vault operation. If one fails, stop that operation and report why.
Always load the relevant Obsidian skills before their operations: Markdown for notes, CLI for CLI use, and Bases for Base queries.
If a required skill is unavailable, pause its dependent operation and report the gap.

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

Use MCP for backlinks, meaning links from other notes to the selected note.
Use its supported search, outgoing-link, and metadata queries for relevant graph context.
Confirm what the connected server actually returns and whether its results are complete.
Use the filesystem for file edits and transfers. Use `rg` for focused text searches when appropriate.

If MCP fails, stop operations that need its graph evidence and report the failure.
Troubleshoot the connection instead of silently replacing its graph queries with filesystem searches.
An already-resolved hash comparison or approved byte copy can continue when it needs no graph decision.
State why MCP is unnecessary for that operation and which graph checks remain unavailable.

EXACT SEARCH finds the requested note and its counterpart.
Match registered notes by `id`, including notes whose names or folders differ.
Every synced Markdown note must have an ID before transfer.
The ID identifies one logical note, shared by its corresponding copies, with at most one copy per vault.
An ID alone does not make a note synced. Its `sync vaults` property declares intended membership.
Linked binaries are included without note IDs, as described below.
Read IDs and sync fields from note metadata.

When the request lacks an ID or an exact match, search names, aliases, titles, and distinctive text.
Try likely misspellings, abbreviations, first names, initials, and joined or separated name forms.
Use relevant links, backlinks, dates, people, and source URLs to distinguish candidates.
These are clues to identity, not proof that similar notes are interchangeable.
If several candidates fit, explain the best match and ask only for the distinction that remains unclear.
Keep searches focused on the request and expand them when the evidence requires it.

IDENTIFY adds missing sync fields after checking for an existing counterpart.
Reuse an existing ID across corresponding copies.
If neither copy has an ID, assign one shared ID after establishing that they represent the same note.
If different notes have the same ID, report the collision before copying.

Use the local templates as examples of field names, values, and note structure.
See [Frontmatter](references/frontmatter.md) before assigning fields.
Use existing types and propose a new type only when there is a clear gap.
An empty note can be intentional and valuable.

Note names and binary filenames must be unique within each vault.
Check for an existing destination name before placing a file.

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

Use Linux or Git Bash on Windows. The same hash command works on any third copy or older file.
Describe concrete differences and recommend what to keep. Do not dismiss whitespace differences.
When interpreting a mismatch, read [Reviewing differences](references/review.md#reviewing-differences).
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
Keep any proposed annotation separate from clipped source text, using the note's existing structure.

PLACEMENT uses the destination's conventions and the note's type.
Type describes what the note is and provides context for interpreting its contents.
Use the local type guidance and the established folder for that type in the destination.
For example, person notes belong in its people folder, whether named `People`, `Areas/People`, or `Persons`.
Prefer the established convention over a few misplaced examples, while respecting deliberate project folders.
A project folder can group several types around a `project` note and notes with type `project notes`.
For example, an article in the source's `Clippings` folder belongs in the destination's established articles folder.
Do not reproduce the source folder structure automatically.
Use existing folders and confirm a new folder when the request does not already specify it.
Keep existing counterparts in place unless the user requests a move.

Do not sync daily notes themselves.
For requests about a period of work or personal notes, read [Date-range reviews](references/review.md#date-range-reviews).
Start with an itemized list of relevant notes and daily-note entries, including what is missing from the other vault.
For personal-to-work transfers, flag personal material that conflicts with the requested work scope before copying it.
Propose any trimming or separate work version explicitly.

## Linked binaries

Include every linked or embedded local binary, such as PDFs and images, as part of the note's sync request.
Binaries have no note IDs or version metadata. Locate them by unique filename and compare whole-file hashes.
When handling binaries, read [Linked binaries](references/file-operations.md#linked-binaries).

## Move, rename, and delete

Move or rename existing files within a vault only when requested.
Before a requested move, rename, or removal, read [Moves and removals](references/file-operations.md#moves-and-removals).

## When to pause

Pause the affected changes when a required precondition fails or evidence leaves a consequential decision unresolved:

- Conflicting IDs, duplicate names, or a link whose intended target is unclear.
- Competing edits, a substantial unexplained rewrite, or a binary conflict without a clear authorized choice.
- Copies list different vaults in `sync vaults`, with no clear intended result, or a removal risks losing the only copy.
- A missing required file, failed graph query, failed copy, or failed final hash comparison.
- Files that changed since review, or a wider scope than the user approved.

Show the evidence, recommend a resolution, and identify what is needed to continue.
A hash mismatch by itself starts comparison. It does not automatically require a decision from the user.
Continue independent requested work when its preconditions still hold.

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
Surface MCP failures, inconsistent folder maps, tooling problems, and other vault issues encountered during the task.
State their effect on this request without starting an unrelated vault-wide repair.

When asked for handoff information, use the [Handoff format](references/review.md#handoff-information).

For a membership report, compare declared `sync vaults` with actual placements by ID.
The existing Base example and small reporting scripts are optional aids described in [README.md](README.md).
