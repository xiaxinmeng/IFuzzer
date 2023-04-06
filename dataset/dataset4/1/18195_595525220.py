def __init__(self, *, loop=None):
        self._waiters = None
        self._locked = False
        if loop is None:
            self._loop = events._get_running_loop()
            if self._loop is None:
                warnings.warn("The creation of asyncio objects without a running "
                              "event loop is deprecated as of Python 3.9.",
                              DeprecationWarning, stacklevel=2)
                self._loop = events.get_event_loop()