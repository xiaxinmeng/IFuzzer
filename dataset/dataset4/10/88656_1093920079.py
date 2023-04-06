from typing import TypeVar

T = TypeVar("T")

Alias = int | list[T]

def f(x: Alias[str]) -> None:
    pass