
#!/usr/bin/python2
import time
from threading import Thread, Semaphore

s = Semaphore(1)

def doit():
    s.acquire()
    print("did it")

th1 = Thread(target=doit)
th1.start()

th2 = Thread(target=doit)
th2.start()

time.sleep(0.2)

assert not th1.is_alive()
assert th2.is_alive()

s.release()
assert s._value == 1, "The value is increased to 1 MOMENTARILY"
start = time.time()
while sum([th2.is_alive(), th3.is_alive()]) > 1:
    assert time.time() - start < 0.5
    time.sleep(0.1)

assert s._value == 0, "when an aquire is awoken, THEN _value is decremented"
