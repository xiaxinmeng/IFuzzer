class LossyQueue(Queue):
    "Queue subclass which drops items on overflow"
    def _init(self, maxsize):
        if maxsize > 0:
            # build the deque with maxsize limit
            self.queue = deque(maxlen=maxsize)
        else:
            # same as normal Queue instance
            self.queue = collections.deque()
        # deque alone handles maxsize,
        # so we pretend we have none
        self.maxsize = 0