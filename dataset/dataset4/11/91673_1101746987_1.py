
from dataclasses import dataclass
from typing import List

@dataclass
class User:
    x: list = field(default_factory=list)
    y: List[int] = field(default_factory=list)
