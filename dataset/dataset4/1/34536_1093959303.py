class A:
  def foo(self):
    "do the foo"
    pass

class B(A):
  def foo(self):
    pass

class C(B):
  def foo(self):
    "do the foo in C"
    pass