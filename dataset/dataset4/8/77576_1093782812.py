class UnhashableRepr(dict):
    __repr__ = _testcapi.instancemethod(dict.__repr__)