import multiprocessing
def x(val):
   return val
multiprocessing.Pool().map(x, range(10))