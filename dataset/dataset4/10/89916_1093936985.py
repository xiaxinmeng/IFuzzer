# cat test.py
from typing import Generic, TypeVar
from unittest import mock

T = TypeVar('T')

class Foo(Generic[T]):
    def bar(self) -> None:
        pass

m = mock.MagicMock(spec=Foo[int])
m.bar()