
class Condition:
    def __init__(self, lock=None):
        (...)
        self._lock = lock
        # Export the lock's acquire() and release() methods
        self.acquire = lock.acquire
        self.release = lock.release
        (...)
