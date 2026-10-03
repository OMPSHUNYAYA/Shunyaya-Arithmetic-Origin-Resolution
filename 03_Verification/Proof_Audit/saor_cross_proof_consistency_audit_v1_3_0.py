#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'02_Algorithms_and_Software'))
import saor_core as C

def run(deep=False):
    checks=0; identity_checks=0; record_checks=0
    # Fixed seed projection equality.
    assert sum(C.SEED_A)==sum(C.SEED_B)==14; checks+=1
    assert math.prod(C.SEED_A)==math.prod(C.SEED_B)==72; checks+=1
    # Fixed module hypotheses.
    for H in (C.ANCHOR4,C.ANCHOR5):
        d=C.base_data(C.SEED_A+H,C.SEED_B+H)
        assert d['prime_cover'] and d['atom_deficit']; checks+=2
    # Aggregate reconstruction and affine basis identities.
    span=100 if deep else 20
    for d4 in range(-span,span+1):
      for d5 in range(-span,span+1):
        N=d4-d5+7; S=5*d4-4*d5+31
        assert -3+S-4*N==d4 and 4+S-5*N==d5; identity_checks+=1
    for a in range(-10,11):
      for b in range(-10,11):
        x,y=5*a+b,-4*a-b
        assert x+y==a and -4*x-5*y==b; identity_checks+=1
    # Machine records use the fixed version and theorem names.
    rec=json.loads((ROOT/'05_Reproduction_and_Verification/SAOR_Theorem_Record_v1_3_0.json').read_text())
    assert rec['version']=='1.3.0'; record_checks+=1
    assert rec['principal_general_result']=='General Prime-Context Critical-Support Synthesis Theorem'; record_checks+=1
    assert rec['sharp_result']['unique_minimum_critical_support']==[5,7,11]; record_checks+=1
    assert rec['sharp_result']['minimum_scope']=='signatures of the form (N,S,supp(E) intersect C)'; record_checks+=1
    print('SAOR cross-proof consistency audit v1.3.0')
    # Note: the identity loops re-confirm linear identities that hold for all
    # integers by direct algebra; they are reported separately so that their
    # count is not read as separate evidence for the masking theorems.
    print(f'fixed_module_hypothesis_checks:PASS:checks={checks}')
    print(f'algebraic_identity_spot_checks:PASS:checks={identity_checks}:implied_by_algebra')
    print(f'machine_record_consistency:PASS:checks={record_checks}')
    print('scope:general_synthesis_requires_prime_cover_atom_deficit_arity_at_least_3')
    print('scope:sharp_complete_classifier_is_fixed_two_module_system')
    print('CONSISTENCY AUDIT: PASS')

def main():
    p=argparse.ArgumentParser(); p.add_argument('--self-test',action='store_true'); p.add_argument('--verify',action='store_true'); a=p.parse_args(); run(a.verify)
if __name__=='__main__': main()
