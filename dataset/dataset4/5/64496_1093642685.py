with _AcquireFutures(fs):
        finished = set(
                f for f in fs
                if f._state in [CANCELLED_AND_NOTIFIED, FINISHED])
        pending = set(fs) - finished
        waiter = _create_and_install_waiters(fs, _AS_COMPLETED)