from __future__ import annotations
import dataclasses

mytype = int

@dataclasses.dataclass
class MyClass1:
    foo: mytype = 1

MyClass2 = dataclasses.make_dataclass(
    f'MyClass2',
    [('foo', mytype, 1)]
)