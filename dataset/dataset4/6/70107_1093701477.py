self.sock.setblocking(False)
try:
    ...  # Get chunks of request body to send
    while datablock:
        select((self._reader,), (self.sock,), (), self._timeout)
        if self._reader.peek():
            ...  # Early response received
        try:
            amount = self.sock.send(datablock)
        except (BlockingIOError, SSLWantRead, SSLWantWrite):
            continue
        datablock = datablock[amount:]
finally:
    self.sock.settimeout(self.timeout)