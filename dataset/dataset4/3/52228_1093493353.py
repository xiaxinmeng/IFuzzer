import time
import thread

def f():
    for m in xrange(1, 13):
        for d in xrange(1,29):
            time.strptime("2010%02d%02d"%(m,d),"%Y%m%d")

for _ in xrange(10):
    thread.start_new_thread(f, ())
time.sleep(3)