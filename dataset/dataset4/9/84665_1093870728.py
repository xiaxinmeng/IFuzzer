class Event:
    _ONE = (1).to_bytes(8, byteorder=sys.byteorder)

    def __init__(self):
        self._event_fd = os.eventfd(0, os.EFD_NONBLOCK)
        self._selector = selectors.DefaultSelector()
        self._selector.register(self._event_fd, selectors.EVENT_READ)

    def is_set(self):
        return self.wait(timeout=0)

    def set(self):
        try:
            os.write(self._event_fd, self._ONE)
        except BlockingIOError:
            pass

    def clear(self):
        try:
            os.read(self._event_fd, 8)
        except BlockingIOError:
            pass

    def wait(self, timeout=None):
        return bool(self._selector.select(timeout=timeout))

    def fileno(self):
        return self._event_fd