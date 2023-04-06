
import inspect
from typing import Generic, TypeVar

T = TypeVar('T')

class A(Generic[T]):
    def __init__(self) -> None:
        pass

print(inspect.signature(A))
