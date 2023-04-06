class BlockingPool(pool.Pool):
    def _setup_queues(self):
        pool.Pool._setup_queues(self)
        self._taskqueue = Queue(3)
        self._inqueue = Queue(3)
        self._quick_put = self._inqueue.put