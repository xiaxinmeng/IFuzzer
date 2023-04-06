import sys

class sl(object):
        def __getslice__(self, a, b):
                return (a, b)