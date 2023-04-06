from multiprocessing.sharedctypes import RawArray
import ctypes

foo = RawArray(ctypes.c_double, 10*1024**3//8)  # Allocate 10GB array