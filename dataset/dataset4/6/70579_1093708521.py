from typing import Generic, TypeVar

T = TypeVar('T')
class Foo(Generic[T]):
    def __init__(self, value: T):
        self.value = value

Bar = Foo[str]

foo = Foo('foo')
bar = Bar('bar')