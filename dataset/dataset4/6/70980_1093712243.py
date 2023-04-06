import os
import sys
import threading
import ctypes
import time

def test():
    while True:
        print(time.time())

_thread = threading.Thread(target=test)

pid = os.fork()
if pid > 0:
    sys.exit(0)

_thread.start()