from __future__ import annotations
from typing import ForwardRef, Optional, get_type_hints
def func(a: Optional["int"]):
    pass
assert get_type_hints(func)["a"] == Optional[ForwardRef("int")]
# one would expect get_type_hints(func)["a"] == Optional[int] (which is the case without the import of __future__.annotations!)