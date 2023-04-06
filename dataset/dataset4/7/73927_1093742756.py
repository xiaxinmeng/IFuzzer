import io

class IntLike():
    def __init__(self, num):
        self._num = num

    def __index__(self):
        return self._num

    __int__ = __index__