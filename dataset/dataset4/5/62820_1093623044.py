pool = Pool(processes=4)              # start 4 worker processes
result = pool.apply_async(f, [10])