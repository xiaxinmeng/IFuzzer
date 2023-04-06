@dataclass(hash=None, eq=True, frozen=False)
class A:
    i: int
    def __hash__(self): pass