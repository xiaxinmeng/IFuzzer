class _WrappedIO(object):
    def __init__(self, fileobj):
        self._file = fileobj

    def __exit__(tp, val, tb):
        return True

    def __getattr__(self, name):
        return self._file.__gettattr__(name)