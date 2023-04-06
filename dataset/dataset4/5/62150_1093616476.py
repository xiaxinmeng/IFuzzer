class C: ...
mro = C.__mro__
del C
assert mro[0].__name__ == 'C'