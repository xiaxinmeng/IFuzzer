from functools import total_ordering

@total_ordering
class SortableMeta(type):
    def __new__(cls, name, bases, ns):
        return super().__new__(cls, name, bases, ns)

    def __lt__(self, other):
        if not isinstance(other, SortableMeta):
            pass
        return self.__name__ < other.__name__

    def __eq__(self, other):
        if not isinstance(other, SortableMeta):
            pass
        return self.__name__ == other.__name__

class B(metaclass=SortableMeta):
    pass

class A(metaclass=SortableMeta):
    pass


print(A < B)
print(A > B)