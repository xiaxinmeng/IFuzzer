class M(type):
  def __subclasscheck__(cls, c):
    return c == 1 or super().__subclasscheck__(c)

class A(metaclass=M):
  pass

issubclass(1, A)
