from dataclasses import dataclass
from typing import Callable

@dataclass(init=True)
class Foo:
    callback: Callable[[int], int] = lambda x: x**2
     
@dataclass(init=False)
class Bar:
    callback: Callable[[int], int] = lambda x: x**2