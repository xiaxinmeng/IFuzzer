import time

def foo():
    import pdb; pdb.set_trace()
    while 1:
        time.sleep(.5)

foo()