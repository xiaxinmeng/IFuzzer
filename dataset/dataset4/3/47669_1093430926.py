from multiprocessing import Process, Manager
sleeping = Manager().Semaphore(0)

def f():
    sleeping.release()

for _ in xrange(10):
    Process(target=f).start()
for _ in xrange(10):
    sleeping.acquire()