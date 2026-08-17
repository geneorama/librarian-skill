#!/usr/bin/env python3
"""
inin.py - set comparison between two Obsidian vaults, matched by frontmatter id.

Answers: which notes labeled to sync to a vault are not actually there?
Implements SKILL.md's "Check" workflow.

Usage (uses config/vaults.yaml, falls back to config-sample):
    inin.py SOURCE_KEY TARGET_KEY

Usage (explicit, ignores config):
    inin.py --explicit SOURCE_VAULT_PATH TARGET_VAULT_PATH TARGET_LABEL

TARGET_LABEL is the name as it appears in the `sync vaults` property
(case-insensitive substring match). In config mode this is just TARGET_KEY.

Read only. Never writes to a vault.

Output classes:
    MISSING    labeled for target, no id match and no filename match in target
    NAME-ONLY  filename exists in target but id does not match (usually the
               target copy is just missing its id - a labeling job, not a copy)
    BAD-ID     id present but not 12 hex characters
"""

import os
import re
import sys

import config_loader

SKIP_DIRS = {".git", ".obsidian", ".trash", ".smart-env"}
ID_RE = re.compile(r"^[0-9a-f]{12}$")


def frontmatter(path):
    """Return the frontmatter of a note as a dict of top-level scalar keys."""
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read(4000)
    except (OSError, UnicodeDecodeError):
        return {}
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        match = re.match(r"^([A-Za-z][A-Za-z ]*):\s*(.*)$", line)
        if match:
            out[match.group(1).strip()] = match.group(2).strip().strip("\"'")
    return out


def scan(root):
    """Map every .md path in a vault to its frontmatter dict."""
    notes = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                path = os.path.join(dirpath, name)
                notes[path] = frontmatter(path)
    return notes


def run(source_root, target_root, label):
    for root in (source_root, target_root):
        if not os.path.isdir(root):
            sys.exit(f"not a directory: {root}")

    source = scan(source_root)
    target = scan(target_root)

    target_ids = {fm["id"] for fm in target.values() if fm.get("id")}
    target_names = {os.path.basename(p)[:-3].lower() for p in target}

    labeled = 0
    rows = []
    for path, fm in source.items():
        if label.lower() not in fm.get("sync vaults", "").lower():
            continue
        labeled += 1
        note_id = fm.get("id")
        name = os.path.basename(path)[:-3]
        if note_id and not ID_RE.match(note_id):
            rows.append(("BAD-ID", note_id, path))
        if note_id and note_id in target_ids:
            continue
        kind = "NAME-ONLY" if name.lower() in target_names else "MISSING"
        rows.append((kind, note_id or "(no id)", path))

    rel = lambda p: os.path.relpath(p, source_root)
    print(f"source:  {source_root}  ({len(source)} notes)")
    print(f"target:  {target_root}  ({len(target)} notes)")
    print(f"labeled to sync to {label}: {labeled}")
    print(f"not matched in target: {sum(1 for r in rows if r[0] != 'BAD-ID')}")
    print()
    for kind, note_id, path in sorted(rows):
        print(f"{kind:10} {note_id:14} {rel(path)}")


def main():
    if sys.argv[1:2] == ['--explicit']:
        if len(sys.argv) != 5:
            sys.exit(__doc__)
        run(sys.argv[2], sys.argv[3], sys.argv[4])
        return

    if len(sys.argv) != 3:
        sys.exit(__doc__)
    source_key, target_key = sys.argv[1], sys.argv[2]
    cfg = config_loader.load()
    print(f"config: {cfg['_source']}")
    run(config_loader.vault_path(cfg, source_key), config_loader.vault_path(cfg, target_key), target_key)


if __name__ == "__main__":
    main()
