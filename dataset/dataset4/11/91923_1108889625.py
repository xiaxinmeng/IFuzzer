import inspect
from typing import TypedDict


class TD(TypedDict):
    a: int
    b: int


inspect.signature(TD)