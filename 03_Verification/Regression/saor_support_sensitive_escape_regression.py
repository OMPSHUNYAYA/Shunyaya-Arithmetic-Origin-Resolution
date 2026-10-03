from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/'02_Algorithms_and_Software'))
import saor_core as C
E,F=(3,7),(5,5)
assert C.stats(E)==C.stats(F)==(2,10)
assert (C.D4(E),C.D5(E))==(C.D4(F),C.D5(F))
assert C.joint_status(E)!=C.joint_status(F)
print('SAOR support-sensitive escape regression: PASS')
