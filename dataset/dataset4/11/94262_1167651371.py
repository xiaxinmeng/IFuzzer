import gc
gc.set_threshold(1, 0, 0)

class Sneaky:
    def __del__(self):
        raise KeyboardInterrupt


def gen():
    yield 1

sneaky = Sneaky()
sneaky._s = Sneaky()
sneaky._s._s = sneaky
del sneaky

g = gen()