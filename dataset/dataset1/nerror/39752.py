import multiprocessing
import os
with multiprocessing.Pool(1) as pool:
    result = pool.map_async(os._exit, [1]).get(timeout=2)
