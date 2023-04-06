from _pydecimal import *
from time import sleep
from random import randint
import sys


sys.setswitchinterval(0.0000001)


def usleep(x):
    sleep(x/1000000.0)

class Test:

    def __init__(self, threadno):
        self.threadno = threadno

    def GetCallback(self):
        usleep(randint(0, 9));
        setcontext(Context(Emax=self.threadno))
        usleep(randint(0, 9))
        c = getcontext()
        try:
            if c.Emax != self.threadno:
                raise RuntimeError("GetCallback: another thread changed this thread's context")
        except AttributeError:
            raise RuntimeError("GetCallback: type(c)==%s and c.Emax disappeared" % type(c))
        usleep(randint(0, 9))
        return self.Callback

    def Callback(self):
        c = getcontext()
        try:
            c.Emax = self.threadno
        except AttributeError:
            raise RuntimeError("Callback: type(c)==%s and c.Emax disappeared" % type(c))

def DoTest(threadno):
    return Test(threadno).GetCallback()