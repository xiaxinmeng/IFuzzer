def f(L):
    return [(x<=y) for x,y in zip(L, L[1:])]