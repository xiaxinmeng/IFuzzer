
from dataclasses import dataclass


@dataclass
class A:
    pass


@dataclass(frozen=True)
class B(A):
    x: int

print("42")
