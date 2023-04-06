import sys
import thread
import time
import signal

fsema = thread.allocate_lock()

def tfunc():
    time.sleep(.1)
    fsema.release()

fsema.acquire()
thread.start_new_thread(tfunc,())
fsema.acquire()
fsema.release()

signal.alarm(3)
signal.pause()