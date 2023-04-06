class A:
  class B:
    class E(Exception):
      pass

raise A.B.E()