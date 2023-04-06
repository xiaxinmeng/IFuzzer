
import time
t = time.time()

def call():
    a = 1
    b = 1
    c = 1
    d = 1
    e = 1
    f = 1

def noop(frame, event, arg):
    return noop

import sys
sys.settrace(noop)

for i in range(1_000_000):
    call()

print('%.2fs' % (time.time() - t,))
