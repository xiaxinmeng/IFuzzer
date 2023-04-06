
from types import MethodType


class myclassmethod:
    def __init__(self, func):
        self.func = func

    def __call__(self, cls):
        return self.func(cls)

    def __get__(self, instance, owner=None):
        if owner is None:
            owner = type(instance)
        return MethodType(self, owner)


class A:
    @myclassmethod
    def f1(cls):
        return cls

    @classmethod
    @myclassmethod
    def f2(cls):
        return cls


assert A.f1() is A
assert A.f2() is A  # <-- fails in 3.9, works in 3.8 and before
