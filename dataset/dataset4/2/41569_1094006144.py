from itertools import islice
def partition(iterable, part_len):
    itr = iter(iterable)
    while 1:
        yield tuple(islice(itr, part_len))