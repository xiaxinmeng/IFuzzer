class _SocketWriter(BufferedIOBase):
    """Simple writable BufferedIOBase implementation for a socket
    
    Does not hold data in a buffer, avoiding any need to call flush()."""
    def write(self, b):
        self._sock.sendall(b)
        return len(b)