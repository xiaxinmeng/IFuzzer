
import bisect
from collections import defaultdict


class Test:
    def __init__(self, value):
        self.value = value


cache = defaultdict(int)

def key(e):
    cache[e] += 1
    assert cache[e] <= 1
    return e.value


l = [Test(i) for i in range(10000)]

bisect.bisect(l, Test(25), key=key)
