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
