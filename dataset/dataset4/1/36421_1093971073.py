import inspect

def leak():
    frame = inspect.currentframe()

while 1:
    leak()