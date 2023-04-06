from os import getpid
from time import sleep
from multiprocessing import Process

def f(sec):
    print("child %s: wait %s seconds" % (getpid(), sec))
    sleep(sec)

if __name__ == '__main__':
    print("parent %s: wait child" % (getpid(),))
    p = Process(target=f, args=(30,))
    p.start()
    p.join()