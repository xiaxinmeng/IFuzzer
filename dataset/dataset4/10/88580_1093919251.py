
from __future__ import annotations  # ***
import dataclasses

@dataclasses.dataclass
class C:
    x: dataclasses.InitVar[int]

    def __post_init__(self, x):
        print(f'hello {x}')

C(0)
