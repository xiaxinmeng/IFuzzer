tp = ThreadPool(5)
xs = tp.map(lambda x: 'a' * int(10e6), range(100))
# now using 1GB mem = 100 * 10MB strs
del xs
gc.collect()
# still using 1GB mem
tp.close(); tp.join()
# now using ~0GB mem