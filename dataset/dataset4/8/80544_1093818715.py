
import dataclasses
import typing
from datetime import datetime


@dataclasses.dataclass
class Foo:
    datetime: typing.Optional[datetime] = None


print(dataclasses.fields(Foo)[0].type)
