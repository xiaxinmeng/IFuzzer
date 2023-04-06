class Crasher(tuple): pass

class Crasher(tuple):
  __slots__ = ()

class Crasher(tuple):
  def __new__(cls,): return tuple.__new__(cls,)
  __slots__ = ()