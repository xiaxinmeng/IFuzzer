class A:
  def f(x): ...
class B(A):
  pass
class C(B):
  pass
class D:
  pass
class E(D,C):
  pass