class S(str): __slots__ = ()

'a'.__class__ = S

def f(a): pass
