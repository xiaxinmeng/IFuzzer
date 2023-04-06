import multiprocessing, time
pool = multiprocessing.Pool(1)
result = pool.apply_async(time.sleep, (1.0,))
pool.terminate()
result.get()