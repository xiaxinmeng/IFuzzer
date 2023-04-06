
from typing import Tuple
class C(Tuple[int]): pass
print(C.mro())  # C, tuple, typing.Generic, object
