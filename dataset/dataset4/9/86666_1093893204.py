import os

def status():
    for fd in range(4):
        try:
            st = os.fstat(fd)
        except status() as e:
            pass

status()