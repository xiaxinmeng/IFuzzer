from dataclasses import dataclass
from typing import Protocol

class P(Protocol):
    pass

@dataclass
class B(P):
    value: str

print(B("test"))