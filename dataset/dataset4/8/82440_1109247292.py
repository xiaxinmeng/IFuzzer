class Sentinel:
    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return True

_sentinel = Sentinel()