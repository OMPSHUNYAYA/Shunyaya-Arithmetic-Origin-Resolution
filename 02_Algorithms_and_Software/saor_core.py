#!/usr/bin/env python3
from __future__ import annotations
import functools, math

VERSION = "1.3.0"
SEED_A=(2,6,6)
SEED_B=(3,3,8)
ANCHOR4=(2,3)
ANCHOR5=(2,3,4,17)

def is_prime(n:int)->bool:
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def normalize_context(E):
    E=tuple(sorted(E))
    if any(not is_prime(p) for p in E):
        raise ValueError("context must be a finite multiset of primes")
    return E

def omega(n:int)->int:
    c=0; d=2; x=n
    while d*d<=x:
        while x%d==0:
            c+=1; x//=d
        d+=1
    if x>1: c+=1
    return c

def prime_divisors(n:int):
    out=set(); d=2; x=n
    while d*d<=x:
        if x%d==0:
            out.add(d)
            while x%d==0: x//=d
        d+=1
    if x>1: out.add(x)
    return out

def stats(E):
    E=normalize_context(E); return len(E),sum(E)

def support_bits(E):
    s=set(normalize_context(E)); return (5 in s,7 in s,11 in s)

def D4(E):
    N,S=stats(E); return -3+S-4*N

def D5(E):
    N,S=stats(E); return 4+S-5*N

def T5(E):
    N,S=stats(E); return S-6*N-2

def sharp_signature(E):
    return (D4(E),D5(E),*support_bits(E))

def masked4(E):
    r=D4(E); e5,e7,_=support_bits(E)
    return r<0 or (r==1 and e5) or (r==3 and e5 and e7)

def masked5(E):
    e5,e7,e11=support_bits(E)
    if not e5: return D5(E)<0
    r=T5(E)
    return r<0 or (r in (1,2) and e7) or (r==5 and e7 and e11)

def joint_status(E): return (masked4(E),masked5(E))


def compose(E,F):
    return normalize_context(tuple(E)+tuple(F))

def effect_phi4(delta:int):
    if delta<0:
        F=(3,)*(-delta)
    elif delta==0:
        F=()
    else:
        k=(delta+2)//3
        F=(7,)*k+(3,)*(3*k-delta)
    assert sum(x-4 for x in F)==delta
    return normalize_context(F)

def effect_phi4_avoid_7(delta:int):
    if delta<0:
        F=(3,)*(-delta)
    elif delta==0:
        F=()
    else:
        k=(delta+6)//7
        F=(11,)*k+(3,)*(7*k-delta)
    assert 5 not in F and 7 not in F and sum(x-4 for x in F)==delta
    return normalize_context(F)

def effect_phi5_avoid_5(delta:int):
    if delta==0:
        F=()
    elif delta>0:
        if delta%2==0:
            F=(7,)*(delta//2)
        else:
            F=(2,)+(7,)*((delta+3)//2)
    else:
        n=-delta; r=n%3
        if r==0: F=(2,)*(n//3)
        elif r==1: F=(2,)*((n+2)//3)+(7,)
        else: F=(2,)*((n+4)//3)+(7,7)
    assert 5 not in F and sum(x-5 for x in F)==delta
    return normalize_context(F)

def effect_tau6(delta:int):
    if delta<0: F=(5,)*(-delta)
    elif delta>0: F=(7,)*delta
    else: F=()
    assert sum(x-6 for x in F)==delta
    return normalize_context(F)

def sharp_future_separator(E,F):
    E=normalize_context(E); F=normalize_context(F)
    kE=sharp_signature(E); kF=sharp_signature(F)
    if kE==kF: return None
    d4E,d5E,b5E,b7E,b11E=kE
    d4F,d5F,b5F,b7F,b11F=kF
    if d4E!=d4F:
        X=effect_phi4(-max(d4E,d4F)); axis='D4'
    elif b5E!=b5F:
        X=effect_phi4(1-d4E); axis='eps5'
        assert 5 not in X
    elif b7E!=b7F:
        setup=() if b5E else (5,)
        d4=D4(compose(E,setup))
        X=normalize_context(setup+effect_phi4_avoid_7(3-d4)); axis='eps7'
        assert 7 not in X
    elif d5E!=d5F:
        if not b5E:
            X=effect_phi5_avoid_5(-max(d5E,d5F))
        else:
            X=effect_tau6(-max(T5(E),T5(F)))
        axis='D5'
    else:
        assert b11E!=b11F
        setup=()
        if not b5E: setup+=(5,)
        if not b7E: setup+=(7,)
        E0=compose(E,setup); F0=compose(F,setup)
        assert T5(E0)==T5(F0)
        X=normalize_context(setup+effect_tau6(5-T5(E0))); axis='eps11'
        assert 11 not in X
    assert joint_status(compose(E,X))!=joint_status(compose(F,X))
    return axis,X

def base_data(A0,B0):
    A0=tuple(A0); B0=tuple(B0)
    if len(A0)!=len(B0) or len(A0)<3: raise ValueError("equal arity at least 3 required")
    if sum(A0)!=sum(B0): raise ValueError("equal sum required")
    if math.prod(A0)!=math.prod(B0): raise ValueError("equal product required")
    P=math.prod(A0); shared=set(A0)&set(B0)
    pd=prime_divisors(P)
    return dict(A0=A0,B0=B0,m0=len(A0),sigma0=sum(A0),product0=P,
                omega0=omega(P),shared=shared,prime_divisors=pd,
                prime_cover=pd<=shared,atom_deficit=omega(P)<2*len(A0),
                exclusive_A=set(A0)-set(B0),exclusive_B=set(B0)-set(A0))

def product_twin_hypotheses(A0,B0):
    d=base_data(A0,B0); return d['prime_cover'] and d['atom_deficit']

def least_composite_not_in(B):
    B=set(B); n=4
    while True:
        if not is_prime(n) and n not in B: return n
        n+=1

def possible_fillers(B):
    B=set(B); Q=least_composite_not_in(B)
    return tuple(q for q in range(2,Q+1) if q not in B)

def odd_permanent_increment(B,q):
    B=set(B); M=max(B|{q,2}); a=1
    while True:
        y=q+a
        if a%2==1 and y>M and not is_prime(y) and y not in B: return a
        a+=2

def synthesis_data(B):
    B=set(B); rows={}; L=0
    for q in possible_fillers(B):
        M=max(B|{q,2}); a=odd_permanent_increment(B,q); C=M+a-q+1
        rows[q]={'M':M,'a':a,'C':C,'L':q+C-1}; L=max(L,q+C-1)
    crit=tuple(p for p in range(2,L+1) if is_prime(p) and p not in B)
    return {'first_unforbidden_composite':least_composite_not_in(B),'q_rows':rows,
            'critical_bound':L,'critical_primes':crit}

def min_safe(B,E):
    forbidden=set(B)|set(normalize_context(E)); q=2
    while q in forbidden: q+=1
    return q

def direct_residual_feasible(B,E,q,k,R):
    if R<0: return False
    forbidden=frozenset(set(B)|set(normalize_context(E)))
    @functools.lru_cache(None)
    def rec(rem,slots,lo):
        if rem==0: return True
        if slots==0: return False
        for r in range(max(1,lo),rem+1):
            if q+r in forbidden: continue
            if rec(rem-r,slots-1,r): return True
        return False
    return rec(R,k,1)

def synthesized_residual_feasible(B,E,k,target_sum):
    if k<2: raise ValueError("two-filler theorem requires at least two filler slots")
    B=set(B); E=normalize_context(E); data=synthesis_data(B)
    low=tuple(p for p in E if p<=data['critical_bound'])
    q=min_safe(B,low); row=data['q_rows'][q]; R=target_sum-k*q
    if R<0: return False
    if R>=row['C']: return True
    return direct_residual_feasible(B,low,q,k,R)

def synthesized_masked(A0,B0,E):
    E=normalize_context(E); d=base_data(A0,B0)
    if not (d['prime_cover'] and d['atom_deficit']):
        raise ValueError("Prime Cover and Atom Deficit required")
    m=d['m0']+len(E); total=d['sigma0']+sum(E)
    for witnesses,forbidden in ((d['exclusive_A'],set(B0)),(d['exclusive_B'],set(A0))):
        for x in witnesses:
            if synthesized_residual_feasible(forbidden,E,m-1,total-x): return False
    return True

def synthesized_signature(A0,B0,E):
    E=normalize_context(E)
    da=synthesis_data(set(B0)); db=synthesis_data(set(A0))
    crit=tuple(sorted(set(da['critical_primes'])|set(db['critical_primes'])))
    s=set(E)
    return (len(E),sum(E),tuple(p in s for p in crit),crit)
