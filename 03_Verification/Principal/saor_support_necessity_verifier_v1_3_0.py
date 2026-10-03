#!/usr/bin/env python3
"""Critical-support necessity verifier.

1. The state classifier f(N,S,T) used by the extractor agrees with the
   closed-form sharp laws on the fixed modules.
2. Run blind on the fixed modules, the extractor certifies exactly {5,7}
   (module 4) and {5,7,11} (module 5), agreeing with the separately proved unique-minimum
   support of the sharp theorem.
3. Every certificate (fixed modules and a sample of anchored pairs) is
   re-checked against the definition-level verification.
"""
from __future__ import annotations
import argparse, collections, itertools, math, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '02_Algorithms_and_Software'))
sys.path.insert(0, str(ROOT / '03_Verification' / 'Definition_Level'))
import saor_core as C
import saor_support_necessity as M
import saor_definition_level_lib as GT

VERSION = '1.3.0'


def classifier_agreement():
    pc4 = M.PairClassifier(C.SEED_A + C.ANCHOR4, C.SEED_B + C.ANCHOR4)
    pc5 = M.PairClassifier(C.SEED_A + C.ANCHOR5, C.SEED_B + C.ANCHOR5)
    n = 0
    for k in range(5):
        for E in itertools.combinations_with_replacement((2, 3, 5, 7, 11, 13, 17, 19, 23, 101), k):
            assert pc4.masked(E) == C.masked4(E) and pc5.masked(E) == C.masked5(E), E
            n += 1
    return n


def gt_check(A0, B0, result):
    n = 0
    for p, (G, Gp) in result['witnesses'].items():
        assert len(G) == len(Gp) and sum(G) == sum(Gp)
        assert (p in G) != (p in Gp)
        assert GT.direct_masked(A0 + G, B0 + G) != GT.direct_masked(A0 + Gp, B0 + Gp), (A0, p, G, Gp)
        n += 1
    return n


def fixed_modules():
    out = {}; checks = 0
    for name, H in (('module4', C.ANCHOR4), ('module5', C.ANCHOR5)):
        A0, B0 = C.SEED_A + H, C.SEED_B + H
        r = M.extract_support_necessity(A0, B0)
        checks += gt_check(A0, B0, r)
        out[name] = r['certified_necessary']
    assert out['module4'] == (5, 7), out
    assert out['module5'] == (5, 7, 11), out
    assert tuple(sorted(set(out['module4']) | set(out['module5']))) == (5, 7, 11)
    return out, checks


def anchored_sample(limit, n_max):
    pairs = []
    groups = collections.defaultdict(list)
    for t in itertools.combinations_with_replacement(range(2, 21), 3):
        groups[(sum(t), math.prod(t))].append(t)
    for g in groups.values():
        pairs += list(itertools.combinations(g, 2))
    pairs = pairs[:limit]
    certs = 0
    for a, b in pairs:
        H = M.canonical_anchor(a, b)
        A0, B0 = a + H, b + H
        r = M.extract_support_necessity(A0, B0, n_max=n_max)
        certs += gt_check(A0, B0, r)
    return len(pairs), certs


def run(deep=False):
    n = classifier_agreement()
    mods, c1 = fixed_modules()
    np_, c2 = anchored_sample(6 if deep else 4, 10)
    print(f'SAOR critical-support necessity verifier v{VERSION}')
    print(f'state_classifier_vs_closed_form:PASS:contexts={n}')
    print(f'fixed_modules_blind_extraction:PASS:module4={mods["module4"]}:module5={mods["module5"]}:joint=(5,7,11)')
    print(f'certificates_vs_definition_level:PASS:fixed={c1}:anchored_pairs={np_}:anchored_certificates={c2}')
    print('TOTAL 3/3 PASS')


def main():
    p = argparse.ArgumentParser(); p.add_argument('--self-test', action='store_true'); p.add_argument('--verify', action='store_true')
    a = p.parse_args(); run(a.verify)


if __name__ == '__main__':
    main()
