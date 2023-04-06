class SomethingElse(object):
    def __init__(self):
        self._instance = None

    @property
    def instance(self):
        if not self._instance:
            self._instance = 'object'