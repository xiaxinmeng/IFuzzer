from itertools import chain, combinations

def powerset(iterable):
    pool = tuple(iterable)
    n = len(pool)
    return chain.from_iterable(combinations(pool, i) for i in range(n+1))

print(list(powerset(range(3))))