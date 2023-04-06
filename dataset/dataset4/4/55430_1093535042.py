def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))