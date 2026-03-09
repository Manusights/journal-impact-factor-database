#!/usr/bin/env python3
import csv, re, sys
from pathlib import Path

if len(sys.argv) != 3:
    print("Usage: normalize_issn.py <input.csv> <output.csv>")
    raise SystemExit(1)

inp, out = Path(sys.argv[1]), Path(sys.argv[2])

pat = re.compile(r'[^0-9Xx]')

def norm(v):
    s = pat.sub('', v or '')
    if len(s) == 8:
        return s[:4] + '-' + s[4:]
    return v or ''

with inp.open() as fi, out.open('w', newline='') as fo:
    r = csv.DictReader(fi)
    w = csv.DictWriter(fo, fieldnames=r.fieldnames)
    w.writeheader()
    for row in r:
        if 'issn' in row:
            row['issn'] = norm(row['issn'])
        w.writerow(row)
print(f"Wrote {out}")
