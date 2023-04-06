from multiprocessing.pool import ThreadPool

def f(x):
    from threading import current_thread
    print(current_thread().name)
    return x*x

if __name__ == '__main__':
    with ThreadPool(5) as p:
        print(p.map(f, [1, 2, 3]))