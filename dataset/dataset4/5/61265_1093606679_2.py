class IsInstance(object):
  def __init__(self, Type):
    self.Type = Type
  def __eq__(self, other):
   return isinstance(other, self.Type)