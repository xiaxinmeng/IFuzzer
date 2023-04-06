def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    collections.deque(islice(iterator, n), maxlen=0)