# Pseudocode
class MyExecutor(ThreadPoolExecutor):
  def __init__(self):
    self._count = 0

  def _decrement(self):
    with self._some_lock:
      self._count -= 1

  def submit(self, fn, *args, **kwargs):
    f = super(self).submit(fn, *args, **kwargs)
    with self._some_lock:
      self._count += 1
    f.add_done_callback(self._decrement)

  @property
  def num_pending_futures(self):
    return self._count