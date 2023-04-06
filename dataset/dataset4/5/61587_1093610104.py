for i in range(n):
    try:
        waiter = self._waiters.pop()
    except KeyError:
        break
    waiter.release()