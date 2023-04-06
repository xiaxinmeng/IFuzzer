from typing import TypeVar, Generic
T = TypeVar('T')
class Node(Generic[T]):
    pass
x = Node[T]()
y = Node[int]()