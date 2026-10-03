# SAOR Verification Guide v1.3.0

From the repository root:

```text
python -B verify.py --self-test
```

runs the compact verification suite.

```text
python -B verify.py --verify
```

runs the complete deterministic suite. Definition-level checks cover transfer semantics, sharp formulas, constructive separators, anchored-cone cases, and support-necessity certificates. Exact execution counts are recorded in the package verification log and metrics file.

No third-party Python packages are required.

The root verifier also checks the scientific-core SHA-256 binding, declared package inventory, UTF-8/LF normalization, and local Markdown links. Common environment clutter such as `.git/`, `.DS_Store`, `*.egg-info`, virtual environments, IDE/cache directories, and build directories is ignored. Unexpected substantive files produce an integrity warning rather than invalidating an otherwise unchanged package; missing declared files and bound-file hash mismatches still fail verification.

After editing any bound file, regenerate the integrity records:

```text
python -B tools/saor_rebind_integrity.py
```
