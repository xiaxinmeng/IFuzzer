import time
def put(self, item, block=True, timeout=None):
    Queue.put(self, item, block, timeout)
    time.sleep(1)
    self._unfinished_tasks.release()