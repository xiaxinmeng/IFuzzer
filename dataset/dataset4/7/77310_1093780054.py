
@dataclasses.dataclass(kw_only=True)
class A:
  a: int
  b: int
  c: int

# A(*, a, b, c)


@dataclasses.dataclass(kw_only='b')
class A:
  a: int
  b: int
  c: int

# A(a, *, b, c)
