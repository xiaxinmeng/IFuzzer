@dataclass(hash=True, eq=True, frozen=False)
class A:
    i: int
    __hash__=None