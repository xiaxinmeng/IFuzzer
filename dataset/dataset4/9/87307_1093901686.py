from dataclasses import asdict, dataclass

@dataclass(eq=True, frozen=True)
class A:
  a: str

@dataclass(eq=True, frozen=True)
class B:
  b: dict[A, str]