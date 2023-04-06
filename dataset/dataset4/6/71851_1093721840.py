num_q = queue.Queue()
map(num_q.put, range(max_workers))