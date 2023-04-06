import multiprocessing as mp
import threading       as mt
import signal
import time
import os

# from uuid.py line 400
import ctypes, ctypes.util
lib = ctypes.CDLL(ctypes.util.find_library('uuid'))

def sigusr2_handler(signum, frame):
    raise RuntimeError('caught sigusr2')
signal.signal(signal.SIGUSR2, sigusr2_handler)

def sub(pid):
    time.sleep(1)
    os.kill(pid, signal.SIGUSR2)