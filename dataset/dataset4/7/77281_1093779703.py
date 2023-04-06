@dataclass
class Base:
    __slots__ = ('x',)
    x: Any

Base()  # No TypeError exception