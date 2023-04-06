from timeit import timeit
timeit('sharedctypes.Array(ctypes.c_float, 500*2048*2048)', 'from multiprocessing import sharedctypes; import ctypes', number=1)