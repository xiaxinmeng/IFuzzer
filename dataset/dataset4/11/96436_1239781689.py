from typing import Any

from _testcapi import sequence_getitem


class Seq:
    def __init__(self, items: list[Any]):
        self._items = items

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: Any) -> Any:
        # no need to handle negative indexes specially here, `list` should do that
        return self._items[index]


seq = Seq([0, 1, 2, 3, 4])

assert len(seq) == 5

# Should raise IndexError, but instead this -7 gets double-corrected
# - PySequence_GetItem corrects -7 -> -2, and then calls seq.__getitem__(-2) 
# - self._items[-2] then handles -2 and returns element 3
print(sequence_getitem(seq, -7))