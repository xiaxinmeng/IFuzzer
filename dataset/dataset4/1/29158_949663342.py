from __future__ import annotations

import dataclasses
from test import dataclass_textanno  # We need to be sure that `Foo` is not in scope


class Custom:
    pass


@dataclasses.dataclass
class Child(dataclass_textanno.Bar):
    custom: Custom


@dataclasses.dataclass(init=False)
class WithFutureInit(Child):
    def __init__(self, foo: dataclass_textanno.Foo, custom: Custom) -> None:
        pass