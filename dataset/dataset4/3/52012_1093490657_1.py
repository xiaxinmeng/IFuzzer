def consume(n, items):
    if n == 0:
        return
    next(islice(items, n-1, None), None)