# SAOR Verification Scope v1.3.0

Executable verification supports, but does not replace, the written proof.

The suite includes:

- direct transfer-definition construction for the sharp theorem;
- a separate definition-level library used to check sharp formulas, constructive separators, anchored-cone cases, and support-necessity certificates;
- explicit construction of Two-Filler separators over residual windows, including adversarial contexts;
- symbolic checking of the support-sensitive formulas;
- exact safe-filler comparison against the synthesized classifier;
- multiple admissible base-anchor modules;
- future-signature stability checks;
- Anchored-Cone Corollary checks over bounded pair censuses;
- algebraic proof-consistency audits;
- compatibility regressions;
- repository-integrity checks.

The definition-level transfer programs do not import or call the sharp closed-form masking functions from the reference implementation.

Finite enumeration and bounded support-necessity searches are evidence only for the regions they state. General theorem claims rely on the written proofs, not on extrapolation from those finite searches.
