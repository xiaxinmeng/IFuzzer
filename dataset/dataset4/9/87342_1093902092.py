
import dataclasses

@dataclasses.dataclass(frozen=True)
class Base:
  pass

@dataclasses.dataclass
class Derived(Base):
  a: int

d = Derived(2)
# OK
