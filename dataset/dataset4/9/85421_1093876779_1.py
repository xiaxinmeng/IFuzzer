from __future__ import annotations

from typing import get_type_hints
from foo import Foo

class Bar(Foo, total=False):
    b: int

print(get_type_hints(Bar))