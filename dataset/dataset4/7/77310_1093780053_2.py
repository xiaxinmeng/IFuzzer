
class A:
  a0: int
  a1: int = field(kw_only=True)
  a2: int


class B(A):
  b0: int
  b1: int = field(kw_only=True)
  b2: int
