import heapq

class foo:
    def __init__(self):
        self.timeout = 0
    def __le__(self, other):
        return self.timeout <= other.timeout

heap = []
heapq.heappush(heap, foo())
heapq.heappush(heap, foo())