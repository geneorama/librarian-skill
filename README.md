# Librarian

An agent skill for keeping Obsidian notes in sync by ID, with whole-file SHA-256 confirmation.
The agent finds counterparts, explains differences, and carries out requested copies, updates, and approved merges.

Start with [SKILL.md](SKILL.md).

## Keep the workflow editable

Keep your live workflow and templates in the vault where you edit them.
Keep machine paths and vault roles in an accessible local file, such as a note beside your vaults.
The [local setup example](config-sample/librarian.local.md) also works with vaults on different drives.

Put a pointer in the startup instructions that your agent actually reads.
The pointer names the local setup, live workflow, and this checkout's `SKILL.md`.
Do not paste another copy of the workflow into each startup file.
A startup file named `SKILLS.md` only works if your agent is instructed to read it.

The live workflow supplies installation-specific decisions. This repository supplies the general skill.
When a workflow change applies generally, ask the agent to make the corresponding repository edit and show the diff.
An instruction can require that reread at each session without a background service.

## Use and install

During development, an explicit startup pointer to this visible checkout is sufficient.
You can edit and version the skill here without maintaining an installed copy.

For automatic discovery, Codex supports skill directories and symlinked skill folders under `$HOME/.agents/skills`.
It detects skill changes automatically. Restart it if an update does not appear.
See [the official skill documentation](https://learn.chatgpt.com/docs/build-skills).

For Linux, a symlink keeps the discovered skill attached to the visible checkout:

```bash
# Changes local skill discovery: create a link to your existing checkout.
# Replace the checkout path. The librarian destination must not already exist.
mkdir -p "$HOME/.agents/skills"
ln -sT '/absolute/path/to/librarian-skill' "$HOME/.agents/skills/librarian"
```

On Windows, use Git Bash for sync commands.
An explicit startup pointer avoids needing a filesystem link for development.
For other agents, use their skill discovery location or the same explicit startup pointer.
Keep personal paths and vault names out of the installed skill files.

## Updates

A skill file does not run itself on a schedule.
A daily or weekly agent task can check a repository for updates when that runtime supports scheduled work.
An example task is: “Check this checkout for upstream changes weekly and summarize changes to the sync instructions.”
Decide separately whether that task can apply updates to a clean checkout.
Local project tasks need access to the checkout at run time.
See [scheduled task documentation](https://learn.chatgpt.com/docs/automations?surface=app).

For development on one machine, the visible checkout plus a startup pointer avoids an installation refresh step.
On another machine, update the checkout and let the startup pointer read its current files.
No scheduler is required for ordinary sync requests.

## Graph queries

The skill uses MCP for backlinks and other graph evidence, with filesystem operations for edits and byte-preserving copies.
MCP supplies an interface. Graph awareness depends on the queries and how the agent interprets their results.
For example, CyanHeads documents search-based backlink queries rather than a dedicated backlink tool.
It also offers structured metadata search and optional outgoing links, useful for note discovery and comparison.
See [the server documentation](https://github.com/cyanheads/obsidian-mcp-server#tools).

Obsidian distinguishes linked mentions from unlinked mentions of a name.
Confirm the actual link target before treating a search result as a backlink.
See [Obsidian's backlink documentation](https://help.obsidian.md/plugins/backlinks).

If the required MCP query fails or cannot supply the needed evidence, pause the dependent operation and report the gap.
An already-resolved file comparison does not need a graph query.

## Existing optional helpers

Single-note work uses filesystem commands and the local Obsidian templates.
The existing Python scripts provide reports when a larger review is requested.
They need Python and PyYAML. They do not implement a sync service.

| File | Purpose |
|---|---|
| `scripts/sync_hash_vaults.py` | Write complete-file hash CSVs for notes declaring both vaults |
| `scripts/sync_diff_report.py` | List IDs present on one side and every differing hash |
| `scripts/inin.py` | Find declared counterparts missing by ID, with filename clues |
| `scripts/type-aggregator.py` | Summarize existing types and folders |
| `references/example-base.md` | Show an editable Obsidian Base for finding managed-note candidates |

Scripts can use explicit paths or `config/vaults.yaml`, with `config-sample/vaults.yaml` as an example.
For the existing configuration format, vault keys must match the names in note metadata.
The script docstrings describe their arguments.
Review membership candidates before copying. A report entry does not authorize a change.

See [MAINTENANCE.md](MAINTENANCE.md) for review, commit, and history-replacement commands.
