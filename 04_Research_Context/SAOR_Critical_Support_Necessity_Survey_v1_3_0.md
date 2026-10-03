# SAOR Critical-Support Necessity Survey v1.3.0

## What was computed

Every distinct equal-sum/equal-product pair of arity `3` with entries in `[2,20]` and arity `4` with entries in `[2,12]` was placed on its canonical anchored cone using the [Anchored-Cone Corollary](../01_Theory/SAOR_Anchored_Cone_Corollary_v1_3_0.md). This gives `126` anchored pairs in the survey region.

The [support-necessity extractor](../02_Algorithms_and_Software/saor_support_necessity.py) was then run on each anchored pair.

Data: [`SAOR_Critical_Support_Necessity_Survey_v1_3_0.csv`](./SAOR_Critical_Support_Necessity_Survey_v1_3_0.csv)

Regenerate with:

```text
python -B 02_Algorithms_and_Software/saor_support_necessity.py --survey survey.csv --n-max 50
```

The computation uses only the Python standard library.

## Meaning of the columns

`candidate_crit` is the finite critical-prime set produced by the general synthesis theorem.

`certified_necessary_support` records coordinates that are rigorously necessary **within classifiers whose support bits are chosen from the synthesized candidate `Crit`**. Every listed prime has an explicit pair of realizable witness contexts with equal `N` and `S`, equal values on the other candidate support bits, and different masking states. These certificates are re-checked by the definition-level transfer verifier.

`no_witness_within_bound` records primes for which no necessity witness was found with `N<=50`. This is bounded evidence only; it is **not** a proof of non-necessity.

Raising the search bound from `N<=30` to `N<=50` changed no survey row.

## Survey measurements

| Quantity | Value |
| --- | --- |
| Anchored pairs | 126 |
| Mean size of synthesized candidate `Crit` | 5.94 (max 10) |
| Mean size of certified necessary support | 2.04 (max 6) |
| Pairs with no certified support witness within the bound | 18 |
| Pairs with a certified necessity witness for prime `7` | 96 |
| Pairs with a certified necessity witness for prime `5` | 42 |
| Largest certified necessary prime in the survey | 19 |

Most common **certified necessary-support sets** in this bounded survey are `{7}` (27 pairs), `{}` (18), `{7,11,13}` (18), `{5,7,11,13}` (16), `{7,11}` (11), `{5,7}` (8), and `{5,7,11}` (6).

The fixed SAOR module 4 returns certified necessary support `{5,7}` and module 5 returns `{5,7,11}`, matching the separate proof of unique minimum support for those fixed modules.

A second example, `(2,8,9)/(3,4,12)` anchored by `{2,3}`, has a certified necessity witness for prime `13`; that witness uses contexts with 12 prime entries.

## Bounded aggregate-only evidence

For 18 survey pairs no support-necessity witness was found within `N<=50`. For one representative pair, `(2,5,9)/(3,3,10)` anchored by `{2,3,5}`, definition-level enumeration also found no support dependence across `3003` tested contexts of size at most `5` over the first ten primes.

This is evidence for aggregate-only behaviour in the tested region. It is **not** a theorem that these 18 pairs depend only on `(N,S)` for all contexts.

## Interpretation

The general synthesis theorem deliberately favors a finite effective candidate support over immediate minimality. This survey shows that necessity certificates can substantially reduce that candidate set in concrete cases and that support-sensitive behaviour occurs across many anchored pairs.

The exact rule that determines which candidate primes are globally necessary remains open in general. The fixed SAOR modules are the present sharp case: their unique minimum critical supports are proved, not inferred from bounded search.
