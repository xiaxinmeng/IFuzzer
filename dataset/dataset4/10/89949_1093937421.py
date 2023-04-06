from abc import ABCMeta, abstractmethod

class Sized(metaclass=ABCMeta):
    @abstractmethod
    def __hash__(self):
        return 0
    @classmethod
    def __instancecheck__(cls, x):
        print('Called')
        return hasattr(x, "__len__")
    @classmethod
    def __subclasscheck__(cls, C):
        return hasattr(C, "__bases__") and hasattr(C, "__len__")