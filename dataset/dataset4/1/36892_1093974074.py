gRef = None

class Foo(object):
  def __del__(self):
    global gRef
    gRef = self
    
x = Foo()
del x