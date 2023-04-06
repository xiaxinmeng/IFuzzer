import numpy as np
import sharedmem
import _tkinter

def parallel_matmul(x):
    R = np.random.randn(3, 3)
    return np.matmul(R, x)

with sharedmem.MapReduce() as pool:
    results = pool.map(parallel_matmul,
        [np.random.randn(3, 5000) for i in range(2)])