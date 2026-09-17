#!/usr/bin/env python3
"""
Scan two Obsidian vaults for "managed" notes (frontmatter has id +
sync vaults including both vault names) and write a CSV of
id,filename,sha256(file) for each vault.

Usage (uses config/vaults.yaml, falls back to config-sample):
    python3 sync_hash_vaults.py [vault_a_key] [vault_b_key] [date_prefix]

Usage (explicit, ignores config):
    python3 sync_hash_vaults.py --explicit <vault_a_path> <vault_a_name> <vault_b_path> <vault_b_name> <output_dir> <date_prefix>

Writes:
    <output_dir>/<date_prefix>-<vault_a_name>-hash.csv
    <output_dir>/<date_prefix>-<vault_b_name>-hash.csv

Notes:
- A note counts as "managed" only if it has both an `id:` field and a
  `sync vaults:` field whose value contains BOTH vault names.
- Hash is computed on the whole file, raw bytes, no normalization. This is
  the exact same hash you get by running, on the file itself, in any
  location - a different machine, an old copy, a different branch, anything
  outside this script:
    sha256sum <file> ## linux and windows (with git bash for windows)
"""
import re
import os
import sys
import hashlib
import csv
import datetime

import config_loader


def scan(root, name_a, name_b):
    rows = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith('.git')]
        for f in files:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dirpath, f)
            try:
                raw = open(p, 'rb').read()
                text = raw.decode('utf-8')
            except Exception:
                continue
            m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.S)
            if not m:
                continue
            fm = m.group(1)
            idm = re.search(r'^id:\s*(\S+)', fm, re.M)
            syncm = re.search(r'^sync vaults:\s*(.+)$', fm, re.M)
            if not idm or not syncm:
                continue
            vaults = syncm.group(1)
            if name_a not in vaults or name_b not in vaults:
                continue
            note_id = idm.group(1)
            h = hashlib.sha256(raw).hexdigest()
            rows.append((note_id, os.path.relpath(p, root), h))
    return rows


def main():
    if sys.argv[1:2] == ['--explicit']:
        if len(sys.argv) != 8:
            print(__doc__)
            sys.exit(1)
        vault_a_path, vault_a_name, vault_b_path, vault_b_name, out_dir, date_prefix = sys.argv[2:8]
    else:
        cfg = config_loader.load()
        default_pair = cfg.get('default_pair', {})
        key_a = sys.argv[1] if len(sys.argv) > 1 else default_pair.get('a')
        key_b = sys.argv[2] if len(sys.argv) > 2 else default_pair.get('b')
        date_prefix = sys.argv[3] if len(sys.argv) > 3 else datetime.date.today().isoformat()
        if not key_a or not key_b:
            print(__doc__)
            sys.exit(1)
        vault_a_path, vault_a_name = config_loader.vault_path(cfg, key_a), key_a
        vault_b_path, vault_b_name = config_loader.vault_path(cfg, key_b), key_b
        out_dir = cfg.get('output_dir', '.')
        print(f"config: {cfg['_source']}")

    rows_a = scan(vault_a_path, vault_a_name, vault_b_name)
    rows_b = scan(vault_b_path, vault_a_name, vault_b_name)

    path_a = os.path.join(out_dir, f"{date_prefix}-{vault_a_name}-hash.csv")
    path_b = os.path.join(out_dir, f"{date_prefix}-{vault_b_name}-hash.csv")

    for path, rows in ((path_a, rows_a), (path_b, rows_b)):
        with open(path, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['id', 'filename', 'hash'])
            w.writerows(sorted(rows))

    print(f"{vault_a_name}: {len(rows_a)} managed notes -> {path_a}")
    print(f"{vault_b_name}: {len(rows_b)} managed notes -> {path_b}")


if __name__ == '__main__':
    main()
