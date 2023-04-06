from dataclasses import dataclass, replace

@dataclass()
class A:
    a: int

class B(A):
    def __init__(self):
        super().__init__(a=1)

obj1 = B()
obj2 = replace(obj1, a=2)