#!/usr/bin/env python3
"""General critical-support synthesis verifier (revised).

Every PASS line printed by this program is backed by a computation in this
file. Nothing is printed as PASS by declaration.
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
ANCHORS = ((2, 3), (2, 3, 4, 17), (2, 3, 4, 5, 17), (2, 3, 4, 5, 7, 11, 17))


def direct_masked(A0, B0, E):
    """Safe-filler evaluation without the synthesized threshold shortcut."""
    E = C.normalize_context(E); d = C.base_data(A0, B0)
    m = d['m0'] + len(E); total = d['sigma0'] + sum(E)
    for witnesses, forbidden in ((d['exclusive_A'], set(B0)), (d['exclusive_B'], set(A0))):
        q = C.min_safe(forbidden, E)
        for x in witnesses:
            R = (total - x) - (m - 1) * q
            if C.direct_residual_feasible(forbidden, E, q, m - 1, R):
                return False
    return True


# ---------------------------------------------------------------- 1. product twins
def product_twin_definition_level(maxn):
    """Prime Cover + Atom Deficit => no one-sided P-neighbour (definition-level)."""
    alphabet = (2, 3, 5, 7, 11, 13); checks = 0
    for H in ANCHORS:
        A = C.SEED_A + H; B = C.SEED_B + H
        d = C.base_data(A, B)
        assert d['prime_cover'] and d['atom_deficit'], H
        for n in range(maxn + 1):
            for E in itertools.combinations_with_replacement(alphabet, n):
                AE, BE = A + E, B + E
                p = math.prod(AE); m = len(AE)
                assert not GT.one_sided_product(p, m, set(BE), set(AE)), (H, E)
                assert not GT.one_sided_product(p, m, set(AE), set(BE)), (H, E)
                checks += 1
    return checks


# ---------------------------------------------------------------- 2. finite support
def verify_finite_support():
    Bs = ((), (2, 3, 8), (2, 3, 4, 8, 17), (2, 3, 4, 5, 8, 17), (2, 3, 5, 7, 12, 19))
    Es = ((), (2,), (5,), (7, 11), (13, 101), (5, 7, 103), (2, 3, 97, 101))
    checks = 0
    for B in Bs:
        data = C.synthesis_data(B)
        for E in Es:
            q = C.min_safe(B, E); row = data['q_rows'][q]
            for k in (2, 3, 5, 8):
                for R in range(-3, row['C'] + 25):
                    a = C.direct_residual_feasible(B, E, q, k, R)
                    b = C.synthesized_residual_feasible(B, E, k, k * q + R)
                    assert a == b, (B, E, q, k, R, a, b)
                    checks += 1
    return checks


# ---------------------------------------------------------------- 3. multi-anchor
def verify_modules(maxn):
    alphabet = (2, 3, 5, 7, 11, 13, 17, 19, 23, 101); checks = 0
    for H in ANCHORS:
        A = C.SEED_A + H; B = C.SEED_B + H
        for n in range(maxn + 1):
            for E in itertools.combinations_with_replacement(alphabet, n):
                assert direct_masked(A, B, E) == C.synthesized_masked(A, B, E), (H, E)
                checks += 1
    return checks


# ---------------------------------------------------------------- 4. two-filler lemma
def two_filler_separator(B, E, q, k, R):
    """Construct the separator of the Two-Filler Lemma; return the filler list."""
    B = set(B); E = set(E)
    M = max(B | {q, 2}); a = C.odd_permanent_increment(B, q)
    forbidden = B | E
    if q + R not in forbidden:
        return [q + R] + [q] * (k - 1)
    p = q + R
    assert p not in B and C.is_prime(p) and p % 2 == 1, 'lemma case analysis violated'
    return [q + a, p - a] + [q] * (k - 2)


def verify_two_filler_lemma(span):
    """For every residual R in [C_q, C_q+span) build the explicit separator and
    check: correct length, correct sum, at most two nonbaseline fillers, every
    filler >= 2 and outside B union supp(E).  Adversarial contexts contain every
    prime in the residual window, forcing the second branch of the lemma."""
    Bs = ((2, 3, 8), (2, 3, 6), (2, 3, 4, 8, 17), (2, 3, 4, 6, 17), (2, 3, 4, 5, 8, 17),
          (2, 3, 5, 7, 12, 19), (2, 3, 4, 9, 25), (2, 3, 4, 6, 8, 9, 10))
    checks = branch2 = 0
    for B in Bs:
        data = C.synthesis_data(B)
        for q, row in data['q_rows'].items():
            Cq = row['C']
            window = [p for p in range(2, q + Cq + span + 1) if C.is_prime(p)]
            low = [p for p in range(2, q) if C.is_prime(p) and p not in B]
            contexts = [tuple(low), tuple(low) + tuple(p for p in window if p > q)]
            for E in contexts:
                if C.min_safe(B, E) != q:
                    continue
                forbidden = set(B) | set(E)
                for k in (2, 3, 6):
                    for R in range(Cq, Cq + span):
                        fill = two_filler_separator(B, E, q, k, R)
                        assert len(fill) == k
                        assert sum(fill) == k * q + R
                        assert sum(1 for v in fill if v != q) <= 2
                        assert all(v >= 2 and v not in forbidden for v in fill), (B, E, q, R, fill)
                        if q + R in forbidden:
                            branch2 += 1
                        checks += 1
    assert branch2 > 0
    return checks, branch2


# ---------------------------------------------------------------- 5. future stability
def verify_future_stability():
    """All pairs of contexts with equal synthesized signature (within a search
    region) keep equal signature and equal masking under every listed future."""
    alphabet = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    futures = ((), (2,), (3,), (5,), (7,), (11,), (13,), (2, 5, 7), (3, 11, 13), (13, 101))
    checks = pairs = 0
    for H in ANCHORS[:2]:
        A = C.SEED_A + H; B = C.SEED_B + H
        groups = collections.defaultdict(list)
        for n in range(0, 3):
            for E in itertools.combinations_with_replacement(alphabet, n):
                s = C.synthesized_signature(A, B, E)
                groups[(s[0], s[1], s[2])].append(E)
        for g in groups.values():
            for E, F in itertools.combinations(g, 2):
                pairs += 1
                for X in futures:
                    assert C.synthesized_signature(A, B, E + X) == C.synthesized_signature(A, B, F + X)
                    assert C.synthesized_masked(A, B, E + X) == C.synthesized_masked(A, B, F + X)
                    checks += 1
    assert pairs > 0
    return pairs, checks


# ---------------------------------------------------------------- 6. arity boundary
def verify_arity_boundary():
    """(a) Distinct equal-sum/equal-product pairs of arity <=2 do not exist, so
    m0>=3 is automatic; (b) every module context has k=m-1>=2 filler slots."""
    checks = 0
    for s in range(4, 120):
        seen = {}
        for a in range(2, s // 2 + 1):
            b = s - a
            key = a * b
            assert key not in seen, ('arity-2 collision', s, a, seen.get(key))
            seen[key] = a
            checks += 1
    for H in ANCHORS:
        m0 = len(C.SEED_A + H)
        assert m0 >= 3 and m0 - 1 >= 2
        checks += 1
    return checks


# ---------------------------------------------------------------- 7. sharp binding
def verify_sharp_binding():
    """Compute (not declare) that the two fixed modules satisfy the hypotheses,
    and record that the bare seed does not satisfy Prime Cover."""
    out = []
    for H in (C.ANCHOR4, C.ANCHOR5):
        d = C.base_data(C.SEED_A + H, C.SEED_B + H)
        assert d['prime_cover'] and d['atom_deficit']
        out.append((H, d['omega0'], 2 * d['m0']))
    seed = C.base_data(C.SEED_A, C.SEED_B)
    assert not seed['prime_cover'], 'seed is expected to fail Prime Cover'
    return out


def run(deep=False):
    pt = product_twin_definition_level(3 if deep else 2)
    finite = verify_finite_support()
    mods = verify_modules(3 if deep else 2)
    tf, tf2 = verify_two_filler_lemma(120 if deep else 40)
    fpairs, fut = verify_future_stability()
    ar = verify_arity_boundary()
    sb = verify_sharp_binding()
    rows = [
        ('product_twin_definition_level', f'PASS:checks={pt}:definition_level_no_one_sided_P_neighbour'),
        ('finite_critical_support_reduction', f'PASS:direct_vs_synthesized={finite}'),
        ('multi_anchor_exact_synthesis', f'PASS:checks={mods}'),
        ('two_filler_eventual_separator', f'PASS:explicit_separators={tf}:second_branch_cases={tf2}'),
        ('future_stable_signature', f'PASS:equal_signature_pairs={fpairs}:future_checks={fut}'),
        ('arity_boundary', f'PASS:checks={ar}:no_distinct_arity2_pairs:k>=2'),
        ('sharp_instance_binding', 'PASS:' + ';'.join(f'anchor={h}:Omega={o}<2m0={t}' for h, o, t in sb) + ':bare_seed_fails_prime_cover'),
    ]
    print(f'SAOR general critical-support synthesis verifier v{VERSION}')
    for k, v in rows:
        print(f'{k}:{v}')
    print(f'TOTAL {len(rows)}/{len(rows)} PASS')


def main():
    p = argparse.ArgumentParser(); p.add_argument('--self-test', action='store_true'); p.add_argument('--verify', action='store_true')
    a = p.parse_args(); run(a.verify)


if __name__ == '__main__':
    main()
