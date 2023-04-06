import sys, time
from ctypes import *

ThreadProc = WINFUNCTYPE(c_uint32, c_void_p)

@ThreadProc
def thread_proc(_):
    import threading
    print(threading.current_thread() is threading.main_thread())
    return 0