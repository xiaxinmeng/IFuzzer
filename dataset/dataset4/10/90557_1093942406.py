
from typing import MutableMapping, KeysView, ItemsView, ValuesView, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class dict(MutableMapping[_KT, _VT]):
    def keys(self) -> KeysView[_KT]: ...
    def values(self) -> ValuesView[_VT]: ...
    def items(self) -> ItemsView[_KT, _VT]: ...
