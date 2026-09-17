There are three levels of comparison: 

1. hash - This tells us if the file is exactly the same
2. diff - A mechanical diff tells us what lines changed specifically
3. read - Intelligently interpreting the note contents provides semantic understanding

Check the hash on the whole file. I need the command line hash equivalent that I can run (without python) to confirm the hash. I need to be able to run the same command in a third location to check that version. I might be testing something outside of Obsidian sync, on a different branch, an old copy, or something else.

In the diff step I expect: Report what's different based on a simple, mechanical diff. 

Examples of differences: 
- Whitespace / newlines
- Invisible non-printed characters (non-breaking spaces, Unicode, etc.)
- Many lines of content
- Renamed note / links in one vault causing a conflict with the links. 
- Differences in a table / formatting (e.g. pipe characters, or image tags)

Those are worth enumerating because the details matter:
- Some differences are obviously more or less important, but even changes in whitespace should not spontaneously happen. 
- If a note is renamed in one vault through the app, then the links automatically update throughout the vault. This can create an unresolved name difference that will need to be resolved, or ignored depending on the situation. 
- About large insertions: It matters if it's original content, text copied from a website, or text generated from AI. They have different but unpredictable levels of authority and expendability depending on context. 

---

#### Claude's summary of the sync note 
 Core idea: Keep two Obsidian vaults (D75, coc-work, geneorama-agents) in sync while working across them. Currently in a pilot phase; interactive/manual only, no automated batch triggers yet.
##### Key concept: id is the sync primary key
- Notes synced across vaults MUST have a unique id
- Notes not synced don't need one
- Never invent a new id when syncing an existing note
##### Workflows
- Identify note: match unsynced notes by graph context, filename, or keywords
- Sync: move/copy notes between vaults (see [[Sync workflow UML - Add note to target (high level)]])
- Check content: diff/hash comparison, ask before resolving differences
##### Guardrails
- Confirm source/destination vault direction before acting, do not rely on pwd
- Confirm operations affecting >10 files
- Never sync daily notes
- Don't invent frontmatter types silently, flag gaps
- Preserve file dates where possible
- Renaming with mv breaks links; moving (unique filename) is fine
- Empty \[\[links]] are usually intentional placeholders, not bugs

Actions defined: EXACT SEARCH, IDENTIFY (LABEL), COPY, UPDATE/REPLACE, DELETE (→ +sync/DELETE for manual deletion), MOVE, PLACEMENT, RECONCILE (SHA-256 hash comparison), REPORT.

Tooling:
- `sync_hash_vaults.py <vault_a> <vault_b>` → per-vault id/filename/hash CSV
- `sync_diff_report.py <csv_a> <csv_b>` → only-in-A / only-in-B / same-id-different-hash, with a noisecheck mode for whitespace/nbsp noise
- `inin.py` → set-membership report
- Hashes cover note body only (frontmatter stripped) — noted as a known gap ("need to fix to match all note, like if I change order")

Metadata fields: id, created, home vault, sync vaults, type — all documented with rules (e.g., type needs judicious curation, never
silently invented).
