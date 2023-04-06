from dataclasses import dataclass
from enum import Enum

@dataclass
class Foo:
    a: int = 0

class Entries(Foo, Enum):
    ENTRY1 = Foo(1)