for n in range(Nmax+1):
    for k in range(0, n+1):
        assert comb_small(n, k) == math.comb(n, k)