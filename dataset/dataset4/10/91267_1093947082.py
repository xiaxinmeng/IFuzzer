from typing import Tuple
from enum import Enum
class Blah(Tuple[str, ...], Enum):
    val = ('a', 'b')