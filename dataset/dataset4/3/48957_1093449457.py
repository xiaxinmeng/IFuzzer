def round(n, i):
    if i >= 0: return n
    i = 10**(-i)
    r = n%(2*i)
    if r < i:
        return n-r
    return n-r+2*i