class O(object):
     pass

class M(type):
     pass

class N(type):
     pass

class A(O, metaclass=M):
     pass

class B(O, metaclass=N):
     pass

print(B.__bases__)
print(B.__mro__)

print(type(B))
print(type(A))
print(issubclass(type(B), type(A)))

class C(A, metaclass=N):
     pass

class D(B, A):
     pass

class E(B, metaclass=N):
     pass