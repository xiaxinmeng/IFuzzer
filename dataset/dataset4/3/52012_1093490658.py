def consume(items, n):
    next(islice(items, n, n), None)