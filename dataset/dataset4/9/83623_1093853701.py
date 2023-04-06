
from __future__ import annotations

import dataclasses
from typing import Annotated, get_type_hints


@dataclasses.dataclass
class C:
    v: Annotated[int, "foo"]


v_type = dataclasses.fields(C)[0].type
print(repr(v_type))  # "Annotated[int, 'foo']"
print(repr(get_type_hints(C)["v"]))  # <class 'int'>
print(repr(eval(v_type)))  # typing.Annotated[int, 'foo']
