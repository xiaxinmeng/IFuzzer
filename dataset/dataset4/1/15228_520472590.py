
with _shutdown_locks_lock:
    _shutdown_locks.discard(tstate_lock)
