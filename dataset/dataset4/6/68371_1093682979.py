from collections import UserDict
from abc import ABCMeta


class MetaMyDict(ABCMeta):

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        return {}

    def __new__(mcls, name, bases, namespace, **kwds):
        return super().__new__(mcls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kargs):
        return super().__init__(name, bases, namespace)

class MyDict(UserDict, metaclass=MetaMyDict, bar='baz'):
    pass

dictionary = MyDict()