
from abc import ABC

class C1:
    pass

issubclass(dict[str, str], C1)  # False

class C2(ABC):
    pass

issubclass(dict[str, str], C2)  # TypeError: issubclass() arg 1 must be a class
