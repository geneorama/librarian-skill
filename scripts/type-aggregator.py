#!/usr/bin/env python3
"""
Count notes per (type, folder) pair in a vault, showing where each type
actually lives. Implements references/taxonomy.md's "Building your own
type->folder table" section. Not a live query — re-run and re-paste when
the taxonomy needs a refresh.

Usage (uses config/vaults.yaml, falls back to config-sample):
    python3 type-aggregator.py <vault_key>

Usage (explicit, ignores config):
    python3 type-aggregator.py --explicit <vault_path>
"""
import os
import re
import sys
from collections import Counter

import yaml

import config_loader

FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)


def tabulate(vault):
    counts = Counter()
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fn in files:
            if not fn.endswith('.md'):
                continue
            path = os.path.join(root, fn)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    head = f.read(4000)
            except Exception:
                continue
            m = FM_RE.match(head)
            if not m:
                continue
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except Exception:
                continue
            t = fm.get('type')
            if not t:
                continue
            folder = os.path.relpath(root, vault)
            if folder == '.':
                folder = '(root)'
            counts[(t, folder)] += 1
    return counts


def report(counts):
    rows = sorted(counts.items(), key=lambda kv: (kv[0][0], -kv[1]))
    print(f"{'type':<15} {'folder':<45} {'count':>5}")
    print("-" * 67)
    for (t, folder), c in rows:
        print(f"{t:<15} {folder:<45} {c:>5}")
    print("-" * 67)
    print("total typed files:", sum(counts.values()))


def main():
    if sys.argv[1:2] == ['--explicit']:
        if len(sys.argv) != 3:
            print(__doc__)
            sys.exit(1)
        vault = sys.argv[2]
    else:
        if len(sys.argv) != 2:
            print(__doc__)
            sys.exit(1)
        cfg = config_loader.load()
        print(f"config: {cfg['_source']}")
        vault = config_loader.vault_path(cfg, sys.argv[1])

    report(tabulate(vault))


if __name__ == '__main__':
    main()
