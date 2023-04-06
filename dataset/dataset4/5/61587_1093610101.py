for i in range(n):
    try:
        waiter = __waiters.popleft()
    except IndexError:
        break
    waiter.release()