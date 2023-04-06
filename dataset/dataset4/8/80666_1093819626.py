cache = {}                  # On reload, this would clear the cache

def f(x):
    if x in cache:
        return cache[x]
    y = x**2
    cache[x] = y
    return y