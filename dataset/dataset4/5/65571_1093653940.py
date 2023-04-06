import multiprocessing.util


def hook(*args):
    print (args)


def func():
    print ('func')


if __name__ == '__main__':
    multiprocessing.util.register_after_fork(hook, hook)
    p = multiprocessing.Process(target=func)
    p.start()