# SAOR Sharp Support-Sensitive Classification v1.3.0

## 1. Fixed seed and modules

Use the seed pair

`U=(2,6,6)`

`V=(3,3,8)`.

Module 4 appends the common anchor `{2,3}`, which is the canonical anchor supplied by the Anchored-Cone Corollary for this seed.
Module 5 appends `{2,3,4,17}`. The added shared values produce a distinct safe-filler regime and an independent aggregate defect; the sharp analysis below exposes `11` as the additional critical support coordinate.
The variable context `E` is any finite multiset of primes.

Write

`N=|E|`

`S=sum E`

and

`D4=-3+S-4N`

`D5=4+S-5N`.

Let `eps5`, `eps7`, `eps11` record whether `5`, `7`, `11` occur in `E`.

## 2. Module 4

Module 4 is masked exactly when

`D4<0`

or

`D4=1 and eps5=1`

or

`D4=3 and eps5=eps7=1`.

Equivalently, the nonnegative exceptional gap set is empty when `5` is absent, `{1}` when `5` is present but `7` is absent, and `{1,3}` when both are present.

## 3. Module 5

When `5` is absent, module 5 is masked exactly when

`D5<0`.

When `5` is present, the safe filler changes from `5` to `6`. Define

`T5=S-6N-2`.

Then module 5 is masked exactly when

`T5<0`

or

`T5 in {1,2} and eps7=1`

or

`T5=5 and eps7=eps11=1`.

## 4. Complete future classifier

Define

`K(E)=(D4(E),D5(E),eps5(E),eps7(E),eps11(E))`.

For the two fixed modules,

`E ~future E' iff K(E)=K(E')`.

Sufficiency follows because the current masking laws and every future update are determined by `K`.
Necessity is constructive: every differing coordinate admits a finite future prime context producing different ordered masking states.

## 5. Minimal critical support

Each of `eps5`, `eps7`, and `eps11` is necessary in a stronger sense: for each prime `p` in `{5,7,11}` there are equal-`(N,S)` context pairs whose full prime supports differ only at `p`, and an explicit future context separates their masking responses. Therefore every classifier of the form `(N,S,supp(E) intersect C)` must contain all three primes.

No prime `>=13` requires an individual support coordinate.

Hence `{5,7,11}` is the **unique minimum** prime-support set for the fixed two-module future classifier. Module 4 alone has unique minimum support `{5,7}`.

## 6. Non-affine escape

The contexts

`E=(3,7)`

and

`E'=(5,5)`

have the same `N=2`, `S=10`, and the same aggregate pair `(D4,D5)=(-1,4)`, but different joint masking states:

`E -> (MASKED,UNMASKED)`

`E' -> (MASKED,MASKED)`.

Thus the support-sensitive classifier contains information not determined by `(N,S)`.

## 7. Proof

The complete written proof is in [Principal Proof, Section 9](./SAOR_Principal_Proof_v1_3_0.md#9-sharp-two-module-specialization). It covers both separation directions (6-side and 8-side) of each module, the change of safe filler when `5` is present, sufficiency, the constructive separators for each signature coordinate, and the necessity witnesses for `eps5`, `eps7` and `eps11`.

Separate recomputation: the [support-necessity extractor](../02_Algorithms_and_Software/saor_support_necessity.py), which does not use these formulas, certifies `{5,7}` for module 4 and `{5,7,11}` for module 5.
