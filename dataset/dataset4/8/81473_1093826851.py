import os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context

class C:
    def __getstate__(self):
        print("pickled in %d" % os.getpid())
        return {}

    def __setstate__(self, state):
        print("unpickled in %d" % os.getpid())

    def hello(self):
        print("Hello world")


if __name__ == "__main__":
    with ProcessPoolExecutor(mp_context=get_context("spawn")) as ex:
        ex.submit(C().hello).result()