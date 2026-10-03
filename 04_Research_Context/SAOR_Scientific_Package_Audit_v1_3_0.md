# SAOR Scientific Package Audit v1.3.0

The package is organized under the following controls:

- masking is formally defined as dual twinhood;
- theorem statements, proof, examples, software, verification, positioning, and claim boundaries are separated;
- the general synthesis theorem and the sharp fixed-system theorem have distinct scopes;
- the Anchored-Cone Corollary is stated separately from the bare-hypothesis theorem;
- aggregate affine compression is presented as a structural corollary;
- the direct transfer-definition checker is separate from the sharp closed-form implementation;
- closed-form formulas are checked through separate code paths and definition-level transfer enumeration rather than against themselves;
- every printed `PASS` line in the principal verifiers is backed by a computation;
- algebraic identity spot checks are reported separately from theorem-evidence counts;
- the sharp `{5,7,11}` support theorem is backed by full-support pairs differing at exactly one required prime, establishing unique minimum support within `(N,S,supp intersect C)` signatures;
- regression programs are identified as regressions;
- support-necessity witnesses are rigorous positive certificates within the synthesized candidate support, while absence of a witness within a finite bound is explicitly labelled bounded evidence;
- comparison language is generic and makes no historical-priority claim;
- editable repository surfaces are excluded from cryptographic binding;
- software and documentation licensing follow the root license map.
