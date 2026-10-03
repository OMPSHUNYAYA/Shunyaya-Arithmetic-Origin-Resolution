# SAOR Verification Evidence Report v1.3.0

The verification architecture separates four evidence types.

## 1. Definition-level transfer checks

The direct transfer verifier constructs one-sided equal-sum and equal-product candidates directly from the transfer definitions. In complete mode it checks `6006` fixed-module/context cases over contexts of size at most `5` from a ten-prime alphabet that includes the large prime `101`.

The reusable definition-level library imports nothing from `saor_core`, explicitly excludes the root itself as required for simple transfer graphs, and is also used to check selected sharp-formula cases, constructive future separators, anchored-cone cases, and support-necessity certificates.

## 2. Theorem-form checks

Principal verifiers check the general safe-filler reduction, multiple anchors, explicit Two-Filler constructions, future-stable signatures, the Anchored-Cone Corollary, sharp support-sensitive formulas, the three single-prime-difference witnesses establishing unique minimum support `{5,7,11}`, and constructive future separators.

The sharp closed form is checked through the general synthesized classifier and through the separate definition-level transfer library.

## 3. Consistency and regression checks

The proof consistency audit checks fixed hypotheses and machine records. Algebraic identity loops are reported as spot checks of identities implied by algebra and are not counted as independent theorem evidence.

Regression programs preserve established compatibility properties and are not presented as proofs of the principal results.

## 4. Package integrity

The root verifier checks required files, the declared package inventory, local Markdown links, UTF-8/LF normalization, and SHA-256 hashes for the bound scientific core. Common environment/VCS clutter is ignored; unexpected substantive extra files warn rather than fail. Missing declared files and scientific hash mismatches remain failures. Editable presentation, legal, configuration, example, survey, and evidence-prose files are deliberately excluded from cryptographic binding.
