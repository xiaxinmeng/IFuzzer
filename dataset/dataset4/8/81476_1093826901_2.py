def comb_small(n, k):
    if not 0 <= k <= n <= Nmax:
        raise ValueError("k or n out of range")
    return (F[n] * Finv[k] * Finv[n-k] % 2**64) << k.bit_count() + (n-k).bit_count() - n.bit_count()