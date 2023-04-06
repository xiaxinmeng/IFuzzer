# cat rep.py
from typing import Protocol

class Proto(Protocol):
    pass

class A:
    pass

class B(A, Proto):
    pass