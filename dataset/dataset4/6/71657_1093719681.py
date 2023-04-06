
from __future__ import print_function

class test(object):
    def __nonzero__(self):
        return False

t = test()
if t:
    print('Hello')
