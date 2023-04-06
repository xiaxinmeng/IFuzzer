from enum import IntEnum, Enum

class A(IntEnum):
   a = 1

class B(A, Enum):
   b= 1

print(B.b)