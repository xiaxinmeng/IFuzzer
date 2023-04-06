class classattribute:
    def __init__(self, value):
        self.value = value
    def __get__(self, *args):
        return self.value
    def __set__(self, value):
        self.value = value
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.value)