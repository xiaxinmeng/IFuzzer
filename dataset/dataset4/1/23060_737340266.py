from typing import Callable
from typing import Callable, TypeVar
T = TypeVar('T')
class C1(Callable[[T], T]): ...

C1[int]  # C1[int]

C1[int].__args__ # (<class 'int'>,)  <- Find this strange, though it makes sense because it's just typing.Generic

C1[int].__origin__ # <class '__main__.C1'>
