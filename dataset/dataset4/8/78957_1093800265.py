
from dataclasses import dataclass
from typing import get_type_hints

class Foo:
    pass

@dataclass
class Bar:
    foo: Foo

print(get_type_hints(Bar.__init__))
