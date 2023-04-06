import json

class F:
    counter = 0
    total = 0
    data = b""

    def __call__(self, o):
        self.counter += 1
        self.data = b"1" + self.data
        self.total += len(self.data)
        print(self.counter, len(self.data), self.total)
        return self.data