
class Strange(object):
    def __init__(self):
        self.i = 0

    def __iter__(self):
        self.i +=2
        for i in range(self.i, self.i + 2):
            yield i
