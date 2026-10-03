#!/usr/bin/env python3
"""Anchored-Cone Corollary verifier.

Checks, for EVERY distinct equal-sum/equal-product pair in a finite search
region (not only pairs that already satisfy Prime Cover and Atom Deficit):

  1. the canonical anchor H = U + (2,)*t0 makes the anchored pair satisfy
     Prime Cover and Atom Deficit (U = uncovered prime divisors,
     t0 = max(0, Omega(P0) - 2*m0 + 1 - |U|));
  2. the general synthesized classifier on the anchored pair agrees with the
     definition-level verification for every listed prime context;
  3. no one-sided P-neighbour exists anywhere on the cone (definition-level verification);
  4. sharpness of the atom threshold in explicit examples: one-sided
     P-neighbours exist below the threshold and vanish at it;
  5. how rare the original hypotheses are without anchoring (reported census).
"""
from __future__ import annotations
import argparse, collections, itertools, math, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '02_Algorithms_and_Software'))
sys.path.insert(0, str(ROOT / '03_Verification' / 'Definition_Level'))
import saor_core as C
import saor_definition_level_lib as GT

VERSION = '1.3.0'


def equal_projection_pairs(m, maxv):
    groups = collections.defaultdict(list)
    for t in itertools.combinations_with_replacement(range(2, maxv + 1), m):
        groups[(sum(t), math.prod(t))].append(t)
    for g in groups.values():
        yield from itertools.combinations(g, 2)


def canonical_anchor(A0, B0):
    d = C.base_data(A0, B0)
    U = tuple(sorted(p for p in d['prime_divisors'] if not (p in A0 and p in B0)))
    t0 = max(0, d['omega0'] - 2 * d['m0'] + 1)
    extra = max(0, t0 - len(U))
    return U, t0, U + (2,) * extra


def census(regions):
    rows = []
    for m, maxv in regions:
        tot = pc = ad = both = 0
        for a, b in equal_projection_pairs(m, maxv):
            d = C.base_data(a, b); tot += 1
            pc += d['prime_cover']; ad += d['atom_deficit']; both += d['prime_cover'] and d['atom_deficit']
        rows.append((m, maxv, tot, pc, ad, both))
    return rows


def cone_agreement(regions, maxn):
    alphabet = (2, 3, 5, 7, 11)
    pairs = cases = 0
    for m, maxv in regions:
        for a, b in equal_projection_pairs(m, maxv):
            U, t0, H = canonical_anchor(a, b)
            A, B = a + H, b + H
            d = C.base_data(A, B)
            assert d['prime_cover'] and d['atom_deficit'], (a, b, H)
            pairs += 1
            for n in range(maxn + 1):
                for E in itertools.combinations_with_replacement(alphabet, n):
                    rep = GT.masking_report(A + E, B + E)
                    assert not rep['P_one_sided_A'] and not rep['P_one_sided_B'], (a, b, H, E)
                    assert (not any(rep.values())) == C.synthesized_masked(A, B, E), (a, b, H, E)
                    cases += 1
    return pairs, cases


def atom_threshold_examples():
    """Anchored-by-U pairs with Atom Deficit failing. Proved: no one-sided
    P-neighbour for N >= t, where t = Omega(P0)-2m0+1 for the U-anchored pair.
    Reported: whether one-sided P-neighbours exist at N = t-1 (sharpness)."""
    examples = [((2, 18, 24), (3, 9, 32)), ((6, 18, 32), (8, 12, 36)), ((12, 30, 54), (18, 18, 60))]
    out = []
    for a, b in examples:
        assert sum(a) == sum(b) and math.prod(a) == math.prod(b)
        U = tuple(sorted(C.prime_divisors(math.prod(a))))
        A, B = a + U, b + U
        d = C.base_data(A, B)
        assert d['prime_cover'] and not d['atom_deficit']
        t = d['omega0'] - 2 * d['m0'] + 1
        row = []
        for N in range(0, t + 2):
            E = (2,) * N
            rep = GT.masking_report(A + E, B + E)
            row.append(rep['P_one_sided_A'] or rep['P_one_sided_B'])
        assert row[0], (a, b, 'expected a one-sided P-neighbour at N=0')
        assert not any(row[t:]), (a, b, t, row)
        out.append((a, b, t, row[t - 1]))
    return out


def uncovered_prime_example():
    """The bare seed fails Prime Cover. Report the exact empty-context
    one-sided-neighbour flags. The explicit assertions also guard simple-graph
    self-vertex exclusion for disjoint-support roots."""
    rep = GT.masking_report(C.SEED_A, C.SEED_B)
    assert rep == {
        'P_one_sided_A': True,
        'P_one_sided_B': False,
        'S_one_sided_A': True,
        'S_one_sided_B': True,
    }, rep
    return rep


def run(deep=False):
    regions_census = ((3, 30), (4, 18), (5, 12))
    regions_cone = ((3, 20), (4, 12)) if not deep else ((3, 26), (4, 14))
    cen = census(regions_census)
    pairs, cases = cone_agreement(regions_cone, 1 if not deep else 2)
    thr = atom_threshold_examples()
    seed = uncovered_prime_example()
    print(f'SAOR anchored-cone corollary verifier v{VERSION}')
    for m, maxv, tot, pc, ad, both in cen:
        print(f'census:arity={m}:values<={maxv}:pairs={tot}:prime_cover={pc}:atom_deficit={ad}:both={both}')
    print(f'canonical_anchor_makes_every_pair_admissible:PASS:pairs={pairs}')
    print(f'cone_classifier_vs_definition_level:PASS:cases={cases}:no_one_sided_P_neighbour')
    print(f'atom_threshold_sufficient:PASS:examples={len(thr)}:' + ';'.join(f'{a}/{b}:t={t}:sharp={s}' for a, b, t, s in thr))
    print(f'info:bare_seed_empty_context_one_sided={seed}')
    print('TOTAL 3/3 PASS')


def main():
    p = argparse.ArgumentParser(); p.add_argument('--self-test', action='store_true'); p.add_argument('--verify', action='store_true')
    a = p.parse_args(); run(a.verify)


if __name__ == '__main__':
    main()
