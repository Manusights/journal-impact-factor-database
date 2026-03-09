# Data Quality for Journal Tables

Journal tables become unreliable quickly when metadata hygiene is weak. This guide gives a minimal quality framework that keeps your dataset useful over time.

## Core quality risks
1. Duplicate journals due to naming variants
2. Inconsistent ISSN formatting
3. Quartile values outside expected set
4. Missing required fields
5. Outdated submission URLs

## Required quality rules
At minimum, each row should include:
- journal_name
- publisher
- subject_area

Recommended fields:
- issn
- quartile
- impact_factor
- submission_url

## Validation pipeline

### 1) Structural validation
Run schema checks against required columns and value types.

### 2) Format normalization
Normalize ISSN and URL formats before analytical use.

### 3) Duplicate review
Use a soft key (`journal_name + publisher`) and manually review collisions.

### 4) Missingness reporting
Run `scripts/qa/check_missing_fields.py` and log coverage trends monthly.

## Governance model
Create one owner for each dataset update cycle.

- Weekly: fix obvious link and format issues
- Monthly: run full missingness and duplicate audit
- Quarterly: review field definitions and taxonomy drift

## Practical quality threshold
Treat a dataset as ready for decision use only when:
- required-field completeness is above 98%
- duplicate collision review is current
- submission links are recently validated

## Related files
- docs/qa/data_quality_rules.md
- scripts/qa/check_missing_fields.py
- scripts/normalize_issn.py
- faq/common_data_errors_in_journal_tables.md
