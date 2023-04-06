
from __future__ import annotations
from dataclasses import dataclass, fields

@dataclass
class Foo:
    x: int

print(fields(Foo)[0].type)
