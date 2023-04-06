import abc
def f():
    pass

class A(metaclass=abc.ABCMeta):
    pass

issubclass(f, A)