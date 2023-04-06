
from _collections_abc import dict_keys
from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")

class DictSubclass(dict[K, V]):
    def keys(self) -> "dict_keys[K, V]":
        return super().keys()
