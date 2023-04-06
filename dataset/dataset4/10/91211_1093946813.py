import os

class A(os.PathLike):
    pass

class B(os.PathLike):
    pass

assert issubclass(A, os.PathLike) # direct inheritance relationship
assert issubclass(B, os.PathLike) # direct inheritance relationship
assert not issubclass(A, B) # A is not derived from B or vice-versa