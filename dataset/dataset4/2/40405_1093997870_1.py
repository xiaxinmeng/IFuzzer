import sys

class teeIO:
    def __init__(self, *files):
        self.__files = files

    def write(self, str):
        for i in self.__files:
            print >> trace, 'writing on %s: %s' % (i, str)
            i.write(str)