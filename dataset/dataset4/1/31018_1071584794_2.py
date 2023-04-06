from typing import TypeVar, Generic

T1 = TypeVar('T1')
class C(Generic[T1]): pass

a = C[int]
reveal_type(a)
b = C[(int,)]
reveal_type(b)