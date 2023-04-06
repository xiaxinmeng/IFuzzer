
from __future__ import annotations

import typing

class A:
    f: 'Undef'

hints = typing.get_type_hints(A)
