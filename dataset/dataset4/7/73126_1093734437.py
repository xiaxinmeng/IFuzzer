# START
import sys

class CustomIter:
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration
    def __length_hint__(self):
        return sys.maxsize

l = list(CustomIter())
#END