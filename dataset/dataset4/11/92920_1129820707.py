import os
import threading


def run(cls, s):
    print(os.getpid())
    print(cls.__dict__)
    print(cls, s)


class A:
    a = 2

    def __str__(self):
        return self.__class__.__name__


b = type("B", (A,), {})
e = b()


class C(A): pass


if __name__ == '__main__':

    threading.Thread(target=run, args=(A, "111",)).start()
    threading.Thread(target=run, args=(b, "222",)).start()
    threading.Thread(target=run, args=(C, "333",)).start()
    threading.Thread(target=run, args=(e, "444",)).start()
    while 1:
        pass