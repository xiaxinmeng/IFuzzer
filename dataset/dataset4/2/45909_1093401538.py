class A: pass
class B(A): pass
b=B()
A.x = 1
assert b.x == A.x
B.x = 2
assert b.x == B.x
del B.x
b.x         # <== AttributeError: 'B' object has no attribute 'x'