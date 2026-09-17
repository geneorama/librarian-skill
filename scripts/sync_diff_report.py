#!/usr/bin/env python3
"""
Compare two hash CSVs produced by sync_hash_vaults.py and report:
  - ids only in A
  - ids only in B
  - ids in both but with different hash (real or noise diffs)

Usage:
    python3 sync_diff_report.py <csv_a> <csv_b>

Optional third arg "noisecheck" re-reads the actual files (given a vault
root pair) and filters out diffs that are only whitespace / non-breaking
space (nbsp) / trailing-blank-line noise, common from Word-pasted content.
This mode needs the vault roots too:

    python3 sync_diff_report.py <csv_a> <csv_b> noisecheck <vault_a_root> <vault_b_root>
"""
import csv
import sys
import re
import os


def load(path):
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            d[row['id']] = row
    return d


def normalize(body):
    body = body.replace(' ', ' ')
    lines = [re.sub(r'[ \t]+$', '', line) for line in body.split('\n')]
    while lines and lines[-1] == '':
        lines.pop()
    return '\n'.join(lines)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    a = load(sys.argv[1])
    b = load(sys.argv[2])
    ids_a, ids_b = set(a), set(b)
    only_a = sorted(ids_a - ids_b)
    only_b = sorted(ids_b - ids_a)
    both = ids_a & ids_b
    diff = sorted(i for i in both if a[i]['hash'] != b[i]['hash'])

    print(f"only in A ({len(only_a)}):")
    for i in only_a:
        print(" ", i, a[i]['filename'])
    print(f"\nonly in B ({len(only_b)}):")
    for i in only_b:
        print(" ", i, b[i]['filename'])
    print(f"\nsame id, different hash ({len(diff)}):")

    if len(sys.argv) == 6 and sys.argv[3] == 'noisecheck':
        root_a, root_b = sys.argv[4], sys.argv[5]
        real, noise = [], []
        for i in diff:
            pa = os.path.join(root_a, a[i]['filename'])
            pb = os.path.join(root_b, b[i]['filename'])
            ta = open(pa, encoding='utf-8').read()
            tb = open(pb, encoding='utf-8').read()
            (noise if normalize(ta) == normalize(tb) else real).append(i)
        print(f"  noise-only (whitespace/nbsp): {len(noise)}")
        print(f"  real diffs: {len(real)}")
        for i in real:
            print(" ", i, a[i]['filename'], "|", b[i]['filename'])
    else:
        for i in diff:
            print(" ", i, a[i]['filename'], "|", b[i]['filename'])


if __name__ == '__main__':
    main()
