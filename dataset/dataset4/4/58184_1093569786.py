import threading
import pprint


class A:
    def __init__(self, **kw):
        pprint.pprint("a")
        super(A, self).__init__()


class B(threading.local, A):
    def __init__(self, **kw):
        pprint.pprint("b")
        super(B, self).__init__()

if __name__ == "__main__":
    B()