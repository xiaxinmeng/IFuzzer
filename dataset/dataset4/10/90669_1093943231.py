from __future__ import annotations
myAnnotated = typing.Annotated

@dataclass
class Foo:
    a: myAnnotated[ClassVar[int]]