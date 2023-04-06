from multiprocessing import Pool


def double(x):
    return 2 * x

def get_numbers():
    raise Exception("oops")
    yield 1
    yield 2