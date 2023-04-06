from heapq import merge
from collections import deque

class Int(int):
    compares = 0
    def __lt__(self, other):
        __class__.compares += 1
        return int(self) < int(other)

def comparisons(iterables):
    Int.compares = 0
    deque(merge(*iterables), maxlen=0)
    return Int.compares

no_overlap = comparisons(
    # (0..999), (1_000..1_999), (2_000..2_999), ...
    map(Int, range(x, x+1_000))
    for x in range(0, 16_000, 1_000)
)

interleaved = comparisons(
    # (0,16,32,...), (1,17,33,...), (2,18,34,...), ...
    map(Int, range(x, 16_000, 16))
    for x in range(16)
)

print(f"No overlap: {no_overlap:,} comparisons")
print(f"Interleaved: {interleaved:,} comparisons")