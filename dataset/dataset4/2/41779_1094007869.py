class A(str):
 pass # implicitly adds __dict__, __weakref__
class B(A):
 __slots__ = ["a", "b"]

b = B()
b.c = 1