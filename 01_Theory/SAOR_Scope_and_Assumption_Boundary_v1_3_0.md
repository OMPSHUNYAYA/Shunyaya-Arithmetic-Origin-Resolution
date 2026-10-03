# SAOR Scope and Assumption Boundary v1.3.0

## Principal general theorem

The general critical-support synthesis theorem applies to distinct equal-sum/equal-product base pairs with common arity at least `3`, under:

- finite prime-only common contexts;
- Prime Cover;
- Atom Deficit;
- retained-factor `P` and `S` transfer semantics;
- masking defined as dual twinhood.

It guarantees an exact synthesized masking classifier with finite critical support and a future-stable signature. It does not assert that the synthesized candidate support is minimal for every base pair.

## Sharp theorem

For the fixed SAOR seed pair and its two specified anchors, the unique minimum critical support is `{5,7,11}` among signatures of the form `(N,S,supp intersect C)` and the five-component signature is a complete iff classifier of future masking behaviour.

## Not claimed

SAOR v1.3.0 does not claim:

- classification of every equal-sum/equal-product realization pair in every context;
- a result for arbitrary composite-valued context alphabets;
- a result for base pairs failing Prime Cover or Atom Deficit outside the anchored cone of the [Anchored-Cone Corollary](./SAOR_Anchored_Cone_Corollary_v1_3_0.md) (inside the cone, every distinct pair is covered);
- classification of arbitrary transfer-path reachability;
- minimality of the general synthesized critical set (the support-necessity extractor certifies necessary coordinates; absence of a witness is bounded-search evidence only);
- novelty of numerical-semigroup gaps, forbidden-part methods, contextual equivalence, or affine integer characters as generic concepts;
- historical priority.

The repository states only results proved within the fixed semantics and hypotheses.
