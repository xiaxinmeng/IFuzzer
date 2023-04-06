from operator import indexOf
from itertools import islice

def mode(data):
    counts = Counter(iter(data))
    if not counts:
        raise StatisticsError('no mode for empty data') from None
    maxcount = max(counts.values())
    index = indexOf(counts.values(), maxcount)
    return next(islice(counts, index, None))