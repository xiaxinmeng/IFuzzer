
from multiprocessing import Process, Queue
import os
import signal
def f(q):
    for i in range(10000):
        q.put([42, None, 'hello'])
        print("Iteration ", i , " " , os.getpid())
if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join(1)
