import _thread
import threading
import sys

done = False
def hook(*args):
    global done
    print(threading.current_thread())
    done = True
sys.excepthook = hook

def worker():
    raise Exception
_thread.start_new_thread(worker, tuple())
while not done:
    pass