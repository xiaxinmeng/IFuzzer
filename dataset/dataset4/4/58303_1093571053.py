def f(): pass

d = {'__qualname__': 42, '__new__': f}
assert d['__new__'] is f
assert '__qualname__' in d
Enum = type.__new__(type, 'Enum', (), d)
assert d['__new__'] is f
assert '__qualname__' in d