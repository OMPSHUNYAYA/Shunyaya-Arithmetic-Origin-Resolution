# Shunyaya Arithmetic Origin Resolution (SAOR)

## Exact realization behaviour under common arithmetic context

> **Equal sum and equal product do not determine how an arithmetic realization behaves under common future context. SAOR gives exact conditions for when distinct realizations become transfer twins, constructs finite classifiers from the arithmetic data, and produces explicit future contexts when the fixed sharp system remains distinguishable.**

**Shunyaya Arithmetic Origin Resolution (SAOR) v1.3.0** studies finite integer-multiset realizations under two retained-factor transfer relations: equal-product transfer (`P`) and equal-sum transfer (`S`). Its main results are a general finite critical-support synthesis theorem, an anchored-cone corollary that brings every distinct equal-sum/equal-product pair into that synthesis regime after an explicit finite common prime anchor, and a sharp complete classifier for a fixed two-module SAOR system.

[![Version](https://img.shields.io/badge/Version-1.3.0-blue)](./VERSION)
[![General theorem](https://img.shields.io/badge/General%20synthesis-proved-brightgreen)](./01_Theory/SAOR_General_Critical_Support_Synthesis_Theorem_v1_3_0.md)
[![Anchored cone](https://img.shields.io/badge/Anchored%20cone-every%20pair-brightgreen)](./01_Theory/SAOR_Anchored_Cone_Corollary_v1_3_0.md)
[![Sharp classifier](https://img.shields.io/badge/Sharp%20classifier-complete-brightgreen)](./01_Theory/SAOR_Sharp_Support_Sensitive_Classification_v1_3_0.md)
[![Critical support](https://img.shields.io/badge/Unique%20minimum%20support-5%2C7%2C11-blueviolet)](./01_Theory/SAOR_Sharp_Support_Sensitive_Classification_v1_3_0.md)
[![Proof](https://img.shields.io/badge/Proof-written-orange)](./01_Theory/SAOR_Principal_Proof_v1_3_0.md)
[![Definition checks](https://img.shields.io/badge/Definition--level%20transfer-checked-brightgreen)](./03_Verification/Definition_Level/saor_direct_transfer_definition_verifier_v1_3_0.py)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](./05_Reproduction_and_Verification/SAOR_Verification_Guide_v1_3_0.md)
[![Dependencies](https://img.shields.io/badge/Runtime-standard%20library%20only-blue)](./05_Reproduction_and_Verification/SAOR_Verification_Guide_v1_3_0.md)
[![Citation](https://img.shields.io/badge/Citation-CFF-blue)](./CITATION.cff)
[![License](https://img.shields.io/badge/License-Apache--2.0%20%7C%20CC%20BY--NC%204.0-blue)](./LICENSE)

[![Verify](https://github.com/OMPSHUNYAYA/Shunyaya-Arithmetic-Origin-Resolution/actions/workflows/verify.yml/badge.svg)](https://github.com/OMPSHUNYAYA/Shunyaya-Arithmetic-Origin-Resolution/actions/workflows/verify.yml)

[Theory at a glance](./01_Theory/SAOR_Theory_at_a_Glance_v1_3_0.md) · [Notation](./01_Theory/SAOR_Notation_v1_3_0.md) · [General theorem](./01_Theory/SAOR_General_Critical_Support_Synthesis_Theorem_v1_3_0.md) · [Anchored-Cone Corollary](./01_Theory/SAOR_Anchored_Cone_Corollary_v1_3_0.md) · [Sharp classifier](./01_Theory/SAOR_Sharp_Support_Sensitive_Classification_v1_3_0.md) · [Principal proof](./01_Theory/SAOR_Principal_Proof_v1_3_0.md) · [Claim boundary](./04_Research_Context/SAOR_Claim_Boundary_v1_3_0.md) · [Verification](./05_Reproduction_and_Verification/SAOR_Verification_Guide_v1_3_0.md)

---

## 1. What SAOR asks

Let `A` and `B` be distinct finite integer multisets with the same arity, sum, and product. Append the same finite prime context `E` to both.

`P`-transfer joins realizations with equal product and at least one shared factor value.

`S`-transfer joins realizations with equal sum and at least one shared factor value.

SAOR calls the contextual roots **MASKED** exactly when they are twins in both transfer graphs:

`N_P(A_E)\{B_E} = N_P(B_E)\{A_E}`

and

`N_S(A_E)\{B_E} = N_S(B_E)\{A_E}`.

A one-sided neighbour is therefore an explicit certificate of `UNMASKED`.

### Standard mathematical language

The `S`-transfer vertices are unordered partitions into exactly `m` integer parts, each at least `2`. The `P`-transfer vertices are multiplicative partitions (factorizations) into exactly `m` factors. The sum-side separator problem is a fixed-length additive representability problem with forbidden parts, and `MASKED` is a twin condition between two vertices in each transfer graph.

These ingredients are elementary; the contribution of SAOR is their integration into an exact synthesis and future-classification mechanism with explicit arithmetic hypotheses, finite support data, and constructive separators.

[Formal definitions and transfer semantics](./01_Theory/SAOR_Definitions_and_Transfer_Semantics_v1_3_0.md)

---

## 2. General critical-support synthesis

For an equal-sum/equal-product base pair, assume:

**Prime Cover** — every prime divisor of the common product already occurs as a factor value in both roots.

**Atom Deficit** — `Omega(P0) < 2*m0`, where `Omega` counts prime factors with multiplicity.

Under these conditions, SAOR proves:

`product side`

`-> exact P-twinhood for every finite prime context`

`sum side`

`-> exact safe-filler representability`

`-> finitely many smallest-safe-filler regimes`

`-> explicit one- or two-filler separators for every sufficiently large residual`

`-> finite low-residual exception table`

`-> exact masking classifier from N, S and finitely many support bits`.

The synthesized critical set is finite and effectively computable from the base-pair arithmetic data. It is **not** claimed minimal in general.

Under the theorem hypotheses, the `P` side is automatically twin; the nontrivial masking classification is therefore carried by the `S` side.

[General synthesis theorem](./01_Theory/SAOR_General_Critical_Support_Synthesis_Theorem_v1_3_0.md) · [Principal proof](./01_Theory/SAOR_Principal_Proof_v1_3_0.md) · [General synthesis example](./06_Examples/SAOR_General_Synthesis_Example_v1_3_0.md)

---

## 3. Every pair has an anchored synthesis cone

The bare Prime Cover and Atom Deficit conditions are restrictive. SAOR therefore proves a stronger reach statement.

For **every distinct equal-sum/equal-product pair**, let

`U = uncovered prime divisors of the common product`

and

`t0 = max(0, Omega(P0) - 2*m0 + 1)`.

Once a common prime context contains `U` and has at least `t0` prime entries, the pair satisfies Prime Cover and Atom Deficit. Every further common prime extension stays inside this admissible region.

Thus every distinct equal-sum/equal-product pair admits an explicit finite common prime anchor after which the general SAOR synthesis theorem applies throughout an upward-closed cone of contexts.

This corollary does **not** classify the contexts outside that cone; there the product side can remain nontrivial.

[Anchored-Cone Corollary](./01_Theory/SAOR_Anchored_Cone_Corollary_v1_3_0.md)

---

## 4. Sharp two-module SAOR classifier

For the fixed seed

`(2,6,6)` and `(3,3,8)`,

module 4 uses the canonical anchor `{2,3}` supplied by the Anchored-Cone Corollary for this seed. Module 5 uses `{2,3,4,17}` to create a second safe-filler regime with an independent aggregate defect; its sharp analysis exposes `11` as the additional critical support coordinate.

For these two specified modules, define

`D4(E) = -3 + S - 4*N`

`D5(E) = 4 + S - 5*N`

where

`N = |E|`

and

`S = sum(E)`.

The variable context `E` is any finite multiset of primes.

The exact future signature is

`K(E) = (D4(E), D5(E), eps5(E), eps7(E), eps11(E))`

where `eps_p(E)=1` exactly when `p` occurs in `E`.

For this fixed two-module system:

`E ~future E' iff K(E) = K(E')`.

Equal signatures therefore give identical masking responses after every finite future prime context. Unequal signatures admit explicit constructive future contexts that separate them.

The support coordinates are exact. Among signatures of the form

`(N(E),S(E),supp(E) intersect C)`,

`Crit={5,7,11}` is the **unique minimum** support set for the fixed two-module classifier. Module 4 alone has unique minimum support `{5,7}`.

[Sharp support-sensitive classification](./01_Theory/SAOR_Sharp_Support_Sensitive_Classification_v1_3_0.md) · [Future separator example](./06_Examples/SAOR_Future_Context_Separator_Example_v1_3_0.md)

---

## 5. Why support information is necessary

The contexts

`E = (3,7)`

and

`E' = (5,5)`

have the same aggregate statistics

`N=2`, `S=10`

and the same aggregate two-coordinate values

`(D4,D5)=(-1,4)`.

Yet their exact joint masking states differ:

`(3,7) -> (MASKED,UNMASKED)`

`(5,5) -> (MASKED,MASKED)`.

So `(N,S)` alone cannot classify the enlarged prime-context system. The sharp theorem proves that the missing information is nevertheless finite and exactly captured by the presence of `5`, `7`, and `11`.

[Prime-5 support escape](./06_Examples/SAOR_Prime5_Support_Escape_Example_v1_3_0.md)

---

## 6. Critical-support necessity extraction

[`saor_support_necessity.py`](./02_Algorithms_and_Software/saor_support_necessity.py) searches the synthesized candidate support for **certified necessary coordinates**.

For every prime it certifies as necessary, the program produces explicit equal-`(N,S)` witness contexts whose masking states differ when that support coordinate changes. Those certificates are re-checked against the definition-level transfer search.

If no witness is found within the declared search bound, the result is reported only as **bounded evidence**, not as proof of non-necessity.

Run without using the sharp formulas as its search rule, the method recovers `{5,7}` for module 4 and `{5,7,11}` for module 5, agreeing with the proved sharp result.

The accompanying survey records certified necessity patterns across anchored small pairs while keeping bounded non-witness results explicitly separate from theorem claims.

[Critical-support necessity survey](./04_Research_Context/SAOR_Critical_Support_Necessity_Survey_v1_3_0.md)

---

## 7. Structural corollary: the aggregate rank-two regime

The aggregate two-coordinate calculus remains useful as a structural corollary.

`D4,D5` reconstruct the aggregate context statistics exactly:

`N = D4 - D5 + 7`

`S = 5*D4 - 4*D5 + 31`.

Therefore every observable depending only on `(N,S)` factors through `(D4,D5)`. Integer-affine per-prime characters form a unimodular rank-two system generated by `p-4` and `p-5`.

The support-sensitive theorem identifies the exact boundary of that aggregate compression for the fixed SAOR system.

[Structural corollaries](./01_Theory/SAOR_Structural_Corollaries_v1_3_0.md)

---

## 8. Verification

SAOR uses only the Python standard library.

```text
python -B verify.py --self-test
```

```text
python -B verify.py --verify
```

The verification architecture deliberately separates evidence types:

- **principal theorem checks** — formulas, synthesis reductions, explicit Two-Filler constructions, future stability, anchored-cone checks, support-necessity certificates;
- **definition-level transfer checks** — direct search for one-sided equal-sum and equal-product neighbours without calling the sharp closed-form masking functions;
- **proof consistency audit** — fixed hypotheses, machine-record consistency, and algebraic identity spot checks clearly labelled as such;
- **regressions** — compatibility properties preserved as regression guards rather than presented as proofs of the principal theorem;
- **integrity checks** — required files, declared package inventory, local links, UTF-8/LF normalization, and SHA-256 binding of the bound scientific core; common environment clutter is ignored and unexpected substantive extras warn rather than fail.

The written proof is complemented by definition-level transfer searches, direct checks of constructive separators, anchored-cone verification, and consistency/regression checks. Exact execution counts remain in the verification records and logs.

[Verification guide](./05_Reproduction_and_Verification/SAOR_Verification_Guide_v1_3_0.md) · [Evidence report](./05_Reproduction_and_Verification/SAOR_Verification_Evidence_Report_v1_3_0.md) · [Verification scope](./05_Reproduction_and_Verification/SAOR_Verification_Scope_v1_3_0.md) · [Integrity policy](./05_Reproduction_and_Verification/SAOR_Cryptographic_Integrity_Scope_Policy_v1_3_0.md)

---

## 9. Repository map

| Area | Contents |
| --- | --- |
| [`01_Theory/`](./01_Theory/) | formal semantics, notation, general synthesis theorem, anchored-cone corollary, sharp classifier, principal proof, structural corollaries, scope |
| [`02_Algorithms_and_Software/`](./02_Algorithms_and_Software/) | standard-library reference implementation and critical-support necessity extraction |
| [`03_Verification/`](./03_Verification/) | principal theorem checks, definition-level transfer checks, proof consistency, regressions |
| [`04_Research_Context/`](./04_Research_Context/) | claim boundary, generic comparison categories, theorem status, positioning, bounded survey evidence |
| [`05_Reproduction_and_Verification/`](./05_Reproduction_and_Verification/) | theorem records, verification evidence, metrics, integrity binding |
| [`06_Examples/`](./06_Examples/) | exact examples of twinhood, support escape, synthesis, future separation, and aggregate compression |
| [`tools/`](./tools/) | integrity regeneration tooling |

---

## 10. Claim boundary and mathematical context

SAOR does **not** claim novelty for equal-sum/equal-product realizations, common-factor graph constructions, forbidden-part methods, finite additive-gap phenomena, contextual equivalence as an abstract idea, or affine integer characters.

Related established themes include equal-sum/equal-product realization problems, the classical Frobenius/coin-representability problem and numerical-semigroup gap phenomena, graph twin/module structures, and contextual equivalence.

The repository's scientific claim is the integrated arithmetic theory proved here:

`retained-factor transfer semantics`

`-> product twinhood under explicit arithmetic conditions`

`-> exact safe-filler reduction`

`-> finite critical-support synthesis`

`-> anchored synthesis cone for every distinct equal-sum/equal-product pair`

`-> sharp complete future classifier with unique minimum support {5,7,11}`.

The general synthesized critical set is not claimed minimal. Bounded absence of a support witness is not presented as proof of non-necessity. Historical priority is not asserted.

[Full claim boundary](./04_Research_Context/SAOR_Claim_Boundary_v1_3_0.md) · [Relationship to established structures](./04_Research_Context/SAOR_Relationship_to_Established_Structures_v1_3_0.md)

---

## 11. Integrity policy

Cryptographic binding is intentionally limited to the bound scientific identity: theorem/semantics/proof files, reference implementation, principal and definition-level verifiers, proof-consistency and regression programs, and selected machine-readable theorem records.

Editable repository surfaces—including `README.md`, `LICENSE`, license texts, `CITATION.cff`, notices, workflows, `PACKAGE_MANIFEST.txt`, examples, verification guides, evidence prose, survey prose/data, and repository-positioning documents—are deliberately excluded from the hash set.

[Integrity scope policy](./05_Reproduction_and_Verification/SAOR_Cryptographic_Integrity_Scope_Policy_v1_3_0.md)

---

## 12. Citation

Preferred collective citation author:

`Shunyaya Framework Authors`

See [`CITATION.cff`](./CITATION.cff) for machine-readable citation metadata.

---

## 13. License

Software, verification programs, workflows, and machine-readable scientific artifacts are licensed under the **Apache License 2.0**.

Research exposition, architecture documentation, and documentation are licensed under **Creative Commons Attribution-NonCommercial 4.0 International**.

See [LICENSE](./LICENSE) for the repository license map and [`LICENSES/`](./LICENSES/) for the complete license texts.

---

## Closing note

SAOR separates visible arithmetic projection from realization behaviour under common context. v1.3.0 proves an effective finite synthesis mechanism, extends that mechanism to an explicit anchored cone for every distinct equal-sum/equal-product pair, and gives a sharp complete future classifier for the fixed two-module system. The repository is structured so that theorem statements, proof, definition-level checks, executable verification, examples, claim boundaries, and integrity records can be inspected separately.
