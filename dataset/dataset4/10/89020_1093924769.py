import gc

class Leak:
    def __init__(self):
        self.fn = self.x

    def x(self):
        pass


gc.set_debug(gc.DEBUG_SAVEALL)

l = Leak()
del l
gc.collect()

for item in gc.garbage:
    print(item)