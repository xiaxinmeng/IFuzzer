from itertools import chain, islice
from typing import Iterable, TypeVar

T = TypeVar('T')  # pylint: disable=invalid-name


def batches(items: Iterable[T], num: int) -> Iterable[Iterable[T]]:
    items = iter(items)
    while True:
        try:
            first_item = next(items)
        except StopIteration:
            break
        yield chain((first_item,), islice(items, 0, num - 1))