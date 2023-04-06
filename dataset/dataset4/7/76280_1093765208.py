def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # This recipe is also called other names like "alternate", "interleave", or
    # "merge". "zip_flat" would also be an accurate name.
    # Algorithm: cycle around the __next__ methods of each iterable. when an
    # iter runs out, remove its __next__ from the cycle.
    nexts = cycle(iter(it).__next__ for it in iterables)
    for reduced_len in reversed(range(len(iterables))):
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            nexts = cycle(islice(nexts, reduced_len))
            # This skips one round of the cycle, starting the next round
            # without the current iter