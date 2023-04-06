from collections import UserList
from typing import Sequence, Optional


class MyList(UserList, Sequence):
    pass


def foo(seq: Optional[Sequence]):
    return seq
