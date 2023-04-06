
def __next__(self):
    with self.lock:
        self.i += 1
        return self.i
