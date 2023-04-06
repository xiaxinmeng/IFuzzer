class IterOrNotIter:
    def __init__(self):
        self.f = open('/tmp/toto.txt')
    def __getattr__(self, item):
        try:
            return self.__getattribute__(item)
        except AttributeError:
            return self.f.__getattribute__(item)