import multiprocessing
manager = multiprocessing.Manager()
value = manager.Value('i', 0)
value.get_lock()