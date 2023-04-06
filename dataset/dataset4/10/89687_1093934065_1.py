
from __future__ import annotations

import foo
import dataclasses
import typing

@dataclasses.dataclass
class B(foo.A):
  pass

typing.get_type_hints(B)
