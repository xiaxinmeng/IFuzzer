import dataclasses
import pydantic

@dataclasses.dataclass
class Foobar:
    a: str
    b: list[int] = dataclasses.field(default_factory=lambda: [1, 2, 3])

Foobar2 = pydantic.dataclasses.dataclass(Foobar)
f2 = Foobar2(a="a")
print(f)