@dataclass(hash=True, eq=False, frozen=False)
class A:
    i: int
    __hash__ = None