# librarian-skill

A skill that turns an AI agent into a **vault librarian** for multi-vault
Obsidian systems: it identifies notes (stable ids in frontmatter), places copies
where their metadata says they belong, notices conflicts and duplicates, and
escalates problems to the owner — who remains the sync engine and final
authority.

This skill folder belongs **outside of every vault**. The instructions are
version-controlled code, not notes — isolated and identical for every agent
that loads them. Download it, replace the example configuration with your
own.

## Layout

```
librarian-skill/
├── SKILL.md                    # role, ground rules, workflows
└── references/
    ├── vaults.md               # vault registry pattern + example vault set
    ├── frontmatter.md          # the sync frontmatter format
    ├── taxonomy.md             # example type taxonomy (adapt per installation)
    ├── logging.md              # sync log + issues note formats
    └── case-archive.md         # the incidents behind the rules
```

## Install

- **Claude Code:** place (or junction/symlink) this folder at
  `<project>/.claude/skills/librarian/` or `~/.claude/skills/librarian/`.
- **Other agent runtimes:** copy the folder into the runtime's skills directory.

The skill carries no state and no dependencies. Installation-specific data (your
vaults, machines, paths, taxonomy, local-skimmer command) lives in a registry
note in *your* vaults — see `references/vaults.md` for the pattern.

## Change policy

Edit → commit, one commit per policy change, so the git history reads as a
decision log.
