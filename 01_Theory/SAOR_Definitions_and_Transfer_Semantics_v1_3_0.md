# SAOR Definitions and Transfer Semantics v1.3.0

## 1. Realizations

A realization is a finite unordered multiset of integers at least `2`.
Two base realizations `A0` and `B0` form an equal-projection pair when they have equal arity, equal sum, and equal product.

A variable context `E` is a finite multiset of primes. It is appended identically to both roots:

`A_E=A0 union E`

`B_E=B0 union E`.

## 2. Retained-factor transfers

Two realizations of the same arity are related by `P`-transfer when they have the same product and share at least one factor value.

They are related by `S`-transfer when they have the same sum and share at least one factor value.

The transfer graphs are simple undirected graphs on realizations of the relevant arity and projection value.

## 3. Formal masking semantics

For `T in {P,S}`, write `N_T(X)` for the neighbours of `X` in the corresponding transfer graph.

The contextual roots are `MASKED` exactly when

`N_P(A_E)\{B_E}=N_P(B_E)\{A_E}`

and

`N_S(A_E)\{B_E}=N_S(B_E)\{A_E}`.

Thus the roots are twins in both transfer relations. Equivalently, exchanging `A_E` and `B_E` while fixing every other realization is an automorphism of each transfer graph.

`UNMASKED` means that this condition fails. A one-sided neighbour is an explicit certificate of unmasking.

## 4. Future masking response

For a fixed module, a future context `F` appends the same additional prime multiset to both contextual roots. Two contexts have the same future masking response when every finite future prime context produces the same masking state.

For a family of modules, the response is the ordered tuple of their masking states.

## 5. Scope

The semantics are exact for the finite realization and prime-context model defined here. Reachability through arbitrary transfer paths is not used as the definition of masking.
