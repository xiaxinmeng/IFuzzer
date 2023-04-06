handle = self._ready.popleft()
if handle._cancelled:
    continue
if self._debug:
    ...
    handle._run()
    ...
else:
    handle._run()