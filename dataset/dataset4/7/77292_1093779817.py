
import _tkinter
import numpy as np
# multiprocessing.set_start_method("spawn")
import multiprocessing

def parallel_matmul(x):
    R = np.random.randn(3, 3)
    return np.matmul(R, x)

if __name__ == '__main__':
    pool = multiprocessing.Pool(4)
    results = pool.map(parallel_matmul, [np.random.randn(3, 5000) for i in range(2)])
