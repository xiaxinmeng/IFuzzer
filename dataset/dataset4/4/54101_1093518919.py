from threading import Event
from time import time

e = Event()

before = time()
e.wait(0.1)
after = time()

print(after - before)