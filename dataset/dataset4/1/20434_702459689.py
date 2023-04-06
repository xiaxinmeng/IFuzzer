
import typing
from dataclasses import dataclass

@dataclass
class T:
    a: "typing.ClassVar[int]"

T()
