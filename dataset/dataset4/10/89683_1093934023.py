
from dataclasses import dataclass
from copy import deepcopy

@dataclass(frozen=True)
class FrozenData:
    # Without slots no errors occur?
    __slots__ = "my_string",

    my_string: str

deepcopy(FrozenData(my_string="initial"))
