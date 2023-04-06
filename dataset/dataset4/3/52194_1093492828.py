import threading
import time

def foo(n):
    while n > 0:
        'y' in 'x' * n
        n -= 1

def bar(sleep, name):
    for i in range(100):
        print (name, i, sleep)
        for j in range(300):
            foo(1500)
            if sleep:
                time.sleep(0)

t0 = threading.Thread(target=bar, args=(False, 't0'))
t1 = threading.Thread(target=bar, args=(False, 't1'))
t2 = threading.Thread(target=bar, args=(True, 't2-interactive'))

list(map(threading.Thread.start, [t0, t1, t2]))
list(map(threading.Thread.join, [t0, t1, t2]))