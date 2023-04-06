import threading
import weakref
import gc


ei = threading.Event()
eo = threading.Event()


def gc_worker():
    ei.wait()
    gc.collect()
    eo.set()


def callback(o):
    ei.set()
    eo.wait()


class C:
    def __del__(self):
        pass


def main():
    t = threading.Thread(target=gc_worker)
    t.start()
    c = C()
    cref = weakref.ref(c, callback)
    del c
    t.join()


main()