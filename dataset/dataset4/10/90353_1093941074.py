
from typing import Annotated, Optional, get_type_hints

class Foo:
    def __init__(self, x: Annotated[Optional[str], "d"] = None): ...

class Foo2:
    x: Annotated[Optional[str], "d"] = None

print(get_type_hints(Foo.__init__, include_extras=False))  # ok
# {'x': typing.Optional[str]}
print(get_type_hints(Foo2, include_extras=False))  # ok
# {'x': typing.Optional[str]}

print(get_type_hints(Foo.__init__, include_extras=True))  # not ok?
# {'x': typing.Optional[typing.Annotated[typing.Optional[str], 'd']]}
print(get_type_hints(Foo2, include_extras=True))  # ok
# {'x': typing.Annotated[typing.Optional[str], 'd']}
