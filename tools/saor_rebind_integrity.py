#!/usr/bin/env python3
"""Regenerate SAOR scientific integrity records from the repository contents.

This tool rewrites:
  * 05_Reproduction_and_Verification/SAOR_Research_Package_Binding_v1_3_0.json
  * 05_Reproduction_and_Verification/SAOR_Computational_Integrity_SHA256_v1_3_0.txt
  * PACKAGE_MANIFEST.txt

Only the declared scientific core is hash-bound. Editable presentation, legal,
configuration, example, survey, and evidence-prose files remain outside the
binding in accordance with the integrity scope policy.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / '05_Reproduction_and_Verification'
BINDING = REC / 'SAOR_Research_Package_Binding_v1_3_0.json'
SHATXT = REC / 'SAOR_Computational_Integrity_SHA256_v1_3_0.txt'
MANIFEST = ROOT / 'PACKAGE_MANIFEST.txt'

BOUND_FILES = [
    '01_Theory/SAOR_Definitions_and_Transfer_Semantics_v1_3_0.md',
    '01_Theory/SAOR_General_Critical_Support_Synthesis_Theorem_v1_3_0.md',
    '01_Theory/SAOR_Anchored_Cone_Corollary_v1_3_0.md',
    '01_Theory/SAOR_Sharp_Support_Sensitive_Classification_v1_3_0.md',
    '01_Theory/SAOR_Principal_Proof_v1_3_0.md',
    '01_Theory/SAOR_Structural_Corollaries_v1_3_0.md',
    '01_Theory/SAOR_Scope_and_Assumption_Boundary_v1_3_0.md',
    '02_Algorithms_and_Software/saor_core.py',
    '02_Algorithms_and_Software/saor_support_necessity.py',
    '03_Verification/Core/saor_core_verification.py',
    '03_Verification/Principal/saor_general_critical_support_synthesis_verifier_v1_3_0.py',
    '03_Verification/Principal/saor_sharp_support_sensitive_classifier_verifier_v1_3_0.py',
    '03_Verification/Principal/saor_anchored_cone_corollary_verifier_v1_3_0.py',
    '03_Verification/Principal/saor_support_necessity_verifier_v1_3_0.py',
    '03_Verification/Definition_Level/saor_direct_transfer_definition_verifier_v1_3_0.py',
    '03_Verification/Definition_Level/saor_definition_level_lib.py',
    '03_Verification/Proof_Audit/saor_cross_proof_consistency_audit_v1_3_0.py',
    '03_Verification/Regression/saor_static_projection_escape_regression.py',
    '03_Verification/Regression/saor_context_masking_oscillation_regression.py',
    '03_Verification/Regression/saor_rank_two_context_regression.py',
    '03_Verification/Regression/saor_affine_compression_corollary_regression.py',
    '03_Verification/Regression/saor_support_sensitive_escape_regression.py',
    '04_Research_Context/SAOR_Claim_Map_v1_3_0.json',
    '04_Research_Context/SAOR_Theorem_Dependency_Map_v1_3_0.json',
    '05_Reproduction_and_Verification/SAOR_Theorem_Record_v1_3_0.json',
    '05_Reproduction_and_Verification/SAOR_Verification_Metrics_v1_3_0.json',
    '05_Reproduction_and_Verification/SAOR_Cross_Version_Regression_Manifest_v1_3_0.json',
    'verify.py',
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


IGNORED_DIR_NAMES={'.git','__pycache__','.venv','venv','.pytest_cache','.idea','build','dist','.mypy_cache','.ruff_cache'}
IGNORED_FILE_NAMES={'.DS_Store','Thumbs.db'}

def ignored_inventory_path(p):
    rel=p.relative_to(ROOT)
    if p.name in IGNORED_FILE_NAMES:
        return True
    return any(part in IGNORED_DIR_NAMES or part.endswith('.egg-info') for part in rel.parts)

def inventory():
    return sorted(
        str(p.relative_to(ROOT)).replace('\\', '/')
        for p in ROOT.rglob('*')
        if p.is_file() and not ignored_inventory_path(p)
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()

    missing = [rel for rel in BOUND_FILES if not (ROOT / rel).exists()]
    if missing:
        raise SystemExit(f'missing bound files: {missing}')

    old = json.loads(BINDING.read_text(encoding='utf-8')) if BINDING.exists() else {}
    new_files = {rel: sha(ROOT / rel) for rel in BOUND_FILES}
    old_files = old.get('files', {})
    changed = [rel for rel in BOUND_FILES if old_files.get(rel) != new_files[rel]]

    print(f'bound files: {len(BOUND_FILES)}  changed or new: {len(changed)}')
    for rel in changed:
        print(f'  {rel}')

    if args.check:
        return

    record = {
        'project': 'Shunyaya Arithmetic Origin Resolution',
        'version': '1.3.0',
        'hash': 'SHA-256',
        'presentation_layer_bound': False,
        'files': new_files,
    }
    BINDING.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    SHATXT.write_text(''.join(f'{h}  {rel}\n' for rel, h in new_files.items()), encoding='utf-8')

    files = inventory()
    MANIFEST.write_text(
        'Shunyaya Arithmetic Origin Resolution v1.3.0\n'
        'Package manifest\n'
        f'Files: {len(files)}\n\n' + '\n'.join(files) + '\n',
        encoding='utf-8',
    )
    print(f'wrote {BINDING.name}, {SHATXT.name}, PACKAGE_MANIFEST.txt ({len(files)} files)')


if __name__ == '__main__':
    main()
