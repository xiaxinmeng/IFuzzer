a = Counter(...)  # e.g 1M elements
b = Counter(...)  # e.g. 10 elements
# or just b = {...} or b = some_iterable_of_values_to_count since update works just
# fine with plain dicts and iterables to count, and making a second Counter is
# unnecessary overhead

a.update(b)