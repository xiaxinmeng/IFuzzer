from collections import UserList
from typing import Sequence
class MyList(UserList, Sequence):
    pass
isinstance(None, Sequence)