import threading, atexit

def foo():
    print(threading.currentThread())

atexit.register(foo)