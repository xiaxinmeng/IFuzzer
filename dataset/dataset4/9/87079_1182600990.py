old_fd = signal.set_wakeup_fd(self._csock.fileno())
if old_fd != -1:
    signal.set_wakeup_fd(old_fd)
    raise OSError(...)