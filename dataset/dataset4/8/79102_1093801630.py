from __future__ import annotations

import typing

def f() -> typing.NoReturn:
    pass

typing.get_type_hints(f)