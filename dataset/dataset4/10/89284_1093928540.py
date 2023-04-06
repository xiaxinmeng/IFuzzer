
from typing import Protocol

class P(Protocol):
    ...

class C(P):
    def __init__(self):
        super().__init__()

C()
