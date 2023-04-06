class X:
  def foo(self):pass

X.foo=classmethod(X.foo)