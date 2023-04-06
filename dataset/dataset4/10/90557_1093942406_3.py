
from typing import KeysView, TypeVar

K = TypeVar("K")
V = TypeVar("V")

class DictSubclass(dict[K, V]):
    def keys(self) -> KeysView[K]:
        return super().keys()
