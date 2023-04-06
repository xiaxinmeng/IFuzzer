
from enum import Enum

class T(Enum):
  TEST = 1

print(T["TEST"])

class S(Enum):
  TEST = lambda a: a

print(S["TEST"])
