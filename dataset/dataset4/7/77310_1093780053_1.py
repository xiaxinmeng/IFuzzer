
@dataclasses.dataclass
class B(A):
  y: int = dataclasses.field(kw_only=True)


B(123, y=456)
