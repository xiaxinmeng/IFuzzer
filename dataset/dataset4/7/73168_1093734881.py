from multiprocessing import Queue
q = Queue()
q.put('foo')
q.get(True, 0)  # raises Empty