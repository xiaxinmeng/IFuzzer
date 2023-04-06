import numpy as np
import multiprocessing
import _tkinter

def parallel_matmul(x):
    R = np.random.randn(3, 3)
    return np.matmul(R, x)

pool = multiprocessing.Pool(4)
results = pool.map(parallel_matmul, [np.random.randn(3, 5000) for i in range(2)])