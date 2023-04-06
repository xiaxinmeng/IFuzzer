import sys
from multiprocessing import Pool

pool = Pool(2)
pool.apply(sys.exit, (0,))