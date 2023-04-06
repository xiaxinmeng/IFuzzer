_NOT_SET = object()


class RecvChannel:
    ...

    def recv_nowait(self, default=_NOT_SET):
        """
        Like recv(), but return the default
        instead of waiting.
        """
        if default is _NOT_SET:
            return _interpreters.channel_recv(self._id)
        else:
            return _interpreters.channel_recv(self._id, default)