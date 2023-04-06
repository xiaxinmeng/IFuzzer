for f in fs:
    with f._condition:
        f._waiters.remove(waiter)