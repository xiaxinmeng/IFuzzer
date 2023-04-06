class as_completed:
    def __init__(fs, *, loop=None, timeout=None):
        self.__fs = fs
        self.__loop = loop
        self.__timeout = timeout

    def __iter__(self):
        # current implementation here
        ...

    async def __aiter__(self):
        # new async implementation here
        ...

    def __next__(self):
        # defined for backward compatibility with code that expects
        # as_completed() to return an iterator rather than an iterable
        if self._iter is None:
            self._iter = iter(self)
        return next(self._iter)