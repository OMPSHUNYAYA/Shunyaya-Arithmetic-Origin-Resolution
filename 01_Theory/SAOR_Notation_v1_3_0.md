# SAOR Notation v1.3.0

SAOR works with finite unordered multisets of integers at least `2`.

- `A0`, `B0`: fixed base realizations.
- `E`, `F`: finite prime contexts, counted with multiplicity.
- `A_E=A0 union E`, `B_E=B0 union E`: common-context extensions.
- `N(E)=|E|`: context cardinality with multiplicity.
- `S(E)=sum E`: context sum.
- `supp(E)`: set of values occurring in `E`.
- `Omega(n)`: number of prime factors of `n`, counted with multiplicity.
- `N_P(X)`, `N_S(X)`: external neighbours under product-transfer and sum-transfer.
- `MASKED`: dual twinhood in the two transfer graphs.
- `UNMASKED`: failure of dual twinhood.
- `Crit`: a finite set of context primes whose presence can affect low-residual separation.
- `eps_p(E)`: `1` when `p in supp(E)`, otherwise `0`.

`union` denotes multiset union when contexts are composed. Support coordinates update by Boolean OR, while `N` and `S` update additively.
