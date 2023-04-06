import os

class Obj(object):
    def __init__(self):
        self.f = open('/dev/null')
        os.close(self.f.fileno())

    def __del__(self):
        self.f.close()

f = Obj()
del f