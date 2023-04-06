from typing import Protocol
from dataclasses import dataclass

class SomeProtocol(Protocol):
    @property
    def some_value(self) -> str: ...

@dataclass
class SomeDataclasss(SomeProtocol):
    some_value: str

if __name__ == '__main__':
    a = SomeDataclasss(some_value="value") # this crashes with AttributeError: can't set attribute 'some_value'