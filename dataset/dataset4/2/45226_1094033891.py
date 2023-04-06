def roundrobin(*iterables):
    pending = deque(iter(i).next for i in reversed(iterables))
    rotate, pop, _StopIteration = pending.rotate, pending.pop, StopIteration
    while pending:
        try:
            while 1:
                yield pending[-1]()
                rotate()
        except _StopIteration:
            pop()