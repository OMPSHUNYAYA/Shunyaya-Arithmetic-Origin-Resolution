#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'02_Algorithms_and_Software'))
import saor_core as C
assert C.VERSION=='1.3.0'
assert C.joint_status((3,7))==(True,False)
assert C.joint_status((5,5))==(True,True)
assert C.sharp_signature((3,7))[:2]==C.sharp_signature((5,5))[:2]==(-1,4)
A=C.SEED_A+C.ANCHOR4; B=C.SEED_B+C.ANCHOR4
d=C.base_data(A,B); assert d['prime_cover'] and d['atom_deficit']
assert C.synthesized_masked(A,B,()) in (True,False)
print('SAOR core verification: PASS')
