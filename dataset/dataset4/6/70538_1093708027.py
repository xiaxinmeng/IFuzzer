import os, signal

def foo(*args):
    print("foo")  # this never gets printed on Windows

signal.signal(signal.SIGTERM, foo)
os.kill(os.getpid(), signal.SIGTERM)