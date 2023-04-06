
import sys, gc
from typing import TypeVar

gc.collect()
for _ in range(10):
 sys.gettotalrefcount()
 T = TypeVar('T')
 U = int | list[T]
 T.blah = U
 del T
 del U
 gc.collect()
