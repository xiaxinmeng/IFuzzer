
In [1]: s = frozenset({1}); id(s) == id(frozenset(s)) == id(s.copy())
Out[1]: True
