from multiprocessing.sharedctypes import RawArray
from ctypes import c_uint32
if __name__ == '__main__':
    shared_array = RawArray(c_uint32, 1500)