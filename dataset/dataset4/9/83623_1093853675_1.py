
from __future__ import annotations
from dataclasses import dataclass
from dataclasses_serialization.json import JSONSerializer

@dataclass
class Foo:
    x: int

JSONSerializer.deserialize(Foo, {'x': 42})
