import gc
tuple(gc.collect() for i in range(11))