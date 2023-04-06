# python3
class Base:
  def __eq__(self, other):
    print("base called")
    return super().__eq__(other)


class Foo(Base):

  def __eq__(self, other):
    print("foo called")
    return NotImplemented