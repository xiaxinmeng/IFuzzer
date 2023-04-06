@dataclasses.dataclass
class D:
    a: Any
    b: Any = field(kw_only=True)
    c: Any