#!/usr/bin/env python3
"""
Compare two hash CSVs produced by sync_hash_vaults.py and report:
  - ids only in A
  - ids only in B
  - ids in both but with different whole-file hashes

Usage:
    python3 sync_diff_report.py <csv_a> <csv_b>

Every mismatch is listed. Use diff -u on the files to inspect the changes.
"""
import csv
import sys


def load(path):
    d = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            if row['id'] in d:
                sys.exit(f"duplicate id {row['id']} in {path}")
            d[row['id']] = row
    return d


def main():
    if len(sys.argv) != 3:
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

    for i in diff:
        print(" ", i, a[i]['filename'], "|", b[i]['filename'])


if __name__ == '__main__':
    main()
