import _collections
class BadDeque(_collections.deque):
    def __new__(cls, *args):
        if len(args):
            return 42
        return _collections.deque.__new__(cls)
#BadDeque() * 42
BadDeque() + _collections.deque([42])

