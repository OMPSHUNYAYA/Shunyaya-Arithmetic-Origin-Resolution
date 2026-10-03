#!/usr/bin/env python3
"""Critical-support necessity extraction for admissible SAOR base pairs.

Given a base pair satisfying Prime Cover and Atom Deficit, the general
synthesis theorem gives a finite candidate set Crit such that the masking
state is a function f(N, S, T) of N=N(E), S=S(E) and T=supp(E) intersect Crit.
This module searches for certified necessary support coordinates inside Crit.

Certified necessity (rigorous)
    p in Crit is NECESSARY when there are realizable states (N,S,T) and
    (N,S,T+{p}), with p not in T, such that f differs. Both states are then
    realized by explicit prime contexts G and G'. These have equal N and S,
    equal bits on Crit\\{p}, and different masking. So every classifier
    whose support coordinates are chosen from the synthesized candidate Crit
    must record p. Witness
    contexts are returned and can be re-checked against the definition-level verification.

Bounded non-necessity (evidence)
    For p without a certificate, no witness exists with N <= n_max and
    |T| <= t_max. This is reported as a bound, not a proof.

Search method
    The search runs over abstract states, not concrete contexts. Only S
    values whose residual falls in a low window [0, C_q) can make f depend
    on support, so for each (N, T) only a few S values are tried. Each
    candidate state is checked for realizability by a dynamic program over
    the allowed primes: every prime of T (or T+{p}) appears at least once,
    no other prime of Crit appears, and any prime outside Crit may appear.
"""
from __future__ import annotations
import argparse, collections, csv, functools, itertools, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import saor_core as C


def _primes_upto(n):
    return [p for p in range(2, n + 1) if C.is_prime(p)]


@functools.lru_cache(maxsize=None)
def _feasible(window: frozenset, q: int, k: int, R: int) -> bool:
    """Can R be written as a sum of at most k increments r>=1 with q+r not in window?"""
    if R < 0:
        return False
    if R == 0:
        return True
    k = min(k, R)                         # at most R nonbaseline slots are ever needed

    @functools.lru_cache(maxsize=None)
    def go(rem, slots, lo):
        if rem == 0:
            return True
        if slots == 0:
            return False
        for r in range(lo, rem + 1):
            if q + r in window:
                continue
            if go(rem - r, slots - 1, r):
                return True
        return False
    return go(R, k, 1)


class PairClassifier:
    """Exact masking evaluator f(N,S,T) for one admissible base pair."""

    def __init__(self, A0, B0):
        d = C.base_data(A0, B0)
        if not (d['prime_cover'] and d['atom_deficit']):
            raise ValueError('Prime Cover and Atom Deficit required')
        self.A0, self.B0, self.d = tuple(A0), tuple(B0), d
        self.dirs = []
        for witnesses, forb in ((d['exclusive_A'], frozenset(B0)), (d['exclusive_B'], frozenset(A0))):
            data = C.synthesis_data(forb)
            self.dirs.append((tuple(sorted(witnesses)), forb, data))
        crit = set()
        for _, _, data in self.dirs:
            crit |= set(data['critical_primes'])
        self.crit = tuple(sorted(crit))
        self.L = max(data['critical_bound'] for _, _, data in self.dirs)

    def _q(self, forb, T):
        q = 2
        while q in forb or q in T:
            q += 1
        return q

    def masked_state(self, N: int, S: int, T: frozenset) -> bool:
        k = self.d['m0'] + N - 1; total = self.d['sigma0'] + S
        for witnesses, forb, data in self.dirs:
            q = self._q(forb, T)
            Cq = data['q_rows'][q]['C']
            for x in witnesses:
                R = total - x - k * q
                if R < 0:
                    continue
                if R >= Cq:
                    return False
                window = frozenset(v for v in (forb | T) if q < v <= q + R)
                if _feasible(window, q, k, R):
                    return False
        return True

    def masked(self, E) -> bool:
        E = C.normalize_context(E)
        return self.masked_state(len(E), sum(E), frozenset(p for p in set(E) if p in self.crit))

    def interesting_S(self, N: int, T: frozenset):
        """S values for which some residual lies in its low window."""
        k = self.d['m0'] + N - 1; out = set()
        for witnesses, forb, data in self.dirs:
            q = self._q(forb, T)
            Cq = data['q_rows'][q]['C']
            for x in witnesses:
                base = x + k * q - self.d['sigma0']
                out.update(range(base - 1, base + Cq + 1))
        return out


class Realizer:
    """Find a prime multiset with |E|=N, sum S, supp(E) intersect Crit == M."""

    def __init__(self, crit, smax):
        self.crit = frozenset(crit)
        self.free = tuple(p for p in _primes_upto(max(smax, 2)) if p not in self.crit)

    def realize(self, N, S, M):
        M = tuple(sorted(M))
        n_rest = N - len(M); s_rest = S - sum(M)
        if n_rest < 0 or s_rest < 0:
            return None
        allowed = tuple(sorted(set(self.free) | set(M)))

        @functools.lru_cache(maxsize=None)
        def go(n, s, i):
            if n == 0:
                return () if s == 0 else None
            if i >= len(allowed):
                return None
            p = allowed[i]
            if p * n > s:
                return None
            r = go(n - 1, s - p, i)     # use p (again)
            if r is not None:
                return (p,) + r
            return go(n, s, i + 1)      # skip p
        r = go(n_rest, s_rest, 0)
        return None if r is None else tuple(sorted(M + r))


def extract_support_necessity(A0, B0, n_max=30, t_max=None):
    """Return candidate Crit, certified-necessary primes with witnesses, and
    primes for which no witness exists within the stated bound."""
    pc = PairClassifier(A0, B0)
    crit = pc.crit
    t_max = len(crit) if t_max is None else t_max
    smax = (max(q for _, _, data in pc.dirs for q in data['q_rows']) + 1) * (pc.d['m0'] + n_max) + pc.L + 50
    rz = Realizer(crit, smax)
    witnesses = {}
    for p in crit:
        others = [c for c in crit if c != p]
        found = None
        for N in range(1, n_max + 1):
            for size in range(0, min(t_max, N - 1, len(others)) + 1):
                for Tt in itertools.combinations(others, size):
                    T = frozenset(Tt); Tp = T | {p}
                    for S in sorted(pc.interesting_S(N, T) | pc.interesting_S(N, Tp)):
                        if S < 2 * N:
                            continue
                        if pc.masked_state(N, S, T) == pc.masked_state(N, S, Tp):
                            continue
                        G = rz.realize(N, S, T); Gp = rz.realize(N, S, Tp)
                        if G is None or Gp is None:
                            continue
                        assert pc.masked(G) != pc.masked(Gp)
                        found = (G, Gp)
                        break
                    if found: break
                if found: break
            if found: break
        if found:
            witnesses[p] = found
    necessary = tuple(p for p in crit if p in witnesses)
    return {
        'pair': (tuple(A0), tuple(B0)),
        'candidate_crit': crit,
        'certified_necessary': necessary,
        'no_witness_within_bound': tuple(p for p in crit if p not in witnesses),
        'witnesses': {p: witnesses[p] for p in necessary},
        'search_bound': {'n_max': n_max, 't_max': t_max},
    }


def canonical_anchor(a, b):
    d = C.base_data(a, b)
    U = tuple(sorted(p for p in d['prime_divisors'] if not (p in a and p in b)))
    t0 = max(0, d['omega0'] - 2 * d['m0'] + 1)
    return U + (2,) * max(0, t0 - len(U))


def survey(regions, out_csv, n_max=30):
    """Anchor every equal-sum/equal-product pair in the regions with its
    canonical anchor (Anchored-Cone Corollary) and search for necessary support coordinates."""
    rows = []
    for m, maxv in regions:
        groups = collections.defaultdict(list)
        for t in itertools.combinations_with_replacement(range(2, maxv + 1), m):
            groups[(sum(t), math.prod(t))].append(t)
        for g in groups.values():
            for a, b in itertools.combinations(g, 2):
                H = canonical_anchor(a, b)
                r = extract_support_necessity(a + H, b + H, n_max=n_max)
                rows.append({
                    'A0': ' '.join(map(str, a)), 'B0': ' '.join(map(str, b)),
                    'anchor': ' '.join(map(str, H)),
                    'candidate_crit': ' '.join(map(str, r['candidate_crit'])),
                    'certified_necessary_support': ' '.join(map(str, r['certified_necessary'])),
                    'no_witness_within_bound': ' '.join(map(str, r['no_witness_within_bound'])),
                    'candidate_size': len(r['candidate_crit']),
                    'certified_size': len(r['certified_necessary']),
                    'n_max': n_max,
                })
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator='\n')
        w.writeheader(); w.writerows(rows)
    return rows


def main():
    ap = argparse.ArgumentParser(description='SAOR critical-support necessity extraction')
    ap.add_argument('--pair', nargs=2, metavar=('A0', 'B0'), help='comma-separated roots, e.g. 2,6,6,2,3 3,3,8,2,3')
    ap.add_argument('--n-max', type=int, default=30)
    ap.add_argument('--survey', metavar='CSV', help='write the anchored survey table to CSV')
    a = ap.parse_args()
    if a.survey:
        rows = survey(((3, 20), (4, 12)), a.survey, n_max=a.n_max)
        print(f'survey rows={len(rows)} -> {a.survey}')
    elif a.pair:
        A0 = tuple(int(x) for x in a.pair[0].split(',')); B0 = tuple(int(x) for x in a.pair[1].split(','))
        r = extract_support_necessity(A0, B0, n_max=a.n_max)
        for k, v in r.items():
            print(f'{k}: {v}')
    else:
        ap.print_help()


if __name__ == '__main__':
    main()
