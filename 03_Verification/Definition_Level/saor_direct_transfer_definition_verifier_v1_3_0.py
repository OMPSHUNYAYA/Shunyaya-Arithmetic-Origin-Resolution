#!/usr/bin/env python3
"""Direct transfer-graph definition-level verification for SAOR v1.3.0.

This program constructs one-sided equal-sum and equal-product candidates from
the transfer definitions. It does not call the closed-form masking functions
from the reference implementation.
"""
from __future__ import annotations
import argparse,itertools,math,sys
SEED_A,SEED_B=(2,6,6),(3,3,8)
ANCHOR={4:(2,3),5:(2,3,4,17)}

def sum_parts(total,m,forb,lo=2):
    if m==0:
        if total==0: yield ()
        return
    for x in range(lo,total//m+1):
        if x not in forb:
            for r in sum_parts(total-x,m-1,forb,x): yield (x,)+r

def prod_parts(n,m,forb,lo=2):
    if m==0:
        if n==1: yield ()
        return
    if m==1:
        if n>=lo and n not in forb: yield (n,)
        return
    x=lo
    while x**m<=n:
        if n%x==0 and x not in forb:
            for r in prod_parts(n//x,m-1,forb,x): yield (x,)+r
        x+=1

def one_sided(a,b,gen):
    sa=set(a); a=tuple(sorted(a)); b=tuple(sorted(b))
    return next((w for w in gen(set(b)) if w!=a and w!=b and sa&set(w)),None)

def direct_masked(E,j):
    a=tuple(sorted(SEED_A+ANCHOR[j]+tuple(E)))
    b=tuple(sorted(SEED_B+ANCHOR[j]+tuple(E)))
    m,s,p=len(a),sum(a),math.prod(a)
    S=lambda f: sum_parts(s,m,f)
    P=lambda f: prod_parts(p,m,f)
    return all(one_sided(x,y,g) is None for g in (S,P) for x,y in ((a,b),(b,a)))

def theorem_masked(E,j):
    E=tuple(E); N=len(E); S=sum(E); supp=set(E)
    if j==4:
        r=-3+S-4*N
        return r<0 or (r==1 and 5 in supp) or (r==3 and 5 in supp and 7 in supp)
    if 5 not in supp:
        return 4+S-5*N<0
    r=S-6*N-2
    return r<0 or (r in (1,2) and 7 in supp) or (r==5 and 7 in supp and 11 in supp)

def run(deep=False):
    maxn=5 if deep else 3
    alphabet=(2,3,5,7,11,13,17,19,23,101) if deep else (2,3,5,7,11,13,17,101)
    checked=0; bad=[]
    for n in range(maxn+1):
        for E in itertools.combinations_with_replacement(alphabet,n):
            for j in (4,5):
                checked+=1; d=direct_masked(E,j); t=theorem_masked(E,j)
                if d!=t: bad.append((E,j,d,t))
    print('SAOR direct transfer-graph definition-level verification v1.3.0')
    print('semantics:dual_twinhood_in_P_and_S_external_neighbour_sets')
    print(f'definition_level_masking:{"PASS" if not bad else "FAIL"}:checks={checked}:max_context_size={maxn}')
    if bad:
        for row in bad[:20]: print('mismatch',row)
        raise SystemExit(1)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--self-test',action='store_true'); p.add_argument('--verify',action='store_true'); a=p.parse_args(); run(a.verify)
if __name__=='__main__': main()
