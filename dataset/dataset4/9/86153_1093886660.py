from __future__ import annotations
from typing import get_type_hints

class C:
    def func(self, a: "C"):
        pass

    print(get_type_hints(func))