class MyBase(object):

    __slots__ = '__fakedict__'

    def __getstate__(self):
        return self.__fakedict__

    def __setstate__(self,state):
        self.__fakedict__ = state