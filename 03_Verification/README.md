# SAOR Verification

The verification suite separates theorem checks, definition-level checks, proof consistency, regressions, and package integrity.

## Principal theorem checks

- `Principal/saor_general_critical_support_synthesis_verifier_v1_3_0.py`
- `Principal/saor_sharp_support_sensitive_classifier_verifier_v1_3_0.py`
- `Principal/saor_anchored_cone_corollary_verifier_v1_3_0.py`
- `Principal/saor_support_necessity_verifier_v1_3_0.py`

These programs check theorem formulas, safe-filler reductions, multiple base-anchor systems, explicit Two-Filler constructions, future-stability identities, the Anchored-Cone Corollary, sharp critical-support witnesses, constructive future separators, and support-necessity certificates.

Every printed `PASS` line in these principal verifiers is backed by an actual computation.

## Definition-level transfer checks

- `Definition_Level/saor_direct_transfer_definition_verifier_v1_3_0.py`
- `Definition_Level/saor_definition_level_lib.py`

These construct one-sided equal-sum and equal-product candidates directly from the transfer definitions. The library imports nothing from `saor_core`; principal verifiers use it to check sharp formulas, constructive separators, anchored-cone cases, and support-necessity certificates.

## Proof consistency audit

- `Proof_Audit/saor_cross_proof_consistency_audit_v1_3_0.py`

This audit checks fixed module hypotheses and machine-record consistency. Its algebraic identity loops are reported separately as spot checks of identities implied by algebra; they are not presented as evidence counts for the masking theorems. Scope declarations are metadata rather than computational tests.

## Regression suite

Regression programs preserve established compatibility properties. They are regression guards, not standalone proofs of the principal theorem.
