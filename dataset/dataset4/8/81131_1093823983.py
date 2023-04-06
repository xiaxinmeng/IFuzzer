def run_until(loop, pred, timeout=30):
    deadline = time.monotonic() + timeout
    while not pred():
        if timeout is not None:
            timeout = deadline - time.monotonic()
            if timeout <= 0:
                raise futures.TimeoutError()
        loop.run_until_complete(tasks.sleep(0.001))