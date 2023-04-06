import multiprocessing
lck1=multiprocessing.Lock()

with lck1:
    print("foo")
