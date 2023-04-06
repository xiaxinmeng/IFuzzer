from typing import ForwardRef, Optional, get_type_hints
def func(a: "Optional[\"int\"]"):
    pass
assert get_type_hints(func)["a"] == Optional[ForwardRef("int")] 
