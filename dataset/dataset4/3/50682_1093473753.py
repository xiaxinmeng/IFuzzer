import multiprocessing
pool = multiprocessing.Pool()
pool.map(len, [], chunksize=1)
# hang forever