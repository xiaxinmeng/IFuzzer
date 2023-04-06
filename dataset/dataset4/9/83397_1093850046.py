def g():
    def f(x : 3 in {1,2,3}, /): ...
    return f

print(g.__code__.co_consts[2])
frozenset({1, 2, 3})