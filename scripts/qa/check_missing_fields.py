#!/usr/bin/env python3
import csv, sys
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: check_missing_fields.py <csv>")
    raise SystemExit(1)

required = ["journal_name", "publisher", "subject_area"]
missing = Counter()
rows = 0
with open(sys.argv[1]) as f:
    r = csv.DictReader(f)
    for row in r:
        rows += 1
        for k in required:
            if not (row.get(k) or "").strip():
                missing[k] += 1

print(f"Rows: {rows}")
for k in required:
    print(f"Missing {k}: {missing[k]}")
