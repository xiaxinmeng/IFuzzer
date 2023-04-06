results = []
pool = Pool(processes=4)
for i in xrange(4):
    results.append(pool.apply_async(f, [10]))