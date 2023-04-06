class C:
    __slots__ = 'abc'
assert 'abc' in C.__dict__