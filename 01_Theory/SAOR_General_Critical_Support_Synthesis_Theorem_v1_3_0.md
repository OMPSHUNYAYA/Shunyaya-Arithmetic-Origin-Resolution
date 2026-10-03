# SAOR General Prime-Context Critical-Support Synthesis Theorem v1.3.0

## Theorem

Let `A0` and `B0` be distinct equal-sum/equal-product realizations of common arity `m0` and common product `P0`. (Distinct such pairs always have `m0>=3`; see Section 1 of the proof.) Assume:

1. **Prime Cover.** Every prime divisor of `P0` occurs as a factor value in both `A0` and `B0`.
2. **Atom Deficit.** `Omega(P0)<2m0`.

Extend both roots by an arbitrary finite prime context `E`.

Then:

1. `A_E` and `B_E` are `P`-transfer twins for every `E`.
2. One-sided `S`-separation reduces exactly to a finite collection of fixed-length safe-filler problems, one for each exclusive base factor value and transfer direction.
3. For every fixed forbidden set and every possible smallest safe filler `q`, there is an effectively computable threshold `C_q` such that every residual `R>=C_q` has a one-sided separator using at most two nonbaseline fillers.
4. Consequently, only finitely many low context primes can affect masking through their individual presence. All larger context primes affect masking only through `N(E)` and `S(E)`.
5. An exact masking classifier can therefore be synthesized from the base pair using `N(E)`, `S(E)`, and finitely many prime-support bits.
6. The synthesized signature is future-stable: equal synthesized signatures remain equal after every common finite prime-context extension and therefore have identical future masking responses.

The general synthesized critical set is effective but need not be minimal.

## Synthesis output

The theorem gives an explicit construction

`base pair`

`-> Prime Cover / Atom Deficit checks`

`-> exclusive factors`

`-> forbidden sets`

`-> finitely many smallest-safe-filler regimes`

`-> two-filler thresholds`

`-> finite low-residual tables`

`-> exact masking classifier`.

The sharp SAOR two-module system admits an additional minimization theorem; its exact critical support is `{5,7,11}`.

## Reach of the hypotheses

Prime Cover and Atom Deficit are rarely satisfied by a bare base pair. The [Anchored-Cone Corollary](./SAOR_Anchored_Cone_Corollary_v1_3_0.md) shows that every distinct equal-sum/equal-product pair satisfies both once the common context contains its uncovered prime divisors and at least `max(0,Omega(P0)-2m0+1)` primes. The theorem therefore applies to every pair on an explicit upward-closed cone of contexts.
