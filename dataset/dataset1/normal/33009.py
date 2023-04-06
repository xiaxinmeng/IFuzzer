from functools import partialmethod
import inspect

class T:
    g = partialmethod((lambda self, x: x), 1)

print(T().g())  # Correctly returns 1.
print(T.g(T()))  # Correctly returns 1.
print(inspect.signature(T.g))  # Crashes.
