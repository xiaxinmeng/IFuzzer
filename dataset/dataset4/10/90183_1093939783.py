import atexit
def func():
    atexit.unregister(func)
    1/0
atexit.register(func)