def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def f(n):
    if n in f.cache:
        return f.cache[n]
    else:
        x = f.cache[n] = factorial(n)
        return x

f.cache = lru_cache()