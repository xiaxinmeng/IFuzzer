def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    nexts = deque(iter(it).__next__ for it in iterables)
    popleft = nexts.popleft
    append = nexts.append
    while nexts:
        next = popleft()
        try:
            yield next()
        except StopIteration:
            pass
        else:
            append(next)