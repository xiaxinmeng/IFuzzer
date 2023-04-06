class Event:
    ...
    def wait(self, timeout=None):
        self._cond.__enter__()
        signaled = self._flag
        if not signaled:
            signaled = self._cond.wait(timeout)
        self._cond.__exit__()
        return signaled