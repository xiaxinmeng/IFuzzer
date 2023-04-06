waiter = _allocate_lock()
waiter.acquire()
self._waiters.add(waiter)
self._release_save()
try:
    return waiter.acquire(timeout)
finally:
    self._acquire_restore()
    self._waiters.discard(waiter)