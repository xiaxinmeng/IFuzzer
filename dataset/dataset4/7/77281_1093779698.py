@dataclass
class Base:
    __slots__ = ('x',)
    x: Any


@dataclass
class Derived(Base):
    x: int
    y: int