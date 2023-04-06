from functools import lru_cache

once = True

@lru_cache(maxsize=10)
def f(x):
    global once
    rv = f'.{x}.'
    if x == 20 and once:
        once = False
        print('Calling again', f(x))
    return rv

for x in range(15):
    f(x)

print(f.cache_info())
print(f(20))
print(f.cache_info())
print(f(21))
print(f.cache_info())