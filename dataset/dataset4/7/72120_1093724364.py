def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = functools.lru_cache()(factorial)
f(20)
print(f.cache_info())