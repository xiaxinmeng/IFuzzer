
import pickle
from dataclasses import dataclass

@dataclass(frozen=True)
class A:
  __slots__ = ('a',)
  a: int

b = pickle.dumps(A(5))
pickle.loads(b)
