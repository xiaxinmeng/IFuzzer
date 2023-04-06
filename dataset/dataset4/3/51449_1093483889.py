import multiprocessing
import queue

def _process_worker(q):
    while True:
        try:
            something = q.get(block=True, timeout=0.1)
        except queue.Empty:
            return
        else:
            pass
            # print('Grabbed item from queue:', something)


def _make_some_processes(q):
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=_process_worker, args=(q,))
        p.start()
        processes.append(p)
    return processes

#p = []
def _do(i):
    print('Run:', i)
    q = multiprocessing.Queue()
#    p.append(q)
    print('Created queue')
    for j in range(30):
        q.put(i*30+j)
    processes = _make_some_processes(q)
    print('Created processes')

    while not q.empty():
        pass
    print('Q is empty')

for i in range(100):
    _do(i)