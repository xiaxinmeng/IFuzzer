import abc
class MyABC:
    __metaclass__ = abc.ABCMeta
    __slots__ = ["a"]

class Unrelated:
    pass
MyABC.register(Unrelated)

u=Unrelated()
assert isinstance(u, MyABC)

MyABC.a.__set__(u, 3) # Boom