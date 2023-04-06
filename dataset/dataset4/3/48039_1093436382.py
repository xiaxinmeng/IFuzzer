def f(datasize, q):
    q.cancel_join_thread()
    q.put(range(datasize))