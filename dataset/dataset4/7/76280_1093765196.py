def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    nexts = cycle(iter(it).__next__ for it in iterables)
    for current_len in reversed(range(1, len(iterables)+1)):
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            nexts = cycle(islice(nexts, current_len - 1))