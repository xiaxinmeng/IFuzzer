import os
import sys
import time
import threading


import ctypes
libgcc_s = ctypes.CDLL("libgcc_s.so.1")

class Thread(threading.Thread):
    daemon = True
    def __init__(self, fh):
        super(Thread, self).__init__()
        self.fh = fh
    def run(self):
        try:
            old_stdout = sys.stdout
            sys.stdout = os.fdopen(self.fh.fileno(), 'w')
            time.sleep(0.1)
        finally:
            sys.stdout.close()
            sys.stdout = old_stdout

def main():
    fh = open('a.txt', 'w+')
    t = Thread(fh)
    t.start()
    t.join()
    del fh

if __name__ == '__main__':
    main()
