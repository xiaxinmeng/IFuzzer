from ctypes import cdll
import multiprocessing as mp
import os

def foo():
    handle = cdll.LoadLibrary("./test.so")
    handle.IncA()

if __name__ == '__main__':
    foo()
    #p = mp.Process(target = foo, args = ())
    #p.start()
    #print(p.pid)
    #p.join()

    pid = os.fork()
    if pid == 0:
        foo()
    else:
        os.waitpid(pid, 0)