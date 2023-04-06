from types import FunctionType
import random

class BadEq:
    def __hash__(self):
        print("hash called")
        return hash("__name__")
    def __eq__(self, other):
        print("eq called")
        raise Exception()

# run until we hit a 0x61616161.. pointer for PyFunctionObject->func_qualname, and crash
for i in range(0,100):
    s = int(random.random() * 1000) * "a"
    try:
        FunctionType(BadEq.__hash__.__code__, {BadEq(): 1})
    except Exception:
        pass
