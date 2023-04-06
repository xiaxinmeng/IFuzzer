from typing import Protocol

class SomeProtocol(Protocol):
    @property
    def some_value(self) -> str: ...

class SomeClass(SomeProtocol):
    def __init__(self, some_value):
        self.some_value = some_value

if __name__ == '__main__':
    a = SomeClass(some_value="value")