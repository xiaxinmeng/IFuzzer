#-- module.py
import logging
import threading
import random
import time

class MyThread(threading.Thread):
    def run(self):
        loops = 5
        while True:
            logging.getLogger("module").debug("Running in thread: %s",
                               threading.currentThread().getName())
            time.sleep(random.random())
            loops -= 1
            if loops < 0:
                break

class MyOtherThread(threading.Thread):
    def run(self):
        loops = 5
        while True:
            logging.getLogger("module").debug("Running in thread: %s",
                               threading.currentThread().getName())
            time.sleep(random.random())
            loops -= 1
            if loops < 0:
                break

def start():
    t1 = MyThread(name="Thread One")
    t2 = MyOtherThread(name="Thread Two")
    t1.start()
    t2.start()
    return t1, t2
#-- module.py ends