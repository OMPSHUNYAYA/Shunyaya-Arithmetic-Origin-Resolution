# SAOR Structural Corollaries v1.3.0

These results are consequences of the principal masking theorems and are not presented as co-equal principal results.

## 1. Rank-two aggregate compression

For contexts in the original affine regime,

`D4=-3+S-4N`

`D5=4+S-5N`.

The transformation is invertible:

`N=D4-D5+7`

`S=5D4-4D5+31`.

Therefore `(D4,D5)` and `(N,S)` contain exactly the same aggregate information.

Any observable depending only on `(N,S)`, affine or non-affine, factors through `(D4,D5)`.

## 2. Affine character basis

For the per-prime characters

`chi_4(p)=p-4`

`chi_5(p)=p-5`,

every integer-affine character `f(p)=a*p+b` has the unique representation

`f=(5a+b)chi_4+(-4a-b)chi_5`.

The coefficient vectors `(1,-4)` and `(1,-5)` have determinant `-1`, so they form a unimodular basis of the integer-affine character group.

## 3. Boundary exposed by support sensitivity

The prime-`5` example proves that aggregate compression is not the full SAOR theory: contexts with identical `(N,S)` can have different masking states. The support-sensitive theorem identifies the exact additional information required for the fixed modules.
