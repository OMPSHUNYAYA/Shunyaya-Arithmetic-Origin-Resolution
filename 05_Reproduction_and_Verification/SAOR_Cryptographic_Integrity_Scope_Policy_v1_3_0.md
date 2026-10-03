# SAOR Cryptographic Integrity Scope Policy v1.3.0

SHA-256 binding is restricted to the scientific identity of SAOR: theorem/semantics/proof files, reference implementation, principal and definition-level verifiers, proof-consistency and regression programs, and selected machine-readable claim/theorem/dependency records.

The following editable or presentation-oriented surfaces are intentionally excluded from cryptographic binding:

- `README.md`;
- `LICENSE` and `LICENSES/`;
- `CITATION.cff`;
- notices and copyright text;
- `VERSION`;
- workflows and repository configuration;
- `pyproject.toml`;
- `PACKAGE_MANIFEST.txt`;
- examples;
- survey prose and survey data;
- verification guides, evidence prose, package logs, and repository-positioning prose.

This separation allows navigation, presentation, legal text, repository metadata, survey evidence, and explanatory material to evolve without changing the bound theorem identity.

The package-inventory check is intentionally tolerant of normal working-directory additions. VCS metadata, operating-system metadata, virtual environments, package-install metadata, IDE/cache directories, and build directories are ignored. Other unlisted substantive files generate a warning rather than an integrity failure. Missing declared package files and SHA-256 mismatches in the bound scientific core remain verification failures.
