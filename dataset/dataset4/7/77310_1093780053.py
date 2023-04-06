
import dataclasses

@dataclasses.dataclass
class A:
  x: int = 1


@dataclasses.dataclass
class B(A):
  y: int  # ERROR: non-default argument follows default argument
