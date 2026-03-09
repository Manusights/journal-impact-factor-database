#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path

if len(sys.argv) != 3:
    print("Usage: csv_to_json.py <input.csv> <output.json>")
    raise SystemExit(1)

inp, out = Path(sys.argv[1]), Path(sys.argv[2])
with inp.open() as f:
    rows = list(csv.DictReader(f))
out.write_text(json.dumps(rows, indent=2))
print(f"Wrote {out}")
