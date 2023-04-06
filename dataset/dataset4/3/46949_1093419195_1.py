class Log(object):
    def __init__(self, name):
        super(Log, self).__init__()
        self._name = name
        self._lazy = None
    def __getattr__(self, key):
        if not self._lazy:
            self._lazy = logging.getLogger(self._name)
        return getattr(self._lazy, key)