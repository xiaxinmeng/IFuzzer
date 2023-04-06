class A:
    @property
    def f(self): pass

A.f.__doc__ = (A.f,)