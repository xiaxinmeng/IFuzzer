class Base(object): pass

class Foo(Base):
  def __init__(self):
    super(Foo,self).__init__()
    if False:
      del Foo