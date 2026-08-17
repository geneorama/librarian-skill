# Vault registry pattern

The skill is generic; every installation supplies its own registry. **The live
registry is a note the owner maintains in their vaults** — recommended: a managed
note in the agent vault (e.g. `registry-vaults`), synced by these same workflows
so every machine sees the current version. Read it before touching files.

**No registry note exists yet?** Stop before any file action. Look first —
configured MCP connections already name every reachable vault, and often
whether each is writable — propose a starting table built from that (see
template below), owner confirms/edits, then save it as the registry note.
Don't ask the owner to type the vault list from scratch when you can already
see it.

## Example vault set

A typical installation has three kinds of vaults:

| Vault (example) | Kind | Role | Access rules |
|---|---|---|---|
| `personal` | Personal master | The large, long-lived vault (often thousands of notes) where most notes originate. Some people run two masters — say, `college` and `work` — the pattern is the same. Default `home vault` for its notes. | Read + place only. Never bulk operations. The personal→shared judgment boundary (SKILL.md) applies to anything leaving it. |
| `work`, `newsletter`, … | Project / shared | Scoped vaults for a job, project, or publication. Often synced between machines by Obsidian Sync — placing a note here is what makes it appear on the other machine. | Read/write per ground rules. |
| `agents` | Agent vault | Shared agent state: the vault registry, taxonomy note, sync log, issues note. Agents read it; the owner curates it. | Read/write per ground rules. |

`sync vaults: <none>` in a note means managed but deliberately unsynced.

## Machine registry (template)

The registry note records, per machine:

| Machine | OS / agent runtime | Vault roots | Local skimmer |
|---|---|---|---|
| `<hostname>` | e.g. Windows + Claude Code | `<path>` per vault present here | command to invoke it, or "none" |

Rules that follow from the table:

- A vault not listed for the current machine is **unreachable**: place nothing,
  improvise no path, note it in the report.
- A vault or machine missing from the registry entirely is itself an issue to
  file.

## Local skimmer

If the installation has a local model or script for confidential skimming (see
SKILL.md, "The confidentiality boundary"), the registry note records how to
invoke it — for example an `ollama run <model>` one-liner or a local script that
takes a file path and returns a verdict. No entry = not configured = don't read
candidate-sensitive files.

## Transport (who moves what)

- **Obsidian Sync** (or the owner's chosen sync service) moves shared vaults
  between machines. The librarian never does machine-to-machine transport — it
  only places files into local vault folders and lets the sync service carry
  them.
- **Git** is version control for this skill and for code — never a note
  transport.
