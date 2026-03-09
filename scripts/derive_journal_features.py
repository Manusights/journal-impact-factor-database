#!/usr/bin/env python3
"""
Derive non-proprietary helper features from journal metadata CSV.
Input columns expected:
  journal_name,publisher,subject_area,quartile,impact_factor
Output adds:
  impact_band,top_quartile_flag
"""
import csv
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("Usage: derive_journal_features.py <input.csv> <output.csv>")
    sys.exit(1)

inp, out = Path(sys.argv[1]), Path(sys.argv[2])


def impact_band(v):
    try:
        x = float(v)
    except Exception:
        return "unknown"
    if x >= 20:
        return "very_high"
    if x >= 10:
        return "high"
    if x >= 5:
        return "mid"
    if x > 0:
        return "emerging"
    return "unknown"

with inp.open() as fi, out.open("w", newline="") as fo:
    r = csv.DictReader(fi)
    fields = r.fieldnames + ["impact_band", "top_quartile_flag"]
    w = csv.DictWriter(fo, fieldnames=fields)
    w.writeheader()
    for row in r:
        row["impact_band"] = impact_band(row.get("impact_factor", ""))
        row["top_quartile_flag"] = "1" if row.get("quartile", "") == "Q1" else "0"
        w.writerow(row)

print(f"Wrote {out}")
