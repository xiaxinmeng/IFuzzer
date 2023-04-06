parent = bytearray # fails
# parent = bytes   # works
# parent = str     # works

class Foo(parent):

  def __new__(klass, x): return parent.__new__(klass, x)

Foo(x = None)