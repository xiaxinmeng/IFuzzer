#!/usr/bin/env python

from multiprocessing import Process
from threading import Thread
from time import sleep

def proc():
    mythread = Thread(target=run)
    mythread.start()
    print('Thread.daemon = %s' % mythread.daemon)
    sleep(4)
    #mythread.join()

def run():
    for i in range(10):
        sleep(0.1)
        print('Tick: %s' % i)

if __name__ == '__main__':
    p = Process(target=proc)
    p.start()
    print('Process.daemon = %s' % p.daemon)
