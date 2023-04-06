from types import SimpleNamespace
ns = SimpleNamespace(_A__x=1, _A__y=2)
class A:
    print(ns.__x, ns.__y) # exactly the same meaning as print(ns._A__x, ns._A__y)
# prints: 1 2

class B:
    __x = 24
    print(locals())
# prints {'__module__': '__main__', '__qualname__': 'B', '_B__x': 24}