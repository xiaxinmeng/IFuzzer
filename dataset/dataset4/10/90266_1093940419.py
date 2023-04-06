from enum import Enum

class Foo:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return f'Foo(a={self.a!r})'

class Entries(Foo, Enum):
    ENTRY1 = Foo(1)