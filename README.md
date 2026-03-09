# Journal Impact Factor Database (Research Utility)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE) [![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)](.) [![Website](https://img.shields.io/badge/Manusights-manusights.com-blue.svg)](https://manusights.com)

This repository provides structured journal metadata for research workflows around journal selection, bibliometrics, and manuscript planning.

## What is included

- `data/fields_of_science.csv`: normalized subject area taxonomy
- `schemas/journal_metadata.schema.json`: JSON schema for journal metadata
- `examples/sample_journal_metadata.csv`: example format for downstream tooling
- `scripts/`: helper scripts for validation and transformation

## Important licensing note

JCR is a licensed product. This repository does **not** redistribute proprietary Clarivate raw exports.

If you have licensed access, you can map your internal JCR data into this public schema for your own use.

## Use cases

- Journal ranking tools
- Internal publication strategy dashboards
- Bibliometric analysis pipelines
- Submission planning utilities

## About Manusights

Manusights helps researchers improve manuscripts before submission using expert peer review.

- Website: https://manusights.com
- Journal guides: https://manusights.com/journal-guides
- Peer review resources: https://manusights.com/resources


## Reproducible outputs

- License and usage guidance: `docs/DATA_LICENSE_AND_USAGE.md`
- Citation metadata: `docs/CITATION.cff`
- Feature engineering helper: `scripts/derive_journal_features.py`

## Cite this resource

If this repository helps your work, cite:

> Manusights. Journal Impact Factor Database (Research Utility). GitHub repository. https://github.com/Manusights/journal-impact-factor-database


## Maintenance

This repository is actively maintained. Content refreshes are planned monthly.

## Contributing

Suggestions are welcome through GitHub Issues and Pull Requests.


## Accuracy boundaries

For official impact factor values, always use licensed primary data from your institution.
This repository is a public utility layer for structure, workflows, and reproducible transformations.


## Related Manusights Resources
- https://github.com/Manusights/journal-impact-factor-database
- https://github.com/Manusights/scientific-peer-review-checklist
- https://github.com/Manusights/journal-submission-guides
- https://github.com/Manusights/ai-generated-manuscript-detection
- https://github.com/Manusights/scientific-writing-resources
- https://github.com/Manusights/awesome-scientific-publishing


## FAQ
- `faq/how_to_choose_between_q1_journals.md`
- `faq/what_to_do_when_impact_factor_is_missing.md`
- `faq/how_to_use_impact_bands_without_overfitting.md`
- `faq/how_to_validate_submission_urls.md`
- `faq/how_to_handle_journal_name_variants.md`
- `faq/how_to_build_a_journal_tracker_sheet.md`
- `faq/how_to_compare_publishers_fairly.md`
- `faq/common_data_errors_in_journal_tables.md`
