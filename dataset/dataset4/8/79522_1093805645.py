from __future__ import annotations
import typing
from collections import OrderedDict
# Understood by mypy
def f(d: OrderedDict[str, str]) -> None:
    pass
typing.get_type_hints(f)