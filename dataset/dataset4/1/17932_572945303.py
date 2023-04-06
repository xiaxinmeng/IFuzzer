
from multiprocessing import Pool
from time import sleep

with Pool(processes=1) as pool:
    result = pool.apply_async(sleep, (10000,))
    result.successful()
