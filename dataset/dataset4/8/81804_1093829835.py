from typing import ClassVar
from dataclasses import dataclass

@dataclass
class MyLoader:
    __spec__: ClassVar["Any"] = None
    name: str

l = MyLoader('test')