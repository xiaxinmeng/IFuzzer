from functools import singledispatch
from typing import Optional

@singledispatch
def load(key: Optional[str] = None, /) -> None:
    raise NotImplementedError

@load.register
def _(key: None, /) -> None:
    print(f"loaded {key=}") 

@load.register
def _(key: str, /) -> None:
    print(f"loaded {key=}")
    
load()  # TypeError: load requires at least 1 positional argument