from threading import Thread
import time

def writenums(f,n):
    start = time.time()
    for x in range(n):
        f.write("%d\n" % x)
    end = time.time()
    print(end-start)

def spin():
    while True:
        pass