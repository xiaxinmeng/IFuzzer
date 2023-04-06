import weakref
import gc


def callback(o):
    gc.collect()


class C:
    def __del__(self):
        pass

def main():
    c = C()
    cref = weakref.ref(c, callback)
    del c


main()