import multiprocessing
import time

def the_test():
    start_time = time.monotonic()
    pool = multiprocessing.Pool(1)
    res = pool.apply_async(int, ("1",))
    pool.close()
    #pool.terminate()
    pool.join()
    dt = time.monotonic() - start_time
    print("%.3f sec" % dt)

the_test()