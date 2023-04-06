from typing import *
Ts = TypeVarTuple('Ts')
T1 = TypeVar('T')
T2 = TypeVar('T')
class C(Generic[T1, T2, Unpack[Ts]]): pass
with self.assertRaises(TypeError):
    C[int]