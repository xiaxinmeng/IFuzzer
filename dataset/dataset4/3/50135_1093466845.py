import sys, time, uuid

def uu(n):
    t = time.time()
    for x in range(n):
        uuid.uuid1()
    print('%.3f microseconds' % ((time.time() - t) * 1000000.0 / n))

uu(50000)