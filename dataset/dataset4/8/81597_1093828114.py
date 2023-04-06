import _thread
import time
import importlib
barrier = 0

def method():
    import threading  # Will make threading the wrong thread.
    global barrier
    print(threading.main_thread())
    print(threading.current_thread())
    barrier = 1

_thread.start_new_thread(method, ())

while barrier != 1:
    time.sleep(.1)

import threading
importlib.reload(threading)
print(threading.main_thread())
print(threading.current_thread())