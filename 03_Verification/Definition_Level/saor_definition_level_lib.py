#!/usr/bin/env python3
"""Definition-level transfer verification for SAOR masking.

This module is written directly from the transfer definitions in
01_Theory/SAOR_Definitions_and_Transfer_Semantics_v1_3_0.md and does NOT import
saor_core. It decides, for two equal-arity realizations A and B, whether a
realization exists that is adjacent to one root and not to the other in the
P-transfer graph (equal product, shared value) or the S-transfer graph (equal
sum, shared value).

A one-sided neighbour of A must
  * have the same arity and the same product (P) or sum (S) as A,
  * share at least one value with A,
  * share no value with B (otherwise it would also be adjacent to B),
  * be different from A itself, because the transfer graphs are simple.

The self-vertex exclusion is checked explicitly. This matters for roots with
disjoint factor-value supports, where A itself can otherwise satisfy the
share-A / avoid-B value conditions.

The search is a memoized depth-first enumeration of nondecreasing value
sequences, so it scales to contexts containing large primes.
"""
from __future__ import annotations
import functools, math

__all__ = ["one_sided_sum", "one_sided_product", "masking_report", "direct_masked"]


def _divisors(n: int):
    small, large = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
        i += 1
    return small + large[::-1]


def one_sided_sum(total: int, m: int, forbidden, shared, exclude_root=None) -> bool:
    """True iff some m-multiset of integers >=2 with sum `total` avoids
    `forbidden`, contains at least one value from `shared`, and is not the
    optional `exclude_root` self vertex."""
    forbidden = frozenset(forbidden); shared = frozenset(shared)
    root = tuple(sorted(exclude_root)) if exclude_root is not None else None
    if root is not None and len(root) != m:
        raise ValueError("exclude_root arity mismatch")

    @functools.lru_cache(maxsize=None)
    def go(rem: int, k: int, lo: int, has: bool, differs: bool) -> bool:
        if k == 0:
            return rem == 0 and has and (root is None or differs)
        if lo * k > rem:
            return False
        idx = m - k
        for v in range(lo, rem // k + 1):
            if v in forbidden:
                continue
            new_differs = differs or (root is not None and v != root[idx])
            if go(rem - v, k - 1, v, has or v in shared, new_differs):
                return True
        return False

    return go(total, m, 2, False, False)


def one_sided_product(prod: int, m: int, forbidden, shared, exclude_root=None) -> bool:
    """True iff some m-multiset of integers >=2 with product `prod` avoids
    `forbidden`, contains at least one value from `shared`, and is not the
    optional `exclude_root` self vertex."""
    forbidden = frozenset(forbidden); shared = frozenset(shared)
    root = tuple(sorted(exclude_root)) if exclude_root is not None else None
    if root is not None and len(root) != m:
        raise ValueError("exclude_root arity mismatch")

    @functools.lru_cache(maxsize=None)
    def go(rem: int, k: int, lo: int, has: bool, differs: bool) -> bool:
        if k == 0:
            return rem == 1 and has and (root is None or differs)
        idx = m - k
        if k == 1:
            if rem < lo or rem in forbidden or not (has or rem in shared):
                return False
            return root is None or differs or rem != root[idx]
        for d in _divisors(rem):
            if d < max(lo, 2):
                continue
            if d ** k > rem:
                break
            if d in forbidden:
                continue
            new_differs = differs or (root is not None and d != root[idx])
            if go(rem // d, k - 1, d, has or d in shared, new_differs):
                return True
        return False

    return go(prod, m, 2, False, False)


def masking_report(A, B) -> dict:
    """Return the four one-sided-neighbour existence flags for roots A, B."""
    A = tuple(A); B = tuple(B)
    if len(A) != len(B):
        raise ValueError("equal arity required")
    m = len(A); s = sum(A); p = math.prod(A)
    if s != sum(B) or p != math.prod(B):
        raise ValueError("equal sum and product required")
    sa, sb = set(A), set(B)
    return {
        "P_one_sided_A": one_sided_product(p, m, sb, sa, exclude_root=A),
        "P_one_sided_B": one_sided_product(p, m, sa, sb, exclude_root=B),
        "S_one_sided_A": one_sided_sum(s, m, sb, sa, exclude_root=A),
        "S_one_sided_B": one_sided_sum(s, m, sa, sb, exclude_root=B),
    }


def direct_masked(A, B) -> bool:
    """MASKED iff no one-sided neighbour exists in either transfer graph."""
    return not any(masking_report(A, B).values())
