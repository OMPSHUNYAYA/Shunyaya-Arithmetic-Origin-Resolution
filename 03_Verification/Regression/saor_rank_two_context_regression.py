def phi(p): return (p-4,p-5)
v2,v3=phi(2),phi(3)
assert v2==(-2,-3) and v3==(-1,-2)
assert v2[0]*v3[1]-v3[0]*v2[1]==1
print('SAOR rank-two context regression: PASS')
