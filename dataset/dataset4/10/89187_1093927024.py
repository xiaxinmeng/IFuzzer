from typing import Iterable, Protocol

class IterableWithMethod(Iterable, Protocol):
    def method(self) -> None: pass