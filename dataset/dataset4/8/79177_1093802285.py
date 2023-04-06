from multiprocessing.pool import ThreadPool

def f(x):
    from threading import current_thread
    print(current_thread().name)
    return x*x

if __name__ == '__main__':
    p1 = ThreadPool(5, name="process-1")
    p1.map_async(f, [1, 2, 3])
    p1.close()

    p2 = ThreadPool(5, name="process-2")
    p2.map_async(f, [1, 2, 3])
    p2.close()

    p1.join()
    p2.join()