class cm(object):
    def __init__(self, o):
        self.o = o
    def __get__(self, obj, type=None):
        return self.o.__get__(obj, type)