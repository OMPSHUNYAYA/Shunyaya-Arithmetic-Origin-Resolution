# SAOR Principal Proof v1.3.0

## 1. Setup

Let `A0,B0` be distinct equal-sum/equal-product realizations of arity `m0>=3`, common sum `Sigma0`, and common product `P0`. Let `E` be a finite prime multiset and define

`A_E=A0 union E`, `B_E=B0 union E`, `m=m0+N(E)`.

Assume Prime Cover and Atom Deficit as stated in the general synthesis theorem.

**Remark (arity is automatic).** Distinct equal-sum/equal-product realizations of arity `1` or `2` do not exist: a pair `{a,b}` is determined by `a+b` and `ab` as the root multiset of `x^2-(a+b)x+ab`. Hence `m0>=3` holds for every distinct base pair, and `k=m-1>=2` for every context.

## 2. Product-transfer twinhood

Every prime divisor of `P0` already occurs as a factor value in both base roots. Every prime introduced by `E` is also a shared factor value of `A_E` and `B_E`.

A one-sided `P`-neighbour of one root must avoid every factor value occurring in the other root. It therefore cannot contain any prime-valued factor: every prime divisor available in the common product is forbidden as a factor value.

Hence each factor in such a candidate must be composite and consumes at least two prime atoms. A candidate of arity `m=m0+N(E)` would require at least `2m` prime atoms.

The contextual product has

`Omega(P0)+N(E)`

prime atoms. Since `Omega(P0)<2m0`,

`Omega(P0)+N(E)<2m0+N(E)<=2m0+2N(E)=2m`.

Thus no one-sided product neighbour exists in either direction. The roots are `P`-twins for every prime context.

**Remark (where Atom Deficit is used).** The argument needs only `Omega(P0)+N(E)<2m`, that is `N(E)>Omega(P0)-2m0`. Atom Deficit is exactly this condition at `N(E)=0`. See the Anchored-Cone Corollary.

## 3. Exact safe-filler reduction of the sum side

Consider an `S`-neighbour of `A_E` that is not an `S`-neighbour of `B_E`. It must share some value with `A_E` while avoiding every value of `B_E`.

The shared value therefore lies in

`supp(A_E)\supp(B_E)=supp(A0)\(supp(B0) union supp(E))`.

Every element `x` of `supp(A0)\supp(B0)` is composite: a prime value of `A0` divides `P0`, so by Prime Cover it also occurs in `B0`. Since `E` contains only primes, `x` is never removed by the context. Hence the shared value is an exclusive base value

`x in supp(A0)\supp(B0)`,

and this exclusive set is the same for every context `E`.

Fix one occurrence of `x`. The remaining `k=m-1` factors must sum to

`Sigma0+S(E)-x`

and avoid

`supp(B0) union supp(E)`.

Conversely, any such safe filling, together with `x`, is a realization of arity `m` and sum `Sigma0+S(E)` that shares `x` with `A_E` and shares no value with `B_E`; it is distinct from `A_E` because `A_E` shares a prime value with `B_E` (Prime Cover, `P0>1`). It is therefore a one-sided `S`-neighbour. One-sided separation is exactly a fixed-length safe-filler representability problem. The opposite direction is symmetric.

## 4. Finitely many smallest-safe-filler regimes

Fix a finite opposite-root forbidden set `B`. Let `q(E)` be the smallest integer at least `2` outside `B union supp(E)`.

Let `Q_B` be the smallest composite integer not in `B`. Since the variable context contains only primes, it cannot forbid `Q_B`. Hence

`q(E)<=Q_B`.

Only finitely many values of `q` can occur, and `q(E)` depends on `supp(E)` only through primes below `Q_B`.

Every safe value is at least `q`, so every safe filling has sum at least `kq`.

## 5. Permanent odd increment

Fix one possible `q`. Put

`M=max(B union {q,2})`.

Choose an odd positive integer `a` such that `q+a` is composite and `q+a>M`. Such an `a` exists:

- if `q` is odd, `q+a` is even, and every even integer `>M` with `M>=2` is composite;
- if `q` is even, `q+a` is odd, and there are arbitrarily large odd composites (for example odd squares), so one exceeding `M` with the correct parity exists.

The filler `q+a` lies outside `B` and, being composite, cannot be forbidden by any prime context.

Define

`C_q=M+a-q+1`.

## 6. Two-Filler Eventual Separator Lemma

Let

`R=target-kq`

be the residual above the all-`q` baseline. Assume `k>=2` (Section 1).

If `R<0`, no filling exists.

Suppose `R>=C_q`.

If `q+R` is safe, replace one baseline `q` by `q+R`.

Otherwise, `q+R>=M+a+1>M`, so it is not in the fixed forbidden set `B`. The only remaining reason it can be forbidden is that it is a context prime; write

`p=q+R`.

Because `p>M>=2`, `p` is an odd prime, and since `a` is odd, `p-a` is even. Moreover,

`R>=M+a-q+1`

implies

`p-a=q+R-a>M`.

Thus `p-a` is an even integer larger than `M>=2`, hence composite, larger than every fixed forbidden value, and immune to prime-context exclusion.

Use two nonbaseline fillers

`q+a`

and

`p-a`.

Their increments over two copies of `q` are

`a`

and

`p-a-q=R-a`,

which sum to `R`. All remaining `k-2` positions use `q`. This constructs a safe filling.

Therefore every `R>=C_q` is feasible.

## 7. Finite critical support

All infeasible nonnegative residuals lie in

`0<=R<C_q`.

Every filler that can occur while resolving such a residual is at most

`q+R<=q+C_q-1`.

Taking the maximum of this bound over the finitely many possible `q` regimes yields a finite number `L_B`.

A context prime greater than `L_B` cannot affect any low-residual safe-filler decision by its individual presence. It can affect the target only through `N(E)` and `S(E)`.

**Finiteness of the low-residual table.** The slot count `k=m0+N(E)-1` is unbounded, but a residual `R>=1` uses at most `R` nonbaseline slots (each nonbaseline filler contributes an increment of at least `1`). Feasibility of `R` with `k` slots therefore equals feasibility with `min(k,R)` slots. For each `q` regime, the low-residual decision is a function of `R<C_q`, `min(k,R)<C_q`, and `supp(E) intersect [2,L_B]`: a finite table.

Applying this construction to each exclusive base value and to both directions produces a finite candidate critical-prime set `Crit` for the whole module.

The masking state is then a function of `N(E)`, `S(E)`, and `supp(E) intersect Crit`: `q` is determined by the support bits, `R` by `N`, `S` and `q`, and feasibility by the rules above.

## 8. Future stability

Use the synthesized signature

`K(E)=(N(E),S(E),supp(E) intersect Crit)`.

For every future prime context `F`,

`N(E union F)=N(E)+N(F)`

`S(E union F)=S(E)+S(F)`

and each support bit updates by Boolean OR.

Therefore `K(E)=K(E')` implies

`K(E union F)=K(E' union F)`

for every `F`. Because the exact masking classifier is a function of `K`, equal signatures have identical future masking responses.

The general construction is sufficient and future-stable; it is not asserted to be minimal for every base pair.

## 9. Sharp two-module specialization

Seed `U=(2,6,6)`, `V=(3,3,8)`; module 4 appends `{2,3}`, module 5 appends `{2,3,4,17}`.

### 9.1 Hypotheses

Module 4: `A0=(2,2,3,6,6)`, `B0=(2,3,3,3,8)`, `Sigma0=19`, `P0=432=2^4*3^3`, `Omega(P0)=7<10=2m0`.
Module 5: `A0=(2,2,3,4,6,6,17)`, `B0=(2,3,3,3,4,8,17)`, `Sigma0=40`, `P0=29376=2^6*3^3*17`, `Omega(P0)=10<14=2m0`.
Both satisfy Prime Cover. By Section 2, the product side never unmasks; masking is decided by the sum side alone. In both modules the exclusive values are `6` (in `A0`) and `8` (in `B0`).

Write `N=N(E)`, `S=S(E)`, `D4=-3+S-4N`, `D5=4+S-5N`, `T5=S-6N-2=2D5-D4-13`.

Below, "the 6-side" means one-sided neighbours of `A_E` (they contain `6` and avoid `supp(B0) union supp(E)`); "the 8-side" means one-sided neighbours of `B_E`. A module is MASKED iff both sides are infeasible.

### 9.2 Module 4

**6-side.** Forbidden `{2,3,8} union supp(E)`, `q=4` always (`4` is composite and not forbidden), `k=4+N>=4`, target `13+S`, residual `R=13+S-4(4+N)=D4`.

Available increments (filler minus `4`): `1` iff `5` not in `E`; `2` (filler `6`) always; `3` iff `7` not in `E`; `4` never (filler `8` forbidden); every `r>=5` with `4+r` safe.

- `5` absent: every `R>=0` is feasible. `R=1,2` use `5`, `6`. For `R>=3`: if `4+R` is safe use it; otherwise `4+R` is `8` (then `R=4=2+2`, fillers `6,6`) or an odd prime `p>=7`, and then `5` and `p-1` work (`p-1` is even, at least `6`, and not `8` since `9` is not prime).
- `5` present, `7` absent: `R=1` is infeasible (the only increment `1` is lost). `R=2,3,4` use `6`, `7`, `6+6`. For `R>=5` with `4+R=p` a context prime: use `9` and `p-5` (even, `>=6`) unless `p=13`, in which case use `7` and `10`.
- `5` and `7` present: increments `1` and `3` are lost and `4` never exists, so `R=1` and `R=3` are infeasible. `R=2,4,5,6,7` use `6`, `6+6`, `9`, `10`, `6+9`. For `R>=5` with `4+R=p` a context prime: use `9` and `p-5` unless `p=13`; for `p=13` (`R=9`) use `6,6,9` (three slots; `k>=6` here).

So the 6-side is infeasible exactly when `D4<0`, or `D4=1` and `eps5=1`, or `D4=3` and `eps5=eps7=1`.

**8-side.** Forbidden `{2,3,6} union supp(E)`, `q=4`, target `11+S`, residual `D4-2`. In each case where the 6-side is infeasible: `D4<0` and `D4=1` give a negative residual; `D4=3` gives residual `1`, whose only increment needs filler `5`, which is forbidden because `eps5=1`. So the 8-side is infeasible whenever the 6-side is.

Hence module 4 is MASKED iff `D4<0` or (`D4=1` and `eps5`) or (`D4=3` and `eps5` and `eps7`).

### 9.3 Module 5, prime 5 absent

**6-side.** Forbidden `{2,3,4,8,17} union supp(E)`, `q=5`, `k=6+N`, target `34+S`, residual `D5`. Filler `6` (increment `1`) is composite and never forbidden. For `R>=1`: if `5+R` is safe use it; otherwise use `6` and `4+R`. (`4+R` is safe except in one case: if `5+R=17` then `4+R=16`; if `5+R` is an odd prime `>=7`, then `4+R` is even, `>=6`, and not `8`; if `5+R=8`, so `R=3`, use `6,6,6` instead, which needs three slots, and `k>=6`.) So the 6-side is feasible iff `D5>=0`.

**8-side.** Forbidden `{2,3,4,6,17} union supp(E)`, `q=5`, target `32+S`, residual `D5-2`, negative whenever `D5<0`.

Hence, with `5` absent, module 5 is MASKED iff `D5<0`.

### 9.4 Module 5, prime 5 present

**6-side.** Forbidden `{2,3,4,5,8,17} union supp(E)`, `q=6`, residual `34+S-6(6+N)=T5`. Increment `2` (filler `8`) and increment `11` (filler `17`) never exist; `3` (`9`), `4` (`10`), `6` (`12`), `8` (`14`) always exist; `1` exists iff `7` is absent; `5` exists iff `11` is absent.

- `7` absent: every `R>=0` is feasible. For `R>=1`: if `6+R` is safe use it; otherwise use `7` and `5+R`, which is safe (`6+R=8` gives `5+R=7`, which is safe since `7` is absent; `6+R=17` gives `16`; an odd prime `6+R>=11` gives an even `5+R>=10`).
- `7` present: `R=1,2` are infeasible (the only increments `<=2` are `1` and `2`). `R=3,4` use `9`, `10`. `R=5` needs increment `5` (filler `11`), since `5` is not a sum of increments from `{3,4}`; so it is infeasible iff `11` is present. For `R>=6`: if `6+R` is safe use it; otherwise `6+R` is `17` (use `9,14`) or a context prime `p>=13` (use `9` and `p-3`, even, `>=10`).

So the 6-side is infeasible exactly when `T5<0`, or `T5 in {1,2}` and `eps7`, or `T5=5` and `eps7` and `eps11`.

**8-side.** Forbidden `{2,3,4,5,6,17} union supp(E)`, `q=7` (or `8` if `7` is in `E`), target `32+S`. The residual is `T5-N-8` (or `T5-2N-14`). In every case where the 6-side is infeasible, `T5<=5` and `N>=1`, so the 8-side residual is negative.

Hence, with `5` present, module 5 is MASKED iff `T5<0` or (`T5 in {1,2}` and `eps7`) or (`T5=5` and `eps7` and `eps11`).

### 9.5 Sufficiency and future action

`K(E)=(D4,D5,eps5,eps7,eps11)` determines `N=D4-D5+7`, `S=5D4-4D5+31`, `T5`, and all three bits, hence both masking states (9.2–9.4). Under a future context `F`, `D4` and `D5` change by `sum(p-4)` and `sum(p-5)` over `F`, and the bits update by OR. So `K(E)=K(E')` implies identical masking under every future context.

### 9.6 Completeness: constructive separators

Let `K(E)!=K(E')`. Take the first differing coordinate in the order below. Each step appends the same context `X` to both and produces different joint masking states.

1. **`D4` differs.** Choose `X` with `sum(p-4)=-max(D4(E),D4(E'))`, using `3`s (each `-1`) or `7`s and `3`s (`ceil(d/3)` sevens and `3*ceil(d/3)-d` threes give `+d`). Afterwards one context has `D4=0` (residual `0`, feasible: module 4 UNMASKED) and the other has `D4<0` (module 4 MASKED).
2. **`eps5` differs, `D4` equal.** Choose `X` free of `5` with `D4` becoming `1` for both. By 9.2, the context containing `5` is masked in module 4 and the other is not.
3. **`eps7` differs, `D4`, `eps5` equal.** Append `5` if absent, then a context free of `7` (built from `11`s, each `+7`, and `3`s, each `-1`) bringing `D4` to `3`. By 9.2, the context containing `7` is masked in module 4 and the other is not.
4. **`D5` differs, all of the above equal.** If `5` is absent, choose `X` free of `5` with `sum(p-5)=-max(D5)` (built from `2`s, `-3` each, and `7`s, `+2` each). Afterwards one context has `D5=0` and the other `D5<0`, and they differ in module 5 by 9.3. If `5` is present, `T5=2D5-D4-13` differs; choose `X` from `5`s and `7`s with `sum(p-6)=-max(T5)`. Afterwards one context has `T5=0` (feasible) and the other has `T5<0`, and they differ in module 5 by 9.4.
5. **Only `eps11` differs.** Append `5` and `7` where absent, then `5`s and `7`s to bring `T5` to `5`. By 9.4, the context containing `11` is masked in module 5 and the other is not.

Hence `E ~future E'` iff `K(E)=K(E')`.

### 9.7 Unique minimum critical support

For each `p` in `{5,7,11}` there are equal-`(N,S)` contexts whose **full prime supports differ only at `p`** and whose future masking responses differ:

| required prime | `E` | `E'` | future `X` | effect |
| --- | --- | --- | --- | --- |
| `5` | `(3,5,5,7)` | `(3,3,7,7)` | `()` | different current joint masking states |
| `7` | `(3,3,5,7)` | `(3,5,5,5)` | `(3,3,3,11)` | module 4 separates |
| `11` | `(3,3,7,11)` | `(3,7,7,7)` | `(3,5,17)` | module 5 separates |

Each pair has the same `N` and `S`. Because the full supports differ only at the displayed prime, any classifier of the form

`(N(E),S(E),supp(E) intersect C)`

that is complete for future masking must include that prime in `C`. Thus every valid support set `C` contains `{5,7,11}`. Sections 9.2--9.5 show that `{5,7,11}` itself suffices, and no prime `>=13` occurs in the exact masking laws. Hence `{5,7,11}` is the **unique minimum** prime-support set for the fixed two-module classifier.

The first two witnesses also apply to module 4 alone, while its exact law uses no other support coordinate. Therefore `{5,7}` is the unique minimum support set for module 4 among classifiers of the same form.

## 10. Structural corollary

In the aggregate affine regime, `(D4,D5)` is an invertible affine encoding of `(N,S)`. The associated affine character basis and rank-two statement follow immediately. They are structural corollaries of the context calculus rather than independent masking theorems.
