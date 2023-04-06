from dataclasses import dataclass, fields
from typing import Optional, get_type_hints

@dataclass
class Nestable:
    child: Optional['Nestable']

o = Nestable(None)
print('fields:', fields(o))
print('type hints:', get_type_hints(Nestable))