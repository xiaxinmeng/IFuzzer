@lru_cache()
def f(x):
    return x

print(f(1))
print(f(1.0))