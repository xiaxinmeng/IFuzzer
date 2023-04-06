from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import sleep

def worker():
    with ProcessPoolExecutor() as pool:
        r = list(pool.map(sleep, [0.01] * 8))


def submit(pool):
    pool.submit(submit, pool)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)
    pool.submit(submit, pool)

    i = 0
    while True:
        r = pool.submit(worker)
        r = r.result()
        print(i)
        i += 1