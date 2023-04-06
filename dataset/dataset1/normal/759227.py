class X(object):
  def __nonzero__(self):
   return self

x=X()
not x
