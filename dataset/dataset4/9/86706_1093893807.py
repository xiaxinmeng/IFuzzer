import os

def daemon():
    pid = os.fork()
    if pid != 0:
        os._exit(0)

daemon()