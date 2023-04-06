import logging
from multiprocessing.pool import Pool
from multiprocessing.util import log_to_stderr

def f(i):
    print(i)

log_to_stderr(logging.DEBUG)

pool = Pool(50)
pool.map(f, range(2))
pool.close()
pool.join()