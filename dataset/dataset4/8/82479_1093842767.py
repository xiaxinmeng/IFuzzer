
# test.py

import typing as t


T = t.TypeVar("T")


class BaseOfGeneric:

    @classmethod
    def f(cls):
        # when called from an instantiated generic type, e.g.,
        # `MyList[int]`, expect `cls` to be the GenericAlias with its type
        # argument already insteantiated
        print(f"current class is {cls}")
        print(f"current class's type: {type(cls)}")


class MyList(t.List[T], BaseOfGeneric):
    pass


MyIntList = MyList[int]

MyIntList.f()
