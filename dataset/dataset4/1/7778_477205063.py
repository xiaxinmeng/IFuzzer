import signal
import os
import sys
import time

import multiprocessing

def fail():
    def handler(*args):
        pass

    while True:
        signal.signal(signal.SIGUSR1, signal.SIG_IGN)
        signal.signal(signal.SIGUSR1, handler)

proc = multiprocessing.Process(target=fail)
proc.start()
time.sleep(1)
pid = proc.pid

i = 0
try:
    while proc.is_alive():
        os.kill(pid, signal.SIGUSR1)
        time.sleep(0.001)
finally:
    proc.join()