
def recv_nowait(self, default=None):
        """
        Like recv(), but return the default
        instead of waiting.
        """
        if default is None:
            default = _NOT_SET
        if default is _NOT_SET:
            return _interpreters.channel_recv(self._id)
        else:
            return _interpreters.channel_recv(self._id, default)
