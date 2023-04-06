from multiprocessing import Pool

def task(arg):
    return arg

def main():
    pool = Pool()
    res = pool.apply_async(task, (3.14,))