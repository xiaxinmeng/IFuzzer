class Foo(Base):
  def __init__(self):
    assert 'Foo' in globals()
    assert Foo
    super(Foo,self).__init__()
    if False:
      del Foo