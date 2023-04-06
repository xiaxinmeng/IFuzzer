class A(object): __slots__=()
class B(object): pass
class C(A,B) : __slots__=()
C().x=2