class A:
    def __new__(cls, a=1, *args, **kwargs):
        return object.__new__(cls)

class B(A):
    def __init__(self, b):
        pass

import inspect
print(inspect.signature(B))