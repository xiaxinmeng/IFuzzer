import gc
import socket
import sys
import threading
import time


class MyQueue(object):

    def __init__(self):
        self.event = threading.Event()
        self.i = 0

    def set_(self,):
        self.event.set()
        time.sleep(1)
        gc.collect()
        if self.i > 2:
            sys.exit()

    def wait(self, name):
        self.event.wait()
        print('waiting')
        self.event.clear()
        self.i += 1
        with open('log.txt', 'a') as fp:
            fp.write(str(self.i) + name)
            fp.write('\n')

    def start(self, daemon_, name):
        threading.Thread(
            target=loop_wrap(self.wait),
            args=(name, ),
            name="wait",
            daemon=daemon_
        ).start()
        
        threading.Thread(
            target=loop_wrap(self.set_),
            name="set",
            daemon=True
        ).start()


def loop_wrap(func):
    def wrapper(*args):
        while True:
            try:
                func(*args)
            except Exception:
                time.sleep(1)
    return wrapper


if __name__ == '__main__':
    queue1 = MyQueue()
    queue2 = MyQueue()
    queue1.start(True, 'queue1')
    queue2.start(True, 'queue2')
    # time.sleep(1)
    print('exit main')
