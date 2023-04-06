class Foo:
  def __init__(self):
    self._x = 42
  @property
  def x(self):
    return self._x