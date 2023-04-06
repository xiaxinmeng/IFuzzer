import contextlib
import multiprocessing


def worker(q):
    with contextlib.closing(q):
        q.put_nowait('hello')


def controller():
    q = multiprocessing.Queue()
    q.close()  # no more 'put's from this process
    p = multiprocessing.Process(target=worker, args=(q, ))
    p.start()
    assert q.get() == 'hello'
    p.join()
    assert p.exitcode == 0
    print('OK!')


if __name__ == '__main__':
    controller()