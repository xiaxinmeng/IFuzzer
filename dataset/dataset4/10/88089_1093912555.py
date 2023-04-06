from typing import NamedTuple, TypeVar, Generic, List, Tuple

T = TypeVar("T")

class New(NamedTuple, Generic[T]):
    x: List[T]
    y: Tuple[T, T]