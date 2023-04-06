class AsyncExitStackWithPop(contextlib.AsyncExitStack):
    """Same as AsyncExitStack but with pop, i.e. removal functionality"""
    async def pop(self, cm):
        callbacks = self._exit_callbacks
        self._exit_callbacks = collections.deque()
        found = None
        while callbacks:
            cb = callbacks.popleft()
            if cb[1].__self__ == cm:
                found = cb
            else:
                self._exit_callbacks.append(cb)
        if not found:
            raise KeyError("context manager not found")
        if found[0]:
            return found[1](None,None,None)
        else:
            return await found[1](None, None, None)