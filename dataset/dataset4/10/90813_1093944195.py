from __future__ import annotations
from typing import TypeAlias, get_type_hints

import typing

class C:
    a: TypeAlias = int

print(get_type_hints(C))