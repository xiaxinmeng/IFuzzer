
from collections.abc import Callable
from typing import Any, TypeVar

V = TypeVar("V")
Function = Callable[[list[V], V, V], float]


def random_fn(fn: Function[Any]) -> Function[Any]:
    return fn
