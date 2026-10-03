for d4 in range(-30,31):
  for d5 in range(-30,31):
    N=d4-d5+7; S=5*d4-4*d5+31
    assert (-3+S-4*N,4+S-5*N)==(d4,d5)
print('SAOR affine compression corollary regression: PASS')
