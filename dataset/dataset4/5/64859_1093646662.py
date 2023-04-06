import multiprocessing, logging

objs = []

def newman(n=50):
    m = multiprocessing.Manager()
    print('created')
    for i in range(n):
        objs.append(m.Value('i',i))
    return m

def foo():
    pass

if __name__ == '__main__':
    ## Try uncommenting next line with Python 3.4
    # multiprocessing.set_start_method('spawn')
    multiprocessing.log_to_stderr(logging.DEBUG)
    print('#### first man')
    m1 = newman()
    print('#### starting foo')
    p = multiprocessing.Process(target=foo)
    p.start()
    p.join()