
import pickle

class Descr:
    __get__ = pickle.dump
    __set__ = None

class M(type):
    def __int__(self):
        self.write = None
        return 0

class X(type, metaclass=M):
    write = Descr()

class Y(metaclass=X):
    pass

Y.write
