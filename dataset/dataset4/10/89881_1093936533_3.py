def _serialize(func):
    """Decorator to serialize a non-reentrant signal function.
    If one client is already in the critical section, set a flag to run the
    section one more time. Testing purposes only.
    """

    lock = threading.Lock()  # Used as atomic test-and-set.
    retry = False

    @functools.wraps(func)
    def _decorator(*args, **kwargs):
        nonlocal retry

        while True:
            if lock.acquire(blocking=False):  # pylint: disable=consider-using-with
                try:
                    retry = False
                    func(*args, **kwargs)
                finally:
                    lock.release()
                if retry:
                    continue
            else:
                # A signal handler that interrupts an existing handler will
                # run to completion (LIFO).
                retry = True
            break

    return _decorator