#!/usr/bin/env bash
set -euo pipefail
FILE="${1:-examples/sample_journal_metadata.csv}"
head -n1 "$FILE" | grep -q "journal_name,issn,publisher,subject_area,quartile,impact_factor,submission_url,publisher_url"
echo "Headers look good: $FILE"
