# SAOR Anchored-Cone Corollary v1.3.0

## Motivation

Prime Cover and Atom Deficit are rarely satisfied by a bare base pair. Among all distinct equal-sum/equal-product pairs with entries in `[2,30]` (arity 3), `[2,18]` (arity 4) and `[2,12]` (arity 5), **none** of arity 3 or 4 and **3 of 573** of arity 5 satisfy both (`03_Verification/Principal/saor_anchored_cone_corollary_verifier_v1_3_0.py`, census lines). The seed `(2,6,6)/(3,3,8)` itself fails Prime Cover.

The corollary below shows that the general synthesis theorem nevertheless applies to **every** distinct equal-sum/equal-product pair once the common context contains a finite anchor.

## Statement

Let `A0,B0` be distinct equal-sum/equal-product realizations with common product `P0` and arity `m0` (necessarily `m0>=3`; see Section 1 of the proof). Define

- the **uncovered primes** `U = { p prime : p | P0, and p is not a factor value of both A0 and B0 }`;
- the **atom threshold** `t0 = max(0, Omega(P0) - 2*m0 + 1)`.

Call a finite prime context `E` **anchored** when

`U subset supp(E)` and `N(E) >= t0`.

Then:

1. For every finite prime multiset `H` with `U subset supp(H)` and `N(H) >= t0`, the pair `(A0 union H, B0 union H)` satisfies Prime Cover and Atom Deficit. The general synthesis theorem therefore applies to it, giving an exact masking classifier with finite critical support and a future-stable signature.
2. On anchored contexts, `A_E` and `B_E` are `P`-transfer twins.
3. The anchored contexts form an upward-closed cone: if `E` is anchored, so is `E union F` for every finite prime context `F`. Future stability therefore holds inside the cone.

The **canonical anchor** is `H* = U` together with `max(0, t0-|U|)` copies of `2`.

## Proof

(1) The primes dividing `P0 * prod(H)` are the primes of `P0` and the primes in `H`. A prime of `P0` is either a common factor value of `A0` and `B0`, or lies in `U` and hence in `H`; in both cases it is a factor value of both anchored roots. Every prime of `H` lies in both anchored roots. This is Prime Cover. For Atom Deficit, `H` consists of primes, so `Omega(P0 * prod(H)) = Omega(P0) + N(H)`, and

`Omega(P0) + N(H) < 2(m0 + N(H))` iff `N(H) > Omega(P0) - 2*m0` iff `N(H) >= t0`.

(2) Apply Section 2 of the proof to the anchored pair with `H = E` and empty further context.

(3) Support and `N` only grow under extension.

## Remarks

- **The atom threshold is sufficient but not always sharp.** For `(2,18,24)/(3,9,32)` and `(6,18,32)/(8,12,36)` (each anchored by its primes), one-sided `P`-neighbours exist at `N=t0-1` and vanish at `t0`. For `(12,30,54)/(18,18,60)` they vanish one step earlier. All three are checked by the verifier.
- **Atom Deficit is genuinely needed below the threshold.** In each example above a one-sided `P`-neighbour exists at `N=0`, so the product side can unmask when Atom Deficit fails.
- **Computational check.** For every equal-sum/equal-product pair of arity 3 with entries `<=20` and arity 4 with entries `<=12` (126 pairs; 228 in complete mode), the canonical anchor makes the pair admissible, and the synthesized classifier agrees with the definition-level verification on every tested context, with no one-sided `P`-neighbour found.

## Scope

The corollary describes masking on anchored contexts. It makes no claim about contexts outside the cone: contexts that omit an uncovered prime, or that have fewer than `t0` primes. There the product side can matter. That is the regime where a genuinely dual (`P` and `S`) theory would live.
