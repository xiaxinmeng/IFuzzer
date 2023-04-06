def partition(iterable, part_len):
    itr = iter(iterable)
    while 1:
        item = tuple(islice(itr, part_len))
        if len(item) < part_len:
            raise StopIteration
        yield item