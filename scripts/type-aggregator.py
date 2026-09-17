import argparse
import os, re, yaml
from collections import Counter

## Example use
## python3 type-aggregator.py --vault /path/to/vault
## python3 type-aggregator.py --vault /path/to/vault --fixed

fm_re = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vault', required=True, help='Path to vault root')
    parser.add_argument('--fixed', action='store_true', help='Use fixed-width text output')
    args = parser.parse_args()

    vault = args.vault
    if not os.path.isdir(vault):
        parser.error(f'vault directory not found: {vault}')

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
            m = fm_re.match(head)
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

    rows = sorted(counts.items(), key=lambda kv: (kv[0][0], -kv[1]))
    if args.fixed:
        print(f"{'type':<15} {'folder':<45} {'count':>5}")
        print("-" * 67)
        for (t, folder), c in rows:
            print(f"{t:<15} {folder:<45} {c:>5}")
        print("-" * 67)
        print("total typed files:", sum(counts.values()))
        return

    print("| type | folder | count |")
    print("|---|---|---:|")
    for (t, folder), c in rows:
        print(f"| {t} | {folder} | {c} |")

    print()
    print(f"**Total typed files:** {sum(counts.values())}")


if __name__ == '__main__':
    main()
