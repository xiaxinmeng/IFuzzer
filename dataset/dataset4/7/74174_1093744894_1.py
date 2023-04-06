reached_crashpad = False
lock = threading.Lock()
i = 0
while not reached_crashpad:
    i += 1
    try:
        sigint_timebomb(i)
        with lock:
            1 + 1
        # this loop keeps executing instructions until any still-armed
        # timebombs go off
        while True:
            reached_crashpad = True
    except KeyboardInterrupt:
        # key invariant: signal can't leave the lock held
        assert not lock.locked()
    else:
        assert False  # can't happen