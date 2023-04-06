
from typing import Annotated, Final
# TypeError: typing.Final[int] is not valid as type argument
var: Annotated[Final[int], "foo"] = 4
