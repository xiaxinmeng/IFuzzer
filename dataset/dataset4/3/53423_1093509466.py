def _checkClosed(self):
    io.RawIOBase._checkClosed(self)
    if self._sslobj is None:
        raise ValueError("I/O operation on closed SSL socket")