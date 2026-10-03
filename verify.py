#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,re,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
VERSION='1.3.0'
BINDING=ROOT/'05_Reproduction_and_Verification/SAOR_Research_Package_Binding_v1_3_0.json'
REQUIRED=[
 'README.md','VERSION','LICENSE','CITATION.cff','verify.py',
 '01_Theory/SAOR_Definitions_and_Transfer_Semantics_v1_3_0.md',
 '01_Theory/SAOR_General_Critical_Support_Synthesis_Theorem_v1_3_0.md',
 '01_Theory/SAOR_Sharp_Support_Sensitive_Classification_v1_3_0.md',
 '01_Theory/SAOR_Principal_Proof_v1_3_0.md',
 '01_Theory/SAOR_Structural_Corollaries_v1_3_0.md',
 '01_Theory/SAOR_Anchored_Cone_Corollary_v1_3_0.md',
 '02_Algorithms_and_Software/saor_core.py',
 '02_Algorithms_and_Software/saor_support_necessity.py',
 '03_Verification/Principal/saor_general_critical_support_synthesis_verifier_v1_3_0.py',
 '03_Verification/Principal/saor_sharp_support_sensitive_classifier_verifier_v1_3_0.py',
 '03_Verification/Definition_Level/saor_direct_transfer_definition_verifier_v1_3_0.py',
 '03_Verification/Definition_Level/saor_definition_level_lib.py',
 '03_Verification/Principal/saor_anchored_cone_corollary_verifier_v1_3_0.py',
 '03_Verification/Principal/saor_support_necessity_verifier_v1_3_0.py',
 '03_Verification/Proof_Audit/saor_cross_proof_consistency_audit_v1_3_0.py',
 '04_Research_Context/SAOR_Claim_Map_v1_3_0.json',
 '05_Reproduction_and_Verification/SAOR_Theorem_Record_v1_3_0.json',
 '05_Reproduction_and_Verification/SAOR_Research_Package_Binding_v1_3_0.json'
]
EDITABLE={'README.md','LICENSE','CITATION.cff','NOTICE','COPYRIGHT_NOTICE.txt','THIRD_PARTY_NOTICES.txt','PACKAGE_MANIFEST.txt','VERSION','pyproject.toml','.gitignore','.gitattributes','.github/workflows/verify.yml'}

IGNORED_DIR_NAMES={'.git','__pycache__','.venv','venv','.pytest_cache','.idea','build','dist','.mypy_cache','.ruff_cache'}
IGNORED_FILE_NAMES={'.DS_Store','Thumbs.db'}

def ignored_inventory_path(p):
    rel=p.relative_to(ROOT)
    if p.name in IGNORED_FILE_NAMES:
        return True
    return any(part in IGNORED_DIR_NAMES or part.endswith('.egg-info') for part in rel.parts)

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(rel,flag=None):
    path=ROOT/rel
    old_argv=sys.argv[:]
    try:
        sys.argv=[str(path)]+([flag] if flag else [])
        runpy.run_path(str(path),run_name='__main__')
    finally:
        sys.argv=old_argv

def local_links(rel):
    text=(ROOT/rel).read_text(encoding='utf-8'); links=re.findall(r'\]\(((?:\.?\.?/)[^)#]+)',text); bad=[]
    for link in links:
        target=((ROOT/rel).parent/link).resolve()
        try: target.relative_to(ROOT.resolve())
        except ValueError: bad.append(link); continue
        if not target.exists(): bad.append(link)
    return links,bad

def integrity():
    failures=[]; checks=0
    for rel in REQUIRED:
        checks+=1
        if not (ROOT/rel).exists(): failures.append(f'missing:{rel}')
    if (ROOT/'VERSION').read_text(encoding='utf-8').strip()!=VERSION: failures.append('version_mismatch')
    checks+=1
    data=json.loads(BINDING.read_text(encoding='utf-8')); checks+=1
    if data.get('version')!=VERSION: failures.append('binding_version')
    if data.get('presentation_layer_bound') is not False: failures.append('presentation_layer_bound')
    bound=data.get('files',{}); checks+=1
    for rel in bound:
        if rel in EDITABLE or rel.startswith('LICENSES/') or rel.startswith('06_Examples/'):
            failures.append(f'editable_file_bound:{rel}')
        checks+=1
    for rel,expected in bound.items():
        p=ROOT/rel; actual=digest(p) if p.exists() else 'MISSING'
        if actual!=expected: failures.append(f'sha256:{rel}')
        checks+=1
    mf=set()
    for line in (ROOT/'PACKAGE_MANIFEST.txt').read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if not line or line.startswith('Shunyaya Arithmetic Origin Resolution') or line=='Package manifest' or line.startswith('Files:'): continue
        mf.add(line)
    # Ignore environment/VCS clutter. Missing manifest files fail; unexpected
    # substantive extras warn but do not invalidate the scientific package.
    actual={str(p.relative_to(ROOT)).replace('\\','/') for p in ROOT.rglob('*') if p.is_file() and not ignored_inventory_path(p)}
    missing=sorted(mf-actual); extras=sorted(actual-mf)
    if missing:
        failures.append('manifest_missing:'+';'.join(missing))
    if extras:
        sample=';'.join(extras[:8])
        suffix='' if len(extras)<=8 else f';...(+{len(extras)-8})'
        print(f'integrity:WARN:unlisted_extra_files:count={len(extras)}:{sample}{suffix}')
    checks+=1
    # Text normalization and local-link checks apply to declared package files.
    for rel in sorted(mf & actual):
        p=ROOT/rel
        if p.suffix.lower() in {'.md','.txt','.json','.py','.cff','.yml','.yaml','.toml'} or p.name in {'LICENSE','NOTICE','VERSION'}:
            raw=p.read_bytes()
            try: raw.decode('utf-8')
            except UnicodeDecodeError: failures.append(f'utf8:{rel}')
            if b'\r' in raw: failures.append(f'line_endings:{rel}')
            checks+=2
    for rel in sorted(mf & actual):
        if rel.endswith('.md'):
            _,bad=local_links(rel)
            if bad: failures.append(f'links:{rel}:{",".join(bad)}')
            checks+=1
    if failures:
        for x in failures: print(f'integrity:FAIL:{x}')
        raise SystemExit(1)
    print(f'integrity:PASS:checks={checks}:bound_files={len(bound)}')

def main():
    p=argparse.ArgumentParser(); p.add_argument('--self-test',action='store_true'); p.add_argument('--verify',action='store_true'); a=p.parse_args(); flag='--verify' if a.verify else '--self-test'
    print(f'SAOR v{VERSION} root verification',flush=True)
    integrity()
    run('03_Verification/Core/saor_core_verification.py')
    run('03_Verification/Principal/saor_general_critical_support_synthesis_verifier_v1_3_0.py',flag)
    run('03_Verification/Principal/saor_sharp_support_sensitive_classifier_verifier_v1_3_0.py',flag)
    run('03_Verification/Principal/saor_anchored_cone_corollary_verifier_v1_3_0.py',flag)
    run('03_Verification/Principal/saor_support_necessity_verifier_v1_3_0.py',flag)
    run('03_Verification/Definition_Level/saor_direct_transfer_definition_verifier_v1_3_0.py',flag)
    run('03_Verification/Proof_Audit/saor_cross_proof_consistency_audit_v1_3_0.py',flag)
    for rel in [
      '03_Verification/Regression/saor_static_projection_escape_regression.py',
      '03_Verification/Regression/saor_context_masking_oscillation_regression.py',
      '03_Verification/Regression/saor_rank_two_context_regression.py',
      '03_Verification/Regression/saor_affine_compression_corollary_regression.py',
      '03_Verification/Regression/saor_support_sensitive_escape_regression.py']:
        run(rel)
    print('ROOT VERIFICATION: PASS')
if __name__=='__main__': main()
