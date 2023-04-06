from abc import ABCMeta
from gc import collect, get_objects
from collections import Counter
from pprint import pprint

class MyMetaclass(ABCMeta):
    pass

class MyClass(metaclass=MyMetaclass):
    pass

def main():
    class Sub(MyClass):
        pass
    assert issubclass(Sub, MyClass)

    class Other:
        pass
    assert not issubclass(Other, MyClass)

def print_object_types(n=5):
    types = Counter(map(type, get_objects())).most_common(n)
    pprint(types, underscore_numbers=True)

N = 1000

for _ in range(1000):
    N += N//10
    for j in range(N):
        main()
    print(N)
    print("before collection:")
    print_object_types()
    while collect():
        pass
    print("after collection:")
    print_object_types()
    print("\n\n")