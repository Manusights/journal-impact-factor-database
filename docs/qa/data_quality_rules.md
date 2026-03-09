# Data Quality Rules

## Required fields
- journal_name
- publisher
- subject_area

## Recommended fields
- issn
- quartile
- impact_factor
- submission_url

## Validation checks
- ISSN format is ####-#### when present
- Quartile in {Q1,Q2,Q3,Q4,NA}
- impact_factor is numeric or null
- URLs start with https://

## Duplicate handling
Treat journal_name + publisher as a soft unique key and review collisions manually.
