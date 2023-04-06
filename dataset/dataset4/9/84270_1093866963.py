import os, _thread, threading, time

def fork_in_thread():
    pid = os.fork()
    if pid:
        # parent
        os._exit(0)