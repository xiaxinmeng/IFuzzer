from multiprocessing import get_context, Queue


def parent():
    ctx = get_context("spawn")
    r_q = Queue() # this segfaults
    # r_q = ctx.Queue() - this doesn't
    print("Parent r_q: %r, %r, %r" % (r_q._rlock, r_q._wlock, r_q._sem), flush=True)
    proc = ctx.Process(target=child, args=(r_q,))
    proc.start()
    # r_q.put("Hello", timeout=3)
    proc.join()
    print(proc.exitcode)


def child(r_q):
    print("Child r_q: %r, %r, %r" % (r_q._rlock, r_q._wlock, r_q._sem), flush=True)


if __name__ == '__main__':
    parent()
