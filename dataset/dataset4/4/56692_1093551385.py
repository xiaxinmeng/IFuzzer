import ctypes, gc
class Nasty:
    def __del__(self):
        gc.collect()