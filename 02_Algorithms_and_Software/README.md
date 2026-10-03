# SAOR Reference Software

`saor_core.py` is the standard-library reference implementation of the fixed v1.3.0 semantics.

It provides:

- prime-context validation;
- the sharp two-module classifier;
- the complete sharp signature `(D4,D5,eps5,eps7,eps11)`;
- Prime Cover and Atom Deficit checks;
- safe-filler synthesis data;
- exact low-residual representability;
- a general synthesized masking classifier;
- a future-stable synthesized signature.

`saor_support_necessity.py` searches the synthesized candidate critical set for **certified necessary support coordinates**. Every certified prime is accompanied by explicit equal-`(N,S)` witness contexts with different masking states. Candidate primes without a witness are reported only as bounded-search evidence.

For the fixed SAOR modules the program recovers `{5,7}` for module 4 and `{5,7,11}` for module 5, agreeing with the separately proved sharp minimality result.

```text
python -B 02_Algorithms_and_Software/saor_support_necessity.py --pair 2,6,6,2,3,4,17 3,3,8,2,3,4,17
python -B 02_Algorithms_and_Software/saor_support_necessity.py --survey survey.csv --n-max 50
```

The definition-level transfer verifier is separate from this reference implementation and does not call the sharp closed-form masking functions.
