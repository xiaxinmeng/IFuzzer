class HighWaterQueue(Queue):

    def _init(self, maxsize):
        Queue.__init__(self, maxsize)
        self.highwater = 0

    def _put(self, item):
        Queue._put(self, item)
        self.highwater = max(self.highwater, self._qsize())