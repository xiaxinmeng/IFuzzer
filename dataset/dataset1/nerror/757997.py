class StringDerived(str):
  __slots__ = ['a']
  def __init__(self, string):
    str.__init__(self, string)
    self.a = 1

class DerivedAgain(StringDerived):
  pass

o = DerivedAgain('hello world')
o.b = 2

