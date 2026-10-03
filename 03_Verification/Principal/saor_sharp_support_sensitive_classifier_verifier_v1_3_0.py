#!/usr/bin/env python3
"""Sharp support-sensitive classifier verifier (revised).

The closed-form sharp classifier (saor_core.masked4 / masked5) is compared with
two evaluations that do not use it:

  * SYN - the general safe-filler classifier (saor_core.synthesized_masked),
          a separate code path derived from the general theorem;
  * GT  - the definition-level transfer verifier (saor_definition_level_lib), which
          enumerates one-sided P- and S-neighbours and imports nothing from
          saor_core.

Constructive separators are checked against SYN for every pair and against GT
whenever the separated contexts are small enough for direct enumeration.
"""
from __future__ import annotations
import argparse, itertools, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '02_Algorithms_and_Software'))
sys.path.insert(0, str(ROOT / '03_Verification' / 'Definition_Level'))
import saor_core as C
import saor_definition_level_lib as GT

VERSION = '1.3.0'
MODULES = {4: C.ANCHOR4, 5: C.ANCHOR5}
GT_MAX_CONTEXT = 8


def syn_joint(E):
    E = C.normalize_context(E)
    return tuple(C.synthesized_masked(C.SEED_A + MODULES[j], C.SEED_B + MODULES[j], E) for j in (4, 5))


def gt_joint(E):
    E = tuple(C.normalize_context(E))
    return tuple(GT.direct_masked(C.SEED_A + MODULES[j] + E, C.SEED_B + MODULES[j] + E) for j in (4, 5))


def formula_audit(maxn_syn, maxn_gt):
    """Closed form vs SYN on a wide alphabet; closed form vs GT on a smaller one."""
    syn_alpha = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 101)
    gt_alpha = (2, 3, 5, 7, 11, 13, 17, 19, 31, 101)
    syn = gtc = 0
    for n in range(maxn_syn + 1):
        for E in itertools.combinations_with_replacement(syn_alpha, n):
            assert C.joint_status(E) == syn_joint(E), ('SYN', E)
            syn += 1
    for n in range(maxn_gt + 1):
        for E in itertools.combinations_with_replacement(gt_alpha, n):
            assert C.joint_status(E) == gt_joint(E), ('GT', E)
            gtc += 1
    return syn, gtc


def prime5_escape():
    E = (3, 7); F = (5, 5)
    assert C.stats(E) == C.stats(F) == (2, 10)
    assert (C.D4(E), C.D5(E)) == (C.D4(F), C.D5(F)) == (-1, 4)
    assert gt_joint(E) == (True, False)
    assert gt_joint(F) == (True, True)
    return 1


def support_necessity():
    """Unique-minimum witnesses for the support coordinates.

    Each pair has equal (N,S), and its full prime supports differ only at the
    displayed prime. A common future context then gives different joint
    masking states. Therefore any complete signature of the form
    (N,S,supp(E) intersect C) must contain that prime.
    """
    cases = {
        5: ((3, 5, 5, 7), (3, 3, 7, 7), ()),
        7: ((3, 3, 5, 7), (3, 5, 5, 5), (3, 3, 3, 11)),
        11: ((3, 3, 7, 11), (3, 7, 7, 7), (3, 5, 17)),
    }
    for prime, (E, F, X) in cases.items():
        assert C.stats(E) == C.stats(F)
        assert set(E) ^ set(F) == {prime}, (prime, E, F)
        bE = C.support_bits(E); bF = C.support_bits(F); idx = {5: 0, 7: 1, 11: 2}[prime]
        assert [i for i in range(3) if bE[i] != bF[i]] == [idx]
        assert gt_joint(E + X) != gt_joint(F + X), (prime, E, F, X)
    return len(cases)


def no_prime_at_least_13_matters():
    """Swapping a prime >=13 for another prime >=13 with the same value of p
    never matters; equivalently, equal-K pairs that differ only in primes >=13
    have equal SYN status under futures (spot check over a region)."""
    big = (13, 17, 19, 23, 29, 31, 37, 41, 43)
    checks = 0
    for E, F in itertools.combinations(itertools.combinations_with_replacement(big, 2), 2):
        if sum(E) != sum(F):
            continue
        for X in ((), (2,), (3,), (5,), (7,), (5, 7), (5, 7, 11), (2, 2, 5, 7), (3, 3, 5, 7, 11)):
            assert syn_joint(E + X) == syn_joint(F + X)
            checks += 1
    assert checks > 0
    return checks


def additivity_or_checks():
    contexts = ((), (2,), (5,), (7,), (11,), (2, 5, 13), (3, 7, 17)); checks = 0
    for E in contexts:
        for F in contexts:
            assert C.D4(E + F) == C.D4(E) + sum(p - 4 for p in F)
            assert C.D5(E + F) == C.D5(E) + sum(p - 5 for p in F)
            bE = C.support_bits(E); bF = C.support_bits(F); b = C.support_bits(E + F)
            assert b == tuple(x or y for x, y in zip(bE, bF)); checks += 1
    return checks


def future_classifier_audit(maxn):
    alphabet = (2, 3, 5, 7, 11, 13)
    contexts = [()]
    for n in range(1, maxn + 1):
        contexts.extend(itertools.combinations_with_replacement(alphabet, n))
    futures = ((), (2,), (3,), (5,), (7,), (11,), (2, 5, 7), (3, 11, 13))
    pairs = sep_syn = sep_gt = equal_checks = 0
    E0, F0 = (13, 23), (17, 19)
    assert C.sharp_signature(E0) == C.sharp_signature(F0)
    for i, E in enumerate(contexts):
        for F in contexts[i + 1:]:
            pairs += 1
            if C.sharp_signature(E) == C.sharp_signature(F):
                for X in futures:
                    assert syn_joint(C.compose(E, X)) == syn_joint(C.compose(F, X))
                    equal_checks += 1
                continue
            axis, X = C.sharp_future_separator(E, F)
            EX, FX = C.compose(E, X), C.compose(F, X)
            assert syn_joint(EX) != syn_joint(FX), (E, F, X)
            sep_syn += 1
            if max(len(EX), len(FX)) <= GT_MAX_CONTEXT:
                assert gt_joint(EX) != gt_joint(FX), (E, F, X)
                sep_gt += 1
    for X in futures:
        assert syn_joint(C.compose(E0, X)) == syn_joint(C.compose(F0, X))
        equal_checks += 1
    return pairs, sep_syn, sep_gt, equal_checks


def run(deep=False):
    syn, gtc = formula_audit(4 if deep else 3, 4 if deep else 2)
    esc = prime5_escape(); nec = support_necessity(); big = no_prime_at_least_13_matters()
    act = additivity_or_checks(); pairs, ss, sg, eq = future_classifier_audit(3 if deep else 2)
    rows = [
        ('closed_form_vs_general_synthesis', f'PASS:contexts={syn}'),
        ('closed_form_vs_definition_level', f'PASS:contexts={gtc}'),
        ('prime5_escape', f'PASS:checks={esc}:definition_level'),
        ('critical_support_unique_minimum', f'PASS:witnesses={nec}:support=(5,7,11):single_prime_support_differences:definition_level'),
        ('primes_at_least_13_irrelevant', f'PASS:checks={big}'),
        ('mixed_context_action', f'PASS:checks={act}'),
        ('complete_future_classifier', f'PASS:pairs={pairs}:separators_vs_synthesis={ss}:separators_vs_definition_level={sg}:equal_signature_future_checks={eq}'),
    ]
    print(f'SAOR sharp support-sensitive classifier verifier v{VERSION}')
    for k, v in rows:
        print(f'{k}:{v}')
    print(f'TOTAL {len(rows)}/{len(rows)} PASS')


def main():
    p = argparse.ArgumentParser(); p.add_argument('--self-test', action='store_true'); p.add_argument('--verify', action='store_true')
    a = p.parse_args(); run(a.verify)


if __name__ == '__main__':
    main()
