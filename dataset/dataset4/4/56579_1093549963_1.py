def _outer_C(*__args__, **__kw__):
    class _inner_C(*__args__, **__kw__):
        def f(self):
            return __class__
    __class__ = _inner_C
    return _inner_C
C = _outer_C(A, B, metaclass=meta)