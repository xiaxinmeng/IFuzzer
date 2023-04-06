
class Fifo(SimpleQueue):

    def __iter__(self):
        return self

    def __next__(self):
        if not self.empty():
            return self.get()
        raise StopIteration
