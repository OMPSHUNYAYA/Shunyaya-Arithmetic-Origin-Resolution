"""Compatibility regression for the seed's static projection coincidence.

The fixed seed realizations (2,6,6) and (3,3,8) have the same sum and product.
The regression preserves that starting projection fact; it is not evidence for
the principal v1.3.0 classification theorem.
"""
import math
A=(2,6,6); B=(3,3,8)
assert sum(A)==sum(B) and math.prod(A)==math.prod(B)
print('SAOR static-projection escape regression: PASS')
