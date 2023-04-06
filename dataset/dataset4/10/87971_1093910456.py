import os
import signal
import multiprocessing

def child_func(qa, qb):
    input = qa.get()
    print('Child received: ', input)
    os.kill(os.getpid(), signal.SIGTERM)
    qb.put('B')
    exit(0)

qa = multiprocessing.Queue()
qb = multiprocessing.Queue()
process = multiprocessing.Process(target=child_func, args=(qa, qb))
process.start()

qa.put('A')
try:
    input = qb.get()
    print('Parent received: ', input)
except Exception as ex:
    print(ex)
process.join()
exit(0)