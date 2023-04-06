
@functools.total_ordering
class KeyedItem:

    def __init__(self, key, item):
        self.key = key
        self.item = item

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key
