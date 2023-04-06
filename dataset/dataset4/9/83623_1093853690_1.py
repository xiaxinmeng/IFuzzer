from __future__ import annotations
import dataclasses
from some_library_typing import mytype as mytype_deconflicted

mytype = int

@dataclasses.dataclass
class MyClass:
    var1: mytype_deconflicted = 'foo'

    def method1(self, val: mytype) -> mytype:
        return val + 1