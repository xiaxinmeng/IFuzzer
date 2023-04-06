def __init__(self):
  ...
  self._pending_free = queue.Queue()

def _exec_pending_free(self):
  while True:
    try:
      block = self._pending_free.get_nowait()
    except queue.Empty:
      break
    self._free(block)

def free(self, block):
  if self._lock.acquire(False):
     self._exec_pending_free()
     self._free(block)
  else:
     # malloc holds the lock
     self._pending_free.append(block)

def malloc():
  with self._lock:
    self._malloc()
    self._exec_pending_free()