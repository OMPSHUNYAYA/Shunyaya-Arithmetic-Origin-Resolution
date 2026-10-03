"""Compatibility regression for the exact two-parameter masking defect.

The defect is D(a,b)=3b-2a-1. The regression checks the alternating
masked/unmasked trajectory associated with contextual masking oscillation.
It is a compatibility guard, not evidence for the principal v1.3.0 theorem.
"""

def D(a,b): return 3*b-2*a-1
for n in range(1,21):
    assert D(3*n,2*n)==-1
    assert D(3*n,2*n+1)==2
print('SAOR contextual masking oscillation regression: PASS')
